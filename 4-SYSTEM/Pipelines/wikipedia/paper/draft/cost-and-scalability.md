# What a pipeline article costs, and whether this scales

*2026-08-02. Volumes measured from the reviewed tara21 run's artifacts
(`corpora/tara21/work/eval/eval.json`); token counts are estimates from measured
characters (method below); prices are current list prices as of this date.*

## Measured volumes (the part that is not an estimate)

The full model chain per article is extract (batched at 25k chars) → claims → outline →
draft → audit. For the three articles:

| term | model calls | input chars | output chars | aligned material offered |
|---|---|---|---|---|
| འཇིག་རྟེན་གསུམ ("three worlds") | 5 | ~89,500 | ~35,000 | 18,065 |
| སྒྲོལ་མ (Tārā) | 11 | ~235,800 | ~17,400 | 165,442 |
| སྡུག་བསྔལ ("suffering") | 6 | ~109,800 | ~32,800 | 40,752 |
| **total** | **22** | **~435,000** | **~85,000** | — |

Wall-clock: roughly 10–20 minutes per article end-to-end (ledger timestamps), fully
parallelizable across articles. The deterministic stages — alignment, rendering, the
character-exact verification gate — cost **zero model dollars** by construction.

## Characters → tokens (the stated assumption)

Tibetan is UTF-8 3 bytes/char, and tokenizer efficiency on Tibetan varies widely by
model (Petrov et al. 2023 measured a ~4× byte premium vs Chinese — the paper's own §1
point, felt in the invoice). We bracket with three rates: **0.7 tokens/char**
(good subword coverage), **1.5** (central), **3.0** (byte-fallback worst case).

## Prices (as of 2026-08-02)

- **Gemini 3.5 Flash** (the pipeline's default local model): **$1.50 in / $9.00 out**
  per MTok; cached input $0.15; batch API −50%. (Gemini 3.6 Flash, July 2026, is
  already $1.50/$7.50 — costs are falling under us.)
- **claude-sonnet-5** (the model that wrote this run's drafts in the sandbox):
  **$3.00 in / $15.00 out** list; introductory $2.00/$10.00 through 2026-08-31.

## Cost per article

All five model stages, uncached, for **all three articles together**:

| tokens/char | Gemini 3.5 Flash | claude-sonnet-5 (list) |
|---|---|---|
| 0.7 | $0.99 | $1.81 |
| 1.5 (central) | $2.13 | $3.87 |
| 3.0 | $4.26 | $7.75 |

**Per article: ≈ $0.33–1.42 on Flash (central ≈ $0.71); ≈ $0.60–2.58 on Sonnet.**
Prompt caching (the claims payload recurs in three stages) and batch pricing each cut
this substantially; the team's July 2026 working estimate of **$0.12–0.60/article** is
consistent with the optimistic end plus caching. The cross-model audit adds
~$0.02–0.10/article per run on Flash — the 3× stability protocol (pass rates over
repeated runs) stays under $0.30/article. The dual-model division (Claude writes,
Gemini audits, or the reverse) roughly averages the two columns rather than doubling
anything: each stage runs once, on one model.

## Is it scalable? The three-line arithmetic

**Machine cost is not the constraint.**

- 10,000 articles ≈ **$3.3k–14k** on Flash (central ~$7k; batched ~$3.5k).
- 100,000 articles — a serviceable encyclopedia — ≈ **$33k–142k** (central ~$71k;
  batched ~$36k). One-time, parallelizable, on falling prices: the machine cost of an
  entire Tibetan encyclopedia is on the order of **one project grant** (for reference,
  Wikimedia Rapid Fund grants run $500–5k; this needs a bigger grant, not a miracle).
- Both figures price the **marginal article**, not the system. Building the pipeline
  and bringing a corpus into it (cleaning, segmentation, alignment, registry curation)
  is skilled up-front engineering; that fixed cost amortizes across every article and
  every corpus the machinery touches — manual writing has no fixed-cost term to
  amortize, which is the honest form of the comparison. Any projection quoted from
  this file should say so (the paper's §8 now does).

**Human review is the constraint — by design.** Throughput is bounded by review
capacity, not model capacity. At an assumed 30–60 reviewer-minutes per article
(**to be measured** in the August evaluation batch — the paper's lead metric), 100,000
articles is **50,000–100,000 person-hours ≈ 24–48 person-years**, spread over a
community. Compare the manual-only baseline: at bo.wikipedia's observed ~350 articles
per year, *writing* the same corpus takes ~285 years. That is the trilemma's third
horn in numbers: supervised automation converts a **writing problem measured in
generations** into a **review problem measured in person-years** — "generations
collapse to years" — and the review problem parallelizes across every fluent reviewer
the community can recruit, which is precisely the resource the revival campaigns
build.

Two multipliers to keep honest in any projection: (1) the extraction tuning pass may
*raise* per-article cost by processing more of the offer (སྒྲོལ་མ's 165k-char offer at
full capture would roughly double that article's input) — quality first, then cost;
(2) failed/repeated runs (audit retries, nondeterminism) add a factor ≈1.2–1.5×, not
an order of magnitude.

*Sources for prices:* Anthropic API pricing (claude-api reference, cached 2026-06-24);
Gemini pricing via [CloudZero](https://www.cloudzero.com/blog/gemini-pricing/),
[PricePerToken](https://pricepertoken.com/pricing-page/model/google-gemini-3.5-flash),
[DevTk.AI](https://devtk.ai/en/blog/gemini-api-pricing-guide-2026/) (all August 2026).
Verify at camera-ready.
