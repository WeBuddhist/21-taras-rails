# Expanding the Digital Footprint of Tibetan: A Semi-Automatic Pipeline for Wikipedia Article Generation Using LLMs

**Tashi Tsering — The OpenPecha Project** · tashitsering@dharmaduta.in
*Draft for the 17th Seminar of the International Association for Tibetan Studies, Kathmandu, 23–29 August 2026.*

> **Draft status (2026-08-02).** Built to the canonical structure in
> `10 - Canonical Paper and Slides Plan.md`. Every pipeline number in this draft comes from
> artifacts on disk in `corpora/tara21/` as reviewed in
> `corpora/tara21/REVIEW-2026-08-02.md`. Slots that require data only the team can supply
> (revival-campaign records, human rater results) are marked **[TO FILL]** — nothing in
> those slots is invented, and §8 says plainly which evaluation legs have run and which
> have not.
>
> **Revised the same day against two external reviews** (a ChatGPT pass and a Gemini
> pass): evidence scope stated in §1/§8/§10 (three-article case study, nothing yet
> published); fidelity vs. support vs. notability separated as distinct verifications
> (§5, §6, §8, §9); claim types glossed as corpus-relative (§5); the
> secondary-source/notability gate and the community-consent + maintenance plan made
> explicit (§6–7); OCR *sic*-faithfulness stated (§5, §9); close paraphrase named as a
> residual risk (§5, §9); fixed engineering cost acknowledged and the 100k-article
> projection widened to $35k–140k (§8); the 23-root-unit count clarified (§4, verified
> against `root.md` and `aligned.json`). TLUE and Welsh figures re-checked against
> `04 - Related Work` — both stand. The submitted title and abstract are unchanged by
> design (`abstract.md` is the record of what was promised).
>
> **Restructured for the corpus batch (same day).** §8 is now two-scale — a
> hand-adjudicated **pilot (N=3)** and a **corpus-wide batch** over the Tārā keyword
> list — so that no argument rests on three articles once the batch lands. Batch
> slots are marked **[TO FILL]** and enumerated in `batch-reporting-checklist.md`,
> which also lists the three prerequisites the batch needs (the local term list is
> down to the pilot's 3 terms and must be regenerated; no batch runner exists;
> the extraction tuning pass is still owed). Nothing in this draft reports a batch
> number that is not yet on disk.

---

## 1. Introduction

Tibetan is spoken by some seven million people and carries one of the largest classical
literatures in Asia, yet its digital footprint is out of all proportion to both facts. As
of July 2026 the Tibetan Wikipedia holds roughly 8,000 content articles — against
hundreds of thousands for comparable-population European languages — with about 31 active
editors in a given month, two administrators, and on the order of 350 new articles a year
(bo.wikipedia statistics, verified 2026-07-24). The consequences now compound in a new
place: large language models. On the TLUE benchmark, most large models score *below the 25%
random-guessing baseline* on Tibetan multiple-choice understanding — GPT-4 at 17.5%,
Qwen-2.5-72B falling from 84.7% in Chinese to 16.5% in Tibetan (TLUE, EMNLP 2025) — and
byte-level tokenizers make Tibetan text four times as expensive to process as Chinese
(Petrov et al. 2023). Ask a commercial AI assistant a basic question about Tibetan
culture *in Tibetan* and it fails, not because Tibetan knowledge is obscure, but because
the open digital text those systems learn from barely includes it. Kornai (2013) called
the endpoint of this trajectory *digital language death*; recent surveys of
under-represented mid-size languages call them "invisible giants" (Khanna & Li 2025).

The dynamic is cyclical, and that is the point of this paper. Wikipedia is, by the
Wikimedia Foundation's own account, "almost always the largest source of training data"
in a language model's corpus; per-language model performance correlates measurably with a
language's share of pretraining text (Language Ranker 2024; Glot500). A language with a
rich Wikipedia becomes a language that machines can serve — search, translation,
question-answering — which in turn lowers the cost of producing more content in it. A
language without one is locked out of the loop entirely. The cycle can be entered
deliberately: Wales did it as government policy from 2017, growing Wicipedia from 91,000
to over 280,000 articles precisely so that Welsh would be visible to technology
companies, and Welsh machine translation improved on the back of it.

This paper presents a working, semi-automatic pipeline built to enter that cycle for
Tibetan: from a root text and its commentaries to cited Tibetan-language Wikipedia
articles, with machine drafting bounded on every side by verification — and a human
editor, not a model, as the sole publishing agent. As a case study we run it over a text
this audience knows intimately: the *Praise to the Twenty-One Tārās*
(སྒྲོལ་མ་ལ་ཕྱག་འཚལ་ཉི་ཤུ་རྩ་གཅིག་གིས་བསྟོད་པ, Tōh. 438) together with sixteen Tibetan
commentaries spanning Sakya, Geluk, Jonang, Nyingma, and Kagyü authors from Drakpa
Gyaltsen to living teachers. The choice is deliberate: readers of this paper can judge
the output against their own knowledge of the text.

We are aware — and §3 makes it the paper's spine — that "AI content for small
Wikipedias" currently names a disaster, not a hope. The mechanism this paper celebrates
is the same one that filled small-language wikis with machine-translated debris and got
Greenlandic Wikipedia closed. Our claim is not that automation helps small languages. It
is that *the sign of the feedback loop is determined by verification*: unverified machine
content degrades the corpus and the models downstream of it; human-gated,
citation-audited content upgrades both. The pipeline exists to hold that line, and the
paper reports — including its failures — how the line held in practice. The scope of
the evidence is stated up front: a complete pipeline, a deeply-audited three-article
pilot, and a corpus-wide batch over the Tārā term list reported as distributions —
articles verified and audited but, as of writing, not yet published. These are early
outputs in the abstract's sense, not a revived encyclopedia.

## 2. Related work

**LLM-to-Wikipedia systems.** STORM (NAACL 2024) established the
research→outline→draft→cite architecture and the editor-rubric evaluation we borrow;
Co-STORM added the human steering the discourse. WikiChat (EMNLP 2023) demonstrated the
grounding filter — generate freely, keep only what retrieved sources support — reaching
97%+ factual accuracy in 25 languages, Tibetan not among them. WikiCrow (FutureHouse
2024) generated cited articles for all 15,616 unnamed human genes and showed machine
drafts can *out-cite* human baselines: 86.1% citation precision against 71.2% for human
Wikipedia articles in the 2024 PaperQA2 evaluation, with 13.5% of cited statements
unsupported (its December 2023 demo separately reported a 9% incorrect-statement rate —
a different metric from a different year). XWikiGen (WWW 2023) and OutlineGen are the
closest low-resource precedents, without citation grounding or a human loop. No
published system does citation-aligned LLM article generation for Tibetan; the
contribution here is the combination — a Class-0/1 language, retrieval-grounded cited
generation, hard verification, and a direct path to community publication.

**Wikipedia and under-resourced languages.** The honest half of this literature is a
failure catalogue, and we cite it before our reviewers do. Scots Wikipedia: ~23,000
articles by one enthusiastic non-speaker, credibility destroyed. Cebuano: six million
bot stubs and recurring closure proposals (Lsjbot). Greenlandic Wikipedia: *closed by
the Language Committee in 2025* over machine-generated content; Inuktitut estimated
two-thirds MT-contaminated; several African-language wikis at 40–60% uncorrected machine
translation (MIT Technology Review, Sept 2025). Thompson et al. (2024) found a startling
share of all low-resource web text is already multi-way machine-translation junk, and
Shumailov et al. (2024, *Nature*) showed models collapse when trained recursively on
synthetic data (with the nuance that *replacement*, not accumulation, drives collapse).
Against this: Content Translation articles — machine draft plus mandatory human edit —
show *lower* deletion rates than from-scratch articles across 2.4M+ creations, and
curated synthetic corpora approach real-data quality (Sangraha Synthetic, TransWebEdu).
The failure mode and the working mode differ in exactly one variable: verification
before publication. The positive precedents — Welsh policy, the Dzongkha Wikipedia
Education Program (dozens of participants, five months, ~80 new articles, fully manual;
the closest Tibetic-script effort and the effort-per-article baseline to beat), Masakhane's
participatory model — all keep speakers in charge of what ships.

**LLM-assisted encyclopedic writing risks.** Hallucination, citation fabrication, and
close paraphrase are the known failure classes; English Wikipedia's G15 speedy-deletion
criterion (Aug 2025) now deletes LLM pages with fabricated or unresolvable references on
sight. §5 and §7 describe how each class is answered *by construction* — including a
deterministic check no prompt can talk its way past.

## 3. Reviving Tibetan Wikipedia: the critical-mass argument

**[TO FILL — the lead's campaign records: workshops run, editors trained, retention.
The public-history reconstruction below stands on bo.wiki's own numbers and is citable
now; the first-person campaign numbers make it land and must come from the team.]**

We write this section in the first person because we have done the manual version of
this work. OpenPecha and its collaborators have run Tibetan Wikipedia editing workshops
and training programs **[TO FILL: counts, dates, cohort sizes]**; the public record of
bo.wikipedia shows what that mode of effort yields: roughly 350 new articles a year
since 2020, 31 active editors in a typical month, two administrators for the whole
project, and — eighteen years after founding — a total the size of a single English
WikiProject. The Dzongkha program's arithmetic is the same: institutional backing,
dozens of trained participants, five months, eighty articles.

At that rate, a minimally serviceable encyclopedia — call it 100,000 articles — is more
than two centuries away. This is not a criticism of the editors; it is the measured
capacity of the manual-only mode under real conditions.

The choice, then, is a trilemma:

1. **Manual-only.** We tried it; we measured it; it does not reach critical mass within
   a generation.
2. **Unsupervised automation.** Demonstrated at scale, and demonstrably catastrophic:
   Scots, Cebuano, Greenlandic (§2). It reaches volume by destroying the property —
   trustworthiness — that makes volume worth having, and it poisons the training
   corpora downstream.
3. **Supervised automation.** Machine drafting under hard verification, throughput
   bounded by review capacity, a named human as publisher.

We claim no demonstrated alternative to the third horn reaches critical mass within a
generation. The number that turns this from rhetoric into a finding is
**reviewer-hours per audit-passed article versus historical editor-hours per article,
projected to a target encyclopedia size** — the "generations collapse to years"
arithmetic. The pipeline's machine side is now measured (§8); the reviewer-hours side is
being measured with the August evaluation batch **[TO FILL: reviewer time logs]**, and
we report in §8 exactly which cells of that table are real today.

## 4. Corpus and case study

The corpus is the *Praise to the Twenty-One Tārās* — the root praise rebuilt from a
plain-text edition, cross-checked against an annotated edition, as the opening
invocation plus 22 stanzas (the 21 homages and the closing couplet), 23 alignable
root units in all, each with a stable block ID — and sixteen
commentaries totalling ~540,000 characters, from a curated dkar-chag supplied by the
team with titles, authors, genres, and school attributions:

| # | Siglum | Author | School | Genre |
|---|--------|--------|--------|-------|
| 1 | TARAC02_DGT | Jetsün Drakpa Gyaltsen | Sakya | rnam bshad |
| 2 | TARAC03_GDD | Gendün Drub (1st Dalai Lama) | Geluk | ṭīkkā |
| 3 | TARAC04_GDG | Gendün Gyatso (2nd Dalai Lama) | Geluk | rnam bshad |
| 4 | TARAC05_TRN | Tāranātha | Jonang | rnam bshad |
| 5 | TARAC06_NDB | Ngülchu Dharmabhadra | Geluk | rnam bshad |
| 6 | TARAC07_KTK | Könchok Tabkhé | Geluk | ṭīkkā |
| 7 | TARAC08_DTG | Dorlop Tenga Tulku | Sūryagupta lineage | commentary on benefits |
| 8 | TARAC09_ANON | anonymous (no colophon) | Sūryagupta lineage | bstod 'grel |
| 9 | TARAC10_DPN | Dombu Pema Namgyal | — | commentary |
| 10 | TARAC11_KMT | Karma Maitri | — | condensed commentary |
| 11 | TARAC12_PDS | Khenchen Palden Sherab | Nyingma | word commentary |
| 12 | TARAC13_TDZ | Sermé Tsang Geshé Tendzin Dönzang | Geluk | bstod 'grel |
| 13 | TARAC14_LZD | Geshé Lobzang Dawa (ed.) | Geluk | interlinear notes |
| 14 | TARAC15_SNT | Sangyé Nyentrul | — | word commentary + visualization |
| 15 | TARAC16_PSR | Draphar Dramé Sungrab Tulku | Geluk (contemporary, 2023) | rnam bshad |
| 16 | TARAC17_TSN | Khenpo Tsültrim Namdak | Kagyü | commentary |

The school composition is skewed — seven Geluk commentaries, one or two for each other
tradition, three unattributed — and §6 and §9 treat that skew as data the pipeline must
respect, not noise.

Ingest is deterministic and reproducible: conservative cleaning (NFC normalization,
U+0F0C→U+0F0B, page-number lines dropped — stored Tibetan punctuation is otherwise never
"fixed"), then segmentation through the production scripts of a sibling OpenPecha
pipeline, no-loss-gated. Re-running the ingest script reproduces every source file
byte-for-byte — a property we verified this week by rebuilding the corpus from the raw
upload on a second machine and obtaining byte-identical verification reports (§8).

Each commentary then receives the scaffolding that makes it *citable at passage level*:
sa-bcad heading tagging, root-verse transclusion anchors (which verse is being
commented on, marked in the file), and a stable block ID on every content block. A
deterministic aligner then maps every commentary span to the root stanza it explains:
**314 aligned spans over the 23 root units — 209 anchored by explicit verse
transclusion, 105 by lexical clustering — with seven of sixteen commentaries at 100%
coverage** (the lowest, at 52%, are precisely the condensed and interlinear genres the
aligner's documentation predicts). Alignment quality is not cosmetic: it determines
which commentary passages the extraction stage is shown for a given term, and the
anchors make every citation traceable to the verse being explained. The invariant that
makes the scaffolding safe is a *reading view*: every added layer must strip back off to
a byte-identical text, so verification never fails on a caret the pipeline itself wrote.

## 5. Pipeline architecture

The pipeline is seventeen steps in four layers — ingest, article generation,
publication, maintenance — designed by the team in a set of hand-off sessions and
implemented as a CLI (`kwiki`) over a tested Python library (546 passing tests), with
one skill per step for agent execution and versioned prompts whose provenance is
recorded per run. The article chain (steps 6–12) is where the distinctive ideas live.

**Atomic claims as the firewall.** After extraction pulls verbatim passages per term
from the aligned commentaries (with source ID and block locator on every passage), a
claims stage compresses them into an *atomic claims table*: one fact per row, in the
pipeline's own Tibetan words, each row carrying the passage indices that support it, the
commentator's school, and a claim type. From that point the sources are closed. The
drafting model sees the outline and the claims table only — never source wording — and
cites *claim indices*; code, not the model, expands each cited claim back to its
underlying passages and renders the references. Two invariants, stated as such:

> **Invariant 1.** No source wording reaches the drafting model. Quotations enter the
> article only from the extraction file, via deterministic rendering.
> **Invariant 2.** Nothing publishes without passing the audit *and* a deterministic
> verification gate; the blocking classes cannot be waived by any model verdict.

Invariant 1 is simultaneously the hallucination firewall (the drafter cannot misquote
what it never saw) and the copyright design: facts are not copyrightable, and of the
canonical Tibetan source repositories none licenses its text for CC BY-SA reuse — so the
pipeline *cites* sources and never copies them into articles. What look like quotations
in an article are renderer-inserted passages from the extraction record, each one
verified (below). We state the limit of this design as plainly as its strength: it
narrows the copyright surface rather than abolishing it. A claims table is still a
paraphrase of its sources, so close paraphrase remains possible in principle; the
audit reads for it, the pre-publication review checks that verbatim material from
in-copyright texts stays within short attributed quotation, and the human reviewer
owns the final judgment. Verification here is quotation fidelity and license routing,
not a legal guarantee.

**Claim typing and voice.** Every claim is typed — *consensus* /
*majority-with-dissent* / *school-position* / *single-commentator* — and the type
triggers voice rules in drafting: a consensus claim may speak plainly; a school position
must name its school; a single commentator must be attributed by name or described as
one commentary. All four types are corpus-relative — *consensus* asserts agreement
within this corpus of commentaries, not a verdict of the tradition at large — and the
audit polices exactly that boundary: the excerpt below is a corpus-level agreement
inflated toward a general one, caught and blocked. In the Tārā run, 47 claims
distributed as 13 consensus, 13 school-position, 21 single-commentator, and —
instructively — zero
majority-with-dissent: praise commentary (bstod 'grel) is simply not a polemical genre
(§6).

**Dual-model division of labor.** The design principle is that *the auditor never
writes*: reading-strength tasks (extraction, claims, audit) and writing are split so
that no model judges its own prose. The run reported here sharpened the principle into
a preliminary finding. The drafts were written by one model family (Claude); the audit
was then run twice — once by the same family, once by a different one (Gemini). The same-model audit
returned "publish, no findings" on all three articles. The cross-model audit found
**five blocking findings on two of the three** — and manual adjudication against the
claims table confirmed four genuine and one borderline (§8, Table 2). One audit-table
excerpt from the run:

> ⛔ **dropped-qualifier** — the draft's lead says "many different scholars agree"
> (མཁས་པ་མི་འདྲ་བ་མང་པོས་མཐུན་པར) where claim 0 says **three** named commentators agree
> (མཁས་པ་མི་འདྲ་བ་གསུམ་གྱིས) — a consensus exaggeration. *Same-model audit: not
> flagged. Cross-model audit: flagged, blocking. Human adjudication: genuine; fixed.*

**The deterministic gate.** Last in the chain, blocking, and LLM-free: every quotation
in the rendered article is re-read from the source file it cites and must match
**character for character** against the stored, NFC-normalized source text (the
comparison runs through the reading view, so the pipeline's own scaffolding
cannot cause a failure); every block locator is checked against the block it names; and
a 12-rule wikitext validator enforces the output contract. There is no bypass flag, and
an audit "publish" verdict does not skip it. In an earlier session this gate caught a
model silently promoting a tsheg to a shad inside a quotation — similarity 0.974,
invisible to a human skimming Tibetan prose, and exactly the class of drift that makes a
quotation no longer a quotation. No reviewer would have caught it; the gate did, by
construction. The strictness has a corollary we adopt deliberately: articles are
*sic*-faithful to the ingested source. A transcription or OCR error in the source is
reproduced in the quotation, never silently repaired — a model that "fixes" the text
it quotes is exactly what the gate exists to catch, and the tsheg-to-shad case is
that class. Textual correction is an editorial act for the source layer — correct
the edition, re-ingest, re-verify — never a liberty of the drafting model.

**Execution model.** One skill per step; immutable per-stage artifacts
(`extract.json` → `claims.json` → `sections.json` → `draft.json` → `audit.json` →
`article.wiki` + `citations.json` + verification report); a per-article `model.json`
recording model and prompt version for every stage — including, in this run, a logged
`fix_passes` record of every post-audit edit; and a resumable ledger per corpus. Prompt
changes follow a feedback rule: the canonical pipeline document is patched first, then
the skill, then a *new* prompt version file — never an in-place rewrite of a shipped
prompt, so any output can be traced to the exact prompt text that produced it.

## 6. Weighting doctrine: breadth and reception

Which concepts deserve articles, and how much voice each position gets inside an
article, are editorial questions. The pipeline operationalizes both from the corpus
itself.

**Breadth decides existence.** A term explained across many commentaries is
encyclopedic; a term one commentator happens to use is not. In the Tārā run, terms were
proposed statistically (frequency and distribution across the sixteen commentaries) and
carry that provenance in the term registry; the pilot's three terms are explained by
5, 16, and 10 distinct commentaries respectively, and the batch runs the same
breadth test across the whole candidate list. The registry marks all
machine-proposed terms as candidates pending human approval — term selection is a
curatorial act, and the pipeline records who (or what) proposed each entry. Breadth
is an editorial salience signal *within the corpus*; it is not notability in
Wikipedia's sense. A term all sixteen commentaries explain may still lack the
independent secondary coverage a standalone article needs, so existence is
double-gated: corpus breadth proposes, and the publication layer disposes — no
article is created without at least one independent, reliable, secondary source
identified for its topic (the English mass-creation standard, adopted voluntarily;
§7), with the human curator making the call.

**Reception decides weight.** Tibetan scholastic culture left a machine-readable
reception record: commentaries quote, endorse, and — crucially — refute one another.
The dgag lan (refutation-and-response) pattern is a due-weight signal: a position that
drew rebuttals from rival colleges has demonstrated historical weight even where it
lacks breadth; an idiosyncrasy nobody engaged gets a sentence. Every claim row carries a
reception field alongside its school tag, and the outline stage weights sections by
breadth × reception. The normalization rule matters in a skewed corpus: when a school
has exactly one representative in the corpus, that commentator's positions are typed
*school-position*, never *fringe* — sole representation is a fact about the corpus, not
about the tradition (the classic zhentong case).

The Tārā run also shows the honest limit of this doctrine: a praise-commentary corpus
generates **no reception-contested claims at all** (0 of 47). The genre explains and
extols; it does not refute. The dgag-lan machinery will earn its keep on the
philosophical corpora — the *Bodhicaryāvatāra* corpus already aligned behind this
pipeline (7,279 spans across ten commentaries, including the Ju Mipham exchanges that
are the textbook dgag-lan case) is where the weighting doctrine will be demonstrated at
full strength. Claiming the demonstration from this genre would be overclaiming; we
state the mechanism, the distribution it produced here, and where the contested case
will come from.

For this audience the point is larger than the mechanism: the pipeline treats
traditional Tibetan intellectual history — its citation practices, its polemical
literature, its school structure — as *editorial policy*, executable and auditable. The
claims database this produces (typed, school-tagged, reception-tagged, locator-carrying
rows over a verse-aligned commentarial corpus) is a Tibetan-studies research artifact in
its own right, independent of Wikipedia.

## 7. Publication and data model

Publication is where small-wiki damage happens, so the path is deliberately narrow.

**Nothing writes to Wikipedia without an explicit `--execute`.** Dry-run is the default
on the MediaWiki client and on every publish path; a dry run plans the edit, writes a
report, and touches nothing. Publication refuses any article whose ledger state is not
`verified`, runs a pre-publication review checklist (every reference resolves; no
sub-consensus position sits in Wikipedia's neutral voice; no sentence draws a
conclusion that requires combining sources — the original-synthesis class; and the
topic's independence case is restated), targets a userspace sandbox before
mainspace, and carries an edit summary disclosing pipeline assistance and linking a
project page — the Content Translation disclosure model, adopted voluntarily. Throughput
is bounded by review capacity, not model capacity: paced publication, no mass creation
(the WP:MASSCREATE standard adopted as policy even though bo.wikipedia's local rules are
thinner). Every citation resolves or the article does not ship (English Wikipedia's G15
now deletes fabricated-reference pages on sight; we build to that bar by construction —
and the Tārā run does not yet clear it, which is one reason its articles remain
unpublished; below).

**Community consent precedes content.** bo.wikipedia has no local policy on
machine-assisted content, and we read that vacuum as *stop*, not as permission: the
global bot policy the wiki adopted requires local community approval for automated
contribution, and a wiki too small to convene a consensus is a reason for more
restraint, not less. Before any mainspace edit, the plan of record is a public,
bilingual proposal on the bo.wikipedia village pump — scope, method, named reviewers,
an explicit invitation to object — posted under an account with disclosed project
affiliation; an on-wiki project page listing every pipeline-assisted article with its
reviewer and sources; and a standing invitation to the wiki's active editors to join
as reviewers and raters, so that approval authority sits with the community the
encyclopedia belongs to. Articles, once published, are maintained through the
pipeline's update path, which never rewrites existing article text: new claims are
inserted, disagreements between the live article and the corpus are flagged for a
human, and new quotations pass the same character-exact gate as on first publication.

The output contract is a versioned wikitext specification enforced by the validator —
down to details learned from live renders: bo.wikipedia's `{{Reflist}}` template injects
its own heading, so the pipeline always emits `== ལུང་ཁུངས། ==` ("Sources cited") with a
bare `<references />` (the Reflist idiom is correct on English Wikipedia, which is
exactly why a model reaches for it; the validator makes the mistake impossible).

**The data model routes by copyright.** The source registry carries author dates and a
copyright status per text, populated via a BDRC metadata fetcher: public-domain texts
queue for Tibetan Wikisource with per-verse anchors, so a citation deep-links to the
passage; in-copyright texts cite to BDRC or WeBuddhist library links. The honest current
state of the Tārā corpus: **every citation the pipeline has produced from it is still
unlinked** — the dkar-chag's only URLs are Google Drive scans, which the citation
resolver correctly refuses. This is a property of the registry, not of any one run, so
generating more articles does not improve it and the batch inherits the debt whole.
Until the registry carries public URLs, a reader can verify quotations only
against the physical editions — which is why these articles are
research artifacts in a review queue, not published pages: the first check of the
pre-publication review lists every URL-less reference, and mainspace publication
waits on the registry (BDRC IDs per commentary, Wikisource anchors for the
public-domain texts), because an article whose quotations a reader cannot check is
the failure mode this pipeline exists to prevent.
The Wikisource and Wikidata legs (works, authors, concepts round-tripped as structured
data) are designed and not yet implemented; every article already leaves behind its
by-product regardless — the claims table, citations with block locators, and a
verse-aligned corpus, all queryable.

## 8. Evaluation

The abstract promises evaluation of early outputs. Evaluation here runs at two scales,
and the distinction matters for what each can support:

- **The pilot (N=3, complete and reviewed).** Three terms from the Tārā corpus
  (སྒྲོལ་མ *Tārā herself*, འཇིག་རྟེན་གསུམ *"the three worlds,"* སྡུག་བསྔལ *"suffering"*),
  run end to end with every intermediate artifact preserved and every audit finding
  hand-adjudicated. Three articles cannot carry a rate, but this depth is what
  exposed the cross-model audit result below — the kind of finding a batch reports
  in aggregate and cannot explain. The pilot is reported in full because the audit
  trail *is* the evidence.
- **The corpus batch (N = [TO FILL], in flight).** Every keyword the term-extraction
  route surfaces from the Tārā corpus — on the order of a hundred candidate terms —
  run through the same chain, reported as distributions rather than narratives:
  gate pass rate, audit pass rate over repeated runs, extraction capture, article
  length, cost and wall-clock per article. **[TO FILL: batch N, per-metric
  distributions — see `batch-reporting-checklist.md` for the exact slots.]**

The batch answers scale; the pilot answers mechanism. We are explicit throughout about
which planned metrics have data today and which are pending, and we separate the
properties that hold *by construction* (and so do not wait on large N) from the ones
that are *empirical* (and do). Design for the human legs follows the small-N norms of
the field (STORM's flagship study was 20 article pairs × 2 raters): three named
native-speaker raters drawn from active bo.wikipedia editors and Tibetan-studies
institutions, a 7-dimension rubric, an AIS-style citation audit on a stratified sample
of the batch, pairwise comparison against existing bo.wiki stubs, and productivity logs
that include a from-scratch writing-time control by the same editors. Human rating
samples the batch; it does not scale with it — which is the paper's point about where
the real constraint sits. **[TO FILL: rater results, reviewer-minutes, pairwise
outcomes.]**

**Pipeline statistics — pilot (measured, on disk).** Three articles, generated
end-to-end in roughly 10–20 wall-clock minutes each (ledger timestamps): 81 extracted
passages → 47 atomic claims (13 consensus / 13 school-position / 21
single-commentator / 0 majority-with-dissent) → 81 rendered citations; 5, 16, and 10
distinct commentaries cited per article; all 16 commentaries cited at least once
across the three. Article lengths 642–1,358 tshegbar — all below the 1,500 target, a
known extraction-volume limitation under active tuning, reported as such.

**Pipeline statistics — batch. [TO FILL]** The same table over the full candidate
term list: N articles attempted, N reaching `verified`, and the distribution of
claims per article, claim types, distinct commentaries cited, and article length.
Two distributional questions the pilot cannot answer and the batch can: how often
the deterministic gate fails a first draft (the pilot's per-run gate failure was
observed in an earlier session, not this one), and whether the zero
majority-with-dissent result is a property of the genre or of three lucky terms.

**Per-stage instrumentation.** A stage-evaluation harness
(`scripts/eval_stages.py`, report in `work/eval/`) now measures each step against
what the previous step offered it, and it localizes the pipeline's weakness
precisely: **extraction capture**. In the pilot, alignment offered 18k, 41k, and 165k
characters of commentary for the three terms; extraction captured 45%, 19%, and
**1.1%** respectively — the model visibly budgets its answer against the size of the
question (the largest offer got the *least* material). Everything downstream of
extraction is
tight: 100% of extracted quotes are character-exact at extract time, 100% of passages
are used by at least one claim, zero claims dropped at parse, 100% of claims placed by
the outline and cited in the draft, and every paragraph carries at least one citation.
The tuning problem is one stage wide, and it is measured. The batch turns that
three-point observation into a curve — capture rate against offer size across the
whole term list **[TO FILL]** — which is the form in which it can actually be tuned
against, and we report it whether or not the tuning pass lands before publication.
What the harness measures
is flow, not truth: it cannot say whether an aligned span genuinely explains its
stanza, whether a claim's type and school tag are right, or whether a passage means
what its claim says. Those are judgment calls — sampled by hand in this run's
adjudication (below) and assigned to the rater batch — and the harness's job is to
localize where that human attention is needed, not to replace it.

**Citation verifiability (measured, on disk — the strongest form).** Across the
pilot's three articles the deterministic gate re-read every quotation from its cited
source file: **81 of 81 character-for-character
exact; 81 of 81 block locators resolve to the named block, none wrong** — with the
batch extending this to **[TO FILL: N quotations across N articles]**, the figure
that turns a clean pilot into a rate. This measures
a different thing than the statement-support rates reported for English systems —
WikiCrow's 86.1% citation precision is a rater's judgment that a source supports a
statement; ours is character-level identity of the quoted evidence. Fidelity, not
support: the gate proves the quoted evidence is real and correctly located, never that
it warrants the sentence citing it. It is also *reproducible*: the corpus was
rebuilt from the raw upload on a second machine and the verification reports came back
byte-identical. The AIS-style *statement-support* audit — does the cited passage support
the prose claim — is the audit stage's job (below) plus the human batch
**[TO FILL]**; no NLI model supports Tibetan, so it is manual by necessity, which is
itself a datum for §1.

**The audit, and a result we did not plan (Table 2).** The run's drafts were audited
twice. Same-model audit: "publish, no findings," three for three. Cross-model audit:
five blocking findings on two articles. Manual adjudication against the claims table:
four genuine — a consensus exaggeration ("many scholars" for three), an
overgeneralization ("a name for *each* verse" where four are attested), a technical-term
shift (མཚན་ཉིད for མཚན་དོན), and an attribution asserted beyond its claim (naming Gendün
Drub where the claim deliberately said "one commentary" — factually right by luck, and
exactly the class that must block, because next time it is wrong) — plus one borderline
(prose stating "none dispute it" where the claim's reception metadata says uncontested
but its text does not). Six surgical edits later — each logged in the article's model
record, with a code assertion that no citation changed — the cross-model audit returns
publish with zero findings on all three, and the gate still passes. Two further
observations belong in any honest report: the auditor shows round-to-round variance —
measured directly by re-auditing the final, fixed articles three times each: pass rates
of 0.67, 0.67, and 1.0, the dissenting runs each raising a single borderline finding —
which is why audit outcomes are reported as pass rates over repeated runs rather than
single verdicts (and why an audit-prompt revision is scheduled); and twice the auditor
*misquoted the draft inside its own finding*,
inventing a typo the draft does not contain — model-written finding text is itself
untrusted, which is why the blocking decision keys on categories and why the
deterministic gate, which cannot hallucinate, sits beneath the audit. The two layers
catch disjoint failure classes: the audit reads meaning (paraphrase drift, weight
inflation), the gate reads characters (quotation integrity). Neither substitutes for
the other, and the same-model audit substitutes for neither. On sample size we are
strict with ourselves: the pilot's three articles and four audit rounds are an
existence proof, not a rate estimate — they establish that a same-model audit *can*
return publish on drafts in which an independent model finds five blocking problems,
four confirmed by hand. That is enough for the design lesson (never report a
same-model audit as independent) and not enough to claim cross-model auditing
dominates in general; the batch's audit pass rates **[TO FILL]** are what would begin
to support the stronger claim, and we will report them as rates over repeated runs
per article, with the same-model comparison run on a stratified subsample rather
than assumed.

**Attribution integrity (measured).** Of the pilot's 34 sub-consensus claims, the
drafts' attribution survived audit on all but the two cases above; both were caught
before publication, and zero attribution errors remain in the verified articles.
Batch: **[TO FILL — attribution-loss findings per 100 sub-consensus claims]**, the
form in which this becomes a rate rather than an anecdote.

**The lead metric.** Reviewer-hours per audit-passed article versus historical
editor-hours, projected to target size — the §3 arithmetic — requires the human review
logs from the August batch **[TO FILL]**. What this run establishes is the machine
side of the fraction, now measured rather than asserted (full working in
`cost-and-scalability.md`): in the pilot, 22 model calls and ~435k input / ~85k output
characters for three articles, costing **roughly $0.33–1.42 per article** at current
Gemini Flash prices (central estimate ≈ $0.71, before caching and batch discounts;
≈2× on claude-sonnet-5 rates), in 10–20 wall-clock minutes each; the batch replaces
this estimate with a measured per-article distribution **[TO FILL]**, including the
retry factor that a three-article run cannot see. Projected, the machine cost
of a 100,000-article encyclopedia is on the order of **$35k–140k depending on
tokenizer behavior and batching (central ≈ $70k)** — one project grant, one-time, on
falling prices. That figure prices the marginal article, not the system: building
the pipeline and bringing a corpus into it — cleaning, segmentation, alignment,
registry curation — is skilled up-front engineering, and the fair comparison is that
this fixed cost amortizes across every article and every corpus the machinery
touches, where manual writing has no fixed-cost term to amortize. The scarce input is
human review, by design
("throughput bounded by review capacity"): at an assumed 30–60 reviewer-minutes per
article, the same 100,000 articles is 24–48 person-years of review spread across a
community — against ~285 years of *writing* at the manual-only baseline rate. That is
"generations collapse to years" in arithmetic; the reviewer-minutes assumption is the
one number the August batch must replace.

**Community reception.** Nothing has been published to bo.wikipedia yet — the review
gate and the citation-URL debt come first. This is a deliberate sequencing, and the
paper prefers a smaller honest table to a larger premature one.

## 9. Discussion

**Ethics.** The doom-spiral evidence (§2) is about *unaccountable volume*: content
nobody fluent verified, at rates nobody could review, with no disclosure. Every design
choice in this pipeline is the negation of one of those properties: a named human
publisher, throughput bounded by review, on-wiki disclosure, verification that is
deterministic where possible and adversarial (cross-model) where not, and an audit
trail from every published sentence back through claims to block-located passages. We
state the residual risk plainly: a fluent reviewer can still wave through a subtly
wrong article; the pipeline reduces the surface a reviewer must distrust — quotations
are machine-guaranteed; judgment calls are flagged and typed — it does not abolish
editorial responsibility, and is not meant to.

**Limitations.** The corpus is sectarian-skewed (7 of 16 commentaries Geluk; three
unattributed) and the weighting doctrine can only normalize what the registry records.
The case-study genre yields no contested claims, so the reception machinery is
demonstrated structurally, not adversarially — the Bodhicaryāvatāra corpus is the real
test. OCR quality upstream bounds everything — and the gate makes articles
*sic*-faithful to whatever the ingested text says (§5), so textual correction is a
curatorial prerequisite, not something the pipeline improvises. The model asymmetry in
Tibetan is real and measured (an extraction model returns a third of the material when the context
grows large — the run's extraction batching exists because of it), and both drafting
and auditing in Tibetan currently ride on models trained mostly on other languages —
the cyclical argument of §1, felt from inside the pipeline. Evaluation is partly
pending: the machine-side batch reports distributions, but the human legs — rating,
citation-support judgment, reviewer time — sample it rather than covering it, so
every claim that depends on human judgment rests on a small annotated subset by
design. Scaling the machine does not scale the reviewing, which is the paper's own
thesis turned on its evaluation. And the
verification the pipeline automates is deliberately the narrow kind: quotation
fidelity, locator correctness, contract compliance. Whether a cited passage supports
its sentence is the audit's reading plus the pending human legs; whether a topic
merits an article at all is a human, policy-bound decision (§6–7); and claims-only
drafting narrows the copyright surface without abolishing close paraphrase in
principle (§5). None of these caveats is a footnote to the thesis; they are the
thesis — the machine does the checkable parts, and the judgment stays human.

**Generalization.** Nothing in the architecture is Tārā-specific: it requires a root
text, commentaries, and a curated registry. The same machinery is already aligned over
the Bodhicaryāvatāra (ten commentaries), and the pattern — layered canon, commentarial
tradition, school structure — is the shape of Sanskrit, Pali, and classical Chinese
scholasticism too. For under-resourced languages generally, the transferable design is
the trilemma's third horn: machine volume, human authority, verification as the hinge —
with the claims database, not the article count, as the durable asset.

## 10. Conclusion

The cycle this paper set out to enter — articles → digital footprint → training
data → better tools → faster articles — is running today in the wrong direction for
Tibetan: absence begetting absence, and, on other small wikis, machine junk begetting
model junk. We have shown a working pipeline built to flip that sign, and the first
evidence that it can: Tibetan articles on a text this audience can check — a
hand-adjudicated pilot and a corpus-wide batch behind it — every quotation
character-verified against its commentary, every claim typed and school-tagged, every
edit logged, audited by a model that did not write the text, and published — when it
publishes — by a person. The per-article artifacts are small; the machine they came
from is not: a reusable editorial system whose every safeguard is a testable invariant,
and a growing claims database over the commentarial tradition that is a research
object for this field regardless of what Wikipedia becomes. The gap the abstract named
is real and cyclical; the answer, on this evidence, is neither refusal nor flood, but
verification with a human hand on the gate.

---

*References: consolidated with URLs in `09 - Reading List and Bibliography.md`; formal
bibliography formatting is deferred to the camera-ready pass. Run artifacts:
`corpora/tara21/` (articles, claims, audits, verification reports, model provenance),
reviewed in `corpora/tara21/REVIEW-2026-08-02.md`.*
