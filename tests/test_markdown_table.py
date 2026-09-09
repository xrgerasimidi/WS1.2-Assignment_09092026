from pathlib import Path
import re


ROOT_DIR = Path(__file__).resolve().parents[1]


def test_markdown_file_contains_table():
    markdown = (ROOT_DIR / "1_markdown.md").read_text(encoding="utf-8")

    has_table_row = re.search(r"^\s*\|.*\|\s*$", markdown, re.MULTILINE)
    has_separator_row = re.search(r"^\s*\|[ -:|]+\|\s*$", markdown, re.MULTILINE)

    assert has_table_row and has_separator_row, "Markdown table not found in 1_markdown.md"