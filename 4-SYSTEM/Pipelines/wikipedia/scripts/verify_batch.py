#!/usr/bin/env python3
"""Run the deterministic gate over every drafted article and write one report.

``kwiki verify`` is per-term and exits non-zero on failure, which is right for a
gate and useless for a batch: what a reviewer needs before a publication round is
the distribution — how many articles pass, which rules they trip, and the exact
list of quotations that are not in the file they cite.

No LLM, no network.  Writes ``work/VERIFY-BATCH.md`` under the corpus and prints
the summary.  Re-run it after any fix pass; the numbers are the fix's evidence.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path

_PIPELINE_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_PIPELINE_ROOT / "src"))

from kangyur_wiki import registry as registry_mod  # noqa: E402
from kangyur_wiki.config import load_settings, vault_root  # noqa: E402
from kangyur_wiki.stages.commentary import reading_view  # noqa: E402
from kangyur_wiki.tibetan.verify import check_quote  # noqa: E402
from kangyur_wiki.wiki.validator import validate  # noqa: E402
from kangyur_wiki.wiki.wikitext import Citation  # noqa: E402

from kangyur_wiki.cli import DEFAULT_CATEGORIES  # noqa: E402  (single source of truth)

FINDING = re.compile(r"^(V\d+)")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--corpus", default="tara21")
    args = parser.parse_args(argv)

    settings = load_settings()
    corpus_dir = settings.corpus_dir(args.corpus)
    reg = registry_mod.load(corpus_dir)
    root = vault_root()

    reading: dict[str, str] = {}
    for source in reg.sources:
        if source.local_path is None:
            continue
        path = root / source.local_path
        if path.exists():
            reading[source.source_id] = reading_view(path.read_text(encoding="utf-8"))

    def loader(source_id: str) -> str:
        return reading.get(source_id, "")

    rows = []
    codes: Counter[str] = Counter()
    failures: list[tuple[str, str, str]] = []
    quoted_total = quoted_ok = 0

    for article in sorted((corpus_dir / "articles").glob("*")):
        wiki_path, cite_path = article / "article.wiki", article / "citations.json"
        if not (wiki_path.exists() and cite_path.exists()):
            continue
        wikitext = wiki_path.read_text(encoding="utf-8")
        citations = [Citation(**c) for c in json.loads(cite_path.read_text("utf-8"))]

        ok = n = 0
        for citation in citations:
            if not citation.quote:
                continue
            n += 1
            if check_quote(citation.quote, loader(citation.source_id)).passed:
                ok += 1
            else:
                failures.append((article.name, citation.source_id, citation.quote))
        quoted_total += n
        quoted_ok += ok

        findings = validate(
            wikitext,
            citations=citations,
            allowed_categories=list(DEFAULT_CATEGORIES),
            source_loader=loader,
        )
        errors = [f for f in findings if f.severity == "error"]
        for finding in errors:
            codes[finding.rule] += 1
        rows.append((article.name, ok, n, len(errors), sorted({f.rule for f in errors})))

    clean = sum(1 for r in rows if r[3] == 0)
    lines = [
        "# Verification batch — deterministic gate only",
        "",
        f"corpus `{args.corpus}` · {len(rows)} drafted articles · no LLM, no network.",
        "",
        f"- **{quoted_ok} of {quoted_total} quotations ({100 * quoted_ok / max(quoted_total, 1):.1f}%) "
        "appear character-for-character in the commentary they cite.**",
        f"- {clean} of {len(rows)} articles carry no validator error.",
        f"- validator errors by rule: {', '.join(f'{c}×{n}' for c, n in sorted(codes.items())) or 'none'}",
        "",
        "| article | quotes verified | validator errors | rules |",
        "|---|---|---|---|",
    ]
    for name, ok, n, errors, rule_codes in rows:
        lines.append(f"| {name} | {ok}/{n} | {errors} | {', '.join(rule_codes) or '—'} |")

    if failures:
        lines += ["", "## Quotations not found in the cited commentary", ""]
        lines += ["| article | source | quotation |", "|---|---|---|"]
        for name, source_id, quote in failures:
            lines.append(f"| {name} | {source_id} | {quote[:90]} |")

    out = corpus_dir / "work" / "VERIFY-BATCH.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print("\n".join(lines[2:9]))
    print(f"\nwrote {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
