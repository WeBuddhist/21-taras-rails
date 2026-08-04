# `corpora/` — frozen historical archive (2026-08-04)

**This directory no longer feeds the pipeline.** As of 2026-08-04 the live data for `tara21`
lives in two vault-native locations:

- **Annotated sources** (cleaned text, block IDs, root-verse transclusion anchors) —
  `1-SOURCES/Text/` and `1-SOURCES/Commentaries/`. These were adopted from
  `tara21/source/` by `scripts/migrate_tara21_to_vault.py`; see that script's docstring for
  exactly what moved and the identity checks it ran before writing anything.
- **Derived pipeline artifacts** (registries, ledger, per-term article state) —
  `3-TRANSFORMATIONS/Wikipedia/tara21/`. `config._default_corpora_dir()` resolves here
  automatically whenever `3-TRANSFORMATIONS/` exists, which it now always does.

Nothing here is read by `kwiki` anymore. It is kept because parts of it are **not
regenerable** and are cited by the IATS paper and by `REVIEW-2026-08-02.md`.

## What's here and why it stays

| Path | Status | Why it's frozen rather than deleted |
|---|---|---|
| `tara21/source/` | superseded by `1-SOURCES/` | The pre-migration annotated bodies, byte-identical (mod. anchor target) to what `1-SOURCES/` now carries — kept as the fork point the migration script diffed against. |
| `tara21/work/archive/` | **not regenerable** | `sandbox-run-2026-08-02/`, `audit-rounds-2026-08-02/`, `fix-pass-2026-08-02/` — the only surviving record of the cloud sandbox run, the overwritten Gemini audit rounds, and the exact fix-pass diffs. See that folder's own README for file-by-file provenance. |
| `tara21/work/ingest/`, `tara21/work/eval/` | historical | Stage 1b intermediates and the per-stage evaluation numbers (`EVAL_REPORT.md`) behind the paper's capture-rate figures. |
| `tara21/INGEST_REPORT.md`, `tara21/REVIEW-2026-08-02.md` | historical | The narrative record of the 2026-08-02 run. **Read `REVIEW-2026-08-02.md` before citing any number from that run** — it is the source of truth for what the pilot articles actually verified. |
| `tara21/sources.yaml`, `terms.yaml`, `ledger.json` (old copies, if still present) | superseded | `sources.yaml`'s `local_path` values here are the pre-migration corpus-relative form (`source/commentaries/…`); the live copy at `3-TRANSFORMATIONS/Wikipedia/tara21/sources.yaml` has vault-relative paths and an added `registered_id` per entry. Do not edit either copy expecting it to affect the other. |
| `_raw_f/`, `སྒྲོལ་མ་ཉེར་གཅིག/`, `tara21_pipeline_output*` | historical | The original upload and the 2026-08-02 sandbox delivery package, as received. |

## Old → new path map

| Old (`corpora/tara21/…`) | New |
|---|---|
| `source/root.md` | `1-SOURCES/Text/སྒྲོལ་མ་ཉེར་གཅིག་གི་བསྟོད་པ།.md` |
| `source/commentaries/TARAC{02..17}_*_bo_segmented.md` | `1-SOURCES/Commentaries/*.md` (matched by `registered_id`; see `sources.yaml`'s `registered_id` field for the mapping) |
| `sources.yaml`, `terms.yaml`, `ledger.json` | `3-TRANSFORMATIONS/Wikipedia/tara21/{sources.yaml,terms.yaml,ledger.json}` |
| `articles/<term>/` | `3-TRANSFORMATIONS/Wikipedia/tara21/articles/<term>/` |
| `review/{pending,approved,published}/` | `3-TRANSFORMATIONS/Wikipedia/tara21/review/…` |
| `work/aligned.json` | `3-TRANSFORMATIONS/Wikipedia/tara21/work/aligned.json` (regenerated fresh against the new paths, not moved) |

One set mismatch, noted in `STATE.md` and resolved during migration: `TARAC03_GDD` (Gendun
Drub's ṭīkā) existed only here, not in the original `1-SOURCES/` upload — it is now
`1-SOURCES/Commentaries/…ཊཱིཀྐ་རིན་པོ་ཆེའི་ཕྲེང་བ།.md`, `registered_id: gendun-drub`.
`anon-rnam-snang` (Dharmabhadra) is the reverse case — in the vault, not in this corpus —
and remains unregistered in the pipeline; still flagged for a human look (its title
duplicates the root text's own Kangyur title).

## The scripts in `scripts/` that reference the old layout

`ingest_tara21.py`, `ingest_tara21_local.py`, `enrich_tara21_terms.py`,
`stamp_en_blockids.py` are one-shot ingest tools from the original ingest run. They still
operate correctly against this frozen `corpora/tara21/` tree (that is what they were built
for) but are not part of the live pipeline path and will not touch `1-SOURCES/` or
`3-TRANSFORMATIONS/`. Left as-is; historical record of how the corpus was originally built.
