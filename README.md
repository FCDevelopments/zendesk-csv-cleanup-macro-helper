# Zendesk CSV Cleanup + Macro Suggestion Helper

> Clean messy Zendesk-style ticket exports and surface the repeated issues most worth turning into macros — one command, no setup.

## What it does
This tool takes a raw Zendesk-style CSV export, strips whitespace and normalizes formatting, drops blank/junk rows, and surfaces the most frequently recurring subject patterns as macro candidates. Outputs a cleaned CSV plus a ranked suggestion report.

## Who it's for
- Support admins who periodically export Zendesk data and manually look for patterns
- Teams wanting to identify which issues deserve a macro or saved reply
- Anyone doing CSV cleanup on messy support exports before passing them upstream

## Problem it solves
Zendesk exports are often messy: inconsistent spacing, partial rows, repeated subjects that could be macros but never get identified systematically. This replaces a manual export-review session with a clean automated pass.

## Usage
```bash
python src/main.py sample_data/zendesk_export_sample.csv --output-dir output
```

Try it with the included messy sample too:
```bash
python src/main.py sample_data/zendesk_messy_sample.csv --output-dir output
```

## Input format
Any Zendesk-style CSV with at minimum a `subject` column. Other common fields (description, status, priority, tags, macro_used) are cleaned and preserved if present.

## Outputs
| File | What it contains |
|---|---|
| `output/cleaned_export.csv` | Normalized, whitespace-stripped version of your input |
| `output/macro_suggestions.csv` | Ranked recurring subjects with priority score |
| `output/report.md` | Human-readable macro suggestion summary |

## Sample output
```
# Macro Suggestions

- Macro for: Password reset needed (2 tickets) [high]
- Macro for: VPN issue (1 ticket) [low]
```

```csv
subject_pattern,ticket_count,priority,suggested_macro_title
Password reset needed,2,high,Macro for: Password reset needed
VPN issue,1,low,Macro for: VPN issue
```

## Requirements
- Python 3.9+
- No external dependencies — uses standard library only

## Limitations (MVP)
- Macro suggestion quality depends on subject consistency in the export
- Tag-pattern suggestions not yet implemented
- No encoding detection for non-UTF-8 files yet
- Minimum count threshold is hardcoded at 1 (all recurring subjects shown)

## Project structure
```
zendesk-csv-cleanup-macro-helper/
├── README.md
├── requirements.txt
├── sample_data/
│   ├── zendesk_export_sample.csv
│   └── zendesk_messy_sample.csv
├── output/
├── src/
│   ├── main.py
│   ├── cleanup.py
│   ├── suggestions.py
│   └── report.py
└── tests/
    ├── test_cleanup.py
    └── test_suggestions.py
```

## Roadmap
- configurable minimum count threshold via CLI flag
- tag-pattern macro suggestions
- encoding detection for non-UTF-8 exports
- before/after diff output for review workflows
