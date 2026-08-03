Work on the IATS paper. Arguments: $ARGUMENTS (a section name, a question, or "status")

## Orient first

`4-SYSTEM/Pipelines/wikipedia/paper/00 - START HERE.md` is the map. They live in `4-SYSTEM/Pipelines/wikipedia/paper/`:

| File | What it holds |
|---|---|
| `abstract.md` | **The submitted abstract, verbatim** — the promises the paper must keep; never edit its body |
| `01 - Paper Argument and Structure` | The thesis, a claim-by-claim evidence table, the outline |
| `02 - What We Already Have` | Asset inventory and the honest gap list |
| `03 - Pipeline Design` | The architecture as the paper describes it |
| `04 - Related Work and Landscape` | STORM etc., low-resource precedents, Tibetan NLP, cyclical-claim evidence |
| `05 - Wikipedia Policy and Community Strategy` | Current rules, failure precedents, the bo.wikipedia plan |
| `06 - Evaluation Plan` | The small-N design: 15 articles, 3 raters, citation audit |
| `07 - Roadmap to August` | Week by week |
| `08 - Presentation and Demo Plan` | Talk structure, offline demo, Tibetan rendering pitfalls |
| `09 - Reading List and Bibliography` | Every source with a URL |

`4-SYSTEM/Pipelines/wikipedia/research/reports/` holds the six underlying research reports if you need to check a claim's source.

## The thesis, so you don't drift from it

Grounded, citation-first LLM drafting plus mandatory native-speaker review can turn Tibetan's
scattered sources into durable encyclopedic content — and the sign of the "AI content feedback loop"
flips from *doom spiral* to *virtuous cycle* only under that human gate.

That last clause is the contribution. The same mechanism the paper celebrates is what MIT Tech
Review documented destroying other small-language Wikipedias. Do not soften this into a caveat;
answering it **is** the paper.

## Rules for writing about the pipeline

- **Report only what has actually run.** The pipeline has a working align + terms + claims + draft
  + audit + verify chain and 547 passing tests, and three tara21 articles have been through it end
  to end (reviewed, cross-model audited, ledger `verified`). If you write evaluation numbers, they
  must come from a real run whose artifacts are on disk — read
  `4-SYSTEM/Pipelines/wikipedia/corpora/tara21/REVIEW-2026-08-02.md` before citing any of them.
- **Two metrics matter most** and they need real data: citation precision (share of cited statements
  a rater confirms) and human review minutes per article. Benchmarks to compare against are in
  `06 - Evaluation Plan`.
- **Cite the counter-literature.** Thompson et al. 2024, Shumailov et al. 2024 (Nature), the MIT
  Tech Review doom-spiral piece. A reviewer who knows this field will raise them; the paper is
  stronger for raising them first.
- **Keep WikiCrow's numbers straight**: 9% is the incorrect-statement rate from the Dec 2023 demo;
  13.5% is the cited-but-unsupported rate from the 2024 PaperQA2 evaluation. Different metrics,
  different years. Never present them as competing estimates of one quantity.
- Venue: **17th IATS Seminar, 23–29 August 2026, The Soaltee Kathmandu** (moved from the earlier
  Boudha venue). Audience is Tibetan-studies scholars, mostly not NLP people — lead with language
  access and preservation, keep model architecture to one slide.
