"""Audit generated markdown for parsing issues.

Scans markdown/ for three categories of problems:
  1. Title / header errors
  2. Badly parsed equations
  3. Malformed tables

Usage: python3 audit_markdown.py
"""

import re
import glob
import os

MD_DIR = "markdown"

# PUA Symbol-font codepoints that should have been mapped/patched away.
PUA_RE = re.compile(r"[\uf000-\uf0ff]")
# Unicode math-italic letters (often leftover fragmented formula variables).
MATH_ITALIC_RE = re.compile(r"[\U0001D400-\U0001D7FF]")
WARN_RE = re.compile(r"^> ⚠️", re.MULTILINE)


def first_h1(text: str) -> str | None:
    m = re.search(r"^# (.+)$", text, re.MULTILINE)
    return m.group(1).strip() if m else None


def audit_title(stem: str, text: str) -> list[str]:
    issues = []
    h1 = first_h1(text)
    if h1 is None:
        issues.append("TITLE: missing H1 title")
        return issues
    # Title still contains the FECHA header fragment
    if re.search(r"FECHA\s*:", h1):
        issues.append(f"TITLE: contains FECHA fragment -> {h1!r}")
    # Title truncated to a bare trailing number or single letter
    if re.search(r"[—-]\s*\d{1,3}$", h1):
        issues.append(f"TITLE: truncated at trailing number -> {h1!r}")
    if re.search(r"\bN[°º]\s*\d{1,2}$", h1):
        issues.append(f"TITLE: truncated mid-reference -> {h1!r}")
    # Title ends abruptly with a lone preposition/letter (heuristic)
    if re.search(r"\bDE?L?\s+D$", h1) or re.search(r"\bDE$", h1):
        issues.append(f"TITLE: ends abruptly -> {h1!r}")
    return issues


def audit_headers(stem: str, text: str) -> list[str]:
    issues = []
    # Repeated page headers left in the body (CIRCULAR N... / FECHA pairs after the H1)
    body = text
    # Count CIRCULAR N<num> followed by FECHA lines in body
    repeated = re.findall(
        r"^CIRCULAR\s*N[°º].*\nFECHA\s*:.*$", body, re.MULTILINE
    )
    if repeated:
        issues.append(f"HEADER: {len(repeated)} repeated CIRCULAR/FECHA header(s) in body")
    # NORMA header repetition
    norma = re.findall(
        r"^NORMA DE CAR[ÁA]CTER GENERAL\s*N[°º].*\nFECHA\s*:.*$", body, re.MULTILINE
    )
    if norma:
        issues.append(f"HEADER: {len(norma)} repeated NORMA/FECHA header(s) in body")
    # Institution footer left over
    foot = re.findall(
        r"^(?:SUPERINTENDENCIA DE VALORES Y SEGUROS DE CHILE|COMISI[ÓO]N PARA EL MERCADO FINANCIERO)\s*$",
        body, re.MULTILINE,
    )
    if foot:
        issues.append(f"HEADER: {len(foot)} leftover institution footer line(s)")
    return issues


def audit_equations(stem: str, text: str) -> list[str]:
    issues = []
    warns = len(WARN_RE.findall(text))
    if warns:
        issues.append(f"EQUATION: {warns} ⚠️ flagged formula block(s) to verify")
    # Leftover PUA chars outside of code fences
    pua = PUA_RE.findall(text)
    if pua:
        issues.append(f"EQUATION: {len(pua)} leftover Symbol-font PUA char(s)")
    # Math-italic fragments not inside a $$ block
    lines = text.split("\n")
    in_math = False
    stray_italic = 0
    for ln in lines:
        s = ln.strip()
        if s == "$$":
            in_math = not in_math
            continue
        if s.startswith("$$") and s.endswith("$$") and len(s) > 4:
            continue
        if not in_math and not s.startswith(">"):
            stray_italic += len(MATH_ITALIC_RE.findall(ln))
    if stray_italic:
        issues.append(f"EQUATION: {stray_italic} math-italic char(s) outside formula blocks")
    return issues


def audit_tables(stem: str, text: str) -> list[str]:
    issues = []
    lines = text.split("\n")
    # Find markdown table blocks: consecutive lines starting with |
    i = 0
    n = len(lines)
    table_idx = 0
    while i < n:
        if lines[i].lstrip().startswith("|"):
            block = []
            while i < n and lines[i].lstrip().startswith("|"):
                block.append(lines[i])
                i += 1
            table_idx += 1
            if len(block) >= 2:
                # Column count consistency
                counts = [ln.count("|") for ln in block]
                if len(set(counts)) > 1:
                    issues.append(
                        f"TABLE #{table_idx}: inconsistent column counts {sorted(set(counts))}"
                    )
                # Missing separator row (second line should be ---)
                if not re.match(r"^\s*\|[\s:|-]*\|\s*$", block[1]) and "---" not in block[1]:
                    issues.append(f"TABLE #{table_idx}: missing/invalid separator row")
                # Mostly-empty table (many empty cells)
                cells = "".join(block).replace("|", "").replace("-", "").strip()
                if not cells:
                    issues.append(f"TABLE #{table_idx}: empty table")
            else:
                issues.append(f"TABLE #{table_idx}: single-line pseudo-table")
        else:
            i += 1
    return issues


def main():
    files = sorted(glob.glob(os.path.join(MD_DIR, "*.md")))
    total = {"TITLE": 0, "HEADER": 0, "EQUATION": 0, "TABLE": 0}
    files_with_issues = 0
    report = []
    for md in files:
        stem = os.path.basename(md)[:-3]
        text = open(md, encoding="utf-8").read()
        issues = []
        issues += audit_title(stem, text)
        issues += audit_headers(stem, text)
        issues += audit_equations(stem, text)
        issues += audit_tables(stem, text)
        if issues:
            files_with_issues += 1
            report.append((stem, issues))
            seen = set()
            for it in issues:
                cat = it.split(" ")[0].rstrip(":")
                if cat in total and cat not in seen:
                    total[cat] += 1
                    seen.add(cat)
    # Print grouped report
    for stem, issues in report:
        print(f"\n### {stem}")
        for it in issues:
            print("  -", it)
    print("\n" + "=" * 60)
    print(f"Files scanned : {len(files)}")
    print(f"Files w/ issues: {files_with_issues}")
    print(f"By category    : {total}")


if __name__ == "__main__":
    main()
