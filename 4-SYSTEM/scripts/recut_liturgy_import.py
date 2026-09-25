#!/usr/bin/env python3
"""recut_liturgy_import.py — re-align imported machine translations onto this vault's root text.

Why this exists. Six zero-shot translations of the Twenty-One Praises (en, zh
from DharmaMitra; hi, mn, ne, vi from Gemini) were produced in the sibling
Liturgy vault against a FLAT block numbering (^1 … ^29) of an earlier cut of the
same critical edition. This vault's root text carries the rails ids (^I-1 …
^a-1) and cuts the same 112 content lines differently in three places (the
title formula, homage 21 + closing couplet, and the benefits section). Every
one of the six translations is line-parallel to the old cut — verified: the
same line count in every block — so the translation can be re-cut onto the
new ids mechanically, line by line, with no re-translation and no guessing.

What it writes, per language, into <track>/work/:

    <new stem>-<tag>.jsonl        a new ledger: one record per NEW block id, in
                                  source order. Each record is the old record
                                  with block_id/heading/source/translation
                                  replaced and a `recut` object recording the
                                  old id(s), the old source text and any line
                                  whose Tibetan reading changed.
    extra-fm.json                 the researched title, backend ids and import
                                  provenance the renderer cannot know, fed to
                                  the renderer with --extra-fm.

and then re-renders the track (dm_translate.py / gm_translate.py
--render-only). The original Liturgy ledger and rendered file stay untouched
under <track>/work/imported-from-liturgy-rails/ as the audit trail.

The old→new map is explicit (MAP below) and every group is checked: the
concatenated old source lines must count exactly the concatenated new source
lines, or the run aborts. Reading changes inside a line are allowed and are
REPORTED, never hidden — they are the blocks a human may want re-translated.

Usage (from the vault root):
    python3 4-SYSTEM/scripts/recut_liturgy_import.py --lang en            # one language
    python3 4-SYSTEM/scripts/recut_liturgy_import.py --all                # all six
    python3 4-SYSTEM/scripts/recut_liturgy_import.py --all --dry-run      # report only
"""

from __future__ import annotations

import argparse
import datetime as _dt
import importlib.util
import json
import pathlib
import subprocess
import sys

VAULT = pathlib.Path(__file__).resolve().parents[2]
# dharmamitra-translate moved to the shared repo (rails/machine-translate) on
# 2026-09-24; the vault copy is archived. Prefer the shared copy next to the vault.
DM = next((p for p in (
    VAULT.parent / "Webuddhist-Skills/rails/machine-translate/scripts/dm_translate.py",
    VAULT / "4-SYSTEM/Skills/_archive/dharmamitra-translate/scripts/dm_translate.py",
) if p.exists()), VAULT.parent / "Webuddhist-Skills/rails/machine-translate/scripts/dm_translate.py")
GM = VAULT / "4-SYSTEM/Skills/gemini-translate/scripts/gm_translate.py"

NEW_ROOT = VAULT / "1-SOURCES/Text/bo-སྒྲོལ་མ་ཉེར་གཅིག་ལ་བསྟོད་པ།.md"
OLD_ROOT = VAULT / "0-INBOX/liturgy-import-2026-09-17/old-root-liturgy-1-SOURCES-སྒྲོལ་མ་ཉེར་གཅིག་ལ་བསྟོད་པ།.md"
OLD_STEM = "སྒྲོལ་མ་ཉེར་གཅིག་ལ་བསྟོད་པ།"          # the Liturgy file stem
IMPORT_DIR = "imported-from-liturgy-rails"

# Live backend ids (library.webuddhist.com, checked 2026-09-17): the root text
# was rebuilt in place, so its ids did not change; each translation TEXT
# survives (its edition was deleted on 2026-09-16 and is re-created by the
# uploader under the same text id).
ROOT_TEXT_ID = "HyUbHGlzS9LsSrgiFQNYE"
ROOT_EDITION_ID = "lEmYv8BrRQkOMPY9ymQpS"
CATEGORY_ID = "LCorCb2K98p3TICt3UCDm"

TRACKS = {
    # tag: (generator folder, language label, live translation text_id, deleted edition_id, site)
    "en": ("Dharmamitra", "english",        "W5o6Tyq3hhQDxhmvdoS7B", "e9YaE4tRs6nI6BU1GeUAE", "https://dharmamitra.org"),
    "zh": ("Dharmamitra", "modern chinese", "O9TxCvL6lhjufpaaOAxAj", "1PHcxVLm39uAPyIVNX6mt", "https://dharmamitra.org"),
    "hi": ("Gemini",      "hindi",          "4NECafzLDkznK7jBxfmHU", "TdhnVTFd3LPTVwRKIkDAC", "https://ai.google.dev"),
    "mn": ("Gemini",      "mongolian",      "7n1BhMN4FNkyaThaBtn3g", "utJelSsTLEzpZemZYfJaB", "https://ai.google.dev"),
    "ne": ("Gemini",      "nepali",         "QGjmqg2hVtIjqJdifTVUV", "cGZFmk4GaMBQQvcGzSZbC", "https://ai.google.dev"),
    "vi": ("Gemini",      "vietnamese",     "vROdFp8qvU9rNYMEwhdjl", "7tOp99UHXoCuVI7raglBw", "https://ai.google.dev"),
}

# Old flat ids -> new rails ids. A group pools the lines of its old blocks, in
# order, and deals them out to its new blocks by the new blocks' line counts.
MAP = (
    [(["1"], ["I-1", "I-2"]), (["2"], ["I-3"])]
    + [([str(o)], [f"1-{n}"]) for o, n in zip(range(3, 23), range(1, 21))]
    + [(["23"], ["1-21", "1-22"]),
       (["24", "25", "26", "27", "28"], ["2-1", "2-2", "2-3", "2-4", "2-5", "2-6"]),
       (["29"], ["a-1"])]
)


def load_dm():
    spec = importlib.util.spec_from_file_location("dm_translate", DM)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def latest_records(path):
    latest = {}
    for line in pathlib.Path(path).read_text(encoding="utf-8").splitlines():
        if line.strip():
            r = json.loads(line)
            if r.get("kind") == "heading":
                continue
            latest[r["block_id"]] = r
    return latest


def recut(tag, dm, dry_run=False, force=False):
    gen, label, text_id, old_edition, site = TRACKS[tag]
    track = VAULT / "3-TRANSFORMATIONS/Translations/machine-drafts/zero-shot" / f"{gen.lower()}-{tag}"
    old_led = track / "work" / IMPORT_DIR / f"{OLD_STEM}-{tag}.jsonl"
    old_md = track / "work" / IMPORT_DIR / f"{OLD_STEM}-{tag}.md"
    if not old_led.exists() or not old_md.exists():
        sys.exit(f"{tag}: imported Liturgy files missing under {track / 'work' / IMPORT_DIR}")

    _, old_units = dm.parse_source(OLD_ROOT)
    new_meta, new_units = dm.parse_source(NEW_ROOT)
    old_blocks = {u["id"]: u for u in old_units if u["kind"] == "block" and u["id"]}
    new_blocks = {u["id"]: u for u in new_units if u["kind"] == "block" and u["id"]}
    new_order = [u["id"] for u in new_units if u["kind"] == "block" and u["id"]]
    old_recs = latest_records(old_led)

    # every new id must be produced exactly once, in source order
    produced = [n for _, news in MAP for n in news]
    assert produced == new_order, f"MAP does not cover the new root in order: {produced} vs {new_order}"

    new_recs, changed, report = {}, [], []
    for olds, news in MAP:
        old_src = [l for o in olds for l in old_blocks[o]["lines"]]
        old_tr = [l for o in olds for l in old_recs[o]["translation"].split("\n") if l.strip()]
        new_src = [l for n in news for l in new_blocks[n]["lines"]]
        if len(old_src) != len(new_src):
            sys.exit(f"{tag}: group {olds}->{news}: {len(old_src)} old source lines vs {len(new_src)} new")
        if len(old_tr) != len(old_src):
            sys.exit(f"{tag}: group {olds}->{news}: translation has {len(old_tr)} lines for {len(old_src)} source lines — not line-parallel, refusing to re-cut")
        # line-level reading diffs, reported per new block
        pos = 0
        for n in news:
            unit = new_blocks[n]
            k = len(unit["lines"])
            tr_lines = old_tr[pos: pos + k]
            src_old = old_src[pos: pos + k]
            diffs = [(i + 1, a, b) for i, (a, b) in enumerate(zip(src_old, unit["lines"])) if a != b]
            base = old_recs[olds[0]] if len(olds) == 1 else old_recs[olds[min(len(olds) - 1, 0)]]
            # for a pooled group take the old record whose block held the FIRST line of this new block
            if len(olds) > 1:
                acc = 0
                for o in olds:
                    if acc <= pos < acc + len(old_blocks[o]["lines"]):
                        base = old_recs[o]
                        break
                    acc += len(old_blocks[o]["lines"])
            rec = dict(base)
            rec["block_id"] = n
            rec["heading"] = unit["heading"]
            rec["source"] = unit["text"]
            rec["translation"] = "\n".join(tr_lines)
            if "line_parity" in rec:
                rec["line_parity"] = True
            rec["recut"] = {
                "from_block_ids": olds if len(olds) > 1 else olds[0],
                "from_ledger": f"work/{IMPORT_DIR}/{OLD_STEM}-{tag}.jsonl",
                "from_vault": "Liturgy-rails",
                "old_source": "\n".join(src_old),
                "ts": _dt.datetime.now().isoformat(timespec="seconds"),
                "source_reading_changed": bool(diffs),
                "changed_lines": [{"line": i, "old": a, "new": b} for i, a, b in diffs],
            }
            new_recs[n] = rec
            if diffs:
                changed.append((n, diffs))
            pos += k
        report.append(f"  {'+'.join(olds):>14} -> {', '.join(news)}  ({len(new_src)} lines)")

    print(f"== {tag} ({gen}, {label}) ==")
    print("\n".join(report))
    if changed:
        print(f"  reading changed inside {len(changed)} new block(s) — translation carried over, review these:")
        for n, diffs in changed:
            for i, a, b in diffs:
                print(f"    ^{n} line {i}:\n      old: {a}\n      new: {b}")
    if dry_run:
        return

    new_stem = NEW_ROOT.stem
    new_led = track / "work" / f"{new_stem}-{tag}.jsonl"
    if new_led.exists() and not force:
        sys.exit(f"{tag}: {new_led} already exists; pass --force to rebuild it from the import")
    with new_led.open("w", encoding="utf-8") as fh:
        for n in new_order:
            fh.write(json.dumps(new_recs[n], ensure_ascii=False) + "\n")
    print(f"  wrote {new_led.relative_to(VAULT)}  ({len(new_recs)} records)")

    old_fm = dm.read_frontmatter(old_md)
    extra = {
        "title": old_fm.get("title_translated") or old_fm.get("title", ""),
        "title_original": old_fm.get("title_original", ""),
        "title_attested": old_fm.get("title_attested", ""),
        "title_source": old_fm.get("title_source", ""),
        "text_id": text_id,
        "edition_id": "",
        "toc_id": "",
        "previous_edition_id": f"{old_edition} (deleted 2026-09-16 with its alignment; re-created by the uploader)",
        "translation_of_text_id": ROOT_TEXT_ID,
        "translation_of_edition_id": ROOT_EDITION_ID,
        "category_id": CATEGORY_ID,
        "license": old_fm.get("license", "public"),
        "source": old_fm.get("source", site),
        "imported_from": f"Liturgy-rails/3-TRANSFORMATIONS/Translations/{gen}/{tag}/{OLD_STEM}-{tag}.md",
        "import_note": (f"Imported 2026-09-17 and re-cut line by line from the Liturgy flat ids ^1-^29 "
                        f"onto this vault's rails ids (recut_liturgy_import.py); the original ledger and "
                        f"render are kept under work/{IMPORT_DIR}/. Reading changes in the Tibetan are "
                        f"recorded per block in the ledger's `recut.changed_lines`."),
    }
    extra_path = track / "work" / "extra-fm.json"
    extra_path.write_text(json.dumps(extra, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    script = DM if gen == "Dharmamitra" else GM
    cmd = [sys.executable, str(script), "--source", str(NEW_ROOT.relative_to(VAULT)),
           "--lang", label, "--lang-tag", tag, "--out", str(track.relative_to(VAULT)),
           "--render-only", "--extra-fm", str(extra_path.relative_to(VAULT))]
    if gen == "Dharmamitra":
        cmd += ["--batch", "5"]     # what the imported en/zh records were produced under
    print("  $ " + " ".join(cmd[1:]))
    subprocess.run(cmd, cwd=VAULT, check=True)


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--lang", default=None, help="one tag: en zh hi mn ne vi")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--dry-run", action="store_true", help="report the map and reading changes, write nothing")
    ap.add_argument("--force", action="store_true", help="overwrite an existing re-cut ledger")
    args = ap.parse_args()
    tags = list(TRACKS) if args.all else ([args.lang] if args.lang else [])
    if not tags:
        ap.error("give --lang <tag> or --all")
    dm = load_dm()
    for tag in tags:
        recut(tag, dm, dry_run=args.dry_run, force=args.force)


if __name__ == "__main__":
    main()
