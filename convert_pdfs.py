"""
PDF to Markdown converter for CMF regulation documents.

Uses markitdown to convert PDFs to Markdown for use as AI agent knowledge base.
Handles Spanish text and notes limitations with equation parsing.

Usage:
    # Convert a single file
    python convert_pdfs.py --file input/ncg_209_2007_refundido.pdf

    # Convert all PDFs
    python convert_pdfs.py --all

    # Convert all, skipping already converted
    python convert_pdfs.py --all --skip-existing
"""

import argparse
import logging
import re
import sys
from pathlib import Path

from markitdown import MarkItDown

INPUT_DIR = Path("input")
OUTPUT_DIR = Path("output")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)],
)
log = logging.getLogger(__name__)


def clean_markdown(text: str, source_file: str) -> str:
    """
    Post-process the raw markdown from markitdown.

    Known issues with PDF → Markdown conversion:
    - Equations are often mangled (symbols replaced, spacing lost). They are
      preserved as-is but wrapped in a callout so downstream agents know to
      treat them with care.
    - Hyphenated line-breaks from PDF columns are rejoined.
    - Excessive blank lines are collapsed.
    """
    # Rejoin words broken across lines by PDF column layout (e.g. "inver-\nsión")
    text = re.sub(r"(\w)-\n(\w)", r"\1\2", text)

    # Collapse runs of 3+ blank lines to 2
    text = re.sub(r"\n{3,}", "\n\n", text)

    # Strip trailing whitespace on each line
    lines = [line.rstrip() for line in text.splitlines()]
    text = "\n".join(lines)

    # Prepend a metadata header so agents know the source and limitations
    header = (
        f"<!-- source: {source_file} -->\n"
        "<!-- language: es -->\n"
        "<!-- note: equations extracted from PDF may be incomplete or malformed. "
        "Treat any mathematical expression with caution and refer to the original PDF "
        "if precision is required. -->\n\n"
    )
    return header + text


def convert_file(pdf_path: Path, output_dir: Path) -> Path:
    """Convert a single PDF to Markdown and write to output_dir."""
    output_dir.mkdir(parents=True, exist_ok=True)
    out_path = output_dir / (pdf_path.stem + ".md")

    log.info("Converting: %s", pdf_path.name)
    md = MarkItDown()
    result = md.convert(str(pdf_path))

    cleaned = clean_markdown(result.text_content, pdf_path.name)
    out_path.write_text(cleaned, encoding="utf-8")
    log.info("  → %s (%d chars)", out_path, len(cleaned))
    return out_path


def convert_all(input_dir: Path, output_dir: Path, skip_existing: bool = False):
    """Convert all PDFs in input_dir."""
    pdfs = sorted(input_dir.glob("*.pdf"))
    if not pdfs:
        log.warning("No PDF files found in %s", input_dir)
        return

    log.info("Found %d PDF files", len(pdfs))
    success, skipped, failed = 0, 0, 0

    for pdf in pdfs:
        out_path = output_dir / (pdf.stem + ".md")
        if skip_existing and out_path.exists():
            log.info("Skipping (already converted): %s", pdf.name)
            skipped += 1
            continue
        try:
            convert_file(pdf, output_dir)
            success += 1
        except Exception as exc:
            log.error("  FAILED %s: %s", pdf.name, exc)
            failed += 1

    log.info(
        "Done. Converted: %d | Skipped: %d | Failed: %d", success, skipped, failed
    )


def main():
    parser = argparse.ArgumentParser(
        description="Convert CMF regulation PDFs to Markdown"
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--file", metavar="PDF", help="Convert a single PDF file")
    group.add_argument("--all", action="store_true", help="Convert all PDFs in input/")
    parser.add_argument(
        "--skip-existing",
        action="store_true",
        help="Skip PDFs that already have a Markdown output",
    )
    args = parser.parse_args()

    if args.file:
        pdf_path = Path(args.file)
        if not pdf_path.exists():
            log.error("File not found: %s", pdf_path)
            sys.exit(1)
        convert_file(pdf_path, OUTPUT_DIR)
    else:
        convert_all(INPUT_DIR, OUTPUT_DIR, skip_existing=args.skip_existing)


if __name__ == "__main__":
    main()
