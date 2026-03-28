"""CLI entry point for the Instagram automation pipeline."""

import argparse
import json
import sys
from pathlib import Path

from pipeline.instagram.captions import generate_caption
from pipeline.instagram.config import ANTHROPIC_API_KEY, BUFFER_ACCESS_TOKEN
from pipeline.instagram.review import review_and_schedule
from pipeline.instagram.scheduler import enforce_alternation, get_next_post_slots
from pipeline.instagram.staging import (
    ensure_folders,
    export_from_photos,
    list_staged_images,
)

QUEUE_FILE = Path("post_queue.json")


def cmd_export(args):
    """Export images from Apple Photos album to staging."""
    ensure_folders()
    print(f"Exporting album '{args.album}' to staging folder...")
    output = export_from_photos(args.album)
    print(output)
    images = list_staged_images()
    print(f"\n{len(images)} image(s) in staging folder.")


def cmd_stage(args):
    """List images currently in the staging folder."""
    images = list_staged_images()
    if not images:
        print("No images in staging folder.")
        return
    print(f"{len(images)} image(s) staged:")
    for img in images:
        print(f"  {img.name}")


def cmd_generate(args):
    """Generate captions for all staged images."""
    if not ANTHROPIC_API_KEY:
        print("Error: ANTHROPIC_API_KEY not set in .env", file=sys.stderr)
        sys.exit(1)

    images = list_staged_images()
    if not images:
        print("No images in staging folder.")
        return

    posts = []
    slots = get_next_post_slots(len(images))

    print(f"Generating captions for {len(images)} image(s)...\n")

    for image_path, slot in zip(images, slots):
        print(f"  Processing {image_path.name}...")
        caption = generate_caption(image_path)
        posts.append(
            {
                "image_path": str(image_path),
                "caption": caption,
                "scheduled_at": slot.isoformat(),
            }
        )
        print(f"  Caption generated.\n")

    posts = enforce_alternation(posts)

    # Reassign slots after alternation reordering
    for post, slot in zip(posts, slots):
        post["scheduled_at"] = slot.isoformat()

    QUEUE_FILE.write_text(json.dumps(posts, indent=2))
    print(f"Queue saved to {QUEUE_FILE} with {len(posts)} post(s).")
    print("\nGenerated captions:")
    for post in posts:
        print(f"\n--- {Path(post['image_path']).name} ({post['scheduled_at']}) ---")
        print(post["caption"])


def cmd_review(args):
    """Review and schedule queued posts."""
    if not BUFFER_ACCESS_TOKEN:
        print("Error: BUFFER_ACCESS_TOKEN not set in .env", file=sys.stderr)
        sys.exit(1)

    if not QUEUE_FILE.exists():
        print("No queue file found. Run 'generate' first.")
        return

    posts = json.loads(QUEUE_FILE.read_text())
    if not posts:
        print("Queue is empty.")
        return

    print(f"Reviewing {len(posts)} post(s)...\n")
    review_and_schedule(posts)

    # Clear queue after review
    QUEUE_FILE.write_text("[]")


def cmd_run(args):
    """Run the full pipeline: generate captions then review."""
    cmd_generate(args)
    print("\n" + "=" * 60)
    print("Starting review...\n")
    cmd_review(args)


def main():
    parser = argparse.ArgumentParser(
        description="Instagram automation pipeline for robertreilly.art"
    )
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # export
    export_parser = subparsers.add_parser(
        "export", help="Export images from Apple Photos album"
    )
    export_parser.add_argument("album", help="Album name (e.g. 'Light Art')")
    export_parser.set_defaults(func=cmd_export)

    # stage
    stage_parser = subparsers.add_parser(
        "stage", help="List staged images"
    )
    stage_parser.set_defaults(func=cmd_stage)

    # generate
    gen_parser = subparsers.add_parser(
        "generate", help="Generate captions for staged images"
    )
    gen_parser.set_defaults(func=cmd_generate)

    # review
    review_parser = subparsers.add_parser(
        "review", help="Review and schedule queued posts"
    )
    review_parser.set_defaults(func=cmd_review)

    # run
    run_parser = subparsers.add_parser(
        "run", help="Full pipeline: generate + review"
    )
    run_parser.set_defaults(func=cmd_run)

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(1)

    args.func(args)


if __name__ == "__main__":
    main()
