#!/usr/bin/env python3
"""Verify that every lock that *should* have applied to a block actually landed
in the translation, and list the blocks that need a re-run.

This is the gate that makes "vocabulary-standardised" a claim rather than a
hope. The prompt-side lock is strong but not total: measured on this corpus, a
batched call honoured 10 of 11 locks, and the eleventh came back inflected
(`pāramitā` for a locked `pāramitās`). So the tiers matter —

    EXACT    the locked rendering appears verbatim
    LOOSE    it appears article-stripped / de-pluralised — an inflection, not drift
    MISSING  it does not appear — real drift, or a legitimate paraphrase

— and only MISSING is actionable.

Expectation source: the **Tibetan source block**. A lock applies to a block iff
its match form occurs in that block's Tibetan. That is mechanical and needs no
verse rails, which this vault does not yet have.

Matching tiers are imported from `graded-translate`, so there is one
implementation of EXACT/LOOSE in the vault, not two.

Stdlib only.
"""
from __future__ import annotations

import argparse
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve()
VAULT = HERE.parents[4]                       # <vault>/4-SYSTEM/Skills/<skill>/scripts/
sys.path.insert(0, str(VAULT / "4-SYSTEM/Skills/graded-translate/scripts"))
try:
    from check_termbase_consistency import loose_form, match_tier, normalize
except ImportError:  # pragma: no cover - the skill is not installed
    print("ERROR: 4-SYSTEM/Skills/graded-translate/scripts/"
          "check_termbase_consistency.py not found — import graded-translate first.",
          file=sys.stderr)
    raise

sys.path.insert(0, str(HERE.parent))
from build_lock_glossary import match_forms, parse_source_blocks  # noqa: E402


def read_glossary(path: pathlib.Path) -> list[tuple[str, str]]:
    pairs = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        for sep in ("\t", " -> ", " → ", "|"):
            if sep in line:
                a, b = line.split(sep, 1)
                if a.strip() and b.strip():
                    pairs.append((a.strip(), b.strip()))
                break
    return pairs


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--glossary", required=True, help="the lock glossary TSV that was sent")
    p.add_argument("--source", required=True, help="the block-ID'd Tibetan source text")
    p.add_argument("--translation", required=True, help="the rendered translation file")
    p.add_argument("--json", help="write the full report here")
    p.add_argument("--only", nargs="*", help="restrict to these block IDs")
    p.add_argument("--loose-is-pass", action="store_true", default=True,
                   help="treat LOOSE as a pass (default: yes — inflection is not drift)")
    p.add_argument("--strict", dest="loose_is_pass", action="store_false",
                   help="treat LOOSE as a failure too")
    a = p.parse_args(argv)

    locks = read_glossary(pathlib.Path(a.glossary))
    src = parse_source_blocks(pathlib.Path(a.source))
    tgt = parse_source_blocks(pathlib.Path(a.translation))

    ids = [b for b in src if (not a.only or b in a.only)]
    rows, missing_blocks = [], set()

    for bid in ids:
        s_text = src[bid]
        t_text = tgt.get(bid)
        if t_text is None:
            rows.append({"block": bid, "term": "—", "rendering": "—",
                         "tier": "NO-TRANSLATION"})
            missing_blocks.add(bid)
            continue
        hay_n, hay_l = normalize(t_text), loose_form(t_text)
        for term, rendering in locks:
            if not any(f in s_text for f in match_forms(term)):
                continue
            tier = match_tier(rendering, hay_n, hay_l)
            rows.append({"block": bid, "term": term, "rendering": rendering,
                         "tier": {"exact": "EXACT", "loose": "LOOSE",
                                  "none": "MISSING"}[tier]})
            if tier == "none" or (tier == "loose" and not a.loose_is_pass):
                missing_blocks.add(bid)

    exact = sum(1 for r in rows if r["tier"] == "EXACT")
    loose = sum(1 for r in rows if r["tier"] == "LOOSE")
    miss = sum(1 for r in rows if r["tier"] == "MISSING")
    total = exact + loose + miss

    print(f"{'BLOCK':<8} {'LOCKED TERM':<22} {'RENDERING':<28} TIER")
    for r in rows:
        if r["tier"] != "EXACT":
            print(f"{r['block']:<8} {r['term']:<22} {r['rendering']:<28} {r['tier']}")
    print()
    print(f"blocks checked : {len(ids)}")
    print(f"lock instances : {total}   EXACT {exact} · LOOSE {loose} · MISSING {miss}")
    if total:
        print(f"landed         : {(exact + loose) / total:.0%} "
              f"({'LOOSE counted as landed' if a.loose_is_pass else 'EXACT only'})")

    if missing_blocks:
        print("\nRe-run these blocks solo with the lock restated:")
        print("  --force --batch 1 --only " + ",".join(sorted(missing_blocks)))

    if a.json:
        pathlib.Path(a.json).write_text(json.dumps({
            "glossary": a.glossary, "source": a.source, "translation": a.translation,
            "loose_is_pass": a.loose_is_pass,
            "totals": {"blocks": len(ids), "instances": total,
                       "exact": exact, "loose": loose, "missing": miss},
            "blocks_needing_rerun": sorted(missing_blocks),
            "rows": rows,
        }, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        print(f"\nreport: {a.json}")

    return 1 if missing_blocks else 0


if __name__ == "__main__":
    sys.exit(main())
