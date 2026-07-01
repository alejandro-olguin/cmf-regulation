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
import json
import logging
import os
import re
import sys
import time
import unicodedata
from pathlib import Path
from typing import Any
from urllib import error as urllib_error
from urllib import request as urllib_request

import pdfplumber

INPUT_DIR = Path("pdf")
OUTPUT_DIR = Path("markdown")
DEFAULT_LLM_AUDIT_CHUNK_LINES = 80
DEFAULT_LLM_AUDIT_OVERLAP_LINES = 10
DEFAULT_LLM_AUDIT_SLEEP_SECONDS = 5.0
DEFAULT_GEMINI_MODEL = "gemini-2.0-flash"
DEFAULT_GEMINI_MAX_RETRIES = 3

def _load_local_settings() -> dict[str, Any]:
    """Load optional local settings from .env and config.local.json."""
    settings: dict[str, Any] = {}

    config_path = Path("config.local.json")
    if config_path.exists():
        try:
            payload = json.loads(config_path.read_text(encoding="utf-8"))
        except Exception as exc:
            log.warning("Ignoring unreadable %s: %s", config_path.name, exc)
        else:
            if isinstance(payload, dict):
                settings.update(payload)

    env_path = Path(".env")
    if env_path.exists():
        try:
            for raw_line in env_path.read_text(encoding="utf-8").splitlines():
                line = raw_line.strip()
                if not line or line.startswith("#") or "=" not in line:
                    continue
                key, value = line.split("=", 1)
                key = key.strip()
                value = value.strip().strip('"').strip("'")
                if key and key not in os.environ:
                    os.environ[key] = value
        except Exception as exc:
            log.warning("Ignoring unreadable %s: %s", env_path.name, exc)

    return settings

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
    r"(?:NORMA DE CAR[ÁA]CTER GENERAL\s*N[°º]\s*:?\s*[\d.]+|"
    r"CIRCULAR\s*N[°º]\s*:?\s*[\d.]+(?:\s*[\w\s]*?)?)\s*\n"
    r"FECHA\s*:?\s*\d{1,2}\.\d{1,2}\.\d{2,4}\s*\n?",
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


def extract_document_title(first_page_text: str, source_file: str | None = None) -> str | None:
    """Extract the document title from the first-page header pattern.

    Priority:
    1. Standard CMF/SVS page header (CIRCULAR or NORMA DE CARÁCTER GENERAL)
       combined with the REF.: description when available.
    2. REF.: line only — used when no repeating standard header is present.
    3. Minimal title derived from the file name — last-resort fallback for
       compendium / recopilation documents that carry no header or REF line.
    """
    m = _PAGE_HEADER_RE.search(first_page_text)

    # Try to find REF.: for a more descriptive title. The marker appears as
    # "REF.:", "REF :" or "REF:" across different document eras, so the period
    # and surrounding spaces are optional.
    ref_m = re.search(
        r"REF\s*\.?\s*:\s*(.+?)(?=\n(?:Para |Esta |[A-Z][a-záéíóúñü]))",
        first_page_text,
        re.DOTALL,
    )
    ref_title = None
    if ref_m:
        # Strip a trailing footnote/page number (1-3 digits) but preserve a
        # legitimate 4-digit year that is part of the title (e.g. "... AGOSTO DE 1988").
        ref_title = re.sub(r"\s+\d{1,3}\s*$", "", ref_m.group(1).strip())
        ref_title = re.sub(r"\s+", " ", ref_title).strip()

    if m:
        header = m.group(0).strip()
        num_m = re.search(r"N[°º]\s*:?\s*([\d.]+)", header)
        num = num_m.group(1).replace(".", "") if num_m else None
        prefix = "CIRCULAR N°" if "CIRCULAR" in header else "NCG N°"
        if ref_title:
            # Trim REF title at first sentence break (period + space) to drop
            # DEROGA clauses and addressee, without splitting numeric periods
            # such as "19.083" or law/decree numbers. REF text sometimes opens
            # with an enumerator ("1. REGULA ... 2.- DEROGA ..."); strip the
            # leading enumerator and cut before the next one.
            short_ref = re.sub(r"^\s*\d+\s*\.\-?\s*", "", ref_title)
            short_ref = re.split(r"\s+\d+\s*\.\-?\s+", short_ref, maxsplit=1)[0].strip()
            short_ref = re.split(r"\.\s", short_ref, maxsplit=1)[0].strip()
            # Drop a trailing DEROGA/MODIFICA clause when it follows real content
            # (but keep it when the whole REF *is* the derogation, e.g. a pure
            # "DEROGA CIRCULAR N° 1127" circular).
            clause = re.search(
                r"\s+(?:Y\s+|,\s*)?(?:DEROGA|MODIFICA|COMPLEMENTA|REEMPLAZA|SUSTITUYE)\b",
                short_ref,
            )
            if clause and clause.start() > 0:
                short_ref = short_ref[: clause.start()].strip()
            # Strip a dangling connector left by a truncated date/reference
            # (e.g. "... N° 3.500, DE" -> "... N° 3.500").
            short_ref = re.sub(r"[,;\s]+(?:DE|DEL|N[°º][\d.\s]*)\s*$", "", short_ref).strip()
            return f"{prefix} {num} — {short_ref}" if num else short_ref
        # No REF description: return the document reference WITHOUT the FECHA
        # line (which must never appear in the title).
        if num:
            return f"{prefix} {num}"
        return re.split(r"\s*\n?FECHA", header)[0].strip().replace("\n", " ")

    # Pure fallback: no repeating header, use REF.: only
    if ref_title:
        return ref_title

    # Last resort: derive a minimal reference title from the file name so that
    # compendium / recopilation documents (no header, no REF) still get an H1.
    if source_file:
        fn = re.match(r"(cir|ncg)_(\d+)_", source_file.lower())
        if fn:
            prefix = "CIRCULAR N°" if fn.group(1) == "cir" else "NCG N°"
            return f"{prefix} {int(fn.group(2))}"
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
            cell = cell.replace("\n", " ").strip()
            # Drop stray leading/trailing ruling pipes that pdfplumber sometimes
            # captures as cell text (they would otherwise become escaped \| and
            # break column counts).
            cell = cell.strip("|").strip()
            cell = cell.replace("|", "\\|")
            cells.append(cell)
        rows.append(cells)

    if not rows:
        return ""

    # Skip tables with no textual content at all (pdfplumber sometimes detects a
    # ruling-only grid with empty cells, which would emit a noise table).
    if not any(cell for row in rows for cell in row):
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
            else:
                # Grid detected but every cell was empty: recover any raw text
                # in the table region instead of emitting an empty table.
                region = page.crop((x0, top, x1, bottom))
                rtxt = region.extract_text()
                if rtxt and rtxt.strip():
                    parts.append(rtxt.strip())

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
    # Remove stray lone-pipe lines (vertical rulings misread as text).
    text = re.sub(r"(?m)^[ \t]*\|[ \t]*$\n?", "", text)
    return re.sub(r"\n{3,}", "\n\n", text)


# ─────────────────────────────────────────────────────────────────────────────
# Symbol font (Windows PUA U+F000–U+F0FF) → Unicode math character mapping
# ─────────────────────────────────────────────────────────────────────────────

# Maps the most common Symbol-font private-use chars to their Unicode math
# equivalents.  Run this AFTER document-specific patches (which may key on the
# raw PUA codepoints) and BEFORE equation detection (so the detector sees
# proper Unicode operators rather than opaque PUA characters).
_SYMBOL_FONT_MAP: dict[str, str] = {
    "\uf020": " ",       # space (Symbol 0x20)
    "\uf021": "\u2200",  # ∀  for all
    "\uf024": "\u2203",  # ∃  there exists
    "\uf028": "(",
    "\uf029": ")",
    "\uf02a": "\u00d7",  # ×  multiplication
    "\uf02b": "+",
    "\uf02c": ",",
    "\uf02d": "\u2212",  # −  minus sign
    "\uf02e": ".",
    "\uf02f": "/",
    "\uf030": "0", "\uf031": "1", "\uf032": "2", "\uf033": "3",
    "\uf034": "4", "\uf035": "5", "\uf036": "6", "\uf037": "7",
    "\uf038": "8", "\uf039": "9",
    "\uf03a": ":", "\uf03b": ";", "\uf03c": "<", "\uf03d": "=", "\uf03e": ">",
    # Greek uppercase
    "\uf041": "\u0391", "\uf042": "\u0392", "\uf043": "\u03a7",
    "\uf044": "\u0394", "\uf045": "\u0395", "\uf046": "\u03a6",
    "\uf047": "\u0393", "\uf048": "\u0397", "\uf049": "\u0399",
    "\uf04b": "\u039a", "\uf04c": "\u039b", "\uf04d": "\u039c",
    "\uf04e": "\u039d", "\uf04f": "\u039f", "\uf050": "\u03a0",
    "\uf051": "\u0398", "\uf052": "\u03a1", "\uf053": "\u03a3",
    "\uf054": "\u03a4", "\uf055": "\u03a5", "\uf056": "\u03c2",
    "\uf057": "\u03a9", "\uf058": "\u039e", "\uf059": "\u03a8",
    "\uf05a": "\u0396", "\uf05b": "[", "\uf05d": "]",
    # Greek lowercase
    "\uf061": "\u03b1", "\uf062": "\u03b2", "\uf063": "\u03c7",
    "\uf064": "\u03b4", "\uf065": "\u03b5", "\uf066": "\u03c6",
    "\uf067": "\u03b3", "\uf068": "\u03b7", "\uf069": "\u03b9",
    "\uf06b": "\u03ba", "\uf06c": "\u03bb", "\uf06d": "\u03bc",
    "\uf06e": "\u03bd", "\uf06f": "\u03bf", "\uf070": "\u03c0",
    "\uf071": "\u03b8", "\uf072": "\u03c1", "\uf073": "\u03c3",
    "\uf074": "\u03c4", "\uf075": "\u03c5", "\uf077": "\u03c9",
    "\uf078": "\u03be", "\uf079": "\u03c8", "\uf07a": "\u03b6",
    "\uf07b": "{", "\uf07c": "|", "\uf07d": "}",
    # Math operators and relations
    "\uf0a3": "\u2264",  # ≤
    "\uf0a5": "\u221e",  # ∞
    "\uf0b0": "\u00b0",  # °
    "\uf0b1": "\u00b1",  # ±
    "\uf0b3": "\u2265",  # ≥
    "\uf0b4": "\u00d7",  # ×
    "\uf0b6": "\u2202",  # ∂
    "\uf0b7": "\u00b7",  # ·
    "\uf0b8": "\u00f7",  # ÷
    "\uf0b9": "\u2260",  # ≠
    "\uf0ba": "\u2261",  # ≡
    "\uf0bb": "\u2248",  # ≈
    "\uf0bc": "\u2026",  # …
    "\uf0a7": "\u2022",  # •  list bullet (Symbol 0xA7)
    "\uf0ae": "\u2192",  # →  right arrow (Symbol 0xAE)
    "\uf0d8": "\u2022",  # •  list bullet
    "\uf0ef": "\u2022",  # •  list bullet
    "\uf0c6": "\u2205",  # ∅
    "\uf0c7": "\u2229",  # ∩
    "\uf0c8": "\u222a",  # ∪
    "\uf0c9": "\u2283",  # ⊃
    "\uf0ca": "\u2287",  # ⊇
    "\uf0cb": "\u2284",  # ⊄
    "\uf0cc": "\u2282",  # ⊂
    "\uf0cd": "\u2286",  # ⊆
    "\uf0ce": "\u2208",  # ∈
    "\uf0cf": "\u2209",  # ∉
    "\uf0d5": "\u220f",  # ∏
    "\uf0d6": "\u221a",  # √
    "\uf0d7": "\u22c5",  # ⋅
    "\uf0d9": "\u2227",  # ∧
    "\uf0da": "\u2228",  # ∨
    "\uf0e5": "\u2211",  # ∑  (summation)
    # Large bracket/paren/brace components — these are purely structural in the
    # old Symbol font layout model; replace with empty strings so the surrounding
    # formula text remains readable without garbage characters.
    "\uf0e6": "", "\uf0e7": "", "\uf0e8": "",   # large ( top/mid/bot
    "\uf0e9": "", "\uf0ea": "", "\uf0eb": "",   # large [ top/mid/bot
    "\uf0ec": "", "\uf0ed": "", "\uf0ee": "",   # large { top/mid/bot
    "\uf0f0": "", "\uf0f1": "", "\uf0f2": "",
    "\uf0f3": "", "\uf0f4": "", "\uf0f5": "",
    "\uf0f6": "", "\uf0f7": "", "\uf0f8": "",   # large ) top/mid/bot
    "\uf0f9": "", "\uf0fa": "", "\uf0fb": "",   # large ] top/mid/bot
    "\uf0fc": "", "\uf0fd": "", "\uf0fe": "",   # large } top/mid/bot
    "\uf0ff": "",
}


def map_symbol_font_chars(text: str) -> str:
    """Replace Symbol-font PUA chars with their Unicode math equivalents.

    Must be called *after* patch_document() (which may match on raw PUA bytes)
    and *before* detect_and_flag_equations() so the detector sees proper
    Unicode operators instead of opaque private-use codepoints.
    """
    for old, new in _SYMBOL_FONT_MAP.items():
        if old in text:
            text = text.replace(old, new)
    return text


# Mathematical Alphanumeric Symbols (U+1D400–U+1D7FF): math-italic/bold variable
# names and digits that PDFs embed in running prose. NFKC folds each to its plain
# ASCII equivalent (e.g. 𝐶→C, 𝑘→k, 𝟎→0), keeping body text readable.
_MATH_ALNUM_MAP: dict[int, str] = {
    c: unicodedata.normalize("NFKC", chr(c))
    for c in range(0x1D400, 0x1D800)
    if unicodedata.normalize("NFKC", chr(c)) != chr(c)
}


def normalize_math_alphanumeric(text: str) -> str:
    """Fold Unicode math-alphanumeric symbols to plain ASCII letters/digits.

    Run *after* equation detection (which uses the math-italic range as a signal)
    so the flagging still works, while the emitted text stays legible.
    """
    return text.translate(_MATH_ALNUM_MAP)


# ─────────────────────────────────────────────────────────────────────────────
# Equation fragment detection  (must run BEFORE line re-joining)
# ─────────────────────────────────────────────────────────────────────────────

_MATH_CHARS = frozenset("+-*/=^∑∫√≤≥≠∞∆−×÷⋅∏∂∈⊂⊃∪∩≈∧∨±°")

# Block-level check: a run of fragments is only flagged as an equation when the
# combined block text contains at least one real mathematical indicator.
# This prevents kerned table headers and footnote reference numbers from being
# wrapped in ⚠️ formula blocks.
_REAL_MATH_BLOCK_RE = re.compile(
    r"[∑∏∫√∆∂∈⊂⊃∪∩≈∧∨≤≥≠\u2212\u00d7÷⋅∞±²³\u03b1-\u03c9\u0391-\u03a9]"  # Unicode math / Greek (° excluded — used as N° in Spanish)
    r"|[\U0001D400-\U0001D7FF]"  # Unicode math italic/bold/script
    r"|[a-zA-Z0-9]\s*=\s*[a-zA-Z0-9(\\]"  # assignment: x = expr
    r"|[0-9]\s+[+\-]\s+[0-9]"  # digit SPACE ± SPACE digit (avoids matching ranges like 1-13)
    r"|[a-zA-Z]\s*\*\s*[0-9]"  # variable × digit (e.g. I*100)
    r"|[0-9]\s*\*\s*[a-zA-Z0-9(]"  # digit × expr
    r"|[\uf000-\uf0ff]",  # any remaining Symbol-font PUA chars (not yet mapped)
    re.UNICODE,
)


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
                block_text = "\n".join(block)
                if _REAL_MATH_BLOCK_RE.search(block_text):
                    # Real equation fragments — wrap in ⚠️ warning block
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
                else:
                    # False positive (kerned table header, footnote ref number,
                    # financial form field code, etc.) — emit lines as-is so
                    # subsequent rejoin/heading stages can handle them normally.
                    for b in block:
                        if b:
                            result.append(b)
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

        # Drop repeated page chrome that survives extraction as a standalone
        # institutional line. These are not document headings.
        if re.fullmatch(r"SUPERINTENDENCIA DE VALORES Y SEGUROS|COMISI[ÓO]N PARA EL MERCADO FINANCIERO", s):
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


# ─── CIR 1476 — Makeham mortality model ─────────────────────────────────────
# Annual survival probability: p_x = s · g^(c^x · (c-1))
# Monthly survival:            p_x = s^t · g^(c^(xt) · (c^t - 1))
# Parameter tables M-95 for males and females.
_CIR_1476_PATCHES = [
    # Annual Makeham formula: fragments "( cx⋅(c−1))\np = s⋅ g\nx"
    (
        re.compile(
            r"\(\s*cx\s*[⋅·\*]\s*\(c\s*[−\-]\s*1\)\s*\)\s*\n"
            r"p\s*=\s*s\s*[⋅·\*]\s*g\s*\n"
            r"x",
        ),
        lambda m: "$$\np_x = s \\cdot g^{c^x \\cdot (c-1)}\n$$",
    ),
    # Monthly Makeham formula: fragments "( ( ))\np = st ⋅ g cxt⋅ct−1\nx"
    (
        re.compile(
            r"\(\s*\(\s*\)\s*\)\s*\n"
            r"p\s*=\s*s\s*t\s*[⋅·\*]\s*g\s*cxt\s*[⋅·\*]\s*ct\s*[−\-]\s*1\s*\n"
            r"x",
        ),
        lambda m: "$$\np_x = s^t \\cdot g^{c^{xt} \\cdot (c^t-1)}\n$$",
    ),
]

# ─── NCG 207 — Nelson-Siegel yield curve & Gompertz mortality ────────────────
_NCG_207_PATCHES = [
    # Gompertz mortality: fragments "q\n=\n1\n- e(- e(a+bx))" on same or adjacent lines
    (
        re.compile(
            r"\bq\s*\n=\s*\n1\s*\n-?\s*e\s*\(\s*-\s*e\s*\(a\s*\+\s*bx\s*\)\s*\)",
            re.DOTALL,
        ),
        lambda m: "$$\nq_x = 1 - e^{-e^{a+bx}}\n$$",
    ),
    # Short fragmented form: "q\n=\n1\n-\ne" → just flag minimal LaTeX
    (
        re.compile(r"\bq\s*\n=\s*\n1\s*\n-\s*\ne\s*\n"),
        lambda m: "$$\nq_x = 1 - e^{-e^{a+bx}}\n$$\n",
    ),
    # Nelson-Siegel: "Yield[t]= a+bexp(−ωt)+cexp(−ωt)" (usually on one line)
    (
        re.compile(
            r"Yield\[t\]\s*=\s*a\s*\+\s*b\s*exp\s*\([^)]+\)\s*\+\s*c\s*exp\s*\([^)]+\)\s*\n"
            r"1\s*2",
        ),
        lambda m: "$$\nYield(t) = a + b_1 \\cdot e^{-\\omega_1 t} + c_2 \\cdot e^{-\\omega_2 t}\n$$",
    ),
]

# ─── NCG 148 — Actuarial loss model (EWMA) ──────────────────────────────────
_NCG_148_PATCHES = [
    # Parameter block: "a = 5.701\nb = -3.778\nc = -1.595."
    (
        re.compile(
            r"(a\s*=\s*5[\.\,]\d+)\s*\n"
            r"(b\s*=\s*-\s*3[\.\,]\d+)\s*\n"
            r"(c\s*=\s*-\s*1[\.\,]\d+\.?)\s*\n",
        ),
        lambda m: (
            "$$\n"
            f"{m.group(1).strip()}, \\quad "
            f"{m.group(2).strip()}, \\quad "
            f"{m.group(3).rstrip('.')}\n"
            "$$\n\n"
        ),
    ),
    # EWMA mean+variance: "m = 1 − λr + λm\n...\nh = (1 − λ)(r − m)^2 + λh"
    (
        re.compile(
            r"\(\s*\)\s*\n"
            r"(m\s*=\s*1\s*[−\-]\s*\S+r\s*\+\s*\S+m)\s*\n"
            r"(x:t\s+x:t\s+x:t[−\-]1)\s*\n"
            r"(h\s*=\s*\(\s*1\s*[−\-]\s*\S+\s*\)\s*\(r\s*[−\-]\s*m\s*\)2\s*\+\s*\S+h)",
            re.DOTALL,
        ),
        lambda m: (
            "$$\n"
            "m_{x:t} = (1 - \\lambda) \\cdot r_{x:t} + \\lambda \\cdot m_{x:t-1}\n\n"
            "h_{x:t} = (1 - \\lambda)(r_{x:t} - m_{x:t})^2 + \\lambda \\cdot h_{x:t-1}\n"
            "$$\n\n"
        ),
    ),
]

# ─── Documents sharing the EC = Σ summation formula ─────────────────────────
# cir_2248, cir_2250, cir_2265, cir_2281 all use these credit-equivalent formulas.
# Raw extraction order (before Symbol mapping): symbol first, then sub/superscripts below.
# Negative netting case: "E C = \uf0e5\ni\nn\n= 1\nN o c\ni\n\uf0b4 F C\ni\n\uf0b4 0 , 4"
# Positive netting case: single-line extraction, usually not fragmented.
_EC_SUMA_PATCHES = [
    # Negative/zero netting case (default x_tolerance=3 extraction):
    # "E C =\nn\n∑i=\n1\nN o c\ni\n× F C\ni\n× 0 , 4"
    (
        re.compile(
            r"E\s*C\s*=\s*\n"
            r"n\s*\n"
            r"[\uf0e5∑\u2211]i\s*=\s*\n"
            r"1\s*\n"
            r"N\s*o\s*c\s*\n"
            r"i\s*\n"
            r"[\uf0b4×\u00d7]\s*F\s*C\s*\n"
            r"i\s*\n"
            r"[\uf0b4×\u00d7]\s*0\s*[,.]?\s*4",
        ),
        lambda m: "$$\nEC = \\sum_{i=1}^{n} Noc_i \\times FC_i \\times 0{,}4\n$$",
    ),
]

# ─── CIR 2249 / CIR 2243 — Provisión por riesgo de crédito ──────────────────
# Provisión_deudor = (EAP − EA) × (PI_deudor/100) × (PDI_deudor/100)
#                   + EA × (PI_aval/100) × (PDI_aval/100)
# Raw extraction (x_tol=1) has kerned subscript words on separate lines.
_PROVISION_DEUDOR_PATCHES = [
    (
        re.compile(
            r"P\s*r\s*o\s*v\s*i\s*s\s*i\s*[oó]\s*n\s*\n"
            r"d\s*e?\s*u\s*d\s*o\s*r\s*\n"
            r"=\s*\(\s*E\s*A\s*P\s*[−\-]\s*E\s*A\s*\)\s*[\uf0b4×\u00d7]\s*\(\s*P\s*I\s*\n"
            r"d\s*e?\s*u\s*d\s*o\s*r\s*\n"
            r"/\s*1\s*0\s*0\s*\)\s*[\uf0b4×\u00d7]\s*\(\s*P\s*D\s*I\s*\n"
            r"d\s*e?\s*u\s*d\s*o\s*r\s*\n"
            r"/\s*1\s*0\s*0\s*\)\s*\+\s*E\s*A\s*[\uf0b4×\u00d7]\s*\(\s*P\s*I\s*\n"
            r"a\s*v(?:\s*/\s*)?\s*a\s*l\s*\n"
            r"/?\s*1\s*0\s*0\s*\)\s*[\uf0b4×\u00d7]\s*\(\s*P\s*D\s*I\s*\n"
            r"a\s*v(?:\s*/\s*)?\s*a\s*l\s*\n"
            r"/?\s*1\s*0\s*0\s*\)",
        ),
        lambda m: (
            "$$\n"
            "Provisi\\acute{o}n_{deudor} = (EAP - EA) \\times \\frac{PI_{deudor}}{100} "
            "\\times \\frac{PDI_{deudor}}{100} + EA \\times \\frac{PI_{aval}}{100} "
            "\\times \\frac{PDI_{aval}}{100}\n"
            "$$"
        ),
    ),
]

# ─── CIR 2281 — Bond duration (Macaulay) and risk exposure formulas ──────────
# After Symbol mapping, blocks look like:
# "𝑀 = ∑𝑡⋅𝐶𝐹_𝑡 /∑𝐶𝐹_𝑡\n𝑡 𝑡\n𝑡 𝑡"
_CIR_2281_PATCHES = [
    (
        re.compile(
            r"(\U0001D440\s*=\s*[∑\u2211]\U0001D461\s*[⋅·]\s*\U0001D436\U0001D439\s*"
            r"/\s*[∑\u2211]\s*\U0001D436\U0001D439)\s*\n"
            r"(\S+\s+\S+)\s*\n"
            r"(\S+\s+\S+)",
            re.DOTALL,
        ),
        lambda m: "$$\nM = \\frac{\\sum_{t} t \\cdot CF_t}{\\sum_{t} CF_t}\n$$",
    ),
]

# ─── NCG 306 — Insurance reserving formulas ──────────────────────────────────
# Annual siniestralidad and ratio de gastos fraction formulas, development
# factors FA and TS ratios.
_NCG_306_PATCHES = [
    # Siniestralidad fraction (two-line: numerator / denominator)
    (
        re.compile(
            r"Siniestralidad\s*=\s*\n"
            r"(Siniestros pagados[^\n]+)\s*\n"
            r"(Prima retenida[^\n]+)\s*\n",
        ),
        lambda m: (
            "$$\n"
            "\\text{Siniestralidad} = \\frac{\\text{Siniestros pagados}}"
            "{\\text{Prima retenida neta de anulaciones}}\n"
            "$$\n\n"
        ),
    ),
    # Ratio de gastos fraction
    (
        re.compile(
            r"Ratio de gastos\s*\n"
            r"(Gastos de explotaci[oó]n[^\n]+)\s*\n"
            r"=\s*\n"
            r"(Prima retenida[^\n]+)\s*\n",
        ),
        lambda m: (
            "$$\n"
            "\\text{Ratio de gastos} = \\frac{\\text{Gastos de explotación} - "
            "\\text{Gastos a cargo de reaseguradores}}{\\text{Prima retenida neta de anulaciones}}\n"
            "$$\n\n"
        ),
    ),
    # TSa = Σ SIai / Σ Pai
    (
        re.compile(
            r"[\uf0e5∑\u2211]\s*\n"
            r"\U0001D461\U0001D44E\s*\n"
            r"SI\s*\n"
            r"TS\s*=\s*i=1\s*ai\s*\n"
            r"a\s*\n"
            r"[\uf0e5∑\u2211]\s*\n"
            r"\U0001D461\U0001D44E\s*\n"
            r"P\s*\n"
            r"i=1\s*ai",
            re.DOTALL,
        ),
        lambda m: "$$\nTS_a = \\frac{\\sum_{i=1}^{t_a} SI_{a,i}}{\\sum_{i=1}^{t_a} P_{a,i}}\n$$",
    ),
    # FA = ∏ FI (product of incremental development factors)
    (
        re.compile(
            r"(?:FA\s*=\s*[\uf0d5∏\u220f]FI|FA\s*=\s*[\uf0d5∏\u220f]\s*FI)\s*\n"
            r"t\s*r\s*\n"
            r"r=t",
        ),
        lambda m: "$$\nFA_t = \\prod_{r=t}^{N-1} FI_r\n$$",
    ),
]

# ─── NCG 243 — Actuarial pension obligation formulas ─────────────────────────
# The PDF uses Unicode math italic (𝑅, 𝑃𝑃𝐼𝑇, etc.) for variables.
# Lines in the PDF are properly Unicode but get fragmented by pdfplumber.
# We patch the main summary formula (page 7) and the actuarial annuity (page 8).
_NCG_243_PATCHES = [
    # Main composite formula
    (
        re.compile(
            r"(\U0001D445\s*=[∑\u2211][∑\u2211]\[.+?G1\U0001D456\U0001D445\s*\]\])\s*\n"
            r"(\U0001D456=1\U0001D457=1)",
            re.DOTALL,
        ),
        lambda m: (
            "$$\n"
            + m.group(1).strip() + "\n"
            + "\\quad i=1\\ldots10,\\; j=1\\ldots6\n"
            "$$"
        ),
    ),
]


# ─── CIR 1058 — Loan amortisation (present value of annuity) formula ─────────
# The consolidated debt equals the annual instalment R times the present-value
# annuity factor. In the PDF the numerator "1 - (1 + 0,01)-10" sits above the
# denominator "0,01" on the next line, forming a fraction.
_CIR_1058_PATCHES = [
    (
        re.compile(
            r"75,77\s*=\s*R\s*\*\s*1\s*-\s*\(\s*1\s*\+\s*0,01\s*\)\s*-?10\s*\n"
            r"0,01\s*\n",
        ),
        lambda m: "$$\n75{,}77 = R \\cdot \\frac{1 - (1 + 0{,}01)^{-10}}{0{,}01}\n$$\n",
    ),
]


def patch_document(text: str, source_file: str) -> str:
    """Apply document-specific patches for known garbled content."""
    if "cir_1058" in source_file.lower():
        for pattern, replacement in _CIR_1058_PATCHES:
            text = pattern.sub(replacement, text)

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

    if "cir_1476" in source_file.lower():
        for pattern, replacement in _CIR_1476_PATCHES:
            text = pattern.sub(replacement, text)

    if "ncg_207" in source_file.lower():
        for pattern, replacement in _NCG_207_PATCHES:
            text = pattern.sub(replacement, text)

    if "ncg_148" in source_file.lower():
        for pattern, replacement in _NCG_148_PATCHES:
            text = pattern.sub(replacement, text)

    if any(x in source_file.lower() for x in ["cir_2248", "cir_2249", "cir_2250", "cir_2265", "cir_2281"]):
        for pattern, replacement in _EC_SUMA_PATCHES:
            text = pattern.sub(replacement, text)

    if any(x in source_file.lower() for x in ["cir_2249", "cir_2243"]):
        for pattern, replacement in _PROVISION_DEUDOR_PATCHES:
            text = pattern.sub(replacement, text)

    if "cir_2281" in source_file.lower():
        for pattern, replacement in _CIR_2281_PATCHES:
            text = pattern.sub(replacement, text)

    if "ncg_306" in source_file.lower():
        for pattern, replacement in _NCG_306_PATCHES:
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


def _chunk_lines(lines: list[str], chunk_size: int, overlap: int) -> list[tuple[int, list[str]]]:
    chunks: list[tuple[int, list[str]]] = []
    if chunk_size <= 0:
        return chunks

    start = 0
    total = len(lines)
    step = max(1, chunk_size - max(0, overlap))
    while start < total:
        end = min(total, start + chunk_size)
        chunks.append((start + 1, lines[start:end]))
        if end >= total:
            break
        start += step
    return chunks


def _extract_json_payload(text: str) -> Any:
    text = text.strip()
    if text.startswith("```"):
        text = re.sub(r"^```(?:json)?\s*", "", text)
        text = re.sub(r"\s*```$", "", text)
    return json.loads(text)


def _gemini_audit_chunk(
    *,
    api_key: str | None,
    model: str,
    source_file: str,
    chunk_start_line: int,
    chunk_lines: list[str],
    max_retries: int = DEFAULT_GEMINI_MAX_RETRIES,
) -> list[dict[str, Any]]:
    numbered = "\n".join(f"{chunk_start_line + i:05d}: {line}" for i, line in enumerate(chunk_lines))
    system_prompt = (
        "Eres un revisor técnico de Markdown convertido desde PDFs regulatorios. "
        "No reescribas el texto. Identifica problemas que luego puedan corregirse con reglas deterministas. "
        "Devuelve SOLO JSON válido con la forma {\"findings\":[...]} y nada más."
    )
    user_prompt = (
        f"Archivo: {source_file}\n"
        f"Rango de líneas: {chunk_start_line}-{chunk_start_line + len(chunk_lines) - 1}\n\n"
        "Revisa este fragmento y detecta problemas de:\n"
        "- saltos de línea o párrafos cortados\n"
        "- headings/títulos repetidos o incoherentes\n"
        "- tablas mal armadas o columnas desalineadas\n"
        "- contenido faltante, truncado o duplicado\n"
        "- fórmulas o ecuaciones sospechosas\n\n"
        "Cada hallazgo debe incluir estos campos:\n"
        "- issue_type: newline|heading|table|missing_content|duplicate|equation|other\n"
        "- severity: low|medium|high\n"
        "- line_start: número entero\n"
        "- line_end: número entero\n"
        "- evidence: cita breve del fragmento\n"
        "- deterministic_fix_hint: sugerencia concreta para una futura regla en el conversor\n"
        "- confidence: número entre 0 y 1\n\n"
        "Si no hay problemas, devuelve {\"findings\":[]}.\n\n"
        f"Fragmento:\n{numbered}"
    )
    if not api_key:
        raise RuntimeError("Gemini audit requires an API key via --llm-audit-api-key or GEMINI_API_KEY")

    payload = {
        "systemInstruction": {"parts": [{"text": system_prompt}]},
        "contents": [{"role": "user", "parts": [{"text": user_prompt}]}],
        "generationConfig": {
            "temperature": 0,
            "responseMimeType": "application/json",
        },
    }
    data = json.dumps(payload).encode("utf-8")
    api_url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={api_key}"
    req = urllib_request.Request(api_url, data=data, headers={"Content-Type": "application/json"}, method="POST")
    last_exc: Exception | None = None
    for attempt in range(max_retries + 1):
        try:
            with urllib_request.urlopen(req, timeout=120) as resp:
                response_text = resp.read().decode("utf-8")
            break
        except urllib_error.HTTPError as exc:
            last_exc = exc
            if exc.code not in {429, 500, 502, 503, 504} or attempt >= max_retries:
                log.warning(
                    "Gemini audit chunk failed for %s lines %d-%d: HTTP %s",
                    source_file,
                    chunk_start_line,
                    chunk_start_line + len(chunk_lines) - 1,
                    exc.code,
                )
                return []
            wait_seconds = 2 ** attempt
            log.warning(
                "Gemini rate-limited for %s lines %d-%d; retrying in %ds (%d/%d)",
                source_file,
                chunk_start_line,
                chunk_start_line + len(chunk_lines) - 1,
                wait_seconds,
                attempt + 1,
                max_retries,
            )
            time.sleep(wait_seconds)
        except urllib_error.URLError as exc:
            last_exc = exc
            if attempt >= max_retries:
                log.warning(
                    "Gemini audit chunk failed for %s lines %d-%d: %s",
                    source_file,
                    chunk_start_line,
                    chunk_start_line + len(chunk_lines) - 1,
                    exc,
                )
                return []
            wait_seconds = 2 ** attempt
            log.warning(
                "Gemini audit transient error for %s lines %d-%d; retrying in %ds (%d/%d)",
                source_file,
                chunk_start_line,
                chunk_start_line + len(chunk_lines) - 1,
                wait_seconds,
                attempt + 1,
                max_retries,
            )
            time.sleep(wait_seconds)
    else:
        if last_exc is not None:
            log.warning(
                "Gemini audit chunk failed for %s lines %d-%d after retries: %s",
                source_file,
                chunk_start_line,
                chunk_start_line + len(chunk_lines) - 1,
                last_exc,
            )
        return []

    response = json.loads(response_text)
    candidates = response.get("candidates", [])
    if not candidates:
        return []
    content_parts = candidates[0].get("content", {}).get("parts", [])
    if not content_parts:
        return []
    content = "".join(part.get("text", "") for part in content_parts if isinstance(part, dict))
    parsed = _extract_json_payload(content)
    findings = parsed.get("findings", []) if isinstance(parsed, dict) else []
    if not isinstance(findings, list):
        return []
    normalized: list[dict[str, Any]] = []
    for finding in findings:
        if isinstance(finding, dict):
            normalized.append(finding)
    return normalized


def audit_markdown_with_gemini(
    markdown_text: str,
    source_file: str,
    *,
    api_key: str | None,
    model: str,
    chunk_lines: int = DEFAULT_LLM_AUDIT_CHUNK_LINES,
    overlap_lines: int = DEFAULT_LLM_AUDIT_OVERLAP_LINES,
    sleep_seconds: float = DEFAULT_LLM_AUDIT_SLEEP_SECONDS,
) -> list[dict[str, Any]]:
    lines = markdown_text.splitlines()
    findings: list[dict[str, Any]] = []
    seen: set[tuple[Any, ...]] = set()

    for chunk_start_line, chunk in _chunk_lines(lines, chunk_lines, overlap_lines):
        if not chunk:
            continue
        chunk_findings = _gemini_audit_chunk(
            api_key=api_key,
            model=model,
            source_file=source_file,
            chunk_start_line=chunk_start_line,
            chunk_lines=chunk,
        )
        for finding in chunk_findings:
            key = (
                finding.get("issue_type"),
                finding.get("line_start"),
                finding.get("line_end"),
                finding.get("evidence"),
                finding.get("deterministic_fix_hint"),
            )
            if key in seen:
                continue
            seen.add(key)
            findings.append(finding)

        if sleep_seconds > 0 and chunk_start_line + len(chunk) < len(lines):
            time.sleep(sleep_seconds)

    return findings


def write_llm_audit_report(out_path: Path, findings: list[dict[str, Any]]) -> Path:
    report_path = out_path.with_name(out_path.stem + ".llm-audit.json")
    report_path.write_text(json.dumps({"findings": findings}, ensure_ascii=False, indent=2), encoding="utf-8")
    return report_path


def load_llm_audit_reports(output_dir: Path) -> list[tuple[Path, list[dict[str, Any]]]]:
    reports: list[tuple[Path, list[dict[str, Any]]]] = []
    for report_path in sorted(output_dir.glob("*.llm-audit.json")):
        try:
            payload = json.loads(report_path.read_text(encoding="utf-8"))
        except Exception as exc:
            log.warning("Skipping unreadable LLM audit report %s: %s", report_path.name, exc)
            continue
        findings = payload.get("findings", []) if isinstance(payload, dict) else []
        if isinstance(findings, list):
            normalized = [finding for finding in findings if isinstance(finding, dict)]
        else:
            normalized = []
        reports.append((report_path, normalized))
    return reports


def summarize_llm_audit_reports(output_dir: Path) -> dict[str, Any]:
    reports = load_llm_audit_reports(output_dir)
    grouped: dict[tuple[str, str], dict[str, Any]] = {}

    for report_path, findings in reports:
        source_stem = report_path.name.removesuffix(".llm-audit.json")
        for finding in findings:
            issue_type = str(finding.get("issue_type", "other"))
            fix_hint = str(finding.get("deterministic_fix_hint", "")).strip() or "(no hint)"
            key = (issue_type, fix_hint)
            bucket = grouped.setdefault(
                key,
                {
                    "issue_type": issue_type,
                    "deterministic_fix_hint": fix_hint,
                    "findings": 0,
                    "files": set(),
                    "examples": [],
                    "confidence_sum": 0.0,
                },
            )
            bucket["findings"] += 1
            bucket["files"].add(source_stem)
            confidence = finding.get("confidence")
            if isinstance(confidence, (int, float)):
                bucket["confidence_sum"] += float(confidence)
            if len(bucket["examples"]) < 3:
                bucket["examples"].append(
                    {
                        "file": source_stem,
                        "line_start": finding.get("line_start"),
                        "line_end": finding.get("line_end"),
                        "evidence": finding.get("evidence"),
                    }
                )

    candidates: list[dict[str, Any]] = []
    for bucket in grouped.values():
        files = sorted(bucket["files"])
        findings_count = bucket["findings"]
        avg_confidence = bucket["confidence_sum"] / findings_count if findings_count else 0.0
        candidates.append(
            {
                "issue_type": bucket["issue_type"],
                "deterministic_fix_hint": bucket["deterministic_fix_hint"],
                "findings": findings_count,
                "files": len(files),
                "file_samples": files[:10],
                "examples": bucket["examples"],
                "avg_confidence": round(avg_confidence, 3),
            }
        )

    candidates.sort(key=lambda item: (-item["findings"], -item["files"], item["issue_type"], item["deterministic_fix_hint"]))
    summary = {
        "report_count": len(reports),
        "candidate_count": len(candidates),
        "candidates": candidates,
    }
    return summary


def write_llm_audit_summary(output_dir: Path, summary: dict[str, Any]) -> Path:
    summary_path = output_dir / "llm-audit-summary.json"
    summary_path.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    return summary_path


def log_llm_audit_summary(summary: dict[str, Any]) -> None:
    log.info("LLM audit reports: %d | candidate rules: %d", summary["report_count"], summary["candidate_count"])
    for candidate in summary["candidates"][:10]:
        log.info(
            "  %s | %s | findings=%d files=%d avg_conf=%.3f",
            candidate["issue_type"],
            candidate["deterministic_fix_hint"],
            candidate["findings"],
            candidate["files"],
            candidate["avg_confidence"],
        )


# ─────────────────────────────────────────────────────────────────────────────
# Main conversion pipeline
# ─────────────────────────────────────────────────────────────────────────────


def convert_file(
    pdf_path: Path,
    output_dir: Path,
) -> Path:
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
                document_title = extract_document_title(raw, pdf_path.name)

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
            r"REF\s*\.?\s*:\s*.+?(?=\n(?:Para |Esta |[A-Z][a-záéíóúñü]))",
            "",
            full_text,
            count=1,
            flags=re.DOTALL,
        )
    # 1. Document-specific patches run FIRST on raw extracted text,
    #    before equation detection scrambles the content.
    full_text = patch_document(full_text, pdf_path.name)
    # 1b. Map Symbol-font PUA chars to Unicode math equivalents.
    #     Runs AFTER patch_document so CIR 1512 / NCG 209 regex patterns still
    #     match their raw PUA codepoints, but BEFORE equation detection so the
    #     detector sees proper Unicode operators.
    full_text = map_symbol_font_chars(full_text)
    # 2. Detect equations (while lines are still short / individual)
    full_text = detect_and_flag_equations(full_text)
    # 2b. Fold math-alphanumeric symbols (𝐶, 𝑘, 𝟎 …) to plain ASCII. Runs after
    #     detection so the math-italic range can still signal formula blocks.
    full_text = normalize_math_alphanumeric(full_text)
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


def convert_all(
    input_dir: Path,
    output_dir: Path,
    skip_existing: bool = False,
):
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
    parser.add_argument(
        "--llm-audit",
        action="store_true",
        help="[DEPRECATED] Ignored. LLM audit path is disabled.",
    )
    parser.add_argument(
        "--llm-audit-api-key",
        default=None,
        help="[DEPRECATED] Ignored.",
    )
    parser.add_argument(
        "--llm-audit-model",
        default=None,
        help="[DEPRECATED] Ignored.",
    )
    parser.add_argument(
        "--llm-audit-chunk-lines",
        type=int,
        default=None,
        help="[DEPRECATED] Ignored.",
    )
    parser.add_argument(
        "--llm-audit-sleep-seconds",
        type=float,
        default=None,
        help="[DEPRECATED] Ignored.",
    )
    args = parser.parse_args()

    if any(
        [
            args.llm_audit,
            args.llm_audit_api_key is not None,
            args.llm_audit_model is not None,
            args.llm_audit_chunk_lines is not None,
            args.llm_audit_sleep_seconds is not None,
        ]
    ):
        log.warning("LLM audit flags are deprecated and currently ignored. Running deterministic conversion only.")

    if args.file:
        pdf_path = Path(args.file)
        if not pdf_path.exists():
            log.error("File not found: %s", pdf_path)
            sys.exit(1)
        convert_file(pdf_path, OUTPUT_DIR)
    else:
        convert_all(
            INPUT_DIR,
            OUTPUT_DIR,
            skip_existing=args.skip_existing,
        )


if __name__ == "__main__":
    main()

