from __future__ import annotations

from collections import Counter
from typing import Dict, List

# Minimum times a subject pattern must appear to be worth a macro suggestion
MIN_COUNT_THRESHOLD = 1


def build_macro_suggestions(rows: List[Dict[str, str]]) -> List[Dict[str, object]]:
    """Generate macro suggestions from recurring subject patterns.

    - deduplicates by subject
    - ranks by frequency
    - skips empty subjects
    - applies a minimum threshold so low-signal patterns are surfaced but clearly ranked
    """
    subject_counter = Counter(
        row.get("subject", "").strip()
        for row in rows
        if row.get("subject", "").strip()
    )

    suggestions: List[Dict[str, object]] = []
    for subject, count in subject_counter.most_common(10):
        if count < MIN_COUNT_THRESHOLD:
            continue
        ticket_word = "ticket" if count == 1 else "tickets"
        suggestions.append(
            {
                "subject_pattern": subject,
                "ticket_count": count,
                "suggested_macro_title": f"Macro for: {subject[:50]}",
                "priority": "high" if count >= 3 else "medium" if count >= 2 else "low",
            }
        )

    return suggestions
