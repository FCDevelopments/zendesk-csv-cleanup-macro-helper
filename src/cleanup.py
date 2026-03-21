from __future__ import annotations

import csv
from pathlib import Path
from typing import Dict, List


def clean_export(path: str) -> List[Dict[str, str]]:
    """Load and clean a Zendesk-style CSV export.

    - strips leading/trailing whitespace from all keys and values
    - normalizes column names to lowercase
    - fills missing values with empty string
    - removes rows where both subject and description are empty
    """
    csv_path = Path(path)
    if not csv_path.exists():
        raise FileNotFoundError(f"Input file not found: {csv_path}")

    with csv_path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        rows: List[Dict[str, str]] = []
        for row in reader:
            # normalize keys to lowercase and strip whitespace from all values
            cleaned = {
                str(key).strip().lower(): str(value or "").strip()
                for key, value in row.items()
            }
            # skip rows where subject AND description are both empty
            subject = cleaned.get("subject", "")
            description = cleaned.get("description", "")
            if not subject and not description:
                continue
            rows.append(cleaned)
    return rows
