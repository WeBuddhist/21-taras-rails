# Audit rounds, 2026-08-02 — recovered record

The cross-model audit of the sandbox run was iterated four times on this machine, and at
the time `kwiki audit` **overwrote `audit.json`/`audit.md` in place** — the intermediate
rounds were destroyed as they were superseded. This directory reconstructs the record.
(The pipeline now preserves every outgoing artifact in `articles/<term>/history/` before
overwriting — `preserve_artifact` in `stages/pipeline.py`, added the same day, so this
cannot happen again.)

Auditor for every round here: **gemini-3.5-flash** via `kwiki audit tara21 <term>`.
The drafts audited were written by claude-sonnet-5 (sandbox run); the fix passes between
rounds are logged per-article in `model.json` under `fix_passes` and described in
`../fix-pass-2026-08-02/`. Adjudication of every finding: `../../..​/REVIEW-2026-08-02.md`.

## Provenance, file by file

**Preserved verbatim** — these files' contents are byte-faithful copies of the
overwritten `audit.md` files, captured by full reads during the session before each
overwrite:

| file | round | verdict |
|---|---|---|
| `round1-སྒྲོལ་མ.audit.md` | 1 (pre-fix drafts) | fix — 3 blocking |
| `round1-སྡུག་བསྔལ.audit.md` | 1 (pre-fix drafts) | fix — 2 blocking |
| `round2-སྒྲོལ་མ.audit.md` | 2 (post-fix, deduped leads) | fix — 1 blocking (render-seam false positive) |
| `round2-འཇིག་རྟེན་གསུམ.audit.md` | 2 | fix — 1 advisory (auditor's own transcription typo) |
| `round2-སྡུག་བསྔལ.audit.md` | 2 | fix — 1 blocking (render-seam false positive) |
| `round3-སྡུག་བསྔལ.audit.md` | 3 (natural leads restored) | fix — 1 blocking (borderline connective) |

**Reconstructed from the recorded verdict** (not preserved bytes — the file was
overwritten unread beyond the CLI verdict line; the no-findings rendering of
`AuditResult.format_report()` is deterministic, so the content is certain, but it is a
reconstruction and labeled as one):

| file | round | verdict |
|---|---|---|
| `round1-འཇིག་རྟེན་གསུམ.audit.md` | 1 | publish — 0 findings |

**Live in the article directories (not duplicated here):**

- Round 3 for སྒྲོལ་མ and འཇིག་རྟེན་གསུམ (publish, 0 findings) — those were their final
  audits; the current `articles/<term>/audit.md`/`audit.json` ARE those rounds.
- Round 4 for སྡུག་བསྔལ (publish, 0 findings) — its final audit, current on disk.
- Round 0, the sandbox's **same-model** audits (claude-sonnet-5 judging its own drafts;
  "publish, no findings" ×3) — byte-preserved in `../sandbox-run-2026-08-02/<term>/`.

**Unrecoverable:**

- The structured `audit.json` for rounds 1–3 (never read before overwrite; only the
  `audit.md` renderings above survive). The finding categories/severities are fully
  present in the `.md` renderings.
- From the earlier cloud sessions (they existed only on that machine's gitignored
  `work/`): `work/archive/claude-run-2026-08-01/` (the Claude-standin artifacts behind
  STATE.md's Claude-vs-Gemini extraction table) and session 2's
  `work/term_candidates.md` (the 105-candidate ranked list). STATE.md's numbers remain
  the citable record for both.

## Why this matters

The audit-stability observation in the review — same-model audit caught 0/5 real
findings; cross-model audit caught all 5 but with round-to-round variance and two
self-introduced misquotes — is evidence for the audit-prompt v2 (step-13 rule) and for
the paper's rule of reporting audit outcomes as pass rates over repeated runs. This
directory is that evidence's primary record.
