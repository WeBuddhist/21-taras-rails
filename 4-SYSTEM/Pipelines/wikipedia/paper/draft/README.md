# paper/draft — the deliverables and how to regenerate them

> **2026-08-23 cleanup.** Superseded paper versions were deleted on the lead's instruction —
> `paper.md` (the 2026-08-02 first draft), `paper-methods.md` and `paper-skeleton.md` (the
> 2026-08-10 intermediates), the 26-page .docx, and the externally supplied
> `…-corrected.md` rewrite (its factual fixes were already harvested on 2026-08-19). All are
> recoverable from git history. What remains is the final set: `paper-src.md` → the 15-page
> .docx, the deck + its builder, and the three working notes (cost, batch checklist, this
> README).

> **2026-08-21 revision — back to 15 pages.** The 2026-08-19 update had grown the paper to
> ~19 pages; `paper-src.md` was cut back to the 15-page budget (12,879 → 10,812 words) and
> the .docx rebuilt. Page count was verified by exporting the .docx to PDF via Pages: this
> build and the known-15-page 2026-08-10 build both render at 19 Pages-pages (Pages inflates
> the Word layout ~×1.27, so 19 Pages-pages ≈ 15 Word pages). Content changes beyond
> compression: **the alignment/transclusion step (old §5.3) is removed from the paper** —
> retired from the production path, nothing downstream consumes aligned data; one honest
> clause in Route A (§5.8) records that the pilot's extraction used it, since the §8
> extraction-capture numbers are measured against it. Sections 5.4–5.12 renumbered to
> 5.3–5.11. **New Figure 3**: a worked example — excerpt of Gendün Drub's promoted sa-bcad
> tree (10 of 37 nodes, English glosses; its leaves under the extended explanation number
> exactly 21). Old Table 3 (human checkpoints) became a prose sentence in §5.0; Tables 4–6
> renumbered 3–5. All measured numbers and [TO FILL] slots preserved.

> **2026-08-19 revision.** `paper-src.md` was updated to the current pipeline state and the
> .docx rebuilt: §5 restructured so every step states input → output → how it works in plain
> language; a new §5.4 (the subject-selection keyword chain); §5.9 extended with the Route B
> batch, the import bridge, and the native-reviewer style-revision loop (v2 skill); batch
> numbers throughout (67 consolidated pages, 43+23 drafted, 42 imported, 861/882 = 97.6%
> verbatim); bo.wikipedia figures re-checked against the live API. Reference for the step
> detail: `../11 - Pipeline Steps in Detail.md` (note: it still documents the alignment step
> the paper no longer reports, as run history). Remaining **[TO FILL]** slots are unchanged —
> they need team data (revival-campaign records, reviewer-minutes, rater results, batch audit
> pass rates).

| file | what |
|---|---|
| `paper-src.md` | **The source of the .docx** — constrained markdown (`%TITLE`/`%AUTHOR`/`%DATE`, `##`/`###` headings, pipe tables, fenced code, `>` quotes, `-`/`1.` lists). Edit here, never in Word. |
| `build_docx.js` | Regenerates the .docx: `node build_docx.js paper-src.md Expanding-the-Digital-Footprint-of-Tibetan.docx` (needs `npm install docx` once, beside this file or on NODE_PATH). Page geometry lives here: A4, 0.8in margins, Times New Roman 10.5pt, single-spaced. |
| `Expanding-the-Digital-Footprint-of-Tibetan.docx` | The 15-page venue-neutral paper, built from `paper-src.md`. |
| `IATS-2026-slides.pptx` | The 16-slide deck per the canonical plan. Same numbers, same `[TO FILL]` markers (slides 3 and 13); slide 12 has the slot for the pre-recorded demo capture. |
| `build_deck.js` | Regenerates the deck: `node build_deck.js` (needs `npm install pptxgenjs react react-dom react-icons sharp` once, beside this file or on NODE_PATH). Edit content here, not in PowerPoint, while numbers are still moving. Every Tibetan run on the slides carries an English gloss — keep that invariant when editing; the IATS audience mostly does not read Tibetan. |
| `cost-and-scalability.md` | Measured per-article machine cost (volumes from `corpora/tara21/work/eval/eval.json`, prices as of 2026-08-02) and the scaling arithmetic behind §8 and slide 13. |
| `batch-reporting-checklist.md` | Every `[TO FILL]` slot the corpus-wide batch feeds, plus the three prerequisites the batch needs before it can run and the list of things a bigger N does *not* fix. Read this before filling any number into §8. |

English check-translations of the three articles (for reviewers who don't read
Tibetan) live beside each article as `article.en.md`, combined in
`corpora/tara21/review/pending/translations-for-review.en.md`. Per-stage evaluation
numbers: `corpora/tara21/work/eval/EVAL_REPORT.md`.

Tibetan on slides is set in **Noto Serif Tibetan** per `../08 - Presentation and Demo Plan.md`
— follow that file's checklist before travel: embed the font (or install on the
presentation laptop), export a PDF of every Tibetan-bearing slide as backup, and check the
two known bad stacks (དྡྷི in Noto v2.001, ཨཱརྻ in Jomolhari on macOS).
