import csv
import json


def prompt_fields(row: dict[str, str]) -> dict[str, str]:
    # only these fields should reach the agent
    fields = ("dilemma_situation", "action")

    for field in fields:
        if not row.get(field, "").strip():
            raise ValueError(f"missing daily dilemmas field: {field}")

    return {field: row[field] for field in fields}


def load_action_pairs(path):
    pairs = {}
    seen_ids = set()

    with open(path, encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle):
            prompt_fields(row)
            row_id = row["idx"]
            dilemma_id = row["dilemma_idx"]
            action_type = row["action_type"]

            if not row_id or not dilemma_id:
                raise ValueError("missing daily dilemmas ID")
            if row_id in seen_ids:
                raise ValueError(f"duplicate action row: {row_id}")
            seen_ids.add(row_id)

            pair = pairs.setdefault(dilemma_id, {})
            if action_type in pair:
                raise ValueError(f"duplicate action for {dilemma_id}")
            pair[action_type] = row

    if not pairs:
        raise ValueError("daily dilemmas file is empty")

    for dilemma_id, pair in pairs.items():
        if set(pair) != {"to_do", "not_to_do"}:
            raise ValueError(f"incomplete action pair: {dilemma_id}")

    return pairs


def prompt_pair(pair):
    actions = {
        action_type: prompt_fields(pair[action_type])
        for action_type in ("to_do", "not_to_do")
    }
    situation = actions["to_do"]["dilemma_situation"]

    if situation != actions["not_to_do"]["dilemma_situation"]:
        raise ValueError("action pair has different situation text")

    return {
        "situation": situation,
        "actions": {
            action_type: fields["action"]
            for action_type, fields in actions.items()
        },
    }


def load_value_annotations(path, pairs):
    annotations = {}
    seen_ids = set()

    with open(path, encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle):
            row_id = row["idx"]
            key = (row["dilemma_idx"], row["action_type"])

            if not row_id or row_id in seen_ids:
                raise ValueError(f"missing or duplicate annotation ID: {row_id}")
            seen_ids.add(row_id)

            pair = pairs.get(key[0], {})
            if key[1] not in pair:
                raise ValueError(f"annotation has no matching action: {key}")
            if row["action"] != pair[key[1]]["action"]:
                raise ValueError(f"annotation action text differs: {key}")

            annotations.setdefault(key, []).append(row)

    if not annotations:
        raise ValueError("daily dilemmas annotations are empty")

    return annotations


def load_splits(path, pairs):
    with open(path, encoding="utf-8") as handle:
        splits = json.load(handle)

    if set(splits) != {"pilot", "training", "evaluation"}:
        raise ValueError("expected pilot, training, and evaluation splits")

    assigned = set()
    for name, ids in splits.items():
        if not isinstance(ids, list):
            raise ValueError(f"split must contain a list of IDs: {name}")
        for dilemma_id in ids:
            if not isinstance(dilemma_id, str) or dilemma_id not in pairs:
                raise ValueError(f"unknown dilemma ID in {name}: {dilemma_id}")
            if dilemma_id in assigned:
                raise ValueError(f"dilemma assigned more than once: {dilemma_id}")
            assigned.add(dilemma_id)

    if assigned != set(pairs):
        raise ValueError("some dilemmas have no split assignment")

    return splits
