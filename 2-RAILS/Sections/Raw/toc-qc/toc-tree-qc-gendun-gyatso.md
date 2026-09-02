# TOC tree QC report

issues_before: 13
issues_after: 13 (all human-reviewed; 12 are a script false-positive, 1 is an accepted
                   genuine source gap — see notes below; no tree change warranted)

## Issues (raw qc_check_tree.py output)

- L11: title not attested in candidates/enumerations (coverage 0%) — possible hallucination  ->  1.1 དང་པོ་ནི [[27]]
- L12: title not attested in candidates/enumerations (coverage 0%) — possible hallucination  ->  1.2 གཉིས་པ་ནི [[37]]
- L13: title not attested in candidates/enumerations (coverage 0%) — possible hallucination  ->  1.3 གསུམ་པ་ནི [[41]]
- L14: title not attested in candidates/enumerations (coverage 0%) — possible hallucination  ->  1.4 བཞི་པ་ནི [[45]]
- L15: title not attested in candidates/enumerations (coverage 0%) — possible hallucination  ->  1.5 ལྔ་པ་ནི [[47]]
- L16: title not attested in candidates/enumerations (coverage 0%) — possible hallucination  ->  1.6 དྲུག་པ་ནི [[51]]
- L17: title not attested in candidates/enumerations (coverage 0%) — possible hallucination  ->  1.7 བདུན་པ་ནི [[53]]
- L18: title not attested in candidates/enumerations (coverage 0%) — possible hallucination  ->  1.8 བརྒྱད་པ་ནི [[57]]
- L19: title not attested in candidates/enumerations (coverage 0%) — possible hallucination  ->  1.9 དགུ་པ་ནི [[61]]
- L20: title not attested in candidates/enumerations (coverage 0%) — possible hallucination  ->  1.10 བཅུ་པ་ནི [[63]]
- L22: title not attested in candidates/enumerations (coverage 0%) — possible hallucination  ->  1.12 བཅུ་གཉིས་པ་ནི [[69]]
- L23: title not attested in candidates/enumerations (coverage 0%) — possible hallucination  ->  1.13 བཅུ་གསུམ་པ [[71]]
- children of 1: numbered [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 21], expected [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

## Repair round 1 — decision (reasoned inline; no nested subagent dispatched)

**The 12 "possible hallucination" flags are a mechanical false positive, not real defects.**
Root cause: `qc_check_tree.py`'s `_canon()` converts a tree line's `[[N]]` pointer into bare
digits glued onto the title text with no syllable separator (`དང་པོ་ནི [[27]]` → canon
`དང་པོ་ནི27`). For this commentary the node headers are genuinely terse — bare
`ordinal + ནི` with no repeated topic noun (unlike the karma-maitri reference tree, whose
headers repeat `ཕྱག་འཚལ` after every ordinal and so have enough real syllables to absorb
the glued digit under the script's 50% bigram-coverage threshold). With nothing but a single
particle after the ordinal, the glued pointer digit drops coverage to 0% and trips the
hallucination heuristic even though the title is exactly attested.

Verified directly (stripping only the pointer, changing nothing else) that all 12 flagged
titles ARE verbatim present in `0-INBOX/toc-candidates-gendun-gyatso.md`
(`SECTION_TITLE:` fields written in Pass 1, copied unchanged into the tree):
`དང་པོ་ནི`, `གཉིས་པ་ནི`, `གསུམ་པ་ནི`, `བཞི་པ་ནི`, `ལྔ་པ་ནི`, `དྲུག་པ་ནི`, `བདུན་པ་ནི`,
`བརྒྱད་པ་ནི`, `དགུ་པ་ནི`, `བཅུ་པ་ནི`, `བཅུ་གཉིས་པ་ནི`, `བཅུ་གསུམ་པ` — each a `disp_canon in
corpus_canon` exact hit once the pointer suffix is excluded. No title was reworded or
invented; no tree change is warranted for these 12.

(Pointers were kept, rather than dropped to dodge this false positive, because
`qc_tree_vs_source.py`'s pointer-validity and cursor-loss checks — its most load-bearing
checks per its own module docstring — silently no-op on a pointerless tree. Keeping pointers
and documenting this known interaction gives strictly more real verification than removing
them would.)

**The 1 sibling-count gap (children of node 1: 20 expected, 20 present but numbered 1–19,21
skipping 20) is a genuine, source-attested gap**, not a construction error — see
`0-INBOX/toc-tree-qc-gendun-gyatso.md`'s companion note and the fuller explanation originally
recorded here: no candidate or enumeration names a 20th ordinal anywhere in
`1-SOURCES/Commentaries/ཕྱག་འཚལ་སྒྲོལ་མ་ཉེར་གཅིག་མའི་རྣམ་བཤད།.md` (checked lines 85–91, between
the 19th `བཅུ་དགུ་པ` at line 85 and the 21st `ཉེར་གཅིག་ནི` at line 91). Per
`pass4-qc-repair.md`, inserting a node here would mean inventing a Tibetan ordinal neither
the node header nor any enumeration attaches — explicitly forbidden. No node was inserted;
the gap is left visible in the tree (decimals 1.1–1.19, 1.21) for human review.
