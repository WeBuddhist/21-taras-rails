---
name: Transclude-Rootexto-Commentary
description: Insert a transclusion of each root-text verse immediately before the sa-bcad statement that introduces that verse, in a commentary that also quotes the verse verbatim before commenting on it. Use when the commentary already reproduces the root verse's wording as its own block (a "quote-then-explain" commentary style), as opposed to a commentary that only announces a verse via a sa-bcad structural heading without quoting it (see `transclusion` and `Transclusion-rootext-into-commentaries` for that case).
creator: Tigerboy
---

# Transclude-Rootexto-Commentary

This skill embeds `![[root-text#^id]]` transclusion links directly above the sa-bcad — the prose line that announces an outline point (e.g. "དང་པོ་ནི།", "...བསྟོད་པར་མཛད་པ་ནི།", always ending in ནི།) — that precedes each point in a commentary where a root-text verse is quoted verbatim (or near-verbatim) before being explained. It exists because many commentaries in this vault reproduce each verse's own wording inline — often with minor orthographic variants from the root's critical edition — rather than only naming the verse via a sa-bcad heading; readers should see the canonical root text pulled in before the commentary starts announcing and discussing it, not several lines down at the point where the commentary's own quotation happens to repeat the wording. The failure modes this skill prevents: transcluding at the wrong position (immediately above the quotation itself, after the sa-bcad, rather than before the sa-bcad that introduces it), re-embedding the same verse repeatedly when a commentary discusses it line-by-line in several separate places, and missing a match because the commentary's wording differs slightly from the root's.

---

## Inputs

- `root-text-file` — full vault-relative path to a root text or translation under `1-SOURCES/Text/` or `1-SOURCES/Translations/`, with `verse_id_format: chapter-verse` in its frontmatter and every verse already carrying a `^chapter-verse` (or `^letter-verse`, for appendix-style sections such as a benefits/phan-yon block) Obsidian block ID.
- `commentary-file` — one commentary file, typically under `1-SOURCES/Commentaries/`, that quotes root verses inline as part of its own text (in whole stanzas, or split line-by-line across several points). If the commentary only references verses through sa-bcad headings and never quotes their wording, this skill does not apply — use `transclusion` instead.

If either file is missing required block IDs, stop and report which IDs are missing rather than guessing a position.

## Output

The same `commentary-file`, modified in place: a transclusion line plus one blank line inserted directly above the sa-bcad paragraph (or paragraphs) leading into every matched verse-quotation block, or directly above the quotation itself when no sa-bcad paragraph precedes it. No existing line is deleted, reordered, or reworded. Total line count increases by exactly two for each verse transcluded.

---

## Output file format

Given a root text with:

```
ཕྱག་འཚལ་སྒྲོལ་མ་མྱུར་མ་དཔའ་མོ། །
སྤྱན་ནི་སྐད་ཅིག་གློག་དང་འདྲ་མ། །
འཇིག་རྟེན་གསུམ་མགོན་ཆུ་སྐྱེས་ཞལ་གྱི། །
གེ་སར་ཕྱེ་བ་ལས་ནི་བྱུང་མ། ། ^1-1
```

and a commentary passage that quotes it (note the orthographic variant, བྱེ་བ vs ཕྱེ་བ, which is tolerated):

```
དང་པོ་ནི།

ཕྱག་འཚལ་སྒྲོལ་མ་མྱུར་མ་དཔའ་མོ། །
སྤྱན་ནི་སྐད་ཅིག་གློག་དང་འདྲ་མ། །
འཇིག་རྟེན་གསུམ་མགོན་ཆུ་སྐྱེས་ཞལ་གྱི། །
གེ་སར་བྱེ་བ་ལས་ནི་བྱུང་མ། ། ^2-2

ཞེས་པ་སྟེ། ...
```

the output is:

```
![[1-SOURCES/Text/<root-text-file>.md#^1-1]]

དང་པོ་ནི།

ཕྱག་འཚལ་སྒྲོལ་མ་མྱུར་མ་དཔའ་མོ། །
སྤྱན་ནི་སྐད་ཅིག་གློག་དང་འདྲ་མ། །
འཇིག་རྟེན་གསུམ་མགོན་ཆུ་སྐྱེས་ཞལ་གྱི། །
གེ་སར་བྱེ་བ་ལས་ནི་བྱུང་མ། ། ^2-2

ཞེས་པ་སྟེ། ...
```

The transclusion moved ahead of the sa-bcad line ("དང་པོ་ནི།"), which stays exactly as worded, right where it was, just now below the embed instead of above it. The commentary's own quotation and block ID are untouched, and nothing after the quotation is touched.

### When the sa-bcad is more than one paragraph deep

Some outline points accumulate more than one ནི।-ending sentence before the quotation — e.g. a heading-level remark plus its own sub-point's announcement. Only the paragraphs that themselves end in ནི། (immediately before their block ID) count as "the sa-bcad" to jump; an ordinary explanatory paragraph that happens to sit between the heading and the sa-bcad, but ends some other way (དང་།, ཅིང་།, ལའོ།, etc.), is left exactly where it is:

```
###### གསུམ་པ་... ^0-2-2-1-1-3
####### དང་པོ་... ^0-2-2-1-1-3-1

[general remark, ends ...ལའོ། ། — does NOT end in ནི།, stays in place]

![[root-text.md#^1-4]]

[the actual sa-bcad, ends ...ཚུལ་ནི། — this is what the transclusion jumped]

ཕྱག་འཚལ་དེ་བཞིན་གཤེགས་པའི་གཙུག་ཏོར། །  ^2-16
```

The transclusion also always lands after any markdown heading(s) (##, ###, …) — those are structural navigation, not part of the sa-bcad, and are never displaced.

---

## Rules

1. **Full vault-relative paths only.** Every transclusion link uses the full path from the vault root with the `.md` extension, e.g. `![[1-SOURCES/Text/སྒྲོལ་མ་ཉེར་གཅིག་གི་བསྟོད་པ།.md#^1-1]]` — never a bare note name or short wiki-link, per the vault-wide convention in `transclusion` Rule 2.
2. **Match by content, tolerant of orthographic variants.** A commentary's quotation rarely matches the root byte-for-byte (tsheg/vowel-length spelling, an alternate reading in the commentary's source witness). Match on substantive overlap — the same padas in the same order, allowing for known variant classes (e.g. ཏུཏྟཱ་ར/ཏུ་ཏྟྭ་ར, ཧཱུཾ/ཧཱུྃ, a synonym substitution) — not exact string equality. If a passage cannot be confidently matched to one specific verse (a paraphrase, or overlap ambiguous between two adjacent verses), stop and report it rather than guessing.
3. **One embed per verse, at its first occurrence.** When a commentary explains a verse line-by-line and quotes it in several separate, non-adjacent places (a pada at a time), insert the transclusion of the *complete* verse only above the sa-bcad leading into the *first* of those quotation points. Do not re-embed the same full verse at each subsequent partial quotation — that clutters the file with repeated, partially-spoiling embeds.
4. **Placement is immediately above the sa-bcad, not immediately above the quotation.** Starting from the quotation paragraph, walk backward through any immediately preceding paragraph(s) that are themselves sa-bcad / outline-announcement prose — recognizable because the paragraph, stripped of its trailing block-ID, ends in ནི། (e.g. "དང་པོ་ནི།", "...བསྟོད་པར་མཛད་པ་ནི།"). Keep walking back through a run of consecutive ནི།-ending paragraphs, but stop as soon as you hit a paragraph that does not end in ནི། (ordinary continuing commentary, e.g. ending in དང་།, ཅིང་།, ལའོ། ), a markdown heading, or another transclusion. Insert directly before the topmost paragraph in that ནི།-ending run. If no ནི།-ending paragraph precedes the quotation at all, insert directly above the quotation itself, exactly as before.
5. **Exactly one blank line between the transclusion and the paragraph now immediately following it** (the topmost sa-bcad paragraph, if the verse has one; otherwise the quotation itself), and the transclusion is preceded by whatever spacing already separated the prior content from that paragraph (do not add a second blank line if one already exists there).
6. **Never duplicate an existing transclusion.** Before inserting, check whether a transclusion of that same root block ID already sits at the correct insertion point identified by Rule 4. If so, skip it and note the skip in the report.
7. **Never modify existing content.** No line of the commentary's own quotation, its sa-bcad wording, its block ID, its explanatory prose, or any heading is deleted, reordered, or reworded. Insertions only — the sa-bcad and quotation keep their exact wording and relative order to each other, they just both move below the newly inserted embed.
8. **Preserve existing block IDs as-is.** Do not renumber, move, or re-anchor any `^...` id already present in the commentary.
9. **Report after writing.** For every insertion: the commentary file, the root block ID transcluded, and the first few words of the sa-bcad (or, if none, the quotation) it was placed above. For every skip (rule 3 split-verse continuations, or rule 6 duplicates): note it and why.

---

## Procedure

1. Read `root-text-file`'s frontmatter. Confirm `verse_id_format: chapter-verse` (or equivalent) is present. Extract every block ID and its verse text into a map `{block_id → verse_text}`, including any appendix-style section (e.g. `^a-1`...`^a-N` for a benefits/phan-yon block, `^I-1`...`^I-N` for a front-matter homage) in addition to the main `^chapter-verse` sequence.
2. Read `commentary-file` in full, and split it into paragraphs (blocks of lines set off by blank lines), keeping track of each paragraph's line range and whether it is a markdown heading (starts with `#`), a transclusion (starts with `![[`), or plain prose/verse text.
3. Scan the paragraphs for every one that quotes root-verse wording: it opens with a verse's characteristic opening words and consists of one to four pada lines ending in `།` / `། །` punctuation. For each such paragraph, match it against the map from step 1 using Rule 2 (content match, variant-tolerant). Record the paragraph's index and the matched `block_id`.
4. Group matches by `block_id`. Where a `block_id` has more than one matched paragraph (a split, line-by-line quotation), keep only the earliest (first in document order) as the insertion anchor for that verse; discard the rest per Rule 3.
5. For each insertion anchor, apply Rule 4: walk backward from the quotation paragraph through consecutive non-heading, non-transclusion paragraphs whose text (stripped of its trailing block-ID) ends in ནི།. The insertion point is immediately before the topmost paragraph reached this way, or immediately above the quotation itself if the paragraph directly before it does not end in ནི། (or is a heading, or is the start of the file).
6. At each insertion point, check Rule 6: does a transclusion of that exact `block_id` already sit there? If yes, drop it from the insertion list and record the skip.
7. Sort the remaining insertion points in descending order of line position (bottom of file first) so earlier insertions do not shift the line numbers of later ones.
8. For each insertion point, in that order, insert two lines: `![[<root-text-file, full vault-relative path>#^<block_id>]]`, then a blank line. Everything that was already at and after the insertion point (the sa-bcad run, then the quotation, then the rest of the file) shifts down unchanged.
9. Write the modified `commentary-file`.
10. Report every insertion made (per Rule 9) and every skip (split-continuation or duplicate).

---

## Completion check

- [ ] Both files confirmed to carry the required block IDs before any write; missing IDs reported and execution stopped rather than guessed
- [ ] Every inserted transclusion link uses the full vault-relative path with `.md` extension
- [ ] Every matched quotation verified against the root by content, not exact string equality, with variant spellings tolerated
- [ ] Every transclusion lands before the full run of ནི།-ending sa-bcad paragraphs leading into its quotation (or immediately above the quotation when no sa-bcad precedes it) — never merely above the quotation itself when a sa-bcad exists
- [ ] Markdown headings and any non-ནི།-ending explanatory paragraph between a heading and its sa-bcad were left in place, not displaced by the transclusion
- [ ] No verse re-embedded more than once when its quotation is split across multiple points in the commentary — only the first occurrence carries the transclusion
- [ ] No existing transclusion duplicated at any insertion point
- [ ] No existing line deleted, reordered, or reworded; only insertions made
- [ ] Exactly one blank line separates each transclusion from the paragraph beneath it
- [ ] Any passage that could not be confidently matched to a single verse was reported to the human rather than guessed
- [ ] Post-write report produced listing every verse inserted and every skip, with reasons
