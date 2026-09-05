---
name: TOC-to-HEADING
description: Ingest a TOC tree's numbered entries as Markdown headings into a matching raw commentary file, by locating each entry's sa-bcad (outline-announcement) phrase in the prose and inserting a heading directly before it. For TOC trees whose [[N]] pointers are source-PDF page numbers (not commentary line numbers) — use toc-tree-ingest instead when the tree carries resolved line-number pointers into an already-canonical 1-SOURCES/Commentaries/ file.
creator: Tigerboy
---

# TOC-to-HEADING

This skill turns a `toc-tree-*.md` outline into Markdown headings inside a **raw** commentary file (`1-SOURCES/Commentaries/New raw data/`), by reading the commentary and finding, for each TOC entry, the sentence or clause that actually announces that section — the *sa-bcad* — and inserting a heading immediately before it. It exists because some TOC trees carry `[[N]]` pointers that are page numbers from the original scanned source, not line numbers in the markdown file; those pointers cannot be used mechanically (see `toc-tree-ingest`, which does the equivalent job for trees with resolved line-number pointers into an already-canonical file). This skill instead does the matching by reading and understanding the Tibetan prose.

The failure mode this prevents: mis-numbered or missing headings from blindly trusting a `[[N]]` page pointer as a line number, or from inserting a heading at a plausible-looking but wrong spot in the prose (e.g. splitting a sentence badly, or stacking headings in the wrong order).

---

## Inputs

| Field | Description |
|---|---|
| `toc_file` | The finished TOC tree — `2-RAILS/Sections/Raw/toc-tree/<id>.md`. A nested bullet list, each line `N.N.N ... [[page]]`, indentation encoding depth. |
| `commentary_file` | The matching raw commentary — `1-SOURCES/Commentaries/New raw data/bo-<name>.md` (or similar). This file is edited **in place**. |

Confirm both files exist and that the TOC tree's top-level (depth-1) entry matches the commentary's existing `# ` title line — that entry is **excluded** from ingestion (it's already the document's H1). If the human contributor has already hand-ingested the first several TOC entries as a worked example (as often happens — see Procedure Step 1), read that portion of the commentary first to confirm the exact formatting conventions in use before touching the rest of the file.

---

## Output

The same `commentary_file`, updated in place: one Markdown heading line inserted for every TOC entry except the excluded top-level one. No existing prose is deleted, reordered, or retyped — only split at a clause boundary where a heading must be inserted mid-paragraph (see Rule 5).

---

## Output file format

**Heading level = TOC depth**, where depth is the count of dot-separated segments in the entry's number:

| TOC number | Segments | Heading |
|---|---|---|
| `1.1` | 2 | `##` |
| `1.2.1` | 3 | `###` |
| `1.2.2.1` | 4 | `####` |
| `1.2.2.1.1` | 5 | `#####` |
| `1.2.2.1.1.1` | 6 | `######` |
| `1.2.2.1.1.3.1` | 7 | `#######` (literal — Markdown/Obsidian will not render this as a real heading past level 6; ask the human contributor how to handle depth >6 before proceeding if any TOC entry goes that deep, since it's a real design tradeoff, not a mechanical default) |

**Heading text = TOC label, cleaned**: take the entry's text before the trailing `[[page]]` reference, strip a trailing tsheg (`་`) if present, then end the heading with a shad (`།`).

```
དང་པོ་མདོར་བསྟན་པ་ [[24]]   →   ## དང་པོ་མདོར་བསྟན་པ།
ཁྲོ་མོའི་ཚུལ་ལ་ཕྱག་འཚལ་བ་ [[126]]   →   ##### ཁྲོ་མོའི་ཚུལ་ལ་ཕྱག་འཚལ་བ།
```

**Spacing**: every heading is followed by a blank line before whatever comes next — content or another heading. When headings are stacked (see Rule 4), each one is separated from the next by a blank line too:

```
##### ཁྲོ་མོའི་ཚུལ་ལ་ཕྱག་འཚལ་བ།

###### དང་པོ་ཁྲོས་པའི་ཞལ་གྱིས་...བསྟོད་པ།

དེའི་རྗེས་སུ་ཁྲོ་མོའི་ཚུལ་ལ་ཕྱག་འཚལ་བ་...
```

---

## Rules

1. **Exclude the top-level (depth-1) TOC entry.** It already exists as the commentary's `# ` document title — never duplicate it as a heading.
2. **Never guess a location.** Every heading must sit directly before the specific sentence or clause in the commentary that actually announces that section (usually ending in `ནི།`, `ལས།`, `དང་།`/`དང༌།`, or restating the TOC label near-verbatim). If no matching announcement can be found, stop and ask the human contributor rather than placing the heading at an approximate spot.
3. **One heading per standalone paragraph is the simple case.** When a TOC entry's announcement is already its own paragraph (blank line before and after), just insert `heading` + blank line directly before it.
4. **Stack headings when one paragraph announces several nested levels at once.** Tibetan outline prose often states a whole chain of divisions in one sentence (e.g. "...this section has two parts: body and mind; the first, body, has..."; culminating in "...the first is:"). When that happens, insert **all** the applicable headings together, each followed by a blank line, directly before that one paragraph — do not split the paragraph itself.
5. **Split the paragraph when an announcement is buried mid-sentence.** Sometimes a paragraph both closes out the previous section's content *and* opens the next one in a single run-on sentence, with no natural paragraph break. Split it at the clause boundary — commonly right after a `དང་།`/`དང༌།` connector, which this text already uses routinely as a paragraph-final "and, continued below" — and insert `blank / heading / blank` between the two resulting paragraph fragments. Never insert a heading in the middle of an unbroken clause.
6. **Preserve exact whitespace when matching.** Raw OCR/segmentation text frequently mixes regular spaces (U+0020) and non-breaking spaces (U+00A0, `\xa0`) within the same line. Normalize this difference for *matching* purposes only — never let it cause a false "not found." When splitting a paragraph (Rule 5), slice the *original* line text at the matched position, not a re-typed/hardcoded copy, so the exact source bytes are preserved on both sides of the split.
7. **Do not touch anything outside the TOC's scope.** Recap paragraphs, summary verses, or transitional content that has no corresponding TOC entry are left exactly as-is — do not invent a heading for them.
8. **Verify before finishing.** Count headings inserted; it must equal the number of TOC entries minus the excluded top-level one. Read back every insertion point to confirm correct nesting order and blank-line spacing.

---

## Procedure

1. **Read both files in full.** Read `toc_file` to get the complete nested list with depths and page numbers. Read `commentary_file` in full (it will usually exceed one page — read it in successive chunks rather than stopping partway).
2. **Check for a worked example.** If part of the TOC has already been hand-ingested into the commentary (a common way the human contributor demonstrates the exact conventions they want), compare those existing headings against their TOC entries to confirm: the heading-level-by-depth mapping, the label-cleanup rule, and the blank-line convention. Use that as ground truth over this document's general guidance if the two ever disagree.
3. **For each remaining TOC entry, in document order:** search the commentary prose for the clause that announces it (per Rule 2). Common signals: the clause restates the TOC label's wording near-verbatim; it ends in `ནི།` (topic-introducing "as for..."); ordinal markers (`དང་པོ་`, `གཉིས་པ་`, `གསུམ་པ་`...) matching the entry's position among its siblings.
4. **Classify the match** as one of the three cases in Rules 3–5 (standalone paragraph / stacked multi-level paragraph / mid-paragraph split) and record the exact insertion point.
5. **Apply all insertions in one pass**, working from the bottom of the file upward (or by unique-text anchor rather than line number) so that earlier insertions never invalidate the position of insertions still to be made.
6. **Re-read the modified file** and confirm: heading count matches TOC entry count (minus the excluded top-level entry); hashtag counts match each entry's depth; every heading has a blank line above and below it; no prose was lost (a line-count check — new line count should equal old line count plus twice the number of `before`-style insertions, plus a smaller fixed amount per split insertion — is a good sanity check, not a substitute for reading the diff).
7. **Report back** which TOC entries required a paragraph split (Rule 5) or a stacked multi-level insertion (Rule 4), since those are the judgment calls most worth a second look by the human contributor.

---

## Completion check

- [ ] Top-level TOC entry excluded (not duplicated as a heading)
- [ ] Every remaining TOC entry has exactly one corresponding heading in the commentary
- [ ] Heading hash-count matches each entry's TOC depth (segments separated by `.`)
- [ ] Heading text = TOC label with the `[[page]]` reference stripped and the trailing tsheg replaced by a shad
- [ ] Blank line present above and below every heading, including between stacked headings
- [ ] No existing prose deleted, reordered, or retyped — paragraph splits (Rule 5) preserve both resulting fragments verbatim
- [ ] Any TOC depth beyond 6 was confirmed with the human contributor rather than defaulted silently
- [ ] File re-read after edits to confirm correct order and spacing
