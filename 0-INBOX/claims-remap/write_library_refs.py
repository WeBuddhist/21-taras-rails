"""Write the remapped library addresses into the tree-guided claims files.

Reads out/<registered_id>.json (from remap_claims.py) and, in
2-RAILS/Claims/raw/tree-guided/<registered_id>.md:
  - adds a `**Library:**` line under each claim's last `**Cite:**` line, citing the
    resegmented file in 1-SOURCES/Commentaries/New raw data/ by its block IDs, which are
    the library segments' `reference`;
  - adds library_source_file / library_text_id / library_edition_id / library_remap to
    the frontmatter.
The old `**Cite:**` lines are left as they are. Re-running replaces earlier Library lines.

Usage (from the vault root):
    python3 0-INBOX/claims-remap/write_library_refs.py            # dry run: counts only
    python3 0-INBOX/claims-remap/write_library_refs.py --write
"""

import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
VAULT = HERE.parents[1]
CLAIMS = VAULT / "2-RAILS/Claims/raw/tree-guided"
DATE = "2026-11-04"

CLAIM_START = re.compile(r"^(?:#+\s+|⚑\s+\*\*)(c-[0-9a-zA-Z-]+)")
FM_KEYS = ("library_source_file", "library_text_id", "library_edition_id", "library_remap")


def library_line(new_file, row):
    if row["verdict"] == "absent-from-edition" or not row["new_refs"]:
        return "**Library:** none — this passage is not in the library edition"
    refs = [r for r in row["new_refs"] if not r.startswith("(")]
    first, rest = refs[0], refs[1:]
    tail = "".join(f", #^{r}" for r in rest)
    return f"**Library:** ({new_file}#^{first}{tail})"


def rewrite(rid, write):
    data = json.loads((HERE / "out" / f"{rid}.json").read_text(encoding="utf-8"))
    rows = {r["claim_id"]: r for r in data["claims"]}
    path = CLAIMS / f"{rid}.md"
    lines = [l for l in path.read_text(encoding="utf-8").split("\n") if not l.startswith("**Library:**")]

    # frontmatter: drop earlier library_* keys, add fresh ones before the closing ---
    end = lines.index("---", 1)
    head = [l for l in lines[1:end] if not l.startswith(FM_KEYS)]
    lib = data["library"]
    head += [
        f'library_source_file: "{data["new_file"]}"',
        f"library_text_id: {lib['text_id']}",
        f"library_edition_id: {lib['edition_id']}",
        f'library_remap: "0-INBOX/claims-remap/out/{rid}.json ({DATE})"',
    ]
    lines = ["---"] + head + lines[end:]

    # claim blocks: insert after the last Cite line of each claim (or its last field, if it has none)
    out, cur, last_cite, last_field, written, missing = [], None, None, None, set(), []

    def flush():
        at = last_cite if last_cite is not None else last_field
        if cur and at is not None:
            if cur in rows:
                out.insert(at + 1, library_line(data["new_file"], rows[cur]))
                written.add(cur)
            else:
                missing.append(cur)

    for line in lines:
        m = CLAIM_START.match(line)
        if m or line.startswith("#"):
            flush()
            cur, last_cite, last_field = (m[1] if m else None), None, None
        out.append(line)
        if cur and line.startswith("**Cite:**"):
            last_cite = len(out) - 1
        if cur and re.match(r"^(-\s*)?\*\*[^*]+:\*\*", line):
            last_field = len(out) - 1
    flush()

    absent = sum(1 for c in written if rows[c]["verdict"] == "absent-from-edition")
    unwritten = sorted(set(rows) - written)
    print(f"{rid:16} library lines={len(written):4} (none={absent}) "
          f"unwritten={unwritten} not in remap={missing}")
    if write:
        path.write_text("\n".join(out), encoding="utf-8")


def main():
    write = "--write" in sys.argv
    ids = [a for a in sys.argv[1:] if not a.startswith("--")]
    ids = ids or [p.stem for p in sorted((HERE / "out").glob("*.json")) if p.stem != "summary"]
    for rid in ids:
        rewrite(rid, write)
    if not write:
        print("dry run — pass --write to change the claims files")


if __name__ == "__main__":
    main()
