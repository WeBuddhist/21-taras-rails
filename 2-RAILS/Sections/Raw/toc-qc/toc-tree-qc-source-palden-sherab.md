# TOC tree vs. source QC report

issues: 1

## Issues

- 3.1 'དང་པོ་': announcing text names a 4-way division but the tree gives it 22 child(ren) — verify by hand which is right

## Notes (not counted as issues)

- (info) 8 node(s) have bare-ordinal-only titles (e.g. "དང་པོ་") with no distinguishing text — title attestation skipped for these, not counted as clean or as an issue

## Human note — the one issue above is a reviewed, accepted heuristic flag

Node `3.1` ("དང་པོ་", verse-by-verse praise) is genuinely divided into 22 children (the
21 homage verses plus one closing summary node, `3.1.22`). The checker's sibling-count
heuristic (check 4) picked up the phrase "དང་པོ་ལ་བཞི་སྟེ..." at `3.1`'s own anchor line
and read it as `3.1`'s own declared child-count — but that 4-way phrase actually announces
a *different*, recurring division: the four aspects (ཚིག་གི་དོན / སྤྱིའི་དོན / སྦས་དོན /
མཐར་ཐུག་གི་དོན) that every one of the 21 verses is separately expounded through, not a
4-way split of `3.1` itself. This is exactly the class of flag the script's own docstring
calls out as "a prompt for human review, not a proof of error" (check 4's description) —
reviewed and accepted, not corrected.
