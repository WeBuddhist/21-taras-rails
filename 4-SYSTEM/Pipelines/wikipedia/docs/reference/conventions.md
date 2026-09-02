# Conventions — block IDs, segment IDs, file naming

The canonical reference for how texts in `corpora/` are addressed. The vendored skills cite this
file, `stages/align.py` parses by it, and the sibling OpenPecha repos
(`webuddhist-library-data-pipeline`, `bodhisattvacharyavatara-rails`) use the same scheme — a
block ID minted here resolves in their vaults and vice versa. Everything below is descriptive of
what the code enforces; where a rule lives in code, the reference is given.

## 1. Block IDs

A block ID is `^` + an ID of word characters and hyphens, at the **end of the block's last line**,
separated by a single space (`align.BLOCK_ID_RE`). IDs are never zero-padded (`^1-1`, not `^01-01`).

| Slot | Form | Example | Meaning |
|---|---|---|---|
| Title line | `^0` | `# ༄༅། །…བཞུགས་སོ། ། ^0` | The document title |
| Intro heading | `^I-0` | `## 0. ཀླད་ཀྱི་དོན། ^I-0` | Front-matter section heading |
| Intro content | `^I-N` | `^I-1`, `^I-3` | Front-matter blocks (homage, translator's line) |
| Chapter heading | `^N-0` | `## 1. ལེའུ་དང་པོ། … ^1-0` | Chapter N heading — **the TOC anchor** |
| Verse / stanza | `^N-V` | `^1-1`, `^6-33`, `^9-175` | Chapter N, traditional verse number V |
| Chapter colophon | `^N-a` | `^1-a` | Letter slot after the chapter's last verse |
| Back matter | `^a-0`, `^b-0` | `## མཛད་བྱང། ^a-0` | མཛད་བྱང, འགྱུར་བྱང section headings |
| TOC entry | `^toc-X-Y-Z` | `^toc-2-1-3` | Entries of a prepended dkar-chag (`add-toc` skill) |

Rules the pipeline depends on:

- **Content vs. structure.** Anything whose ID ends in `-0`, or is the bare `^0`, is editorial
  structure (headings), not root-text content. `align.parse_root` skips those; everything else is
  alignable content. Colophon blocks (`^N-a`) are content in the file but are not verses.
- **Verse numbers are the traditional chapter-relative numbers.** Gaps are normal (an edition may
  omit verses); never renumber to close a gap.
- **One stanza per block.** A stanza is typically 4 verse-lines (sometimes 2 or 8), one line per
  verse-line, `། །` at each line end, block ID on the last line. See
  `4-SYSTEM/Skills/format-tibetan-root-text/SKILL.md` for the full formatting procedure.
- **No spaces in IDs** — only letters, digits, hyphens, underscores.
- `^TOC-N` chapter anchors are **deprecated** — they parse without a usable TOC downstream. Chapter
  headings take `^N-0`, always.

### 1a. Commentary block IDs

A root text is numbered by its own traditional verse numbers. A commentary has none, so it is
numbered by **its own sa-bcad outline**: `stages/commentary.stamp_block_ids` walks the file and
gives every content block an ID derived from the heading above it.

| Slot | Form | Example | Meaning |
|---|---|---|---|
| Sa-bcad heading | `^N-0`, `^N-N-0`, … | `## བསྟོད་པ་དངོས་ ^1-0` | Outline node at depth 1, 2, 3… |
| Content block | `^<heading>-<n>` | `^1-1-2-1`, `^1-1-2-2` | The n-th block under heading `^1-1-2-0` |
| Front matter | `^I-n` | `^I-1`, `^I-15` | Content before the first heading — homage, title gloss |

Heading IDs come from **`tag-inline-toc`**, which derives them from the sa-bcad depth and refuses a
skipped level; `stamp_block_ids` never mints one. Content IDs are sequential within their heading
and are assigned last, over the final block structure, so a later insertion cannot strand an ID
mid-block. The `-0` suffix keeps meaning "heading", exactly as in a root text, so `^1-1-1` (the
first block under `^1-1-0`) and `^1-1-1-0` (a child heading of it) are distinct and tell you which
they are.

Three properties the pipeline relies on:

- **Stamping is idempotent.** Re-running never renumbers an existing ID; a second pass over a grown
  file continues past the highest number already used under that heading.
- **A transclusion-only block gets no ID.** An anchor is navigation, not content.
- **The reading view is invariant.** `commentary.reading_view` removes every layer of scaffolding —
  block IDs, transclusion lines, inserted headings, wikilink wrappers — and what it returns must be
  byte-identical before and after any ingest step. This is what `kwiki commentaries` checks after
  each step, and it is why quote verification still works on a stamped file: the verify gate reads
  through the scaffolding rather than around it.

An **inserted** heading (`##`–`######` plus a numeric ID ending `-0`) is removed by the reading view
entirely, because its title is a short name the model wrote for the outline node, not something the
commentator said — an article must not be able to quote it. A heading that arrived with the source
keeps its text and loses only the `#` marker.

The citation locator built from this is `source_id#^block_id` — `TARAC02_DGT#^1-1-2-1`. It is
recorded in `citations.json` and the review report and is **not** rendered into the `<ref>`: the ref
format is fixed by [`wikitext-spec.md`](wikitext-spec.md) §2 and an Obsidian block ID means nothing
to a Wikipedia reader. Its job is internal — it tells stage 7 which paragraph to check a quotation
against, and it tells a reviewer where to look.

## 2. Transclusions (alignment anchors)

A commentary is aligned to the root by transcluding the root verse before the commentary passage
that discusses it:

```
![[bo-བློ་ལྡན་ཤེས་རབ།#^1-4]]        short form (preferred; matches the target vault's precedent)
![[1-SOURCES/Text/BCAV08_SH_sk.md#^1-a]]   full-path form (also valid)
```

`align._existing_transclusions` treats any `![[…#^ID]]` as a human-checked anchor for verse `ID`;
these always win over inferred matches. Spacing around transclusions (the sa-bcad rules) is
specified in `4-SYSTEM/Skills/Transclusion-rootext-into-commentaries/SKILL.md`.

## 3. File naming

```
corpora/<corpus-id>/source/root.md                       the root text
corpora/<corpus-id>/source/commentaries/<SIGLUM>.md      one file per commentary
```

Commentary sigla follow the sibling repos' scheme, e.g. `BCAC14_GDR_bo_segmented.md`:

- `BCAC14` — text-family code + number (`BCA` = Bodhicaryāvatāra, `C` = commentary);
- `GDR` — author initials (Gyaltsab Dharma Rinchen);
- `_bo` — language tag;
- `_segmented` — processing state suffix, if the file has been through segmentation;
- `.toc.md` — variant carrying its own table of contents.

The `source_id` used in citations (`spyodjug-s003`) is minted by the registry from the team's
sheet row and recorded in `sources.yaml`; the commentary *file* is matched to it by substring
(`cli.py`'s `source_loader`), so keep sigla unique and stable. **Never rename a source file after
ingest** — `aligned.json` and every citation record the name.

## 4. Source-file front matter

Ingested files carry YAML front matter (inherited from the sibling vaults; preserved verbatim):

```yaml
book_id: BCAC14_GDR_bo          # the siglum
title: བྱང་ཆུབ་སེམས་དཔའི་…       # Tibetan title
author: རྒྱལ་ཚབ་དར་མ་རིན་ཆེན།      # Tibetan author
file_type: commentary | translation | root
language: Tibetan
lang_tag: bo
status: segmented | 1-segmented # processing state
```

Front matter is metadata, not content: the aligner and the extractor skip it, and nothing in the
pipeline edits it after ingest.

## 5. Tibetan text normalization

- Storage is always **NFC** (`tibetan.normalize.nfc`). Every comparison the pipeline makes — quote
  verification, term lookup, alignment probes — normalizes to NFC first.
- Tsheg is **U+0F0B** (་). The non-breaking tsheg U+0F0C (༌) is replaced with U+0F0B at *cleaning*
  time only (`clean-raw-text`); after ingest, stored punctuation is never edited.
- Shad is **U+0F0D** (།); double shad **U+0F0E** (༎) appears only in colophons.
- Verse-line separator is `། །` (shad, space, shad). A single shad directly followed by a Tibetan
  letter mid-line marks two merged half-lines (see `format-tibetan-root-text`).
- **Never "fix" Tibetan punctuation in stored source data.** A tsheg or shad in a title or a quote
  is orthography; the verify gate compares character-for-character.

## 6. Term identity

A term's citation form ends in a shad (`བྱང་ཆུབ་སེམས།`), its lemma form in a tsheg
(`བྱང་ཆུབ་སེམས་`). They are **one term**: identity is `registry.term_key` — NFC, trimmed, terminal
tsheg/shad stripped, nothing else. Interior punctuation is significant (`ཆོས་སྐུ` ≠ `ཆོསསྐུ`).
Wikipedia title variants (tsheg / shad / bare) are a separate, live hazard — the publisher probes
all three (`wiki/client.title_variants`); see `docs/reference/wikitext-spec.md` §3.

## 7. Where things live per corpus

See the per-corpus contract in [`CLAUDE.md`](../../CLAUDE.md): `source/` is never modified after
ingest; `work/` is reproducible and never hand-edited; `sources.yaml` / `terms.yaml` at the corpus
root are the curated registry; `articles/<term>/` holds per-term artifacts; `ledger.json` tracks
status.
