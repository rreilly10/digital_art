# Instagram Automation Pipeline — Setup Status

## What's Done (on the remote branch)

All pipeline code is written, tested, and pushed to `claude/instagram-automation-pipeline-7F1g0`.

### Files created:
- `pipeline/instagram/config.py` — env vars, system prompt, scheduling constants
- `pipeline/instagram/staging.py` — osxphotos export + folder management (ToPost/Posted/Skipped)
- `pipeline/instagram/captions.py` — Claude API vision-based caption generation
- `pipeline/instagram/buffer_client.py` — Buffer API media upload + draft scheduling
- `pipeline/instagram/scheduler.py` — Tue/Fri 9am CST time slots, Italy/non-Italy alternation
- `pipeline/instagram/review.py` — CLI manual review (approve/edit/skip per post)
- `pipeline/instagram/cli.py` — main entry point with subcommands
- `.env.example` — template for API keys
- `tests/instagram/` — 16 tests (all passing)
- Updated `requirements.txt` with anthropic, python-dotenv, pytz
- Updated `.gitignore` to exclude post_queue.json

## What You Need To Do On Your Mac

### 1. Pull the branch
```bash
cd ~/path/to/digital_art
git fetch origin
git checkout claude/instagram-automation-pipeline-7F1g0
```

### 2. Install dependencies
```bash
pip install osxphotos anthropic requests python-dotenv pytz
```

### 3. Create your .env file
```bash
cp .env.example .env
```
Then edit `.env` and fill in:
- `ANTHROPIC_API_KEY` — from console.anthropic.com
- `BUFFER_ACCESS_TOKEN` — from Buffer developer settings
- `BUFFER_PROFILE_ID` — your Instagram profile ID in Buffer

### 4. Grant Terminal full disk access
System Preferences > Privacy & Security > Full Disk Access > add Terminal (or iTerm)

This is required for osxphotos to read your Apple Photos library.

### 5. Create the staging folders
```bash
mkdir -p ~/Desktop/ToPost ~/Desktop/Posted ~/Desktop/Skipped
```

### 6. Run the pipeline

Export images from a Photos album:
```bash
python -m pipeline.instagram.cli export "Light Art"
```

See what's staged:
```bash
python -m pipeline.instagram.cli stage
```

Generate captions for all staged images:
```bash
python -m pipeline.instagram.cli generate
```

Review and schedule (approve/edit/skip each post):
```bash
python -m pipeline.instagram.cli review
```

Or run generate + review together:
```bash
python -m pipeline.instagram.cli run
```

### 7. Verify tests pass locally
```bash
python -m pytest tests/instagram/ -v
```

## What Could Not Be Done Remotely

- osxphotos requires macOS and access to your Photos library
- Buffer API calls need real credentials to test end-to-end
- Caption generation needs a real ANTHROPIC_API_KEY and actual images
- The review CLI is interactive (approve/edit/skip) so it needs a terminal on your machine
