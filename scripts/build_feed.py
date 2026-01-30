import json
from pathlib import Path
from datetime import datetime

BASE_DIR = Path(__file__).resolve().parent.parent
TOS_DIR = BASE_DIR / "tos"
DATA_DIR = BASE_DIR / "data"
FEED_FILE = DATA_DIR / "feed.json"

DATA_DIR.mkdir(exist_ok=True)

items = []

for md_file in TOS_DIR.glob("*.md"):
    slug = md_file.stem

    items.append({
        "service": slug.capitalize(),
        "slug": slug,
        "date": datetime.utcnow().strftime("%Y-%m-%d"),
        "status": "yellow",
        "summary": ["Initial ToS snapshot created"],
        "diff_url": ""
    })

feed = {
    "updated_at": datetime.utcnow().isoformat(),
    "items": items
}

with open(FEED_FILE, "w", encoding="utf-8") as f:
    json.dump(feed, f, indent=2)

print(f"✅ Feed generated with {len(items)} items")
