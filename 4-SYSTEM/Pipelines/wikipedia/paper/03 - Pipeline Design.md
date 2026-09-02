# Pipeline Design — What the Paper Describes

The pipeline the paper presents is the Railroad citation chain extended by a "last mile" to Wikipedia. Stages 1–4 exist in the vault today; stage 5 is the pre-conference build. See [[02 - What We Already Have]] for what's on disk.

## The five stages

```
1. INGEST            2. STRUCTURE           3. EXTRACT             4. DRAFT               5. PUBLISH (new)
raw Tibetan text ──▶ block-ID'd digital ──▶ term × commentary ──▶ Tibetan article ──▶ MediaWiki wikitext
+ commentaries       edition, verse         tables, glossaries,    with layered           + external citations
                     context packages       raw cited passages     citations              + human review gate
                                                                                          + upload w/ disclosure
[library-data-       [2-authoritative-      [term-extractor        [wiki-creator          [to build]
 pipeline, ledger]    context, 2-RAILS]      skill]                 skill / drafting]
```

**Human checkpoints** (these make it "semi-automatic" — name them all in the talk):
- Ingest: two review checkpoints inside `/annotate`; deterministic lint before upload.
- Structure/Extract: read-only `1-Human-Sources`; verbatim-only extraction with block IDs; typed gap-notes instead of guesses; divergence flags (⚑) instead of consensus-flattening.
- Draft: no-parametric-knowledge rule — the LLM formats and phrases; interpretive authority stays with the cited commentary tradition.
- Publish: a named, fluent human line-edits, source-checks, and is the *sole publishing agent*. Human-only `status: complete`.

## Design principle 1: "Cite, don't copy" (licensing — this is load-bearing)

Wikipedia text must be licensable CC BY-SA 4.0. **None of our four canonical source repositories allows that for their text:**

| Source | Text license | Usable how |
|---|---|---|
| 84000 | CC BY-NC-ND 4.0 (translations) | **Citation only.** But glossary/metadata are CC BY 4.0 → ingestible |
| Lotsawa House | CC BY-NC 4.0 | Citation only |
| Treasury of Lives | Non-commercial full text; **metadata CC0** | Citation only (metadata ingestible); verify terms manually — site blocks robots |
| BDRC | Mixed: PD Mark on public-domain works; fair-use limited access on in-copyright | Citation + PD works; cannot waive copyright |

So the pipeline **generates original Tibetan prose over cited facts** (facts are not copyrightable) and never translates, closely paraphrases, or excerpts source text into articles. Classical root texts and commentaries that are public domain are the exception — but modern editions/translations of them often are not. Say this on a slide: it converts a vulnerability into a design feature, and it is exactly what "citation alignment, not text reuse" means.

## Design principle 2: Citations must be G15-proof by construction

English Wikipedia's G15 speedy-deletion criterion (adopted Aug 2025) deletes LLM pages showing fabricated/unresolvable references or leftover chatbot text. Regardless of bo.wikipedia's thinner rules, build the checks in:

- Every reference resolves (URL alive, BDRC/84000 ID valid, ISBN/DOI checks out).
- Citation metadata correct (author/title/date).
- The cited passage actually supports the sentence (manual spot-check protocol in [[06 - Evaluation Plan]]).
- No AI-generated sources, no open wikis as sources (Rigpa Wiki, Buddha-Nature, Tibetan Buddhist Encyclopedia are research aids, **not** citable references).
- ≥1 independent, reliable, *secondary* source per article (the WP:MASSCREATE standard, adopted voluntarily).
- Zero placeholder/meta text in output.

## The citation mapping (stage 5's core work)

Vault-internal block refs → external citable identifiers:

```
![[kunzang-pelden Done#^4-24]]   ──▶   <ref>{{cite book |author=Kunzang Pelden |title=... 
                                        |at=BDRC W... |...}}</ref>
```

Practical mapping targets, in order of preference:
1. **Published critical editions / academic literature** (books, journal articles) — strongest.
2. **BDRC** catalog IDs for classical texts (bibliographic authority; scans).
3. **84000** translation pages (stable URLs; peer-reviewed translations of Kangyur).
4. **Treasury of Lives** for biographical topics (peer-reviewed, 1,500+ biographies).
5. **Monlam Grand Tibetan Dictionary** (223 printed volumes — published lexicographic source) for lexical claims.

The rails frontmatter already has fields for external IDs — populate them once per source file, and every downstream citation inherits the mapping. That's a few hours of librarian work for the 16 Heart Sutra sources, not a research project.

## MediaWiki conversion (to build — small, deterministic)

A script (not an LLM) converting a finished vault article to wikitext: headers → `==`, wikilinks → internal links (red links are fine and useful), layered citations → `<ref>` with citation templates, reference list → `{{reflist}}`, plus an on-wiki disclosure template noting pipeline assistance and the human reviewer (Content Translation's trackability is the model). Keep the raw-transclusion appendix *out* of the published article; it stays in the vault as the audit trail.

## Topic selection policy (feeds [[06 - Evaluation Plan]])

- Start from the 79 extracted Heart Sutra terms — the machine layer is already built for them.
- Filter by **notability**: keep only terms with at least one independent secondary source (academic literature, Treasury of Lives, published encyclopedias). Flag: no independent secondary coverage was found for ཟབ་མོ་སྣང་བ། as a standalone topic — verify or swap it (see [[05 - Wikipedia Policy and Community Strategy]]).
- Prefer topics that are **red links or stubs on bo.wikipedia** (maximum marginal value; enables pairwise comparison against existing stubs in the eval).
- Mix core doctrine (སྟོང་པ་ཉིད།, བྱང་ཆུབ་སེམས།), figures (commentators — Treasury of Lives coverage), and texts (the Heart Sutra itself).

## What the pipeline is NOT (say this explicitly)

- Not machine translation of English Wikipedia (that's MinT/Content Translation — the incumbent, and weak for Tibetan: NLLB-200's Tibetan is near-zero quality, chrF ~2–7).
- Not mass generation (Lsjbot anti-pattern). Throughput is **bounded by review capacity, not model capacity** — publish only what a named fluent human has verified.
- Not autonomous. The human is not "in the loop" as a safety valve; the human is the *publisher*.
