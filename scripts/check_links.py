#!/usr/bin/env python3
"""Validate internal Markdown links across the repo — files AND #anchors.

lychee (in CI) checks external + relative file links well, but does not verify
that an in-repo `#anchor` actually matches a heading. This does, using GitHub's
heading-slug rules, and ignores links inside fenced or inline code so code
samples like `tools[name](arg)` aren't misread as links.

Exit code 0 = clean, 1 = problems found. No dependencies (stdlib only).
"""
from __future__ import annotations

import re
import sys
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
FENCE_RE = re.compile(r"```.*?```", re.DOTALL)
INLINE_CODE_RE = re.compile(r"`[^`]*`")
HEADING_RE = re.compile(r"^#{1,6}\s+(.*)")
LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


def strip_fenced(text: str) -> str:
    """Remove fenced code blocks only (used for heading detection)."""
    return FENCE_RE.sub("", text)


def strip_code(text: str) -> str:
    """Remove fenced AND inline code so their contents aren't parsed as links."""
    return INLINE_CODE_RE.sub("", FENCE_RE.sub("", text))


def slug(heading: str) -> str:
    """Approximate GitHub's heading-anchor slug."""
    s = heading.strip().lower()
    s = re.sub(r"[^\w\s-]", "", s)  # drop punctuation
    return s.replace(" ", "-")


def heading_slugs(body: str) -> set[str]:
    seen: dict[str, int] = {}
    slugs: set[str] = set()
    for line in body.splitlines():
        m = HEADING_RE.match(line)
        if not m:
            continue
        base = slug(m.group(1))
        n = seen.get(base, 0)
        slugs.add(base if n == 0 else f"{base}-{n}")
        seen[base] = n + 1
    return slugs


def main() -> int:
    mds = list(ROOT.rglob("*.md"))
    # Headings: strip only fenced code, so inline-code text in a heading is kept
    # (slug() drops the backtick chars but preserves the words — matching GitHub).
    slugs_by_file = {
        md.resolve(): heading_slugs(strip_fenced(md.read_text("utf-8", errors="ignore")))
        for md in mds
    }

    problems: list[tuple[str, str, str]] = []
    for md in mds:
        body = strip_code(md.read_text("utf-8", errors="ignore"))
        for m in LINK_RE.finditer(body):
            target = m.group(1).strip()
            if target.startswith(("http://", "https://", "mailto:")):
                continue
            path_part, _, anchor = target.partition("#")
            if path_part == "":
                dest = md.resolve()
            else:
                dest = (md.parent / path_part).resolve()
                if dest.is_dir():
                    dest = dest / "README.md"
                if not dest.exists():
                    problems.append((str(md), target, "missing file"))
                    continue
            if anchor and anchor not in slugs_by_file.get(dest, set()):
                problems.append((str(md), target, f"anchor #{anchor} not found"))

    print(f"checked {len(mds)} markdown files (file + anchor links)")
    if problems:
        print(f"PROBLEMS: {len(problems)}")
        for path, target, why in problems:
            print(f"  - {path}: {target} -> {why}")
        return 1
    print("OK: all internal file and anchor links resolve")
    return 0


if __name__ == "__main__":
    sys.exit(main())
