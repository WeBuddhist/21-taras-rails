# Parser — Root Text

Takes a source file and its linter output and writes the API payloads for the text, edition, table of contents and (for translations and commentaries) alignment.

Run `linter-root-text` first.

## What it does

1. **extract_text_input** — takes `text_input` from the lint JSON (or `resolved` from a `.lint.errors.json`), drops empty fields and contributors without an id, writes `text.json`
2. **build_edition** — builds the edition content and its segments with character spans from the body text (headings left out), writes `edition.json`
3. **build_toc** — builds a nested table of contents from the headings (headings are used only here), writes `toc.json`
4. **build_alignment** — for `file_type` `translation` or `commentary` only, links segments to the root text through transclusions, writes `alignment.json`

## Output

```
output/
  <stem>/                  # one folder per source file, named after it
    <stem>.text.json        # text_input payload
    <stem>.edition.json     # edition metadata, content and segments
    <stem>.toc.json         # nested TOC with character spans
    <stem>.alignment.json   # translation/commentary → root-text alignments
```

## Edition

- `metadata.type` comes from `edition_type` (default `critical`); `metadata.source` from `source` or `source_url`
- **Headings are not part of the edition.** They add no segment and no text to `content`; they are used only for the table of contents
- Blocks are separated by blank lines. Each content block becomes one segment, with one span per line, and its block ID (without `^`) as `reference`
- The block ID is removed from the text; lines are joined with no separator
- Blocks without a block ID are skipped with a warning (headings too); so are content blocks whose ID has more than 3 parts
- Inline formatting for interlinear glosses (`<small>…</small>`) is dropped from `content`: the gloss text stays, the tags do not. The source file is never changed.
- Non-breaking spaces (U+00A0) become ordinary spaces in `content`.
- Transclusion lines (`![[...#^ref]]`) are left out of the content

### Segment types

The shape of the block is checked first, then its ID:

| Test | Type | Example |
|------|------|---------|
| **Two or more lines with no empty line between them** | `verse` | a quoted verse, one line per unit |
| ID starts with `T` or `t` | `top_segment` | `^T-1` |
| Any part is an uppercase Roman numeral | `front_matter` | `^I-1`, `^2-I-3` |
| Any part is lowercase letters only | `back_matter` | `^a-1` |
| Anything else | the document default | `^1-1`, `^1-2x3`, `^1-U4` |

**Verse wins over the ID.** A verse in the front matter or the colophon is `verse`, not `front_matter` or `back_matter`: those mark where a block sits, and the block's shape says what it is. The ID types only blocks that are not verse.

The document default is `verse`. It is `paragraph` when the file has `commentary_of`, or is a translation whose `root_text` is a commentary.

An empty line inside a block — including a line holding only an invisible character such as a zero-width space — stops it being verse, and the parser warns about it. Such a block is usually two paragraphs that each need their own block ID, and Obsidian shows no gap there, so the warning is the only sign.

A block of prose that was hard-wrapped onto several lines without a blank line between them reads as verse to this rule. Keep a paragraph on one line.

## Table of contents

- Built from the headings; the heading level (`#` count) sets the nesting
- Spans are character offsets into the edition `content`, which has no heading text. A section starts where the text after its heading starts, and ends where the next heading at the same or a higher level starts (or at the end of the content)
- A heading with no text before the next heading gets an empty span (`start` = `end`)
- Titles are keyed by `lang_tag` (default `en`); Tibetan titles in Wylie are converted to Unicode

## Alignment

Transclusions (`![[<root file>#^ref]]`) link segments of a translation or commentary to segments of the root text.

- `source_segment_reference` — segment in this file
- `target_segment_reference` — segment in the root text

Transclusions in blocks without a block ID are collected and attached to the next block that has one, together with any transclusions in that block. The list then starts over. A group of transclusions before one block therefore gives a many-to-one alignment.

Headings are never aligned, and waiting transclusions are dropped when a heading comes before the next content block. Transclusions that point to a heading in the `root_text` file are skipped with a warning, since headings are not segments.

## Requirements

```
pip install PyYAML pyewts
```

Python 3.8+.

## How to run

Run from the vault root (the folder that contains `1-SOURCES/` and `4-SYSTEM/`):

```bash
python3 4-SYSTEM\scripts\parser-root-text\parser.py "1-SOURCES\Text\<lang>-<title>.md" "4-SYSTEM\scripts\linter-root-text\output\<lang>-<title>.lint.json"
```

## Notes

- If the lint JSON has no alt titles or contributors, the parser warns and carries on
