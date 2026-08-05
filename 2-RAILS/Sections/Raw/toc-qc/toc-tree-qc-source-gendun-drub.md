# TOC tree vs. source QC report

issues: 5

## Issues

- 2 གཉིས་པ་དངོས་བཤད་པ: title attested in the source but not near pointer [[28]] (found near line 24) — possible cursor loss
- 2.2.2 གཉིས་པ་རྒྱས་པར་བཤད་པ: title attested in the source but not near pointer [[44]] (found near line 34) — possible cursor loss
- 2.2.3 གསུམ་པ་ཕན་ཡོན་བསྟན་པ: title attested in the source but not near pointer [[228]] (found near line 34) — possible cursor loss
- pointer [[28]] is shared by 3 nodes (2, 2.1, 2.2) — repeated-pointer collision, the extractor likely lost its cursor partway through this run
- pointer [[52]] is shared by 4 nodes (2.2.2.2, 2.2.2.2.1, 2.2.2.2.1.1, 2.2.2.2.1.1.1) — repeated-pointer collision, the extractor likely lost its cursor partway through this run

## Notes (not counted as issues)

- (none)

## Human review — all 5 remaining issues checked against the source and accepted as genuine, not extraction error

The commentary's own outlining style repeatedly **fuses** an ordinal node-header with the
announcement of that same node's own sub-division, on one physical (resegmented) line —
so a node opened this way carries no topic words of its own at its pointer; its
descriptive name can only be recovered from the parent enumeration a few lines earlier.
That is exactly what `qc_tree_vs_source.py`'s own module docstring calls out as a
plausible non-error ("a same-line collision across nested levels is often legitimate, not
wrong"), extended here to the sibling case of a *combined* title whose topic half is
attested a few lines before its pointer rather than at it.

1. **`2 གཉིས་པ་དངོས་བཤད་པ` (pointer [[28]], topic found near line 24)** — line 24 is the
   top-level enumeration itself ("འདི་ལ་གཉིས། གླེང་གཞི་དང་། དངོས་བཤད་པའོ། །", i.e. "this
   has two: the setting, and the actual teaching"). Its second part, དངོས་བཤད་པ, is never
   reopened with its own topic words — line 28 ("གཉིས་པ་ལ། རྩ་བའི་སྔགས་...") is a bare
   `གཉིས་པ་ལ` that immediately cascades into announcing *its own* two children (the
   root-mantra praise and the twenty-one homages) rather than restating "དངོས་བཤད་པ".
   Per `pass3-tree.md`'s matching rule ("keep the node header's ordinal... keep the full
   descriptive topic phrase otherwise"), the enumeration's topic word is combined with the
   node header's ordinal into one title, pointed at the node's own opening line (28) rather
   than the enumeration (24) — the more useful anchor for a reader, at the cost of this
   flag.
2. **`2.2.2 གཉིས་པ་རྒྱས་པར་བཤད་པ` (pointer [[44]], topic found near line 34)** — identical
   pattern: རྒྱས་པར་བཤད་པ ("the elaboration") is named in the three-part enumeration at
   line 34 ("མདོར་བསྟན་པ་རྒྱས་པར་བཤད་པ། ཕན་ཡོན་བསྟན་པ་དང་གསུམ།"); its own node header at
   line 44 is a bare `གཉིས་པ་ལ` that cascades straight into its own three-part
   sub-announcement (history-praise / body-praise / activity-praise).
3. **`2.2.3 གསུམ་པ་ཕན་ཡོན་བསྟན་པ` (pointer [[228]], topic found near line 34)** — same
   pattern again: ཕན་ཡོན་བསྟན་པ ("teaching the benefits") is the third part of that same
   line-34 enumeration, not reopened by name until its own four-part sub-announcement at
   line 228 ("གསུམ་པ་ལ་ཕན་ཡོན་བསམ་པའི་ཁྱད་པར...བཞི།").
4. **pointer [[28]] shared by 3 nodes (2 → 2.1 → 2.2)** — a parent → first-child →
   second-item chain opening on one physical line. Verified verbatim at line 28: "གཉིས་པ་
   ལ། རྩ་བའི་སྔགས་ཀྱིས་བསྟོད་པ་འདི་དང་། །ཕྱག་འཚལ་བ་ནི་ཉི་ཤུ་རྩ་གཅིག ཅེས་གཉིས་སུ་ཕྱེ་བའི།" —
   node 2 opens, its first child 2.1 (root-mantra praise) opens in the same breath, and its
   second child 2.2 (the twenty-one homages) is named in the same sentence's closing
   division clause. No intervening explanatory prose separates any of the three.
5. **pointer [[52]] shared by 4 nodes (2.2.2.2 → 2.2.2.2.1 → 2.2.2.2.1.1 → 2.2.2.2.1.1.1)**
   — a direct four-generation parent → first-child → first-grandchild →
   first-great-grandchild chain, confirmed verbatim at line 52 of the source: "གཉིས་པ་ལ།
   ལོངས་སྐུའི་...བསྟོད་པ་གཉིས། དང་པོ་ལ། ཞི་བའི་...བསྟོད་པ་གཉིས། དང་པོ་ལ། ཕྱག་འཚལ་དྲུག་
   ཡོད་པའི། དང་པོ་ཞལ་མདངས་གསལ་...ནི།" — four cascading announcements with no
   explanatory prose between any of them, on the single densest paragraph of the
   commentary's front matter (the body-praise → peaceful-aspect → six-verse-group →
   first-verse chain). This is the "extended... down one uninterrupted chain of
   first-children" case, not the cursor-loss signature of collisions across *different*,
   unrelated titled subsections.
