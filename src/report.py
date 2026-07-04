from __future__ import annotations

import csv
from pathlib import Path
from typing import Dict, List


def write_outputs(rows: List[Dict[str, str]], suggestions: List[Dict[str, object]], output_dir: str) -> None:
    out_dir = Path(output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    cleaned_export = out_dir / "cleaned_export.csv"
    suggestions_csv = out_dir / "macro_suggestions.csv"
    report_md = out_dir / "report.md"

    if rows:
        fieldnames = list(rows[0].keys())
        with cleaned_export.open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)

    with suggestions_csv.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["subject_pattern", "ticket_count", "priority", "suggested_macro_title"])
        writer.writeheader()
        writer.writerows(suggestions)

    lines = ["# Macro Suggestions", ""]
    for item in suggestions:
        lines.append(f"- {item['suggested_macro_title']} ({item['ticket_count']} tickets)")

    report_md.write_text("\n".join(lines), encoding="utf-8")
