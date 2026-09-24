#!/usr/bin/env python3
"""Seed `2-RAILS/termbases/term-localization.md` from the keyword registry.

`term-definition` and `term-localization` both fill columns of a table they do not
create. This script creates it: one row per registry term that actually occurs in
the root text, ordered by composite rank, with Meaning and every target-language
cell empty.

Seeding the *whole* matched set rather than a top-N is deliberate and costs nothing:
an unfilled row is inert in every consumer. `term-definition` skips a row whose
Meaning cell it cannot fill, `term-localization` skips a row whose Meaning cell is
empty, and `build_lock_glossary.py` skips a row with no rendering. So the cut-off is
a decision a human makes by filling rows, not one this script makes by omitting them.

Not part of the canonical `Webuddhist-Skills` copy of `term-definition` — added in
21-taras-rails 2026-09-22. Stdlib only.
"""
from __future__ import annotations

import argparse
import datetime
import json
import pathlib
import sys

VAULT = pathlib.Path(__file__).resolve().parents[4]
DEFAULT_REGISTRY = VAULT / "2-RAILS/Keywords/source-term-registry.json"
DEFAULT_OUT = VAULT / "2-RAILS/termbases/term-localization.md"


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--registry", default=str(DEFAULT_REGISTRY))
    p.add_argument("--source", required=True, help="the root text, to filter to terms it uses")
    p.add_argument("--languages", nargs="+", default=["En"], help="target-language columns")
    p.add_argument("--top", type=int, default=0, help="keep only the top N by rank (0 = all)")
    p.add_argument("--out", default=str(DEFAULT_OUT))
    a = p.parse_args(argv)

    reg = json.loads(pathlib.Path(a.registry).read_text(encoding="utf-8"))
    text = pathlib.Path(a.source).read_text(encoding="utf-8")

    rows = [t for t in reg["terms"]
            if not t.get("dropped") and t.get("match_form")
            and (t["match_form"] in text or t["match_form"].rstrip("་") in text)]
    rows.sort(key=lambda t: t.get("rank") or 10**6)
    if a.top:
        rows = rows[: a.top]

    out = pathlib.Path(a.out)
    if out.exists():
        print(f"ERROR: {out} already exists. Refusing to overwrite a table that may "
              f"hold filled cells — move it aside first.", file=sys.stderr)
        return 1

    cols = ["Rank", "Bo", "Match form", "Attested En renderings", "Meaning", *a.languages]
    head = "| " + " | ".join(cols) + " |\n| " + " | ".join("---" for _ in cols) + " |"
    body = "\n".join(
        "| {r} | {bo} | `{mf}` | {en} | | {blanks} |".format(
            r=t.get("rank") or "", bo=t["lemma"], mf=t["match_form"],
            en=", ".join(t.get("english_renderings") or [])[:80],
            blanks=" | ".join("" for _ in a.languages))
        for t in rows)

    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(f"""---
title: Term localization table
source_registry: {pathlib.Path(a.registry).relative_to(VAULT)}
root_text: {a.source}
terms: {len(rows)}
languages: [{", ".join(a.languages)}]
filled_meaning: 0
generated: {datetime.date.today()}
status: draft
---

# Term localization — {len(rows)} terms

The vocabulary-standardisation table. One row per registry term that occurs in the
root text, ordered by the keyword run's composite rank.

- **Meaning** is filled by `term-definition`: verbatim commentary definitions, each
  cited to its block ID. Never paraphrase into this column.
- **The language columns** are filled by `term-localization`, deriving each rendering
  *from the Meaning cell* rather than from a dictionary. A row with an empty Meaning
  cell is skipped, not guessed.
- **A row left entirely empty is inert.** Every consumer skips it. So this table
  being long is not a commitment to filling all of it — work down from rank 1 and
  stop where the returns stop.
- `graded-translate` Phase 1 exports the filled rows into a track's own
  `termbase.md`, which is the contract `dharmamitra-termlocked` locks to.

Regenerate with `4-SYSTEM/Skills/term-definition/scripts/seed_term_table.py`
(it refuses to overwrite an existing table).

{head}
{body}
""", encoding="utf-8")
    print(f"terms in registry : {len(reg['terms'])}")
    print(f"terms in root text: {len(rows)}")
    print(f"languages         : {', '.join(a.languages)}")
    print(f"written           : {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
