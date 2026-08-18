#!/usr/bin/env python3
"""Write the corpus registry at the path the pipeline actually reads.

``config.Settings.corpora_dir`` has resolved to ``3-TRANSFORMATIONS/Wikipedia/``
since the 2026-08-03 rewire, so ``kwiki`` looks for
``3-TRANSFORMATIONS/Wikipedia/<corpus>/sources.yaml``.  In this vault that file
was never written: the only registry is the frozen pre-migration one at
``corpora/tara21/sources.yaml``, whose ``local_path`` still names the corpus's
own private copy (``source/commentaries/TARAC02_DGT_bo_segmented.md``) and which
carries no ``registered_id``.  Every stage that resolves a source — align,
extract, verify — therefore finds nothing.

This script closes that gap without touching the frozen archive:

1. read the frozen registry for the curated metadata (title, author, school,
   genre, collection, scan_url, …), which is the part a human wrote and no
   script should regenerate;
2. join it to the vault by ``registered_id`` using the same siglum table
   ``migrate_tara21_to_vault.py`` used, resolving each id to the one
   ``1-SOURCES/Commentaries/*.md`` whose front matter declares it;
3. write a registry whose ``local_path`` is vault-relative and whose
   ``registered_id`` cross-references both that file and ``2-RAILS/Claims/``.

``source_id`` is deliberately carried over unchanged (``TARAC02_DGT_bo_segmented``).
It is the stable siglum every existing artifact — citations, ledger, the archived
2026-08-02 run — was written against; the file it points at is free to move.

Idempotent: re-running reproduces the same file.  ``--dry-run`` prints the plan.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

import yaml

_PIPELINE_ROOT = Path(__file__).resolve().parents[1]
_VAULT_ROOT = _PIPELINE_ROOT.parents[2]

#: registered_id -> corpus siglum.  Same table as ``migrate_tara21_to_vault.MAPPINGS``;
#: duplicated rather than imported so this script stays runnable if that one-shot
#: migration script is ever retired.
COMMENTARY_SIGLA: dict[str, str] = {
    "drakpa-gyaltsen": "TARAC02_DGT",
    "gendun-drub": "TARAC03_GDD",
    "gendun-gyatso": "TARAC04_GDG",
    "taranatha": "TARAC05_TRN",
    "anon-utpala": "TARAC06_NDB",
    "konchok-thabkhe": "TARAC07_KTK",
    "tenga-tulku": "TARAC08_DTG",
    "anon-trinle-char": "TARAC09_ANON",
    "pema-namgyal": "TARAC10_DPN",
    "karma-maitri": "TARAC11_KMT",
    "palden-sherab": "TARAC12_PDS",
    "tenzin-dhonzang": "TARAC13_TDZ",
    "lobsang-dawa": "TARAC14_LZD",
    "sangye-nyentrul": "TARAC15_SNT",
    "sungrab-tulku": "TARAC16_PSR",
    "tsultrim-namdak": "TARAC17_TSN",
}

FRONTMATTER_ID = re.compile(r"^registered_id:\s*(\S+)\s*$", re.MULTILINE)


def vault_commentaries() -> dict[str, Path]:
    """``{registered_id: path}`` for every ``1-SOURCES/`` commentary that declares one."""
    found: dict[str, Path] = {}
    for path in sorted((_VAULT_ROOT / "1-SOURCES" / "Commentaries").glob("*.md")):
        match = FRONTMATTER_ID.search(path.read_text(encoding="utf-8")[:4000])
        if match is None:
            continue
        registered_id = match.group(1)
        if registered_id in found:
            raise SystemExit(
                f"two commentaries claim registered_id {registered_id!r}: "
                f"{found[registered_id].name} and {path.name}"
            )
        found[registered_id] = path
    return found


def vault_root_text() -> Path:
    texts = sorted((_VAULT_ROOT / "1-SOURCES" / "Text").glob("*.md"))
    if len(texts) != 1:
        raise SystemExit(f"expected exactly one root text in 1-SOURCES/Text/, found {len(texts)}")
    return texts[0]


def rel(path: Path) -> str:
    return str(path.relative_to(_VAULT_ROOT))


def build(corpus: str) -> tuple[dict, list[str]]:
    frozen_path = _PIPELINE_ROOT / "corpora" / corpus / "sources.yaml"
    if not frozen_path.exists():
        raise SystemExit(f"no frozen registry at {frozen_path}")
    data = yaml.safe_load(frozen_path.read_text(encoding="utf-8"))

    by_siglum = {sid: rid for rid, sid in COMMENTARY_SIGLA.items()}
    commentaries = vault_commentaries()
    notes: list[str] = []

    for source in data["sources"]:
        if source["source_id"] == "root":
            source["registered_id"] = "root"
            source["local_path"] = rel(vault_root_text())
            continue
        siglum = source.get("siglum")
        registered_id = by_siglum.get(siglum)
        if registered_id is None:
            notes.append(f"! {siglum}: no registered_id in the siglum table — left unresolved")
            source.setdefault("registered_id", None)
            continue
        path = commentaries.get(registered_id)
        if path is None:
            notes.append(f"! {registered_id} ({siglum}): no 1-SOURCES file declares it")
            source["registered_id"] = registered_id
            continue
        source["registered_id"] = registered_id
        source["local_path"] = rel(path)

    unclaimed = set(commentaries) - {
        s.get("registered_id") for s in data["sources"] if s.get("registered_id")
    }
    for registered_id in sorted(unclaimed):
        notes.append(
            f"! {registered_id}: in 1-SOURCES but not in the registry — "
            "no citation can name it until a human adds an entry"
        )

    data["generated_by"] = "scripts/build_vault_registry.py"
    data["generated_from"] = f"corpora/{corpus}/sources.yaml (frozen pre-migration registry)"
    return data, notes


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--corpus", default="tara21")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args(argv)

    data, notes = build(args.corpus)
    out = _VAULT_ROOT / "3-TRANSFORMATIONS" / "Wikipedia" / args.corpus / "sources.yaml"

    for source in data["sources"]:
        print(f"  {source['source_id']:<28} {source.get('registered_id') or '—':<18} {source.get('local_path')}")
    for note in notes:
        print(note)

    if args.dry_run:
        print(f"\n(dry run) would write {out}")
        return 0

    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(
        yaml.safe_dump(data, allow_unicode=True, sort_keys=False, width=10**6),
        encoding="utf-8",
    )
    print(f"\nwrote {out}")
    return 1 if any(n.startswith("!") for n in notes) else 0


if __name__ == "__main__":
    sys.exit(main())
