# CLAUDE.md

> **Scope.** These instructions govern work **inside this folder only** —
> `4-SYSTEM/Pipelines/wikipedia/`. Everywhere else in the vault, the rules in
> [`4-SYSTEM/CLAUDE.md`](../../CLAUDE.md) apply, including the read-only rule on `4-SYSTEM/`. This
> folder is the exception: it is a working program, and refining its code, prompts and docs is the
> job. It does **not** license edits to `4-SYSTEM/Skills/`, `4-SYSTEM/Guidelines/`, or anything in
> `1-SOURCES/`, `2-RAILS/`, `3-TRANSFORMATIONS/` — the citation chain still holds.
>
> "This repo" below means this folder. Paths are relative to it unless they start with `4-SYSTEM/`.
> Moved here from IATS-2026 on 2026-08-03; see `STATE.md` for what changed in the move.

Agent entry point for this pipeline. Read [`STATE.md`](STATE.md) first — it is the handover note saying
what works, what is blocked, and what comes next. Then [`PLAN.md`](PLAN.md) for the architecture,
[`docs/reference/cowork-pipeline.md`](docs/reference/cowork-pipeline.md) for the canonical 17-step
pipeline the team designed (the article chain implements its steps 6–12), and
[`docs/reference/wikitext-spec.md`](docs/reference/wikitext-spec.md) for the output contract.

## Slash commands

| Command | Use it for |
|---|---|
| `/ingest <corpus> <root> [commentaries...]` | Bring a new text in: clean, segment, headings, block IDs, anchors, align |
| `/pipeline <corpus> <term>` | Generate and verify one term's article (extract → claims → outline → draft [→ polish] → audit → verify) |
| `/publish <corpus> <term>` | Dry-run, pre-publication review, then publish to bo.wikipedia |
| `/paper [section]` | Work on the IATS paper |

## Setup, if the environment is cold

Run everything from this folder. The venv is not committed — create it once:

```bash
python3 -m venv .venv && ./.venv/bin/pip install -e '.[dev]'
cp .env.example .env      # then add GEMINI_API_KEY
./.venv/bin/python -m pytest -q
./.venv/bin/python -c "from kangyur_wiki.config import load_settings; print(load_settings())"
```

The last line should print `gemini_api_key=<set>`. `.env` in this folder is read by
`config.load_settings()`; a real environment variable of the same name wins over it.

## What this repo is

Two things: the IATS 2026 paper (`paper/`) and the pipeline that the paper is about. The pipeline
takes a Tibetan root text plus its commentaries and produces cited Tibetan Wikipedia articles,
creating or updating them on bo.wikipedia behind a human review gate.

## Before any task

1. **`docs/reference/wikitext-spec.md` is the output contract.** The drafting prompt targets it,
   the validator enforces it, the publisher ships it. Do not change the emitted format anywhere
   else; change the spec and let the other two follow.
2. **Prompts live in `prompts/`, versioned, with YAML front-matter recording provenance.**
   Finalized 2026-08-02: the tree holds exactly **one active version per stage** — the version the
   library renders — and each file's front matter records what it derives from. Superseded
   versions (including the original forum harvests) are staged in `_to_delete/prompts/` pending
   the human emptying it; git history is the archive. The rule going forward is unchanged: never
   rewrite a shipped version in place — patch `docs/reference/cowork-pipeline.md` (the canonical
   home) and the matching skill first, then add a **new version file** here recording what changed
   and why, and stage the old one for deletion once the new one is proven.
3. **the vault's `4-SYSTEM/Skills/` holds skills ported from sibling repos** (`webuddhist-library-data-pipeline`,
   `bodhisattvacharyavatara-rails`). Prefer porting their proven scripts over writing new logic;
   they have been used in production. The ingest chain is clean → segment (root:
   `format-tibetan-root-text`, commentaries: `commentary-segmentation`) → TOC (`add-toc`,
   `tag-inline-toc`) → lint (`lint-annotations`) → align (`Transclusion-rootext-into-commentaries`).
   For a corpus with no curated term list: `zeroshot-translator` → `english-keyword-extraction`
   builds a bilingual en↔bo candidate list for human review. `term-definition-from-commentaries`
   is the proven reference contract behind `prompts/04-extract`.

   `cowork-pipeline/` is different in kind: the team's own 17-step pipeline as one
   skill per step, generated in the lead's claude.ai session (2026-08-01) and kept verbatim —
   its `PROVENANCE.md` maps every step to what this repo implements, and
   `docs/reference/cowork-pipeline.md` is the reconstructed canonical document behind it. Prompt
   patches land in that document first, then sync to the skill and to a **new version file**
   under `prompts/` (the step-13 feedback rule).

   Where a vendored script has been changed, the change is recorded in that skill's Provenance
   section with the measurement that justified it. Two are changed so far, both in the commentary
   chain; read those notes before touching either script.

4. **Segmenting a commentary is half the job.** `kwiki commentaries <corpus>` is the other half —
   sa-bcad headings, root-verse transclusion anchors, and a block ID on every content block. Skip it
   and alignment is entirely probabilistic and a citation can name a file but not a passage.
   `docs/reference/conventions.md` §1a is the grammar.

5. **The reading view is the contract between ingest and the gate.** Ingest may add scaffolding to a
   `source/` file; `commentary.reading_view()` must be able to take all of it back off, and stage 7
   compares quotations against that view rather than the raw bytes. Add a layer the view does not
   know about and faithful quotations start failing on the pipeline's own marginalia — which in the
   report is indistinguishable from a hallucinating model.

## Two rules that are load-bearing

**Never emit `{{Reflist}}`.** bo.wikipedia's `Template:Reflist` begins with its own
`== ཡོང་ཁུངས། ==` heading, so `== ལུང་ཁུངས། ==` + `{{Reflist}}` renders two stacked headings.
Always `== ལུང་ཁུངས། ==` followed by `<references />`. This is verified against a live render, and
it is the single most likely failure mode because the `{{Reflist}}` idiom is correct on English
Wikipedia and every LLM reaches for it by default.

**Nothing writes to Wikipedia without an explicit `--execute`.** `dry_run=True` is the default on
`WikiClient` and on every publish path. A dry run plans the edit, writes a report, and makes no
network write. Treat `--execute` the way `data-pipeline` treats its uploader: explicit human
confirmation, every time.

## The verification gate is not optional

Stage 7 (`verify`) is deterministic, blocking, and uses no LLM. A quotation that does not appear
character-for-character in its cited source file fails the build. This is the mechanism the paper's
central argument rests on — that human-verified, citation-audited generation is what separates this
from the machine-translation flooding that has damaged other small-language Wikipedias. Do not add
a bypass flag.

Two more invariants joined it from the canonical pipeline (2026-08-02) and are equally
non-negotiable:

- **Claims-only drafting** (stage 4b): after the claims table is built, the drafting model never
  sees source wording — it cites claim indices, and code expands them to passages and renders the
  refs. Do not pass passages back into the draft or polish prompts.
- **The audit blocks** (stage 6b): added facts and attribution loss (`AUDIT_BLOCKING`) fail the
  build regardless of the model's own verdict. The LLM audit complements the deterministic gate —
  it reads meaning, the gate reads characters — and neither replaces the other.

## Per-corpus contract

**Sources and derived artifacts live in two different places as of 2026-08-04** (see
`STATE.md`'s dated entry for the migration that made this so). Sources are the vault's own
ground truth, annotated in place; everything the pipeline derives lives under its own corpus
folder in `3-TRANSFORMATIONS/`:

```
1-SOURCES/Text/<root>.md              root text — segmented, block-ID'd, NEVER modified
                                       except by the sanctioned `kwiki commentaries` promotion
1-SOURCES/Commentaries/<title>.md     one file per commentary, same contract

3-TRANSFORMATIONS/Wikipedia/<corpus-id>/
  sources.yaml     source registry: metadata + citation URLs — curated, hand-editable;
                   `local_path` names the `1-SOURCES/` file directly (vault-relative);
                   `registered_id` cross-references that file's own frontmatter and
                   `2-RAILS/Claims/`
  terms.yaml       key-term registry from the team's sheet — curated, hand-editable
  work/            aligned.json                             — reproducible, don't hand-edit
  articles/<term>/ extract.json, claims.json, sections.json, draft.json, draft_polished.json?,
                   audit.json + audit.md, article.wiki, citations.json, report.md, model.json
  claims/          claims-extraction method comparisons (opus/sonnet/toc-scaffolded/
                   tree-guided) — pipeline-owned, not `2-RAILS/Claims/` rails; see
                   `claims/_comparison-report.md`
  review/          pending/ → approved/ → published/         — the human gate
  ledger.json      status per term, resumable
```

The old `corpora/<corpus-id>/` layout (a private copy of the sources plus everything above)
is frozen at `corpora/` — see `corpora/README.md` for exactly what moved where and why some
of it (the 2026-08-02 run's archive) stays there permanently, not regenerable.

## Conventions

- Block IDs: `^chapter-verse` (`^1-1`, `^6-33`), not zero-padded. Heading IDs end in `-0`.
  Same scheme as the sibling OpenPecha repos — see `docs/reference/conventions.md`.
- Tibetan text is always NFC-normalized. Tsheg is U+0F0B (་), shad U+0F0D (།). Never "fix"
  Tibetan punctuation in stored source data.
- Secrets come from `.env` via `config.Settings`. Never read `os.environ` directly in a stage,
  and never log a credential.
