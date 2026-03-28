"""Tests for caption generation module."""

from pathlib import Path
from unittest.mock import MagicMock, patch

from pipeline.instagram.captions import _read_image_base64, generate_caption


def test_read_image_base64_jpeg(tmp_path):
    img = tmp_path / "test.jpg"
    img.write_bytes(b"\xff\xd8\xff\xe0test image data")

    data, media_type = _read_image_base64(img)

    assert media_type == "image/jpeg"
    assert isinstance(data, str)
    assert len(data) > 0


def test_read_image_base64_png(tmp_path):
    img = tmp_path / "test.png"
    img.write_bytes(b"\x89PNG\r\n\x1a\ntest")

    data, media_type = _read_image_base64(img)

    assert media_type == "image/png"


def test_generate_caption_calls_api(tmp_path):
    img = tmp_path / "test.jpg"
    img.write_bytes(b"\xff\xd8\xff\xe0fake image")

    mock_response = MagicMock()
    mock_response.content = [MagicMock(text="Test caption.\n#doublexposure #compositephotography #surrealphotography")]

    with patch("pipeline.instagram.captions.anthropic.Anthropic") as mock_client_cls:
        mock_client = MagicMock()
        mock_client.messages.create.return_value = mock_response
        mock_client_cls.return_value = mock_client

        caption = generate_caption(img)

    assert "Test caption" in caption
    mock_client.messages.create.assert_called_once()
    call_kwargs = mock_client.messages.create.call_args.kwargs
    assert call_kwargs["model"] == "claude-sonnet-4-20250514"
    assert "composite" in call_kwargs["system"].lower() or "double exposure" in call_kwargs["system"].lower()
