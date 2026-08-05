# TOC tree QC report

issues: 1

## Issues

- L13: title not attested in candidates/enumerations (coverage 0%) — possible hallucination  ->  1.3 གསུམ་པ་ [[29]]

## Human note on the remaining issue (not auto-repaired)

Root-caused, not a tree defect: `_TREE_LINE_RE` in `qc_check_tree.py` strips the
legacy `^toc-N-N` block-ID suffix but was never updated for this vault's actual
`[[N]]` line-pointer convention (confirmed against the promoted
`2-RAILS/Sections/Raw/toc-tree/karma-maitri.md`, which also uses `[[N]]`). For a
bare-ordinal leaf (`དང་པོ་`, `གཉིས་པ་`, `གསུམ་པ་` with no topic words — three such
leaves exist here: 1.1/1.2/1.3), the pointer digits leak into the fuzzy
syllable-coverage fallback as if they were title text. Direct inspection (`_canon`/
`_title_bigram_coverage` called by hand) showed 1.1's and 1.2's "attestation" was
itself a coincidental digit match (`25`, `27` happened to also appear as unrelated
pada-numbers elsewhere in the corpus text) — not a real pass — while 1.3's `29`
did not coincidentally appear anywhere, so it alone was flagged. Renaming these
three leaves to carry real topic text (`དང་པོ་གང་གིས་སྒྲོལ་བ` etc., drawn from
Enumeration Block 2) makes this checker pass cleanly but was reverted: it then
fails `qc_tree_vs_source.py` (title attested only near the parent's announcement
at line 23, not near the leaf's own line 27/29 — a genuine "cursor loss" shape),
because the node headers at lines 25/27/29 in the source are truly bare ("1 དང་པོ་
ནི།" / "1 གཉིས་པ་ནི།" / "1 གསུམ་པ་ནི།" — no topic words at that point in the text).
Bare-ordinal titles are the correct, source-faithful choice; `qc_tree_vs_source.py`
already special-cases them ("title attestation skipped for these, not counted as
clean or as an issue" — see its own report). Left as one known,
tool-artifact issue rather than force a change that would make the tree less
faithful to the source. A human contributor could fix `_TREE_LINE_RE` to also
strip `\[\[\d+\]\]`/`\[\[\?\]\]`, which would make this issue disappear without any
change to the tree itself.
