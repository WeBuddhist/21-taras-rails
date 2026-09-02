# Resegmentation Log — pema-namgyal (manual pass, superseding the earlier automated run)

The earlier automated `resegment.py` run (see the 32 merge ops originally logged
here, and `0-INBOX/temp/RESEG-pema-namgyal/windows/window-000{0,1}.json`) had
already been copied into `1-SOURCES/Commentaries/...pema-namgyal...md` — verified
byte-identical (same MD5) against the then-current source file before this pass
began. Two problems with that automated output were found on review against the
reference commentary `karma-maitri` (`1-SOURCES/Commentaries/...karma-maitri...md`,
`2-RAILS/Sections/Raw/toc-tree/karma-maitri.md`), which segments and block-IDs
each author-numbered homage item (1, 2, 3, …) as its own separate citable unit:

1. 20 of the automated MERGE ops had paired up two *distinct* numbered homage-items
   (e.g. item 5 with item 6, item 31 with item 32, …) into one block each. This
   contradicts the one-numbered-item-per-block convention established by
   karma-maitri and would have halved citation granularity for verse-level rails.
   -> Un-merged: each of these 20 blocks was split back into its two original
      numbered items (splitting only at whitespace already present between the
      two clauses -- no characters altered).
2. The final block (originally-atomic raw-OCR line, item 47 plus the hidden-meaning
   digression, the benefit section, and the colophon -- ~3100 characters, far past
   the ~2-4 line target) had never been split at all, because `resegment.py` can
   only merge, never split; no REVIEW flag had been raised for it either.
   -> Split into 8 sense-unit paragraphs at clear topic transitions (hidden-meaning
      digression / tantra cross-reference / hand-off sentence / benefits-of-recitation
      opening / benefits gained / poison-antidote benefit / recitation-count benefit /
      closing attribution+colophon).

Done by direct LLM judgment (no GEMINI_API_KEY / google-genai available in this
environment) rather than the scripted Gemini call, applying the same whitespace-only
integrity rule as `resegment.py`'s `check_integrity()`:
`strip_all_whitespace(before) == strip_all_whitespace(after)` -- verified to hold
(byte-for-byte, via independent squeeze-compare) before the source file was written.

Paragraphs before this pass: 50   Paragraphs after: 77
