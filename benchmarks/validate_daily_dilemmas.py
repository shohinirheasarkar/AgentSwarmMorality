import hashlib
import json
from pathlib import Path

from benchmarks.daily_dilemmas import (
    load_action_pairs,
    load_splits,
    load_value_annotations,
    prompt_pair,
)


def validate():
    root = Path(__file__).resolve().parent.parent
    source = json.loads(
        (root / "benchmarks/daily_dilemmas_source.json").read_text()
    )
    raw = root / source["raw_directory"]
    checksums = json.loads((raw / "checksums.json").read_text())

    if set(checksums) != set(source["files"]):
        raise ValueError("checksum file does not match source manifest")
    for filename, expected in checksums.items():
        actual = hashlib.sha256((raw / filename).read_bytes()).hexdigest()
        if actual != expected:
            raise ValueError(f"checksum mismatch: {filename}")

    pairs = load_action_pairs(
        raw / "dilemma_to_action_to_values_aggregated.csv"
    )
    annotations = load_value_annotations(
        raw / "action_to_party_to_value.csv", pairs
    )
    for dilemma_id, pair in pairs.items():
        prompt_pair(pair)
        for action_type in pair:
            if (dilemma_id, action_type) not in annotations:
                raise ValueError(f"action has no annotations: {dilemma_id}")

    splits = load_splits(root / "data/splits/daily_dilemmas.json", pairs)
    print(f"validated {len(pairs)} dilemmas")
    print(f"annotation rows: {sum(map(len, annotations.values()))}")
    for name, ids in splits.items():
        print(f"{name}: {len(ids)}")


if __name__ == "__main__":
    validate()
