from __future__ import annotations

import csv
from pathlib import Path
from typing import Dict, List


def clean_export(path: str) -> List[Dict[str, str]]:
    """Load and clean a Zendesk-style CSV export.

    Cleaning steps applied to every row:
    1. Strip leading/trailing whitespace from all column names
    2. Normalize column names to lowercase for consistent downstream access
    3. Fill any missing/None values with an empty string
    4. Strip whitespace from all cell values
    5. Drop rows where both subject AND description are empty
       (these are junk rows with no useful content)

    Args:
        path: path to the Zendesk CSV export file

    Returns:
        list of cleaned row dicts ready for further processing

    Raises:
        FileNotFoundError: if the file does not exist at the given path
    """
    csv_path = Path(path)

    if not csv_path.exists():
        raise FileNotFoundError(f"Input file not found: {csv_path}")

    with csv_path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        rows: List[Dict[str, str]] = []

        for row in reader:
            # Normalize keys and strip whitespace from all values in one pass
            cleaned = {
                str(key).strip().lower(): str(value or "").strip()
                for key, value in row.items()
            }

            # Skip rows that have no subject AND no description — nothing useful here
            subject = cleaned.get("subject", "")
            description = cleaned.get("description", "")
            if not subject and not description:
                continue

            rows.append(cleaned)

    return rows
