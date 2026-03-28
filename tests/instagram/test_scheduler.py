"""Tests for the Instagram post scheduler."""

from datetime import datetime

import pytz

from pipeline.instagram.scheduler import (
    enforce_alternation,
    get_next_post_slots,
    is_italy_post,
)


def test_is_italy_post_with_florence():
    caption = "Florence from above.\n#doublexposure #compositephotography #florence #italy #surrealphotography"
    assert is_italy_post(caption) is True


def test_is_italy_post_with_venice():
    caption = "A canal in Venice.\n#doublexposure #compositephotography #venice #italy #surrealphotography"
    assert is_italy_post(caption) is True


def test_is_italy_post_non_italy():
    caption = "Brooklyn Bridge at night.\n#doublexposure #compositephotography #newyork #brooklynbridge #surrealphotography"
    assert is_italy_post(caption) is False


def test_get_next_post_slots_returns_correct_count():
    tz = pytz.timezone("US/Central")
    # Use a known Monday
    after = datetime(2026, 3, 30, 10, 0, 0, tzinfo=tz)
    slots = get_next_post_slots(4, after=after)
    assert len(slots) == 4


def test_get_next_post_slots_only_tuesday_friday():
    tz = pytz.timezone("US/Central")
    after = datetime(2026, 3, 30, 10, 0, 0, tzinfo=tz)
    slots = get_next_post_slots(4, after=after)
    for slot in slots:
        assert slot.strftime("%A") in ("Tuesday", "Friday")


def test_get_next_post_slots_are_at_9am():
    tz = pytz.timezone("US/Central")
    after = datetime(2026, 3, 30, 10, 0, 0, tzinfo=tz)
    slots = get_next_post_slots(2, after=after)
    for slot in slots:
        assert slot.hour == 9
        assert slot.minute == 0


def test_enforce_alternation_no_consecutive_italy():
    posts = [
        {"caption": "Florence.\n#florence #italy", "image_path": "a.jpg"},
        {"caption": "Venice.\n#venice #italy", "image_path": "b.jpg"},
        {"caption": "Brooklyn.\n#newyork #brooklynbridge", "image_path": "c.jpg"},
        {"caption": "Forest.\n#forest #architecture", "image_path": "d.jpg"},
    ]
    result = enforce_alternation(posts)

    for i in range(len(result) - 1):
        if is_italy_post(result[i]["caption"]):
            assert not is_italy_post(result[i + 1]["caption"]), (
                f"Consecutive Italy posts at index {i} and {i + 1}"
            )


def test_enforce_alternation_all_italy():
    posts = [
        {"caption": "Florence.\n#florence #italy", "image_path": "a.jpg"},
        {"caption": "Venice.\n#venice #italy", "image_path": "b.jpg"},
    ]
    result = enforce_alternation(posts)
    assert len(result) == 2


def test_enforce_alternation_preserves_all_posts():
    posts = [
        {"caption": "Florence.\n#florence #italy", "image_path": "a.jpg"},
        {"caption": "Brooklyn.\n#newyork", "image_path": "b.jpg"},
        {"caption": "Venice.\n#venice #italy", "image_path": "c.jpg"},
    ]
    result = enforce_alternation(posts)
    assert len(result) == len(posts)
    paths = {p["image_path"] for p in result}
    assert paths == {"a.jpg", "b.jpg", "c.jpg"}
