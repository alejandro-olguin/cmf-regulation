"""
PDF to Markdown converter for CMF regulation documents.

Uses pdfplumber for layout-aware extraction with table detection, header/footer
removal, equation flagging, and paragraph line re-joining.

Usage:
    python convert_pdfs.py --file input/ncg_209_2007_refundido.pdf
    python convert_pdfs.py --all
    python convert_pdfs.py --all --skip-existing
"""

import argparse
import logging
import re
import sys
from pathlib import Path

import pdfplumber

INPUT_DIR = Path("input")
OUTPUT_DIR = Path("output")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)],
)
log = logging.getLogger(__name__)

# ─────────────────────────────────────────────────────────────────────────────
# Page header / footer removal
# ─────────────────────────────────────────────────────────────────────────────

_PAGE_HEADER_RE = re.compile(
    r"NORMA DE CAR[ÁA]CTER GENERAL\s+N[°º]\s*[\d]+\s*\n"
    r"FECHA\s*:\s*\d{1,2}\.\d{1,2}\.\d{4}\s*\n?",
    re.MULTILINE,
)
_PAGE_FOOTER_RE = re.compile(
    r"COMISI[ÓO]N PARA EL MERCADO FINANCIERO\s*\n\s*\d+\s*\n",
    re.MULTILINE,
)
_PAGE_FOOTER_NO_NUM_RE = re.compile(
    r"COMISI[ÓO]N PARA EL MERCADO FINANCIERO\s*\n",
    re.MULTILINE,
)


def extract_document_title(first_page_text: str) -> str | None:
    """Extract the document title from the first-page header pattern."""
    m = _PAGE_HEADER_RE.search(first_page_text)
    if m:
        return m.group(0).strip().replace("\n", " — ")
    return None


def remove_page_chrome(text: str) -> str:
    """Remove repeated page headers, footers and standalone page numbers."""
    text = _PAGE_HEADER_RE.sub("", text)
    text = _PAGE_FOOTER_RE.sub("", text)
    text = _PAGE_FOOTER_NO_NUM_RE.sub("", text)
    # Note: we do NOT remove standalone single-digit lines here because they may
    # be formula subscripts (e.g. "0" in "r_0"). Page numbers are already removed
    # as part of the footer pattern above.
    return text


# ─────────────────────────────────────────────────────────────────────────────
# Table formatting
# ─────────────────────────────────────────────────────────────────────────────


def format_table_as_markdown(table: list) -> str:
    """Convert a pdfplumber table (list of lists) to a markdown table string."""
    if not table:
        return ""

    rows = []
    for row in table:
        cells = []
        for cell in row:
            cell = "" if cell is None else str(cell)
            cell = cell.replace("\n", " ").replace("|", "\\|").strip()
            cells.append(cell)
        rows.append(cells)

    if not rows:
        return ""

    max_cols = max(len(r) for r in rows)
    rows = [r + [""] * (max_cols - len(r)) for r in rows]

    header = rows[0]
    separator = ["---"] * max_cols
    body = rows[1:]

    lines = [
        "| " + " | ".join(header) + " |",
        "| " + " | ".join(separator) + " |",
    ]
    for row in body:
        lines.append("| " + " | ".join(row) + " |")

    return "\n".join(lines)


# ─────────────────────────────────────────────────────────────────────────────
# Page content extraction (text + tables, bbox-aware)
# ─────────────────────────────────────────────────────────────────────────────


def extract_page_content(page) -> str:
    """
    Extract text and tables from a single pdfplumber page.
    Uses table bounding boxes to crop the page, preventing content duplication.
    """
    try:
        table_objects = page.find_tables()
    except Exception:
        table_objects = []

    if not table_objects:
        return page.extract_text() or ""

    table_objects = sorted(table_objects, key=lambda t: t.bbox[1])

    parts = []
    prev_bottom = 0
    pw = page.width
    ph = page.height

    for tbl in table_objects:
        x0, top, x1, bottom = tbl.bbox

        if top > prev_bottom + 2:
            above = page.crop((0, prev_bottom, pw, top))
            txt = above.extract_text()
            if txt and txt.strip():
                parts.append(txt.strip())

        data = tbl.extract()
        if data:
            md = format_table_as_markdown(data)
            if md:
                parts.append(md)

        prev_bottom = bottom

    if prev_bottom < ph - 2:
        below = page.crop((0, prev_bottom, pw, ph))
        txt = below.extract_text()
        if txt and txt.strip():
            parts.append(txt.strip())

    return "\n\n".join(parts)


# ─────────────────────────────────────────────────────────────────────────────
# Miscellaneous text cleanup
# ─────────────────────────────────────────────────────────────────────────────


def fix_kerning_artifacts(text: str) -> str:
    """Fix common PDF kerning artifacts in numbers and hyphenated words."""
    # "digit SPACE comma digit" → "digit comma digit"  (e.g. "0 ,1" → "0,1")
    text = re.sub(r"(\d) ,(\d)", r"\1,\2", text)
    # "digit SPACE %" → "digit%"
    text = re.sub(r"(\d) %", r"\1%", text)
    # Multi-digit percentage: "2 0,3%" → "20,3%", "1 1,3%" → "11,3%" etc.
    text = re.sub(r"\b(\d) (\d,\d+%)", r"\1\2", text)
    text = re.sub(r"\b(\d) (\d+%)", r"\1\2", text)
    # Hyphenated word-breaks at line endings
    text = re.sub(r"(\w)-\n(\w)", r"\1\2", text)
    return text


def collapse_blank_lines(text: str) -> str:
    return re.sub(r"\n{3,}", "\n\n", text)


# ─────────────────────────────────────────────────────────────────────────────
# Equation fragment detection  (must run BEFORE line re-joining)
# ─────────────────────────────────────────────────────────────────────────────

_MATH_CHARS = frozenset("+-*/=^∑∫√≤≥≠∞∆−×÷")


def _is_equation_fragment(line: str) -> bool:
    """
    Return True if a line looks like a broken math formula fragment.

    Detects two patterns:
    1. Very short lines (≤ 15 chars) containing math operators
    2. Spaced-out character lines (kerning artefact) like "e n s u a l = 1 2 1 + i a"
       where most tokens are single characters and there is a math operator.
    """
    s = line.strip()
    if not s:
        return False

    # Never flag markdown table rows (separator or data rows)
    if s.startswith("|"):
        return False

    # Short line with math operator
    if len(s) <= 15 and any(c in _MATH_CHARS for c in s):
        return True

    # Short single token (subscript/superscript or isolated variable)
    if len(s) <= 4 and re.match(r"^[\w\d\(\)\[\]\{\}\.\,\s]+$", s):
        return True

    # Spaced-out characters (kerned formula) — most tokens are single chars
    # and the line contains at least one digit or operator
    tokens = s.split()
    if len(tokens) >= 4:
        single_char_ratio = sum(1 for t in tokens if len(t) == 1) / len(tokens)
        if single_char_ratio >= 0.6 and any(
            c.isdigit() or c in _MATH_CHARS for c in s
        ):
            return True

    return False


def detect_and_flag_equations(text: str) -> str:
    """
    Detect runs of ≥ 3 consecutive broken equation fragments and wrap them
    in a visible warning block.  Must be called before rejoin_wrapped_lines
    so the individual short lines are still present.
    """
    lines = text.split("\n")
    result = []
    i = 0

    while i < len(lines):
        stripped = lines[i].strip()

        if _is_equation_fragment(stripped):
            block = [stripped]
            j = i + 1
            frag_count = 1

            while j < len(lines):
                s = lines[j].strip()
                if not s:
                    if j + 1 < len(lines) and _is_equation_fragment(
                        lines[j + 1].strip()
                    ):
                        block.append("")
                        j += 1
                        continue
                    else:
                        break
                if _is_equation_fragment(s):
                    block.append(s)
                    frag_count += 1
                    j += 1
                else:
                    break

            if frag_count >= 3:
                result.append(
                    "> ⚠️ **Fórmula matemática** — "
                    "extracción automática incompleta; consultar PDF original."
                )
                result.append("> ```")
                for b in block:
                    result.append(f"> {b}")
                result.append("> ```")
                i = j
                continue

        result.append(lines[i])
        i += 1

    return "\n".join(result)


# ─────────────────────────────────────────────────────────────────────────────
# Paragraph line re-joining  (must run AFTER equation detection)
# ─────────────────────────────────────────────────────────────────────────────


def _is_non_joinable(s: str) -> bool:
    """
    Return True for lines that must NOT be joined with the following line.
    """
    if not s:
        return True
    if s.startswith(("#", ">", "|", "▪", "•", "*", "```")):
        return True
    if re.match(r"^\d+(\.\d+)*[\.\s]", s):
        return True
    if re.match(r"^[a-zA-Z][\.\)]\s", s):
        return True
    if re.match(r"^[ivxIVX]+\)\s", s):
        return True
    if s.startswith("- ") or s.startswith("– "):
        return True
    if s.isupper() and 3 < len(s) < 80 and " " in s:
        return True
    return False


def rejoin_wrapped_lines(text: str) -> str:
    """
    Re-join lines soft-wrapped by the PDF renderer.
    Only joins when the continuation line starts with a lowercase letter (Spanish).
    Does NOT touch lines already inside equation blocks (> prefix) or code fences (```).
    """
    lines = text.split("\n")
    result = []
    i = 0
    in_code_block = False

    while i < len(lines):
        current = lines[i].rstrip()
        stripped = current.strip()

        # Toggle code-fence state; never join inside a code block.
        if stripped.startswith("```"):
            in_code_block = not in_code_block
            result.append(current)
            i += 1
            continue

        if in_code_block:
            result.append(current)
            i += 1
            continue

        if not _is_non_joinable(stripped):
            while i + 1 < len(lines):
                tail = current.rstrip()
                if tail.endswith((".", ":", ";", "?", "!", "»", '"', ")")):
                    break
                if _is_non_joinable(tail.strip()):
                    break

                next_raw = lines[i + 1]
                next_s = next_raw.strip()

                if not next_s:
                    break
                if _is_non_joinable(next_s):
                    break
                if next_s[0].islower():
                    current = tail + " " + next_s
                    i += 1
                else:
                    break

        result.append(current)
        i += 1

    return "\n".join(result)


# ─────────────────────────────────────────────────────────────────────────────
# Markdown heading promotion
# ─────────────────────────────────────────────────────────────────────────────


def add_markdown_headings(text: str) -> str:
    """
    Promote section titles to markdown heading syntax.
    Deliberately excludes: REF lines, equation lines, lines with "=" signs.
    """
    lines = text.split("\n")
    result = []

    for line in lines:
        s = line.strip()

        if s.startswith("#"):
            result.append(line)
            continue

        # Skip equation / blockquote lines
        if s.startswith(">"):
            result.append(line)
            continue

        # Skip lines containing "=" (likely equations, not headings)
        if "=" in s and not re.match(r"^\d+\.", s):
            result.append(line)
            continue

        # Skip REF: label lines
        if s.startswith("REF.:"):
            result.append(line)
            continue

        # Main numbered section: "1. Título" or "7. Disposiciones..."
        if re.match(r"^\d+\.\s+[A-ZÁÉÍÓÚÑ]", s) and len(s) < 100:
            result.append(f"## {s}")
            continue

        # Subsection: "1.1 Título"
        if re.match(r"^\d+\.\d+\s+[A-ZÁÉÍÓÚÑ]", s) and len(s) < 100:
            result.append(f"### {s}")
            continue

        # Lettered subsection at annex level: "A. Instrumentos..." "B. Mutuos..."
        if re.match(r"^[A-Z]\.\s+[A-ZÁÉÍÓÚÑ]", s) and len(s) < 100:
            result.append(f"#### {s}")
            continue

        # ANEXO headings
        if re.match(r"^ANEXO\s+N[°º]\s*\d+", s):
            result.append(f"## {s}")
            continue

        # Short all-caps headings (e.g. "DETERMINACION DEL VECTOR...")
        # but NOT long all-caps preamble text and NOT lines with ":" (label:value)
        if (
            s.isupper()
            and 5 < len(s) < 80
            and " " in s
            and ":" not in s
            and not s.startswith("|")
            and not s.startswith("REF")
            and not s.startswith("NORMA")
            and not s.startswith("LAS")
            and not s.startswith("OBLIGACIONES")
            and not s.startswith("ENTIDADES")
        ):
            result.append(f"### {s}")
            continue

        result.append(line)

    return "\n".join(result)


# ─────────────────────────────────────────────────────────────────────────────
# Document-specific patches for known garbled content
# ─────────────────────────────────────────────────────────────────────────────

# Internacional default risk table — reconstructed from PDF page 10.
# Row labels match the Nacional table structure; percentages read from raw text.
_INTERNACIONAL_TABLE = """\
**Internacional (CdR Global) / Duración Modificada**

| CdR Internacional | 0 a 5 años | 6 a 10 años | 11 o más años |
| --- | --- | --- | --- |
| AAA | 0,1% | 0,3% | 0,4% |
| AA+ | 0,1% | 0,3% | 0,5% |
| AA | 0,1% | 0,4% | 0,6% |
| AA- | 0,1% | 0,4% | 0,7% |
| A+ | 0,1% | 0,4% | 0,8% |
| A | 0,1% | 0,5% | 1,0% |
| A- | 0,2% | 0,7% | 1,2% |
| BBB+ | 0,3% | 0,9% | 1,5% |
| BBB | 0,4% | 1,2% | 2,1% |
| BBB- | 0,7% | 2,3% | 3,4% |
| BB+ | 1,0% | 3,0% | 4,4% |
| BB | 1,7% | 4,8% | 6,7% |
| BB- | 2,7% | 7,3% | 9,8% |
| B+ | 4,4% | 9,9% | 12,4% |
| B | 5,7% | 11,3% | 13,4% |
| B- | 9,2% | 15,6% | 17,2% |
| CCC-C | 20,3% | 25,6% | 27,2% |
| D | 52,3% | 52,3% | 52,3% |"""

# Known mathematical formulas for NCG 209 (reconstructed from context).
_FORMULA_PATCHES = [
    # ET vector notation (ANEXO 1)
    # Raw text: "VTD TSA: Vector de tasas...\nE T =\n t\nt\n\nt\n1\n2\nn\n\nt\nj\n= tasa cero real..."
    (
        re.compile(
            r"(VTD TSA: Vector de tasas de descuento de orden n\.)\s*\n"
            r"E\s*T\s*=\s*\n"
            r".*?"
            r"= tasa cero real correspondiente al año j\s*;\s*j = 1,\s*\.\.\.,\s*n\.",
            re.DOTALL,
        ),
        lambda m: (
            f"{m.group(1)}\n\n"
            "> **ET** = [t₁, t₂, ..., tₙ]\n\n"
            "> donde **tⱼ** = tasa cero real correspondiente al año j; j = 1, ..., n."
        ),
    ),
    # Monthly rate mensualización formula (ANEXO 1)
    # Raw text: "aplicar la siguiente fórmula:\ni m\nj\ne n s u a l = ...\nn u a l − 1\ndonde j ="
    (
        re.compile(
            r"(aplicar la siguiente fórmula:)\s*\n"
            r"i\s+m\s*\n"
            r"j\s*\n"
            r"e\s+n\s+s\s+u\s+a\s+l\s*=.*?\n"
            r"j\s*\n"
            r"n\s+u\s+a\s+l\s+[−\-]\s*1\s*\n"
            r"(donde j = año)",
            re.DOTALL,
        ),
        lambda m: (
            f"{m.group(1)}\n\n"
            "```\ni_mensual(j) = (1 + i_anual(j))^(1/12) - 1\n```\n\n"
            f"{m.group(2)}"
        ),
    ),
    # Inflation formulas (ANEXO 2)
    # Raw text: "Inflación Anual Primer Quinquenio (ipq) =\n( 1\n...\nInflación Anual Primer Decenio (ipd) =..."
    (
        re.compile(
            r"(Inflación Anual Primer Quinquenio \(ipq\)\s*=)\s*\n"
            r".*?"
            r"(Inflación Anual Primer Decenio \(ipd\)\s*=).*?BCU10\s*\n"
            r"(Inflación Anual Segundo Quinquenio \(isq\)\s*=)\s*\n"
            r".*?"
            r"(Donde:)",
            re.DOTALL,
        ),
        lambda m: (
            f"{m.group(1)}\n\n"
            "```\nipq = (1 + iBCP5) / (1 + rBCU5) - 1\n```\n\n"
            f"{m.group(2)}\n\n"
            "```\nipd = (1 + iBCP10) / (1 + rBCU10) - 1\n```\n\n"
            f"{m.group(3)}\n\n"
            "```\nisq = (1 + ipd)² / (1 + ipq) - 1\n```\n\n"
            f"{m.group(4)}"
        ),
    ),
    # UF conversion formula (ANEXO 2)
    # Raw: "...fórmula:\nU F\nt\n= U F\n0\n* (1 + i j q ) t /1 2...\nDonde:"
    (
        re.compile(
            r"(Con\s+base en las tasas ipq e isq.*?fórmula:)\s*\n"
            r"U\s+F\s*\n"
            r"t\s*\n"
            r"=\s*U\s+F\s*\n"
            r"0\s*\n"
            r"\*[^\n]+\n"
            r"(Donde:)",
            re.DOTALL,
        ),
        lambda m: (
            f"{m.group(1).strip()}\n\n"
            "```\nUFt = UF0 × (1 + i_jq)^(t/12)\n"
            "  donde j = p  si t ≤ 60\n"
            "        j = s  si t > 60\n```\n\n"
            f"{m.group(2)}"
        ),
    ),
    # Duration Modified formula (ANEXO 3)
    # Raw text: "Donde:\nD\nDuración Modificada del Instrumento = − t\n(1+r )\n0\nCon:\nDt =\n[frags]\nr0 = Tasa original"
    (
        re.compile(
            r"Donde:\s*\nD\s*\n"
            r"(Duración Modificada del Instrumento\s*=\s*[−\-]\s*t)\s*\n"
            r"\(1\+r\s*\)\s*\n"
            r"0\s*\n"
            r"Con:\s*\nDt\s*=\s*\n"
            r".*?"
            r"(r0 = Tasa original)",
            re.DOTALL,
        ),
        lambda m: (
            "Donde:\n\n"
            "```\n"
            "DM = Dt / (1 + r0)\n\n"
            "     Σ[ t × Ct / (1+r0)^t ]\n"
            "Dt = ─────────────────────────\n"
            "       Σ[ Ct / (1+r0)^t ]\n"
            "```\n\n"
            f"{m.group(2)}"
        ),
    ),
]

# Detects the garbled Internacional table block that pdfplumber cannot parse.
# Matches from the "C" header + concatenated-ratings line to just before "Nacional".
_INTERNACIONAL_BLOCK_RE = re.compile(
    r"C\n[A-Z\+\-]{10,}\n.*?(?=\nNacional\n)",
    re.DOTALL,
)


def patch_document(text: str, source_file: str) -> str:
    """Apply document-specific patches for NCG 209."""
    if "ncg_209" not in source_file.lower():
        return text

    # Replace garbled Internacional table block
    text = _INTERNACIONAL_BLOCK_RE.sub(
        _INTERNACIONAL_TABLE + "\n\n", text
    )

    # Apply formula reconstructions
    for pattern, replacement in _FORMULA_PATCHES:
        text = pattern.sub(replacement, text)

    # Fix truncated leasing default table header (pdfplumber misses table start)
    text = text.replace(
        "| aso en el pago de cuotas | % de castigo en flujos |",
        "| Meses de atraso en el pago de cuotas | % de castigo en flujos |",
    )

    return text


# ─────────────────────────────────────────────────────────────────────────────
# Metadata header
# ─────────────────────────────────────────────────────────────────────────────


def build_metadata_header(source_file: str, title: str | None) -> str:
    title_line = f"# {title}\n\n" if title else ""
    return (
        f"<!-- source: {source_file} -->\n"
        "<!-- language: es -->\n"
        "<!-- note: Las fórmulas matemáticas extraídas de PDFs pueden ser incompletas.\n"
        "     Los bloques marcados con ⚠️ deben verificarse contra el PDF original. -->\n\n"
        + title_line
    )


# ─────────────────────────────────────────────────────────────────────────────
# Main conversion pipeline
# ─────────────────────────────────────────────────────────────────────────────


def convert_file(pdf_path: Path, output_dir: Path) -> Path:
    """Convert a single PDF to Markdown and write to output_dir."""
    output_dir.mkdir(parents=True, exist_ok=True)
    out_path = output_dir / (pdf_path.stem + ".md")

    log.info("Converting: %s", pdf_path.name)

    pages_content: list[str] = []
    document_title: str | None = None

    with pdfplumber.open(str(pdf_path)) as pdf:
        for page_num, page in enumerate(pdf.pages):
            raw = extract_page_content(page)

            # Capture the document title from the very first page header
            if page_num == 0 and document_title is None:
                document_title = extract_document_title(raw)

            clean = remove_page_chrome(raw)
            clean = fix_kerning_artifacts(clean)
            clean = collapse_blank_lines(clean)
            if clean.strip():
                pages_content.append(clean.strip())

    full_text = "\n\n".join(pages_content)

    # Operation order matters:
    # 1. Document-specific patches run FIRST on raw extracted text,
    #    before equation detection scrambles the content.
    full_text = patch_document(full_text, pdf_path.name)
    # 2. Detect equations (while lines are still short / individual)
    full_text = detect_and_flag_equations(full_text)
    # 3. Re-join wrapped paragraph lines (⚠️ blocks are non-joinable via ">" prefix)
    full_text = rejoin_wrapped_lines(full_text)
    # 4. Promote section headings
    full_text = add_markdown_headings(full_text)
    # 5. Final blank-line normalisation
    full_text = collapse_blank_lines(full_text)

    result = build_metadata_header(pdf_path.name, document_title) + full_text
    out_path.write_text(result, encoding="utf-8")
    log.info("  → %s (%d chars)", out_path, len(result))
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

    log.info("Done. Converted: %d | Skipped: %d | Failed: %d", success, skipped, failed)


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

