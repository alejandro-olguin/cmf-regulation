"""
PDF to Markdown converter for CMF regulation documents.

Uses pdfplumber for layout-aware extraction with table detection, header/footer
removal, equation flagging, and paragraph line re-joining.

Usage:
    python convert_pdfs.py --file pdf/ncg_209_2007_refundido.pdf
    python convert_pdfs.py --all
    python convert_pdfs.py --all --skip-existing
"""

import argparse
import logging
import re
import sys
from pathlib import Path

import pdfplumber

INPUT_DIR = Path("pdf")
OUTPUT_DIR = Path("markdown")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)],
)
log = logging.getLogger(__name__)

# ─────────────────────────────────────────────────────────────────────────────
# Page header / footer removal
# ─────────────────────────────────────────────────────────────────────────────

# Matches any repeating page header of the form:
#   CIRCULAR Nº 1512   or  CIRCULARN°2180    or  NORMA DE CARÁCTER GENERAL N° 209
#   FECHA: 02.01.2001      FECHA :25.06.2015     FECHA : 24.12.2007
_PAGE_HEADER_RE = re.compile(
    r"(?:NORMA DE CAR[ÁA]CTER GENERAL\s+N[°º]\s*[\d]+|"
    r"CIRCULAR\s*N[°º]\s*[\d]+(?:\s*[\w\s]*?)?)\s*\n"
    r"FECHA\s*:?\s*\d{1,2}\.\d{1,2}\.\d{4}\s*\n?",
    re.MULTILINE,
)
# CMF footer (post-2017 institution name)
_PAGE_FOOTER_RE = re.compile(
    r"COMISI[ÓO]N PARA EL MERCADO FINANCIERO\s*\n\s*\d+\s*\n?",
    re.MULTILINE,
)
_PAGE_FOOTER_NO_NUM_RE = re.compile(
    r"COMISI[ÓO]N PARA EL MERCADO FINANCIERO\s*\n",
    re.MULTILINE,
)
# SVS footer (pre-2017 institution name: Superintendencia de Valores y Seguros)
_PAGE_FOOTER_SVS_RE = re.compile(
    r"SUPERINTENDENCIA DE VALORES Y SEGUROS DE CHILE\s*\n\s*\d+\s*\n?",
    re.MULTILINE,
)
_PAGE_FOOTER_SVS_NO_NUM_RE = re.compile(
    r"SUPERINTENDENCIA DE VALORES Y SEGUROS DE CHILE\s*\n",
    re.MULTILINE,
)


def extract_document_title(first_page_text: str) -> str | None:
    """Extract the document title from the first-page header pattern.

    Priority:
    1. Standard CMF/SVS page header (CIRCULAR or NORMA DE CARÁCTER GENERAL) — clean, concise.
    2. REF.: line — used when no repeating standard header is present.

    For CIRCULAR docs: combines the circular number with the REF.: description.
    For NORMA docs: uses the header directly (no REF.: line present).
    """
    m = _PAGE_HEADER_RE.search(first_page_text)

    # Try to find REF.: for a more descriptive title
    ref_m = re.search(r"REF\.\s*:\s*(.+?)(?=\n(?:Para |Esta |[A-Z][a-záéíóúñü]))", first_page_text, re.DOTALL)
    ref_title = None
    if ref_m:
        ref_title = re.sub(r"\s+\d+\s*$", "", ref_m.group(1).strip())
        ref_title = re.sub(r"\s+", " ", ref_title)

    if m:
        header = m.group(0).strip().replace("\n", " — ")
        # For CIRCULAR docs, prepend the circular number to the REF.: description
        if ref_title and "CIRCULAR" in header:
            circ_num = re.search(r"CIRCULAR\s*N[°º]\s*(\d+)", header)
            if circ_num:
                # Trim REF title at first period to drop DEROGA clauses and addressee
                short_ref = ref_title.split(".")[0].strip() if "." in ref_title else ref_title
                return f"CIRCULAR N° {circ_num.group(1)} — {short_ref}"
        return header

    # Pure fallback: no repeating header, use REF.: only
    if ref_title:
        return ref_title
    return None


def remove_page_chrome(text: str) -> str:
    """Remove repeated page headers, footers and standalone page numbers."""
    text = _PAGE_HEADER_RE.sub("", text)
    # CMF footer (post-2017)
    text = _PAGE_FOOTER_RE.sub("", text)
    text = _PAGE_FOOTER_NO_NUM_RE.sub("", text)
    # SVS footer (pre-2017)
    text = _PAGE_FOOTER_SVS_RE.sub("", text)
    text = _PAGE_FOOTER_SVS_NO_NUM_RE.sub("", text)
    # Standalone signer line found in SVS-era documents
    text = re.sub(r"^SUPERINTENDENTE\s*\n", "", text, flags=re.MULTILINE)
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
                result.append("> ")
                result.append("> $$")
                for b in block:
                    result.append(f"> {b}")
                result.append("> $$")
                i = j
                continue

        result.append(lines[i])
        i += 1

    return "\n".join(result)


# ─────────────────────────────────────────────────────────────────────────────
# Cross-page sentence continuation merge  (runs BEFORE equation detection)
# ─────────────────────────────────────────────────────────────────────────────


_CROSS_PAGE_TERMINAL = frozenset(".!?;")
_CROSS_PAGE_STRUCTURAL = ("#", "|", ">", "`", "$", "-", "–", "▪", "•", "*")


def merge_cross_page_continuation(text: str) -> str:
    """
    When pages are joined with a blank line and a sentence runs across the
    page break, remove that blank line so subsequent rejoin logic can merge
    the fragments.

    Only merges when the last non-blank line before the gap ends without
    terminal punctuation AND the first non-blank line after the gap starts
    with a lowercase letter (clearly a mid-sentence continuation).
    """
    lines = text.split("\n")
    result: list[str] = []

    for i, line in enumerate(lines):
        if line.strip() == "" and result:
            # Find last non-blank line already in result
            prev = next((r for r in reversed(result) if r.strip()), "")
            # Find next non-blank line after this gap
            nxt = next((lines[j].strip() for j in range(i + 1, min(i + 3, len(lines)))
                        if lines[j].strip()), "")

            if (prev and nxt and
                    prev.rstrip()[-1] not in _CROSS_PAGE_TERMINAL and
                    nxt[0].islower() and
                    not any(nxt.startswith(p) for p in _CROSS_PAGE_STRUCTURAL)):
                # Drop the blank line (don't append it)
                continue

        result.append(line)

    return "\n".join(result)


# ─────────────────────────────────────────────────────────────────────────────
# Paragraph line re-joining  (must run AFTER equation detection)
# ─────────────────────────────────────────────────────────────────────────────


def _is_non_joinable(s: str) -> bool:
    """
    Return True for lines that must NOT be joined with the following line.
    Used both to decide whether a line can be extended (outer check) and
    whether a candidate continuation should be appended (inner check).
    """
    if not s:
        return True
    if s.startswith(("#", ">", "|", "▪", "•", "*", "```", "$$")):
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
    # Short label-only lines ending with colon (e.g. "Donde:", "AV:", "Notas:")
    if re.match(r"^\w[\w\s]{0,25}:\s*$", s):
        return True
    return False


def rejoin_wrapped_lines(text: str) -> str:
    """
    Re-join lines soft-wrapped by the PDF renderer.
    Joins when the continuation line starts with any letter (lower or upper)
    that is not a structurally distinct element.
    Does NOT touch lines already inside equation blocks (> prefix) or code fences.
    """
    lines = text.split("\n")
    result = []
    i = 0
    in_code_block = False

    # Variable/formula definition lines (r0 =, t =, FPj =, Ct =, etc.) should
    # never be appended as continuation of the previous line.
    _VAR_DEF_RE = re.compile(r"^[A-Za-z]\w{0,5}\d*\s*=\s")

    while i < len(lines):
        current = lines[i].rstrip()
        stripped = current.strip()

        # Toggle code-fence or math-block state; never join inside either.
        if stripped.startswith("```") or stripped == "$$":
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
                # Terminal punctuation stops extension.
                # ")" is intentionally excluded: it's common mid-sentence in
                # Spanish legal text (e.g. "(ET)\nlibre de riesgos").
                if tail.endswith((".", ":", ";", "?", "!", "»", '"')):
                    break
                if _is_non_joinable(tail.strip()):
                    break

                next_raw = lines[i + 1]
                next_s = next_raw.strip()

                if not next_s:
                    break
                if _is_non_joinable(next_s):
                    break
                # Never pull a variable-definition line as a continuation.
                if _VAR_DEF_RE.match(next_s):
                    break
                if next_s[0].isalpha():
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
    # Strip trailing footnote reference numbers from all-caps headings before processing.
    # e.g. "INVERSIONES 1" → "INVERSIONES"  (where 1 is a superscript footnote)
    text = re.sub(
        r"^([A-ZÁÉÍÓÚÑ][A-ZÁÉÍÓÚÑ\s]{4,})\s+\d{1,2}$",
        lambda m: m.group(1).rstrip(),
        text,
        flags=re.MULTILINE,
    )

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

        # Roman numeral top-level sections: "I. TITULO", "II TITULO", "III. TITULO"
        if re.match(r"^(XIV|XIII|XII|XI|IX|VIII|VII|VI|IV|V|I{1,3}|X{1,3})[\.|\s]\s*[A-ZÁÉÍÓÚÑ]", s) and len(s) < 120:
            result.append(f"## {s}")
            continue

        # Main numbered section: "1. Título" or "7. Disposiciones..."
        # Guard: heading must be short OR end with terminal punct, AND must not
        # look like a sentence (verbs like Deberán, Corresponde, etc.) or a form
        # field line (contains underscores or parenthesised numbers like (3)).
        if (re.match(r"^\d+\.\s+[A-ZÁÉÍÓÚÑ]", s) and len(s) < 100
                and (len(s) < 70 or s.endswith((".", ":", "?", "!")))
                and not re.search(r"[_]{3}|\(\d\)", s)
                and not re.match(r"^\d+\.\s+(Deber[aá]|Corresponde|Ser[aá]|Se |Cuando |En |La |Las |Los |El )", s)):
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
            # Check if previous heading was cut mid-title (ends without terminal
            # punctuation) — if so, append to it instead of creating a new heading.
            prev_heading = next((r for r in reversed(result) if r.strip()), "")
            if (prev_heading.startswith(("#", "##", "###")) and
                    not prev_heading.rstrip().endswith((".", ":", "?", "!"))):
                result[-1] = prev_heading.rstrip() + " " + s
            else:
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
            "$$\ni_{mensual}(j) = \\left(1 + i_{anual}(j)\\right)^{1/12} - 1\n$$\n\n"
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
            "$$\ni_{pq} = \\frac{1 + i_{BCP5}}{1 + r_{BCU5}} - 1\n$$\n\n"
            f"{m.group(2)}\n\n"
            "$$\ni_{pd} = \\frac{1 + i_{BCP10}}{1 + r_{BCU10}} - 1\n$$\n\n"
            f"{m.group(3)}\n\n"
            "$$\ni_{sq} = \\frac{(1 + i_{pd})^2}{1 + i_{pq}} - 1\n$$\n\n"
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
            "$$\nUF_t = UF_0 \\cdot \\left(1 + i_{jq}\\right)^{t/12}"
            "\\quad \\text{donde } j = p \\text{ si } t \\leq 60,\\; j = s \\text{ si } t > 60\n$$\n\n"
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
            "$$\nDM = \\frac{D_t}{1 + r_0}\n$$\n\n"
            "$$\nD_t = \\frac{\\sum_{t} \\frac{t \\cdot C_t}{(1+r_0)^t}}"
            "{\\sum_{t} \\frac{C_t}{(1+r_0)^t}}\n$$\n\n"
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

# ─── CIR 1512 formula patches ───────────────────────────────────────────────
# U+F053 is the Symbol-font private-use Sigma (Σ) used throughout CIR 1512.
_SIG = "\uf053"

_CIR_1512_FORMULA_PATCHES = [
    # Ak = ΣΣ FAji  (flows of eligible assets per tranche)
    (
        re.compile(
            r"(de acuerdo a la siguiente fórmula:)\s*\n"
            r"Ak\s*=\s*" + _SIG + r"\s*" + _SIG + r"\s*FAji\s*\n"
            r"todo i en todo j\s*\n"
            r"el tramo K\s*\n"
            r"(donde:)",
        ),
        lambda m: (
            f"{m.group(1)}\n\n"
            "$$\nA_k = \\sum_{j} \\sum_{i \\in \\text{tramo K}} FA_{ji}\n$$\n\n"
            f"{m.group(2)}"
        ),
    ),
    # Bk = ΣΣ FPNji  (net insurance liability flows per tranche)
    (
        re.compile(
            r"(de acuerdo a\nla siguiente fórmula:|de acuerdo a la siguiente fórmula:)\s*\n"
            r"Bk\s*=\s*" + _SIG + r"\s*" + _SIG + r"\s*FPNji\s*\n"
            r"todo i en todo j\s*\n"
            r"el tramo K\s*\n"
            r"(donde:)",
        ),
        lambda m: (
            f"{m.group(1).replace(chr(10), ' ')}\n\n"
            "$$\nB_k = \\sum_{j} \\sum_{i \\in \\text{tramo K}} FPN_{ji}\n$$\n\n"
            f"{m.group(2)}"
        ),
    ),
    # CK = ΣΣ FPFji  (financial liability flows per tranche)
    (
        re.compile(
            r"(de acuerdo a la siguiente fórmula:)\s*\n"
            r"CK\s*=\s*" + _SIG + r"\s*" + _SIG + r"\s*FPFji\s*\n"
            r"todo i en\s*todo j\s*\n"
            r"el tramo k\s*\n"
            r"(donde:)",
        ),
        lambda m: (
            f"{m.group(1)}\n\n"
            "$$\nC_K = \\sum_{j} \\sum_{i \\in \\text{tramo k}} FPF_{ji}\n$$\n\n"
            f"{m.group(2)}"
        ),
    ),
    # VPPj = ΣΣ FPji × [...] (policy present value — double sum over tranches and periods)
    (
        re.compile(
            r"tramo k = 10\s*\n"
            r"VPPj\s*=\s*" + _SIG + r"\s*" + _SIG + r"\s*FPji x \(\(1\+TMj\)-i x CPk,j \+ \(1\.03\)-i x \(1 -CPk,j\)\)\s*\n"
            r"tramo k = i todo i en\s*\n"
            r"el tramo k\s*\n"
            r"(en que:)",
        ),
        lambda m: (
            "$$\n"
            "VPP_j = \\sum_{k=1}^{10} \\sum_{i \\in \\text{tramo k}} FP_{ji} \\cdot "
            "\\left[(1+TM_j)^{-i} \\cdot CP_{k,j} + (1{,}03)^{-i} \\cdot (1-CP_{k,j})\\right]\n"
            "$$\n\n"
            f"{m.group(1)}"
        ),
    ),
    # VPPj = Σ FPji × (1+TVj)^-i  (policy present value using sale rate)
    (
        re.compile(
            r"(utilizando la siguiente expresión:)\s*\n"
            r"VPPj\s*=\s*" + _SIG + r"\s*FPji x \(1 \+ TVj\)-1\s*\n"
            r"todo i\s*\n"
            r"(donde:)",
        ),
        lambda m: (
            f"{m.group(1)}\n\n"
            "$$\nVPP_j = \\sum_{i} FP_{ji} \\cdot (1 + TV_j)^{-i}\n$$\n\n"
            f"{m.group(2)}"
        ),
    ),
    # PUj = Σ FPji × (1+TVj)^-i  (single premium equals sum of discounted flows)
    (
        re.compile(
            r"(que cumple la siguiente condición:)\s*\n"
            r"PUj\s*=\s*" + _SIG + r"\s*FPji x \(1 \+ TVj\)-1\s*\n"
            r"todo i\s*\n"
            r"(Por definición)",
        ),
        lambda m: (
            f"{m.group(1)}\n\n"
            "$$\nPU_j = \\sum_{i} FP_{ji} \\cdot (1 + TV_j)^{-i}\n$$\n\n"
            f"{m.group(2)}"
        ),
    ),
    # VPPj = Σ FPji × (1+TCj)^-i  (policy present value using equivalent cost rate)
    (
        re.compile(
            r"(determinará una \"tasa de costo de emisión equivalente\" \(TCj\), tal que:)\s*\n"
            r"VPPj\s*=\s*" + _SIG + r"\s*FPji x \(1 \+ TCj\)-1\s*\n"
            r"todo i\s*\n"
            r"(De tal modo)",
        ),
        lambda m: (
            f"{m.group(1)}\n\n"
            "$$\nVPP_j = \\sum_{i} FP_{ji} \\cdot (1 + TC_j)^{-i}\n$$\n\n"
            f"{m.group(2)}"
        ),
    ),
    # VPP' = ΣΣΣ FPji × [...] (adjusted reserve — triple sum)
    (
        re.compile(
            r"tramo k = 10\s*\n"
            r"VPP`\s*=\s*" + _SIG + r"\s*" + _SIG + r"\s*" + _SIG + r"\s*FPji x \(\(1\+TMj\)-i x CPk \+ \(1\.03\)-i x \(1 - CPk\)\)\s*\n"
            r"todo j tramo k = i todo i en el tramo k\s*\n"
            r"(en que:)",
        ),
        lambda m: (
            "$$\n"
            "VPP' = \\sum_{j} \\sum_{k=1}^{10} \\sum_{i \\in \\text{tramo k}} FP_{ji} \\cdot "
            "\\left[(1+TM_j)^{-i} \\cdot CP_k + (1{,}03)^{-i} \\cdot (1-CP_k)\\right]\n"
            "$$\n\n"
            f"{m.group(1)}"
        ),
    ),
    # Mensualización fraction formula  (mortality rate proportional distribution)
    # After extraction the fraction is split: numerator stays as text, denominator
    # becomes a markdown table (pdfplumber detects the fraction grid as a table).
    # Raw post-extraction:
    #   "a través de la siguiente formula:\nA\ny*q\nX\n\n| q m |\n| --- |\n| (x/y )+i |\n\nx\nDonde,"
    (
        re.compile(
            r"(a través de la siguiente formula:)\s*\n"
            r"A\s*\ny\*q\s*\nX\s*\n\n"
            r"\| q m \|\n\| --- \|\n\| \(x/y \)\+i \|\n"
            r"x\s*\n"
            r"(Donde,)",
        ),
        lambda m: (
            f"{m.group(1)}\n\n"
            "$$\n"
            "q^m_{(x/y)+i} = \\frac{y \\cdot {}^{A}q_x}{1 - i \\cdot y \\cdot {}^{A}q_x}\n"
            "$$\n\n"
            f"{m.group(2)}"
        ),
    ),
]


def patch_document(text: str, source_file: str) -> str:
    """Apply document-specific patches for known garbled content."""
    if "ncg_209" in source_file.lower():
        # Replace garbled Internacional table block
        text = _INTERNACIONAL_BLOCK_RE.sub(
            _INTERNACIONAL_TABLE + "\n\n", text
        )
        # Apply NCG 209 formula reconstructions
        for pattern, replacement in _FORMULA_PATCHES:
            text = pattern.sub(replacement, text)
        # Fix truncated leasing default table header (pdfplumber misses table start)
        text = text.replace(
            "| aso en el pago de cuotas | % de castigo en flujos |",
            "| Meses de atraso en el pago de cuotas | % de castigo en flujos |",
        )

    if "cir_1512" in source_file.lower():
        for pattern, replacement in _CIR_1512_FORMULA_PATCHES:
            text = pattern.sub(replacement, text)

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
    # 0. Collapse mid-sentence page-break blank lines before anything else.
    full_text = merge_cross_page_continuation(full_text)
    # 0b. Strip REF.: block from body if it was extracted as the document title
    #     (avoids duplicating the heading in body text).
    if document_title and not _PAGE_HEADER_RE.search(document_title):
        full_text = re.sub(
            r"REF\.\s*:\s*.+?(?=\n(?:Para |Esta |[A-Z][a-záéíóúñü]))",
            "",
            full_text,
            count=1,
            flags=re.DOTALL,
        )
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

