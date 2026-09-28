---
name: dharmamitra-termlocked
description: >
  Produce a **vocabulary-standardised** translation through DharmaMitra's cat-translate
  API: build a lock glossary from the track's termbase (or from
  2-RAILS/Keywords/source-term-registry.json), send it with every call so the API
  uses the locked rendering instead of its own, then mechanically verify that every
  lock that should have applied actually landed, and re-run only the blocks where it
  did not.

  Trigger on "term-locked translation", "translate with the termbase", "vocabulary-
  standardised translation via DharmaMitra", "lock the vocabulary and translate",
  "re-translate with the standardised terms", "check the locks landed".

  This is NOT `dharmamitra-translate`. That skill produces the zero-shot machine
  baseline with no termbase, by design. This one produces a governed track and
  writes to a different folder, so the two are never confused.
---

# dharmamitra-termlocked

`dharmamitra-translate` answers *what does the machine say on its own?* — and its value
depends on nothing being whispered to it. This skill answers a different question: *what
does the text say when the tradition's own vocabulary is fixed in advance?* Both are
wanted, and they must not be mixed in one file, so this skill writes its own track and
labels it `track_type: term-locked`.

| Phase | Does | Writes |
|---|---|---|
| 1 — Build | Turns the termbase into a lock glossary and reports its coverage **before any call is spent** | `<track>/lock-glossary.tsv` + coverage report |
| 2 — Translate | Runs `dm_translate.py` with the glossary, into the term-locked track | `<track>/<stem>-<tag>.md` + ledger |
| 3 — Verify | Checks every lock that should have applied per block: EXACT / LOOSE / MISSING | `<track>/work/lock-report.json` |
| 4 — Repair | Re-runs only the MISSING blocks, solo, and re-verifies | updated ledger + re-render |

Phase 3 is not optional. The lock is a prompt-side instruction, and a prompt-side
instruction is strong, not total — see **What the API actually does** below. The
guarantee comes from the check, not from the asking.

---

## What the API actually does — measured, not assumed

Probed against `cat-translate` on 2026-09-22 with this vault's root text, four arms per
block (control / glossary in `context` / glossary in `style_instruction` / both), the
locked renderings chosen to differ from the zero-shot output so any effect is mechanically
visible.

| Call shape | Control | With glossary |
|---|---|---|
| Solo calls, 3 blocks, 11 locks | 5 / 11 | **10 / 11** |
| One batched call (3 blocks, `[[n]]` markers), 11 locks | 3 / 11 | **10 / 11** |

Four things follow, and the skill is built on them:

1. **The lock works.** The jump from 3/11 to 10/11 on a batched call is the whole
   justification for this skill existing.
2. **Batching is safe.** All three `[[n]]` markers came back intact in every glossed arm.
   There is no need to force `--batch 1`; the default batch of 3 keeps the run short.
3. **Injection position does not matter.** `context`, `style_instruction` and both scored
   identically. The skill therefore uses `dm_translate.py`'s existing `context` path and
   adds nothing — there is no evidence a second copy helps.
4. **The residual failure is inflection, not drift.** The single miss in both runs was a
   locked `pāramitās` coming back as `pāramitā`. That is why Phase 3 grades
   EXACT / LOOSE / MISSING and treats LOOSE as landed. A check that demanded exact strings
   would report a false failure here and send a good block back for a wasted re-run.

A fifth observation is worth recording because it argues for this skill from the other
side: the control arm rendered ‌རོ་ལངས་ as `vetālas`, while the committed zero-shot baseline
file renders the same block as `Zombies`. Same endpoint, same text, different run. The
machine's unlocked vocabulary is not stable across runs, so "it got it right last time" is
not a property anything can be built on.

The probe is reproducible: `references/glossary-probe-2026-09-22.md`.

---

## Two failure modes this skill exists to prevent

**The silent shad.** Registry lemmas carry a trailing shad (`སྒྲོལ་མ།`); running Tibetan
carries a tsheg (`སྒྲོལ་མ་`). `dm_translate.py` matches a glossary entry by plain substring,
so an unconverted lemma matches nothing and is dropped without a word. On this vault's root
text, **74 of 370 lemmas match as-is; 348 match after conversion.** A glossary fed in raw
produces a file that looks vocabulary-standardised and has four fifths of its vocabulary
unlocked. `build_lock_glossary.py` does the conversion and fails the run if coverage falls
below `--min-coverage`.

**The silent cap.** `dm_translate.py` sent at most 15 glossary entries per call as a
hard-coded constant. This corpus's busiest block (`^1-13`) matches 31 locks, so a sixth of
the vocabulary in that block would be dropped — again silently. The cap is now
`--glossary-max-hits` (with `--track-type` and `--rails-used` alongside it, so the
track is labelled for what it is), `build_lock_glossary.py` prints the busiest block's load, and every
ledger record carries `glossary_hits` and `glossary_dropped` so the audit is possible after
the fact.

---

## Inputs

| Input | Required | Description |
|---|---|---|
| **Source file** | ✓ | The block-ID'd root text under `1-SOURCES/Text/`. |
| **Target language** | ✓ | A language **label** (`english`), never an ISO code. Ask if not stated. |
| **Lock source** | ✓ | Either the track's `termbase.md` (**the canonical contract** — normal case) or `2-RAILS/Keywords/source-term-registry.json` with a renderings TSV. |
| **Track folder** | ✓ | `3-TRANSFORMATIONS/Translations/Dharmamitra-termlocked/<tag>/`. Never the zero-shot track. |
| **Style / context header** | — | `<track>/style.md`, `<track>/context-header.md`, seeded on first run exactly as in `dharmamitra-translate`. |

### Where the locked renderings come from

The registry is **descriptive**: it records which English words a term *has been* rendered
by. Locking is a **decision**, and decisions do not belong in `2-RAILS/`. The chain is:

```
2-RAILS/Keywords/source-term-registry.json      which terms, canonical lemma per concept
        ↓  term-definition
2-RAILS/termbases/term-localization.md          Meaning column: verbatim commentary definitions, cited
        ↓  term-localization
        same table, target-language columns     rendering derived from the definition, not a dictionary
        ↓  graded-translate Phase 1
<track>/termbase.md                             THE CONTRACT — one locked rendering per term
        ↓  this skill
```

`--use-first-rendering` short-circuits that chain by taking the registry's first attested
English gloss. It exists for a smoke test and produces exactly the quality you would
expect — on this corpus it yields locks like `water bear lotus` and `hum shatter`, which
are keyword-extraction glosses, not translations. **Never use it for a run anyone will
read.**

## Output

```
3-TRANSFORMATIONS/Translations/Dharmamitra-termlocked/<tag>/
├── about.md                      # what this track is, and how it differs from the baseline
├── style.md                      # style_instruction, verbatim (seeded, editable)
├── context-header.md             # work-neutral preamble (seeded, editable)
├── termbase.md                   # the contract this run locked to
├── lock-glossary.tsv             # what was actually sent, built from termbase.md
├── <source stem>-<tag>.md        # the translation
└── work/
    ├── <source stem>-<tag>.jsonl # ledger — each record carries glossary_hits
    ├── lock-coverage.txt         # Phase 1 report
    └── lock-report.json          # Phase 3 report
```

Frontmatter differs from the baseline track in exactly these keys:

```yaml
track: DharmaMitra term-locked (<language>)
track_type: term-locked          # NOT machine-baseline
rails_used: 2-RAILS/Keywords/source-term-registry.json, <track>/termbase.md
termbase: 3-TRANSFORMATIONS/Translations/Dharmamitra-termlocked/<tag>/termbase.md
lock_glossary: <track>/lock-glossary.tsv
locks_sent: <n>
locks_exact: <n>
locks_loose: <n>
locks_missing: <n>
status: draft
```

`locks_missing` must be `0`, or the shortfall is named in the report and in `note:`.
Never promote past `status: draft`; an LLM does not mark its own translation complete.

---

## Rules

1. **Never write into the zero-shot track.** `Dharmamitra/<tag>/` is the baseline and must
   stay unlocked — it is the control this track is measured against. Writing a term-locked
   file there destroys the comparison and is not recoverable from the ledger.
2. **Never run Phase 2 without Phase 1's coverage report.** A glossary that lost its locks
   to the shad problem costs a whole run to discover afterwards.
3. **Never skip Phase 3.** "Locked" without a check is a hope.
4. **LOOSE is a pass.** Inflection and pluralisation are the target language working
   normally. Only MISSING is actionable. `--strict` exists but is not the default.
5. **Every source block ID appears exactly once in the output**, in source order.
6. **Respect the daily quota** — 400 requests/day, ~10/min. A Phase 4 repair pass spends
   one call per block, so count the repairs before launching them. `--dry-run` costs
   nothing.
7. **The ledger is append-only.** To change a rendering, change `termbase.md`, rebuild the
   glossary, and re-run the affected blocks with `--force`.
8. **This output is still not a finished translation.** It goes to `commentary-fact-check`
   next; term-locking fixes vocabulary, not meaning.

---

## Procedure

All commands run from the vault root. `TRACK` below is
`3-TRANSFORMATIONS/Translations/Dharmamitra-termlocked/<tag>`.

### Step 1 — Build the lock glossary and read the coverage report

```bash
python3 4-SYSTEM/Skills/dharmamitra-termlocked/scripts/build_lock_glossary.py \
  --termbase "$TRACK/termbase.md" \
  --source "1-SOURCES/Text/<file>.md" \
  --out "$TRACK/lock-glossary.tsv" \
  | tee "$TRACK/work/lock-coverage.txt"
```

Read three numbers off the report before going further:

- **coverage %** — below 50% the script fails the run. Below ~90% on a termbase built for
  *this* text, something is wrong: wrong source file, or lemmas that were never converted.
- **locks that match no block** — each one is a term the termbase claims and the text does
  not contain. Legitimate for a termbase shared across texts; a mistake otherwise.
- **max locks in one block** — this sets `--glossary-max-hits` in Step 2. If it is 31, send
  at least 31.

### Step 2 — Smoke-test six blocks, then run the rest

```bash
python3 4-SYSTEM/Skills/dharmamitra-translate/scripts/dm_translate.py \
  --source "1-SOURCES/Text/<file>.md" --lang <language> \
  --out "$TRACK" \
  --track-type term-locked \
  --rails-used "2-RAILS/Keywords/source-term-registry.json, $TRACK/termbase.md" \
  --glossary "$TRACK/lock-glossary.tsv" \
  --glossary-max-hits <max from Step 1, rounded up> \
  --limit 6
```

Read the six blocks back against the termbase by eye before spending the rest of the run.
Then drop `--limit`. Blocks already in the ledger are skipped, so the same command resumes.

Translate the headings separately, as in `dharmamitra-translate`:

```bash
… --headings
```

### Step 3 — Verify the locks landed

```bash
python3 4-SYSTEM/Skills/dharmamitra-termlocked/scripts/check_locks.py \
  --glossary "$TRACK/lock-glossary.tsv" \
  --source "1-SOURCES/Text/<file>.md" \
  --translation "$TRACK/<stem>-<tag>.md" \
  --json "$TRACK/work/lock-report.json"
```

A lock is expected in a block iff its match form occurs in that block's **Tibetan** — the
expectation is read off the source, so it needs no verse rails. The script prints every
non-EXACT row and exits non-zero when anything is MISSING.

### Step 4 — Repair, then re-verify

`check_locks.py` prints the exact re-run flags. Run them, re-render, and run Step 3 again:

```bash
python3 4-SYSTEM/Skills/dharmamitra-translate/scripts/dm_translate.py \
  --source "1-SOURCES/Text/<file>.md" --lang <language> \
  --out "$TRACK" --track-type term-locked \
  --glossary "$TRACK/lock-glossary.tsv" --glossary-max-hits <n> \
  --force --batch 1 --only <comma-separated ids check_locks.py listed>
```

A block that is still MISSING after one solo repair is a **human decision**, not a third
re-run: either the locked rendering does not fit that block's syntax, or the termbase entry
is wrong. Record it in the report and in the track's `note:`; do not hand-edit the
translation to make the check pass.

### Step 5 — Report

Blocks done / total, calls spent, the coverage figure from Step 1, EXACT / LOOSE / MISSING
from Step 3, the blocks repaired, and any block still MISSING with the reason. State plainly
that the track is `status: draft` and has not yet been fact-checked.

### Step 6 — Hand off

`commentary-fact-check` next, against the verse-aligned commentaries in
`1-SOURCES/Commentaries/New raw data/` (the only ones carrying `![[…#^id]]` anchors), then
`claims-fact-check` for the consolidated cross-commentary view. Upload is
`translation-upload`'s decision and nobody else's.

---

## Completion check

- [ ] Lock source was a `termbase.md`, not `--use-first-rendering`
- [ ] Coverage report read before any API call; coverage plausible for this text
- [ ] `--glossary-max-hits` ≥ the busiest block's lock count from Step 1
- [ ] Output went to `Dharmamitra-termlocked/<tag>/`, never to `Dharmamitra/<tag>/`
- [ ] Six-block smoke test read back against the termbase
- [ ] Headings translated with `--headings`
- [ ] Every source block ID appears exactly once, in source order
- [ ] `check_locks.py` run; EXACT / LOOSE / MISSING recorded in the frontmatter
- [ ] Every MISSING either repaired or explained — none hand-edited away
- [ ] Frontmatter carries `track_type: term-locked`, `termbase`, `lock_glossary`, `status: draft`
- [ ] Nothing under `1-SOURCES/`, `2-RAILS/`, or the zero-shot track was modified

---

## Provenance

Written 2026-09-22 for this vault. Drives `dharmamitra-translate`'s `dm_translate.py`
rather than forking it; the two changes that skill needed are marked
`FORK(21-taras-rails)` in its source (`--glossary-max-hits`, and `glossary_hits` /
`glossary_dropped` on every ledger record). The EXACT / LOOSE matching tiers are imported
from `graded-translate`'s `check_termbase_consistency.py`, so the vault has one
implementation of them rather than two. `graded-translate` Phase 3 is the same check
against verse rails; this skill's variant reads its expectations off the Tibetan source
because this vault has no `2-RAILS/Verses/` yet.
