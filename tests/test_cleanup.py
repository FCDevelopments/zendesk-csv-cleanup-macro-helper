from src.cleanup import clean_export
from pathlib import Path


def test_clean_export_strips_whitespace() -> None:
    sample = Path("zendesk-csv-cleanup-macro-helper/sample_data/zendesk_export_sample.csv")
    rows = clean_export(str(sample))
    for row in rows:
        for key, value in row.items():
            assert value == value.strip(), f"Field '{key}' has leading/trailing whitespace"


def test_clean_export_no_empty_keys() -> None:
    sample = Path("zendesk-csv-cleanup-macro-helper/sample_data/zendesk_export_sample.csv")
    rows = clean_export(str(sample))
    for row in rows:
        for key in row:
            assert key != "", "Empty column name found after cleanup"


def test_clean_export_missing_file_raises() -> None:
    try:
        clean_export("nonexistent.csv")
        assert False, "Expected FileNotFoundError"
    except FileNotFoundError:
        pass
