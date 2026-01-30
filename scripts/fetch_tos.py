import json
import requests
import trafilatura
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SERVICES_FILE = BASE_DIR / "services.json"
TOS_DIR = BASE_DIR / "tos"

TOS_DIR.mkdir(exist_ok=True)

with open(SERVICES_FILE, "r", encoding="utf-8") as f:
    services = json.load(f)

for service in services:
    name = service["name"]
    slug = service["slug"]
    url = service["url"]

    print(f"Fetching {name}...")

    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (compatible; ReavoBot/1.0; +https://github.com/miromaik/reavo-ledger)"
        }
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()
    except Exception as e:
        print(f"❌ Failed to fetch {name}: {e}")
        continue

    text = trafilatura.extract(response.text)

    if not text:
        print(f"⚠️ Could not extract text from {name}")
        continue

    file_path = TOS_DIR / f"{slug}.md"
    file_path.write_text(text, encoding="utf-8")

    print(f"✅ Saved {file_path}")
