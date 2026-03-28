"""CLI-based manual review interface for Instagram posts."""

import subprocess
import sys
import tempfile
from pathlib import Path

from pipeline.instagram.buffer_client import schedule_post
from pipeline.instagram.staging import move_to_posted, move_to_skipped


def _open_in_editor(text: str) -> str:
    """Open text in the user's preferred editor and return the edited result."""
    import os

    editor = os.environ.get("EDITOR", "nano")

    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".txt", delete=False
    ) as f:
        f.write(text)
        tmp_path = f.name

    subprocess.call([editor, tmp_path])

    with open(tmp_path, "r") as f:
        result = f.read()

    Path(tmp_path).unlink()
    return result.strip()


def _display_post(image_path: Path, caption: str, scheduled_date: str):
    """Display post details for review."""
    print("\n" + "=" * 60)
    print(f"  Image: {image_path.name}")
    print(f"  Scheduled: {scheduled_date}")
    print("-" * 60)
    print(f"\n{caption}\n")
    print("=" * 60)


def review_post(
    image_path: Path, caption: str, scheduled_at: str
) -> tuple[str, str | None]:
    """Present a post for manual review.

    Args:
        image_path: Path to the image.
        caption: Generated caption.
        scheduled_at: ISO 8601 scheduled time string.

    Returns:
        Tuple of (action, final_caption) where action is one of
        'approve', 'edit', 'skip' and final_caption is the caption
        to use (None if skipped).
    """
    _display_post(image_path, caption, scheduled_at)

    while True:
        print("  [a] Approve  |  [e] Edit caption  |  [s] Skip")
        choice = input("  > ").strip().lower()

        if choice == "a":
            return "approve", caption
        elif choice == "e":
            edited = _open_in_editor(caption)
            print("\nEdited caption:")
            print(edited)
            confirm = input("\nUse this caption? [y/n] > ").strip().lower()
            if confirm == "y":
                return "edit", edited
            # Loop back to show options again
        elif choice == "s":
            return "skip", None
        else:
            print("  Invalid choice. Enter a, e, or s.")


def review_and_schedule(posts: list[dict]):
    """Run the full review loop for a list of posts.

    Each post dict should have keys: image_path, caption, scheduled_at.

    Args:
        posts: List of post dicts to review and schedule.
    """
    approved = 0
    skipped = 0

    for i, post in enumerate(posts, 1):
        image_path = Path(post["image_path"])
        caption = post["caption"]
        scheduled_at = post["scheduled_at"]

        print(f"\n--- Post {i}/{len(posts)} ---")
        action, final_caption = review_post(image_path, caption, scheduled_at)

        if action in ("approve", "edit"):
            try:
                schedule_post(image_path, final_caption, scheduled_at)
                move_to_posted(image_path)
                print(f"  Scheduled for {scheduled_at}")
                approved += 1
            except Exception as e:
                print(f"  Error scheduling: {e}", file=sys.stderr)
        elif action == "skip":
            move_to_skipped(image_path)
            print("  Skipped.")
            skipped += 1

    print(f"\nDone. Approved: {approved}, Skipped: {skipped}")
