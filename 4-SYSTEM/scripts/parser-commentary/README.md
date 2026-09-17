# Parser — Commentary

Takes a commentary file and its linter output and writes the API payloads for the text, edition, table of contents and alignment to the root text.

Forked from `parser-root-text`. Content segments default to **`paragraph`**, and `alignment.json` is always written. Run `linter-commentary` first.

## What it does

1. **extract_text_input** — takes `text_input` from the lint JSON (or `resolved` from a `.lint.errors.json`), drops empty fields and contributors without an id, writes `text.json` (includes `commentary_of` when set)
2. **build_edition** — builds the edition content and its segments with character spans from the body text (headings left out), writes `edition.json`
3. **build_toc** — builds a nested table of contents from the headings (headings are used only here), writes `toc.json`
4. **build_alignment** — links commentary segments to root-text segments through transclusions, writes `alignment.json`

The parser stops if the file's `file_type` is set to anything other than `commentary`.

## Output

```
output/
  <stem>.text.json        # text_input payload (with commentary_of)
  <stem>.edition.json     # edition metadata, content and segments
  <stem>.toc.json         # nested TOC with character spans
  <stem>.alignment.json   # commentary → root-text alignments
```

## Edition

Same as `parser-root-text` (see its README): headings add no segment and no text to `content` (they are used only for the TOC), one segment per content block, the block ID as `reference`, `metadata.source` from `source` or `source_url`, `metadata.type` from `edition_type` (default `critical`).

### Segment types

The type comes from the block ID. The rows are checked from top to bottom; the first match wins.

| Block / ID | Type | Example |
|------------|------|---------|
| ID starts with `T` or `t` | `top_segment` | `^T-1` |
| Any part is an uppercase Roman numeral | `front_matter` | `^I-1`, `^2-I-3` |
| ID contains `<number>x<number>` | `paragraph` | `^1-2x3` |
| Last part is `U<number>` (unnumbered) | `paragraph` | `^1-U4` |
| Any part is lowercase letters only | `back_matter` | `^a-1` |
| Anything else | `paragraph` | `^1-1` |

## Alignment

Transclusions in the commentary (`![[1-SOURCES/Text/<lang>-<title>.md#^1-1]]`) say which root-text segment the commentary is discussing.

- `source_segment_reference` — segment in the commentary
- `target_segment_reference` — segment in the root text

A transclusion, or a group of consecutive transclusions, opens a scope. Every commentary block that follows is aligned to those root-text segments until the scope ends, at either:

- the next transclusion group, or
- any heading — commentary after a heading must carry its own transclusion to be aligned

Headings are never aligned. Transclusions that point to a heading in the `root_text` file are skipped with a warning, since headings are not segments. Alignment can be many-to-one (several paragraphs on one verse) or many-to-many (several paragraphs on a group of verses).

## Requirements

```
pip install PyYAML pyewts
```

Python 3.8+.

## How to run

Run from the vault root (the folder that contains `1-SOURCES/` and `4-SYSTEM/`):

```bash
python3 4-SYSTEM\scripts\parser-commentary\parser.py "1-SOURCES\Commentaries\<lang>-<title>.md" "4-SYSTEM\scripts\linter-commentary\output\<lang>-<title>.lint.json"
```

## Notes

- If the lint JSON has no alt titles or contributors, the parser warns and carries on
- Blocks without a block ID are skipped with a warning; so are content blocks whose ID has more than 3 parts
- Blocks that contain only transclusions are left out of the edition content; they feed alignment only
- TOC spans are offsets into the edition `content` (which has no heading text), built the same way as in `parser-root-text`
- Tibetan TOC titles in Wylie are converted to Unicode
