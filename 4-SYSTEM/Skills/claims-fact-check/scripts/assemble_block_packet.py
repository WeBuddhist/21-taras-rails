#!/usr/bin/env python3
"""Assemble one block's fact-check packet: the Tibetan, the translation, every
verse-aligned commentary's prose for that block, and the consolidated claims page
for the spine slot the block belongs to.

The point is to put the whole corpus's view of one segment in front of the auditor
at once. `commentary-fact-check` deliberately runs one commentary per session so
the reader is never tempted to blend two traditions; that is the right discipline
for grading against a single authority, and the wrong shape for asking "is this
rendering supported by *anyone*?". This packet answers the second question, and the
claims page — which already separates Consensus from ⚑ Divergences — is what keeps
it from collapsing into blending.

Writes a markdown packet. Spends no API calls, reads nothing outside the vault.
Stdlib only.
"""
from __future__ import annotations

import argparse
import json
import pathlib
import re
import subprocess
import sys
import tempfile

VAULT = pathlib.Path(__file__).resolve().parents[4]   # <vault>/4-SYSTEM/Skills/<skill>/scripts/
EXTRACT = VAULT / "4-SYSTEM/Skills/commentary-fact-check/scripts/extract_commentary.py"
ALIGNED = VAULT / "1-SOURCES/Commentaries/New raw data"
CLAIMS = VAULT / "2-RAILS/Claims"
BLOCK_ID_RE = re.compile(r"\^([A-Za-z0-9][A-Za-z0-9-]*)\s*$")


def slot_for(block_id: str) -> str | None:
    """Block ID -> canonical spine slot (slot IDs: vault-annex.md §2a).

    Mapped against the root text as it ACTUALLY stands, which is not what the
    annex §2 describes. The file's own IDs are:

        ^I-0..^I-3   title / invocation
        ^1-0..^1-21  the twenty-one homages          -> tara-01 .. tara-21
        ^1-22        the mantra-praise closing line  -> benefits
        ^2-0..^2-6   the ཕན་ཡོན benefits stanzas      -> benefits
        ^a-0, ^a-1   the colophon                    -> benefits

    The annex says the benefits section is `^a-1`-`^a-7`; no such run exists in
    the file. The slot IDs are unchanged — only this mapping is corrected —
    because a slot ID is a registry entry a human owns, and renaming one orphans
    its topic page.
    """
    m = re.fullmatch(r"1-(\d+)", block_id)
    if m:
        n = int(m.group(1))
        if 1 <= n <= 21:
            return f"tara-{n:02d}"
        return "benefits"          # ^1-22 closes the praise, not a homage
    if re.fullmatch(r"[2a]-\d+", block_id):
        return "benefits"
    return None


def parse_blocks(path: pathlib.Path) -> dict[str, str]:
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


def registered_id(path: pathlib.Path) -> str:
    m = re.search(r"^registered_id:\s*(\S+)", path.read_text(encoding="utf-8"), re.M)
    return m.group(1) if m else path.stem


def commentary_passages(path: pathlib.Path) -> dict[str, str]:
    """Run commentary-fact-check's extractor and read its JSON back.

    It writes to a path and prints a human summary to stdout, so it is always
    given a real temp file — asking it for stdout returns the summary, which
    parses as nothing and looks exactly like a file with no anchors.
    """
    with tempfile.NamedTemporaryFile("r", suffix=".json", delete=False) as fh:
        tmp = pathlib.Path(fh.name)
    try:
        r = subprocess.run([sys.executable, str(EXTRACT), str(path), "--json", str(tmp)],
                           capture_output=True, text=True)
        if r.returncode != 0 or not tmp.stat().st_size:
            raise RuntimeError((r.stderr or r.stdout).strip().splitlines()[-1]
                               if (r.stderr or r.stdout).strip() else "no output")
        data = json.loads(tmp.read_text(encoding="utf-8"))
    finally:
        tmp.unlink(missing_ok=True)
    return {k: (v if isinstance(v, str)
                else v.get("text") or json.dumps(v, ensure_ascii=False))
            for k, v in data.items()}


def strip_trailing_headings(text: str) -> str:
    """Drop the next section's heading off the end of a bucket.

    The extractor attributes everything between one transclusion marker and the
    next to the first marker's verse, so a `### <next homage> ^N-0` heading that
    sits before the next marker lands at the tail of this verse's prose. It is
    the following verse's label, not this verse's commentary, and leaving it in
    invites an auditor to read it as one.
    """
    lines = text.rstrip().splitlines()
    while lines and (not lines[-1].strip() or lines[-1].lstrip().startswith("#")):
        lines.pop()
    return "\n".join(lines).strip()


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--block", required=True, help="block ID, e.g. 1-6 (no caret)")
    p.add_argument("--root", required=True, help="the Tibetan root text")
    p.add_argument("--translation", required=True, help="the translation being audited")
    p.add_argument("--commentaries", default=str(ALIGNED),
                   help="folder of verse-aligned commentaries (default: New raw data/)")
    p.add_argument("--out", required=True, help="packet markdown to write")
    a = p.parse_args(argv)

    bid = a.block.lstrip("^")
    root = parse_blocks(pathlib.Path(a.root))
    tr = parse_blocks(pathlib.Path(a.translation))
    if bid not in root:
        print(f"ERROR: block ^{bid} is not in {a.root}", file=sys.stderr)
        return 2

    parts = [
        f"# Fact-check packet — `^{bid}`\n",
        f"- root: `{a.root}`",
        f"- translation: `{a.translation}`",
        f"- spine slot: `{slot_for(bid) or '(none — not a homage or benefits block)'}`\n",
        "## Tibetan (root)\n", "```\n" + root[bid] + "\n```\n",
        "## Translation under audit\n",
        "```\n" + (tr.get(bid) or "*** NOT TRANSLATED ***") + "\n```\n",
        "## Commentary prose for this block\n",
    ]

    found, silent, failed = 0, [], []
    for f in sorted(pathlib.Path(a.commentaries).glob("*.md")):
        try:
            passages = commentary_passages(f)
        except Exception as exc:  # noqa: BLE001 — a file without anchors is normal
            failed.append((f.name, str(exc)[:120]))
            continue
        text = strip_trailing_headings(passages.get(bid) or "")
        rid = registered_id(f)
        if text:
            found += 1
            parts.append(f"### `{rid}`\n\n{text}\n")
        else:
            silent.append(rid)

    if silent:
        parts.append("### Silent on this block\n\n"
                     + ", ".join(f"`{s}`" for s in silent)
                     + "\n\nSilence is evidence of nothing. It does not license a reading;"
                       " it only means this commentary is not among the witnesses here.\n")
    if failed:
        parts.append("### Not read (no transclusion anchors)\n\n"
                     + "\n".join(f"- `{n}` — {e}" for n, e in failed) + "\n")

    slot = slot_for(bid)
    claims_path = CLAIMS / f"{slot}.md" if slot else None
    if claims_path and claims_path.exists():
        parts.append(f"## Consolidated claims — `2-RAILS/Claims/{slot}.md`\n")
        parts.append("Consensus / ⚑ Divergences / Unique as consolidated across all "
                     "sixteen commentaries. **A ⚑ divergence means the corpus itself is "
                     "split: a translation that follows either attested position is not "
                     "wrong.**\n")
        parts.append(claims_path.read_text(encoding="utf-8"))
    elif slot:
        parts.append(f"## Consolidated claims\n\n`2-RAILS/Claims/{slot}.md` does not exist. "
                     "Grade against the commentary prose above only, and say so in the "
                     "report — do not treat the absence as consensus.\n")

    out = pathlib.Path(a.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(parts), encoding="utf-8")

    print(f"block            : ^{bid}")
    print(f"spine slot       : {slot or '—'}")
    print(f"commentaries with prose: {found}")
    print(f"silent           : {len(silent)}")
    if failed:
        print(f"unreadable       : {len(failed)}  ({', '.join(n for n, _ in failed)})")
    print(f"claims page      : {'yes' if claims_path and claims_path.exists() else 'no'}")
    print(f"packet           : {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
