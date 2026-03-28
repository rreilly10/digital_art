"""Manage image staging folders and osxphotos export."""

import shutil
import subprocess
from pathlib import Path

from pipeline.instagram.config import (
    IMAGE_EXTENSIONS,
    POSTED_DIR,
    SKIPPED_DIR,
    STAGING_DIR,
)


def ensure_folders():
    """Create staging, posted, and skipped folders if they don't exist."""
    for folder in [STAGING_DIR, POSTED_DIR, SKIPPED_DIR]:
        folder.mkdir(parents=True, exist_ok=True)


def export_from_photos(album_name: str, dest: Path | None = None):
    """Export images from an Apple Photos album using osxphotos.

    Args:
        album_name: Name of the album (supports nested like "Art/Light Art").
        dest: Destination folder. Defaults to STAGING_DIR.
    """
    dest = dest or STAGING_DIR
    ensure_folders()

    cmd = ["osxphotos", "export", str(dest), "--album", album_name]
    result = subprocess.run(cmd, capture_output=True, text=True)

    if result.returncode != 0:
        raise RuntimeError(
            f"osxphotos export failed: {result.stderr.strip()}"
        )

    return result.stdout.strip()


def list_staged_images() -> list[Path]:
    """Return sorted list of image files in the staging folder."""
    ensure_folders()
    images = [
        f
        for f in STAGING_DIR.iterdir()
        if f.is_file() and f.suffix.lower() in IMAGE_EXTENSIONS
    ]
    return sorted(images, key=lambda p: p.name)


def move_to_posted(image_path: Path):
    """Move an image from staging to posted folder."""
    ensure_folders()
    dest = POSTED_DIR / image_path.name
    shutil.move(str(image_path), str(dest))
    return dest


def move_to_skipped(image_path: Path):
    """Move an image from staging to skipped folder."""
    ensure_folders()
    dest = SKIPPED_DIR / image_path.name
    shutil.move(str(image_path), str(dest))
    return dest
