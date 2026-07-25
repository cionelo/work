#!/usr/bin/env python3
"""Guardrail, link, and asset checks for itsnemo.dev/work.

Usage: python3 scripts/check-site.py
Exit 0 = clean. Exit 1 = violations printed as file:line: message.

Rules come from docs/superpowers/specs/2026-07-24-work-website-product-pivot-design.md
sections 8 and 9. Adding a rule here is cheaper than catching a bad claim in production.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PAGES = ["index.html", "system.html", "services.html", "portfolio.html", "about.html"]

# Claims the infrastructure cannot back, plus positioning we deliberately killed.
BANNED_EVERYWHERE = [
    r"24/7",
    r"\bSLA\b",
    r"\buptime\b",
    r"\bHIPAA\b",
    r"\bFERPA\b",
    r"\bSOC ?2\b",
    r"\bguarantee",
    r"\bunlimited\b",
    r"\bdev team\b",
    r"\baffordable\b",
    r"\bcheap\b",
    r"87%",
]

# Client, partner, and vendor names. about.html is exempt: it names Western Colorado
# University as part of Nemo's own biography, which is not a client claim.
CLIENT_NAMES = [
    r"Trailhead",
    r"Bluecove",
    r"Sawyer",
    r"Gusto",
    r"rcrtr",
    r"Little Bites",
    r"Nashville",
    r"Western Colorado",
]
CLIENT_NAME_EXEMPT = {"about.html"}

# Wording the spec pins exactly, scoped to the one page each rule is about. If the
# trigger phrase appears on the named file, the required phrase must appear there
# too. File-scoped so an unrelated mention elsewhere (e.g. a proof line on
# index.html) doesn't trip a rule that exists to pin the case study's honest status
# wording on portfolio.html.
REQUIRED_PAIRS = [
    ("portfolio.html", "children's museum", "Built and delivered"),
]

# Site's own canonical base URL. Meta content values (e.g. og:image) built on this
# prefix point at local assets and are worth resolving like any other local target.
BASE_URL = "https://itsnemo.dev/work/"

TAG_RE = re.compile(r'(?:href|src)="([^"]+)"')
CONTENT_RE = re.compile(r'content="([^"]+)"')
ID_RE = re.compile(r'id="([^"]+)"')


def strip_comments(text):
    """Blank out HTML comments so TODO notes don't trip the copy rules.

    Preserves newlines inside the comment so line numbers in later reports still
    line up with the real file — only non-newline characters are blanked.
    """
    def blank(m):
        return "".join(c if c == "\n" else " " for c in m.group(0))

    return re.sub(r"<!--.*?-->", blank, text, flags=re.S)


def check_banned(name, text, problems):
    body = strip_comments(text)
    patterns = list(BANNED_EVERYWHERE)
    if name not in CLIENT_NAME_EXEMPT:
        patterns += CLIENT_NAMES
    for i, line in enumerate(body.splitlines(), 1):
        for pat in patterns:
            if re.search(pat, line, re.I):
                problems.append(f"{name}:{i}: banned phrase /{pat}/ -> {line.strip()[:90]}")


def check_required_pairs(name, text, problems):
    body = strip_comments(text)
    for filename, trigger, required in REQUIRED_PAIRS:
        if filename != name:
            continue
        if trigger.lower() in body.lower() and required.lower() not in body.lower():
            problems.append(f"{name}:0: '{trigger}' present but required wording '{required}' missing")


def check_links(name, text, ids_by_file, problems):
    for i, line in enumerate(text.splitlines(), 1):
        for target in TAG_RE.findall(line):
            if target.startswith(("http://", "https://", "mailto:", "tel:", "data:")):
                continue
            path_part, _, anchor = target.partition("#")
            if path_part:
                resolved = (ROOT / path_part).resolve()
                if not resolved.exists():
                    problems.append(f"{name}:{i}: missing target -> {target}")
                    continue
                target_file = path_part
            else:
                target_file = name
            if anchor and target_file in ids_by_file and anchor not in ids_by_file[target_file]:
                problems.append(f"{name}:{i}: dead anchor -> {target}")
        for target in CONTENT_RE.findall(line):
            if not target.startswith(BASE_URL):
                continue
            path_part = target[len(BASE_URL):]
            resolved = (ROOT / path_part).resolve()
            if not resolved.exists():
                problems.append(f"{name}:{i}: missing target -> {target}")


def main():
    problems = []
    texts = {}
    for name in PAGES:
        path = ROOT / name
        if not path.exists():
            problems.append(f"{name}:0: page missing")
            continue
        texts[name] = path.read_text(encoding="utf-8")

    ids_by_file = {n: set(ID_RE.findall(t)) for n, t in texts.items()}

    for name, text in texts.items():
        check_banned(name, text, problems)
        check_required_pairs(name, text, problems)
        check_links(name, text, ids_by_file, problems)

    if problems:
        print(f"FAIL — {len(problems)} problem(s):\n")
        for p in problems:
            print("  " + p)
        return 1
    print(f"PASS — {len(texts)} pages: no banned phrases, no dead links, no missing assets.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
