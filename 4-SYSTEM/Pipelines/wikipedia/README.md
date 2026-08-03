# Wikipedia pipeline (`kwiki`)

Ported into this vault from the **IATS-2026** repo on 2026-08-03. Give it a Tibetan root text and
its commentaries; it aligns them, selects key terms, extracts cited explanatory material, drafts
Tibetan Wikipedia articles, and creates or updates them on bo.wikipedia. A human review gate sits
before anything is published.

This is the pipeline behind the IATS 2026 paper *"Expanding the Digital Footprint of Tibetan: A
Semi-Automatic Pipeline for Wikipedia Article Generation Using LLMs"*. The paper itself stays in
IATS-2026 — only the machinery came here.

---

## What is in this folder

| Path | What |
|---|---|
| `src/kangyur_wiki/` | The `kwiki` package — stages, CLI, Gemini client, wikitext emitter/validator, the deterministic verify gate |
| `scripts/` | Standalone scripts: `bdrc_fetch.py` (step 1), `gemini_polish.py` (canonical stage 6a), `claude_article.py` (the Claude stand-in route), `eval_stages.py` (per-stage evaluation harness), `export_corpus_registry.py`, `stamp_en_blockids.py`, and the tara21 ingest/term runners |
| `prompts/` | Versioned stage prompts, one active version per stage, YAML front matter recording provenance |
| `cowork-pipeline/` | The team's canonical 17-step pipeline, one skill per step, kept **verbatim** — see its `PROVENANCE.md` |
| `docs/reference/` | `wikitext-spec.md` (the output contract), `cowork-pipeline.md` (the canonical 17-step document), `conventions.md`, `open-questions.md` |
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

The slash commands `/ingest`, `/pipeline` and `/publish` (in `.claude/commands/`) drive these with
the full procedure and the reporting rules.

## Corpora

`kwiki` reads and writes `corpora/<corpus-id>/` **relative to this folder** — that directory did
not come across. The tara21 corpus (sources, 16 segmented commentaries, `aligned.json`, the three
generated articles, the review record and the raw OCR inputs) is still in
`~/Desktop/work/IATS-2026/corpora/`. Copy or re-ingest before running anything corpus-shaped.

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
