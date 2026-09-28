#!/usr/bin/env python3
"""Compare a direct-from-Tibetan Gemini run against the English-mediated registry.

Two routes to the same target — a list of Tibetan key terms with per-block
provenance:

  A  keyword-extract : Tibetan -> English translation -> YAKE/TF-IDF candidates
                       -> map each occurrence back -> regroup by Tibetan term
  B  gemini-keyword-extract : ask a model to read the Tibetan directly

Neither is ground truth, so this script does not score one against the other. It
reports where they agree, what each finds alone, and — the part that actually
decides anything — whether the disagreements are *real terms* or artefacts.

Matching is on the normalised Tibetan string (tsheg/shad/anusvara-insensitive),
because the two routes hold their terms in different citation conventions:
registry lemmas end in a shad, Gemini copies the running form. Comparing raw
strings would report near-total disagreement and be meaningless.

Stdlib only.
"""
from __future__ import annotations

import argparse
import json
import pathlib
import re
import sys

VAULT = pathlib.Path(__file__).resolve().parents[4]


def norm(s: str) -> str:
    s = (s or "").replace("ྃ", "ཾ")
    return re.sub(r"[་།༎\s༑]+", "", s)


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--gemini", required=True, help="gk_extract.py output")
    p.add_argument("--registry", default=str(VAULT / "2-RAILS/Keywords/source-term-registry.json"))
    p.add_argument("--source", required=True, help="the Tibetan root text")
    p.add_argument("--out", help="write the full comparison JSON here")
    p.add_argument("--md", help="write a readable report here")
    p.add_argument("--drop-absent", action="store_true",
                   help="exclude Gemini terms graded ABSENT (default: keep, flagged)")
    a = p.parse_args(argv)

    gem = json.loads(pathlib.Path(a.gemini).read_text(encoding="utf-8"))
    reg = json.loads(pathlib.Path(a.registry).read_text(encoding="utf-8"))
    root = pathlib.Path(a.source).read_text(encoding="utf-8")

    # ---- side B: Gemini, normalised, with the blocks it was attributed to
    g_terms: dict[str, dict] = {}
    for bid, rows in gem["by_block"].items():
        for r in rows:
            if a.drop_absent and r["verification"] == "ABSENT":
                continue
            k = norm(r["term"])
            if not k:
                continue
            e = g_terms.setdefault(k, {"surfaces": set(), "blocks": set(),
                                       "glosses": set(), "kinds": set(),
                                       "verification": set()})
            e["surfaces"].add(r["term"])
            e["blocks"].add(bid)
            if r.get("gloss_en"):
                e["glosses"].add(r["gloss_en"])
            if r.get("kind"):
                e["kinds"].add(r["kind"])
            e["verification"].add(r["verification"])

    # ---- side A: the registry, restricted to terms that occur in THIS text,
    #      because that is the only population the two routes both had access to.
    r_terms: dict[str, dict] = {}
    for t in reg["terms"]:
        if t.get("dropped"):
            continue
        mf = t.get("match_form") or ""
        if mf not in root and mf.rstrip("་") not in root:
            continue
        k = norm(t["lemma"])
        if not k:
            continue
        r_terms[k] = {"lemma": t["lemma"], "rank": t.get("rank"),
                      "glosses": t.get("english_renderings") or [],
                      "blocks": set(t.get("root_text_blocks") or [])}

    both = sorted(set(g_terms) & set(r_terms))
    only_g = sorted(set(g_terms) - set(r_terms))
    only_r = sorted(set(r_terms) - set(g_terms))

    # ---- provenance agreement, on the terms both routes found
    prov_same, prov_diff, prov_nocmp = [], [], []
    for k in both:
        gb, rb = g_terms[k]["blocks"], r_terms[k]["blocks"]
        if not rb:
            prov_nocmp.append(k)
        elif gb == rb:
            prov_same.append(k)
        else:
            prov_diff.append((k, sorted(gb), sorted(rb)))

    # ---- how the registry ranked what Gemini missed: the question that matters
    missed_by_rank = sorted(
        ((r_terms[k]["rank"] or 10**6, k) for k in only_r))[:25]
    top50 = {k for k in r_terms if (r_terms[k]["rank"] or 10**6) <= 50}
    top50_found = len(top50 & set(g_terms))

    tot_g, tot_r = len(g_terms), len(r_terms)
    overlap_pct = f"{len(both) / max(1, min(tot_g, tot_r)):.0%}"

    print("=" * 62)
    print("  A  keyword-extract registry (terms occurring in this text)")
    print("  B  gemini-keyword-extract, direct from Tibetan")
    print("=" * 62)
    print(f"A terms            : {tot_r}")
    print(f"B terms            : {tot_g}"
          + (" (ABSENT dropped)" if a.drop_absent else " (ABSENT kept, flagged)"))
    print(f"in both            : {len(both)}   ({overlap_pct} of the smaller side)")
    print(f"only A             : {len(only_r)}")
    print(f"only B             : {len(only_g)}")
    print()
    print(f"A's top 50 by rank : {top50_found}/{len(top50)} also found by B")
    print()
    print("provenance, on terms both found:")
    print(f"  same block set   : {len(prov_same)}")
    print(f"  different        : {len(prov_diff)}")
    print(f"  A had no blocks  : {len(prov_nocmp)}")
    if not a.drop_absent:
        v = gem.get("verification", {})
        print()
        print(f"B verification     : VERBATIM {v.get('VERBATIM', 0)} · "
              f"NORMALIZED {v.get('NORMALIZED', 0)} · ABSENT {v.get('ABSENT', 0)}")

    print("\nHighest-ranked A terms B did not find:")
    for rank, k in missed_by_rank[:15]:
        t = r_terms[k]
        print(f"  {rank:>4}  {t['lemma']:<22} {', '.join(t['glosses'][:2])}")

    print("\nB terms A does not have (first 20):")
    for k in only_g[:20]:
        e = g_terms[k]
        flag = "" if e["verification"] == {"VERBATIM"} else f"  [{'/'.join(sorted(e['verification']))}]"
        print(f"  {sorted(e['surfaces'])[0]:<26} {', '.join(sorted(e['glosses'])[:1])}{flag}")

    payload = {
        "schema": "keyword-route-comparison/1",
        "a_registry": a.registry, "b_gemini": a.gemini,
        "a_terms": tot_r, "b_terms": tot_g,
        "in_both": len(both), "only_a": len(only_r), "only_b": len(only_g),
        "a_top50_found_by_b": f"{top50_found}/{len(top50)}",
        "provenance": {"same": len(prov_same), "different": len(prov_diff),
                       "a_had_no_blocks": len(prov_nocmp),
                       "differences": [{"term": k, "b_blocks": gb, "a_blocks": rb}
                                       for k, gb, rb in prov_diff]},
        "b_verification": gem.get("verification"),
        "only_a_terms": [{"lemma": r_terms[k]["lemma"], "rank": r_terms[k]["rank"],
                          "glosses": r_terms[k]["glosses"]} for k in only_r],
        "only_b_terms": [{"surfaces": sorted(g_terms[k]["surfaces"]),
                          "glosses": sorted(g_terms[k]["glosses"]),
                          "kinds": sorted(g_terms[k]["kinds"]),
                          "blocks": sorted(g_terms[k]["blocks"]),
                          "verification": sorted(g_terms[k]["verification"])}
                         for k in only_g],
        "in_both_terms": [{"lemma": r_terms[k]["lemma"],
                           "b_surfaces": sorted(g_terms[k]["surfaces"]),
                           "rank": r_terms[k]["rank"]} for k in both],
    }
    if a.out:
        pathlib.Path(a.out).write_text(
            json.dumps(payload, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        print(f"\nfull comparison: {a.out}")

    if a.md:
        v = gem.get("verification", {})
        lines = [
            "# Keyword route comparison — A (English-mediated) vs B (Gemini on Tibetan)",
            "",
            f"- **A** `{a.registry}` — `keyword-extract`, restricted to the {tot_r} terms that "
            f"occur in this root text (the only population both routes could see).",
            f"- **B** `{a.gemini}` — `gemini-keyword-extract`, model "
            f"`{gem.get('model')}`, {gem.get('blocks_processed')} blocks in "
            f"batches of {gem.get('batch')}.",
            "",
            "Neither route is ground truth. This report says where they agree and what each "
            "sees alone; it does not score one against the other.",
            "",
            "## Totals",
            "",
            "| | count |",
            "|---|---|",
            f"| A terms (in this text) | {tot_r} |",
            f"| B terms | {tot_g} |",
            f"| found by both | {len(both)} |",
            f"| only A | {len(only_r)} |",
            f"| only B | {len(only_g)} |",
            f"| A's top 50 by rank, also found by B | {top50_found}/{len(top50)} |",
            "",
            "Matching is on the tsheg/shad/anusvara-normalised Tibetan string: the two routes "
            "hold terms in different citation conventions (A's lemmas end in a shad, B copies "
            "the running form), so raw-string comparison would report near-total disagreement "
            "and mean nothing.",
            "",
            "## B's self-verification",
            "",
            "Every term B returned was checked against the block it was attributed to:",
            "",
            "| grade | count | meaning |",
            "|---|---|---|",
            f"| VERBATIM | {v.get('VERBATIM', 0)} | the exact string is in that block |",
            f"| NORMALIZED | {v.get('NORMALIZED', 0)} | present after normalisation — a citation form |",
            f"| ABSENT | {v.get('ABSENT', 0)} | not in the block — paraphrase, conflation or invention |",
            "",
            "## Provenance agreement (terms both routes found)",
            "",
            "| | count |",
            "|---|---|",
            f"| identical block set | {len(prov_same)} |",
            f"| different block set | {len(prov_diff)} |",
            f"| A recorded no blocks | {len(prov_nocmp)} |",
            "",
            "## Highest-ranked A terms that B did not find",
            "",
            "A's rank is the composite score (claim density / structure / presence). A miss "
            "high in this list matters more than a long tail of misses.",
            "",
            "| A rank | lemma | glosses |",
            "|---|---|---|",
        ]
        for rank, k in missed_by_rank:
            t = r_terms[k]
            lines.append(f"| {rank} | {t['lemma']} | {', '.join(t['glosses'][:3])} |")
        lines += ["", "## Terms B found that A does not have", "",
                  "| term | gloss | kind | blocks | verification |", "|---|---|---|---|---|"]
        for k in only_g:
            e = g_terms[k]
            lines.append(f"| {sorted(e['surfaces'])[0]} | {', '.join(sorted(e['glosses'])[:2])} "
                         f"| {', '.join(sorted(e['kinds'])[:2])} "
                         f"| {', '.join(sorted(e['blocks'])[:6])} "
                         f"| {'/'.join(sorted(e['verification']))} |")
        pathlib.Path(a.md).write_text("\n".join(lines) + "\n", encoding="utf-8")
        print(f"report         : {a.md}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
