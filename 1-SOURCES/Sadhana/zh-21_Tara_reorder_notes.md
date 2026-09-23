# Reorder/resegmentation notes — zh-21_Tara_Chinese_Subtitles_Long_TC+SC.md

Method: aligned every Tibetan line in File B against the same line in File A
(bo-ཟབ་ཏིག་སྒྲོལ་ཆོག.md), using the already-corrected sibling file
`zh-Chinese_Pecha_Text_Only.md` (vs. its `.backup-before-reorder.md`) as a
verified reference for the correct order, since it is line-for-line parallel
to this file's original (broken) order. Reordering was applied to this
file's actual Tibetan + phonetic + Chinese triplets, keeping each triplet
intact.

## What changed
- ~1,780 lines re-sequenced into File A's order. The dominant error pattern
  (confirmed throughout the whole document) was that within almost every
  4-line verse, lines 2 and 3 had been swapped; a smaller number of verses
  had lines 1 and 2 swapped. Both are now corrected.
- One real **segmentation** bug: the opening invocation block ("ན་མོ་གུ་རུ་
  ཨཱརྻཱ་ཏཱ་རཱ་ཡེ...སྐྱབས་སེམས་ནི།", near the start of "Chapter 1") had 7
  separate lines from File A (^1-1 through ^1-4) merged into a single
  Tibetan+Chinese pair. This has been split back into 7 lines, each paired
  with its own segment of the original Chinese translation (segmented at
  the natural comma/period boundaries — text itself was not altered).
- The table-of-contents block at the very top (10 entries, "དཀར་ཆག") has no
  counterpart in File A and was left untouched at the top, since it's front
  matter, not part of the liturgy's sequential order.
- A handful of one-off annotations with no File A counterpart (translator
  credits "མཁན་པོ་འགྱུར་མེད་རྡོ་རྗེ་ནས་བསྒྱུར", "ཚར་གསུམ" = recite 3 times) were
  kept, repositioned next to the passage they apparently annotate.

## Flagged for your own review (placed by best-effort proximity, not a confirmed File A match)
These 3 lines could not be pinned to an exact position with confidence,
because they are short, repeating phrases (translator credits / a mantra
fragment) with no unique anchor in File A. Content was preserved; only their
exact position is a best guess:
1. "མཁན་པོ་འགྱུར་མེད་རྡོ་རྗེ་ནས་བསྒྱུར" / "堪布久美多吉翻譯。" — a translator
   credit line, placed near line ~385 in the new file.
2. "ཙིཏྟཾ་ཤྲཱི་ཡཿ ཀུ་རུ་ཧཱུྂ།" (heart-mantra installation fragment) — placed
   near line ~738.
3. "མཁན་པོ་འགྱུར་་མེད་རྡོ་རྗེ་ནས་བསྒྱུར" / "由堪布久美多吉翻譯。" — another
   translator credit, placed near line ~739.

## Verification performed
- Every Tibetan+phonetic+Chinese triplet in the original file is preserved
  exactly once in the new file (checked by exact multiset comparison of all
  lines) — nothing was dropped or duplicated, aside from the one intentional
  7-way split described above.
- ~99% of lines were matched to File A with a unique or tightly-local text
  match (high confidence). The opening-invocation resegmentation above was
  verified by hand against File A line-by-line.
