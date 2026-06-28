---
name: pdf-markdown-pipeline
description: Domain knowledge for the CMF regulation PDF-to-Markdown converter. Use when debugging formula extraction, writing new document patches, or investigating ⚠️ formula warnings.
---

# CMF Regulation PDF → Markdown Pipeline

## Architecture Overview

All conversion logic lives in `convert_pdfs.py`. The pipeline for each PDF runs:

1. **`extract_page_content(page)`** — Extracts text per page. Uses `page.extract_text()` with **default tolerances (x_tolerance=3, y_tolerance=3)** when no tables are found.
2. **`remove_page_chrome()`** — Strips page headers/footers.
3. **`fix_kerning_artifacts()`** — Fixes spaced digits, hyphen breaks.
4. **`merge_cross_page_continuation()`** — Joins text split across page boundaries.
5. **`patch_document()`** — Document-specific LaTeX reconstructions. Runs on **raw PUA text**.
6. **`map_symbol_font_chars()`** — Maps `\uf0XX` Symbol-font PUA chars to Unicode math.
7. **`detect_and_flag_equations()`** — Wraps real formula fragments in `> ⚠️ $$ ... $$`.
8. **`rejoin_wrapped_lines()`** — Re-joins soft-wrapped paragraph lines.
9. **`add_markdown_headings()`** — Promotes numbered/Roman/all-caps sections.
10. **`collapse_blank_lines()`** — Normalises spacing.

## Critical: Extraction Tolerance Affects Pattern Matching

**The most common debugging pitfall.** `extract_page_content()` uses `x_tolerance=3` (default), NOT 1. Debugging with `page.extract_text(x_tolerance=1)` gives **different line groupings** than the actual pipeline.

| x_tolerance | Same formula line |
|---|---|
| x_tol=1 (debug) | `E C = \uf0e5\ni\nn\n= 1` — ∑ on same line as `E C =` |
| x_tol=3 (pipeline) | `E C =\nn\n\uf0e5i=\n1` — ∑ combined with `i=` on next line |

**Always test patches using `extract_page_content()`**, not raw `page.extract_text(x_tolerance=1)`:

```python
import convert_pdfs as cv
import pdfplumber

with pdfplumber.open('pdf/some_file.pdf') as pdf:
    for page in pdf.pages:
        raw = cv.extract_page_content(page)
        # Now process with fix_kerning_artifacts etc to see actual pipeline input
        clean = cv.remove_page_chrome(raw)
        clean = cv.fix_kerning_artifacts(clean)
        print(repr(clean[idx:idx+200]))
```

## Critical: Patch Ordering

`patch_document()` runs **BEFORE** `map_symbol_font_chars()`. This means:
- Patches must match **raw PUA codepoints** (e.g., `\uf0e5` for ∑, `\uf0b4` for ×)
- NOT their Unicode equivalents (`∑`, `×`)
- Use character classes to handle both: `[\uf0e5∑\u2211]`, `[\uf0b4×\u00d7]`

Exception: CIR 1512 patches key on `\uf053` (Symbol Σ). If `map_symbol_font_chars()` ran first, it would map `\uf053` → `Σ` breaking those patches. Order is intentional.

## Critical: LaTeX Replacements Must Use Lambdas

`re.sub()` processes plain replacement strings for backslash escapes. `\s`, `\m`, `\c` are invalid in Python 3.11+. **All replacements containing LaTeX backslashes must use lambdas**:

```python
# WRONG — causes re.error in Python 3.11+
(pattern, r"$$\n\sum_{i=1}^{n}\n$$")

# CORRECT
(pattern, lambda m: "$$\n\\sum_{i=1}^{n}\n$$")
```

## Symbol Font PUA Mapping

Key `\uf0XX` → Unicode mappings (see `_SYMBOL_FONT_MAP` in code):
- `\uf0e5` → `∑` (summation)
- `\uf0b4` → `×` (times)
- `\uf0a3` → `≤`, `\uf0b3` → `≥`
- `\uf0ec`–`\uf0fe` → `""` (large bracket components, purely structural)
- `\uf053` → `Σ` (used in CIR 1512 patches — must patch BEFORE mapping)

## Formula Warning System

- `detect_and_flag_equations()` wraps ≥3 consecutive fragment lines in `> ⚠️ $$ ... $$`
- A block only gets ⚠️ if `_REAL_MATH_BLOCK_RE` matches — prevents false positives from kerned table headers
- `_REAL_MATH_BLOCK_RE` checks for: Unicode math operators, Greek letters, math-italic chars, assignment `x = y`, multiplication with `*`, remaining PUA chars
- Count real warnings with `grep -r "^> ⚠️" markdown/ | wc -l` (header comment also contains ⚠️ but is not a formula block)

## Writing Document-Specific Patches

Add patches to the `_DOCNAME_PATCHES` list and route them in `patch_document()`:

```python
_MY_PATCHES = [
    (
        re.compile(
            r"fragment\s*line\s*1\s*\n"
            r"fragment\s*line\s*2\s*\n"
            r"fragment\s*line\s*3",
        ),
        lambda m: "$$\n\\text{LaTeX formula here}\n$$",
    ),
]

# In patch_document():
if "my_doc_prefix" in source_file.lower():
    for pattern, replacement in _MY_PATCHES:
        text = pattern.sub(replacement, text)
```

### Common Kerning Patterns in Spanish CMF PDFs

Spanish words get split by x_tolerance=3 extraction:
- "deudor" → `d eu d o r` or `d\s*e\s*u\s*d\s*o\s*r` — use `d\s*e?\s*u\s*d\s*o\s*r` in patterns
- "aval" → `av\n/\nal` (slash separator between syllables) — use `a\s*v(?:\s*/\s*)?\s*a\s*l`
- "Provisión" → `P r o v is ió n` — use `P\s*r\s*o\s*v\s*i\s*s\s*i\s*[oó]\s*n`

### Summation Pattern (∑ as subscript/superscript)

With default extraction, summation limits appear as:
```
∑i=     # ∑ combined with index variable
n
= 1     # lower limit
```
Pattern: `r"[\uf0e5∑\u2211]i\s*=\s*\n n\s*\n =\s*1"` → `r"\sum_{i=1}^{n}"`

Full EC credit-equivalent formula pattern (appears in CIR 2248/2249/2250/2265/2281):
```
E C =
n
∑i=
1
N o c
i
× F C
i
× 0 , 4
```

## Currently Patched Documents

- **NCG 209**: Nelson-Siegel yield curve formulas
- **CIR 1512**: Insurance reserve summation (Symbol Σ = `\uf053`)
- **CIR 1476**: Makeham mortality table parameters
- **NCG 207**: Gompertz mortality + Nelson-Siegel
- **NCG 148**: EWMA VaR model
- **NCG 306**: Insurance reserving (TSa, FA chain-ladder)
- **NCG 243**: Actuarial pension obligation formulas
- **CIR 2281**: Macaulay duration
- **CIR 2248/2249/2250/2265**: EC = Σ Noc × FC × 0.4 (credit equivalent)
- **CIR 2243/2249**: Provisión deudor risk credit formula

## Remaining Real Formula Warnings (as of last run: 83 blocks / 24 files)

Top offenders that still need manual LaTeX patches:
- `ncg_243` (26): Complex Unicode math-italic actuarial pension formulas
- `ncg_218` (15): Piecewise commission formulas — need `\begin{cases}` LaTeX
- `ncg_306` (7): Actuarial life insurance commutation functions (äx:n, Nx, Dx)
- `cir_2281` (4): Complex positive EC formula with nested sum in denominator
- `cir_1581` (5): Fund performance formulas

## Running the Converter

```bash
# Single file
python3 convert_pdfs.py --file pdf/some_file.pdf

# All files
python3 convert_pdfs.py --all

# Skip already-converted files
python3 convert_pdfs.py --all --skip-existing

# Check formula warning counts
grep -rl "^> ⚠️" markdown/ | while read f; do count=$(grep -c "^> ⚠️" "$f"); echo "$count ${f##markdown/}"; done | sort -rn
```
