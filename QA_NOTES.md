# QA_NOTES.md

## Zendesk CSV Cleanup + Macro Suggestion Helper QA Pass

### Verified
- clean and messy CSV exports both processed successfully
- whitespace stripping on all keys and values works
- empty-row filtering works (rows with no subject AND no description are dropped)
- macro suggestion deduplication works (same subject counted correctly)
- suggestions ranked by frequency
- priority field added to suggestions output (low/medium/high by count)
- bug found and fixed: report writer was missing the new `priority` field — resolved
- outputs generated successfully:
  - `output/cleaned_export.csv`
  - `output/macro_suggestions.csv`
  - `output/report.md`
- MVP runs with standard-library Python only

### Test coverage added
- `tests/test_cleanup.py` — whitespace stripping, empty key check, missing file handling
- `tests/test_suggestions.py` — deduplication, ranking by count, empty input handling

### Current limitations
- macro suggestion quality depends on subject consistency in the export
- tag-pattern suggestions not yet implemented
- missing column detection is not yet strict
- no encoding detection for non-UTF-8 exports

### QA decision
**Pass for internal MVP / portfolio packaging prep**

### Positioning confirmed
**Primary:** Support Ops Cleanup Tool
**Secondary:** Macro Suggestion Helper

### Before public release
- add encoding detection for non-UTF-8 files
- add configurable minimum count threshold via CLI flag
- tighten README with before/after example output
- initialize Git repo and prepare GitHub-ready packaging
