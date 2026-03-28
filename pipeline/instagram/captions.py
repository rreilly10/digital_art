"""Generate Instagram captions using the Claude API with vision."""

import base64
from pathlib import Path

import anthropic

from pipeline.instagram.config import (
    ANTHROPIC_API_KEY,
    CAPTION_MODEL,
    SYSTEM_PROMPT,
)


def _read_image_base64(image_path: Path) -> tuple[str, str]:
    """Read an image file and return (base64_data, media_type)."""
    suffix = image_path.suffix.lower()
    media_type_map = {
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".png": "image/png",
        ".gif": "image/gif",
        ".webp": "image/webp",
    }
    media_type = media_type_map.get(suffix, "image/jpeg")

    with open(image_path, "rb") as f:
        data = base64.standard_b64encode(f.read()).decode("utf-8")

    return data, media_type


def generate_caption(image_path: Path) -> str:
    """Generate an Instagram caption for the given image.

    Args:
        image_path: Path to the image file.

    Returns:
        Generated caption text with hashtags.
    """
    client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)

    image_data, media_type = _read_image_base64(image_path)

    message = client.messages.create(
        model=CAPTION_MODEL,
        max_tokens=1000,
        system=SYSTEM_PROMPT,
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "image",
                        "source": {
                            "type": "base64",
                            "media_type": media_type,
                            "data": image_data,
                        },
                    },
                    {
                        "type": "text",
                        "text": "Generate a caption for this composite photograph.",
                    },
                ],
            }
        ],
    )

    return message.content[0].text
