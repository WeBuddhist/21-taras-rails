# Fix passes over the sandbox drafts, 2026-08-02 — complete edit record

Author of every edit: claude-fable-5 (Claude Code, local session), acting as the
Claude leg of the pipeline per STATE.md's "Claude route" note. Every pass re-rendered
`article.wiki`/`citations.json` through `render_draft_payload` (the same deterministic
renderer `run_draft` uses) with a code assertion that **no citation changed**, then
re-ran `kwiki audit` (gemini-3.5-flash) and `kwiki verify`. Summarized per-article in
`model.json → fix_passes`; adjudication in `../../..​/REVIEW-2026-08-02.md`; the audit
rounds these responded to are in `../audit-rounds-2026-08-02/`.

## Pass 1 — `fix_pass.py` (this directory)

Responds to audit round 1 (5 blocking findings) + the lead term-duplication defect.
Six edits; exact old→new strings are in the script itself. Baseline drafts (pre-edit)
are byte-preserved in `../sandbox-run-2026-08-02/<term>/draft.json`.

## Pass 2 — lead restoration (inline script; edits recorded here)

Audit round 2 exposed a seam: the auditor reads `draft.json`, the reader sees
`render(draft.json)` — the truncated leads from pass 1 audited as "missing subject".
Fixed at the root by the `render_lead` dedup guard (emitter, with unit test), then the
natural leads were restored so the audited text equals the read text. Rendered output
asserted byte-identical before/after. The three edits (prefix replacements on
`lead[0].text`):

| term | old prefix | new prefix |
|---|---|---|
| སྒྲོལ་མ | `ཞེས་པའི་མིང་གི་ངེས་ཚིག་ལ་` | `སྒྲོལ་མ་ཞེས་པའི་མིང་གི་ངེས་ཚིག་ལ་` |
| འཇིག་རྟེན་གསུམ | `ཞེས་པ་ནི་ཐུན་མོང་` | `འཇིག་རྟེན་གསུམ་ཞེས་པ་ནི་ཐུན་མོང་` |
| སྡུག་བསྔལ | `ཞེས་པའི་མིང་དོན་ལ་བརྟེན་ནས་` | `སྡུག་བསྔལ་ཞེས་པའི་མིང་དོན་ལ་བརྟེན་ནས་` |

## Pass 3 — སྡུག་བསྔལ lead rewrite to claim-0's frame (inline script; edit recorded here)

Responds to audit round 3's borderline objection to the lead's derivational connective
("based on the meaning of the word suffering"), by hewing to claim 0's own frame
(མཚན་དོན་གྱི་སྐབས་སུ). One prefix replacement on `lead[0].text`:

- old: `སྡུག་བསྔལ་ཞེས་པའི་མིང་དོན་ལ་བརྟེན་ནས་སྒྲོལ་མའི་མཚན་གྱི་དོན་ཡང་འགྲེལ་བར་བྱེད་དེ། སེམས་ཅན་རྣམས་`
- new: `སྡུག་བསྔལ་ནི། སྒྲོལ་མའི་མཚན་དོན་གྱི་སྐབས་སུ་མཁས་པ་རྣམས་མཐུན་པར། སེམས་ཅན་རྣམས་`

After pass 3: audit **publish, 0 findings** and verify **PASS** on all three; ledger
set `verified` per `cli.article` semantics (both gates passed).
