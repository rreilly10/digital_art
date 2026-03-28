import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY", "")
BUFFER_ACCESS_TOKEN = os.environ.get("BUFFER_ACCESS_TOKEN", "")
BUFFER_PROFILE_ID = os.environ.get("BUFFER_PROFILE_ID", "")

STAGING_DIR = Path(os.environ.get("STAGING_DIR", os.path.expanduser("~/Desktop/ToPost")))
POSTED_DIR = Path(os.environ.get("POSTED_DIR", os.path.expanduser("~/Desktop/Posted")))
SKIPPED_DIR = Path(os.environ.get("SKIPPED_DIR", os.path.expanduser("~/Desktop/Skipped")))

CAPTION_MODEL = "claude-sonnet-4-20250514"

POSTING_DAYS = ["Tuesday", "Friday"]
POSTING_HOUR = 9  # 9:00 AM CST
POSTING_TIMEZONE = "US/Central"
POSTS_PER_WEEK = 2

IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".heic", ".tiff"}

SYSTEM_PROMPT = """You write Instagram captions for a composite/double exposure photography account called robertreilly.art.

Style rules:
- Stoic, direct, no flourish
- Never use poetic language, metaphors, or anything try-hard
- Format: Location or subject. What was layered. One plain question at the end.
- Maximum 2-3 sentences total
- No emoji ever

Hashtag rules:
- Always include: #doublexposure #compositephotography #surrealphotography
- Add 2 location-specific tags relevant to the image
- Never more than 5 hashtags total
- No generic tags like #photography or #art
- Place hashtags on a new line after the caption

Output only the caption and hashtags. Nothing else."""

CAPTION_EXAMPLES = [
    "Brooklyn Bridge at night layered with a forest. Shot years apart. What do you see first?\n#doublexposure #compositephotography #newyork #brooklynbridge #surrealphotography",
    "Florence from above. Layered with a lake shot from the same trip. What do you see first?\n#doublexposure #compositephotography #florence #italy #surrealphotography",
    "The Arno with a dry riverbed underneath. Shot the same week. What do you notice?\n#doublexposure #compositephotography #florence #arno #surrealphotography",
    "A canal in Venice layered with succulents. What do you see first?\n#doublexposure #compositephotography #venice #italy #surrealphotography",
    "Trees layered with a steel structure. The geometry survived. What do you notice first?\n#doublexposure #compositephotography #forest #surrealphotography #architecture",
    "Florence and Venice. Different trips, different years. What do you see first?\n#doublexposure #compositephotography #florence #venice #surrealphotography",
]
