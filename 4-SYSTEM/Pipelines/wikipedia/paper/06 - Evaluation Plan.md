# Evaluation Plan — Small, Honest, Defensible

The abstract promises to "evaluate its early outputs." Nothing exists yet — this is the single biggest abstract-to-evidence gap, and it is closable in the 4 weeks. The design below is squarely within published norms (STORM's flagship human study was 20 article pairs × 2 raters; AIS used small trained pools).

## Corpus

- **15 articles** (acceptable range 10–20), drawn from the Heart Sutra term list + figures/texts, each 500–1,500 syllables.
- Stratify across ~3 domains: doctrine/philosophy, figures (Treasury of Lives coverage), texts.
- Include **3–5 topics that already have bo.wikipedia stubs** → enables blind pairwise comparison.
- Every topic pre-cleared for notability (≥1 independent secondary source — see [[05 - Wikipedia Policy and Community Strategy]]).

## Raters

- **3 native Tibetan speakers** with editorial or academic background (mirror STORM's "experienced editor" criterion). Recruit now; name them (with consent) in the paper.
- Candidate pools: bo.wikipedia active editors (e.g. `Tsampaeater`), Monlam AI language team, Esukhia network, Rangjung Yeshe Institute (conveniently, the conference co-host).
- Every article rated by ≥2 raters; a shared subset of ≥5 articles rated by all 3 for agreement estimation.

## Instruments (four legs)

### 1. Rubric (primary) — 7 dimensions, 1–5 Likert
STORM's five (Interest, Coherence/Organization, Relevance/Focus, Coverage, **Verifiability**) + two Tibetan-specific: **Fluency/grammatical correctness** and **Terminology/register appropriateness** (honorifics, established Buddhist terms). Add a **Neutrality** check (STORM found 7/10 editors flagged un-neutral tone; WP:Good Article criteria back this). Use 2–3 anchored items per dimension (van der Lee et al. best practices). Report means ± sd and **Krippendorff's ordinal α** (0.667/0.8 conventions; NLG-typical agreement is only 0.3–0.5 — cite that as context, don't panic over moderate α).

### 2. Citation audit (the headline metric)
Sample ~10 cited statements per article (~150 judgments). One rater applies the **AIS two-stage protocol** (interpretability check → "According to source P, …" attribution judgment, binary); second rater double-codes 30%. **Manual by necessity — no NLI model supports Tibetan** (state this as a finding). Report:
- **Citation precision** (% cited statements supported — ALCE/WikiCrow definition)
- **Uncited-claim rate**
- **Unsupported-fact (hallucination) rate** via FActScore-style atomic facts

Benchmark anchors for interpretability: WikiCrow 86.1% precision / 3.5% uncited vs human-Wikipedia 71.2% / 13.6%. (Keep WikiCrow's numbers straight: 9% = incorrect-statement rate, Dec 2023 demo; 13.5% = cited-but-unsupported rate, 2024 eval. Different metrics, different years.)

### 3. Pairwise preference
For the 3–5 topics with existing bo.wiki stubs: blind A/B, pipeline draft vs existing article. Pairwise/best-worst scaling is far more reliable than absolute ratings at small N (Kiritchenko & Mohammad).

### 4. Productivity (the sustainability evidence)
For every article log:
- **Time**: generation + human review/edit time; vs from-scratch writing time for 2–3 control articles by the same editor. (Reference points: NMT post-editing +36% translator throughput; DivEMT's caution that gains aren't automatic — measure, don't assume. Log actual times; perceived time is unreliable.)
- **HTER at syllable level** between LLM draft and approved version (segment with OpenPecha's own **botok** — nice touch: our tokenizer measuring our pipeline).
- **Acceptance rate** per section: kept / lightly edited / rewritten / deleted.
- **Cost**: API cost per article (≈$0.12–0.60 at July 2026 prices — negligible; the honest headline is that *reviewer-minutes are the real currency*).

## Zero-cost structural proxies

Syllable count, section count, reference count, wikilink density — plus the **Wikimedia language-agnostic article-quality model** via the Lift Wing API, which (unlike ORES) works for any wiki including bo. Its feature weights (length .395, references .181, sections .123, wikilinks .115, media .114, categories .070) justify the proxies. Caveat in paper: model trained on en/fr/ar wikis, scores are wiki-relative.

## What we explicitly cannot do (turn into evidence for claim 1)

- No COMET/BERTScore — XLM-R's training corpus (CC-100) excludes Tibetan; neural metric scores would be out-of-distribution garbage.
- No automatic readability — Wikimedia's readability model excludes Tibetan.
- No ORES article-quality model for bo.
- No Tibetan NLI → no automatic citation checking (hence the manual AIS protocol).
- BLEU only meaningful with explicit segmentation (botok); **chrF/chrF++ is the safest automatic metric** if any translation sub-component needs scoring. FLORES-200 (`bod_Tibt`) is essentially the only standard test set that includes Tibetan.

Each unavailable tool is one more datum for "Tibetan lacks NLP infrastructure" — the paper's opening claim measuring itself.

## Minimum viable version (if time collapses)

WikiCrow-style statement-level audit of **5 articles** (~300 statements, 2 raters) + productivity logs + structural proxies. Even that converts the abstract's promise into evidence: "N=5 articles, 312 statements, X% supported, Y min/article review time."

## Deliverables checklist

- [ ] Topic list (15) with pre-cleared secondary sources — week 1
- [ ] Rater recruitment (3, named) — week 1–2
- [ ] Rubric sheet (bo/en bilingual) + audit protocol sheet — week 2
- [ ] Time-logging instrumented in the pipeline — immediately
- [ ] Ratings + audit complete — end of week 3
- [ ] Numbers in slides — week 4
