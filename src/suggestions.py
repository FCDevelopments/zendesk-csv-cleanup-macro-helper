from __future__ import annotations

from collections import Counter
from typing import Dict, List

# Minimum number of times a subject must appear to be included in suggestions.
# Set to 1 so all recurring subjects surface, ranked by frequency.
# Increase this to filter out low-signal one-offs in larger datasets.
MIN_COUNT_THRESHOLD = 1


def build_macro_suggestions(rows: List[Dict[str, str]]) -> List[Dict[str, object]]:
    """Generate ranked macro suggestion candidates from recurring ticket subjects.

    Logic:
    - counts how often each unique subject appears across all tickets
    - deduplicates automatically via Counter
    - ranks by frequency (most common first)
    - assigns a priority label (high/medium/low) based on count
    - returns the top 10 subjects as suggestion candidates

    Args:
        rows: cleaned ticket rows from cleanup.py

    Returns:
        list of suggestion dicts, each with subject_pattern, ticket_count,
        priority, and suggested_macro_title
    """
    # Count occurrences of each non-empty subject string
    # strip() here ensures "Password reset " and "Password reset" count as the same
    subject_counter = Counter(
        row.get("subject", "").strip()
        for row in rows
        if row.get("subject", "").strip()  # skip blank subjects
    )

    suggestions: List[Dict[str, object]] = []

    # most_common(10) returns subjects sorted by count, highest first
    for subject, count in subject_counter.most_common(10):
        if count < MIN_COUNT_THRESHOLD:
            continue  # skip anything below the threshold

        # Assign a simple priority tier based on how often the subject appears
        # This helps support leads know which macros to write first
        if count >= 3:
            priority = "high"
        elif count >= 2:
            priority = "medium"
        else:
            priority = "low"

        suggestions.append({
            "subject_pattern": subject,
            "ticket_count": count,
            "suggested_macro_title": f"Macro for: {subject[:50]}",  # truncate long subjects
            "priority": priority,
        })

    return suggestions
