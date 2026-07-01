# CMF Regulation PDF to Markdown

This repository converts Chilean CMF regulation PDFs (Spanish) into Markdown files for AI knowledge use.

## Repository Structure

- `pdf/`: source PDF files
- `markdown/`: converted Markdown outputs
- `convert_pdfs.py`: conversion pipeline
- `conversion_status.csv`: tracking file with conversion status and manual verification flag

## Requirements

- Python 3.10+
- `pdfplumber`

Install dependency:

```bash
pip install pdfplumber
```

## Usage

Convert a single PDF:

```bash
python3 convert_pdfs.py --file pdf/<filename>.pdf
```

Convert all PDFs:

```bash
python3 convert_pdfs.py --all
```

`--llm-audit` and related flags are currently deprecated and ignored.
The converter runs in deterministic mode only.

Skip files that already have markdown output:

```bash
python3 convert_pdfs.py --all --skip-existing
```

## Notes

- The pipeline includes cleanup for page artifacts, line wrapping, and formula detection.
- Mathematical formulas that may need manual review are flagged in markdown with `⚠️`.
- `conversion_status.csv` includes `needs_further_manual_verification` for tracking remaining manual checks.
