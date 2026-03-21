import argparse
from cleanup import clean_export
from suggestions import build_macro_suggestions
from report import write_outputs


def main() -> None:
    parser = argparse.ArgumentParser(description="Zendesk CSV Cleanup + Macro Suggestion Helper")
    parser.add_argument("input_csv", help="Path to the Zendesk CSV export")
    parser.add_argument("--output-dir", default="output", help="Directory for generated outputs")
    args = parser.parse_args()

    df = clean_export(args.input_csv)
    suggestions = build_macro_suggestions(df)
    write_outputs(df, suggestions, args.output_dir)
    print("Zendesk cleanup + macro suggestion run complete.")


if __name__ == "__main__":
    main()
