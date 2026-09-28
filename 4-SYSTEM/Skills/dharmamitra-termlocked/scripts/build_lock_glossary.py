#!/usr/bin/env python3
"""Build the lock glossary that `dm_translate.py --glossary` reads, and report
its coverage against the source text *before* any API call is spent.

Two input shapes:

  --termbase <track>/termbase.md          the canonical per-track contract
  --registry 2-RAILS/Keywords/source-term-registry.json  (+ --renderings <tsv>)

Output is a TSV of `source term<TAB>target rendering` lines, plus a coverage
report naming every lemma that matches no block of the source.

Why this script exists rather than piping the termbase straight in
-----------------------------------------------------------------
Registry lemmas carry a trailing shad (`སྒྲོལ་མ།`); running Tibetan carries a
tsheg (`སྒྲོལ་མ་`). `dm_translate.py` matches a glossary entry by plain substring
against the block, so a lemma fed in unconverted matches nothing and is dropped
in silence. Measured on this vault's root text: 74 of 370 lemmas match as-is,
348 match after conversion. A glossary that silently loses four fifths of its
locks produces a translation that looks vocabulary-standardised and is not.

Stdlib only.
"""
from __future__ import annotations

import argparse
import json
import pathlib
import re
import sys

BLOCK_ID_RE = re.compile(r"\^([A-Za-z0-9][A-Za-z0-9-]*)\s*$")
TIB = re.compile(r"[ༀ-࿿]")


# ------------------------------------------------------------------ forms


def match_forms(lemma: str) -> list[str]:
    """Surface forms of a Tibetan lemma worth matching against running text.

    The tsheg form first (it is what actually occurs mid-sentence); the bare
    stem second, which also catches the term at a clause end where a shad or a
    case particle follows.
    """
    stem = lemma.rstrip("།").rstrip("་").strip()
    if not stem:
        return []
    return [stem + "་", stem]


# ------------------------------------------------------------------ inputs


def parse_termbase(path: pathlib.Path) -> list[tuple[str, str]]:
    """Read `| source lemma | locked rendering | … |` rows out of a termbase.md.

    Several source variants in one cell may be separated by ` / `. The header
    row and the `|---|` rule are skipped.
    """
    rows = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line.startswith("|") or set(line) <= set("|- :"):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) < 2:
            continue
        src, tgt = cells[0], cells[1]
        if not src or not tgt or not TIB.search(src):
            continue  # header row, or a non-Tibetan source column
        for variant in (v.strip() for v in src.split(" / ")):
            if variant:
                rows.append((variant, tgt))
    return rows


def parse_registry(path: pathlib.Path,
                   renderings: pathlib.Path | None) -> list[tuple[str, str]]:
    """Registry lemmas + a rendering per lemma.

    The registry is descriptive — it records which English words a term *has
    been* rendered by, never which one is locked. Locking is a decision, so a
    rendering source is required: either an explicit TSV, or the registry's own
    first `english_renderings` value with `--use-first-rendering` (a draft
    convenience, never a published run).
    """
    reg = json.loads(path.read_text(encoding="utf-8"))
    chosen: dict[str, str] = {}
    if renderings:
        for line in renderings.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            for sep in ("\t", " -> ", " → ", "|"):
                if sep in line:
                    a, b = line.split(sep, 1)
                    chosen[a.strip()] = b.strip()
                    break
    out = []
    for t in reg["terms"]:
        if t.get("dropped"):
            continue
        lemma = t["lemma"]
        r = chosen.get(lemma) or chosen.get(t.get("id", ""))
        if not r and ARGS.use_first_rendering:
            r = (t.get("english_renderings") or [None])[0]
        if r:
            out.append((lemma, r))
    return out


def parse_source_blocks(path: pathlib.Path) -> dict[str, str]:
    """{block_id: text} for every block that ends in a ` ^id`, headings excluded."""
    blocks, buf = {}, []
    for line in path.read_text(encoding="utf-8").splitlines():
        s = line.strip()
        if s.startswith("#") or s.startswith("![["):
            buf = []
            continue
        m = BLOCK_ID_RE.search(s)
        if m:
            buf.append(s[: m.start()].rstrip())
            blocks[m.group(1)] = "\n".join(b for b in buf if b)
            buf = []
        elif s:
            buf.append(s)
    return blocks


# -------------------------------------------------------------------- main


def main(argv=None) -> int:
    global ARGS
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--termbase", help="a track's termbase.md (the canonical contract)")
    p.add_argument("--registry", help="2-RAILS/Keywords/source-term-registry.json")
    p.add_argument("--renderings", help="TSV of `lemma<TAB>locked rendering` (with --registry)")
    p.add_argument("--use-first-rendering", action="store_true",
                   help="with --registry and no --renderings: take the registry's first "
                        "attested English rendering. Draft only — never a published run.")
    p.add_argument("--source", required=True, help="the block-ID'd source text")
    p.add_argument("--out", required=True, help="glossary TSV to write")
    p.add_argument("--min-coverage", type=float, default=0.5,
                   help="fail if fewer than this fraction of locks match any block "
                        "(default 0.5; 0 disables)")
    ARGS = p.parse_args(argv)

    if bool(ARGS.termbase) == bool(ARGS.registry):
        p.error("give exactly one of --termbase or --registry")

    pairs = (parse_termbase(pathlib.Path(ARGS.termbase)) if ARGS.termbase
             else parse_registry(pathlib.Path(ARGS.registry),
                                 pathlib.Path(ARGS.renderings) if ARGS.renderings else None))
    if not pairs:
        print("ERROR: no locked pairs found in the input.", file=sys.stderr)
        return 2

    blocks = parse_source_blocks(pathlib.Path(ARGS.source))
    corpus = "\n".join(blocks.values())

    lines, matched, unmatched = [], [], []
    for lemma, rendering in pairs:
        forms = [f for f in match_forms(lemma) if f in corpus]
        if forms:
            # Emit the longest matching form: it is the most specific and avoids
            # a stem matching inside a longer compound.
            lines.append(f"{max(forms, key=len)}\t{rendering}")
            hits = sorted(b for b, t in blocks.items()
                          if any(f in t for f in match_forms(lemma)))
            matched.append((lemma, rendering, hits))
        else:
            unmatched.append((lemma, rendering))

    out = pathlib.Path(ARGS.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(
        "# lock glossary — source term<TAB>locked rendering\n"
        f"# built from: {ARGS.termbase or ARGS.registry}\n"
        f"# source text: {ARGS.source}\n"
        f"# {len(lines)} of {len(pairs)} locks occur in the source\n"
        + "\n".join(lines) + "\n", encoding="utf-8")

    cov = len(lines) / len(pairs)
    print(f"locks in  : {len(pairs)}")
    print(f"locks kept: {len(lines)}  ({cov:.0%} of the input occurs in the source)")
    print(f"written   : {out}")

    # The per-block load is what decides whether dm_translate's hit cap bites.
    load = {b: sum(1 for _, _, hits in matched if b in hits) for b in blocks}
    if load:
        worst = max(load.values())
        busiest = [b for b, n in load.items() if n == worst][:5]
        print(f"max locks in one block: {worst}  (e.g. {', '.join(busiest)})")
        if worst > 15:
            print("  NOTE: dm_translate.py sends at most --glossary-max-hits locks per "
                  "call (default 15). Raise it, or this block loses locks.")

    if unmatched:
        print(f"\n{len(unmatched)} lock(s) match no block of the source — dropped:")
        for lemma, rendering in unmatched[:40]:
            print(f"  {lemma}\t→ {rendering}")
        if len(unmatched) > 40:
            print(f"  … and {len(unmatched) - 40} more")

    if ARGS.min_coverage and cov < ARGS.min_coverage:
        print(f"\nERROR: coverage {cov:.0%} is below --min-coverage "
              f"{ARGS.min_coverage:.0%}. This usually means the lemmas were not "
              f"converted to their match form, or the wrong source file was given.",
              file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
