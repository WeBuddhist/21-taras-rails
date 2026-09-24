#!/usr/bin/env python3
"""
build_variant_menu.py
=====================
Build the consolidated bo->en variant menu that `glossary-select` chooses from,
sourced from the `keyword-extract` run's per-block en<->bo mappings rather than
from an interlinear gloss.

For each source-language lemma it emits every English rendering the pivot
(zero-shot) translation actually used, with an occurrence count and the block
IDs the rendering occurs in.

Usage:
  build_variant_menu.py --mappings-dir DIR --keyword-verses FILE \
      --registry FILE --out FILE [--pivot NAME] [--lang-pair bo-en]
"""

import argparse, glob, json, os, re, sys
from collections import defaultdict
from datetime import date


SUFFIXES = ("ations", "ation", "ingly", "ing", "ions", "ion", "ness", "ally",
            "edly", "ly", "es", "ed", "s")


def stem(phrase):
    """Crude derivational stem, for triage only — groups inflectional variants
    (`disease`/`diseases`, `pacification`/`pacifying`) so they are not mistaken
    for a genuine lexical choice. Never used to merge rows, only to label them."""
    out = []
    for word in re.split(r"[\s-]+", phrase.lower().strip()):
        if not word:
            continue
        for suf in SUFFIXES:
            if word.endswith(suf) and len(word) - len(suf) >= 3:
                word = word[: -len(suf)]
                break
        while len(word) > 4 and word[-1] in "yiec":
            word = word[:-1]
        out.append(word[:6])
    return " ".join(out)


def load_mappings(mappings_dir):
    """block_id -> [(en, bo)], drop:true rows excluded."""
    pairs = defaultdict(list)
    dropped = []
    files = sorted(glob.glob(os.path.join(mappings_dir, "*.json")))
    if not files:
        sys.exit(f"no mapping files found in {mappings_dir}")
    for path in files:
        with open(path, encoding="utf-8") as fh:
            data = json.load(fh)
        for block_id, rows in data.items():
            for row in rows:
                en, bo = row.get("en"), row.get("bo")
                if not en or not bo:
                    continue
                if row.get("drop"):
                    dropped.append((block_id, en, bo, row.get("note", "")))
                    continue
                pairs[block_id].append((en, bo))
    return pairs, dropped, files


def load_block_text(keyword_verses_path):
    """block_id -> pivot English text, reconstructed from the occurrence records."""
    with open(keyword_verses_path, encoding="utf-8") as fh:
        kv = json.load(fh)
    text = {}
    for rec in kv.values():
        for occ in rec.get("occurrences", []):
            vid = occ.get("verse_id")
            if vid and vid not in text:
                text[vid] = occ.get("text", "")
    return text


def count_in(text, phrase):
    """Word-boundary count of `phrase` in `text`, case-insensitive."""
    if not text or not phrase:
        return 0
    pat = r"(?<!\w)" + re.escape(phrase) + r"(?!\w)"
    return len(re.findall(pat, text, flags=re.IGNORECASE))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--mappings-dir", required=True)
    ap.add_argument("--keyword-verses", required=True)
    ap.add_argument("--registry", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--pivot", default="zero-shot")
    ap.add_argument("--lang-pair", default="bo-en")
    args = ap.parse_args()

    src_lang, tgt_lang = args.lang_pair.split("-", 1)

    pairs, dropped, mapping_files = load_mappings(args.mappings_dir)
    block_text = load_block_text(args.keyword_verses)

    with open(args.registry, encoding="utf-8") as fh:
        registry = json.load(fh)
    reg = {t["lemma"]: t for t in registry["terms"]}

    # bo -> en -> {"blocks": set, "count": int}
    menu = defaultdict(lambda: defaultdict(lambda: {"blocks": set(), "count": 0}))
    for block_id, rows in pairs.items():
        text = block_text.get(block_id, "")
        for en, bo in rows:
            cell = menu[bo][en]
            cell["blocks"].add(block_id)
            n = count_in(text, en)
            cell["count"] += n if n else 1  # attested at least once by the mapping

    def families(bo):
        """Distinct lexical families among a lemma's renderings."""
        fams = defaultdict(list)
        for en in menu[bo]:
            fams[stem(en)].append(en)
        return fams

    def sort_key(bo):
        t = reg.get(bo)
        return (0, t["rank"]) if t else (1, 0)

    lemmas = sorted(menu, key=sort_key)
    multi = [b for b in lemmas if len(menu[b]) > 1]
    lexical = [b for b in lemmas if len(families(b)) > 1]
    inflection_only = [b for b in multi if b not in set(lexical)]
    total_renderings = sum(len(menu[b]) for b in lemmas)
    unregistered = [b for b in lemmas if b not in reg]

    out = []
    out.append("---")
    out.append(f"language_pair: {args.lang_pair}")
    out.append(f"source_language: {src_lang}")
    out.append(f"target_language: {tgt_lang}")
    out.append(f"producer: glossary-select/scripts/build_variant_menu.py")
    out.append(f"pivot_translation: {args.pivot}")
    out.append("raw_sources:")
    for f in mapping_files:
        out.append(f"  - {f}")
    out.append(f"registry: {args.registry}")
    out.append(f"total_keywords: {len(lemmas)}")
    out.append(f"total_distinct_renderings: {total_renderings}")
    out.append(f"contested_keywords: {len(multi)}")
    out.append(f"lexically_contested: {len(lexical)}")
    out.append(f"inflection_only: {len(inflection_only)}")
    out.append(f"dropped_pairs: {len(dropped)}")
    out.append(f"generated: {date.today().isoformat()}")
    out.append("status: draft")
    out.append("---")
    out.append("")
    out.append(f"# Variant menu — {src_lang} → {tgt_lang}")
    out.append("")
    out.append(
        "Descriptive. Every English rendering the pivot translation actually used for each "
        f"{src_lang} lemma, with its occurrence count and the block IDs it occurs in. "
        "This is the menu `glossary-select` chooses from; it prescribes nothing."
    )
    out.append("")
    out.append(
        f"**{len(lexical)} of {len(lemmas)} lemmas need a real decision.** "
        f"{len(multi)} carry more than one rendering, but {len(inflection_only)} of those differ "
        "only by inflection (`disease`/`diseases`, `pacification`/`pacifying`) — one lexical "
        "choice covers them, and the translator inflects to fit the line. A lemma marked ⚑ has "
        "two or more genuinely distinct renderings; a lemma marked ~ has one lexical family in "
        "several forms. The grouping is a crude suffix heuristic for triage only — read the rows, "
        "not the mark."
    )
    out.append("")
    out.append("Keywords are ordered by the keyword run's composite rank, so the table can be "
               "worked top-down and stopped where the returns stop. Unregistered lemmas "
               "(present in the mapping, absent from the registry) sort last.")
    out.append("")
    out.append("Regenerate with `build_variant_menu.py`; do not hand-edit. To correct the data, "
               "fix the mapping files and re-run.")
    out.append("")

    for bo in lemmas:
        t = reg.get(bo)
        rank = t["rank"] if t else "—"
        match_form = t["match_form"] if t else "—"
        fams = families(bo)
        if len(fams) > 1:
            contested = " ⚑"
        elif len(menu[bo]) > 1:
            contested = " ~"
        else:
            contested = ""
        out.append(f"## {bo}{contested}")
        out.append("")
        out.append(f"- Rank: {rank} · Match form: `{match_form}`")
        out.append("")
        out.append("| Rendering | Count | Family | Blocks |")
        out.append("| --- | --- | --- | --- |")
        fam_ids = {k: i + 1 for i, k in enumerate(sorted(fams))}
        for en, cell in sorted(
            menu[bo].items(), key=lambda kv: (-kv[1]["count"], kv[0])
        ):
            blocks = ", ".join(sorted(cell["blocks"]))
            out.append(f"| {en} | {cell['count']} | {fam_ids[stem(en)]} | {blocks} |")
        out.append("")

    if dropped:
        out.append("---")
        out.append("")
        out.append("## Dropped pairs")
        out.append("")
        out.append("Pairs the keyword run adjudicated as extraction artefacts. Recorded so the "
                   "decision is visible, not silently lost.")
        out.append("")
        out.append("| Block | Rendering | Lemma | Note |")
        out.append("| --- | --- | --- | --- |")
        for block_id, en, bo, note in sorted(dropped):
            out.append(f"| {block_id} | {en} | {bo} | {note} |")
        out.append("")

    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    with open(args.out, "w", encoding="utf-8") as fh:
        fh.write("\n".join(out))

    print(f"wrote {args.out}")
    print(f"  lemmas: {len(lemmas)}  renderings: {total_renderings}")
    print(f"  contested: {len(multi)}  (lexical: {len(lexical)}, inflection-only: {len(inflection_only)})")
    print(f"  dropped pairs: {len(dropped)}  unregistered lemmas: {len(unregistered)}")


if __name__ == "__main__":
    main()
