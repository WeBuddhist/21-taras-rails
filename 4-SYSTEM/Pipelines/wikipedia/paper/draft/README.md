# paper/draft — the deliverables and how to regenerate them

> **2026-08-19 revision.** `paper-src.md` was updated to the current pipeline state and the
> .docx rebuilt: §5 restructured so every step states input → output → how it works in plain
> language; a new §5.4 (the subject-selection keyword chain); §5.9 extended with the Route B
> batch, the import bridge, and the native-reviewer style-revision loop (v2 skill); batch
> numbers throughout (67 consolidated pages, 43+23 drafted, 42 imported, 861/882 = 97.6%
> verbatim); bo.wikipedia figures re-checked against the live API. Reference for the step
> detail: `../11 - Pipeline Steps in Detail.md`. Remaining **[TO FILL]** slots are unchanged —
> they need team data (revival-campaign records, reviewer-minutes, rater results, batch audit
> pass rates).

| file | what |
|---|---|
| `paper-src.md` | **The source of the .docx** — constrained markdown (`%TITLE`/`%AUTHOR`/`%DATE`, `##`/`###` headings, pipe tables, fenced code, `>` quotes, `-`/`1.` lists). Edit here, never in Word. |
| `Expanding-the-Digital-Footprint-of-Tibetan-corrected.md` | Externally supplied correction pass (2026-08-10, dropped in after `paper-src.md` that evening) — a heavily hedged rewrite with a changed title. **Not** the docx source. Its factual fixes (dated API snapshot) were harvested into `paper-src.md` on 2026-08-19; its softened thesis framing was deliberately not adopted (the canonical plan keeps the doom-spiral/virtuous-cycle claim as the contribution, and the submitted title/abstract stand). |
| `build_docx.js` | Regenerates the .docx: `node build_docx.js paper-src.md Expanding-the-Digital-Footprint-of-Tibetan.docx` (needs `npm install docx` once, beside this file or on NODE_PATH). Page geometry lives here: A4, 0.8in margins, Times New Roman 10.5pt, single-spaced. |
| `Expanding-the-Digital-Footprint-of-Tibetan.docx` | The 15-page venue-neutral paper, built from `paper-src.md`. |
| `Expanding-the-Digital-Footprint-of-Tibetan-26pp.docx` | The superseded 26-page version, kept for reference (2026-08-10). |
| `paper.md` | Full first draft to the canonical structure (`../10 - Canonical Paper and Slides Plan.md`). Every pipeline number comes from the reviewed run — `corpora/tara21/REVIEW-2026-08-02.md`. `[TO FILL]` slots need team-only data: revival-campaign records (§3), human-rater + reviewer-minutes results (§8). |
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
