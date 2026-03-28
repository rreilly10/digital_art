"""Tests for staging folder management."""

from pathlib import Path
from unittest.mock import patch

from pipeline.instagram.staging import list_staged_images, move_to_posted, move_to_skipped


def test_list_staged_images_filters_extensions(tmp_path):
    with patch("pipeline.instagram.staging.STAGING_DIR", tmp_path):
        (tmp_path / "photo.jpg").touch()
        (tmp_path / "photo.png").touch()
        (tmp_path / "notes.txt").touch()
        (tmp_path / "data.csv").touch()

        images = list_staged_images()
        names = [img.name for img in images]

        assert "photo.jpg" in names
        assert "photo.png" in names
        assert "notes.txt" not in names
        assert "data.csv" not in names


def test_list_staged_images_empty(tmp_path):
    with patch("pipeline.instagram.staging.STAGING_DIR", tmp_path):
        images = list_staged_images()
        assert images == []


def test_move_to_posted(tmp_path):
    staging = tmp_path / "staging"
    posted = tmp_path / "posted"
    staging.mkdir()
    posted.mkdir()

    src = staging / "test.jpg"
    src.write_text("image data")

    with patch("pipeline.instagram.staging.POSTED_DIR", posted):
        dest = move_to_posted(src)

    assert dest == posted / "test.jpg"
    assert not src.exists()
    assert (posted / "test.jpg").exists()


def test_move_to_skipped(tmp_path):
    staging = tmp_path / "staging"
    skipped = tmp_path / "skipped"
    staging.mkdir()
    skipped.mkdir()

    src = staging / "test.jpg"
    src.write_text("image data")

    with patch("pipeline.instagram.staging.SKIPPED_DIR", skipped):
        dest = move_to_skipped(src)

    assert dest == skipped / "test.jpg"
    assert not src.exists()
    assert (skipped / "test.jpg").exists()
