import hashlib
import json
from pathlib import Path
from urllib.request import urlopen


def download():
    root = Path(__file__).resolve().parent.parent
    source_path = root / "benchmarks/daily_dilemmas_source.json"
    source = json.loads(source_path.read_text())
    destination = root / source["raw_directory"]
    destination.mkdir(parents=True, exist_ok=True)
    checksums = {}

    for filename in source["files"]:
        url = (
            f'{source["repository"]}/resolve/'
            f'{source["revision"]}/{filename}'
        )
        with urlopen(url, timeout=60) as response:
            content = response.read()

        path = destination / filename
        if path.exists():
            if path.read_bytes() != content:
                raise ValueError(f"existing file differs: {path}")
        else:
            path.write_bytes(content)

        checksums[filename] = hashlib.sha256(content).hexdigest()

    checksum_path = destination / "checksums.json"
    checksum_path.write_text(
        json.dumps(checksums, indent=2, sort_keys=True) + "\n"
    )


if __name__ == "__main__":
    download()
