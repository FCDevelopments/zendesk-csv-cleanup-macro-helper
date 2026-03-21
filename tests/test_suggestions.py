from src.suggestions import build_macro_suggestions


def test_build_macro_suggestions_deduplicates() -> None:
    rows = [
        {"subject": "Password reset needed", "description": ""},
        {"subject": "Password reset needed", "description": ""},
        {"subject": "VPN issue", "description": ""},
    ]
    suggestions = build_macro_suggestions(rows)
    subjects = [s["subject_pattern"] for s in suggestions]
    assert subjects.count("Password reset needed") == 1


def test_build_macro_suggestions_ranks_by_count() -> None:
    rows = [
        {"subject": "VPN issue", "description": ""},
        {"subject": "Password reset needed", "description": ""},
        {"subject": "Password reset needed", "description": ""},
    ]
    suggestions = build_macro_suggestions(rows)
    assert suggestions[0]["subject_pattern"] == "Password reset needed"
    assert suggestions[0]["ticket_count"] == 2


def test_build_macro_suggestions_handles_empty() -> None:
    suggestions = build_macro_suggestions([])
    assert suggestions == []
