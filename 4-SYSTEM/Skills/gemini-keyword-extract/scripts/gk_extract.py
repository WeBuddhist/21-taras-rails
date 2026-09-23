#!/usr/bin/env python3
"""Extract key terms directly from Tibetan blocks with Gemini, with provenance.

The point of contrast: `keyword-extract` detects candidates in an English
translation and maps them back to Tibetan, because YAKE/TF-IDF cannot run on
unsegmented Tibetan. This script asks a model to read the Tibetan itself. It is
built to be *compared* against that route, not to replace it unexamined.

Every returned term is checked against the block it was claimed from, and graded:

    VERBATIM    the exact string occurs in that block
    NORMALIZED  it occurs after tsheg/shad/anusvara normalisation (a citation form)
    ABSENT      it does not occur — a paraphrase, a conflation, or an invention

ABSENT terms are kept, flagged, and reported. They are never silently dropped and
never silently trusted: an unverifiable term is the whole risk of reading the
source language directly, so it is measured rather than assumed away.

Needs GEMINI_API_KEY (environment, or --env-file). Stdlib only.
"""
from __future__ import annotations

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

API_BASE = "https://generativelanguage.googleapis.com/v1beta/models"
DEFAULT_MODEL = "gemini-3.1-pro-preview"
KEY_ENV = "GEMINI_API_KEY"
BLOCK_ID_RE = re.compile(r"[ \t]\^([A-Za-z0-9][A-Za-z0-9._-]*)[ \t]*$")
BACKOFF = [10, 20, 40, 60, 120]

SYSTEM = """\
You are a Tibetan philologist compiling a key-term index for a classical Buddhist text.

For each numbered block of Tibetan below, list the CONTENT TERMS a scholar would index:
substantive nouns and noun phrases, technical/doctrinal vocabulary, proper names, deity
names, epithets, mantra syllables, and named classes of beings.

Rules, in order of importance:
1. Copy each term EXACTLY as the substring appears in that block. Do not normalise the
   spelling, do not supply a dictionary citation form, do not add or remove a tsheg or
   shad. If you cannot copy it exactly, omit it.
2. Do NOT list grammatical particles, case markers, comparison markers (ལྟ་བུ་, བཞིན་),
   intensifiers (རབ་ཏུ་, ཤིན་ཏུ་), copulas, or pronouns. They are frequent everywhere and
   are not key terms.
3. A term appearing in two blocks is listed under both. Attribute each term ONLY to the
   block it actually appears in.
4. Prefer the longest meaningful unit that is a single concept (སྟོན་ཀའི་ཟླ་བ་ "autumn
   moon" rather than ཟླ་བ་ alone) — but also list the head noun separately when it carries
   its own doctrinal weight.
5. `gloss_en` is a short English gloss, 1-4 words, for cross-referencing only.
6. `kind` is one of: doctrinal, deity, person, being-class, mantra, epithet, object,
   quality, action, place.

Each block is introduced by a line of the form <<ID>>, where ID is that block's
identifier. Set `block_id` to the ID **exactly as it appears between the angle brackets**
— just the identifier, with no prefix, no caret, and no surrounding words.

Return every block you were given, in order, even if a block yields no terms."""

SCHEMA = {
    "type": "OBJECT",
    "properties": {
        "blocks": {
            "type": "ARRAY",
            "items": {
                "type": "OBJECT",
                "properties": {
                    "block_id": {"type": "STRING"},
                    "terms": {
                        "type": "ARRAY",
                        "items": {
                            "type": "OBJECT",
                            "properties": {
                                "term": {"type": "STRING"},
                                "gloss_en": {"type": "STRING"},
                                "kind": {"type": "STRING"},
                            },
                            "required": ["term", "gloss_en"],
                        },
                    },
                },
                "required": ["block_id", "terms"],
            },
        }
    },
    "required": ["blocks"],
}


# ----------------------------------------------------------------- helpers


def load_key(env_file):
    key = os.environ.get(KEY_ENV)
    if key:
        return key
    for cand in filter(None, [env_file,
                              "4-SYSTEM/Pipelines/wikipedia/.env",
                              os.path.expanduser("~/.zshrc")]):
        p = pathlib.Path(cand)
        if not p.exists():
            continue
        for line in p.read_text(encoding="utf-8", errors="replace").splitlines():
            m = re.match(rf"\s*(?:export\s+)?{KEY_ENV}\s*=\s*[\"']?([^\"'\s#]+)", line)
            if m:
                return m.group(1)
    sys.exit(f"ERROR: {KEY_ENV} not found in the environment or any known env file.")


def parse_blocks(path):
    """{block_id: text} for content blocks. Headings and transclusions excluded."""
    blocks, buf = {}, []
    for line in pathlib.Path(path).read_text(encoding="utf-8").splitlines():
        s = line.strip()
        if s.startswith("---"):
            continue
        if s.startswith("#") or s.startswith("![["):
            buf = []
            continue
        m = BLOCK_ID_RE.search(s)
        if m:
            buf.append(s[: m.start()].rstrip())
            txt = "\n".join(b for b in buf if b)
            if txt:
                blocks[m.group(1)] = txt
            buf = []
        elif s:
            buf.append(s)
    return blocks


def norm_tib(s):
    """Tsheg/shad/whitespace-insensitive form, plus the anusvara equivalence the
    keyword methodology's §4.4 variant pass established (U+0F83 <-> U+0F7E)."""
    s = s.replace("ྃ", "ཾ")
    return re.sub(r"[་།༎\s༑]+", "", s)


def resolve_block_id(raw, batch):
    """Map whatever the model put in `block_id` onto one of the batch's real IDs.

    Gemini has been observed echoing the source's own label — asked for `1-3` it
    returned `BLOCK 1-3` — and the formatting is not stable run to run: in one
    32-block run two of seven batches came back with bare IDs and five with the
    label prefix. Matching on the exact string silently loses whole batches, so
    the id is stripped of decoration and then matched, longest candidate first so
    `1-2` never claims a row belonging to `1-22`.
    """
    cleaned = re.sub(r"^[\s#^*>\[]*(?:block|segment|id)?[\s:#^>\]]*", "",
                     str(raw or "").strip(), flags=re.I).strip("<>[]() \t")
    for b in batch:
        if cleaned == b:
            return b
    for b in sorted(batch, key=len, reverse=True):
        if re.search(rf"(?<![A-Za-z0-9-]){re.escape(b)}(?![A-Za-z0-9-])", str(raw or "")):
            return b
    return None


def grade(term, block_text):
    if term in block_text:
        return "VERBATIM"
    if norm_tib(term) and norm_tib(term) in norm_tib(block_text):
        return "NORMALIZED"
    return "ABSENT"


def call_api(body, model, key, timeout, retries):
    url = f"{API_BASE}/{model}:generateContent"
    data = json.dumps(body, ensure_ascii=False).encode("utf-8")
    for attempt in range(1, retries + 1):
        req = urllib.request.Request(
            url, data=data, method="POST",
            headers={"Content-Type": "application/json", "x-goog-api-key": key})
        t0 = time.time()
        try:
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                payload = json.loads(resp.read().decode("utf-8"))
            cands = payload.get("candidates") or []
            if not cands:
                raise ValueError((payload.get("promptFeedback") or {})
                                 .get("blockReason", "no candidates"))
            text = "".join(p.get("text", "")
                           for p in (cands[0].get("content") or {}).get("parts", [])
                           if "text" in p)
            um = payload.get("usageMetadata") or {}
            return json.loads(text), {
                "model_version": payload.get("modelVersion", model),
                "elapsed_s": round(time.time() - t0, 2),
                "prompt_tokens": um.get("promptTokenCount"),
                "output_tokens": um.get("candidatesTokenCount"),
            }
        except urllib.error.HTTPError as exc:
            detail = exc.read().decode("utf-8", "replace")[:200]
            if exc.code in (429, 500, 503) and attempt < retries:
                wait = BACKOFF[min(attempt - 1, len(BACKOFF) - 1)]
                print(f"    HTTP {exc.code} → sleep {wait}s", file=sys.stderr)
                time.sleep(wait)
                continue
            raise RuntimeError(f"HTTP {exc.code}: {detail}") from exc
        except (urllib.error.URLError, TimeoutError, ValueError) as exc:
            if attempt < retries:
                time.sleep(BACKOFF[min(attempt - 1, len(BACKOFF) - 1)])
                continue
            raise RuntimeError(str(exc)) from exc
    raise RuntimeError("retries exhausted")


# -------------------------------------------------------------------- main


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--source", required=True, help="block-ID'd Tibetan text")
    p.add_argument("--out", required=True, help="output JSON")
    p.add_argument("--model", default=DEFAULT_MODEL)
    p.add_argument("--batch", type=int, default=5, help="blocks per call (default 5)")
    p.add_argument("--only", help="comma-separated block IDs")
    p.add_argument("--limit", type=int, default=0, help="first N blocks only (smoke test)")
    p.add_argument("--temperature", type=float, default=None)
    p.add_argument("--sleep", type=float, default=2.0)
    p.add_argument("--timeout", type=int, default=180)
    p.add_argument("--retries", type=int, default=4)
    p.add_argument("--env-file", default=None)
    p.add_argument("--list", action="store_true", help="parse only, no calls")
    a = p.parse_args(argv)

    blocks = parse_blocks(a.source)
    ids = list(blocks)
    if a.only:
        want = {x.strip().lstrip("^") for x in a.only.split(",")}
        ids = [i for i in ids if i in want]
    if a.limit:
        ids = ids[: a.limit]

    if a.list:
        for i in ids:
            print(f"^{i:<8} {len(blocks[i]):>4} chars  {blocks[i].splitlines()[0][:50]}")
        print(f"\n{len(ids)} blocks, {-(-len(ids) // a.batch)} calls at --batch {a.batch}")
        return 0

    key = load_key(a.env_file)
    batches = [ids[i: i + a.batch] for i in range(0, len(ids), a.batch)]
    print(f"{len(ids)} blocks → {len(batches)} calls (model {a.model}, batch {a.batch})")

    per_block, ledger, usage = {}, [], {"prompt": 0, "output": 0}
    for bi, batch in enumerate(batches, 1):
        src = "\n\n".join(f"<<{b}>>\n{blocks[b]}" for b in batch)
        gen = {"responseMimeType": "application/json", "responseSchema": SCHEMA}
        if a.temperature is not None:
            gen["temperature"] = a.temperature
        body = {"systemInstruction": {"parts": [{"text": SYSTEM}]},
                "contents": [{"role": "user", "parts": [{"text": src}]}],
                "generationConfig": gen}

        print(f"[{bi}/{len(batches)}] ^{',^'.join(batch)} … ", end="", flush=True)
        data, info = call_api(body, a.model, key, a.timeout, a.retries)
        usage["prompt"] += info.get("prompt_tokens") or 0
        usage["output"] += info.get("output_tokens") or 0

        returned, unresolved = {}, []
        for r in data.get("blocks", []):
            bid = resolve_block_id(r.get("block_id"), batch)
            if bid is None:
                unresolved.append(r.get("block_id"))
                continue
            returned[bid] = r.get("terms") or []
        missing = [b for b in batch if b not in returned]
        n_terms = 0
        for b in batch:
            rows = []
            for t in returned.get(b, []):
                term = (t.get("term") or "").strip()
                if not term:
                    continue
                rows.append({"term": term,
                             "gloss_en": (t.get("gloss_en") or "").strip(),
                             "kind": (t.get("kind") or "").strip(),
                             "verification": grade(term, blocks[b])})
            per_block[b] = rows
            n_terms += len(rows)
        absent = sum(1 for b in batch for r in per_block[b]
                     if r["verification"] == "ABSENT")
        print(f"{n_terms} terms"
              + (f", {absent} ABSENT" if absent else "")
              + (f", MISSING BLOCKS {missing}" if missing else "")
              + (f", UNRESOLVED IDS {unresolved}" if unresolved else "")
              + f"  ({info['elapsed_s']}s)")

        ledger.append({"batch": bi, "block_ids": batch, "terms": n_terms,
                       "absent": absent, "blocks_not_returned": missing,
                       "unresolved_ids": unresolved, **info,
                       "ts": _dt.datetime.now().isoformat(timespec="seconds")})
        if bi < len(batches):
            time.sleep(a.sleep)

    tally = {k: sum(1 for b in per_block.values() for r in b if r["verification"] == k)
             for k in ("VERBATIM", "NORMALIZED", "ABSENT")}
    total = sum(tally.values())
    distinct = len({r["term"] for b in per_block.values() for r in b})

    out = pathlib.Path(a.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps({
        "schema": "gemini-block-terms/1",
        "source": a.source, "model": a.model, "batch": a.batch,
        "date": _dt.date.today().isoformat(),
        "blocks_processed": len(ids),
        "term_instances": total, "distinct_terms": distinct,
        "verification": tally, "usage": usage,
        "by_block": per_block, "ledger": ledger,
    }, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")

    print(f"\nblocks         : {len(ids)}")
    print(f"term instances : {total}   (distinct strings: {distinct})")
    for k in ("VERBATIM", "NORMALIZED", "ABSENT"):
        pct = f"{tally[k] / total:.0%}" if total else "—"
        print(f"  {k:<11}: {tally[k]:>4}  {pct}")
    print(f"tokens         : {usage['prompt']} in / {usage['output']} out")
    print(f"written        : {out}")
    if tally["ABSENT"]:
        print("\nABSENT terms are in the output flagged, not dropped. They are the "
              "measured cost of reading the source language directly — review before "
              "treating this run as a registry.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
