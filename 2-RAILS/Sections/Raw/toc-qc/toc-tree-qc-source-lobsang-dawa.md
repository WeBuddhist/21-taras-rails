# TOC tree vs. source QC report

issues: 2

## Issues

- 1.2.2.1.2.2 ཕྱག་མཚན་གྱི་སྒོ་ནས་བསྟོད་པ: title attested in the source but not near pointer [[48]] (found near line 44) — possible cursor loss
- pointer [[30]] is shared by 4 nodes (1.2.2, 1.2.2.1, 1.2.2.1.1, 1.2.2.1.1.1) — repeated-pointer collision, the extractor likely lost its cursor partway through this run

## Notes (not counted as issues)

- (info) 15 node(s) have bare-ordinal-only titles (e.g. "དང་པོ་") with no distinguishing text — title attestation skipped for these, not counted as clean or as an issue

## Human review — both remaining issues checked against the source and accepted as genuine, not extraction error

1. **1.2.2.1.2.2 (pointer [[48]])** — this is the tree's one gap-filled node: the source's
   own khro-mo (wrathful-aspect) 7-part enumeration at line 44 names a 2nd part
   ("ཕྱག་མཚན་གྱི་སྒོ་ནས་བསྟོད་པ", hand-implement/mudrā aspect) that is never reopened
   with its own ordinal-led header — the commentary jumps straight from item "19" to item
   "21" at line 48 with no "གཉིས་པ་ནི།" marker (verified directly against
   `1-SOURCES/Commentaries/…མཆན་འགྲེལ་བཞུགས་སོ།.md` lines 46–48; the numbering itself
   skips "20"). Per `toc-tree-extraction/prompts/pass3-tree.md`'s gap-filling rule, the
   node is inserted using the enumeration's own part text, un-ordinalled (the source gives
   it no ordinal to preserve). Its pointer is placed at line 48 — where the sub-point's
   actual content (mudrā/hand-gesture imagery) begins — rather than at line 44 (the
   enumeration), which is the more useful anchor for a reader even though the enumeration
   is where the title string itself is verbatim attested. This is a genuine structural gap
   in the source's own numbering, not a tree-building error.
2. **pointer [[30]] shared by 4 nodes (1.2.2 → 1.2.2.1 → 1.2.2.1.1 → 1.2.2.1.1.1)** — a
   direct four-generation parent → first-child → first-grandchild → first-great-grandchild
   chain. The source cascades all four announcements back-to-back with no intervening
   explanatory prose on one physical (resegmented) line — confirmed verbatim at line 30 of
   the source: "གཉིས་པ་ལ་གཉིས། … དང་པོ་ལ་གཉིས། … དང་པོ་ལ་དྲུག … དང་པོ་ནི།". This is exactly
   the "parent and its first child sharing one line is normal" case the checker's own
   module docstring names as legitimate, extended down one uninterrupted chain of
   first-children rather than across unrelated siblings — not the cursor-loss signature
   (repeated collisions across *different* titled subsections) the check is designed to
   catch.
