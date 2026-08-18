#!/usr/bin/env python3
"""Bring a skill-flow article into the layout ``kwiki verify``/``publish`` reads.

Two article factories exist in this vault and they do not share a file layout:

*the kwiki chain*   ``articles/<term>/{article.wiki,citations.json,…}`` plus a
                    ``ledger.json`` entry — what ``kwiki verify`` and
                    ``kwiki publish`` know how to open.
*the skill flow*    ``term-articles/<slug>/{article.md,citations.md}`` — the
                    ``wiki-article-from-claims`` skill's output, drafted from
                    ``2-RAILS/Claims/<slug>.md``.  The wikitext sits inside a
                    ```` ```wikitext ```` fence so Obsidian renders it verbatim;
                    the citation audit trail is a markdown table.

Every article this vault currently has — 43 term-articles, 22 slot-articles —
came from the skill flow, so the publish path cannot see a single one of them.
This script is the bridge.  It is deliberately mechanical: it moves and reshapes,
it never rewrites wikitext and never invents a citation.  What it produces is
exactly what the deterministic gate then re-checks against ``1-SOURCES/``.

Ledger status is ``drafted``, never ``verified``.  ``verified`` means the gate
passed *and* the stage-6b audit cleared, and neither is this script's to assert.

    python scripts/import_term_article.py                 # every article
    python scripts/import_term_article.py mudra lotus     # named slugs
    python scripts/import_term_article.py --dry-run mudra
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path

_PIPELINE_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_PIPELINE_ROOT / "src"))

import yaml  # noqa: E402

from kangyur_wiki import registry as registry_mod  # noqa: E402
from kangyur_wiki.config import load_settings  # noqa: E402
from kangyur_wiki.ledger import Ledger, TermStatus, ledger_path  # noqa: E402

#: The article body lives inside this fence in every skill-flow ``article.md``.
FENCE = re.compile(r"^```wikitext\s*$(.*?)^```\s*$", re.MULTILINE | re.DOTALL)
FRONTMATTER = re.compile(r"\A---\s*$(.*?)^---\s*$", re.MULTILINE | re.DOTALL)
LEAD_TERM = re.compile(r"'''([^']+)'''")
#: Block IDs are written ``#^0-62`` in the citations table but stored on a Citation
#: *without* the caret — that is the key ``commentary.parse_blocks`` yields, and the
#: locator check looks the segment up in that index. Keep the caret and every citation
#: silently reports as unlocated.
BLOCK_ID = re.compile(r"\^([0-9A-Za-z][0-9A-Za-z-]*)")
#: Tibetan runs in straight double quotes — how every citations.md marks a quotation.
QUOTED = re.compile(r'"([^"]+)"')
#: A cell saying "not quoted": an em-dash lead, or an explicit parenthetical.
NOT_QUOTED = re.compile(r"^\s*(—|-|–|no\b|not quoted)", re.IGNORECASE)
TIBETAN = re.compile(r"[ༀ-࿿]")


def strip_term(term: str) -> str:
    """The directory/lookup form of a term — what ``cli.verify`` and ``cli.publish`` use."""
    return unicodedata.normalize("NFC", term).strip().strip("།་ ")


@dataclass
class Row:
    """One citation event as the citations.md table records it."""

    ref: str
    commentary: str
    claim_id: str
    quote_cell: str
    block_cell: str


def parse_frontmatter(text: str) -> dict:
    match = FRONTMATTER.search(text)
    return yaml.safe_load(match.group(1)) or {} if match else {}


def extract_wikitext(article_md: Path) -> str:
    text = article_md.read_text(encoding="utf-8")
    match = FENCE.search(text)
    if match is None:
        raise ValueError(f"no ```wikitext fence in {article_md}")
    return match.group(1).strip() + "\n"


def _column_index(header: list[str], *needles: str) -> int | None:
    """First column whose header contains any needle, in needle priority order."""
    for needle in needles:
        for index, cell in enumerate(header):
            if needle in cell.lower():
                return index
    return None


def parse_citation_rows(citations_md: Path) -> list[Row]:
    """Every row of the reference-map table, whatever the header wording.

    The tables were written by hand across many sessions and their headers drift
    ("Ref" / "Ref name" / "Ref (named)" / "#"; "Claim ID" / "Claim ID(s) drawn on";
    some carry an extra "Quoted in article?" column).  The *semantics* never drift,
    so columns are located by keyword rather than by position.
    """
    rows: list[Row] = []
    header: list[str] | None = None
    idx: dict[str, int | None] = {}

    for line in citations_md.read_text(encoding="utf-8").splitlines():
        line = line.rstrip()
        if not line.startswith("|"):
            header = None
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if all(set(c) <= {"-", ":", " "} for c in cells) and cells:
            continue  # the |---|---| separator
        if header is None or "commentary" in " ".join(cells).lower() and "claim" in " ".join(cells).lower():
            header = cells
            idx = {
                "ref": _column_index(header, "ref", "#"),
                "commentary": _column_index(header, "commentary"),
                "claim": _column_index(header, "claim"),
                # "quotation" before "quoted": a table with both columns means the
                # second is a yes/no flag and the first is the text.
                "quote": _column_index(header, "quotation", "quoted"),
                "block": _column_index(header, "source block", "block"),
            }
            continue

        def cell(key: str) -> str:
            position = idx.get(key)
            if position is None or position >= len(cells):
                return ""
            return cells[position]

        commentary = cell("commentary")
        if not commentary:
            continue
        rows.append(
            Row(
                ref=cell("ref"),
                commentary=commentary,
                claim_id=cell("claim"),
                quote_cell=cell("quote"),
                block_cell=cell("block"),
            )
        )
    return rows


def clean_id(cell: str) -> str:
    """A cell's leading token, stripped of markup: the registered_id when there is one."""
    text = re.sub(r"[`*\[\]]", "", cell)
    text = re.sub(r"\(.*?\)", " ", text)
    if not text.strip():
        return ""
    return text.strip().split()[0].strip(".,;:")


def resolve_source(row: Row, sources: dict[str, object]) -> object | None:
    """Which commentary a row names — the tables say it four different ways.

    ``registered_id`` in the Commentary column is the intended form, but the
    column also appears as a claim-qualified id (``taranatha:c-9-3``), as a
    Tibetan author-and-title string, and as an English author name — in which
    cases the *Ref* column usually still carries the bare id, because that is
    the ``<ref name>`` the wikitext uses.  Author/title containment is the last
    resort, and it is a containment test against the registry rather than a
    guess, so a miss is reported instead of silently mis-attributed.
    """
    for cell in (row.commentary, row.ref):
        token = clean_id(cell)
        for candidate in (token, token.split(":")[0]):
            if candidate in sources:
                return sources[candidate]

    haystack = re.sub(r"[`*]", "", f"{row.commentary} {row.ref}")
    for source in sources.values():
        title = (getattr(source, "title", "") or "").strip("།་ ")
        author = (getattr(source, "author", "") or "").split("(")[0].strip("།་ ")
        if len(title) > 12 and title[:24] in haystack:
            return source
        if len(author) > 6 and author in haystack:
            return source
    return None


ELISION = re.compile(r"\.\.\.|…")


def article_quotes(wikitext: str) -> list[str]:
    """Every quoted run in the article body — what a reader actually sees quoted."""
    return [q.strip() for q in QUOTED.findall(wikitext) if q.strip()]


def fragments(quote: str) -> list[str]:
    """An elided quotation as the verbatim fragments it actually asserts.

    ``"སྐུ་མདོག་… ཨུཏྤལ་སྔོན་པོ"`` claims two runs are in the source, not one; checking
    the joined string can only fail.  Fragments shorter than a few syllables are
    dropped — they carry no evidence and would match almost anything.
    """
    return [f.strip("། ་") for f in ELISION.split(quote) if len(f.strip("། ་")) >= 12]


def unelide(quote: str, candidates: list[str]) -> str:
    """A table quote written with an ellipsis, restored from the article's own text.

    The citations tables abbreviate a long quotation (``"སྐུ་མདོག་… ཨུཏྤལ་སྔོན་པོ"``)
    because they are written to be read.  The gate compares character for character,
    so an abbreviated quote can never pass — and reporting it as a failed quotation
    would be a lie about the article, which quotes the passage in full.  Match the
    table's opening fragment against the article's own quoted runs and check *that*.

    Falls back to the quote as written when nothing matches, so an unrecoverable
    abbreviation is reported by the gate rather than silently dropped.
    """
    head = ELISION.split(quote)[0].strip()
    if len(head) < 8:
        return quote
    exact = [c for c in candidates if c.startswith(head)]
    if len(exact) == 1:
        return exact[0]
    # Two commentaries in this corpus open a passage with the same two dozen
    # syllables, so a shortened prefix can match the wrong article quote. An
    # ambiguous prefix is no evidence: leave the ellipsis in and let the caller
    # check the fragments instead of silently attributing the wrong text.
    loose = [c for c in candidates if c.startswith(head[:24])]
    return loose[0] if len(loose) == 1 else quote


def extract_quotes(cell: str) -> list[str]:
    """Every verbatim quotation in a Quotation cell.

    Most tables wrap each quotation in straight double quotes; a few write the
    Tibetan bare, with the "was it quoted?" answer in its own column.  A cell
    that opens with an em-dash or "no" is a paraphrase marker, not a quotation.
    """
    if NOT_QUOTED.match(cell):
        return []
    quoted = [q.strip() for q in QUOTED.findall(cell) if q.strip()]
    if quoted:
        return quoted
    bare = re.sub(r"[`*]", "", cell)
    bare = re.sub(r"\([^)]*\)\s*$", "", bare).strip()
    # Only a cell that is *mostly* Tibetan is a bare quotation; a cell of English
    # prose ("opening line only") is a note about the citation, not the citation.
    if bare and len(TIBETAN.findall(bare)) > 0.6 * len(bare.replace(" ", "")):
        return [bare]
    return []


def build_citations(
    rows: list[Row], sources: dict[str, object], in_article: list[str]
) -> tuple[list[dict], list[str]]:
    citations: list[dict] = []
    notes: list[str] = []
    last_block: dict[str, str] = {}

    for row in rows:
        source = resolve_source(row, sources)
        if source is None:
            label = clean_id(row.commentary) or row.commentary[:40]
            notes.append(f"unknown commentary {label!r} (row: {row.claim_id or row.ref})")
            continue

        blocks = BLOCK_ID.findall(row.block_cell)
        quotes = extract_quotes(row.quote_cell)
        # A row citing several claims lists its blocks in the same order as its
        # quotations; pair them when the counts agree, and fall back to the row's
        # first block (then the commentary's last seen block) when they do not.
        default_block = blocks[0] if blocks else last_block.get(source.source_id, "")
        if blocks:
            last_block[source.source_id] = blocks[0]

        base = {
            "source_id": source.source_id,
            "author": source.author or "",
            "title": source.title or "",
            "year": getattr(source, "year", "") or "",
            "page": "",
            "url": getattr(source, "wikisource_text_url", None) or "",
            "isbn": getattr(source, "isbn", "") or "",
        }
        if quotes:
            for index, quote in enumerate(quotes):
                segment = blocks[index] if len(blocks) == len(quotes) else default_block
                # An abbreviated table quote is restored from the article's own text
                # where possible; where not, it is split into the fragments it really
                # asserts, so each is checked rather than the whole failing on the gap.
                checkable = [quote]
                if ELISION.search(quote):
                    restored = unelide(quote, in_article)
                    checkable = [restored] if not ELISION.search(restored) else fragments(quote)
                for piece in checkable or [quote]:
                    citations.append(
                        {**base, "segment_id": segment, "quote": unicodedata.normalize("NFC", piece)}
                    )
        else:
            citations.append({**base, "segment_id": default_block, "quote": ""})
    return citations, notes


def import_one(
    article_dir: Path,
    corpus_dir: Path,
    terms: list[str],
    source_by_registered_id: dict[str, object],
    *,
    dry_run: bool,
) -> dict:
    slug = article_dir.name
    article_md = article_dir / "article.md"
    citations_md = article_dir / "citations.md"

    raw = article_md.read_text(encoding="utf-8")
    front = parse_frontmatter(raw)
    if front.get("status") == "not-drafted" or FENCE.search(raw) is None:
        # A deliberate non-article: the skill found no citable claim and refused to
        # draft rather than reach for parametric knowledge. Nothing to publish.
        return {"slug": slug, "skipped": front.get("status") or "no wikitext fence", "notes": []}
    wikitext = extract_wikitext(article_md)

    lead = LEAD_TERM.search(wikitext)
    lead_term = lead.group(1) if lead else ""
    stripped = strip_term(lead_term)
    canonical = next((t for t in terms if strip_term(t) == stripped), "")

    rows = parse_citation_rows(citations_md) if citations_md.exists() else []
    citations, notes = build_citations(rows, source_by_registered_id, article_quotes(wikitext))

    result = {
        "slug": slug,
        "kind": front.get("article_kind", ""),
        "lead_term": lead_term,
        "term": canonical or lead_term,
        "in_terms_yaml": bool(canonical),
        "rows": len(rows),
        "citations": len(citations),
        "quoting": sum(1 for c in citations if c["quote"]),
        "notes": notes,
    }
    if not stripped:
        result["notes"] = notes + ["no bold lead term in the wikitext — cannot name the article"]
        return result

    target = corpus_dir / "articles" / strip_term(result["term"])
    result["target"] = str(target)
    if dry_run:
        return result

    target.mkdir(parents=True, exist_ok=True)
    (target / "article.wiki").write_text(wikitext, encoding="utf-8")
    (target / "citations.json").write_text(
        json.dumps(citations, ensure_ascii=False, indent=1) + "\n", encoding="utf-8"
    )
    (target / "import.json").write_text(
        json.dumps(
            {
                "imported_by": "scripts/import_term_article.py",
                "imported_from": str(article_dir.relative_to(corpus_dir)),
                "method": front.get("method", "wiki-article-from-claims"),
                "source_status": front.get("status", ""),
                "rows_parsed": len(rows),
                "citations_written": len(citations),
                "unresolved_rows": notes,
            },
            ensure_ascii=False,
            indent=1,
        )
        + "\n",
        encoding="utf-8",
    )
    return result


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("slugs", nargs="*", help="article slugs; default is every article")
    parser.add_argument("--corpus", default="tara21")
    parser.add_argument(
        "--kind",
        choices=("term", "slot", "both"),
        default="both",
        help="term-articles/, slot-articles/, or both",
    )
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args(argv)

    settings = load_settings()
    corpus_dir = settings.corpus_dir(args.corpus)
    reg = registry_mod.load(corpus_dir)
    source_by_registered_id = {
        s.registered_id: s for s in reg.sources if s.registered_id and s.registered_id != "root"
    }
    terms = [t.term for t in reg.terms]

    folders: list[Path] = []
    for kind, folder in (("term", "term-articles"), ("slot", "slot-articles")):
        if args.kind in (kind, "both"):
            folders.extend(sorted(p for p in (corpus_dir / folder).glob("*") if p.is_dir()))
    if args.slugs:
        wanted = set(args.slugs)
        folders = [f for f in folders if f.name in wanted]
        missing = wanted - {f.name for f in folders}
        if missing:
            raise SystemExit(f"no such article slug(s): {', '.join(sorted(missing))}")

    results = []
    for folder in folders:
        try:
            results.append(import_one(folder, corpus_dir, terms, source_by_registered_id, dry_run=args.dry_run))
        except Exception as exc:  # a broken article must not stop the batch
            results.append({"slug": folder.name, "error": str(exc), "notes": []})

    if not args.dry_run:
        led = Ledger.load(ledger_path(settings.corpora_dir, args.corpus), corpus_id=args.corpus)
        now = datetime.now(timezone.utc).isoformat(timespec="seconds")
        for result in results:
            if "error" in result or not result.get("target"):
                continue
            entry = led.get(result["term"])
            if entry is not None and entry.status in {TermStatus.VERIFIED, TermStatus.APPROVED, TermStatus.PUBLISHED}:
                continue  # never walk a term backwards out of a passed gate
            led.set_status(result["term"], TermStatus.DRAFTED, now)
        led.save()

    width = max((len(r["slug"]) for r in results), default=4)
    unresolved = 0
    for result in sorted(results, key=lambda r: r["slug"]):
        if "skipped" in result:
            print(f"  {result['slug']:<{width}}  skipped — {result['skipped']}")
            continue
        if "error" in result:
            print(f"  {result['slug']:<{width}}  ERROR  {result['error']}")
            unresolved += 1
            continue
        flag = " " if result["in_terms_yaml"] else "?"
        print(
            f"  {result['slug']:<{width}} {flag} {result['term']:<20} "
            f"{result['citations']:>3} citations ({result['quoting']} quoting)"
        )
        for note in result["notes"]:
            print(f"      ! {note}")
            unresolved += 1

    print(f"\n{len(results)} articles, {sum(r.get('citations', 0) for r in results)} citations, {unresolved} unresolved rows")
    if args.dry_run:
        print("(dry run — nothing written)")
    print("? = lead term not found in terms.yaml; check the title before publishing.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
