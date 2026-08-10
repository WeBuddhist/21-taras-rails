# Paper skeleton — for review before drafting

**Working title:** *Expanding the Digital Footprint of Tibetan: A Semi-Automatic
Pipeline for Wikipedia Article Generation Using LLMs*

**Venue policy:** venue-neutral. No conference is named anywhere in the paper; no
"this audience knows this text" framing; no presentation/demo/slide material. The
paper must stand alone for any NLP, digital-humanities, or area-studies venue.
Length target ~8,000–10,000 words (a per-venue trim plan is noted at the bottom).

**One-line thesis:** grounded, citation-first LLM drafting plus mandatory human
review can turn a scattered commentarial corpus into durable encyclopedic content —
and the sign of the "AI content feedback loop" flips from doom spiral to virtuous
cycle *only* under that verification.

**Evidence base (all on disk today):** the reviewed 3-article pilot
(81/81 character-verified citations, cross-model audit), the rails corpus
(16 TOC trees, 2,975 claims, 16 spine maps, 24 consolidated topic pages,
418-citation consolidation audit), 3 slot-articles. Human-rater results and
reviewer-minutes remain **[TO FILL]** and every section that depends on them says so.

---

## §1 Introduction (~800 w)

- The digital gap, in numbers: bo.wikipedia ~8,000 articles / 31 active editors /
  2 admins vs 7M speakers; TLUE below-random LLM scores (GPT-4 17.5%); 4× tokenizer
  cost. One sentence each, all cited.
- The cyclical mechanism: Wikipedia as the largest per-language training source;
  the Welsh precedent for entering the cycle deliberately.
- The counter-evidence stated *up front*: machine content is currently destroying
  small-language wikis (Greenlandic closure, Scots, Cebuano). The paper's claim is
  not "automation helps" but "verification determines the sign of the loop."
- Case study announced: *Praise to the Twenty-One Tārās* + 16 commentaries —
  chosen as a bounded, well-commented classical corpus with a living interpretive
  tradition (venue-neutral framing; no audience-familiarity argument).
- **Contributions list** (bulleted, the reviewable core):
  1. A working end-to-end pipeline: raw OCR → cleaned, block-addressable sources →
     structural trees → atomic claims → consolidated topic pages → cited Tibetan
     wikitext, with a deterministic character-exact verification gate.
  2. A measured negative result about self-evaluation: a same-model audit passed
     drafts in which a cross-model audit found 5 blocking errors, 4 confirmed by
     hand.
  3. An adversarial-audit error taxonomy (418 citations checked) converted into
     executable consolidation rules and two standing gates.
  4. The claims database itself as a research artifact: 2,975 typed, school-tagged,
     block-located claims over a verse-aligned commentarial corpus.
  5. A transferable design pattern for under-resourced languages: model judgment
     everywhere, model authority nowhere.

## §2 Related work (~900 w)

- **LLM-to-Wikipedia systems:** STORM/Co-STORM, WikiChat (25 languages, not
  Tibetan), WikiCrow (86.1% citation precision vs 71.2% human, 13.5% unsupported —
  keep the 9%-vs-13.5% metrics distinction straight), XWikiGen/OutlineGen. Gap
  claim: no published citation-aligned LLM article generation for Tibetan.
- **Under-resourced-language Wikipedias:** the failure catalogue first (Scots,
  Cebuano/Lsjbot, Greenlandic closure, Inuktitut contamination; Thompson et al.
  2024 on MT-junk; Shumailov et al. 2024 on model collapse), then the working
  modes (Content Translation deletion rates, Welsh policy, Dzongkha education
  program, Masakhane). The one-variable difference: verification before
  publication.
- **Tibetan digital infrastructure:** BDRC, OpenPecha, ACIP, Adarsha, Lotsawa
  House — positioned as what the pipeline consumes, not duplicates.

## §3 Why automation at all: the three options (~600 w)

The argument, stated plainly — there are only three ways to grow Tibetan
Wikipedia to a useful size:

1. **By hand.** Measured at ~350 new articles a year; a serviceable encyclopedia
   is centuries away at that rate.
2. **Unsupervised automation** (bots / raw machine translation, no human review).
   Already tried on other small wikis; it destroyed them (Scots, Cebuano,
   Greenlandic — §2).
3. **Supervised automation.** Machines draft, code verifies every quotation, a
   human reviews and is the only one who publishes. This paper's pipeline.

The paper argues option 3 is the only demonstrated way to reach a useful
encyclopedia within a generation without destroying trust. The number that
proves or breaks it: minutes of human review per verified article vs hours of
writing per manual article, projected to a target encyclopedia size — machine
side measured (§8), human side **[TO FILL]**.

*(Decision taken: kept as its own short section; can be folded into §1 later if
a venue's page limit demands it.)*

## §4 Corpus and case study (~700 w)

- Root text as a **critical edition**: replaced the OCR export (wrong verse
  segmentation; missing benefits section); 17 of 21 homages differ between
  witnesses; superseded witness retained. Why this matters: the pipeline is
  *sic*-faithful downstream, so editing happens here or nowhere.
- The 16 commentaries: the sigla/author/school/genre table; the school skew
  (7 Geluk, 3 unattributed) named as data the pipeline must respect.
- Block-ID addressing (`^1-1`) as the corpus-wide citation primitive; one root
  stanza shown.
- Honesty note kept: the corpus currently exists in two annotated copies (rails
  conventions vs pipeline conventions), scheduled to unify.

## §5 The pipeline (~3,500 w — the core section)

Opens with the design-principles frame and the stage map table (stage / skill /
deterministic gate / artifact), then the two load-bearing invariants (no source
wording past the claims stage; nothing publishes without audit + review). Each
subsection = ~1 paragraph of prose + 1 verbatim prompt excerpt or code excerpt +
1 real corpus artifact. Everything below already exists in `paper-methods.md`;
drafting is mostly compression and de-IATS-ing.

- **5.1 Cleaning** — profile-first bespoke-cleaner design; 8 mechanical
  transformations; U+0F0C→U+0F0B; never overwrite raw.
- **5.2 Normalisation** — the four-rung comparison-key ladder (nfc / collapse /
  strip_markup / fuzzy_key); storage never edited.
- **5.3 Segmentation** — root-text shad grammar; commentary boundary rules; the
  `assert_no_loss` abort.
- **5.4 Structural annotation** — heading grammar (`^N-…-0`), inline sa-bcad
  wikilink tagging; "the model never retypes prose" + `verify_prose_unchanged`.
- **5.5 TOC-tree extraction** — four isolated passes (candidates / verbatim
  enumerations / tree build / QC repair); both deterministic checkers, including
  the recorded self-consistency failure that motivated the second checker.
- **5.6 Alignment** — transclusion anchors (0.80 threshold; measured 116→209
  recall fix) + lexical clustering with monotonic assignment; word-commentary
  structural limit; 314 spans on this corpus.
- **5.7 Claims extraction** — three methods compared; the five guards with their
  measured origins (114/118 byte-identical, 5 ID collisions, 7/14 false
  `(stated)`); claim format + one real claim + one ⚑ tension; `verify_claims.py`.
- **5.8 Spine maps** — routing without interpretation; exactly-one-disposition
  invariant; the coarse-tree hard case (claim-ID-range routing).
- **5.9 Question generation + consolidation** — deterministic packet assembly
  with loud failures; **questions generated, not authored** (facet grid +
  claim-inversion + negative controls, real examples); Consensus / ⚑ Divergence /
  Unique with the 15-commentary consensus and whose-tears divergence as worked
  examples; the manifest-diff coverage check.
- **5.10 Consolidation audits** — the 418-citation adversarial audit; error
  taxonomy → Rules 9–16 + two gates (deterministic + fresh-context adversarial);
  the Tibetan-language consolidation variant as a controlled comparison.
- **5.11 Article generation — both routes, with what exists today made explicit.**
  *Route A (term articles):* the kwiki chain (extract → claims → outline → draft
  [→ polish] → audit). **Three articles exist and are verified** — སྒྲོལ་མ,
  འཇིག་རྟེན་གསུམ, སྡུག་བསྔལ (2026-08-02 run; artifacts on disk: drafts, claims
  tables, audit rounds, verify reports, ledger at `verified`). These carry the
  paper's headline numbers (81/81, cross-model audit). The corpus-wide ~100-term
  batch has NOT run — marked **[TO FILL]**, never implied otherwise.
  *Route B (slot articles):* `wiki-article-from-claims` from consolidated topic
  pages. **Three articles exist** — tara-01, tara-02, tara-03 — with citations.md
  audit trails (13/13 and 8/8 quotation checks PASS; tara-01's trail missing,
  noted as a defect).
  Content: claims-only drafting verified in code (drafting prompt receives claims
  + outline only; code expands claim indices to passages and renders refs); voice
  rules by claim type; the fenced polish pass; the audit stage with code-enforced
  blocking categories; one real article lead from each route.
- **5.12 The deterministic verification gate** — exact/collapsed/fuzzy tiers
  ("found is not the gate: passed is"); the reading view; block-locator
  resolution; the 12-rule wikitext validator with the two bo.wikipedia-specific
  rules; *sic*-faithfulness and the tsheg→shad catch.
- **5.13 Publication path** — dry-run default; ledger states; pre-publication
  checklist; community-consent-before-content; paced rollout; nothing published
  yet, and why (citation-URL debt).

## §6 Editorial doctrine: breadth and reception (~700 w)

- Breadth decides existence (double-gated by independent secondary sources);
  reception decides weight (dgag-lan as machine-readable due-weight signal);
  sole-representative normalization (school-position, never fringe).
- The honest limit, kept prominent: this genre yields **zero** contested claims
  (0/47 pilot; no dgag-lan signal in 2,975 claims) — the doctrine is demonstrated
  structurally here, adversarially only on the Bodhicaryāvatāra corpus (7,279
  spans, ten commentaries) queued behind it.
- Framing for general venues: traditional scholastic citation/refutation practice
  operationalized as executable editorial policy.

## §7 Publication and data model (~500 w)

- Cite-don't-copy as the licensing design (no canonical Tibetan repository is
  CC BY-SA; facts over text; renderer-inserted verified quotations).
- Copyright routing (PD → Wikisource anchors; in-copyright → BDRC/library links).
- Current debt stated plainly: every citation still unlinked (W1/W2); articles
  are research artifacts in a review queue until the registry carries public URLs.
- The by-product argument: claims database + verse-aligned corpus survive
  regardless of what happens on-wiki.

## §8 Evaluation (~1,200 w)

Two scales + one rails-side audit; separate by-construction properties from
empirical ones throughout.

- **Citation fidelity (measured):** 81/81 character-exact, 81/81 locators
  resolve; byte-identical reproduction on a second machine. Fidelity ≠ support,
  stated explicitly.
- **The cross-model audit result (measured, the centerpiece):** same-model audit
  "publish ×3" vs cross-model 5 blocking findings on 2 articles; 4 confirmed
  genuine + 1 borderline (the four cases listed); fix pass logged with
  no-citation-changed assertion; auditor round-to-round variance (0.67/0.67/1.0)
  and auditor self-misquotation → report pass rates over repeated runs, never
  single verdicts; never report a same-model audit as independent.
- **Consolidation audit (measured):** 418 citations, 0 fabricated IDs, 1
  critical / 1 moderate / ~16 minor; taxonomy → executable rules; deterministic
  gate reproduced every mechanical human finding plus one the human missed.
- **Per-stage instrumentation (measured):** extraction capture is the one weak
  stage (45% / 19% / 1.1% against offer size; the 93k-vs-12k context experiment;
  the batching fix). Everything downstream is tight (100% quote-exactness at
  extract time, 100% passage utilization, 100% claim placement).
- **Pipeline statistics (measured):** 10–20 min/article; 81 passages → 47 claims
  (type distribution) → 81 citations; cost ≈ $0.33–1.42/article; lengths under
  target, reported as a known limitation.
- **[TO FILL] slots, clearly boxed:** corpus-batch distributions; native-speaker
  rater results (rubric, N raters); reviewer-minutes (the lead metric feeding
  §3's arithmetic); pairwise comparison vs existing stubs.

## §9 Discussion (~800 w)

- Ethics: each doom-spiral property negated by a named design choice; residual
  risk stated (a fluent reviewer can still wave through a subtly wrong article;
  close paraphrase not abolished in principle).
- Limitations from the artifacts themselves: sectarian skew; genre yields no
  reception signal; OCR bounds everything (*sic*-faithfulness corollary); model
  asymmetry in Tibetan; two-copy corpus duplication; slot-articles drafted from
  draft-status rails; one missing citations trail; one tree's pointer drift;
  methods 1–2 comparison not re-runnable from disk; evaluation's human legs
  pending.
- Generalization: nothing is Tārā-specific — root text + commentaries + registry;
  the pattern transfers to Sanskrit, Pali, classical Chinese scholasticism and to
  other low-resource languages with layered canons; the trilemma's third horn as
  the transferable design.

## §10 Conclusion (~350 w)

- The cycle, the sign, the gate. The durable deliverable is the reusable
  editorial machine + the claims database, not N articles.

---

## Planned tables and figures

| # | Item | Source |
|---|------|--------|
| T1 | The 16 commentaries (siglum, author, school, genre) | `paper.md` §4 table |
| T2 | Stage map: stage / skill / deterministic gate / artifact | `paper-methods.md` §5.0 |
| T3 | Cross-model audit adjudication (5 findings × verdict) | REVIEW-2026-08-02 |
| T4 | Consolidation-audit error taxonomy → rule/gate mapping | audit findings + Rules 9–16 |
| T5 | Evaluation summary (measured vs [TO FILL], two scales) | §8 sources |
| F1 | Pipeline diagram (ingest → rails → article → gate → publish) | to draw |
| F2 | One claim's full provenance chain: article sentence → ref → claim → block → source line | tara-02 artifacts |

## What gets deleted from the existing drafts (the de-IATS pass)

- The venue line, dates, and all "Kathmandu"/"seminar" references.
- "readers of this paper can judge the output against their own knowledge of the
  text" → replaced with a neutral corpus-selection rationale.
- All presentation/demo/slide references (§8's demo notes, QR codes, etc. never
  enter the paper).
- First-person revival-campaign storytelling in §3 → compressed to cited public
  bo.wikipedia statistics + a neutral statement that the authors ran editor
  training programs **[TO FILL: numbers]**, with the trilemma carried by the
  public numbers.

## Per-venue trim plan (not part of the paper)

- Full version: as above (~9k words).
- 8-page NLP-style version: cut §3 into §1, compress §6–7 to one section, move
  prompt excerpts to an appendix, keep §5 and §8 intact.
- Area-studies/DH version: keep §3 and §6 at full length, compress §5.1–5.4 into
  one "ingest" subsection, keep the claims/consolidation/audit stages detailed.

## Decisions taken (from review, 2026-08-10)

1. §3 stays its own section, written in plain language (see above).
2. **Both article routes**, with the on-disk inventory stated explicitly in §5.11
   (three verified term articles from the 2026-08-02 run; three slot articles;
   the ~100-term batch is [TO FILL]).
3. **No appendix**: prompts and code excerpts live in the body of §5, next to
   their examples, as in `paper-methods.md`. (An appendix only reappears as a
   trim option for page-limited venues.)

## Remaining question

- Author list / affiliation line — currently single-author, The OpenPecha
  Project; confirm or supply the final list.
