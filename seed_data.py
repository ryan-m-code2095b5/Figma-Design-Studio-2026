"""Load the bundled sample decks into the local data store."""

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from quizcraft.config import Config  # noqa: E402
from quizcraft.models import Deck  # noqa: E402
from quizcraft.storage import JsonStorage  # noqa: E402


def main() -> int:
    config = Config.from_env()
    config.ensure_directories()
    storage = JsonStorage(config.data_dir)

    source = config.assets_dir / "datasets" / "decks.json"
    if not source.exists():
        print(f"Sample data not found at {source}")
        return 1

    raw = json.loads(source.read_text(encoding="utf-8"))
    for item in raw:
        deck = Deck.from_dict(item)
        storage.upsert_deck(deck)
        print(f"Imported deck '{deck.title}' with {deck.size} cards")

    print(f"Done. Data stored in {config.data_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
