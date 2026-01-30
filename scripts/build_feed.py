import subprocess
import json
from pathlib import Path
from datetime import datetime

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
FEED_FILE = DATA_DIR / "feed.json"

DATA_DIR.mkdir(exist_ok=True)

# sprawdzamy które pliki się zmieniły
result = subprocess.run(
    ["git", "diff", "--name-only", "HEAD"],
    capture_output=True,
    text=True
)

changed_files = result.stdout.splitlines()

items = []

for file in changed_files:
    if file.startswith("tos/") and file.endswith(".md"):
        slug = Path(file).stem

        items.append({
            "service": slug.capitalize(),
            "slug": slug,
            "date": datetime.utcnow().strftime("%Y-%m-%d"),
            "status": "yellow",
            "summary": ["Terms of Service updated"],
            "diff_url": ""
        })

feed = {
    "updated_at": datetime.utcnow().isoformat(),
    "items": items
}

with open(FEED_FILE, "w", encoding="utf-8") as f:
    json.dump(feed, f, indent=2)

print(f"✅ Feed updated with {len(items)} changes")
