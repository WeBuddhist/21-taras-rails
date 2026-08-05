# TOC tree vs. source QC report

issues: 2

## Issues

- 1.3 ཕན་ཡོན་བསྟན་པ: title attested in the source but not near pointer [[207]] (found near line 25) — possible cursor loss
- pointer [[43]] is shared by 4 nodes (1.2.2, 1.2.2.1, 1.2.2.1.1, 1.2.2.1.1.1) — repeated-pointer collision, the extractor likely lost its cursor partway through this run

## Human review of the 2 flagged issues (both accepted as legitimate, not repaired)

- **1.3 ཕན་ཡོན་བསྟན་པ / pointer [[207]]**: this node is a genuine FILL-GAP case per
  toc-tree-extraction's pass3 rule ("Every part of a genuine sa-bcad division MUST
  appear as a child node... insert it using the part's title text"). The top-level
  announcement at line 25 declares 3 parts (མདོར་བསྟན་པ / རྒྱས་པར་བཤད་པ / ཕན་ཡོན་
  བསྟན་པ), but the source never opens the 3rd part with its own ordinal-led header
  — verified by exhaustive read of the whole commentary body. Line 207 is where the
  benefit-of-recitation content that fulfils this promised 3rd part actually begins
  (verified by reading the surrounding prose: "she who together with the buddhas'
  emanations swiftly bestows blessing... one attains an excellent state... and
  ultimately reaches buddhahood" — a textbook ཕན་ཡོན་/benefit passage). The checker
  finds the LABEL text only at line 25 (where it was announced, not where its
  content lives) because no verbatim occurrence of the phrase exists at line 207 —
  expected for a filled gap, not a cursor-loss error.
- **pointer [[43]] shared by 4 nodes (1.2.2, 1.2.2.1, 1.2.2.1.1, 1.2.2.1.1.1)**:
  verified against the source — line 43 is a single unbroken sentence that
  genuinely cascades four consecutive sa-bcad divisions with no intervening prose:
  "གཉིས་པ་སྐུའི་...ལ་གཉིས...(→1.2.2)...དང་པོ་ལ་གཉིས...(→1.2.2.1)...དང་པོ་ལ་དྲུག
  ...(→1.2.2.1.1)...དང་པོ་ནི།(→1.2.2.1.1.1)". This is the same fused-announcement
  pattern already attested as legitimate in this vault's sibling tree
  `2-RAILS/Sections/Raw/toc-tree/tenga-tulku.md` (e.g. its 1.2.2.1.1 and
  1.2.2.1.1.1 also share one pointer). Not a repair candidate — breaking the four
  nodes onto four different lines would misrepresent a real feature of the source.
