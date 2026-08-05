# TOC tree vs. source QC report

issues_before: 1
issues_after: 1 (human-reviewed, accepted — see note)

## Issues

- 2 གཉིས་པ་དེའི་ཕན་ཡོན: title attested in the source but not near pointer [[95]] (found near line 27) — possible cursor loss

## Notes (not counted as issues)

- (info) 1 node(s) have bare-ordinal-only titles (e.g. "དང་པོ་") with no distinguishing text — title attestation skipped for these, not counted as clean or as an issue

## Repair round 1 — decision (reasoned inline; no nested subagent dispatched)

Not a cursor-loss bug. Node 2's title `གཉིས་པ་དེའི་ཕན་ཡོན` was deliberately assembled from two
places in the source per pass3-tree.md's matching rule ("use the node header's ORDINAL
together with the fuzzy name to align it to the right part... prefer the node header's
wording, do NOT create a duplicate sibling"):

- the topic noun `དེའི་ཕན་ཡོན` ("its benefits") is declared once, up front, in the top-level
  announcement at source line 27 (`འདི་ལ་གཉིས། བསྟོད་པ་དངོས་དང་། དེའི་ཕན་ཡོན་བཤདཔའོ།`) — this
  is item 2 of the work's own two-part division;
- the section itself does not reopen with that noun repeated — it reopens with a bare
  `གཉིས་པ་ནི` at line 95, exactly the same terse ordinal-only style as every one of the 21
  homage headers in node 1's branch.

Pointer `[[95]]` is correct: it marks where the benefits section actually begins in the
document (verified: `1.19 བཅུ་དགུ་པ [[85]]` → `1.21 ཉེར་གཅིག་ནི [[91]]` → `2 ... [[95]]` is
strictly increasing, consistent with document order, no collision). Repointing to line 27
(where the topic noun textually lives) would place node 2 BEFORE node 1's own children,
breaking monotonicity for a false gain. Re-titling node 2 to the bare `གཉིས་པ་ནི` (matching
1.1–1.19's style exactly) would silence the flag but throw away the one piece of information
that says what part 2 actually is. Kept both the descriptive title and the correct pointer;
this flag is the checker's documented and expected behavior for a topic named once early and
reopened later under a bare ordinal — the same pattern pass3-tree.md's worked example
explicitly instructs matching, not an extraction defect.
