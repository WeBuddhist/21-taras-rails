# Where we left off

Updated **2026-08-02**. This file is the handover note — read it first in a new session, then
[`PLAN.md`](PLAN.md) and [`docs/reference/cowork-pipeline.md`](docs/reference/cowork-pipeline.md).

## Moved into the rails vault — 2026-08-03

**This pipeline now lives at `4-SYSTEM/Pipelines/wikipedia/` inside the `21-taras-rails` vault, and
that is where the work happens from here.** The IATS-2026 repo is no longer the working copy. Every
path in this file that was repo-root-relative is now relative to this folder, with two exceptions:

- The **ingest-chain skills** moved to the vault proper, `4-SYSTEM/Skills/` — `clean-raw-text`,
  `format-tibetan-root-text`, `commentary-segmentation`, `tag-inline-toc`, `lint-annotations`,
  `Transclusion-rootext-into-commentaries`, `english-keyword-extraction`,
  `term-definition-from-commentaries`, `zeroshot-translator`. `skill_script()` in
  `stages/commentary.py` resolves them there. `vendor/skills/` no longer exists; where this file
  says `vendor/skills/<name>`, read `4-SYSTEM/Skills/<name>`. The team's 17-step
  `cowork-pipeline/` set stayed here, at the top of this folder.
- `add-toc` was **not** carried over — the vault already had its own, which writes to
  `0-INBOX/temp/` rather than `texts/<id>/work/`. Use the vault's.

Everything else came across whole and was verified in place on 2026-08-03: **547 passed, 1 skipped**;
`kwiki align tara21` reproduces **314 spans, 209 transclusion-anchored**; `kwiki verify` gives
**PASS ×3** with **81/81 citations block-located**. The numbers below still hold.

Slash commands are `/ingest`, `/pipeline`, `/publish`, `/paper` in the vault's `.claude/commands/`.
Setup is in [`README.md`](README.md) — the venv is not committed, so create it before first use.

### Rewired to read 1-SOURCES — same day, second pass

The pipeline no longer keeps its own copy of the texts. `config.vault_root()` locates the vault;
the root text and commentaries are resolved out of `1-SOURCES/` through each `sources.yaml`
entry's `local_path`, and every derived artifact now defaults to
`3-TRANSFORMATIONS/Wikipedia/<corpus>/`. `source_id` is unchanged, so the existing articles,
citations and ledger stay valid. 547 tests still pass. Both defaults fall back to the old
in-folder layout for a standalone checkout.

**`corpora/` cannot be deleted yet — two things block it:**

1. **`1-SOURCES/Commentaries/` has not been through the ingest chain.** All 16 files carry
   0 block IDs, 0 headings, 0 transclusion anchors; the root text uses `1.`/`2.` line numbers,
   not `^1-1`. Their text *is* the same as the corpus copies — verified at 99.25% on
   `TARAC02_DGT`, the difference being non-breaking tsheg U+0F0C → U+0F0B, exactly what
   `clean-raw-text` normalises. The chain has to run over them before `kwiki align` or any
   citation can resolve.
2. **The two sets are not the same 16 texts.** Joined by title against
   `scripts/ingest_tara21.py`'s own siglum table, 15 of 16 map cleanly. The exceptions:
   - `TARAC03_GDD` — དགེ་འདུན་གྲུབ, *ཊཱིཀྐ་རིན་པོ་ཆེའི་ཕྲེང་བ* — is **in the corpus, not in the
     vault**, and is **cited 10 times** across the three verified articles (third most-cited).
   - `R1B1817B6` — དྷརྨ་བྷ་དྲ, *ཡང་དག་པ་རྫོགས་པའི་སངས་རྒྱས་...* — is **in the vault, not in the
     corpus**.

   Both came from the same upload: `corpora/སྒྲོལ་མ་ཉེར་གཅིག/` holds Gendun Drub's commentary as
   `རྒྱལ་བ་དགེ་འདུན་གྲུབ་ཀྱི་སྒྲོལ་མའི་འགྲེལ་པ།.docx.txt`, one of four `.docx` editions the vault
   ingest did not take. Resolving this is a human call, not a merge conflict to guess at.

## Works right now

The repo is installed and runnable. 546 tests pass (`./.venv/bin/python -m pytest`).

```bash
./.venv/bin/kwiki align spyodjug        # 7,279 aligned spans across 10 commentaries
./.venv/bin/kwiki terms spyodjug        # 545 terms seeded, 520 already have bo.wiki articles

./.venv/bin/kwiki commentaries tara21   # stage 1b: headings, anchors, block IDs
./.venv/bin/kwiki align tara21          # 315 spans, 209 of them transclusion-anchored, 85.6% mean coverage
./.venv/bin/kwiki article tara21 སྒྲོལ་མ།  # now the full chain: extract → claims → outline → draft → audit → verify
```

**`tara21` now has three articles through the FULL new chain (claims → draft → audit → verify),
cross-model audited and ledger-`verified`.** Written by claude-sonnet-5 in a cloud sandbox,
reviewed and re-gated locally on 2026-08-02 — the review, the five audit findings, the fix pass,
and the remaining debts are all in **`corpora/tara21/REVIEW-2026-08-02.md`** (read it before
citing any number in the paper). The paper draft and slide deck built from that reviewed run live
in `paper/draft/`.

## What changed on 2026-08-02 (fifth session — the sandbox run reviewed, cross-model audited)

The lead ran the pipeline over tara21 in a cloud sandbox (Gemini blocked there, so the whole
chain ran on claude-sonnet-5 via the Claude stand-in route) and dropped the output zip into
`corpora/`. This session reviewed it end to end — full narrative in
`corpora/tara21/REVIEW-2026-08-02.md`. The short version:

- **The gate reproduces.** `corpora/tara21/` was rebuilt from the raw upload
  (`corpora/_raw_f/` + `scripts/ingest_tara21.py`, paths repointed), and local `kwiki verify`
  produced byte-identical PASS reports for all three articles: 81/81 quotations
  character-for-character real. After the deterministic `kwiki commentaries --skip-toc` +
  `kwiki align` restore (314 spans, 209 transclusion), all 81 citations' block locators
  resolve — the sandbox's "0 block-located" was its own verify failing to resolve IDs that
  were in the artifacts all along.
- **The same-model audit was wrong and the cross-model audit proved it.** The sandbox's
  claude-audits-claude verdicts were "publish, no findings" ×3. Local gemini-3.5-flash audits
  found 5 blocking findings on 2 articles; hand-adjudication against claims.json confirmed 4
  genuine (consensus exaggeration, overgeneralization, མཚན་དོན→མཚན་ཉིད shift, attribution
  beyond the claim) + 1 borderline (claim-metadata-supported). Fixed by surgical draft.json
  edits, re-rendered deterministically (`render_draft_payload`; citation arrays asserted
  unchanged), re-audited to **publish 0 findings ×3 + verify PASS ×3**, ledger `verified` ×3.
  Every edit is logged in each article's `model.json` under `fix_passes`.
- **`render_lead` now dedups a lead that opens with the term** (every Claude draft did;
  `'''term'''term...` was the result). Emitter-side, spec output unchanged, test added; suite
  546 passed + 1 skipped. The audit also exposed a seam worth knowing: it audits `draft.json`,
  the reader sees `render(draft.json)` — keep drafts' leads natural (the renderer handles the
  bold), or the auditor flags phantom "missing subject" errors.
- **Auditor variance is real** (novel borderline lead objections in 3 of 4 rounds; two
  findings quoted the draft with typos the draft doesn't contain — grep before believing an
  audit quote). `06b-audit/v1` catches what matters but needs a v2 pinning lead-framing and
  claim-metadata support; step-13 rule applies. Report audit outcomes as pass rates.
- Still owed before publish: **W2 everywhere** (no public URLs — bdrc_fetch), W4 length, the
  human term-list decision, and commit `2c2db31` dropped corpus sources from git while
  .gitignore's comment still claims the repo is self-contained — restore or re-document.

### Evaluation, translations, and cost (same day, third pass)

- **`scripts/eval_stages.py`** — the per-stage evaluation harness. Deterministic metrics
  per term (offer → capture → utilization → coverage → gate), plus `--audit-stability N`
  for repeated independent Gemini audits in an isolated temp workspace (no ledger churn).
  Report: `corpora/tara21/work/eval/EVAL_REPORT.md` + `eval.json`. The headline finding:
  **extraction capture is the weak stage and now has a number** — of what alignment
  offered, extraction captured 45% / 19% / **1.1%** (the biggest offer got the least;
  the tuning pass has its target). Everything downstream is tight: 100% extract-time
  quote fidelity, 100% passage utilization, 0 dropped claims, 100% claim coverage in
  drafts. **Audit stability on the final articles: pass rates 0.67 / 0.67 / 1.0 over
  3 runs each** — the pass-rate number the paper reports.
- **English check-translations** of all three articles (labeled review aids, by Claude):
  `articles/<term>/article.en.md` ×3, combined for the human reviewer at
  `review/pending/translations-for-review.en.md`. The deck now carries an English gloss
  on every Tibetan run (IATS audience), and the paper glosses all Tibetan inline.
- **Cost measured** (`paper/draft/cost-and-scalability.md`): 22 model calls, ~435k chars
  in / ~85k out for the three articles → **≈ $0.33–1.42/article on Gemini 3.5 Flash**
  (central ≈ $0.71; ≈2× on claude-sonnet-5 list). 100k articles ≈ $35–70k machine cost —
  one grant, one-time. The constraint is reviewer-minutes, by design; August batch
  measures it.

### Artifact preservation (same day, follow-up pass)

The review had itself destroyed evidence: `kwiki audit`/`verify` re-runs overwrote the
intermediate audit rounds in place. Fixed in both directions:

- **The pipeline now preserves before it overwrites.** Every per-stage writer
  (`_write_json`/`_write_text` in `stages/pipeline.py`) snapshots an existing artifact to
  `articles/<term>/history/<name>.<UTC>.<ext>` first — audit rounds, verify reports,
  drafts, the polish a re-draft invalidates (preserved, then unlinked), and the
  `model.json` reset at the top of `cli.article` (its per-stage *merges* stay exempt —
  they accumulate). `preserve_artifact()` is the one writer; regression test in
  `tests/test_pipeline_e2e.py::test_reruns_preserve_prior_artifacts_in_history`;
  **547 passed, 1 skipped**.
- **The run's full record is archived inside the corpus.** `corpora/tara21/work/archive/`:
  `sandbox-run-2026-08-02/` (byte copy of the package: pre-fix drafts, same-model audits,
  original reports), `audit-rounds-2026-08-02/` (the overwritten Gemini rounds 1–3,
  verbatim where read before overwrite, one file reconstructed-and-labeled; README maps
  provenance file by file), `fix-pass-2026-08-02/` (fix_pass.py + exact old→new strings
  of the two inline passes). Plus `corpora/tara21/INGEST_REPORT.md` (the dangling STATE
  reference now exists — local rebuild numbers), `scripts/ingest_tara21_local.py` (the
  repointed-paths runner as a committed script), `paper/draft/build_deck.js` + README
  (deck is regenerable), and empty `review/{pending,approved,published}/`.
- Unrecoverable, noted in the archive README: intermediate `audit.json` bytes (only the
  `.md` renderings survived), and the cloud-only `work/archive/claude-run-2026-08-01/` +
  `work/term_candidates.md` from sessions 2–3 — STATE.md's tables remain their citable
  record.

### Paper revision pass (same day — two external reviews answered)

The human brought a ChatGPT and a Gemini critique of `paper/draft/paper.md`; the draft was
revised against both (change log in the draft-status block at the top of the file).
Applied: case-study scoping in §1/§8/§10 (nothing published, N=3 framed as walkthrough +
existence proof), fidelity-vs-support-vs-notability separation (§5/§6/§8/§9),
corpus-relative gloss on claim types (§5), the secondary-source/notability double gate
(§6), a community-consent + update-path maintenance paragraph (§7, from the plan in
`paper/05`), OCR *sic*-faithfulness (§5/§9), close-paraphrase honesty (§5/§9), fixed
engineering cost + projection widened to $35k–140k (§8; cost note updated to match), and
the 23-root-unit clarification (§4 — verified against `root.md` + `aligned.json`: 22
stanzas `^1-1`…`^1-22` plus invocation `^I-1`). Checked and left standing: TLUE and Welsh
figures (match `paper/04`), WikiCrow's two metrics, all run numbers (match the REVIEW).
Deliberately not done: title change (the abstract is submitted verbatim and stands),
renaming the `consensus` claim type in code, a spyodjug dgag-lan mini-run for §6 (needs a
live model run + review before any number enters the paper — it is the single
highest-value pre-deadline addition), N expansion (term list still human-unapproved).
`build_deck.js` slide-9 speaker note updated to match; **the .pptx was not regenerated**
(no node_modules here) — regenerate with the [TO FILL] data pass.

### Paper restructured for the corpus-wide batch (same day)

The lead decided to generate articles for **all** tara21 keywords, so the draft no
longer rests on N=3: §8 is now two-scale — **pilot (N=3, hand-adjudicated, keeps the
audit-trail depth)** + **batch (corpus-wide, distributional)** — with every batch
number an explicit `[TO FILL]`. New file **`paper/draft/batch-reporting-checklist.md`**
enumerates every slot the batch feeds, section by section, plus what a bigger N does
*not* fix (human review still samples; notability still per-topic; W2 debt unchanged;
terms still `status: candidate`). §7's citation-debt sentence was generalized from
"all three articles" to a registry property so it does not go stale mid-batch.

**Three prerequisites the batch needs, all discovered while checking the numbers:**

1. **The term list is gone locally.** `corpora/tara21/terms.yaml` has only the pilot's
   3 terms; session 2's 105-candidate list was cloud-only (already listed as
   unrecoverable above). It is regenerable — `scripts/enrich_tara21_terms.py` carries
   the en→bo mapping inline: **96 distinct Tibetan terms over the 23 root units**. Needs
   its hardcoded `/tmp/iats` paths repointed, and the YAKE input JSON is absent from
   `vendor/skills/english-keyword-extraction/scripts/output/` (skippable — the script's
   own ranking uses `aligned.json` support).
2. **No batch runner.** `kwiki article` is one term per invocation; a driver is needed
   that tolerates per-term failure, records per-term wall-clock + call counts, and
   keeps the ledger resumable.
3. **The extraction tuning pass is still owed** (capture 45% / 19% / 1.1%). Running the
   batch pre-tuning is defensible — it yields the capture-vs-offer curve — but decide
   up front which run the paper reports, or articles get regenerated.

Also worth logging when the batch runs: **reviewer-minutes per article from the very
first article reviewed** — the paper's lead metric (§3/§8) is still `[TO FILL]` and
retrospective time estimates are unreliable per `paper/06`.

## What changed on 2026-08-02 (fourth session — the team's canonical pipeline landed)

The lead designed the full pipeline in two claude.ai sessions on 2026-08-01
(shares `09ecaf85…` and `dbdee4e9…`, links in the provenance files) and handed them over to be
merged. Their architecture takes precedence where it conflicts with what was here; the big
conflict was **drafting from organized passages** — replaced by **claims-only drafting**.

- **`vendor/skills/cowork-pipeline/`** — the 17 per-step skills from the first chat, verbatim
  (extracted from the share snapshot byte-for-byte; the ZIP itself is not downloadable). Its
  `PROVENANCE.md` maps every step to what this repo implements.
- **`docs/reference/cowork-pipeline.md`** — the canonical 17-step document reconstructed from
  the second chat (initial version verbatim + the four described edit rounds; the embedded
  prompts survive verbatim in the skills). It is the canonical home of the step prompts: patch
  there first, then sync to the skill and to a new `prompts/` version file.
- **New stages in `kwiki article`** (all wired, stub-tested, model-untested):
  - **4b claims** (`kwiki claims`, `prompts/04b-claims/v1.md`): passages → atomic claims table
    (`claims.json`) — one fact per row, own words, claim-typed (consensus / majority-with-dissent
    / school-position / single-commentator), reception-tagged (dgag lan as a due-weight signal).
    Claims with no valid passage indices are dropped at parse time.
  - **5 outline** (`prompts/05-organize/v2-claims-outline.md`): built from claims only, weighted
    by breadth × reception, `attribution_required` marks, gap report.
  - **6 draft** (`prompts/06-draft/v3-claims-only.md`): the drafter sees outline + claims only —
    never source wording. It cites claim indices; `render_draft_payload` expands them to passages
    and renders refs, so quotations enter the article only from `extract.json`.
  - **6a polish** (optional, `--polish` / `kwiki polish`, `prompts/06a-polish/v1-gemini-handoff.md`):
    the canonical `gemini_polish.py`. Hard constraints enforced in **code**: a changed citations
    array / paragraph count / heading order rejects the rewrite untouched.
  - **6b audit** (`kwiki audit`, `prompts/06b-audit/v1.md`): sentence-vs-claims reading check;
    `added-fact` and `attribution-loss` block regardless of the model's verdict
    (`AUDIT_BLOCKING` — do not shrink it). Audit failure → ledger `failed` → publish refuses.
  - The deterministic stage-7 gate is untouched and still runs last; the e2e test proves the
    corrupt-quote case fails the build even when the audit says publish.
- **Ledger** gained `claimed` and `audited` statuses; `model.json` now records the prompt file
  per new stage (and pins the polish model version — the feedback loop needs it to tell prompt
  problems from model drift).
- **`sources.yaml` schema extended** (`registry.Source`): `school` (feeds claims attribution),
  `copyright` (the **router**: PD → Wikisource anchors; else BDRC/WeBuddhist link),
  `author_dates`, `webuddhist_url` (now in the citation-URL preference chain after BDRC).
- **`scripts/bdrc_fetch.py`** — the canonical step-1 script, stdlib-only, tested live:
  `python scripts/bdrc_fetch.py W22084` follows scan → instance → work → creator, prints titles,
  author + dates, and the derived copyright hint (`copyrighted-assumed` + TODO when uncertain).
- **`prompts/08-review/v1-prepublication.md`** — the review gate that canonically gates the whole
  publication layer; `/publish` now runs it before any `--execute`.
- **`paper/10 - Canonical Paper and Slides Plan.md`** — the lead's paper structure + 16-slide
  deck (trilemma framing, revival §3, reviewer-hours lead metric), reconstructed with provenance;
  `00 - START HERE` points at it.
- Deliberately **not** changed: `prompts/04-extract/v2` (proven on tara21 — the chats' passage
  prompt adds nothing its contract lacks; its canonical text is preserved in skill 06 if the team
  wants to A/B it), the deterministic aligner (stronger than the chats' judgment-only step 2,
  same invariants), and the update path (still passage-based — claims-mode for updates is open).
- Not yet implemented from the canonical pipeline: Wikisource publishing and the Wikidata sync
  (steps 14–15 — no clients exist), the outlier stage (step 7) as code, and per-term locked
  glossaries (`glossary_for` returns the term itself for now).

**Expect the first live run of the new chain to need the tuning pass.** Every new prompt is
`model_tested: none`, written in English against Gemini, and the audit stage has never judged a
real draft. Run `kwiki article tara21 སྒྲོལ་མ།` (create path, small term first), read `claims.json`
and `audit.md` end to end, and version-bump prompts per the feedback rule rather than editing
them in place.

### Finalization pass (same day, second sitting)

On the lead's instruction the prompt tree was **finalized to one active version per stage** —
superseded versions moved to `_to_delete/prompts/` (the repo's staging-for-deletion idiom; git
history is the archive; the human empties the folder):

- moved: `02-align/v1-forum-236-v3` and `03-terms/v1-forum-289-v3` (never rendered by any code —
  align and terms are deterministic; kept until now as forum-harvest reference),
  `04-extract/v1`, `05-organize/v1`, `06-draft/v1-forum-324`, `06-draft/v2-canonical`.
- stayed: one prompt per stage — `01-toc/v1`, `04-extract/v2-block-locators`, `04b-claims/v1`,
  `05-organize/v2-claims-outline`, `06-draft/v3-claims-only`, `06a-polish/v1-gemini-handoff`,
  `06b-audit/v1`, `07-update/v1`, `08-review/v1-prepublication`.
- **`vendor/skills/` was deliberately NOT thinned**: the cowork-pipeline set replaces article
  *prompts*, not the ingest machinery — `clean-raw-text`, `commentary-segmentation`,
  `tag-inline-toc`, `lint-annotations`, `Transclusion-*` etc. are executed by
  `kwiki commentaries`/`/ingest`, and `english-keyword-extraction`/`zeroshot-translator` are the
  TF-IDF route the cowork step 3 assumes exists. `term-definition-from-commentaries` stays as the
  reference contract behind the active extract prompt.

The review pass over the finalized chain found and fixed three seams: (1) a re-run of the draft
stage now deletes a stale `draft_polished.json` (a later standalone `kwiki audit` would have
preferred old text; regression test added); (2) standalone `kwiki claims|polish|audit` now merge
their model + prompt version into `model.json` (`stage_models`), so the pin-and-log rule holds
on re-runs, where the feedback loop needs it most; (3) `kwiki claims` records an error string on
failure. PLAN.md's prompt-tree diagram and CLAUDE.md rule 2 were updated to the finalized
layout. 546 tests pass.

### The Gemini leg now has its script — and the model division is explicit

`scripts/gemini_polish.py` was the one script the canonical document names that did not exist
(the third, `publish.py`, is `kwiki publish` + the not-yet-built Wikisource/Wikidata legs). It
is the declared script of `vendor/skills/cowork-pipeline/11-polish/`: renders the handoff
prompt, calls Gemini, enforces the four hard constraints **in code**, writes back, and logs the
model version per run. `kwiki polish` and the script both call one `run_polish`, and
`pipeline.record_stage_model()` is now the single writer of `model.json` for every entry point,
so the pin-and-log rule cannot be bypassed by choosing a different door. `--dry-run` renders
the prompt without calling anything.

**The divergence worth knowing about, because it affects what the paper may claim:** the
canonical design runs Claude for claims/draft/audit and Gemini for the polish alone — *the
auditor never writes*. This repo ships only a Gemini client, so `kwiki article` runs every
model stage on Gemini, which means **the audit judges text its own model wrote**. That is now
surfaced rather than buried: the run prints a note whenever auditor == writer, `--audit-model`
buys cross-model independence, and `scripts/claude_article.py prompt|apply <term> audit` is the
Claude route (this repo's headless Cowork equivalent, and it also covers `claims` and `draft`).
Use the Claude route for any run whose numbers go in the paper, and never report a same-model
audit as independent. Full table in `vendor/skills/cowork-pipeline/PROVENANCE.md`.

## What changed on 2026-08-01 (third session — the commentaries became citable)

The second session's commentaries carried blocks and nothing else: no headings, no block IDs, no
anchors. Alignment was therefore 100% probabilistic and a citation could name a book but not a
passage. Both are fixed.

- **`kwiki commentaries <corpus>` — stage 1b**, the chain that was missing between segmentation and
  alignment: stage-2 refinement → sa-bcad headings (`tag-inline-toc`, Phase 1 on Gemini) →
  root-verse transclusion anchors → a block ID on every content block. Intermediates in
  `work/ingest/commentaries/`, summary in `work/ingest/COMMENTARY_REPORT.md`, promotion over
  `source/` only if every step held. Over tara21: **581 headings, 209 anchors, 3,947 block IDs**,
  16/16 files.
- **The invariant that makes it safe**: `commentary.reading_view()` takes every layer of scaffolding
  back off, and the result must be byte-identical (whitespace-collapsed) before and after each step.
  A file that fails is left alone and reported. The verify gate reads through the same view, so a
  quotation spanning a block boundary cannot fail on a caret the pipeline itself wrote.
- **Alignment, before → after**: 258 spans → **315**; all-cluster → **209 transclusion + 106
  cluster**; mean coverage 70.1% → **85.6%**; 0 → **7 of 16** commentaries at 100%; median span
  1,056 → **583 characters** (headings bound the spans).
- **Segment provenance end to end.** `segments_for_term` narrows an aligned span to the individual
  blocks that mention the term; the extract context labels each with its block ID; `Passage` →
  `Citation.segment_id` carries it to `citations.json` and the report; stage 7 additionally checks
  each quotation against *that block*. A wrong locator is a reported warning, never a gate failure —
  the quotation is real and in the file it cites. **All 51 citations across the three articles are
  block-located and every locator is correct.** `segment_id` is deliberately *not* rendered into the
  `<ref>`: the ref format is fixed by the spec and a block ID means nothing to a reader.
- **`.env` is now actually read.** `load_settings()` looked only at `os.environ`, so the key in the
  file the README tells you to create never reached the pipeline — the real reason every model stage
  reported "GEMINI_API_KEY is not set". Precedence is environment > `.env` > TOML > default, and an
  injected `env` mapping suppresses the file so tests stay hermetic.
- **Three fixes to `01_transclude_verses.py`** (recorded in that skill's Provenance). The
  load-bearing one: `is_closer()` compared Tibetan against Latin transliterations and could never
  fire, making the single-line-citation branch dead code — and the incipit-inside-a-`ཞེས`-frame is
  *the* citation shape in a བསྟོད་འགྲེལ. Regression-checked against the spyodjug vault's own anchors:
  782 placed vs 775, none lost.
- **`tag_inline_toc.py` accepts `body_start_line`**, a line number, as an alternative to the
  verbatim context string. On this corpus the context form is unusable — `དང་པོ་ནི།` recurs dozens of
  times per file and no substring of that line is unique — and a line number is the strongest form
  of the skill's own "the model never retypes prose, it only points" rule.
- **`prompts/01-toc/v1.md`** (new) and **`prompts/04-extract/v2-block-locators.md`** (v1 left
  intact; v2 pins what `segment_id` means and requires it back verbatim).

Built and tested: Tibetan normalization/verification/keyness · root↔commentary alignment
(deterministic, with a coverage report) · MediaWiki Action API client (dry-run default) · wikitext
emitter + 12-rule validator · Gemini client with caching and structured output · source/term
registry from the team's Google Sheet · ledger · CLI · the stage chain extract → organize → draft →
verify · **the update path** (`kwiki update`: classify duplicate/new/conflict against the live
article, insert-only merge, ⚑ conflicts for the human, orphaned-footnote repair, diff + audit
trail — `wiki/merge.py`, `run_update`, 16 tests).

Two end-to-end stub tests prove the safety property on both paths: a quotation that is not
character-for-character in its cited commentary **fails the gate** (`tests/test_pipeline_e2e.py`,
`tests/test_merge.py`).

## What changed on 2026-08-01 (second session — tara21 ingested, first real articles)

- **`tara21` ingested from the team's upload** (root + 16 commentaries + dkar-chag xlsx; 21 files
  minus the 4 duplicate editions the sheet itself flags). `scripts/ingest_tara21.py` is the
  reproducible ingest: clean (NFC, U+0F0C→U+0F0B, page-number lines) → root rebuilt as 21 homage
  stanzas `^1-1`…`^1-21` plus `^I-1` and the closing couplet `^1-22`, cross-checked against the
  annotated edition → commentaries through the vendored `preclean_commentary.py` +
  `segment_commentary.py --structural` (no-loss gated) → `sources.yaml` from the dkar-chag.
  Re-running it reproduces every `source/` file byte-for-byte.
- **Alignment**: 258 spans, all `cluster` method, coverage 47.8%–91.3% (mean ~70%) — higher than
  the spyodjug baseline because these are prose bstod-'grel that quote the stanza before
  expounding it. The two lowest (`TARAC04_GDG` 47.8%, `TARAC11_KMT`/`TARAC14_LZD` 52.2%) are the
  bsdus-'grel and mchan-'grel — the word-commentary pattern `align.py`'s docstring predicts.
- **Term list via the translation-mediated route** (no curated sheet exists for this corpus):
  the Lotsawa House English translation, block-ID stamped (`scripts/stamp_en_blockids.py`), through
  `english-keyword-extraction`'s YAKE and Reuters-IDF passes, then en→bo enrichment read off the
  aligned Tibetan stanza (`scripts/enrich_tara21_terms.py`). 129 enriched keywords → 105
  candidates → `terms.yaml` with `status: candidate` on every row. **They are candidates, not a
  curated list: a human has not approved them.** Ranked by aligned-commentary support in
  `work/term_candidates.md`.
- **Three articles generated and verified.** Superseded by the Gemini run — see the table below.
  The artifacts are archived at `work/archive/claude-run-2026-08-01/`.
- **Every citation is unlinked** (W2 on every one). The dkar-chag's only link per text is a Google
  Drive scan, which `resolve_citation_url` correctly rejects. **Still true after the Gemini run**,
  and still the single biggest thing an editor must fix before publishing: a reader cannot check any
  of these quotations.

### Superseded: the Claude stand-in run

`generativelanguage.googleapis.com` was 403'd at the egress proxy in the environment the second
session ran in, so stages 4–6 were driven by Claude through `scripts/claude_article.py`. **That is
no longer necessary** — the key loads and the API answers from this machine. The artifacts are kept
at `corpora/tara21/work/archive/claude-run-2026-08-01/` for the model comparison below, which is a
real result worth keeping rather than a workaround worth hiding.

### Claude vs Gemini on the same prompts — the tuning pass is still owed

| term | Claude (v1 prompts, span context) | Gemini 3.5 Flash (v2 prompts, block context) |
|---|---|---|
| `འཇིག་རྟེན་གསུམ།` | 16 passages, 7,901 chars | 19 passages, 5,628 chars, 3 sections |
| `ཡི་གེ་བཅུ་པ།` | 16 passages, 5,190 chars | 14 passages, 5,604 chars, 3 sections |
| `སྒྲོལ་མ།` | 35 passages, 13,050 chars | 19 passages, 7,508 chars, 4 sections |

All three Gemini articles **PASS**: 0 validator errors, every quotation exact, **50/50 citations
block-located with no wrong locator**, no `{{Reflist}}`. Each carries a `model.json` naming the
model and the prompt file per stage — `kwiki article` writes it now, rather than only the Claude
stand-in script.

The Gemini articles are **shorter on the term with the most material**, and the reason is measurable
rather than mysterious: asked about `སྒྲོལ་མ།` with 93,000 characters of context in one call, Gemini
returned ten passages totalling 873 characters — from the corpus's central term across sixteen
commentaries. The same model on the same prompt with 12,000 characters returned twenty passages
totalling 5,224. It budgets its answer against the size of the question.

`run_extract` therefore batches: material above `EXTRACT_BATCH_CHARS` (25,000) is split into several
calls, never splitting a commentary across two (rule ༦ asks which commentaries are silent, and the
model can only answer that about one it has seen whole). That alone took `སྒྲོལ་མ།` from 10 passages
to 18–19. **It has not closed the gap to Claude's 35, and that is the tuning pass this file has been
predicting since session one** — topic 289's author says the prompts were built and tested on Claude
only. Smaller batches, or a per-commentary pass, are the obvious next things to try.

### The gate bit, on a single shad

One `འཇིག་རྟེན་གསུམ།` run **failed**, on this quotation:

```
model:  འཇིག་རྟེན་གསུམ་ནི།  སྟེང་འོག་གི་དབྱེ་བས་རྩ་གསུམ་གསུམ་དྲུག་གོ།
source: འཇིག་རྟེན་གསུམ་ནི་  སྟེང་འོག་གི་དབྱེ་བས་རྩ་གསུམ་གསུམ་དྲུག་གོ།
```

A tsheg silently promoted to a shad. Similarity 0.974; caught at the `fuzzy` tier, which is
deliberately *not* a pass. Two things worth keeping:

- **This is the safety property working, on a real model, unprompted.** No human reviewer reading
  Tibetan prose at speed would have caught that, and it is precisely the kind of drift that makes a
  quotation not a quotation. It is the best evidence the paper has for the gate's value.
- **Runs are not deterministic.** The same term passed on the next attempt with no code change.
  Report a pass rate over repeated runs in the evaluation batch, never a single run.

### Two emitter issues the run surfaced (not blocking, not yet filed)

1. `see_also` renders `[[སྒྲོལ་མ་]]` — a trailing tsheg inside the link target, which will not
   match the bo.wikipedia title `སྒྲོལ་མ།`. Every article has this. `wiki/wikitext.py`.
2. The lead renders `'''སྒྲོལ་མ།'''་ནི་…` — shad-then-tsheg, from `join_boundary` on a
   shad-terminated term. Legal per V10, reads oddly.

## What changed on 2026-08-01

- **Update path built** (was "next move 3"). `kwiki update <corpus> <term>` fetches the existing
  article (any title variant, redirects followed; or `--from-file`), reuses `extract.json` when
  present, and writes `existing.wiki`, `update_ops.json`, `merged` → `article.wiki`,
  `update_report.md` (ops + ⚑ conflicts + diff), `report.md`. Verification policy for merges is a
  documented subset (`merge.BLOCKING_RULES`): new-quote gate + reference-display integrity block;
  the pre-existing page state (foreign refs, off-allowlist categories) is advisory.
- **Seven skills ported from the Obsidian vaults** into `vendor/skills/`, each with provenance:
  `commentary-segmentation` (deterministic, no-loss-gated), `add-toc`, `tag-inline-toc`,
  `lint-annotations`, `english-keyword-extraction` (YAKE/TF-IDF on an English translation +
  en→bo enrichment — the translation-mediated term route), `zeroshot-translator`,
  `term-definition-from-commentaries`. `/ingest` now sequences the full chain: clean → segment →
  TOC → lint → align, and documents the keyword route for corpora with no curated term list.
- **`docs/reference/conventions.md` written** (was referenced by CLAUDE.md and two skills but did
  not exist): block-ID grammar incl. `^I-*` intro, `^N-a` colophon and `^a-0` back-matter slots,
  transclusion forms, file naming/sigla, front matter, normalization, term identity.
- **`prompts/02-align/v1-forum-236-v3.md` created** from the harvested forum text (topic 236 v3,
  provenance in front matter; corpus names templated).
- Layout docs corrected (`sources.yaml`/`terms.yaml` live at the corpus root, not `source/`);
  README/PLAN status lines un-staled.

## No longer blocked on Gemini

`GEMINI_API_KEY` in `.env` at the repo root now reaches the pipeline (it never did before —
`load_settings()` read only `os.environ`). Check it with:

```bash
./.venv/bin/python -c "from kangyur_wiki.config import load_settings; print(load_settings())"
```

`gemini_api_key=<set>` means the create path runs. The **update** path has still never been run
against a live model — `kwiki update spyodjug བདེ་གཤེགས་` is the first thing to try, and
`prompts/07-update/v1.md` is our own authorship with no forum baseline, so inspect its first output
hard.

## Expect the first real run to need prompt work

The team's prompts in `prompts/` were harvested verbatim from the OpenPecha forum, but topic 289's
author states in Tibetan that it was **built and tested on Claude only**, and topics 309/324 label
their outputs `Claude Opus4` with a warning that other models differ. We are using Gemini. Budget a
tuning pass; add new version files rather than editing the harvested originals. The update prompt
(`prompts/07-update/v1.md`) is our own authorship — no forum baseline exists — so inspect its first
outputs especially hard.

## Decisions still open

Full list with recommendations in [`docs/reference/open-questions.md`](docs/reference/open-questions.md).
The ones that will come up first:

1. **Which corpus is the real v1 target?** The prompts are written around འཕགས་པ་སྡུད་པ; the
   published articles are about ཡིག་བརྒྱ; what is aligned here is the Bodhicaryāvatāra.
2. **Which Wikipedia account publishes?** A new bot account (flag approval takes weeks on a wiki
   with 2 admins) or an existing `Pecha-*` account with disclosure (available today).
3. **Gloss length** — the team's own specs contradict each other (<10 vs ≥10 ཚེག་བར). The validator
   rule is blocked until this is pinned.
4. **Title variant to create at** — `སངས་རྒྱས་`, `སངས་རྒྱས།` and bare all exist as separate pages.

## Next four moves

1. ~~Run the new chain live once~~ **Done (fifth session)** — three articles through the full
   chain, cross-model audited, ledger `verified`; see `corpora/tara21/REVIEW-2026-08-02.md`.
   What replaced it: **audit-prompt v2** (pin lead-framing and claim-metadata support — the
   review's findings table is the evidence base; step-13 rule) and **a repeated-runs pass
   rate** for the paper's evaluation table.
2. **Put public URLs in `corpora/tara21/sources.yaml`** — the copyright router now says how:
   `scripts/bdrc_fetch.py <RID>` per commentary for metadata + death dates → `copyright` field →
   PD texts queue for Wikisource, the rest get a BDRC/WeBuddhist `webuddhist_url`/`bdrc_id`
   link. Every citation in all three articles is unlinked (W2); an article whose quotations no
   reader can check is the thing the paper claims this pipeline does not produce.
3. **The extract tuning pass.** Gemini returns markedly less than Claude on a term with a lot of
   material (table above). Batching helped and did not finish the job. Try a smaller
   `EXTRACT_BATCH_CHARS`, or one call per commentary, and measure against the archived Claude run —
   `work/archive/claude-run-2026-08-01/` is the baseline. (The update path has also never touched
   a live model — `kwiki update spyodjug བདེ་གཤེགས་`.)
4. Dry-run publish to the userspace sandbox — now behind the pre-publication review
   (`prompts/08-review/`) — and look at it rendered on the real wiki: fonts, ref markers, the
   `<references />` block. Then the evaluation batch (`paper/06 - Evaluation Plan.md`, lead
   metric per `paper/10 - Canonical Paper and Slides Plan.md`); IATS is 23–29 August.

## Do not break these

- `docs/reference/wikitext-spec.md` is the output contract. Change it there, not in the emitter.
- Never emit `{{Reflist}}` — bo.wikipedia's template injects its own heading, producing a double
  heading. Always `== ལུང་ཁུངས། ==` + `<references />`.
- Nothing writes to Wikipedia without `--execute`, and the verification gate has no bypass — on
  the update path too (`merge.BLOCKING_RULES` may not be shrunk).
- An update never modifies existing article text: insert-only, conflicts go to the human ⚑.
- **The reading view is the contract between ingest and the gate.** Anything that adds scaffolding
  to a `source/` file must be removable by `commentary.reading_view()`, and the gate must keep
  reading through it. Add a layer without teaching the view about it and quote verification starts
  failing on the pipeline's own marginalia — which looks exactly like a hallucinating model.
- `Citation.segment_id` stays out of the rendered `<ref>`. It is internal provenance; the ref format
  is the spec's.
- **Claims-only drafting** (canonical invariant 1): never pass passages or source wording into the
  draft/polish prompts — the drafter cites claim indices and code renders the refs.
- **The audit blocks** (canonical invariant 2): `AUDIT_BLOCKING` (added-fact, attribution-loss)
  may not be shrunk, and an audit failure must keep the term off the publish path.
- Prompt patches follow the step-13 rule: canonical doc (`docs/reference/cowork-pipeline.md`)
  first, then the skill, then a **new version file** under `prompts/` — never an in-place edit.
