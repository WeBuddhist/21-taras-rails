Run the article pipeline for one or more key terms. Arguments: $ARGUMENTS

Expected form: `<corpus-id> <term> [more terms...]`, e.g. `spyodjug བྱང་ཆུབ་ཀྱི་སེམས།`.
If no term is given, pick the next `pending` term from the ledger (`kwiki status <corpus>`).

## Before you start

1. Read `4-SYSTEM/Pipelines/wikipedia/docs/reference/wikitext-spec.md` — it is the output contract — and skim
   `4-SYSTEM/Pipelines/wikipedia/docs/reference/cowork-pipeline.md` — the canonical 17-step pipeline this chain implements
   (stages 4–7 here are its steps 6–12; the skills live in `4-SYSTEM/Pipelines/wikipedia/cowork-pipeline/`).
2. Confirm the corpus is aligned:
   `3-TRANSFORMATIONS/Wikipedia/<corpus>/work/aligned.json` must exist. If not, run
   `./4-SYSTEM/Pipelines/wikipedia/.venv/bin/kwiki align <corpus>` first and **read the coverage table** — a commentary below
   ~50% coverage will contribute little, and that is worth telling the human before spending tokens.
3. Confirm the commentaries carry block IDs (`grep -c ' \^' 1-SOURCES/Commentaries/*.md`).
   If they do not, run `/ingest`'s `kwiki commentaries <corpus>` step first. Without them every
   citation can name only a file, and the segment-provenance numbers below will all be zero.
4. Confirm the Gemini key loads:
   `./4-SYSTEM/Pipelines/wikipedia/.venv/bin/python -c "from kangyur_wiki.config import load_settings; print(load_settings())"`
   should print `gemini_api_key=<set>`. It is read from `.env` in the pipeline folder (`4-SYSTEM/Pipelines/wikipedia/`). If it is missing,
   stop and say so; do not fake a run.

## Run

**Pick the path first.** If the term already has a bo.wikipedia article (check
`3-TRANSFORMATIONS/Wikipedia/<corpus>/terms.yaml` — a `wikipedia_url` means it exists; 520 of 545 spyodjug terms do),
use the **update path**; otherwise the create path.

Create path (stages 4–7: extract → claims → outline → draft [→ polish] → audit → verify):

```bash
./4-SYSTEM/Pipelines/wikipedia/.venv/bin/kwiki article <corpus> <term>
```

Add `--polish` for the optional stage-6a literary rewrite. The claims table (stage 4b) is the
hinge: from it on, **the drafting model never sees source wording** — it cites claim indices, and
the code expands them to the passages and renders the refs. The audit (stage 6b) reads the
drafted text back against the claims table; the deterministic verify gate still runs last.
Single stages can be re-run from disk: `kwiki claims|polish|audit|verify <corpus> <term>` (a
re-run of `claims` invalidates everything after it — re-run outline → draft → audit → verify).

### Which model runs which stage — this matters for what you report

The canonical design uses **two models with different jobs**: Claude for the reading and
judgment stages (claims, draft, audit), Gemini for one thing only — the literary Tibetan
rewrite. *"The stylist is never trusted; the auditor never writes."*

- **The Gemini stage has its own script**, which is what the polish skill declares:
  ```bash
  ./4-SYSTEM/Pipelines/wikipedia/.venv/bin/python 4-SYSTEM/Pipelines/wikipedia/scripts/gemini_polish.py <corpus> <term>
  ```
  It pins and logs the model version per run, and enforces the four hard constraints in code —
  a rewrite that changes any citations array, paragraph count, heading order or see-also is
  rejected whole and nothing on disk changes. `--dry-run` renders the handoff prompt without
  calling anything. `kwiki polish` is the same code by another door.
- **`kwiki article` runs everything on Gemini by default**, because the pipeline ships only a
  Gemini client. That means the audit judges the draft its own model wrote, which is
  materially weaker — a model is a poor judge of its own drift. The run prints a note saying so.
  Two ways out, in increasing order of fidelity: `--audit-model <other>` for cross-model
  independence, or the Claude route below.
- **The Claude route** (the pipeline's headless equivalent of a Cowork skill) — use it for any run
  whose audit or claims numbers will appear in the paper:
  ```bash
  ./4-SYSTEM/Pipelines/wikipedia/.venv/bin/python 4-SYSTEM/Pipelines/wikipedia/scripts/claude_article.py prompt <term> audit
  ```
  That renders the real prompt to a file; read it, write the JSON reply next to it, then
  `apply` runs the repo's own stage code on your answer. Stages: `extract`, `claims`,
  `organize`, `draft`, `audit`, `verify`. Whatever ran is recorded in `model.json`.

**Never report a same-model audit as though it were independent.** If the paper's evaluation
section cites audit findings, say which model audited which model's text.

Update path (extract → classify against the live article → merge → verify):

```bash
./4-SYSTEM/Pipelines/wikipedia/.venv/bin/kwiki update <corpus> <term>
```

Both write everything under `3-TRANSFORMATIONS/Wikipedia/<corpus>/articles/<term>/`. The update path additionally
writes `existing.wiki` (the snapshot it ran against), `update_ops.json` (the model's
classification), and `update_report.md` (applied/skipped operations, ⚑ conflicts, and the diff).
**Read the ⚑ conflicts to the human verbatim** — they are the cases the pipeline refused to
decide, and deciding them is the human's job, not yours.

## After a double-PASS: the vault's own Local-Wiki

`kwiki article` auto-emits to `2-RAILS/Local-Wiki/<term>.md` the moment both the audit and the
deterministic verify gate pass — the same grounding material (contextual definition from the
lead, verbatim per-commentary attestations, any contested claims as Divergences), rendered into
the vault's own rails format rather than left stranded in `3-TRANSFORMATIONS/`. Read the emitted
file and report its counts (commentaries cited, attestations, divergences) alongside the article
numbers below. If it was skipped (the CLI reports why rather than failing the run), say so and
run it by hand once the cause is fixed: `kwiki local-wiki <corpus> <term>` (same status gate as
`kwiki publish` — the term must already be `verified` or later).

## Then report honestly

Read `3-TRANSFORMATIONS/Wikipedia/<corpus>/articles/<term>/report.md` and `audit.md`, and tell the human:

- how many passages were extracted, from how many distinct commentaries;
- how many **claims** they became, and the claim-type distribution — how many are below
  consensus (`school-position`, `single-commentator`, …), because those carry mandatory in-text
  attribution and are what the audit protects;
- the **audit verdict** and every blocking finding verbatim (added facts and attribution loss
  block publication — that is load-bearing invariant 2 of the canonical pipeline);
- whether verification **passed or failed**, and for failures, quote the actual finding — never
  summarise a failure as a success;
- **how many citations name the commentary block they came from**, and how many of those locators
  are wrong (the "Segment provenance" section of the report). A wrong locator is not a failed
  citation — the quotation is real and in the file it cites — but it sends a reviewer to the wrong
  paragraph, so report it rather than rounding it away;
- any citation that resolved to no URL (these are listed as warnings and need a human to add a
  source link);
- the token/cost figures if the run reported them.

If verification failed, diagnose before re-running. The usual causes, in order of likelihood:

1. **A quotation is not verbatim** — the model paraphrased at extract time. This is a prompt
   problem, not a code problem. Look at `extract.json` and compare against the commentary file.
   Compare against the *reading view*, not the raw bytes: `python -c "from
   kangyur_wiki.stages.commentary import reading_view; ..."`. The gate reads through the block IDs
   and anchors, so eyeballing the raw file will show you carets the checker never saw.
2. **`{{Reflist}}` crept in** (rule V4) — the emitter should make this impossible; if it happens,
   the bug is in `wiki/wikitext.py`, not the prompt.
3. **A section has no citation** (V8) — the outline put a heading where there was no material.

A *locator* failure is different and never blocks: the model echoed the wrong `segment_id`. Fix it
in the prompt (`4-SYSTEM/Pipelines/wikipedia/prompts/04-extract/`), not in the gate.

If the **audit** failed, run the feedback step (canonical step 13,
`4-SYSTEM/Pipelines/wikipedia/cowork-pipeline/13-feedback/`): classify each finding by the stage that caused it —
extraction (passage missed or mistagged) · claims (claim wrong, mistyped, badly worded) · draft ·
rewrite — and propose a one-line patch to that stage's prompt. In this pipeline a prompt patch means a
**new version file** under `4-SYSTEM/Pipelines/wikipedia/prompts/<stage>/` recording what changed and why, plus the same change
in `4-SYSTEM/Pipelines/wikipedia/docs/reference/cowork-pipeline.md` (the canonical home) and the skill. Never edit a shipped
prompt version in place. If the causal stage is the rewrite, check `model.json`'s pinned model
version before blaming the prompt.

Do not add a bypass flag, and do not lower a rule's severity to make a run pass — the audit's
blocking categories (`AUDIT_BLOCKING`) may not be shrunk either.
