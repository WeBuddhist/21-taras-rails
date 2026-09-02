# Resegmentation Log — gendun-drub

Method: manual sense-unit grouping by Claude (no GEMINI_API_KEY / google-genai
available in this environment), followed by a deterministic whitespace-only
integrity check equivalent to `resegment.py`'s `squeeze()`/`check_integrity()`.

The two prior automated attempts left the source as 23 undifferentiated
numbered blobs (raw OCR paragraph units, each spanning many sentences with no
internal line breaks) — not the one-clause-per-line shape the standard
`resegment.py` merge-based pipeline expects. Because the required edit here is
paragraph *splitting* rather than line *merging*, the grouping judgment was
made directly by Claude (reading each of the 23 blobs and inserting paragraph
breaks at sense-unit boundaries — root-verse citations kept together, each
word-by-word gloss kept together, each outline/transition sentence kept
separate), and only the deterministic whitespace-only verification step was
reused from the skill (same squeeze-and-compare logic as `resegment.py`).

Source blobs in  : 23  (raw OCR paragraph units, numbered "1." – "23.",
                        corresponding to the front matter + 21 praise verses
                        + the phan-yon/colophon unit)
Paragraphs out    : 117
Integrity check   : PASS — strip_all_whitespace(source_before) ==
                     strip_all_whitespace(source_after)
                     (17120 non-whitespace characters, identical on both sides)
File size         : 51014 bytes -> 51178 bytes (delta is entirely added
                     newlines: 117 - 23 = 94 new paragraph breaks)

No word or character was added, removed, or reordered. Only whitespace
(newlines) was inserted, splitting each of the 23 raw blobs into short
sense-unit paragraphs, one per physical line, blank-line separated —
matching the paragraph density of the other commentaries already processed
in this batch (cf. karma-maitri, konchok-thabkhe, etc.).

Applied directly to:
`1-SOURCES/Commentaries/སྒྲོལ་མ་ཕྱག་འཚལ་ཉེར་གཅིག་གི་ཊཱིཀྐ་རིན་པོ་ཆེའི་ཕྲེང་བ།.md`

A copy of the resulting text (pre-toc-tree-ingest, i.e. before headings/block
IDs are inserted) is kept at `0-INBOX/resegmented/gendun-drub.reseg.md` for
parity with the sibling commentaries' outputs.
