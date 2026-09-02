#!/usr/bin/env python3
"""Step 3 of the translation-mediated term route: en -> bo enrichment, then ranking.

The YAKE/TF-IDF pass (4-SYSTEM/Skills/english-keyword-extraction) produced ranked
English keywords per verse. This script attaches the Tibetan term each English
keyword *renders in that verse* — read off the aligned Tibetan stanza with the
same block ID, not looked up in a dictionary — per the skill's Step 3 route (a).

It then does what the skill's "Feeding the article pipeline" section asks:
aggregates `bo` terms across verses and ranks them, here by the only measure
that predicts whether stage 4 will find anything — how many aligned commentary
spans, across how many distinct commentaries, actually contain the term.

Writes:
  work/root.en_en_bo_keyword_meaning_enriched.json   the bilingual candidate list
  work/term_candidates.md                            the ranked list for human review
  terms.yaml                                         written only with --write-terms
"""

from __future__ import annotations

import argparse
import json
from collections import defaultdict
from pathlib import Path

from kangyur_wiki.stages.align import load_alignment, spans_for_term
from kangyur_wiki.tibetan.normalize import nfc

CORPUS = Path("/tmp/iats/corpora/tara21")
WORK = CORPUS / "work"
YAKE = Path("/tmp/iats/vendor/skills/english-keyword-extraction/scripts/output/root.en-keyword_verses_yake.json")

# English keyword -> the Tibetan it renders, per verse. Read off the root stanza
# with the same block ID. Terms are given in citation form (terminal shad), the
# convention forum topic 289 uses and `registry.term_key` normalises away.
ENRICH: dict[str, list[tuple[str, str]]] = {
    "I-1": [("homage", "ཕྱག་འཚལ།"), ("noble lady tārā", "རྗེ་བཙུན་མ་འཕགས་མ་སྒྲོལ་མ།"), ("tārā", "སྒྲོལ་མ།")],
    "1-1": [("homage", "ཕྱག་འཚལ།"), ("tārā", "སྒྲོལ་མ།"), ("swift", "མྱུར་མ།"), ("valiant", "དཔའ་མོ།"),
            ("glance", "སྤྱན།"), ("lightning", "གློག"), ("triple world", "འཇིག་རྟེན་གསུམ་མགོན།"),
            ("lotus", "ཆུ་སྐྱེས།"), ("heart", "གེ་སར།")],
    "1-2": [("moon", "ཟླ་བ།"), ("autumn", "སྟོན་ཀ"), ("radiance", "འོད།"), ("stars", "སྐར་མ།"),
            ("countenance", "ཞལ།")],
    "1-3": [("golden", "སེར་སྔོ།"), ("lotus-hand", "པདྨ།"), ("generosity", "སྦྱིན་པ།"),
            ("diligence", "བརྩོན་འགྲུས།"), ("endurance", "དཀའ་ཐུབ།"), ("serenity", "ཞི་བ།"),
            ("patience", "བཟོད་པ།"), ("meditation", "བསམ་གཏན།")],
    "1-4": [("crown", "གཙུག་ཏོར།"), ("tathāgata", "དེ་བཞིན་གཤེགས་པ།"), ("perfections", "ཕ་རོལ་ཕྱིན་པ།"),
            ("heirs of the victors", "རྒྱལ་བའི་སྲས།"), ("victories", "རྣམ་པར་རྒྱལ་བ།")],
    "1-5": [("tuttāra", "ཏུཏྟཱ་ར།"), ("hūṃ", "ཧཱུཾ།"), ("seven worlds", "འཇིག་རྟེན་བདུན་པོ།"),
            ("summon", "འགུགས་པ།")],
    "1-6": [("indra", "བརྒྱ་བྱིན།"), ("agni", "མེ་ལྷ།"), ("brahmā", "ཚངས་པ།"), ("maruts", "རླུང་ལྷ།"),
            ("śiva", "དབང་ཕྱུག"), ("bhūtas", "འབྱུང་པོ།"), ("vetālas", "རོ་ལངས།"),
            ("gandharvas", "དྲི་ཟ།"), ("yakṣas", "གནོད་སྦྱིན།")],
    "1-7": [("traṭ", "ཊད།"), ("phaṭ", "ཕཊ།"), ("yantras", "འཁྲུལ་འཁོར།"), ("leg bent", "གཡས་བསྐུམས།")],
    "1-8": [("ture", "ཏུ་རེ།"), ("fearsome", "འཇིགས་པ་ཆེན་མོ།"), ("demons", "བདུད།"),
            ("furrowed brow", "ཁྲོ་གཉེར།"), ("foe", "དགྲ་བོ།")],
    "1-9": [("three jewels", "དཀོན་མཆོག་གསུམ།"), ("mudrā", "ཕྱག་རྒྱ།"), ("wheels", "འཁོར་ལོ།"),
            ("radiance", "འོད།")],
    "1-10": [("crown", "དབུ་རྒྱན།"), ("tuttāre", "ཏུཏྟཱ་ར།"), ("demons", "བདུད།"), ("smile", "བཞད་པ།")],
    "1-11": [("earthly guardians", "ས་གཞི་སྐྱོང་བ།"), ("hūṃ", "ཧཱུཾ།"), ("misfortune", "ཕོངས་པ།"),
             ("frown", "ཁྲོ་གཉེར།")],
    "1-12": [("moon", "ཟླ་བ།"), ("crown", "དབུ་རྒྱན།"), ("amitābha", "འོད་དཔག་མེད།"),
             ("locks", "རལ་བ།")],
    "1-13": [("apocalyptic flames", "བསྐལ་པའི་ཐ་མའི་མེ།"), ("enemies", "དགྲ།"),
             ("garland of flames", "འབར་བའི་ཕྲེང་བ།")],
    "1-14": [("hūṃ", "ཧཱུཾ།"), ("seven netherworlds", "རིམ་པ་བདུན་པོ།"), ("palms", "ཕྱག་མཐིལ།")],
    "1-15": [("blissful", "བདེ་མ།"), ("gracious", "དགེ་མ།"), ("tranquil", "ཞི་མ།"),
             ("nirvāṇa", "མྱ་ངན་འདས།"), ("oṃ", "ཨོཾ།"), ("svāhā", "སྭཱ་ཧཱ།"), ("evil", "སྡིག་པ།")],
    "1-16": [("ten syllables", "ཡི་གེ་བཅུ་པ།"), ("mantra", "སྔགས།"), ("hūṃ", "ཧཱུཾ།"),
             ("wisdom-syllable", "རིག་པ།"), ("foes", "དགྲ།")],
    "1-17": [("ture", "ཏུ་རེ།"), ("seed", "ས་བོན།"), ("meru", "རི་རབ།"), ("mandara", "མནྡྷ་ར།"),
             ("vindhya", "འབིགས་བྱེད།"), ("three worlds", "འཇིག་རྟེན་གསུམ།")],
    "1-18": [("divine lake", "ལྷ་ཡི་མཚོ།"), ("deer-marked", "རི་དྭགས་རྟགས་ཅན།"), ("tāra", "ཏཱ་ར།"),
             ("phaṭ", "ཕཊ།"), ("poisons", "དུག")],
    "1-19": [("gods", "ལྷ།"), ("kiṃnaras", "མིའམ་ཅི།"), ("armour", "གོ་ཆ།"),
             ("nightmares", "རྨི་ལམ་ངན་པ།"), ("strife", "རྩོད།")],
    "1-20": [("sun and moon", "ཉི་མ་ཟླ་བ།"), ("eyes", "སྤྱན།"), ("hara", "ཧ་ར།"),
             ("tuttāre", "ཏུཏྟཱ་ར།"), ("diseases", "རིམས་ནད།")],
    "1-21": [("three realities", "དེ་ཉིད་གསུམ།"), ("grahas", "གདོན།"), ("vetālas", "རོ་ལངས།"),
             ("yakṣas", "གནོད་སྦྱིན།"), ("ture", "ཏུ་རེ།"), ("peace", "ཞི་བ།")],
    "1-22": [("root mantra", "རྩ་བའི་སྔགས།"), ("praise", "བསྟོད་པ།"),
             ("twenty-one verses of homage", "ཕྱག་འཚལ་བ་ཉི་ཤུ་རྩ་གཅིག")],
}

# The benefit verses (English 22-27) have no Tibetan counterpart in this upload's
# root edition, which stops at the closing couplet. Their terms are still real —
# every commentary discusses ཕན་ཡོན — so they are carried with a note.
ENRICH_NO_ROOT: dict[str, list[tuple[str, str]]] = {
    "2-1": [("devotion", "མོས་གུས།"), ("goddess", "ལྷ་མོ།")],
    "2-2": [("fearlessness", "མི་འཇིགས་པ།"), ("misdeeds", "སྡིག་པ།"), ("evil destinies", "ངན་འགྲོ།")],
    "2-3": [("empowerment", "དབང་བསྐུར།"), ("buddhahood", "བྱང་ཆུབ།")],
    "2-4": [("poison", "དུག")],
    "2-5": [("spirits", "གདོན།"), ("pestilence", "རིམས་ནད།")],
    "2-6": [("progeny", "བུ།"), ("riches", "ནོར།"), ("obstacles", "བར་ཆད།")],
}

NOTE_NO_ROOT = "benefit verse; not in this upload's root edition (f003 stops at the closing couplet)"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--write-terms", action="store_true",
                    help="write terms.yaml from the ranked candidates (human-review gate)")
    ap.add_argument("--top", type=int, default=40)
    args = ap.parse_args()

    yake = json.loads(YAKE.read_text(encoding="utf-8")) if YAKE.exists() else {}
    root_en = {}
    for block in (WORK / "root.en.md").read_text(encoding="utf-8").split("\n\n"):
        block = block.strip()
        if "^" in block:
            vid = block.rsplit("^", 1)[1].strip()
            root_en[vid] = block.rsplit("^", 1)[0].strip()

    enriched: dict[str, dict] = {}
    for table, note in ((ENRICH, None), (ENRICH_NO_ROOT, NOTE_NO_ROOT)):
        for vid, pairs in table.items():
            yk = {k["key"]: k for k in yake.get(vid, {}).get("keywords", [])}
            kws = []
            for rank, (en, bo) in enumerate(pairs, start=1):
                entry = {
                    "key": en,
                    "rank": yk.get(en, {}).get("rank", rank),
                    "score": yk.get(en, {}).get("score", None),
                    "count": yk.get(en, {}).get("count", 1),
                    "bo": nfc(bo),
                }
                if note:
                    entry["note"] = note
                kws.append(entry)
            enriched[vid] = {"text": root_en.get(vid, ""), "keywords": kws}

    out = WORK / "root.en_en_bo_keyword_meaning_enriched.json"
    out.write_text(json.dumps(enriched, ensure_ascii=False, indent=2), encoding="utf-8")
    n_kw = sum(len(v["keywords"]) for v in enriched.values())
    print(f"{out.name}: {len(enriched)} verses, {n_kw} enriched keywords")

    # ---- aggregate + rank against the alignment ----
    alignment = load_alignment(WORK / "aligned.json")
    agg: dict[str, dict] = {}
    for vid, v in enriched.items():
        for kw in v["keywords"]:
            rec = agg.setdefault(kw["bo"], {"bo": kw["bo"], "en": set(), "verses": set()})
            rec["en"].add(kw["key"])
            rec["verses"].add(vid)

    rows = []
    for bo, rec in agg.items():
        spans = spans_for_term(alignment, bo)
        sources = {s.source_id for s in spans}
        rows.append({
            "term": bo,
            "en": sorted(rec["en"]),
            "verses": sorted(rec["verses"]),
            "spans": len(spans),
            "commentaries": len(sources),
        })
    rows.sort(key=lambda r: (-r["commentaries"], -r["spans"], r["term"]))

    md = ["# tara21 — candidate key terms (translation-mediated route)", "",
          "Ranked by how much *aligned commentary* actually discusses the term: the number of",
          "distinct commentaries first, then the number of aligned spans. A term with 0 spans",
          "cannot produce an article from this corpus, however central it is to the text.",
          "",
          "A human approves this list before anything downstream runs (PLAN.md §3, stage 3).",
          "",
          "| # | term (bo) | commentaries | spans | root verses | English keyword(s) |",
          "|---|---|---|---|---|---|"]
    for i, r in enumerate(rows, start=1):
        md.append(f"| {i} | {r['term']} | {r['commentaries']} | {r['spans']} | "
                  f"{', '.join(r['verses'][:6])}{' …' if len(r['verses']) > 6 else ''} | "
                  f"{', '.join(r['en'][:4])} |")
    (WORK / "term_candidates.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    (WORK / "term_candidates.json").write_text(
        json.dumps(rows, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"term_candidates.md: {len(rows)} candidates, "
          f"{sum(1 for r in rows if r['spans'] == 0)} with no aligned material")
    for r in rows[:args.top]:
        print(f"  {r['commentaries']:2d} comm  {r['spans']:4d} spans  {r['term']}")

    if args.write_terms:
        keep = [r for r in rows if r["spans"] > 0]
        y = ["version: 1", "corpus_id: tara21",
             "corpus_name: སྒྲོལ་མ་ལ་ཕྱག་འཚལ་ཉི་ཤུ་རྩ་གཅིག་གིས་བསྟོད་པ",
             "# Candidate list from the translation-mediated route",
             "# (zeroshot/published en translation -> YAKE + TF-IDF -> en->bo enrichment).",
             "# NOT a curated list from the team's sheet: every row still needs human review.",
             "# `status: candidate` marks that. Ranked by aligned-commentary support;",
             "# candidates with no aligned material at all are omitted (see work/term_candidates.md).",
             "terms:"]
        for r in keep:
            y += [f'- term: "{r["term"]}"',
                  "  editor: null",
                  "  status: candidate",
                  "  wikipedia_url: null"]
        (CORPUS / "terms.yaml").write_text("\n".join(y) + "\n", encoding="utf-8")
        print(f"terms.yaml: {len(keep)} candidate terms written")


if __name__ == "__main__":
    main()
