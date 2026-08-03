#!/usr/bin/env python3
"""Turn one tab of the team's Google Sheet export into a corpus registry.

Run this, not a hand edit, when the sheet changes:

    python scripts/export_corpus_registry.py \\
        --tab སྤྱོད་འཇུག --corpus-id spyodjug

It writes ``corpora/<corpus-id>/sources.yaml`` and ``terms.yaml``, which are
version-controlled and *are* the pipeline's input — the sheet itself is never
read at run time.  Because the extraction is a script rather than a one-off,
re-exporting after the editors add fifty terms is a one-line diff to review
instead of an afternoon of transcription.

``--split-index`` pins the source/term boundary when the heuristic guesses
wrong; run with ``--dry-run`` first to see what it inferred.

Stdlib + the package only.  No network: the two JSON artifacts under
``research/`` are the export.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_REPO_ROOT / "src"))

from kangyur_wiki.registry import load_from_xlsx_export, save  # noqa: E402


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--tab", required=True, help="sheet tab name, e.g. སྤྱོད་འཇུག")
    parser.add_argument(
        "--corpus-id", required=True, help="directory name under corpora/, e.g. spyodjug"
    )
    parser.add_argument(
        "--registry-json", default=str(_REPO_ROOT / "research" / "registry.json")
    )
    parser.add_argument(
        "--hyperlinks-json", default=str(_REPO_ROOT / "research" / "hyperlinks.json")
    )
    parser.add_argument("--corpora-dir", default=str(_REPO_ROOT / "corpora"))
    parser.add_argument(
        "--split-index",
        type=int,
        default=None,
        help="pin the first term row (0-based) instead of inferring it",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="report what would be written without writing it",
    )
    args = parser.parse_args(argv)

    registry = load_from_xlsx_export(
        args.registry_json,
        args.hyperlinks_json,
        args.tab,
        corpus_id=args.corpus_id,
        split_index=args.split_index,
    )
    linked = sum(1 for term in registry.terms if term.exists_on_wiki)
    print(
        f"{args.tab}: split_index={registry.split_index} "
        f"sources={len(registry.sources)} terms={len(registry.terms)} "
        f"({linked} already on bo.wikipedia)"
    )
    if args.dry_run:
        return 0

    sources_path, terms_path = save(registry, Path(args.corpora_dir) / args.corpus_id)
    print(f"wrote {sources_path}")
    print(f"wrote {terms_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
