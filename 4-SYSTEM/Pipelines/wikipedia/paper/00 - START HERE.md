# IATS 2026 Paper — Start Here

**Paper:** *Expanding the Digital Footprint of Tibetan: A Semi-Automatic Pipeline for Wikipedia Article Generation Using LLMs*
**Author:** Tashi Tsering, The OpenPecha Project (tashitsering@dharmaduta.in)
**Abstract:** the submitted text is preserved verbatim in [[abstract]] — every promise the paper must keep is in there; quote-check against it, not from memory.
**Venue:** 17th Seminar of the International Association for Tibetan Studies (IATS), **23–29 August 2026, The Soaltee Kathmandu, Nepal** (venue moved from the earlier-announced Hyatt/Boudha location). Organized by HiCAS (Kathmandu University) and KU-CBS at Rangjung Yeshe Institute. Contact: iats2026@conftool.com. Presentations may be in English or Tibetan.

> [!warning] Timeline
> Today is **24 July 2026**. The seminar starts **in 4 weeks**. Everything in these notes is scoped to be achievable in that window. The week-by-week plan is in [[07 - Roadmap to August]].

> [!important] Update 2026-08-02 — the lead's canonical plan supersedes where it conflicts
> The paper structure and slide deck were designed end-to-end in the lead's claude.ai session
> (2026-08-01) and reconstructed in [[10 - Canonical Paper and Slides Plan]]. Where that plan and
> the notes below disagree — section order, the new §3 revival/critical-mass argument, the slide
> sequence — **the canonical plan wins.** These notes remain the source for verified facts,
> policy detail, and demo logistics.

> [!tip] Update 2026-08-02 (later) — a full draft now exists, built on a reviewed pipeline run
> **`paper/draft/paper.md`** is the complete first draft to the canonical structure, and
> **`paper/draft/IATS-2026-slides.pptx`** the 16-slide deck. Every pipeline number in both comes
> from the reviewed tara21 run (three articles, full chain, cross-model audited, 81/81 quotations
> character-verified — `corpora/tara21/REVIEW-2026-08-02.md`). The **[TO FILL]** slots are the
> revival-campaign records (§3, slide 3) and the human-rater/reviewer-minutes results (§8,
> slide 13) — data only the team can supply. The 2026-08-01 note below ("no live Gemini run yet")
> is superseded: the chain has now run live end to end.
>
> Later the same day the draft was revised against two external reviews (ChatGPT + Gemini,
> supplied by the lead) — scope narrowed to the three-article case study, verification kinds
> separated, notability/community-consent gates made explicit. The change log is the
> draft-status block at the top of `paper/draft/paper.md`; the title and abstract stand.

## The one-paragraph situation

The abstract promises seven things: (1) Tibetan is digitally underrepresented, (2) a semi-automatic pipeline that generates cited Tibetan Wikipedia articles, (3) human-in-the-loop editorial oversight, (4) automated extraction/structuring/citation-alignment, (5) a bigger digital footprint feeding Tibetan NLP and LLM-app visibility, (6) a sustainable cyclical model for under-resourced languages, and (7) a demo plus evaluation of early outputs. **The good news:** the Railroad/WeBuddhist work already contains a working prototype of (2)–(4) — two polished Tibetan encyclopedia articles on Heart Sutra concepts, 79 English term articles, a term-extraction skill, and an auditable ingestion pipeline. **The gaps:** only 2 Tibetan articles exist, citations are vault-internal (not yet Wikipedia-ready), nothing has been uploaded to bo.wikipedia, and no evaluation has been run. The four weeks are about closing exactly those gaps.

> [!note] Update 2026-08-01 — the pipeline now exists as code, not just as vault prototype
> Claims (2)–(4) are no longer carried by the Railroad prototype alone: this repo implements the
> full chain (align → terms → extract → organize → draft → **deterministic verify gate** → publish
> with dry-run default, plus the update path for the 520 terms whose articles already exist), with
> 491 passing tests and Wikipedia-ready external citations resolved from `sources.yaml`. See
> [`STATE.md`](../STATE.md). Still true and still the critical path: **no live Gemini run yet (no
> API key), nothing uploaded to bo.wikipedia, no evaluation run** — claim (7) remains the gap the
> remaining weeks must close.

## The strongest cards we hold (from research, all verified 2026-07-24)

1. **The prototype is real.** Two finished, multi-commentary, fully block-cited Tibetan articles + a scalable extraction layer. See [[02 - What We Already Have]].
2. **Nobody else does this for Tibetan.** STORM, WikiChat (25 languages), WikiCrow, WikiAutoGen — none supports Tibetan. Wikimedia's own MinT covers Tibetan only as weak NLLB-200 machine translation. The novelty claim is defensible. See [[04 - Related Work and Landscape]].
3. **The community-consent story is unusually strong.** bo.wikipedia's *only human administrator* is an OpenPecha-affiliated account (`Pecha-G.Dhargyal`, active as of June 2026). This flips the biggest objection to AI content on small wikis — but it must be formalized publicly. See [[05 - Wikipedia Policy and Community Strategy]].
4. **The numbers are vivid.** bo.wikipedia: 8,072 articles, 31 active editors/month, 2 admins, ~350 new articles/year — for 7M+ speakers. Frontier LLMs score *below random* on the Tibetan TLUE benchmark (GPT-4: 68.9% → 17.5%). Tokenizers make Tibetan 4×+ more byte-expensive than Chinese.

## The four biggest risks (each has a mitigation doc)

| Risk | Mitigation |
|---|---|
| "Evaluate early outputs" promised, none exists | Small honest audit, 4-week design in [[06 - Evaluation Plan]] |
| AI-generated content is now heavily restricted on Wikipedia (en-wiki ban Mar 2026, G15 speedy deletion) | Frame as *machine-drafted, human-published*; do's/don'ts in [[05 - Wikipedia Policy and Community Strategy]] |
| Source licensing: 84000/Lotsawa House/ToL/BDRC are all NC/ND or fair-use — text cannot be reused on Wikipedia | "Cite, don't copy" design principle, [[03 - Pipeline Design]] |
| Live demo in Kathmandu (wifi unconfirmed; Sept 2025 Nepal internet shutdown precedent) | Offline-first demo plan, [[08 - Presentation and Demo Plan]] |

## Reading order

1. [[01 - Paper Argument and Structure]] — thesis, claim-by-claim evidence map, paper outline
2. [[02 - What We Already Have]] — vault asset inventory and honest gap list
3. [[03 - Pipeline Design]] — the architecture the paper describes (and the missing "last mile" to MediaWiki)
4. [[04 - Related Work and Landscape]] — STORM etc., low-resource precedents, Tibetan NLP, the cyclical-claim evidence
5. [[05 - Wikipedia Policy and Community Strategy]] — the rules, the failures to avoid, the bo.wikipedia plan
6. [[06 - Evaluation Plan]] — concrete small-N design achievable before August
7. [[07 - Roadmap to August]] — week-by-week
8. [[08 - Presentation and Demo Plan]] — talk structure, demo, Tibetan rendering pitfalls
9. [[09 - Reading List and Bibliography]] — every source with URL

## Immediate to-dos (this week — details in [[07 - Roadmap to August]])

- [ ] **Redact credentials** before anything is demoed or published: hardcoded Obsidian REST API key in `WeBuddhist/webuddhist-term-extractor-updated-SKILL.md` (line 27) and the previously-flagged WeBuddhist credentials in the rails plan-uploader.
- [ ] Email **iats2026@conftool.com** about AV/projector/wifi for the session.
- [ ] Post a public proposal on the bo.wikipedia village pump (see [[05 - Wikipedia Policy and Community Strategy]]).
- [ ] Pick the 12–15 article topics and verify each has at least one independent secondary source (see [[06 - Evaluation Plan]] and the notability warning about ཟབ་མོ་སྣང་བ། in [[05 - Wikipedia Policy and Community Strategy]]).
- [ ] Start logging time on every pipeline run from now on — the productivity numbers become the sustainability argument.
