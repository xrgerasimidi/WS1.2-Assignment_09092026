from pathlib import Path
import json
import re


ROOT_DIR = Path(__file__).resolve().parents[1]


def test_notebook_markdown_references_sine_wave_svg():
    notebook_path = ROOT_DIR / "2_markdown_ipynb.ipynb"
    notebook = json.loads(notebook_path.read_text(encoding="utf-8"))
    image_pattern = re.compile(
        r"!\[.*?\]\((?:\./|\\)?auxiliary_files[\\/]+sine_wave\.svg\)"
    )

    found_image = any(
        image_pattern.search("".join(cell["source"]).replace("\\", "/"))
        for cell in notebook["cells"]
        if cell["cell_type"] == "markdown"
    )

    assert found_image, "sine_wave.svg not found in a markdown cell"