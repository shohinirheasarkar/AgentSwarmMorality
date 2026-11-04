import hashlib
import json
from pathlib import Path

from benchmarks.daily_dilemmas import load_action_pairs, load_splits


def create_splits():
    root = Path(__file__).resolve().parent.parent
    source = root / "data/raw/daily_dilemmas"
    pairs = load_action_pairs(
        source / "dilemma_to_action_to_values_aggregated.csv"
    )
    ids = sorted(
        pairs,
        key=lambda dilemma_id: hashlib.sha256(
            f"daily-dilemmas-pilot-v1:{dilemma_id}".encode()
        ).hexdigest(),
    )
    splits = {
        "pilot": ids[:20],
        "training": [],
        "evaluation": ids[20:],
    }
    path = root / "data/splits/daily_dilemmas.json"
    if path.exists():
        raise FileExistsError(f"split file already exists: {path}")

    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(splits, indent=2) + "\n")
    load_splits(path, pairs)


if __name__ == "__main__":
    create_splits()
