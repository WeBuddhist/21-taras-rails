# TOC tree QC report

issues_before: 1
issues_after: 0

## Repair history

Round 1: node `1 དང་པོ་ [[23]]` flagged "title not attested in candidates/enumerations
(coverage 0%) — possible hallucination". The node is genuine (line 23 of the source reads
`...འགྲེལ་བ་ལ། དང་པོ། ཨོཾ་རྗེ་བཙུན་མ་འཕགས་མ་སྒྲོལ་མ་ལ་འཚལ་ལོ། ཞེས་པ་ལ།`) — not a
hallucination, but a bare-ordinal node with zero adjoining topic words, which the
bigram-coverage check cannot score (0% is the checker's floor for empty topic text, not
evidence of invention; see qc_tree_vs_source.py's own explicit "bare-ordinal-only titles"
note for the same case). Resolved by extending the title to include the immediately
following quoted line it introduces — `དང་པོ་ཨོཾ་རྗེ་བཙུན་མ་འཕགས་མ་སྒྲོལ་མ་ལ་འཚལ་ལོ` —
mirroring how every one of the other 22 top-level nodes is titled (ordinal/numeral + the
full first pada of the line it introduces). This is not fabricated text: both words already
sit on the source line adjacent to the ordinal; the correction only widens where the title
snippet is cut. Re-check: 0 issues.

## Issues

- (none)
