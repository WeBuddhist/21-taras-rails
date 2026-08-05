# TOC tree vs. source QC report

issues_before: 1
issues_after: 1 (human-reviewed, accepted — see note)

## Issues

- pointer [[45]] is shared by 4 nodes (1.2.2, 1.2.2.1, 1.2.2.1.1, 1.2.2.1.1.1) — repeated-pointer collision, the extractor likely lost its cursor partway through this run

## Notes (not counted as issues)

- (none)

## Repair round 1 — decision (reasoned inline; no nested subagent dispatched)

Not a cursor-loss bug. This is a direct four-generation parent → first-child →
first-grandchild → first-great-grandchild chain (1.2.2 → 1.2.2.1 → 1.2.2.1.1 → 1.2.2.1.1.1),
exactly the same pattern already reviewed and accepted for this vault's `lobsang-dawa` tree
(see `0-INBOX/toc-tree-qc-source-lobsang-dawa.md`, pointer [[30]] shared by the same four-deep
chain shape).

Verified directly against the resegmented source
(`1-SOURCES/Commentaries/ཕྱག་འཚལ་ཉེར་གཅིག་གི་ཕན་ཡོན་དང་བཅས་པ་གསལ་བའི་མེ་ལོང...md`, line 45):
the author cascades four nested sa-bcad announcements back-to-back with no intervening
explanatory prose — "གཉིས་པ་སྐུའི་རྣམ་པའི་སྒོ་ནས་ཕྱག་འཚལ་བ་ལ། ལོངས་སྐུའི་རྣམ་པ་དང་། ཆོས་སྐུའི་
རྣམ་པའི་སྒོ་ནས་ཕྱག་འཚལ་བ་གཉིས། དང་པོ་ལོངས་སྐུའི་རྣམ་པའི་སྒོ་ནས་ཕྱག་འཚལ་བ་ལའང་ཞི་བའི་རྣམ་པ་
དང་།ཁྲོ་བོའི་རྣམ་པའི་སྒོ་ནས་ཕྱག་འཚལ་བ་གཉིས་ལས། དང་པོ་ཞི་བའི་རྣམ་པའི་སྒོ་ནས་ཕྱག་འཚལ་བ་ལ།
ཕྱག་འཚལ་དྲུག་གི་སྒོ་ནས་བསྟོད་པར་མཛད་པ་ལ།དང་པོ་ཞལ་མདངས་གསལ་ཞིང་འོད་ཟེར་འཕྲོ་བའི་སྒོ་ནས་
བསྟོད་པར་མཛད་པ་ནི།" — one continuous physical line (this exact grouping, with the blank-line
paragraph boundaries left untouched around it, was a deliberate decision made in the
`commentary-resegment` pass: these four announcements are already adjacent in the pre-resegment
source with no dividing prose, so joining them onto one paragraph line changed only whitespace,
never text). All four nodes' pointers correctly point at the one line where each of their
announcing clauses actually lives — repointing any of them elsewhere would misrepresent the
source. This is exactly the "division and its first branch routinely open on the same sa-bcad
sentence" case the checker's own module docstring names as legitimate, chained down one
uninterrupted first-child lineage rather than scattered across unrelated siblings — not the
cursor-loss signature (the same value recurring across *different*, unrelated titled
subsections) the check exists to catch.
