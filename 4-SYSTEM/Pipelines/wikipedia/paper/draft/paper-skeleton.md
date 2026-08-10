# Paper skeleton — for review before drafting

**Working title:** *Expanding the Digital Footprint of Tibetan: A Semi-Automatic
Pipeline for Wikipedia Article Generation Using LLMs*

**Venue policy:** venue-neutral. No conference is named anywhere in the paper; no
"this audience knows this text" framing; no presentation/demo/slide material. The
paper must stand alone for any NLP, digital-humanities, or area-studies venue.
Length target ~11,000–12,000 words with §5 at full detail (a per-venue trim plan
is noted at the bottom).

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

## Front matter

- **Abstract slot (~200 w):** written last, venue-neutral. Shape: the gap (2
  sentences) → pipeline + case study (2) → the verification thesis (1) →
  measured results with numbers (2–3) → the cyclical implication (1). No venue
  names, no demo language.
- **Keywords:** Tibetan, low-resource languages, Wikipedia, large language
  models, grounded generation, citation verification, digital humanities.

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
- **Research questions**, stated so §8 can answer them one-to-one:
  - **RQ1 (fidelity):** can an LLM pipeline produce Tibetan encyclopedic text
    whose every quotation and locator is verifiably real — by construction,
    not by sampling? (Measured: yes on the pilot; batch pending.)
  - **RQ2 (layered verification):** what do independent verification layers —
    deterministic gate, cross-model audit, adversarial consolidation audit —
    catch that a single check, especially a same-model check, misses?
    (Measured: the paper's centerpiece results.)
  - **RQ3 (economics):** does supervised automation change the review-time
    arithmetic enough to make a small-language encyclopedia reachable within a
    generation? (**[TO FILL]** — the human legs.)

## §2 Related work (~900 w)

- **LLM-to-Wikipedia systems:** STORM/Co-STORM, WikiChat (25 languages, not
  Tibetan), WikiCrow (86.1% citation precision vs 71.2% human, 13.5% unsupported —
  keep the 9%-vs-13.5% metrics distinction straight), XWikiGen/OutlineGen. Gap
  claim: no published citation-aligned LLM article generation for Tibetan.
- **Attribution and grounding evaluation:** AIS-style "attributable to
  identified sources" protocols and citation-precision ratings (WikiCrow's
  numbers are rater judgments of *support*), positioned against this paper's
  character-level *fidelity* gate — stricter, narrower, complementary. The
  fidelity/support distinction is carried through §8, and the absence of any
  Tibetan NLI or attribution model (making support judgment manual by
  necessity) is itself a datum for §1's gap argument.
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

## §5 The pipeline (~4,500–5,000 w — the core section)

Opens with the design frame, then one subsection per stage. Fixed shape for
every stage so the section reads uniformly: **Purpose** (1–2 sentences) →
**Mechanism** (how it works, who does what) → **Quoted material** (the exact
prompt/code excerpt, named here so you can veto any of them) → **Example** (a
real artifact from the corpus) → **Numbers** (only measured ones).

### 5.0 Design frame (~250 w)

- Three principles, each restated at the stage where it bites:
  (1) *the model judges; the script verifies* — every stage ends in a
  deterministic gate that fails closed; (2) *isolation over context* — precision
  work is split into single-purpose subagent calls that see only their own input
  (one chunk, one node, one commentary, one topic packet); (3) *nothing
  interpretive touches the source layer* — sources receive only structure, under
  no-loss assertions.
- The stage-map table (T2): stage / skill / deterministic gate / artifact —
  14 rows, the section's roadmap.
- The two load-bearing invariants quoted verbatim from the canonical pipeline
  document: no source wording past the claims stage; nothing publishes without
  audit + review. "Everything else is replaceable machinery around those two
  rules."
- **The failure-class coverage table (T6)** — every known failure class
  (misquotation, citation fabrication, wrong locator, added fact, attribution
  loss, consensus flattening, silent claim loss, count errors, close
  paraphrase) × which layer catches it × the on-disk evidence it has actually
  fired. The paper's layered-defense argument in one view.
- **The human-checkpoint table (T7)** — every point where a human decides:
  cleaning-profile approval, segmentation residue (STAGE2_MANUAL), tree-QC
  ambiguity sign-off, term-list approval, rails `status: complete` promotion
  (human-only), pre-publication review, `--execute`. This is what
  "semi-automatic" means, made enumerable.

### 5.1 Cleaning (~250 w) — skill: `clean-raw-text`

- **Purpose:** strip mechanical OCR/PDF debris; change nothing else.
- **Mechanism:** profile-first — the skill profiles the raw text and reports the
  profile JSON to the human *before any change*; then generates and runs a
  bespoke cleaner limited to 8 mechanical transformations (page markers, running
  headers repeating >5×, U+0F0C→U+0F0B, mid-word spaces, orphaned-fragment
  joins, blank-line collapse). Verse lines (ending `།།` / `། །`) never collapse
  into prose. Ambiguous repeated lines are flagged and asked about, not removed.
- **Quoted material:** Rules 1–2 and 7–8 of the skill ("Never overwrite raw" /
  "Do not interpret text" / the U+0F0C rule "This is never ambiguous" / spaces
  deleted, not replaced); the cleaner's constants block (`PAGE_MARKER`,
  `MID_SPACE` regex over the Tibetan range, the verse-line heuristic).
- **Example:** the running-header false-positive caveat from the skill's worked
  run — headers stripped only as whole-line matches because the same string
  occurs legitimately mid-sentence as a title reference.
- **Stated non-goals:** no syllable repair, no restructuring — deferred to the
  format skills and the human edition (§4).

### 5.2 Normalisation (~200 w) — module: `tibetan/normalize.py`

- **Purpose:** one shared normalisation ladder so every downstream guarantee
  names which comparison it makes; stored text is never edited.
- **Mechanism:** four rungs — `nfc` (storage form) → `collapse` (minus
  whitespace; the verbatim-comparison key) → `strip_markup` (minus editorial
  furniture) → `fuzzy_key` (minus all shads/tshegs/head marks; a match here is a
  warning, never a pass). Every reduction returns an offset map back into the
  NFC text so matches report true positions.
- **Quoted material:** the module docstring (the ladder + "that drift is exactly
  how a citation ends up looking checked when it is not") and the six-character
  `FUZZY_DROP` set with its rationale (editions disagree about punctuation far
  more often than letters).
- **Numbers:** none — this stage's claim is *by construction*.

### 5.3 Segmentation (~400 w) — skills: `format-tibetan-root-text`, `commentary-segmentation`

- **Purpose:** make every verse and prose block a separately citable unit with a
  stable block ID, without altering one character.
- **Mechanism, root text:** a small grammar of Tibetan punctuation — `། །` as
  verse-line separator; the mid-verse-break regex (`(?<![།]) །(?=[^\s།])`) that
  splits two half-verses merged on one line; double-shad `།།` as a
  colophon-only marker used to find chapter boundaries; one block ID per stanza
  (`^chapter-verse`), headings `^N-0`. Two deterministic formatters
  (colophon-driven and table-driven).
- **Mechanism, commentaries:** a rule engine over seven lexical boundary cues —
  terminal particles (`འོ`/`ནོ`/`དོ`/`སོ`…+`།`), quote-close (`ཞེས་སོ། །`…),
  quote-open (`…ལས།`), enumeration-head (`…ལ་གསུམ་སྟེ།`), ordinal-open
  (`དང་པོ་…`), the objection pair (`…ཞེ་ན།`/`འོ་ན་…`), and a protected
  verse-stanza detector (2–4 uniform clause units of 6–11 syllables, peeled out
  whole, never re-cut). Target granularity 1–2 sentences (~40 syllables).
  Residue with no lexical cue goes to a human as `STAGE2_MANUAL`, whose hand-edit
  rules end "over-long is safer than wrong"; the overall bias is stated as
  "when in doubt, under-cut."
- **Quoted material:** the shad-grammar block; the seven boundary rules
  (condensed); the `assert_no_loss` function verbatim — output minus whitespace
  must equal input minus whitespace or nothing is written.
- **Example:** the `^1-1` stanza of the root text as segmented.

### 5.4 Structural annotation (~300 w) — skill: `tag-inline-toc` + the heading grammar

- **Purpose:** make the commentary's own inline structure announcements
  (sa-bcad) navigable — editorial headings whose IDs end in a reserved `-0`
  slot, and wikilinks wrapping each announced term so structure links to the
  section it announces.
- **Mechanism:** two phases with a hard boundary. Phase 1 is *model-only*
  meaning work — the skill forbids regex extraction and explains why (every
  surface rule spawns three exceptions). Phase 2 is *script-only* rendering:
  block IDs derived from depth by code (numbering bugs impossible by
  construction); wraps are exact substrings; the result is diffed back against
  the source and the run aborts on any prose change. "The model never retypes
  prose — it only points at substrings that already exist."
- **Quoted material:** the phase-1 rationale paragraph; the
  `verify_prose_unchanged` gate ("PROSE INTEGRITY VIOLATION"); a wikilink-tagged
  enumeration line.
- **Example:** the tenga-tulku commentary's seven-level heading chain
  (`^1-2-2-1-1-3-1-0`) — real depth, not a toy.
- **Design lesson kept:** this corpus forced a contract change — sa-bcad openers
  here are bare ordinals (`དང་པོ་ནི།`) recurring up to forty times per file with
  no unique substring, so line-number anchors had to be added; evidence that
  annotation contracts must be corpus-tested, not assumed.

### 5.5 TOC-tree extraction (~550 w) — skill: `toc-tree-extraction`

- **Purpose:** one QC-clean, decimal-numbered sa-bcad tree per commentary — the
  scaffold that claims extraction, spine mapping, and consolidation all lean on.
- **Mechanism:** an orchestrator dispatching four *isolated* passes, each a
  separate context that sees only its own prompt and input (the
  candidate-extraction call never sees tree-building instructions, so it cannot
  drift). Pass 0: deterministic chunking, 150 lines with 25-line overlap so
  every candidate appears whole in at least one window. Pass 1 (per chunk):
  section candidates of three types — announcement, node header, closing count —
  with the precision dial set explicitly ("when you are not confident … LEAVE IT
  OUT"). Pass 2 (per chunk): verbatim enumeration clauses under a strict
  START/STOP rule (stop at the closing particle; the sentence elaborating part
  one is body text and must not appear). Pass 3 (single subagent): build the
  tree, treating the author's own enumerations as *more authoritative than
  candidates* — used both to kill false positives and to fill structural gaps,
  with the counter-rule that doctrinal lists (content, not divisions) never
  become nodes; titles matched by meaning, not string equality; Tibetan ordinal
  must agree with the decimal's last segment.
- **The gate (pass 4):** two deterministic checkers, looped with fresh repair
  subagents until zero issues. Checker A (tree vs the model's own extraction
  corpus): structural invariants + three-tier title attestation (exact →
  ordinal-verified → syllable-bigram coverage ≥0.5, below which "possible
  hallucination"). Checker B (tree vs *the commentary itself*): pointer
  validity, title attestation within ±3 lines of its pointer, document-order
  monotonicity plus the repeated-pointer "lost cursor" signature (≥3 shared
  values), sibling-count congruence against the announcing text's own cardinal.
- **Quoted material:** the task-isolation rationale; pass 2's START/STOP rule;
  pass 3's authority-ordering paragraph; and checker B's docstring **in full** —
  the recorded failure where all three early trees passed checker A with zero
  issues while carrying a top-level misattachment, an unresolved anchor, and
  seven collided pointers. This is the paper's strongest evidence that
  self-consistency checking is insufficient and source-anchored checking is
  mandatory.
- **Example:** the tenga-tulku finished tree excerpt (7 levels, line pointers).
- **Numbers:** 16/16 commentaries have promoted QC-clean trees. One residual
  defect reported honestly: one tree's line pointers drifted because its source
  was re-stamped *after* QC ran — recorded inside the affected downstream file
  and flagged for human follow-up.

### 5.6 Alignment (~400 w) — skill: `Transclusion-rootext-into-commentaries` + module: `stages/align.py`

- **Purpose:** map every commentary span to the root stanza it explains — the
  step that decides which passages extraction is shown and makes every citation
  traceable to a verse.
- **Mechanism:** deterministic first, LLM only for the remainder, because
  "alignment errors are silent … deterministic matching can fail to find a
  verse, but it cannot invent a location." Layer 1, transclusion anchors:
  variant-tolerant quotation matching (character-overlap ≥0.80 absorbs
  orthographic variants like བསྒོམ/སྒོམ; full quotations beat passing
  citations; a single-line match needs a citation frame `ཞེས་པ་ནི།`), dry-run
  first, idempotent. Layer 2, lexical clustering for verses never quoted whole:
  each verse contributes probes (whole lines weighted 3.0, 9-char n-grams 1.0);
  densest windows of *distinct* probes are scored; one cluster per verse is
  chosen under a monotonicity constraint (commentaries follow their root text in
  order → score-weighted longest-increasing-subsequence). Any LLM-proposed span
  is re-verified to exist verbatim: "we accept its *judgement* about which
  passage is relevant, never its *reproduction* of the text."
- **Quoted material:** the deterministic-first rationale; `_monotonic_assign`'s
  docstring; the `verify_spans` docstring.
- **Numbers (all measured):** the recall fix on this corpus — 116→209 anchored
  verses (33%→59%) with three named root causes (a comparison against Latin
  transliterations that could never match; blank lines counted as mismatches; no
  incipit path). The benchmark P/R table (prose commentaries 95–96% precision at
  51–59% recall; the word-commentary 58%/19% — "structural, not a tuning
  problem": word-commentaries dissolve the stanza into glosses and genuinely
  never quote it). Final corpus state: **314 spans (209 anchor + 105 cluster),
  7/16 commentaries at 100% coverage**, the lowest being exactly the condensed
  and interlinear genres the documentation predicts.

### 5.7 Claims extraction (~500 w) — skill: `tree-guided-claims` (three methods compared)

- **Purpose:** convert commentary prose into atomic, block-cited claim rows —
  the layer everything downstream cites instead of source files.
- **Principle first:** *extract first, merge later.* Extraction reads one
  commentary in isolation; merge decisions made during reading are made with
  incomplete information ("the first commentary read silently defines the topic
  space").
- **Three methods compared** (table): fixed nine-category inventory
  (`commentary-claims`), TOC-scaffolded re-bucketing, tree-guided fresh
  extraction. Why tree-guided won — the comparison audit's findings, all
  quantified: the "second extraction" turned out to be a re-bucketing (**114 of
  118 Tibetan strings byte-identical** to the earlier run), claim counts copied
  rather than recomputed, transcription errors inherited, and the false framing
  hid real defects (a cross-document contamination; a fabricated mantra promoted
  to canonical status).
- **The five guards** (quoted, each with its measured origin): claim IDs never
  node IDs (5 collisions on one file); claim_count computed, never inherited;
  node-boundary placement by construction (each node read from its own line
  window alone); `(stated)` means the name is in *this claim's own* Tibetan
  (7/14 tags failed this on the old run); every claim independently re-derived.
- **Mechanism:** one isolated subagent per TOC node, given only the extraction
  rules, its node's line window, and its node's decimal+title — never another
  node's output, never another commentary's file. Claim IDs
  `c-<node-decimal>-<n>`. A per-commentary grounding index (FIG/PER/PLC/TXT/EVT
  entity tables, source-attested only) that `Referent:` fields point into, with
  basis tags `(stated)` / `(node)` / `(section-opener)` / `[unanchored]` —
  "a verdict, not a failure to try."
- **The gate:** `verify_claims.py`, four hard checks — quote containment
  (NFC+punctuation-normalised substring of the cited block; ellipsis fragments
  tested individually), claim_count recomputation, ID-collision scan,
  `(stated)`-referent validation. Repair by fresh per-node subagent; "never
  suppress a finding to make the count read zero."
- **Examples:** one real claim block (the མྱུར་མ gloss, c-1-1-4) and one real ⚑
  internal-tension block (the "seven worlds" double explanation, c-1-5-3).
- **Numbers:** 16 files, **2,975 claims** (62–368 per commentary), all
  `status: draft` — the LLM never marks its own extraction complete.

### 5.8 Spine maps (~300 w) — skill: `spine-map`

- **Purpose:** answer once per commentary: which of its own nodes (or claims)
  hold which canonical slot of the root text (tara-01…21, benefits, origin,
  structure) — so consolidation never re-derives routing.
- **Why it exists:** the pilot re-derived routing inside every topic run —
  "correct but quadratic in the wrong variable" (~400 full-file reads over a
  3.8 MB corpus vs 16 once-per-commentary judgments).
- **Mechanism & invariants (quoted):** routing only, never interpretation (the
  map records addresses, not doctrine); node numbering never assumed uniform
  (one commentary nests homages at `1.1.N`, another at top level, another
  titles by epithet, another runs all 21 in one undivided node); **every claim
  gets exactly one disposition** — mapped by node subtree, routed by claim ID,
  flagged ambiguous, or logged unmapped; neither zero (silent loss) nor two
  (silent duplication). Silence is a finding, recorded with a reason.
- **Example (the hard case):** tsultrim-namdak carries all twenty-one homages
  in a single undivided node, so its map routes by *claim-ID range*, using the
  extraction's own "Verse N quoted" claims as boundary markers — shown against
  a regular ordinal-titled row from karma-maitri.
- **Gate:** `verify_spine_map.py` — node existence, claim existence,
  disposition completeness, all counts recomputed, slot hygiene.
- **Numbers:** 16/16 maps exist.

### 5.9 Packet assembly, question generation, consolidation (~550 w) — script: `assemble_packet.py`; skill: `claims-consolidation`

- **Packet assembly is a script, not a model.** It collects one slot's claims
  from every commentary, copying each claim block character-for-character ("a
  script cannot mis-transcribe བོད་ཡིག" — this closed a whole error class the
  pilot audit found: silently elided syllables, normalized orthography), and
  emits a `## Manifest` of every claim ID included. Failures are loud: exit
  non-zero with named errors for a commentary with no disposition for the slot,
  or with claims but no spine map at all ("it is missing from this packet
  entirely") — quoted verbatim.
- **Questions are generated, not authored** (the methodology passage quoted in
  full): (i) a mechanical facet grid from the spine (21 homages × observed
  facets: name/etymology, colour, implements, stance, activity, mantra,
  benefit); (ii) claim-inversion — every distinctive claim in the packet becomes
  a question asked of all the others. The union is the question set, making
  consolidation a *derived completeness check*: free extraction first, generated
  questions catch what free reading missed. Real examples shown, one per kind,
  including a **negative-control question** ("Is lobsang-dawa's silence on this
  slot a real gap, or is the same content routed elsewhere?"). A question
  nobody answers is kept and marked, never deleted.
- **Consolidation:** one agent per topic, working only from the packet. Per
  facet: **Consensus** (with full per-commentary attestation lists) /
  **⚑ Divergences** (never flattened — vault hard rule) / **Unique**; plus a
  Coverage table where silence is itself a finding; citations always
  `registered_id:claim_id`.
- **Worked examples (all real):** the fifteen-commentary consensus on the
  origin narrative (Avalokiteśvara's tears → lotus → Tārā) with its attestation
  list; the "whose tears" divergence, where one side exists only as a
  commentator's report of unnamed "earlier commentaries"; and the
  དཔའ་མོ/དཔལ་མོ case — consolidation surfacing a *root-text-level variant
  reading* (two different etymologies licensed by one syllable), while
  flagging a second apparent witness as a probable transcription slip. This
  example carries the section's argument that consolidation is a philological
  instrument, not just an aggregator.
- **The coverage check:** manifest diffed against every claim ID the page
  cites; every gap either folded in or logged with a reason under "Claims
  reviewed, not separately cited" — "no third state." Caught real gaps in
  ~5–12% of mapped claims per pilot page.
- **Numbers:** 24 consolidated topic pages on disk, all `status: draft`.

### 5.10 Consolidation audits (~400 w) — script: `verify_consolidation.py`; skill: `claims-consolidation-audit`

- **The founding audit:** 2026-08-07, one fresh agent per pilot page, **every
  one of 418 unique citations** re-checked against the raw claims files.
  Headline: **zero fabricated claim IDs; 1 critical, 1 moderate, ~16 minor.**
  The critical case quoted in full — a real corpus idea attached to the wrong
  claim ID ("cited as independently corroborating … the raw claim contains no
  flaws framing"), the failure class no existence check can catch.
- **The taxonomy** (listed): partial-support padding of consensus lists; same
  claim on both sides of a divergence; page-level harmonizations presented as a
  claim's own reading; epistemic upgrades ("endorses" for a tentative སྙམ་མོ);
  silently elided syllables in quotes; hand-tallied count labels (**five of
  five wrong** on the worst page); consulted claims with no disposition.
- **Taxonomy → machinery (T4):** each error class became a rule (Rules 9–16:
  full-statement support; corroboration re-read, not remembered; one side per
  divergence; verbatim quotes or marked ellipsis; harmonization attributed to
  the page; epistemic strength copied, never upgraded; counts computed; every
  claim dispositioned) or a check in one of two standing gates.
- **Gate 1 (deterministic):** citation existence, per-paragraph count-label
  recomputation, both-sides overlap flags, disposition completeness, prefix
  discipline — "validated by reproducing every mechanical finding of the human
  audit, **plus one it missed**."
- **Gate 2 (adversarial):** a fresh context that did not write the page ("an
  agent auditing its own consolidation re-reads its own intentions, not the
  text"); ground truth is the raw claims file only — never the auditor's
  knowledge of the tradition; severity critical/moderate/minor; report-only;
  consolidator fixes, auditor re-checks; no critical or moderate finding may
  remain.
- **The `-bo` variant:** Tibetan-language twin pages under identical rules and
  both gates (bilingual anchor headings keep the deterministic checker
  parsing), with a strict independence rule — the Tibetan consolidator must not
  read the English counterpart — making the pairs a controlled comparison of
  consolidation quality by working language.

### 5.11 Article generation (~550 w) — both routes, on-disk inventory explicit

- **Term/topic selection precedes both routes and is a human gate.** Route A
  terms were machine-proposed by corpus keyness (frequency × distribution
  across the 16 commentaries) and are marked `status: candidate` in the term
  registry — no human has yet approved the list, and the registry records who
  (or what) proposed each entry. Route B topics come from the canonical spine
  (the 21 homages + the global slots). Existence is double-gated by §6's
  breadth doctrine and the independent-secondary-source requirement.
- *Route A (term articles):* the kwiki chain (extract → claims → outline →
  draft [→ polish] → audit). **Three articles exist and are verified** —
  སྒྲོལ་མ, འཇིག་རྟེན་གསུམ, སྡུག་བསྔལ (2026-08-02 run; drafts, claims tables,
  audit rounds, verify reports, ledger at `verified` all on disk). These carry
  the paper's headline numbers. The ~100-term corpus batch has NOT run —
  **[TO FILL]**, never implied otherwise.
  - The Tibetan extraction prompt's seven rules (one quoted verbatim:
    character-for-character quotation with the warning that a machine will
    check every letter; "add nothing from your own knowledge"; write
    "འགྲེལ་བཤད་མེད།" rather than invent).
  - The claims prompt: one verifiable fact per row in the pipeline's own
    Tibetan; a claim with no supporting passage must not exist; **synthesis
    forbidden** (no claim may require two sources combined); claim types
    weighted "by authority and response, not headcount" (a school's sole
    corpus representative is a school-position, never single-commentator).
  - **Claims-only drafting verified in code:** the drafting prompt receives
    outline + claims + glossary and nothing else; its closing line quoted
    ("you never write a ref or a URL"); `render_draft_payload` quoted — code,
    not the model, expands claim indices to passages and renders refs.
  - Voice rules by claim type (consensus may sit in neutral voice; everything
    below gets mandatory in-text attribution). The polish pass structurally
    fenced: output rejected by a code diff if any citations array, heading
    order, or paragraph count changed ("the stylist is never trusted with
    structure; that check is code, not prompt").
  - The audit stage: six finding categories; `AUDIT_BLOCKING` quoted — added
    facts and attribution loss block in code regardless of the model's verdict
    ("a model that lists an added fact and still says 'publish' is overruled by
    its own finding"). One real blocking finding shown (the dropped-qualifier:
    "three scholars" inflated to "many").
- *Route B (slot articles):* `wiki-article-from-claims` from consolidated topic
  pages. **Three articles exist** — tara-01/02/03 (citations.md trails 13/13
  and 8/8 quotation PASS; tara-01's trail missing, noted as a defect).
  - The fixed resolution chain: consolidated attestation → raw claim →
    **བོད་ཡིག** + block citation; an unresolvable attestation is dropped and
    logged, never guessed. Section headings "a menu, not a quota." Due weight
    follows attestation counts; ⚑ divergences presented per position, never
    adjudicated. The citations.md audit trail anatomy (reference map,
    unresolvables, warnings, per-quotation verification).
  - One real article lead (tara-02) shown as wikitext.

### 5.12 The deterministic verification gate (~400 w) — modules: `tibetan/verify.py`, `wiki/validator.py`

- **Purpose:** the blocking, LLM-free last line: every quotation re-read from
  the file it cites; every locator resolved; the output contract enforced.
- **Quoted material:** the three-tier docstring in full — exact (pass),
  collapsed (pass; "line wrapping is not part of the text"), fuzzy (**not** a
  pass; letters agree, punctuation doesn't), missing (fail) — ending "so
  `found` is not the gate: `passed` is." The reading-view function: the
  commentary with every ingest layer stripped back off ("not one Tibetan
  character touched"), because a faithful quotation must never fail "on a
  caret we put there ourselves." Block-locator resolution: the quotation must
  also appear inside the specific block its citation names.
- **The wikitext validator:** rules V1–V12 as a table, with the two
  target-wiki-specific rules explained — V4 (never `{{Reflist}}`: the local
  template injects its own heading; always `== ལུང་ཁུངས། ==` +
  `<references />`) and V10 (a tsheg must survive every `'''`/`[[` boundary —
  a Tibetan spelling error MediaWiki itself never surfaces). The validator's
  empirical base: of 677 sampled bo.wikipedia articles, 15% raw model dumps,
  75% uncited, ~126 with `<ref>` tags and nothing to display them.
- **The corollary, stated as policy:** articles are ***sic*-faithful** to the
  ingested edition. The gate once caught a model silently promoting a tsheg to
  a shad inside a quotation — similarity 0.974, invisible to a human skimming.
  Textual correction happens at the source layer (correct the edition,
  re-ingest, re-verify), never in the drafting model. No bypass flag exists;
  an audit "publish" verdict does not skip the gate.

### 5.13 Publication path (~250 w) — `kwiki publish`

- Nothing writes to the wiki without an explicit `--execute`; dry-run is the
  default on the client and every publish path. Publication refuses any term
  whose ledger state is not `verified` (state machine: pending → extracted →
  claimed → organized → drafted → audited → verified → approved → published).
- The pre-publication review checklist: every reference resolves; no
  sub-consensus position in neutral voice; no original synthesis; the topic's
  independent-secondary-source case restated.
- Community consent precedes content: the target wiki has no local policy on
  machine-assisted content and the project reads that vacuum as *stop* — a
  public bilingual proposal, an on-wiki project page naming every
  pipeline-assisted article and its reviewer, throughput bounded by review
  capacity, no mass creation.
- **Current status, stated plainly:** the three term articles sit at
  `verified`, one step short of `approved`; nothing has been published; the
  named blocker is the citation-URL debt (§7) — an article whose quotations a
  reader cannot check is the failure mode this pipeline exists to prevent.

### 5.14 Execution model and provenance (~250 w)

- One skill per step; immutable per-stage artifacts (`extract.json` →
  `claims.json` → `sections.json` → `draft.json` → `audit.json` →
  `article.wiki` + citations + verify report); every artifact overwrite now
  snapshots the prior version into `history/` — added after this run's audit
  rounds were found to overwrite one another, an evidence-preservation lesson
  reported as such.
- A per-article `model.json` records model ID, timestamp, and exact prompt
  version for every stage, including a logged `fix_passes` record of every
  post-audit edit — any published sentence traces to the model and prompt that
  produced it.
- Prompt-change discipline: a shipped prompt version is never rewritten in
  place — the canonical pipeline document is patched first, then the skill,
  then a *new* version file.
- **Models used in the reported runs, stated plainly (T5a):** pilot drafting /
  extraction / claims on claude-sonnet-5 (the sandbox stand-in route);
  cross-model audit on gemini-3.5-flash, with the same-model comparison run
  deliberately. The library is model-agnostic; the model asymmetry in Tibetan
  is reported as a finding (§8), not a design choice. 547 passing tests; the
  verification gate needs no API key and no network.

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
