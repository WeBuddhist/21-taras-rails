#!/usr/bin/env python3
"""Stamp ^chapter-verse block IDs onto the English translation of the root text.

The Lotsawa House translation numbers its verses `(1)`…`(27)` inline. Those
numbers are the traditional verse numbers, so they map straight onto the root
text's block IDs: `(N)` -> `^1-N` for the twenty-one homages, the unnumbered
closing couplet -> `^1-22`, and the benefit verses `(22)`…`(27)` -> `^2-1`…`^2-6`
(chapter 2 = ཕན་ཡོན, which the Tibetan edition in this upload does not carry but
every commentary discusses).

Output: corpora/tara21/work/root.en.md — a work artifact, not source.
"""

from __future__ import annotations

import re
from pathlib import Path

SRC = Path("/tmp/iats/corpora/tara21/source/twenty-one-tara-praise.en.md")
OUT = Path("/tmp/iats/corpora/tara21/work/root.en.md")

NUM = re.compile(r"\((\d+)\)\s*$")
FOOTNOTE = re.compile(r"(?<=[a-zA-Zʼ’.,;!?—-])\d{1,2}(?=\s*(?:\(|$|[,.;]))")


def main() -> None:
    lines = SRC.read_text(encoding="utf-8").splitlines()
    out: list[str] = []
    buf: list[str] = []
    started = False
    for line in lines:
        s = line.strip()
        if s.startswith("Oṃ. Homage to the noble lady"):
            started = True
        if not started:
            continue
        if s.startswith("|") or s.startswith("Version:") or s.startswith("sgrol ma la"):
            break
        if s.startswith("##"):
            out += ["", "## The Excellent Benefits of the Praise ^2-0", ""]
            continue
        if not s:
            continue
        m = NUM.search(s)
        body = FOOTNOTE.sub("", NUM.sub("", s).strip()) if m else FOOTNOTE.sub("", s)
        buf.append(body.strip())
        if m:
            n = int(m.group(1))
            vid = f"1-{n}" if n <= 21 else f"2-{n - 21}"
            out.append("\n".join(buf) + f" ^{vid}")
            out.append("")
            buf = []
        elif s.startswith("This Praise with the twenty-one"):
            pass
        elif s.startswith("Is itself the root mantra"):
            out.append("\n".join(buf) + " ^1-22")
            out.append("")
            buf = []
        elif s.startswith("This completes the Praise"):
            buf = []

    header = [
        "---",
        "title: The Praise to Tārā with Twenty-One Verses of Homage (block-ID stamped)",
        "source: corpora/tara21/source/twenty-one-tara-praise.en.md",
        "note: work artifact — block IDs stamped from the translation's own verse numbers",
        "---",
        "",
    ]
    OUT.write_text("\n".join(header + out).rstrip() + "\n", encoding="utf-8")
    ids = re.findall(r"\^([\w-]+)", OUT.read_text(encoding="utf-8"))
    print(f"{OUT}: {len([i for i in ids if not i.endswith('-0')])} verses stamped")
    print(" ", ", ".join(ids))


if __name__ == "__main__":
    main()
