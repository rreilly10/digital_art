"""Buffer API client for scheduling Instagram posts."""

from pathlib import Path

import requests

from pipeline.instagram.config import BUFFER_ACCESS_TOKEN, BUFFER_PROFILE_ID

BUFFER_BASE_URL = "https://api.bufferapp.com/1"


def _headers() -> dict:
    return {"Authorization": f"Bearer {BUFFER_ACCESS_TOKEN}"}


def upload_media(image_path: Path) -> str:
    """Upload an image to Buffer and return the media link.

    Args:
        image_path: Path to the image file.

    Returns:
        The uploaded media thumbnail URL or photo link from Buffer.
    """
    url = f"{BUFFER_BASE_URL}/media/upload.json"

    with open(image_path, "rb") as f:
        response = requests.post(url, headers=_headers(), files={"file": f})

    response.raise_for_status()
    data = response.json()
    return data.get("thumbnail", data.get("photo", ""))


def schedule_post(
    image_path: Path, caption: str, scheduled_at: str
) -> dict:
    """Create a scheduled draft post on Buffer.

    Args:
        image_path: Path to the image file.
        caption: Post caption text with hashtags.
        scheduled_at: ISO 8601 timestamp for scheduling.

    Returns:
        Buffer API response as dict.
    """
    photo_url = upload_media(image_path)

    url = f"{BUFFER_BASE_URL}/updates/create.json"
    payload = {
        "profile_ids": [BUFFER_PROFILE_ID],
        "text": caption,
        "media": {"photo": photo_url},
        "scheduled_at": scheduled_at,
        "now": False,
    }

    response = requests.post(url, headers=_headers(), json=payload)
    response.raise_for_status()
    return response.json()
