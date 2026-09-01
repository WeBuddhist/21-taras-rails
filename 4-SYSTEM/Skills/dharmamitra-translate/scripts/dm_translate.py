#!/usr/bin/env python3
"""dm_translate.py — block-by-block zero-shot translation via DharmaMitra cat-translate.

Reads a block-ID'd source file from 1-SOURCES/, sends ONE block (one verse /
one prose block) per API call, threads the previously translated blocks back in
as rolling context, and writes both an append-only JSONL ledger (audit trail,
resume point) and a rendered block-ID-aligned markdown translation.

Never writes to 1-SOURCES/. Output goes to a machine-baseline track folder under
3-TRANSFORMATIONS/Translations/ and never replaces an existing human or
rails-generated translation.

Endpoint: POST https://dharmamitra.org/api-search/cat-translate/v1/translate
No API key. Stdlib only (urllib) — no pip install.

Usage:
  dm_translate.py --source 1-SOURCES/Text/<file>.md --lang english
  dm_translate.py --source ... --lang german --limit 3          # smoke test
  dm_translate.py --source ... --lang english --only 1-1,1-2
  dm_translate.py --source ... --lang english --render-only     # re-render from ledger
  dm_translate.py --source ... --list                           # parse check, no calls
"""

import argparse
import datetime as _dt
import json
import os
import pathlib
import re
import sys
import time
import urllib.error
import urllib.request

RATE_LIMIT_BACKOFF = [20, 40, 60, 90, 120, 180]

ENDPOINT = os.environ.get(
    "DHARMAMITRA_CAT_TRANSLATE_URL",
    "https://dharmamitra.org/api-search/cat-translate/v1/translate",
)

BLOCK_ID_RE = re.compile(r"[ \t]\^([A-Za-z0-9][A-Za-z0-9._-]*)[ \t]*$")

# Language label -> vault lang tag. Extend as new tracks are commissioned.
LANG_TAGS = {
    "english": "en", "german": "de", "french": "fr", "spanish": "es",
    "italian": "it", "portuguese": "pt", "russian": "ru", "hindi": "hi",
    "nepali": "ne", "sinhala": "si", "bengali": "bn", "thai": "th",
    "vietnamese": "vi", "japanese": "ja", "korean": "ko", "mongolian": "mn",
    "chinese": "zh", "modern chinese": "zh", "indonesian": "id",
}

DEFAULT_STYLE = (
    "Translate this Tibetan verse of praise line by line: render each Tibetan "
    "line as one line of the target language, in the same order, and keep the "
    "same number of lines as the source. Devotional but clear register. Keep "
    "mantra syllables and proper names in transliteration rather than "
    "translating them. Do not add commentary, notes, or explanation."
)

SOURCE_LANG_FIELDS = {
    "tibetan": "input_tibetan",
    "sanskrit": "input_sanskrit",
    "chinese": "input_chinese",
    "pali": "input_pali",
}


# ---------------------------------------------------------------- parsing


def parse_source(path):
    """Return (frontmatter_dict_partial, [unit, ...]).

    unit = {"kind": "heading"|"block", "id": str|None, "text": str,
            "lines": [str], "heading": str|None}
    """
    raw = pathlib.Path(path).read_text(encoding="utf-8")
    lines = raw.split("\n")

    meta = {}
    if lines and lines[0].strip() == "---":
        for i in range(1, len(lines)):
            if lines[i].strip() == "---":
                for fm_line in lines[1:i]:
                    m = re.match(r"^([A-Za-z_][A-Za-z0-9_]*):\s*(.*)$", fm_line)
                    if m:
                        meta[m.group(1)] = m.group(2).strip().strip('"')
                lines = lines[i + 1:]
                break

    units, buf, current_heading = [], [], None

    def flush():
        nonlocal buf
        if not buf:
            return
        body = [l for l in buf if l.strip()]
        buf = []
        if not body:
            return
        m = BLOCK_ID_RE.search(body[-1])
        block_id = m.group(1) if m else None
        if m:
            body[-1] = body[-1][: m.start()].rstrip()
        units.append({
            "kind": "block",
            "id": block_id,
            "lines": body,
            "text": "\n".join(body),
            "heading": current_heading,
        })

    for line in lines:
        stripped = line.strip()
        if not stripped:
            flush()
            continue
        if stripped.startswith("#"):
            flush()
            m = BLOCK_ID_RE.search(stripped)
            hid = m.group(1) if m else None
            htext = stripped[: m.start()].rstrip() if m else stripped
            level = len(htext) - len(htext.lstrip("#"))
            htext = htext.lstrip("#").strip()
            if level >= 2:
                current_heading = htext
            units.append({
                "kind": "heading", "id": hid, "text": htext,
                "lines": [htext], "heading": current_heading, "level": level,
            })
            continue
        buf.append(line.rstrip())
    flush()
    return meta, units


# ---------------------------------------------------------------- context


def load_glossary(path):
    """Read `source term<TAB or ' -> '>target rendering` lines. Comments with #."""
    if not path:
        return []
    entries = []
    for line in pathlib.Path(path).read_text(encoding="utf-8").split("\n"):
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        for sep in ("\t", " -> ", " → ", "|"):
            if sep in line:
                src, tgt = line.split(sep, 1)
                entries.append((src.strip().strip("|").strip(), tgt.strip().strip("|").strip()))
                break
    return [e for e in entries if e[0] and e[1]]


def build_context(header, done, unit, glossary, window, char_cap):
    """Compose the `context` field: work header + glossary hits + rolling prior blocks."""
    parts = [header.strip()] if header.strip() else []

    hits = [f"{s} → {t}" for s, t in glossary if s and s in unit["text"]]
    if hits:
        parts.append("Terminology already fixed for this text:\n" + "\n".join(hits[:15]))

    rolling = []
    for rec in done[-window:] if window > 0 else []:
        rolling.append(
            f"[{rec['block_id']}] source:\n{rec['source']}\n"
            f"[{rec['block_id']}] translation already produced for this document:\n{rec['translation']}"
        )
    if rolling:
        parts.append(
            "Preceding blocks of this same document and their translations — "
            "match this terminology, register and line shape:\n\n" + "\n\n".join(rolling)
        )

    ctx = "\n\n".join(parts)
    # Trim oldest rolling entries first until under the cap.
    while len(ctx) > char_cap and rolling:
        rolling.pop(0)
        parts[-1] = (
            "Preceding blocks of this same document and their translations — "
            "match this terminology, register and line shape:\n\n" + "\n\n".join(rolling)
        )
        ctx = "\n\n".join(parts)
    return ctx[:char_cap]


# ---------------------------------------------------------------- track seeding


ABOUT_TEMPLATE = """---
title: "{title} — DharmaMitra zero-shot ({lang})"
track_type: machine-baseline
target_language: {lang}
lang_tag: {tag}
translation_of: {src}
generator: dharmamitra cat-translate v1
endpoint: {endpoint}
rails_used: none
termbase: none
status: draft
seeded: {today}
---

# {tag}-dharmamitra-zeroshot — about this track

A **machine baseline**, not a rails-governed translation track.

Every file here is raw output of DharmaMitra's public `cat-translate` endpoint,
produced one block ID at a time by
`4-SYSTEM/Skills/dharmamitra-translate/scripts/dm_translate.py`. Nothing in it
passed through `2-RAILS/`: no verse-context package, no consolidated bilingual
glossary, no per-track `termbase.md`, no human review. It therefore does **not**
satisfy the Translation-track contract in
[`../About Transformations.md`](../About%20Transformations.md) §3, and it is not
eligible to be marked `status: complete` or to be cited by any other
transformation.

## What it is for

- A comparison baseline against which a rails-governed translation can be judged.
- A drafting aid and a source of candidate renderings for
  `2-RAILS/Bilingual-Glossaries/` (via `glossary-extract-raw`).
- A fast first look at a text in a language no track covers yet.

## What governs it

| File | Role |
| --- | --- |
| `style.md` | The `style_instruction` string, sent **verbatim** to the API on every call. Edit it, then re-run with `--force` to regenerate. |
| `context-header.md` | The fixed work-level orientation prepended to every call's `context` field. |
| `work/{tag}.jsonl` | Append-only ledger: one record per API call — source, translation, the exact context sent, timings. The audit trail and the resume point. |
| `{slug}-{tag}.md` | The rendered translation, block-ID aligned to the source. |

## Provenance

- Endpoint: `{endpoint}` (public, unauthenticated)
- Source: [`{src}`]({src})
- Granularity: one source block ID per API call
- Rolling context: the preceding translated blocks of this same document are
  threaded into each call so terminology and register stay coherent.

Regenerate or extend with:

```bash
python3 4-SYSTEM/Skills/dharmamitra-translate/scripts/dm_translate.py \\
  --source "{src}" --lang {lang}
```
"""


def seed_track(out_dir, meta, args, src_rel, slug):
    """Write the track's human-editable governing files if they are missing."""
    about = out_dir / "about.md"
    if not about.exists():
        about.write_text(ABOUT_TEMPLATE.format(
            title=meta.get("title_in_english") or meta.get("title") or src_rel,
            lang=args.lang, tag=args.lang_tag, src=src_rel, slug=slug,
            endpoint=ENDPOINT, today=_dt.date.today().isoformat(),
        ), encoding="utf-8")
        print(f"seeded {about}")
    style_md = out_dir / "style.md"
    if not style_md.exists():
        style_md.write_text(args.style.strip() + "\n", encoding="utf-8")
        print(f"seeded {style_md}")
    ch = out_dir / "context-header.md"
    if not ch.exists():
        ch.write_text(args.context_header_text.strip() + "\n", encoding="utf-8")
        print(f"seeded {ch}")


# ---------------------------------------------------------------- api


def call_api(body, timeout, retries, verbose=False):
    """POST one block. Backs off hard on 429 — the endpoint is public and shared."""
    data = json.dumps(body, ensure_ascii=False).encode("utf-8")
    last = None
    for attempt in range(1, retries + 1):
        req = urllib.request.Request(
            ENDPOINT, data=data,
            headers={"Content-Type": "application/json", "Accept": "application/json"},
            method="POST",
        )
        try:
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                payload = json.loads(resp.read().decode("utf-8"))
            text = (payload.get("translation") or "").strip()
            if not text:
                raise ValueError(f"empty translation in response: {payload!r}")
            return text
        except urllib.error.HTTPError as exc:
            last = exc
            if exc.code == 429:
                # Shared public endpoint: throttle rather than hammer.
                wait = int(exc.headers.get("Retry-After") or 0) or RATE_LIMIT_BACKOFF[
                    min(attempt - 1, len(RATE_LIMIT_BACKOFF) - 1)]
                print(f"    ! 429 rate-limited; waiting {wait}s (attempt {attempt}/{retries})",
                      file=sys.stderr)
                time.sleep(wait)
                continue
            wait = 2 ** attempt
            print(f"    ! HTTP {exc.code} (attempt {attempt}/{retries}); retrying in {wait}s",
                  file=sys.stderr)
            time.sleep(wait)
        except Exception as exc:  # noqa: BLE001 — network/parse failures, then back off
            last = exc
            if attempt < retries:
                wait = 2 ** attempt
                print(f"    ! attempt {attempt}/{retries} failed ({exc}); retrying in {wait}s",
                      file=sys.stderr)
                time.sleep(wait)
    raise RuntimeError(f"cat-translate failed after {retries} attempts: {last}")


# ---------------------------------------------------------------- render


def render(out_md, units, ledger, meta, args, source_rel):
    by_id = {r["block_id"]: r for r in ledger}
    lines = []
    fm = {
        "title": f'{meta.get("title_in_english") or meta.get("title") or source_rel} — DharmaMitra zero-shot ({args.lang})',
        "file_type": "translation",
        "track_type": "machine-baseline",
        "translation_of": source_rel,
        "source_language": args.source_language,
        "target_language": args.lang,
        "lang_tag": args.lang_tag,
        "generator": "dharmamitra cat-translate v1",
        "endpoint": ENDPOINT,
        "focus": args.focus,
        "context_blocks": args.context_blocks,
        "style_instruction": args.style,
        "rails_used": "none",
        "generated": _dt.date.today().isoformat(),
        "blocks_translated": len(by_id),
        "blocks_total": sum(1 for u in units if u["kind"] == "block" and u["id"]),
        "status": "draft",
    }
    lines.append("---")
    for k, v in fm.items():
        if isinstance(v, str) and ("\n" in v or ":" in v or '"' in v):
            v = '"' + v.replace('"', "'").replace("\n", " ") + '"'
        lines.append(f"{k}: {v}")
    lines.append("---")
    lines.append("")
    lines.append(
        "> [!warning] Machine baseline — not a rails-governed translation.\n"
        "> Every line below is raw DharmaMitra `cat-translate` output, produced one "
        "block at a time with no termbase, no verse-context rails, and no human "
        "review. It is a comparison baseline and a drafting aid only. See "
        "`about.md` in this folder."
    )
    lines.append("")

    for unit in units:
        if unit["kind"] == "heading":
            hashes = "#" * unit.get("level", 2)
            hid = f" ^{unit['id']}" if unit["id"] else ""
            lines.append(f"{hashes} {unit['text']}{hid}")
            lines.append("")
            continue
        if not unit["id"]:
            continue
        rec = by_id.get(unit["id"])
        if args.layout == "parallel":
            for sl in unit["lines"]:
                lines.append(f"> {sl}")
            lines.append("")
        if rec:
            tlines = rec["translation"].split("\n")
            tlines = [t for t in tlines if t.strip()]
            if not tlines:
                tlines = ["[empty]"]
            tlines[-1] = f"{tlines[-1]} ^{unit['id']}"
            lines.extend(tlines)
        else:
            lines.append(f"*[not yet translated]* ^{unit['id']}")
        lines.append("")

    pathlib.Path(out_md).write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


# ---------------------------------------------------------------- main


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--source", required=True, help="block-ID'd source file under 1-SOURCES/")
    p.add_argument("--lang", default="english", help="target language LABEL, not ISO code")
    p.add_argument("--lang-tag", default=None, help="override the vault lang tag (en, de, …)")
    p.add_argument("--source-language", default="tibetan",
                   choices=sorted(SOURCE_LANG_FIELDS), help="which input_* field to fill")
    p.add_argument("--focus", default="tibetan",
                   choices=["equal", "tibetan", "chinese", "pali", "sanskrit"])
    p.add_argument("--out", default=None, help="track folder (default: derived, see --track)")
    p.add_argument("--track", default=None,
                   help="track slug (default: <lang-tag>-dharmamitra-zeroshot)")
    p.add_argument("--style", default=None, help="style_instruction, verbatim to the API")
    p.add_argument("--style-file", default=None, help="file whose contents are the style_instruction")
    p.add_argument("--context-header", default=None,
                   help="file with the fixed work-level context prepended to every call")
    p.add_argument("--glossary", default=None,
                   help="optional 'source<TAB>target' lines; matching entries join the context")
    p.add_argument("--context-blocks", type=int, default=3,
                   help="how many prior translated blocks to thread back in (0 disables)")
    p.add_argument("--context-cap", type=int, default=3000, help="max chars of context")
    p.add_argument("--only", default=None, help="comma-separated block IDs")
    p.add_argument("--limit", type=int, default=0, help="stop after N new calls (0 = all)")
    p.add_argument("--sleep", type=float, default=4.0,
                   help="seconds between calls; the public endpoint rate-limits above ~10/min")
    p.add_argument("--timeout", type=int, default=90, help="per-call timeout (do not lower)")
    p.add_argument("--retries", type=int, default=6)
    p.add_argument("--layout", default="parallel", choices=["parallel", "translation-only"])
    p.add_argument("--force", action="store_true", help="re-translate blocks already in the ledger")
    p.add_argument("--render-only", action="store_true", help="re-render markdown from the ledger")
    p.add_argument("--list", action="store_true", help="print parsed units and exit")
    p.add_argument("--dry-run", action="store_true", help="print request bodies, make no calls")
    args = p.parse_args()

    src_path = pathlib.Path(args.source)
    if not src_path.exists():
        sys.exit(f"source not found: {src_path}")
    if "1-SOURCES" not in str(src_path.resolve()):
        print(f"note: source is outside 1-SOURCES/ ({src_path})", file=sys.stderr)

    meta, units = parse_source(src_path)
    blocks = [u for u in units if u["kind"] == "block" and u["id"]]

    if args.list:
        for u in units:
            kind = "H" if u["kind"] == "heading" else " "
            print(f"{kind} ^{u['id'] or '-':<6} {len(u['lines'])} line(s)  {u['lines'][0][:48]}")
        print(f"\n{len(blocks)} translatable blocks, "
              f"{sum(1 for u in units if u['kind'] == 'heading')} headings")
        return

    args.lang = args.lang.strip().lower()
    args.lang_tag = args.lang_tag or LANG_TAGS.get(args.lang) or re.sub(r"[^a-z]", "", args.lang)[:3]
    track = args.track or f"{args.lang_tag}-dharmamitra-zeroshot"
    out_dir = pathlib.Path(args.out or f"3-TRANSFORMATIONS/Translations/{track}")
    work_dir = out_dir / "work"
    work_dir.mkdir(parents=True, exist_ok=True)

    if args.style_file:
        args.style = pathlib.Path(args.style_file).read_text(encoding="utf-8").strip()
    elif not args.style:
        style_md = out_dir / "style.md"
        args.style = (style_md.read_text(encoding="utf-8").strip()
                      if style_md.exists() else DEFAULT_STYLE)

    header = ""
    if args.context_header:
        header = pathlib.Path(args.context_header).read_text(encoding="utf-8").strip()
    else:
        ch = out_dir / "context-header.md"
        if ch.exists():
            header = ch.read_text(encoding="utf-8").strip()
        else:
            title = meta.get("title_in_english") or meta.get("title") or src_path.stem
            author = meta.get("author_in_english") or meta.get("author") or "unknown"
            header = (f"Work: {title} (author: {author}). A canonical Tibetan text; "
                      f"the blocks below are being translated one at a time, in order.")

    args.context_header_text = header

    glossary = load_glossary(args.glossary)
    ledger_path = work_dir / f"{args.lang_tag}.jsonl"
    ledger = []
    if ledger_path.exists():
        for line in ledger_path.read_text(encoding="utf-8").split("\n"):
            if line.strip():
                ledger.append(json.loads(line))

    slug = re.sub(r"[^a-z0-9]+", "-", (meta.get("title_in_english") or src_path.stem).lower()).strip("-")[:40] or "text"
    out_md = out_dir / f"{slug}-{args.lang_tag}.md"
    src_rel = str(src_path)

    if not args.dry_run:
        seed_track(out_dir, meta, args, src_rel, slug)

    if args.render_only:
        render(out_md, units, ledger, meta, args, src_rel)
        print(f"rendered {out_md} from {len(ledger)} ledger entries")
        return

    done_ids = {r["block_id"] for r in ledger}
    wanted = [b.strip() for b in args.only.split(",")] if args.only else None
    todo = [b for b in blocks
            if (wanted is None or b["id"] in wanted)
            and (args.force or b["id"] not in done_ids)]
    if args.limit:
        todo = todo[: args.limit]

    print(f"source     : {src_path}")
    print(f"target     : {args.lang} ({args.lang_tag})   focus={args.focus}")
    print(f"track      : {out_dir}")
    print(f"blocks     : {len(blocks)} total, {len(done_ids)} already in ledger, {len(todo)} to do")
    if not todo:
        render(out_md, units, ledger, meta, args, src_rel)
        print(f"nothing to translate; re-rendered {out_md}")
        return

    for n, unit in enumerate(todo, 1):
        prior = [r for r in ledger if r["block_id"] != unit["id"]]
        ctx = build_context(header, prior, unit, glossary,
                            args.context_blocks, args.context_cap)
        body = {"input_tibetan": "", "input_chinese": "", "input_pali": "",
                "input_sanskrit": "", "context": ctx, "focus": args.focus,
                "target_language": args.lang, "style_instruction": args.style}
        body[SOURCE_LANG_FIELDS[args.source_language]] = unit["text"]

        print(f"[{n}/{len(todo)}] ^{unit['id']} … ", end="", flush=True)
        if args.dry_run:
            print("(dry run)")
            print(json.dumps(body, ensure_ascii=False, indent=2))
            continue

        t0 = time.time()
        try:
            translation = call_api(body, args.timeout, args.retries)
        except RuntimeError as exc:
            print(f"\nSTOPPED at ^{unit['id']}: {exc}", file=sys.stderr)
            print("Ledger is intact; nothing done so far is lost. Resume with the same "
                  "command (already-translated blocks are skipped), or raise --sleep.",
                  file=sys.stderr)
            break
        elapsed = time.time() - t0

        rec = {
            "block_id": unit["id"],
            "heading": unit["heading"],
            "source": unit["text"],
            "translation": translation,
            "target_language": args.lang,
            "focus": args.focus,
            "style_instruction": args.style,
            "context": ctx,
            "endpoint": ENDPOINT,
            "elapsed_s": round(elapsed, 2),
            "ts": _dt.datetime.now().isoformat(timespec="seconds"),
        }
        ledger = [r for r in ledger if r["block_id"] != unit["id"]] + [rec]
        with ledger_path.open("a", encoding="utf-8") as fh:
            fh.write(json.dumps(rec, ensure_ascii=False) + "\n")
        first = translation.split("\n")[0]
        print(f"{elapsed:.1f}s  {first[:60]}")
        if args.sleep and n < len(todo):
            time.sleep(args.sleep)

    if not args.dry_run:
        # Ledger is append-only; keep the last record per block for rendering.
        latest = {}
        for r in ledger:
            latest[r["block_id"]] = r
        ordered = [latest[b["id"]] for b in blocks if b["id"] in latest]
        render(out_md, units, ordered, meta, args, src_rel)
        print(f"\nwrote {out_md}  ({len(ordered)}/{len(blocks)} blocks)")
        print(f"ledger {ledger_path}")


if __name__ == "__main__":
    main()
