"""Scheduling logic for Instagram posts.

Rules:
- 2 posts per week: Tuesday and Friday at 9:00 AM CST
- Never post two Italy pieces back to back
- Alternate Italy / non-Italy where possible
"""

from datetime import datetime, timedelta

import pytz

from pipeline.instagram.config import POSTING_DAYS, POSTING_HOUR, POSTING_TIMEZONE

DAY_MAP = {
    "Monday": 0,
    "Tuesday": 1,
    "Wednesday": 2,
    "Thursday": 3,
    "Friday": 4,
    "Saturday": 5,
    "Sunday": 6,
}

ITALY_TAGS = {"#florence", "#venice", "#italy", "#arno"}


def is_italy_post(caption: str) -> bool:
    """Check if a caption contains Italy-related hashtags."""
    lower = caption.lower()
    return any(tag in lower for tag in ITALY_TAGS)


def get_next_post_slots(count: int, after: datetime | None = None) -> list[datetime]:
    """Generate the next `count` posting time slots.

    Args:
        count: Number of slots to generate.
        after: Start looking after this datetime. Defaults to now.

    Returns:
        List of timezone-aware datetimes in CST.
    """
    tz = pytz.timezone(POSTING_TIMEZONE)
    now = after or datetime.now(tz)

    target_days = sorted(DAY_MAP[d] for d in POSTING_DAYS)
    slots = []

    current = now.replace(hour=POSTING_HOUR, minute=0, second=0, microsecond=0)
    if current <= now:
        current += timedelta(days=1)

    while len(slots) < count:
        if current.weekday() in target_days:
            slots.append(current)
        current += timedelta(days=1)

    return slots


def enforce_alternation(posts: list[dict]) -> list[dict]:
    """Reorder posts to avoid consecutive Italy pieces.

    Each post dict must have a 'caption' key. Posts are reordered in-place
    to alternate Italy/non-Italy where possible.

    Args:
        posts: List of dicts with at least 'caption' and 'image_path' keys.

    Returns:
        Reordered list of posts.
    """
    italy = [p for p in posts if is_italy_post(p["caption"])]
    non_italy = [p for p in posts if not is_italy_post(p["caption"])]

    result = []
    last_was_italy = True  # Start with non-Italy preference

    while italy or non_italy:
        if last_was_italy and non_italy:
            result.append(non_italy.pop(0))
            last_was_italy = False
        elif not last_was_italy and italy:
            result.append(italy.pop(0))
            last_was_italy = True
        elif non_italy:
            result.append(non_italy.pop(0))
            last_was_italy = False
        else:
            result.append(italy.pop(0))
            last_was_italy = True

    return result
