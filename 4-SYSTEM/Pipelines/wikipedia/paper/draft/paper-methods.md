# Expanding the Digital Footprint of Tibetan: A Semi-Automatic Pipeline for Wikipedia Article Generation Using LLMs — full methods draft

**Tashi Tsering — The OpenPecha Project** · tashitsering@dharmaduta.in
*Draft for the 17th Seminar of the International Association for Tibetan Studies, Kathmandu, 23–29 August 2026.*

> **Draft status (2026-08-10).** This is the **methods-expanded companion** to
> `paper.md` (the canonical draft of 2026-08-02, revised same day against two external
> reviews). It does not replace that draft: §§1–3, 6, 9–10 here are abridged from it and
> its calibrated claims stand. What this version adds is the thing the canonical draft
> compresses into two pages: **§5, the pipeline stage by stage** — cleaning,
> normalisation, segmentation, structural annotation, TOC-tree extraction, alignment,
> claims extraction, spine mapping, question generation, consolidation, the two
> consolidation audits, article generation, the deterministic verification gate, and
> publication — with the skill that executes each stage, the load-bearing prompt text
> verbatim, the decisive parts of the deterministic scripts, and a real artifact from
> the 21-Tārās corpus at every step. Every number is from artifacts on disk
> (`corpora/tara21/REVIEW-2026-08-02.md`; `2-RAILS/`; `0-INBOX/claims-audit-findings-2026-08-07.md`).
> Slots only the team can fill — revival-campaign records, human-rater results,
> reviewer-minutes — remain **[TO FILL]**, exactly as in the canonical draft.

---

## 1. Introduction (abridged — full argument in `paper.md` §1)

Tibetan is spoken by some seven million people and carries one of the largest classical
literatures in Asia, yet the Tibetan Wikipedia holds roughly 8,000 content articles,
with ~31 active editors a month and two administrators (verified 2026-07-24). The
consequence now compounds inside language models: on the TLUE benchmark most large
models score *below the 25% random baseline* on Tibetan (GPT-4: 17.5%), and byte-level
tokenizers make Tibetan roughly four times as expensive to process as Chinese. The
dynamic is cyclical — Wikipedia is usually the largest source of per-language training
text, so a language without one is locked out of the loop — and the cycle can be
entered deliberately, as Wales did from 2017.

This paper presents a working, semi-automatic pipeline built to enter that cycle for
Tibetan: from a root text and its commentaries to cited Tibetan-language Wikipedia
articles, with machine drafting bounded on every side by verification and a human
editor, not a model, as the sole publishing agent. We are aware that "AI content for
small Wikipedias" currently names a disaster, not a hope (Scots, Cebuano, Greenlandic —
§2). Our claim is not that automation helps small languages; it is that **the sign of
the feedback loop is determined by verification**: unverified machine content degrades
the corpus and the models downstream of it; human-gated, citation-audited content
upgrades both. The scope of the evidence is stated up front: a complete pipeline, a
deeply audited three-article pilot on the *Praise to the Twenty-One Tārās*, a
rails-side consolidation corpus of 24 topic pages over 2,975 extracted claims, and
three further slot-articles drafted from them — verified and audited but, as of
writing, **nothing yet published to bo.wikipedia**.

## 2. Related work (abridged — full treatment in `paper.md` §2)

STORM (NAACL 2024) established research→outline→draft→cite; WikiChat (EMNLP 2023) the
grounding filter, in 25 languages, Tibetan not among them; WikiCrow (FutureHouse 2024)
showed machine drafts can out-cite human baselines — 86.1% citation precision against
71.2% human in the 2024 PaperQA2 evaluation, with 13.5% of cited statements unsupported
(its December 2023 demo separately reported a 9% incorrect-statement rate — a different
metric from a different year). No published system does citation-aligned LLM article
generation for Tibetan. The failure literature — Scots, Cebuano's six million bot
stubs, Greenlandic's 2025 closure, Thompson et al. (2024) on MT-junk saturation of
low-resource web text, Shumailov et al. (2024, *Nature*) on model collapse — differs
from the working mode (Content Translation's lower deletion rates, Welsh policy, the
Dzongkha education program) in exactly one variable: verification before publication.

## 3. Reviving Tibetan Wikipedia: the critical-mass argument (abridged)

**[TO FILL — the lead's campaign records: workshops run, editors trained, retention.]**
The manual-only mode is measured at ~350 new articles a year; a serviceable
encyclopedia is more than two centuries away at that rate. The choice is a trilemma:
manual-only (measured; does not reach critical mass in a generation), unsupervised
automation (demonstrated, and demonstrably catastrophic), or supervised automation —
machine drafting under hard verification, throughput bounded by review capacity, a
named human as publisher. The number that turns this from rhetoric into a finding is
reviewer-hours per audit-passed article versus historical editor-hours, projected to a
target encyclopedia size (§8).

## 4. Corpus and case study

The corpus is the *Praise to the Twenty-One Tārās*
(སྒྲོལ་མ་ལ་ཕྱག་འཚལ་ཉི་ཤུ་རྩ་གཅིག་གིས་བསྟོད་པ, Tōh. 438) and sixteen Tibetan
commentaries (~540,000 characters) spanning Sakya, Geluk, Jonang, Nyingma, and Kagyü
authors from Drakpa Gyaltsen to living teachers (the full table with sigla, schools,
and genres is in `paper.md` §4). The root text is a **critical edition**: it replaced
an OCR export on 2026-08-07 because the OCR's verse segmentation was wrong and it
omitted the entire benefits (ཕན་ཡོན) section; its `source_description` records that
the two witnesses differ in reading at **17 of the 21 homages** (e.g. homage 3
གསེར་སྔོ vs སེར་སྔོ), and the superseded witness is retained in `0-INBOX/`. That
editorial act matters downstream: the pipeline is *sic*-faithful to whatever the
ingested edition says (§5.12), so textual correction happens here, at the source
layer, or not at all.

Each verse and prose block carries a stable Obsidian block ID — the vault's sole
cross-file reference mechanism:

```
ཕྱག་འཚལ་སྒྲོལ་མ་མྱུར་མ་དཔའ་མོ། །
སྤྱན་ནི་སྐད་ཅིག་གློག་དང་འདྲ་མ། །
འཇིག་རྟེན་གསུམ་མགོན་ཆུ་སྐྱེས་ཞལ་གྱི། །
གེ་སར་ཕྱེ་བ་ལས་ནི་བྱུང་མ། ། ^1-1
```

One honesty note the paper keeps visible: the corpus exists in **two annotated
copies** — the vault's `1-SOURCES/` files (sa-bcad headings `^N-N-0`, `status: 0-raw`)
feed the rails-side chain of §§5.5–5.11b, while the pipeline's own
`corpora/tara21/source/` copies (flat `^I-N` block IDs plus root-verse transclusion
anchors `![[root#^1-1]]`) feed the `kwiki` article chain of §5.11a. The two annotation
conventions have not yet been unified on one copy; the citation chain is intact in
both, but the duplication is real and is scheduled to collapse into `1-SOURCES/`.

## 5. The pipeline, stage by stage

### 5.0 Design principles and the map

The pipeline is a set of **skills** — versioned, step-by-step procedures in
`4-SYSTEM/Skills/`, one `SKILL.md` per operation — driven by a tested Python CLI
(`kwiki`, 547 passing tests) and a family of small deterministic scripts. Three
principles repeat at every stage:

1. **The model judges; the script verifies.** Linguistic judgment (what is a sa-bcad,
   what does a passage claim) is model work; everything checkable — byte identity,
   count arithmetic, ID resolution, structural invariants — is done or re-done by
   deterministic code that fails closed. Every stage below ends in a gate a model
   cannot talk its way past.
2. **Isolation over context.** Wherever precision matters, the work is split into
   single-purpose subagent calls that see only their own input — one chunk, one node,
   one commentary, one topic packet — so an error cannot propagate by contamination
   and a task cannot drift into its neighbour's instructions.
3. **Nothing interpretive touches the source layer.** `1-SOURCES/` receives only
   structure: block boundaries, IDs, headings, navigation links. Every script that
   writes near a source file carries a no-loss assertion that aborts if a single
   non-whitespace character changed.

The chain, with its skills, gates, and artifacts:

| # | Stage | Skill / module | Deterministic gate | Output |
|---|-------|----------------|--------------------|--------|
| 1 | Cleaning | `clean-raw-text` / `clean-commentary-text` | profile shown before any change; never overwrites raw | `work/cleaned.md` |
| 2 | Normalisation | `tibetan/normalize.py` (library) | NFC on ingest; comparison keys only, storage never edited | — |
| 3 | Segmentation | `format-tibetan-root-text`, `commentary-segmentation` | `assert_no_loss` (whitespace-squeeze equality) | block-ID'd source files |
| 4 | Structural annotation | `tag-inline-toc` (+ heading grammar) | `verify_prose_unchanged` diff-back | headings `^N-…-0`, inline wikilinks |
| 5 | TOC-tree extraction | `toc-tree-extraction` (4 isolated passes) | `qc_check_tree.py` + `qc_tree_vs_source.py`, both zero-issue | `2-RAILS/Sections/Raw/toc-tree/<id>.md` |
| 6 | Alignment | `Transclusion-rootext-into-commentaries`, `stages/align.py` | `verify_spans` (span must exist verbatim) | `aligned.json` / anchors |
| 7 | Claims extraction | `tree-guided-claims` (per-node subagents) | `verify_claims.py` (4 hard checks) | `Claims/raw/tree-guided/<id>.md` |
| 8 | Spine mapping | `spine-map` (one subagent per commentary) | `verify_spine_map.py` (disposition completeness) | `Claims/raw/spine-map/<id>.md` |
| 9 | Packet assembly | `assemble_packet.py` (script, no model) | exits non-zero on any gap | packet + manifest |
| 10 | Question generation + consolidation | `claims-consolidation` (one agent per topic) | manifest diff (coverage check) | `2-RAILS/Claims/<topic>.md` |
| 11 | Consolidation audits | `verify_consolidation.py`; `claims-consolidation-audit` | gate 1 zero-error; gate 2 no critical/moderate | audit report |
| 12 | Article generation | `kwiki` stages 4–6b, or `wiki-article-from-claims` | claims-only invariant enforced in code | `article.wiki` + `citations` |
| 13 | Verification | `tibetan/verify.py` + `wiki/validator.py` | character-exact quotations; V1–V12 | verify report |
| 14 | Publication | `kwiki publish` | `dry_run=True` default; ledger must be `verified` | bo.wikipedia edit (none yet) |

Two invariants govern the article chain, stated as such in the canonical pipeline
document (`docs/reference/cowork-pipeline.md`):

> 1. **Nothing downstream ever touches source wording after the claims stage** — the
>    claims table is the only drafting input; passages remain in the vault as
>    verification material.
> 2. **Nothing is published that hasn't survived the audit and the pre-publication
>    review.** Everything else is replaceable machinery around those two rules.

### 5.1 Cleaning

**Skill: `clean-raw-text`** (generalised from `clean-commentary-text`). The skill does
not clean directly: it *profiles* the raw OCR/PDF text, reports the profile JSON to the
human before touching anything, then generates and runs a bespoke Python cleaner. The
skill's rules are the contract (verbatim, `clean-raw-text/SKILL.md`):

> 1. **Never overwrite `raw.md`.** Output goes to `texts/<text-id>/work/cleaned.md` only.
> 2. **Do not interpret text.** Do not fix spelling, do not paraphrase, do not add or
>    remove content beyond the mechanical issues listed in the Procedure. […]
> 7. **Non-breaking tshegs (U+0F0C ༌), for Tibetan text,** are always replaced with the
>    standard inter-syllable tsheg (U+0F0B ་). This is never ambiguous.
> 8. **Extra mid-word spaces** (a space between two script characters where no sentence
>    boundary exists) are removed — the space is deleted, not replaced.

The generated cleaner handles exactly eight mechanical transformations — page markers
(`^\s*-\d+-\s*$`), running headers (lines repeating verbatim >5 times), U+0F0C→U+0F0B,
mid-word spaces (`([ༀ-࿿]) +([ༀ-࿿])` → `\1\2`, repeated until stable), orphaned
fragment joins, blank-line collapse — and nothing else. Verse lines (heuristic: ending
`།།` or `། །`) are never collapsed into prose. The worked example bundled with the
skill records the false-positive discipline that makes header-stripping safe:

> "the header text also appears legitimately as a title reference mid-sentence — the
> script only strips lines where the string is the *entire* stripped line content,
> never a substring match."

What cleaning explicitly does **not** do — fix broken syllables, restructure headings,
repair OCR — is deferred to later stages or to the human edition (§4): "Does not fix
broken syllables … that is a job for the format skills, not this one."

### 5.2 Normalisation

Normalisation is a library, not a stage that edits files:
`src/kangyur_wiki/tibetan/normalize.py`. Its module docstring is the design statement
(verbatim):

> Four normalisations, one module. Every guarantee this pipeline makes about a
> quotation is really a claim about *which* normalisation was compared, so the
> verifier, the aligner and the term selector must not each grow their own — that
> drift is exactly how a citation ends up looking checked when it is not.
>
> The ladder, loosest last:
>
> `nfc`           canonical form only. The storage format for everything on disk.
> `collapse`      NFC minus whitespace. Line wrapping legitimately differs between a
>                 commentary file and the article quoting it; nothing else may. This
>                 is the verbatim-comparison key.
> `strip_markup`  NFC minus the editorial furniture that sits *inside* source files —
>                 Obsidian transclusions, block IDs, wikilink wrappers, bold, `<ref>`.
> `fuzzy_key`     all of the above plus every shad, tsheg and head mark. Tolerates
>                 orthographic variation between editions; a match at this level is a
>                 warning, never a pass.
>
> Nothing here edits stored data. These functions build *comparison keys* and return
> new strings; the Tibetan punctuation in the corpus is never touched.

The characters `fuzzy_key` drops are exactly the six that editions disagree about more
often than they disagree about letters:

```python
#: shad U+0F0D, nyis shad U+0F0E, tsheg U+0F0B, and the head marks U+0F05, U+0F04, U+0F08.
FUZZY_DROP: Final = frozenset("།༎་༅༄༈")
```

Each reduction also returns an offset map back into the NFC text (an `array('i')`, not
a list — a 3 MB commentary produces millions of entries), so a match found in a reduced
view can be reported at its true character offset in the stored file. The rule
"Tibetan text is always NFC-normalized; never 'fix' Tibetan punctuation in stored
source data" is repo policy (`CLAUDE.md`), applied at ingest and nowhere else.

### 5.3 Segmentation

**Root text — skill: `format-tibetan-root-text`.** Turns the cleaned root text into
one-stanza-per-paragraph verse with `^chapter-verse` block IDs and `^N-0` chapter
anchors. The segmentation rules are a small grammar of Tibetan punctuation (verbatim):

> - **Verse-line separator**: `། །` (shad U+0F0D, space, shad). Each verse-line ends
>   with this.
> - **Mid-verse line break**: A single shad `།` preceded by a space and immediately
>   followed by a Tibetan syllable … Pattern: `[letter] །[letter]` — e.g. `ག །ན` …
>   must be split with a newline. The negative-lookbehind `(?<![།])` prevents matching
>   the second shad inside a `། །` pair …
> - **Stanza**: typically 4 verse-lines (sometimes 2 or 8). One block ID per stanza.
> - **Double-shad** `།།` appears **only** in chapter colophons, never in regular verse.
>   Use this to detect colophon lines reliably.

Two deterministic formatters implement it (`format_bca.py` auto-detects chapter
boundaries from the text's own colophon formula; `format_bo_root.py` is table-driven).

**Commentaries — skill: `commentary-segmentation`.** Breaks a commentary into
citation-sized blocks (target: 1–2 sentences of prose, one stanza per verse block, one
quotation per quote block; a prose block over ~40 tsheg-delimited syllables is split
unless indivisible) **without altering a character**. The stage-1 segmenter is a rule
engine over seven lexical boundary cues — terminal particles (`འོ`/`ནོ`/`དོ`/`སོ`… +
`།`), quote closers (`ཞེས་སོ། །`, `ཅེས་སོ། །` …), quote openers (`…ལས།`), enumeration
heads (`…ལ་གསུམ་སྟེ།`), ordinal openers (`དང་པོ་…`), objection close/open
(`…ཞེ་ན།` / `འོ་ན་…`), and a protected verse-stanza detector (2–4 uniform-length
clause units of 6–11 syllables each, peeled out whole and never re-cut). What makes
the stage safe to run at all is the no-loss gate, in code:

```python
def assert_no_loss(original: str, segmented: str):
    if _squeeze(original) != _squeeze(segmented):
        sys.exit("ABORT: segmentation altered non-whitespace content. No file written.")
```

The residue no lexical cue can cut is flagged `STAGE2_MANUAL` for a human, whose
hand-edit rules end with the skill's summary of its own bias: "When a passage genuinely
cannot be cut without breaking sense, leave it whole. Over-long is safer than wrong."

### 5.4 Structural annotation: headings and inline sa-bcad tagging

Tibetan commentaries announce their own structure inline — the author enumerates the
coming sections before elaborating each. The vault makes that structure navigable in
two coordinated layers: editorial headings whose block IDs always end in `-0`
(`## … ^1-0`, `### … ^1-2-0`; the zero slot is reserved so headings can never collide
with content IDs), and wikilink tags wrapping each announced term
(`[[#^1-2-0|བཤད་པ་]]`) so the enumeration sentence links forward to the section it
announces. A real seven-level example from the tenga-tulku commentary:

```
### གཉིས་པ་རྒྱས་པར་བཤད་པ་ ^1-2-0
#### གཉིས་པ་སྐུའི་རྣམ་པའི་སྒོ་ནས་ཕྱག་འཚལ་བ་ ^1-2-2-0
###### དང་པོ་སངས་རྒྱས་ཀྱིས་གུས་པས་བསྟེན་པའི་ཚུལ་ ^1-2-2-1-1-3-1-0
```

**Skill: `tag-inline-toc`.** Its architecture is the paper's clearest statement of the
model/script division of labour (verbatim):

> Sa bcad detection has too many surface variants … A rule/regex extractor cannot
> separate genuine sa bcad from look-alikes, and cannot find verbatim term boundaries —
> every rule spawns three exceptions, and tuning it is an endless loop. **Phase 1 reads
> for meaning; it does not pattern-match with code.** The only script in this skill is
> the Phase-2 renderer.

And the converse guarantee:

> Because block IDs are assigned by code, depth-skipping and numbering bugs are
> impossible by construction. Because wraps are exact-substring and the result is
> diffed back against the source, silent transcription drift is caught and the run
> fails loudly. **The model never retypes prose** — it only points at substrings that
> already exist.

The renderer's gate:

```python
def verify_prose_unchanged(source: str, tagged: str) -> None:
    """Assert tagged differs from source only by headings + link wrappers."""
    before = prose_signature(source, drop_headings=False)
    after = prose_signature(tagged, drop_headings=True)
    if before == after:
        return
    ...
    raise TagError("PROSE INTEGRITY VIOLATION at prose line ...")
```

The skill's own change log records a corpus-driven design lesson: the tara21
commentaries' sa-bcad openers are near-universally bare ordinals (`དང་པོ་ནི།`,
`གཉིས་པ་ནི།`) recurring "up to forty times in one file with no unique substring
anywhere on them" — which forced line-number anchors into the annotation contract,
because a context-only contract left those sections legally unannotatable.

### 5.5 TOC-tree extraction

**Skill: `toc-tree-extraction`** — builds, per commentary, the complete nested decimal
sa-bcad tree that every later stage leans on (claims inherit their location from it;
spine maps route by it). The skill is explicitly an *orchestrator*, and the reason is a
finding about prompt design (verbatim):

> The … precision comes from **task isolation**: each pass is a *separate API call*
> with only that one task's system prompt and only the relevant input. The
> candidate-extraction call never sees the tree-building instructions, so it cannot
> drift into tree-building; the verbatim-copy call never sees the "interpret and
> reconcile" instructions, so it stays literal. Merging the four jobs into one
> prompt/one context collapses that isolation and precision drops.

**Pass 0 (deterministic):** `chunk_file.py --chunk-size 150 --overlap 25 --index-only`
— the 25-line overlap guarantees every candidate appears whole in at least one window.

**Pass 1 — section candidates**, one isolated subagent per chunk. The prompt defines
three section types (announcement — `དང་པོ་ལ་གཉིས་ཏེ། མཚན་དོན་དང་། འགྱུར་ཕྱག་གོ།`;
node header — `གཉིས་པ་འགྱུར་ཕྱག་ནི།`; closing count — `ཞེས་རྣམ་པ་གསུམ་མོ།`) and sets
the recall/precision dial explicitly: "when you are not confident that something is a
structural section rather than incidental text, LEAVE IT OUT. A clean list of real
sections is worth more than an exhaustive list full of false positives."

**Pass 2 — verbatim enumerations**, one isolated subagent per chunk, whose entire job
is a START/STOP rule (verbatim):

> - **START** at the topic word being divided (or its ordinal) …
> - **STOP** the instant the division is closed: at the closing particle (ཏེ། / ལས། /
>   འོ། / མོ། / ནོ། །) of the count clause …
> - **DO NOT** continue into the next sentence. The sentence that begins elaborating
>   the first part — typically opening དང་པོ་ནི་… — is **commentary body**. It must
>   NOT appear in your output.

**Pass 3 — tree building**, one isolated subagent, whose authority ordering is the
stage's central idea: the author's own enumerations are "MORE AUTHORITATIVE than
individual candidates," used both to eliminate false positives and to fill structural
gaps — with the counter-rule that doctrinal lists (items enumerated as subject matter,
not as divisions) "must NOT be added to the tree … ONLY when its parts are subsequently
OPENED as their own sections." Titles are matched by meaning, not string equality
(enumeration `…མཚན་དོན་བཤད་པའོ། །` = node header `གཉིས་པ་མཚན་དོན་ཅུང་ཟད་བཤད་པ་ལ་གཉིས་ཏེ།`),
ordinals are kept but never fabricated, and the Tibetan ordinal must agree with the
decimal's last segment.

**Pass 4 — two deterministic QC checkers, then an isolated repair subagent, looped to
zero issues.** `qc_check_tree.py` checks the tree against the model's own
candidates+enumerations corpus: indentation, ordinal↔decimal agreement, duplicate
decimals, gap-free sibling sequences, and three-tier title attestation (exact → ordinal
verified → syllable-bigram coverage ≥ 0.5, below which: "possible hallucination").
`qc_tree_vs_source.py` checks the tree against **the commentary itself**, and its
docstring is the most honest paragraph in the vault — a record of why self-consistency
checking is insufficient:

> All three trees shipped in this vault … reported `issues_before: 0, issues_after: 0`
> from `qc_check_tree.py` while carrying, between them: a top-level misattachment
> (twenty homage children filed under "explaining the benefits" instead of "the praise
> proper"), an unresolved `[[?]]` node with an obvious textual anchor one line away,
> and seven collided line pointers … (the value `130` repeated four times — the
> extractor lost its cursor). This script is the check that would have caught those,
> because it reads the one thing the other checker cannot: the commentary itself.

Its four checks: line-pointer validity (`[[?]]` is *always* an issue), title
attestation within ±3 lines of the pointer, document-order monotonicity plus
repeated-pointer collisions (≥3 shared values = the "lost cursor" signature), and
sibling-count congruence against the announcing text's own cardinal ("a prompt for
human review, not a proof of error"). Promotion to
`2-RAILS/Sections/Raw/toc-tree/<id>.md` requires both checkers clean; the skill's gate
rule: "never declare the tree clean on a subagent's say-so, and never report zero
issues when a checker was not actually run."

A finished tree (tenga-tulku, excerpt; `[[N]]` are line pointers into the source):

```
* 1. ཕྱག་འཚལ་ཉི་ཤུ་རྩ་གཅིག་གིས་བསྟོད་པ་ [[22]]
   * 1.1 དང་པོ་མདོར་བསྟན་པ་ [[24]]
   * 1.2 གཉིས་པ་རྒྱས་པར་བཤད་པ་ [[31]]
      * 1.2.2 གཉིས་པ་སྐུའི་རྣམ་པའི་སྒོ་ནས་ཕྱག་འཚལ་བ་ [[45]]
         * 1.2.2.1.1.3.1 དང་པོ་སངས་རྒྱས་ཀྱིས་གུས་པས་བསྟེན་པའི་ཚུལ་ [[71]]
```

All sixteen commentaries have promoted, QC-clean trees. One known residual defect is
recorded *inside the affected claims file* rather than hidden: gendun-gyatso's source
was re-stamped two minutes *after* its tree's QC ran, so the tree's line pointers have
drifted against the current file — "a `toc-tree-extraction`/QC follow-up item, flagged
for human review."

### 5.6 Alignment: which commentary passage explains which stanza

Two mechanisms, deliberately ordered. **Transclusion anchors first** (skill:
`Transclusion-rootext-into-commentaries`): where a commentary quotes the stanza, a
`![[root#^1-1]]` line is inserted above the quotation — dry-run first, variant-tolerant
matching (character-overlap ≥ 0.80, so `བསྒོམ`/`སྒོམ` and `ཟློག`/`བཟློག` absorb), full
quotations preferred over passing citations, single-line matches accepted only inside a
citation frame (`ཞེས་པ་ནི།`). The skill's 2026-08-01 change record is a measured recall
result on this corpus: **116 → 209 anchored verses (33% → 59%)** across 16 commentaries
× 22 verses, with three named root causes fixed (a dead comparison against Latin
transliterations; blank lines counted as mismatches; no incipit-citation path) — and a
named structural limit: the three commentaries still at zero "are the word-commentaries
— བསྡུས་འགྲེལ and མཆན་འགྲེལ — which dissolve the stanza into glosses and genuinely
never quote it."

**Lexical clustering second** (`stages/align.py`), for the remainder. Its module
docstring states the ordering rationale — "alignment errors are silent … Deterministic
matching can fail to find a verse, but it cannot invent a location" — and carries a
measured precision/recall table (BCA chapter 1, 37 verses): prose commentaries 95–96%
precision at ~51–59% recall; the word-commentary 58%/19%, "structural, not a tuning
problem." Instead of searching for the stanza as a string, the aligner asks where
*fragments cluster*: each verse contributes probes (whole lines weighted 3.0, 9-char
n-grams weighted 1.0), the densest windows of *distinct* probes are scored
(`MIN_CLUSTER_SCORE = 3.0`), and one cluster per verse is chosen under a monotonicity
constraint — commentaries follow their root text in order, so assignment is a
score-weighted longest-increasing-subsequence:

```python
def _monotonic_assign(candidates):
    """Choose one cluster per verse so positions increase down the text.

    Commentaries follow their root text in order. Treating that as a constraint
    rather than a coincidence resolves the ambiguity that sinks naive matching: a
    phrase recurring in chapters 1 and 9 is pinned to the right one by its
    neighbours."""
```

An LLM pass may propose spans for what remains, but its output is never trusted as
text: `verify_spans` re-checks that every proposed span "is a real, contiguous stretch
of its commentary file … we accept its *judgement* about which passage is relevant,
never its *reproduction* of the text."

Result on tara21 (verified in the 2026-08-02 review): **314 aligned spans over the 23
root units — 209 by transclusion anchor, 105 by clustering — seven of sixteen
commentaries at 100% coverage**, the lowest being exactly the condensed and interlinear
genres the aligner's documentation predicts.

### 5.7 Claims extraction: three methods, one winner

The claims layer converts commentary prose into atomic, citable rows. The methodology
document (`Guidelines/claims-methodology.md`) fixes the core principle first:
**extract first, merge later** — "Merge decisions made *during* reading are made with
incomplete information: the first commentary read silently defines the topic space."
Extraction reads one commentary in isolation; consolidation compares finished files and
is disposable.

Three extraction methods were run and compared as genuinely different techniques:

| Method | Skill | Character |
|---|---|---|
| Fixed categories | `commentary-claims` | one pass, nine fixed categories A–I (framing, glosses, iconography, doctrine, activity, ritual, benefits, attributions, ⚑ internal tensions) |
| TOC-scaffolded | `toc-scaffolded-claims` | existing extraction re-bucketed under the tree, plus a typed grounding index (FIG/PER/PLC/TXT/EVT) and per-claim `Referent:` anchoring |
| Tree-guided | `tree-guided-claims` | fresh extraction, one isolated subagent per TOC node |

The comparison's negative findings are why tree-guided is now the standard, and they
are quantified in the skill itself: the "toc-scaffolded" run turned out not to be an
independent extraction at all — **114 of 118 Tibetan strings in one file byte-identical
to the earlier run's**, claim counts copied rather than recomputed, transcription
errors inherited — and presenting a re-bucketing as a second extraction "hid real
defects (a cross-document contamination, a fabricated mantra promoted to canonical
status)." Five load-bearing guards came out of that audit, each traceable to a measured
failure:

> 1. **Claim IDs are never node IDs** … the `toc-scaffolded` files had `1.1` denoting
>    both a claim and a section, **five such collisions on one file alone**.
> 2. **`claim_count` is computed by counting, at the end, never inherited or estimated.**
> 3. **A node-boundary check backs every claim's placement** — each node is read from
>    its own line window alone … so a claim cannot be extracted under the wrong node
>    by construction rather than by discipline.
> 4. **`stated` means the referent's verbatim name occurs in *this claim's own* quoted
>    Tibetan** — on the original run, **7 of 14 claims tagged `(stated)` in one file
>    contained no form of the referent's name at all**.
> 5. **Every claim is independently re-derived**, never re-bucketed.

Claim IDs are `c-<node-decimal-with-dashes>-<n>` (node 1.2.3's third claim is
`c-1-2-3-3` — a string that cannot be mistaken for a heading number). Each per-node
subagent receives *only* the extraction rules, its node's line window, and its node's
decimal and title — never another node's output, never another commentary's file. A
real claim from the corpus (gendun-gyatso, node 1.1):

```
#### c-1-1-4 Gloss: "Swift" (མྱུར་མ)
**བོད་ཡིག:** དམན་ཏན་ཇི་ལྟ་བུ་དང་ལྡན་ཞེ་ན། མྱུར་མ་སོགས་ཏེ། ཐུགས་རྗེས་སེམས་ཅན་གྱི་དོན་ལ་
སྐད་ཅིག་ཀྱང་གཡེལ་བ་མེད་པའི་འཕྲིན་ལས་བྱུང་བས་ན་ཕྱུརམ།
**English:** … because her compassionate activity for the welfare of sentient beings
never lags even for an instant, she is [called] "the swift one."
**Type:** word-gloss
**Referent:** FIG-1 (section-opener)
**Cite:** (1-SOURCES/Commentaries/ཕྱག་འཚལ་སྒྲོལ་མ་ཉེར་གཅིག་མའི་རྣམ་བཤད།.md#^0-5)
```

Internal disagreement inside one commentary is preserved, never averaged (a real ⚑
entry, same file):

```
⚑ **c-1-5-3 The "seven worlds" — two explanations of the enumeration**
- **Position 1:** … ཞེས་རྗེ་བཙུན་གྲགས་པ་རྒྱལ་མཆེན་གྱིས་བཤད། — (…md#^0-14)
- **Position 2:** འགའ་ཞེ་ན་… ཟེར་རོ། — (…md#^0-14)
```

The deterministic backstop, `verify_claims.py`, enforces four hard checks (exit code =
issue count): quote containment — every **བོད་ཡིག** string, NFC- and
punctuation-normalised, must be a literal substring of its cited block, with
ellipsis-joined fragments tested individually; `claim_count` recomputation; the
ID-collision scan; and `(stated)`-referent validation. Repair is by fresh per-node
subagent, "never suppress a finding to make the count read zero."

**State on disk: 16 tree-guided claims files, 2,975 claims (62–368 per commentary),
all `status: draft`** — the LLM never marks its own extraction complete.

### 5.8 Spine maps: routing without interpretation

Consolidation needs to know, for every commentary, which of its own TOC nodes hold
which canonical spine slot (tara-01 … tara-21, benefits, origin, structure). The pilot
design answered that question inside every topic run — "correct but quadratic in the
wrong variable" (~400 full-file reads over a 3.8 MB corpus). The fix is the
**spine-map** layer: one routing table per commentary, built once, reused by every
topic. The skill's defining constraint:

> **Routing only — never interpretation.** This file records addresses. Do not restate,
> summarise, paraphrase, or evaluate a claim's content anywhere in it. […]
> **Node numbering is never assumed uniform** … One commentary nests a homage at
> `1.1.N`, another at top level `N`, another titles nodes by epithet instead of
> ordinal, another runs all twenty-one homages inside a single undivided node. […]
> **Every claim gets exactly one disposition** … Neither zero (silent loss) nor two
> (silent duplication into two packets) is acceptable.

A regular map row and the hard case, side by side. karma-maitri's tree is flat and
ordinal-titled, so nodes route directly:

```
| `tara-05` | `^1-5` | `1.1.5` | ལྔ་པ་ཕྱག་འཚལ་ | 7 |
```

tsultrim-namdak carries all twenty-one homages inside a single undivided node, so its
map routes **by claim-ID range**, using the extraction's own "Verse N quoted" claims as
boundary markers:

```
| `tara-05` | `c-2-1-2-1-16`–`c-2-1-2-1-18`, `c-3-8` | Same pattern, bounded by "Verse 5 quoted." |
```

`verify_spine_map.py` recomputes every count and enforces disposition completeness;
silence is recorded, never inferred ("A registered slot this commentary genuinely does
not treat goes in Silent slots with a reason … A slot that is neither mapped nor marked
silent is a gap"). All sixteen maps exist.

### 5.9 Packet assembly, question generation, and consolidation

**Packet assembly is a script, not a model.** `assemble_packet.py <slot>` collects one
spine slot's claims out of every commentary's raw file, copying each claim block
**character-for-character** — "A script cannot mis-transcribe བོད་ཡིག" — and emits a
`## Manifest` of every `registered_id:claim_id` included, which becomes the input to
the coverage check. Its failure modes are loud by design:

```python
print(f"ERROR: {rid} has no disposition for slot `{slot}` — add a Slot map row "
      f"or a Silent slots row to its spine map", file=sys.stderr)
print(f"ERROR: {rid} has a raw claims file but no spine map — it is missing from "
      f"this packet entirely. Run the spine-map skill on it before consolidating.",
      file=sys.stderr)
```

**Questions are generated, not authored.** The methodology document (verbatim):

> No human writes the question list. Two free sources:
>
> 1. **From the spine, mechanically:** 21 Tārās × observed facets (name/etymology,
>    colour, implements, stance, activity, mantra, benefit) plus global topics ≈ a
>    scripted question grid.
> 2. **From the extractions themselves:** every raw claim implies a question — one
>    commentary's "the left hand's three fingers symbolise the Three Jewels" becomes
>    "what does each commentary say the left hand symbolises?", asked of all the
>    others.
>
> The union of both is the question set. This makes question-driven consolidation a
> **derived completeness check**: free extraction first, then generated questions
> catch what free reading missed.

Real questions from `2-RAILS/Claims/tara-01.md` (14 in its `consolidation_questions:`
frontmatter), one of each kind — grid, inversion, and a *negative control* probing
whether a commentary's silence is real:

> - "How does each commentary etymologise the three names of the homage — Tārā, Swift
>   (myur ma), Heroine (dpa' mo)?"
> - "Does any commentary dispute whose tears produced the lotus Tārā arose from?"
> - "Is lobsang-dawa's silence on this slot a real gap, or is the same content routed
>   elsewhere in that commentary?"

**Consolidation** is one agent per topic, working only from the packet, writing per
facet: **Consensus** (with per-commentary attestations), **⚑ Divergences** (never
flattened — vault hard rule), **Unique** (single-commentary claims), plus a Coverage
table in which silence is itself a finding. Citations are always
`registered_id:claim_id`. A question nobody answers is kept and marked, never deleted.
From the finished tara-01 page — a fifteen-commentary consensus with its full
attestation list, and a divergence in which one side exists only as a commentator's
report of "earlier commentaries":

> Avalokiteśvara …, seeing that however many beings he delivered from saṃsāra their
> number never diminished, wept; from his tears … a lotus grew, and Tārā arose from
> its opened pollen/blossom. This is attested — independently, in each commentary's
> own words — by every one of the fifteen contributing commentaries in this packet.
> — attested: anon-trinle-char:c-3-1-15 … tsultrim-namdak:c-2-1-2-1-6 (15 commentaries)
>
> ⚑ **Whose tears produced the lotus.** konchok-thabkhe explicitly flags, within its
> own text, that "earlier commentaries" (unnamed …) gloss the tantra's second line as
> referring to Tārā's own eyes/tears, whereas konchok-thabkhe itself — following
> Nyima Sbaspa — reads the tears as Avalokiteśvara's …

Consolidation even surfaces **root-text-level variants**: the tara-01 page's first ⚑
records that one commentary's own quotation of the verse reads དཔལ་མོ ("Glorious One")
where the corpus reads དཔའ་མོ ("Heroine") — "the two readings license different
etymologies for the same syllable-position" — while flagging a second apparent witness
as a probable transcription slip inside its own raw extraction.

After writing, the **coverage check** diffs the packet manifest against every claim ID
the page cites; every claim in the gap is either folded in or logged with a reason
under "Claims reviewed, not separately cited" — "no third state." In the pilot this
caught real gaps in roughly 5–12% of a topic's mapped claims per page.

**State on disk: 24 consolidated topic pages** (tara-01 … tara-21 + benefits, origin,
structure), all `status: draft`.

### 5.10 The consolidation audits — and the error taxonomy that rewrote the rules

On 2026-08-07 the three pilot topic pages were adversarially audited: a fresh agent per
page re-checked **every one of 418 unique citations** against the raw claims files.
Headline: **zero fabricated claim IDs** — and one critical finding, one moderate, ~16
minor, in a stable taxonomy. The critical case is the audit design's whole
justification (verbatim from the findings file):

> 1. **CRITICAL — `gendun-gyatso:c-1-2-1` (Face section).** Cited as independently
>    corroborating anon-trinle-char's "three flaws" framing (dust, mist/haze, cloud).
>    The raw claim contains no flaws framing — only "face supremely white and beautiful
>    like stacked full autumn moons." Correct attestation is almost certainly
>    `gendun-drub:c-2-2-2-2-1-1-1-3` …

A deterministic script can prove a cited claim *exists*; only a reader can prove it
*says* what the page attributes to it — the consolidator had a real corpus idea
attached to the wrong claim ID, a failure no existence check can catch. The minor
findings were equally instructive: partial-support padding of consensus lists, the same
claim cited on both sides of one divergence, page-level harmonizations presented as a
claim's own reading, epistemic upgrades ("endorses" for a tentative སྙམ་མོ aside),
silently elided syllables in Tibetan quotes ("བརྒྱད་གཉིས་སྒྲིགས" for raw
བརྒྱད་གཉིས་**པ་**སྒྲིགས), and hand-tallied "(N commentaries)" labels — **five of five
wrong on the worst page**.

That taxonomy was converted directly into machinery — each error class became either a
rule (`claims-consolidation` Rules 9–16: full-statement support; corroboration re-read,
not remembered; one side per divergence; verbatim quotes or marked ellipsis;
harmonization attributed to the page, not the claim; epistemic strength copied, never
upgraded; counts computed, never hand-tallied; every consulted claim gets a
disposition) or a check in one of **two standing gates**:

- **Gate 1 — deterministic** (`verify_consolidation.py`): citation existence, count
  labels recomputed per paragraph, consensus/divergence overlap flags, disposition
  completeness against the Coverage table, prefix discipline. Zero errors required.
  "Validated by reproducing every mechanical finding of the human audit, plus one it
  missed" (an undispositioned claim the human auditor overlooked).
- **Gate 2 — adversarial attribution audit** (skill: `claims-consolidation-audit`): a
  fresh agent that did not write the page checks every attribution against the raw
  claims — "An agent auditing its own consolidation re-reads its own intentions, not
  the text." Ground truth is the raw claims file only, never the auditor's knowledge
  of the tradition. Severity: critical / moderate / minor; report-only; the
  consolidator fixes, the auditor re-checks; no critical or moderate finding may
  remain.

A Tibetan-language consolidation variant (`claims-consolidation-bo`) produces `-bo`
twin pages under the same rules and both gates, with bilingual structural headings
(`### མཐུན་སྣང (Consensus)`) so the deterministic checker still parses them, and a
strict independence rule: the `-bo` consolidator must not read the English counterpart
— the pairs double as a controlled comparison of consolidation quality by working
language.

### 5.11 Article generation

Two drafting routes share one doctrine — **claims-only drafting** — and one gate
(§5.12).

**(a) The `kwiki` per-term chain** (extract → claims → outline → draft [→ polish] →
audit), which produced the reviewed pilot's three articles (སྒྲོལ་མ, འཇིག་རྟེན་གསུམ,
སྡུག་བསྔལ). The extraction prompt is in Tibetan; its seven rules are the contract
(04-extract, condensed): quote character-for-character — "ཡི་གེ་གཅིག་ཀྱང་བསྒྱུར་བ་དང་།
བསྡུ་བ་དང་། ཚིག་སྒྱུར་བྱེད་མི་ཆོག" — with the warning that a machine will check every
letter; take only passages that *explain* the term, not mere occurrences; echo the
block's own `segment_id`; never truncate; never flatten disagreement; write
"འགྲེལ་བཤད་མེད།" rather than invent; add nothing from your own knowledge. The claims
prompt then compresses passages into the atomic table — "One verifiable fact per claim,
written in Tibetan in your own words … A claim with no supporting passage must not
exist … **Forbidden: synthesis.** No claim may require two sources combined to reach a
conclusion neither states alone" — with claim types (consensus /
majority-with-dissent / school-position / single-commentator) weighted "by authority
and response, not headcount: a commentator who is the sole representative of his school
in this corpus is a `school-position`, never `single-commentator`."

From that point the sources are closed. The drafting prompt receives **only** the
outline and the claims table — verified in code: the stage-06 `prompt_render` call
passes `term`, `outline_json`, `claims_json`, `glossary`, and nothing else — and its
closing line tells the model exactly how little it is trusted with:

> `citations` are **claim indices** into the supplied claims list. The pipeline
> attaches the underlying source quotations and renders the refs — you never write a
> ref or a URL.

Code, not the model, expands each cited claim back to its passages and renders the
references:

```python
def render_draft_payload(term, data, claims, passages, registry, ...):
    """The model cites *claims*; this expands each claim to the passages behind it
    and renders the refs. Quotations therefore enter the article only from
    ``extract.json``, never from the drafting model — which is what keeps the
    stage-7 character-for-character gate meaningful under claims-only drafting."""
```

Voice follows claim type (a consensus claim may sit in Wikipedia's neutral voice;
everything below consensus gets mandatory in-text attribution), the optional Gemini
polish pass is structurally fenced (its output is rejected by a code diff if any
citations array, heading order, or paragraph count changed — "The stylist is never
trusted with structure; that check is code, not prompt"), and the audit stage reads the
draft back sentence-by-sentence against the claims table with six finding categories
(added-fact, dropped-qualifier, terminology-drift, attribution-loss, wrong-claim,
meaning-shift). Two categories block in code regardless of the model's verdict:

```python
AUDIT_BLOCKING = frozenset({"added-fact", "attribution-loss"})

@property
def passed(self) -> bool:
    """Belt and braces on purpose — a model that lists an added fact and still
    says "publish" is overruled by its own finding."""
    return self.verdict == "publish" and not self.blocking
```

A real blocking finding from the pilot's audit rounds:

> ⛔ [blocking] **dropped-qualifier** — The draft changes 'three different scholars'
> (མཁས་པ་མི་འདྲ་བ་གསུམ་) to 'many different scholars' (མཁས་པ་མི་འདྲ་བ་མང་པོ་),
> exaggerating the consensus.

**(b) The rails route** (skill: `wiki-article-from-claims`), which turns one
consolidated topic page into a slot-article — the route behind the three per-homage
articles now in `3-TRANSFORMATIONS/Wikipedia/tara21/slot-articles/`. The consolidated
page supplies the facts; the raw claims files supply the verbatim Tibetan and the
`1-SOURCES/` block citations; parametric knowledge supplies nothing: "No parametric
knowledge — no dates, Sanskrit forms, iconographic details, or doctrinal framings that
are not in a claim, however standard they seem. If it cannot be cited, it does not go
in." The resolution chain is fixed (consolidated attestation → raw claim → **བོད་ཡིག**
+ `Cite:` block); an attestation that does not resolve is dropped and logged under
*Unresolvable attestations*, never guessed. Section headings are "a menu, not a quota"
(མཚན་གྱི་ངེས་ཚིག → སྐུ་ཡི་རྣམ་པ། → ཕྲིན་ལས་དང་ནུས་མཐུ། → … → the fixed tail
འབྲེལ་ཡོད་ཤོག་ངོས། → ལུང་ཁུངས། → དཔྱད་གཞིའི་ཡིག་ཆ།); due weight follows attestation
counts (consensus forms the unattributed backbone cited to 2–4 representative
commentaries; ⚑ divergences present every position with attribution, never
adjudicated). The lead of the tara-02 article, as drafted:

```wikitext
'''བློ་གཏེར་དབྱངས་ཅན་མ་'''ནི་ སྒྲོལ་མར་ཕྱག་འཚལ་ཉེར་གཅིག་གིས་བསྟོད་པའི་གཉིས་པའི་ཕྱག་འཚལ་ཏེ<ref
name="taranatha">ཏཱ་ར་ནཱ་ཐ། ཕྱག་འཚལ་ཉེར་གཅིག་གི་བསྟོད་པའི་རྣམ་པར་བཤད་པ།</ref>…, རྩ་བའི་ཚིགས་བཅད་ལས་
"ཕྱག་འཚལ་སྟོན་ཀའི་ཟླ་བ་ཀུན་ཏུ། ། གང་བ་བརྒྱ་ནི་བརྩེགས་པའི་ཞལ་མ། །…" ཞེས་གསུངས་པ་ལྟར…
```

Each article ships with a `citations.md` audit trail: a reference map (named ref →
commentary → claim IDs → verbatim quoted Tibetan → source blocks), unresolvable
attestations, warnings, and a per-quotation verification table (tara-03: 13/13 PASS;
tara-02: 8/8 PASS, "No quotation required correction or removal").

### 5.12 The deterministic verification gate

Last in the chain, blocking, and LLM-free. The quotation checker's docstring states
the tiering, and the tiering *is* the policy:

> Three tiers, deliberately unequal:
>
> `exact`      the quote is a substring of the source. A pass.
> `collapsed`  a substring once whitespace is removed from both. A pass — line
>              wrapping is not part of the text.
> `fuzzy`      a substring once shads, tshegs, head marks and markup are also removed.
>              **Not** a pass. The letters agree but the punctuation does not, which
>              means the article is not quoting what the file says …
> `missing`    a failure.
>
> Reporting a fuzzy hit as success would quietly reintroduce exactly the class of
> error this gate exists to catch, so `found` is not the gate: `passed` is.

The comparison runs through a **reading view** — the commentary with every layer
ingest added (block IDs, transclusion lines, inserted headings, wikilink wrappers)
stripped back off, "not one Tibetan character touched," line structure preserved so
offsets still land — because a faithful quotation spanning a block boundary must never
fail "on a caret we put there ourselves." Independently, every block locator is
resolved: the quotation must also appear inside the specific block its citation names.
And a 12-rule wikitext validator (V1–V12, plus warnings W1–W4) enforces the output
contract, including two rules idiosyncratic to bo.wikipedia and learned from live
renders: V4 — never `{{Reflist}}`, whose local template injects its own heading, so
always `== ལུང་ཁུངས། ==` + `<references />`; and V10 — a tsheg must survive every
`'''` and `[[` boundary, a Tibetan spelling error MediaWiki itself will never surface.
The empirical case for the validator is measured on the target wiki: of 677 sampled
bo.wikipedia articles, 15% are raw model dumps with no markup, 75% have no citations,
~126 carry `<ref>` tags with nothing to display them.

The strictness has a corollary adopted deliberately: articles are ***sic*-faithful**
to the ingested source. In an earlier session the gate caught a model silently
promoting a tsheg to a shad inside a quotation — similarity 0.974, invisible to a human
skimming Tibetan prose. Textual correction is an editorial act for the source layer
(§4) — correct the edition, re-ingest, re-verify — never a liberty of the drafting
model. There is no bypass flag, and an audit "publish" verdict does not skip the gate.

### 5.13 Publication

Nothing writes to Wikipedia without an explicit `--execute`; `dry_run=True` is the
default on the MediaWiki client and every publish path. Publication refuses any term
whose ledger state is not `verified` (the ledger's create path: pending → extracted →
claimed → organized → drafted → audited → verified → approved → published), runs a
pre-publication review checklist (every reference resolves; no sub-consensus position
in neutral voice; no original synthesis; the topic's independent-secondary-source case
restated), targets a userspace sandbox before mainspace, and carries an edit summary
disclosing pipeline assistance. Community consent precedes content: bo.wikipedia has
no local policy on machine-assisted content, and the project reads that vacuum as
*stop* — a public bilingual village-pump proposal, an on-wiki project page naming every
pipeline-assisted article and its reviewer, and paced publication bounded by review
capacity are the plan of record. **As of this draft nothing has been published**: the
pilot's three terms sit at `verified`, one step short of `approved`, and every citation
still lacks a public URL (§7–8) — an article whose quotations a reader cannot check is
the failure mode this pipeline exists to prevent.

## 6. Weighting doctrine: breadth and reception (abridged — full text in `paper.md` §6)

Breadth decides existence (a term explained across many commentaries is encyclopedic;
corpus breadth proposes, the publication layer disposes — no article without an
independent secondary source). Reception decides weight: Tibetan scholastic culture
left a machine-readable reception record — commentaries quote, endorse, and refute one
another — and every claim row carries a reception field beside its school tag; a
position that drew dgag lan has demonstrated weight, a sole corpus representative of a
school is a *school-position*, never fringe. The Tārā run also shows the doctrine's
honest limit: a praise-commentary corpus generates **zero reception-contested claims
(0 of 47 in the pilot; no dgag-lan signal anywhere in the 2,975-claim corpus)** — the
genre explains and extols. The Bodhicaryāvatāra corpus already aligned behind this
pipeline (7,279 spans, ten commentaries, the Ju Mipham exchanges) is where the
machinery will be demonstrated adversarially.

## 7. Publication and data model (abridged — full text in `paper.md` §7)

The data model routes by copyright: none of the canonical Tibetan source repositories
licenses its text for CC BY-SA reuse, so the pipeline **cites sources and never copies
them** — facts are not copyrightable; what look like quotations are renderer-inserted
passages from the extraction record, each character-verified. Public-domain texts queue
for Tibetan Wikisource with per-verse anchors; in-copyright texts cite to BDRC or
library links. The honest current state: **every citation the pipeline has produced
from this corpus is still unlinked** (W1/W2 on all articles — no year/page, no public
URL; the registry's only URLs are Google Drive scans, which the resolver correctly
refuses). Until the registry carries public URLs, these articles are research artifacts
in a review queue, not published pages. Every article leaves behind its by-product
regardless: the claims database, citations with block locators, and a verse-aligned
corpus, all queryable.

## 8. Evaluation

Evaluation runs at two scales — the hand-adjudicated pilot (N=3) and the corpus batch
**[TO FILL]** — plus, new in this draft, the rails-side consolidation audit, which is
itself an evaluation with its own N.

**Citation verifiability (measured, strongest form).** Across the pilot's three
articles the deterministic gate re-read every quotation from its cited source file:
**81 of 81 character-for-character exact; 81 of 81 block locators resolve to the named
block, none wrong.** The corpus was rebuilt from the raw upload on a second machine and
the verification reports came back byte-identical. This measures *fidelity*, not
*support* — the gate proves the quoted evidence is real and correctly located, never
that it warrants the sentence citing it; statement-support is the audit's job plus the
pending human legs (no NLI model supports Tibetan, so it is manual by necessity —
itself a datum for §1).

**The cross-model audit result (unplanned, and the run's most important finding).**
The drafts were audited twice. Same-model audit: "publish, no findings," three for
three. Cross-model audit: **five blocking findings on two of the three articles**;
manual adjudication against the claims table confirmed four genuine (a consensus
exaggeration — "many scholars" for three; an overgeneralization — "a name for *each*
verse" where four are attested; a technical-term shift — མཚན་ཉིད for མཚན་དོན; an
attribution asserted beyond its claim — naming Gendün Drub where the claim
deliberately said "one commentary," right by luck and exactly the class that must
block) plus one borderline. Six surgical edits later — each logged in the article's
model record, with a code assertion that no citation changed — the cross-model audit
returns publish on all three and the gate still passes. The auditor also showed
round-to-round variance (re-auditing the fixed articles three times: pass rates 0.67,
0.67, 1.0) and twice misquoted the draft inside its own findings — model-written
finding text is itself untrusted, which is why blocking keys on categories and why the
deterministic gate sits beneath the audit. Design lesson, stated as a rule: **never
report a same-model audit as independent**, and report audit outcomes as pass rates
over repeated runs, never single verdicts.

**The consolidation audit (measured, rails side).** 418 unique citations across three
topic pages, every one re-checked by a fresh agent: **zero fabricated claim IDs; 1
critical, 1 moderate, ~16 minor findings** — a taxonomy converted wholesale into Rules
9–16 and two standing gates (§5.10), with the deterministic gate subsequently
reproducing every mechanical finding of the human audit plus one it missed.

**Per-stage instrumentation.** `scripts/eval_stages.py` measures each stage against
what the previous stage offered it and localizes the pipeline's weakness precisely:
**extraction capture.** Alignment offered 18k, 41k, and 165k characters for the three
pilot terms; extraction captured 45%, 19%, and **1.1%** — the model budgets its answer
against the size of the question (measured directly: asked about སྒྲོལ་མ with 93,000
characters of context in one call, the extraction model returned ten passages totalling
873 characters; the same model on the same prompt with 12,000 characters returned
twenty passages totalling 5,224 — hence `EXTRACT_BATCH_CHARS = 25_000`: ask smaller
questions rather than shout louder in the prompt). Everything downstream of extraction
is tight: 100% of extracted quotes character-exact at extract time, 100% of passages
used by at least one claim, 100% of claims placed and cited, every paragraph carrying
at least one citation.

**Pipeline statistics (pilot, on disk).** Three articles in 10–20 wall-clock minutes
each; 81 passages → 47 claims (13 consensus / 13 school-position / 21
single-commentator / 0 majority-with-dissent) → 81 rendered citations; 5, 16, and 10
distinct commentaries cited; all 16 cited at least once across the three; lengths
642–1,358 tshegbar, all under the 1,500 target — a known extraction-volume limitation,
reported as such. Machine cost ≈ $0.33–1.42 per article at current prices; the scarce
input is human review by design, and the reviewer-minutes number the August batch must
supply is the paper's lead metric **[TO FILL: batch N, distributions, rater results,
reviewer-minutes]**.

**Rails-side inventory (on disk, 2026-08-10).** 16 QC-clean TOC trees; 16 tree-guided
claims files, 2,975 claims; 16 spine maps; 24 consolidated topic pages; 3 slot-articles
drafted from them (117, 48, and 132 `<ref>` tags; per-quotation verification 13/13 and
8/8 PASS on the two with citation trails). All rails artifacts are `status: draft`
pending domain-specialist review — the LLM never marks its own output complete.

## 9. Discussion (abridged — full text in `paper.md` §9)

Every design choice is the negation of one property of the doom-spiral evidence: a
named human publisher, throughput bounded by review, on-wiki disclosure, verification
deterministic where possible and adversarial (cross-model, fresh-context) where not,
and an audit trail from every published sentence back through claims to block-located
passages. The residual risks are stated plainly: a fluent reviewer can still wave
through a subtly wrong article; claims-only drafting narrows the copyright surface
without abolishing close paraphrase in principle; OCR quality upstream bounds
everything, and the gate makes articles *sic*-faithful to it. This draft adds the
methods-level limitations the artifacts themselves record: the corpus exists in two
annotated copies pending unification; the three slot-articles were drafted from
`rails_status: draft` pages with the human contributor accepting that risk explicitly;
one article's citation trail (`tara-01/citations.md`) is missing; one promoted tree's
line pointers drifted after a post-QC resegmentation and are flagged for follow-up;
methods 1 and 2 of the claims comparison have no surviving outputs on disk, so the
comparison is documented but not re-runnable from this vault; and article lengths are
below the stub threshold pending the extraction tuning pass. None of these is a
footnote to the thesis; they are the thesis — the machine does the checkable parts,
every defect is written down where a reviewer will find it, and the judgment stays
human.

## 10. Conclusion

The cycle this paper set out to enter is running today in the wrong direction for
Tibetan. We have shown a working pipeline built to flip its sign, now visible at full
methods depth: a cleaning layer that touches nothing it cannot name, normalisation as
comparison keys over an untouched corpus, segmentation behind a no-loss assertion,
structure extracted in isolated passes and gated by two deterministic checkers, claims
extracted node-by-node under five measured guards, routing separated from
interpretation, questions generated rather than authored, consolidation audited twice
— once by script, once by an adversarial fresh context — articles drafted from claims
alone, and a character-exact gate no model verdict can waive, with a human hand on the
only switch that publishes. The per-article artifacts are small; the machine is not: a
reusable editorial system whose every safeguard is a testable invariant, and a growing
claims database over the commentarial tradition — 2,975 typed, school-tagged,
block-located rows and counting — that is a research object for this field regardless
of what Wikipedia becomes.

---

*References: consolidated with URLs in `09 - Reading List and Bibliography.md`; formal
bibliography formatting deferred to the camera-ready pass. Run artifacts:
`corpora/tara21/` (articles, claims, audits, verification reports, model provenance),
reviewed in `corpora/tara21/REVIEW-2026-08-02.md`; rails artifacts under `2-RAILS/`
and `3-TRANSFORMATIONS/Wikipedia/tara21/`; consolidation audit in
`0-INBOX/claims-audit-findings-2026-08-07.md`. Prompts quoted are the active versions
under `prompts/` and the skills' own `SKILL.md` files; code quoted is at the cited
modules in `src/kangyur_wiki/` and the skills' `scripts/` directories.*
