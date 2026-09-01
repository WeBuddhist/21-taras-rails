#!/usr/bin/env python3
"""
Heuristic grouper for the tsultrim-namdak resegmentation, acting in place of
the Gemini call in resegment.py (no API key available in this environment;
the grouping judgment is performed by the agent directly, per the isolated-
pass constraint on this task).

Key signal: the cleaned source file's OWN remaining blank lines. Every blank
line still present after clean-raw-text is a genuine paragraph/section
boundary carried over from the original book (verse-stanza vs. prose-
explanation boundaries, TOC-entry boundaries, foreword-vs-foreword
boundaries, etc.) -- not an OCR page-break artifact (those were already
stripped). Treated as a HARD constraint: no merge group may cross one.

Within each such blank-line-delimited chunk:
  - if the whole chunk is <= 4 lines, merge it as a single block (it is
    already one natural unit -- a verse stanza, a TOC entry, a short
    dedication, etc.)
  - otherwise, greedily accumulate lines into groups of 2-4, closing a
    group at the first line ending in a shad preceded by a sentence-final
    particle (the same family resegment.py's own TERMINAL_RE uses for safe
    window cuts), capped at 4 lines.
"""
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, "4-SYSTEM/Skills/commentary-resegment/scripts")
import resegment as R  # noqa: E402

TERMINAL_RE = re.compile(
    r'(?:སོ|འོ|ནོ|དོ|ཏོ|ཡོ|ངོ|བོ|མོ|རོ|ལོ|གོ|ཤོག|མཆིས|གསོལ|ཅིག)[།༎༏]+[\s།༎༏]*$'
)

PATH = Path("1-SOURCES/Commentaries/སྒྲོལ་འགྲེལ་ཚོགས་གཉིས་རྒྱ་མཚོར་འཇུག་པའི་གྲུ་གཟིངས།.md")


def chunk_boundaries():
    """Return the set of linenos (1-indexed, in the FULL file incl. frontmatter)
    that are the LAST line of a blank-line-delimited chunk in the body."""
    text = PATH.read_text(encoding="utf-8")
    end = text.index("\n---\n", 4) + 5
    fm_lines = text[:end].count("\n")
    body_lines = text[end:].split("\n")
    last_of_chunk = set()
    cur_last = None
    for i, line in enumerate(body_lines):
        lineno = fm_lines + i + 1
        if line.strip() == "":
            if cur_last is not None:
                last_of_chunk.add(cur_last)
                cur_last = None
        else:
            cur_last = lineno
    if cur_last is not None:
        last_of_chunk.add(cur_last)
    return last_of_chunk


def propose(lines, boundary_ends, max_group=4):
    """lines: list of {"lineno":int,"text":str} for one window.
    boundary_ends: set of linenos that are the last line of their chunk."""
    groups = []
    cur = []
    for item in lines:
        cur.append(item["lineno"])
        is_boundary = item["lineno"] in boundary_ends
        if is_boundary or len(cur) >= max_group or TERMINAL_RE.search(item["text"].strip()):
            if len(cur) >= 2:
                groups.append(cur)
            cur = []
    return groups


def main():
    newline, frontmatter, units = R.parse_file(PATH)
    windows = R.make_windows(units, 120)
    boundary_ends = chunk_boundaries()

    outdir = Path("0-INBOX/temp/RESEG-tsultrim-namdak/proposed")
    outdir.mkdir(parents=True, exist_ok=True)
    total_groups = 0
    for w in windows:
        groups = propose(w["lines"], boundary_ends)
        total_groups += len(groups)
        ops = [{"op": "merge", "lines": g} for g in groups]
        data = {
            "window_idx": w["idx"],
            "heading": w["heading"],
            "line_range": [w["lines"][0]["lineno"], w["lines"][-1]["lineno"]],
            "operations": ops,
        }
        (outdir / f"window-{w['idx']:04d}.json").write_text(
            json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Proposed groupings for {len(windows)} windows, {total_groups} merge groups -> {outdir}")
    print(f"Chunk boundaries (paragraph-level): {len(boundary_ends)}")


if __name__ == "__main__":
    main()
