# Wikipedia pipeline (`kwiki`)

Moved here from the **IATS-2026** repo on 2026-08-03. **This is the working copy** — IATS-2026 is
no longer used for running or refining the pipeline. Give it a Tibetan root text and its
commentaries; it aligns them, selects key terms, extracts cited explanatory material, drafts
Tibetan Wikipedia articles, and creates or updates them on bo.wikipedia. A human review gate sits
before anything is published.

This is the pipeline behind the IATS 2026 paper *"Expanding the Digital Footprint of Tibetan: A
Semi-Automatic Pipeline for Wikipedia Article Generation Using LLMs"* — the paper notes and draft
are in `paper/`.

**Start at [`STATE.md`](STATE.md)** — the handover note: what works, what is blocked, what comes
next. Then [`PLAN.md`](PLAN.md) for the architecture.

---

## What is in this folder

| Path | What |
|---|---|
| `STATE.md` | ★ Handover note — read first |
| `PLAN.md` | Master build plan: architecture, stages, decisions, phasing, risks |
| `src/kangyur_wiki/` | The `kwiki` package — stages, CLI, Gemini client, wikitext emitter/validator, the deterministic verify gate |
| `scripts/` | Standalone scripts: `bdrc_fetch.py` (step 1), `gemini_polish.py` (canonical stage 6a), `claude_article.py` (the Claude stand-in route), `eval_stages.py` (per-stage evaluation harness), `export_corpus_registry.py`, `stamp_en_blockids.py`, and the tara21 ingest/term runners |
| `prompts/` | Versioned stage prompts, one active version per stage, YAML front matter recording provenance |
| `cowork-pipeline/` | The team's canonical 17-step pipeline, one skill per step, kept **verbatim** — see its `PROVENANCE.md` |
| `docs/reference/` | `wikitext-spec.md` (the output contract), `cowork-pipeline.md` (the canonical 17-step document), `conventions.md`, `open-questions.md` |
| `corpora/` | Per-corpus working directories — `tara21/` is the live one; see below |
| `research/` | The six research reports the code and validator cite for their empirical case, plus `registry.json` / `hyperlinks.json` (the corpus-registry export `export_corpus_registry.py` reads) |
| `paper/` | The IATS paper: notes `00`–`10`, `abstract.md` (submitted, verbatim — never edit its body), and `draft/` (paper.md, slide deck, cost-and-scalability, batch-reporting checklist) |
| `tests/` | 547 tests, no network |

The ingest-stage skills this pipeline drives — `clean-raw-text`, `format-tibetan-root-text`,
`commentary-segmentation`, `tag-inline-toc`, `lint-annotations`,
`Transclusion-rootext-into-commentaries`, `english-keyword-extraction`, `zeroshot-translator` —
live with the rest of the vault's skills in [`../../Skills/`](../../Skills/) and are registered in
[`SKILLS-CATALOG.md`](../../Skills/SKILLS-CATALOG.md). `kwiki commentaries` resolves their scripts
there directly.

## Setup

```bash
cd 4-SYSTEM/Pipelines/wikipedia && python3 -m venv .venv && ./.venv/bin/pip install -e '.[dev]'
```

Then `cp .env.example .env` and add `GEMINI_API_KEY`. `.venv/` and `.env` are gitignored.

```bash
./.venv/bin/python -m pytest -q
./.venv/bin/python -c "from kangyur_wiki.config import load_settings; print(load_settings())"
```

The last line should print `gemini_api_key=<set>`.

## Running it

```bash
./.venv/bin/kwiki align <corpus>            # deterministic, no key needed
./.venv/bin/kwiki commentaries <corpus>     # headings, root-verse anchors, block IDs
./.venv/bin/kwiki article <corpus> <term>   # extract → claims → outline → draft → audit → verify
./.venv/bin/kwiki update <corpus> <term>    # the update path (the majority case)
./.venv/bin/kwiki publish <corpus> <term>   # dry-run default; --execute to write
```

The slash commands `/ingest`, `/pipeline` and `/publish` (in the vault's `.claude/commands/`) drive
these with the full procedure and the reporting rules; `/paper` works on the paper. The vault's
`.claude/settings.json` allowlists the venv binaries, keeps `KWIKI_DRY_RUN=true`, and puts
`kwiki publish` behind an explicit ask.

## Where the texts come from — rewired 2026-08-03

The pipeline **no longer carries its own copy of the texts.** It reads the root text and the
commentaries out of the vault's `1-SOURCES/`, and writes every derived artifact to
`3-TRANSFORMATIONS/Wikipedia/<corpus>/`:

| | Where | What |
|---|---|---|
| in | `1-SOURCES/Text/`, `1-SOURCES/Commentaries/` | The texts, block IDs and anchors included. The rails work owns them — clean, segment, TOC, block IDs, transclusion anchors are all vault skills, and stages 1–2 of this pipeline *are* that work rather than a private duplicate of it. |
| out | `3-TRANSFORMATIONS/Wikipedia/<corpus>/` | `sources.yaml`, `terms.yaml`, `ledger.json`, `work/`, `articles/`, `review/` — all generated. Wikipedia articles are transformations, so they sit in the vault's citation chain. |

The binding between the two is `sources.yaml`: every entry's `local_path` names the `1-SOURCES/`
file it stands for. That is what lets `source_id` stay a stable siglum (`TARAC02_DGT_bo_segmented`)
while the file it points at is a Tibetan-titled source file — citations and existing artifacts
survive a rename. `config.vault_root()` finds the vault; both defaults fall back to the old
in-folder layout when the pipeline is checked out standalone.

## Corpora

> **Being retired.** `corpora/` is the pre-rewire layout, kept only until `1-SOURCES/` carries the
> ingest treatment and the one missing commentary is resolved (see `STATE.md`). Nothing new should
> be written here.

What is here:

| Path | What |
|---|---|
| `corpora/tara21/` | The live corpus: `source/root.md` + 16 segmented commentaries, `sources.yaml`, `terms.yaml`, `ledger.json`, `work/aligned.json`, three generated `articles/`, `INGEST_REPORT.md`, `REVIEW-2026-08-02.md`, and `work/archive/` — the run's full evidence record, **not regenerable** |
| `corpora/སྒྲོལ་མ་ཉེར་གཅིག/` | The original raw Tibetan inputs: 21 OCR/segmentation `.txt` files plus the dkar-chag `.xlsx` |
| `corpora/_raw_f/` | The 21 root-verse fragments `ingest_tara21_local.py` rebuilds from |
| `corpora/tara21_pipeline_output/` + `.zip` | The 2026-08-02 cloud sandbox package as delivered |

Verified in place on 2026-08-03: `kwiki align tara21` → 314 spans, 209 transclusion-anchored,
85.6% mean coverage; `kwiki verify` → PASS ×3, 81/81 citations block-located. Same numbers as
`STATE.md` reports.

Corpora are **tracked in git** here, unlike in IATS-2026 — this is the working repo, and
`work/archive/` is a citable record. Obsidian is told to ignore `4-SYSTEM/Pipelines/` (via
`.obsidian/app.json` → Files & Links → Excluded files), so the corpus intermediates stay out of
search and the graph while remaining on disk.

## Two rules that are load-bearing

**Never emit `{{Reflist}}`.** bo.wikipedia's `Template:Reflist` begins with its own
`== ཡོང་ཁུངས། ==` heading, so `== ལུང་ཁུངས། ==` + `{{Reflist}}` renders two stacked headings.
Always `== ལུང་ཁུངས། ==` followed by `<references />`.

**Nothing writes to Wikipedia without an explicit `--execute`.** `dry_run=True` is the default on
`WikiClient` and on every publish path.

## The verification gate is not optional

Stage 7 (`verify`) is deterministic, blocking, and uses no LLM: a quotation that does not appear
character-for-character in its cited source file fails the build. Two invariants sit beside it:
**claims-only drafting** (after the claims table, the drafting model never sees source wording —
it cites claim indices and code expands them), and **the audit blocks** (added facts and
attribution loss fail the build regardless of the model's verdict; `AUDIT_BLOCKING` may not be
shrunk). Do not add a bypass flag.

## Patching a prompt

Never rewrite a shipped version in place. Patch `docs/reference/cowork-pipeline.md` (the canonical
home) and the matching `cowork-pipeline/` skill first, then add a **new version file** under
`prompts/<stage>/` recording what changed and why. This is the step-13 feedback rule.
