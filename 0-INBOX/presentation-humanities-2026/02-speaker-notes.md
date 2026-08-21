# Speaker notes — what to say on each slide

Talking points only, in bullets. Not a script to read — the slides carry almost no text, so
**the talk is the content**. Timings are cumulative targets; if you're past the time on a slide,
skip ahead rather than compress.

**Audience assumption:** humanities scholars. They know Tibetan textual traditions cold and know
almost nothing about software engineering. So: *never* say "pipeline stage," "orchestrator,"
"deterministic checker," or "gate" without giving the plain-language version first. Every
technical concept gets an analogy from *their* world — the seminar room, the critical edition,
the index card, the concordance, the proofreader.

**The three rhetorical moves that carry the whole talk:**
1. The problem is not a lack of material. Tibetan has *more* classical literature than the
   languages doing this well.
2. The scary thing about AI on small wikis has already happened, and it was a disaster. I'm going
   to tell you why this is the opposite of that.
3. The machine does not have authority anywhere in this system. It has judgement everywhere.

---

## ACT I — The gap (0:00 → 4:00)

### Slide 1 — Title · 0:00–0:20

- Name, project (OpenPecha), and the one-line frame.
- "This is a talk about making Tibetan legible to machines — without letting machines decide
  what Tibetan says."

### Slide 2 — Two numbers · 0:20–1:00

- Seven million speakers. One of the largest classical literatures in Asia.
- Eight thousand articles on the Tibetan Wikipedia. *(Use the fresh count — see the verify list.)*
- Thirty-six active editors in a typical month. Two administrators. About 350 new articles a year.
- Eighteen years after founding, the whole Tibetan Wikipedia is roughly the size of a single
  English-language WikiProject.
- **Pause here.** Don't explain the number. Let it sit.

### Slide 3 — Who does more with less · 1:00–1:40 *(cut first if long)*

- Welsh: in 2017 the Welsh Government made growing the Welsh Wikipedia *explicit policy* — the
  stated reason being to make Welsh visible to technology companies.
- 91,000 articles to over 280,000. It became the most-viewed Welsh-language website. And Welsh
  machine translation improved on the back of it.
- That's this talk's argument, made a decade earlier, by a government, with results.
- The point of the chart: every one of these languages has **fewer speakers and a smaller
  classical corpus than Tibetan**. The constraint was never the amount of material. We have more
  material than almost anyone. What we don't have is the *conversion*.

### Slide 4 — The models can't read us · 1:40–2:30

- This used to be a question of visibility. It's now a question of capability.
- On the TLUE benchmark — Tibetan multiple-choice understanding — most large models score
  **below the random-guessing baseline.** GPT-4 at 17.5% against a 25% floor.
- The one to point at: Qwen-2.5-72B scores 84.7% in Chinese and 16.5% in Tibetan. Same model.
- Worse than a coin toss isn't "needs work." It means the language is effectively *not in the
  training data.*
- And there's a cost dimension: byte-level tokenisers make Tibetan roughly four times as
  expensive to process as Chinese. We pay more per word to be served worse.
- The link to Wikipedia: by the Wikimedia Foundation's own account, Wikipedia is almost always
  the single largest source in a language model's training corpus. Per-language model
  performance tracks a language's share of pretraining text.
- So when someone asks an AI assistant a question about Tibetan culture, *in Tibetan*, and gets
  a wrong answer — that isn't because the knowledge is obscure. It's because the open digital
  text those systems learned from barely includes us.

### Slide 5 — The loop has a sign · 2:30–3:15

- So it's a loop, and right now it runs the wrong way: absence begets absence.
- **Left ring:** no articles → little training text → the tools can't serve the language → fewer
  people work in it online → still no articles.
- Kornai gave the endpoint of that trajectory a name: *digital language death.*
- **Right ring:** cited articles → digital footprint → better tools → faster articles.
- Here's the thing worth holding onto for the rest of the talk: **it's the same loop.** The
  machinery is identical. The only thing that determines which direction it runs is whether
  anything was verified before it was published.

### Slide 6 — Three options · 3:15–4:00

- There are only three ways to grow a small-language Wikipedia to useful size.
- **By hand.** I'll give you the arithmetic in a moment.
- **Unsupervised automation.** This is not hypothetical and I want to name it before anyone in
  the audience does. The Scots Wikipedia: about 23,000 articles written by one enthusiastic
  non-speaker — credibility destroyed. Cebuano: six million bot stubs, repeated closure
  proposals. And the Greenlandic Wikipedia was **closed by the Language Committee in 2025** over
  machine-generated content. Inuktitut is estimated two-thirds contaminated by machine
  translation. Several African-language wikis sit at 40–60% uncorrected machine translation.
- So when someone says "AI content for small Wikipedias," they are currently naming a disaster,
  not a hope. I want to be very clear that I know that.
- **Supervised automation** is the third option, and the rest of this talk is an existence proof
  that it's real.
- One counterweight worth knowing: Wikipedia's own Content Translation tool — machine draft plus
  *mandatory* human edit — produces articles with **lower** deletion rates than from-scratch
  articles, across more than 2.4 million creations. The failure mode and the working mode differ
  in exactly one variable.

---

## ACT II — How the work is done (4:00 → 7:00)

### Slide 7 — The arithmetic of "by hand" · 4:00–4:40 *(cut second if long)*

- The Dzongkha Wikipedia Education Program in Bhutan — the closest Tibetic-script precedent,
  entirely manual. Institutional backing, dozens of trained participants, five months.
  **Eighty articles.**
- Tibetan Wikipedia: about 350 articles a year.
- At that rate, a minimally serviceable encyclopedia — call it 100,000 articles — is more than
  two centuries away.
- **Say this deliberately:** that is not a criticism of the editors. Those are some of the most
  committed volunteers in any language community. It's the measured capacity of the mode.

### Slide 8 — Agent and harness · 4:40–5:20

- Two words I'll use for the rest of the talk, so let me define them in plain terms.
- **The model** — Claude, in our case — is the thing that reads Tibetan and makes judgements. It's
  the apprentice.
- **The harness** is everything around it: what files it can open, what it's allowed to write,
  what tools it can run, what rules are pinned above the bench.
- Think of a workshop. The apprentice is capable but has no memory of house procedure and no
  authority. The bench, the racked tools, the rulebook on the wall, the in-tray and out-tray —
  that's the harness. It's what makes the apprentice's work *reproducible* instead of
  *improvisational*.
- **An "agent"** is just the apprentice actually working at that bench: reading a file, making a
  judgement, writing an output, running a check — in a loop, without being told each step.
- Concretely: I work in a plain Obsidian vault of markdown files. Claude Desktop reads and
  writes those files directly. There's no database. Every intermediate stage stays human-readable
  and reviewable in place — which matters enormously for the review step later.

### Slide 9 — Skills: the Matrix analogy · 5:20–6:10

- Here's the analogy I actually find most useful, and it's from *The Matrix*.
- Neo needs to fight. He doesn't train for years. Someone loads a program, and then — "I know
  kung fu."
- **A skill is exactly that.** It's a file — step-by-step instructions for one specific operation
  — that gets loaded into the model right before it does that operation.
- The model does *not* know how to extract a sa-bcad tree from a Tibetan commentary. Nothing in
  its training taught it our conventions. But the skill file says: here's what a sa-bcad
  announcement looks like, here are the five passes to run, here's the numbering scheme, here's
  what to do when the declared count doesn't match the children you found.
- This vault has **63 of them**. Cleaning OCR. Formatting a root text into verses. Segmenting a
  commentary. Extracting a tree. Extracting claims. Building a spine map. Consolidating a topic.
  Drafting an article. Auditing one.
- **The important part for this audience:** a skill is a *text file*. Not code. Not a black box.
  A domain expert can read it, disagree with it, and edit it — and I'll come back at the end to
  how that's exactly what happened.
- And skills are *versioned*. When we change how something is done, we write a new version and
  record what changed and why. We never rewrite a shipped one in place — because if you do, you
  can no longer say what produced last month's output.

### Slide 10 — Scripts: the machine · 6:10–7:00

- The other half is scripts — small Python programs. And the analogy is a machine.
- You put something in the hopper. Rules are bolted to the side. The same thing comes out the
  chute, every time. No judgement, no interpretation, no mood, no creativity. A machine cannot
  be persuaded.
- **The division of labour is the single most important design decision in this project**, and
  it's one sentence: *the model judges; the script verifies.*
- Judgement work — is this line a structural announcement or is it prose? does this gloss say the
  flower is blue or that it's clear-hued? — that's a reader's job, and the model does it.
- Machine work — does this exact string of Tibetan appear, character for character, in the file
  it claims to come from? — that's a ruler's job, and code does it.
- And the crucial asymmetry: **the script has the final say.** If the model says "publish" and the
  machine says the quotation doesn't match, the build fails. There is no override flag. We
  deliberately did not build one.

---

## ACT III — One verse, all the way through (7:00 → 15:00)

### Slide 11 — The corpus · 7:00–7:40

- The case study: the *Praise to the Twenty-One Tārās* — Tohoku 438, in the Kangyur, attributed
  by tradition to Vairocana. Probably the most widely recited Tārā liturgy across every Tibetan
  tradition.
- Sixteen commentaries. About 540,000 characters. Drakpa Gyaltsen, the First and Second Dalai
  Lamas, Tāranātha, Ngulchu Dharmabhadra, Khenchen Palden Sherab, living teachers. Sakya, Geluk,
  Jonang, Nyingma, Kagyü.
- I chose it because it's *bounded and heavily commented* — small enough to audit completely, rich
  enough that every generated sentence can be checked against a named human source.
- One methodological note that will matter to this room: the root text we use is a **critical
  edition**, not an OCR export. The edition we replaced had wrong verse segmentation and stopped
  mid-clause at the twenty-first homage, omitting the benefits section that every commentary
  comments on. The edition's own apparatus records that its two witnesses differ at **17 of the
  21 homages**.
- **Now the promise:** I'm going to take one verse — the third homage — and one commentary —
  Gendün Drub, the First Dalai Lama — and follow them all the way to a finished article. Every
  screen you see from here is a real file.

### Slide 12 — Getting the text in · 7:40–8:30

- Most of this material exists as *images*. Scans from BDRC and elsewhere. So step one is OCR.
  Sometimes we get a text version off the internet instead, and then it needs a different kind of
  cleaning.
- Cleaning is done under a rule that matters: the script first builds a **profile** of the
  mechanical junk it found — page-number lines, running headers, the wrong tsheg character — shows
  that profile to a human, and only then runs a cleaner limited to *exactly* those fixes. It never
  interprets. A doubtful reading is a question for the editor, not for the machine.
- Then segmentation: cutting the commentary into citation-sized blocks. This runs behind what I'd
  call a **no-loss gate** — if the segmented text differs from the original by one non-whitespace
  character once you squeeze out spacing, the script aborts and writes nothing. And where no rule
  can safely make a cut, it hands the passage to a human under a stated bias: over-long is safer
  than wrong.
- **And then the thing that everything else depends on.** Every block gets a permanent address —
  a block ID.
- Why that matters to you: a footnote that points at a *file* is a promise. A footnote that points
  at a *block* is an address. Somebody can open it. Every citation in every artifact I'm about to
  show you resolves to one of these.

### Slide 13 — The sa-bcad tree · 8:30–9:20

- Tibetan commentators announce their own structure. "This has two parts." "The second of these
  has six." That's the sa-bcad, and it's the architecture of the argument.
- We extract it as a nested outline, with a pointer from every node into the source.
- This is Gendün Drub's: **37 nodes, seven levels deep.** And look at the leaf nodes under
  "extended explanation" — there are exactly twenty-one. The tree recovered the praise's own
  architecture, as the commentator declared it. Nobody imposed that.
- One engineering finding that I think generalises, because it surprised us: extraction is split
  into **five separate passes** that don't see each other's instructions. A call that never sees
  the tree-building instructions can't drift into tree-building. A call whose only job is to copy
  an enumeration verbatim, and which never sees the words "interpret and reconcile," stays
  literal. When we merged those jobs into one call, precision dropped.
- And the tree-builder treats the author's **own enumerations as more authoritative than
  individual candidates**: if he says "this has six parts," six children must appear. Doctrinal
  lists — things enumerated as subject matter rather than as divisions of the text — never become
  nodes.
- The branch highlighted here is where our verse lives: node 2.2.2.2.1.1.2, "praise by way of her
  body colour, hand-emblem, and cause."

### Slide 14 — Claims · 9:20–10:20

- Now the step that I think is genuinely the interesting one for this audience.
- We convert commentary prose into **atomic claims**. And the right analogy is the index card, or
  a Zettelkasten slip. One card, one fact.
- Each card carries: the **verbatim Tibetan**, an English gloss, a **type**, what it's *about*, and
  a **block-level citation**.
- Here are the five real claims from that one node of Gendün Drub. Point at the types: this one is
  a *word-gloss* — "blue" refers to her body colour, "gold" indicates a clear hue. This one is
  *iconography* — her left ring-finger holds a water-born lotus at her heart, held so its opening
  faces her ear, and that is the sign of the ten pure perfections. This one is *structural* — it's
  just the commentator saying "secondly." That still gets a card, because knowing what's structure
  and what's content is itself information.
- Across the sixteen commentaries: **2,975 claims.**
- Two rules make this trustworthy, and both came out of a failure we had:
  - **Extract first, merge later.** Each commentary is read *in complete isolation* — never
    alongside another commentary, never alongside an earlier extraction. Because merge decisions
    made while reading rest on incomplete information: the first commentary you read silently
    defines the topic space for all the rest.
  - **One model call per node.** Each call sees only its own node's text and its own node's title.
    That makes the guarantees *structural* rather than disciplinary — a call that only ever sees
    one node physically cannot file a claim under the wrong node, and cannot import content from a
    commentary it was never shown.
- And behind it, a script re-checks every card: is this Tibetan string actually a literal substring
  of the block it cites? Was the claim count computed by counting, or inherited? *(That second
  check exists because an earlier method inherited counts instead of recomputing them, and we
  caught it.)*
- **Worth saying explicitly:** even if we never published a single Wikipedia article, this claims
  database — typed, school-tagged, block-located, across sixteen commentaries — is a research
  object for Tibetan studies in its own right.

### Slide 15 — Two routes · 10:20–10:50

- Now: which subjects get articles?
- **Route one — by structure.** Use the root text's own shape. Twenty-one homages, plus the
  benefits section, plus two recurring bodies of material that sit outside the homage sequence.
  Twenty-four slots, one article each.
- **Route two — by keyword.** Ask what the corpus actually spends its attention on, and write an
  article per subject.
- We do both. They converge again at consolidation, in two slides.

### Slide 16 — The keyword chain · 10:50–11:40 *(cut third if long)*

- The headline: **detect in English, measure in Tibetan.**
- The problem: Tibetan is written without word boundaries — the tsheg separates *syllables*, not
  words — so standard keyword statistics can't run on it directly. But here's the trick: *counting
  a string you already know* needs no word segmentation at all.
- So: generate a deliberately **literal** English translation, verse by verse, keeping every block
  ID. Literal, not literary — because published translations paraphrase, and a keyword absent in
  English is not absent in Tibetan.
- Run the standard tools over the English — TF-IDF and YAKE, treating each verse as its own
  document so that the words appearing in every verse get punished.
- Then, for each English candidate, open the same-numbered *Tibetan* block and identify the exact
  span it translates. Regroup by the **Tibetan** term.
- Why per-occurrence mapping matters — this is the part I'd want a translator to hear. Statistics
  on a translation measure the *translator's* vocabulary, and they lie in two directions at once.
  One Tibetan term splits across renderings — ཡེ་ཤེས་ becomes "wisdom," "gnosis," "pristine
  awareness," the count divides three ways and the term sinks. And two different Tibetan terms
  collapse into one English word — "wisdom" is both ཤེས་རབ་ and ཡེ་ཤེས་, and you get a merged count
  belonging to no actual term. Mapping per occurrence and regrouping by Tibetan fixes both.
- **193 plus 313 English candidates → 367 unique Tibetan terms.**
- Then scoring. Three signals, and raw frequency is deliberately the *weakest*:
  - **Attention** (dominant): how many claims are *about* the term, across how many commentaries.
  - **Structure**: does it appear in section titles? do commentaries explicitly define it?
  - **Presence** (tie-breaker only): frequency, counted in the commentators' own prose with
    root-text quotations excluded — because a commentary that quotes the verse inflates every
    word in it.
- The empirical validation is my favourite number in the project: **before** the attention signal,
  Tibetan intensifier particles sat in the top 20. **After** it, not one survives into the top 60.
  Frequency alone cannot tell ལྟ་བུ་ ("like") from ཡེ་ཤེས་ — both are everywhere. But no commentary
  ever *defines* ལྟ་བུ་. No section is titled by it. No claim is about it.
- Then a **mechanical** cutoff — calibrated once and frozen, so it's reproducible rather than a
  matter of taste: a term enters the queue only if at least half the commentaries engage it *and*
  at least twenty claims are about it. **114 of 367 pass.** Nothing is deleted — terms that fail
  stay in the registry as glossary candidates.
- Then a subject filter: is this an encyclopedic *subject*, or is it section material? A body part
  with a hundred claims is still section material. A deity with twenty is still standalone.
  **44 standalone subjects.**
- Finally we check the live wiki: does an article already exist? **25 update, 19 create.**
- **One aside worth thirty seconds:** the same Tibetan keyword list is what we use for
  standardising vocabulary in translation work. The keyword chain isn't only serving Wikipedia.

### Slide 17 — The spine map · 11:40–12:20

- Problem: every commentary numbers itself differently. One nests the seventh homage at 1.1.7.
  Another has it at top level as node 7. One runs all twenty-one homages inside a single
  undivided node with no internal structure at all.
- So before you can compare them, you need a shared coordinate system.
- **The analogy for this room:** Stephanus pagination for Plato. Bekker numbers for Aristotle. A
  fixed set of addresses that every edition can be mapped onto, so that a citation means the same
  thing no matter whose text you're holding.
- We build one small routing table per commentary — which of *its* nodes hold which canonical
  slot's content. Built once, reused by every topic afterwards.
- And that hard case — the commentary with all twenty-one homages in one undivided node — gets
  routed by **claim-ID range** instead, using its own "verse N quoted" claims as boundary markers.
- The invariant: every claim gets **exactly one** disposition. Routed, flagged ambiguous, or
  logged as unmapped. Never zero, which would be silent loss. Never two, which would be silent
  duplication. A script recomputes every count and refuses to finish if anything is undisposed.
- And "unmapped" is a *legitimate* outcome, not a failure — a commentary's own front matter,
  colophon, ritual appendices and story collections belong to no slot. Those claims are preserved;
  they just don't feed a topic page.

### Slide 18 — Consolidation as viva · 12:20–13:10

- Now we bring the sixteen back together. And the way we do it is the part I'd most want to
  defend in a seminar.
- **We don't ask "what does each commentary say" and summarise.** We put the *same question* to
  all sixteen and record the answers.
- The questions are **generated, not authored** — two free sources. From the spine, mechanically:
  twenty-one homages times the facets that recur across the corpus — name, colour, implements,
  stance, activity, mantra, benefit. And from the extractions themselves: every claim that one
  commentary makes implies a question you can ask of the other fifteen.
- So consolidation becomes a **derived completeness check**. Free reading first, then generated
  questions catch what free reading missed.
- Four possible outcomes per question:
  - **Consensus** — with the full attestation list, every commentary named.
  - **⚑ Divergence** — recorded, attributed, *never averaged*.
  - **Unique** — a single commentary's claim, attributed inline.
  - **Silence** — and this is the one I want to underline. If nobody addresses a question, that
    stays on the page marked "no commentary addresses this." It is never quietly deleted. **A
    silence in the tradition is a finding about the tradition.**
- And afterwards a script diffs the list of claims that went *into* the packet against every claim
  the finished page actually *cites*. Anything in the gap is either folded in or logged with a
  one-line reason. There's no third state. In the pilot, that check caught real gaps in roughly
  5–12% of a topic's claims per page.

### Slide 19 — What it finds · 13:10–14:00 *(protect this slide; cut something else)*

- Concretely, on the lotus page — ten generated questions, 120 claims from all sixteen
  commentaries.
- **Consensus:** wherever a commentary glosses the verse's own word པདྨ, it identifies the flower
  specifically as an **utpala** — a blue lotus — not a generic lotus. Four commentaries say it in
  so many words, and not one claim in the packet glosses it as any other species.
- **Divergence** — and here's where the method earns its keep. On Tārā's origin: most commentaries
  narrate Avalokiteśvara weeping, a lotus growing from his tears, and Tārā arising from its pollen.
  But **Tāranātha and Karma Maitri don't say that.** They say the pollen issues from
  Avalokiteśvara's "water-born face" — the face itself as a standing lotus epithet. No tears, no
  tear-event.
- And the way we established that is worth stating: the word སྤྱན་ཆབ — tears — **does not appear
  anywhere in either commentary's file.** Not "the model thinks they disagree." A checkable fact
  about two documents.
- We're careful about what we then assert: we record it as a difference in *what these
  commentaries' captured claims state*, not as a positive denial. A fuller account may sit
  elsewhere in their text. That distinction is written into the page.
- **And one more, which I did not expect the system to produce.** It surfaced a *root-text
  variant*. Our critical edition reads གསེར་སྔོ at homage three. Gendün Drub's text quotes
  སེར་སྔོ. One syllable — and the two readings license different etymologies.
- So this stopped being just an aggregator somewhere along the way. It's a philological
  instrument.

### Slide 20 — The article · 14:00–15:00

- And here's the article. In Tibetan, on པདྨ, with footnotes.
- Trace one footnote with the pointer: the sentence cites a named reference; the reference resolves
  to specific claim IDs; each claim carries verbatim Tibetan; that Tibetan cites a block; the block
  is in a named commentary file. Five links, and every one of them is checkable by hand.
- Two rules govern the drafting, and they're both refusals:
- **Claims-only drafting.** Once the claims table is built, **the drafting model never sees source
  wording again.** It writes from the claims list and cites *claim indices*. Code — not the model —
  expands each index back into its quotations and renders the references.
  - Why that's the crux: it means the model *cannot* smudge a quotation, because it was never
    shown one to smudge. And it's what makes a character-for-character check meaningful rather
    than decorative. This is verified in code, incidentally — the thing that builds the prompt
    passes nothing else.
- **No parametric knowledge.** No date, no Sanskrit form, no iconographic detail, no doctrinal
  framing that isn't in a claim — however standard it seems, however confident the model is.
- And the consequence I'm proudest of: of the 44 standalone subjects, **one was refused outright**
  — there weren't enough citable claims to write it. It has no article. The refusal is the evidence
  that the rule actually binds; a system that always produces an article isn't following a rule.
- Voice follows claim type, too: consensus can be stated in the plain encyclopedic voice.
  Anything below consensus takes mandatory in-text attribution — *this* commentator says this.

---

## ACT IV — Trust and publication (15:00 → 18:00)

### Slide 21 — Two checks · 15:00–16:15

- Two things check the work, and I want to be precise that **they check different things and
  neither replaces the other.**
- **The machine check.** Last in the chain, blocking, and uses no AI at all. It re-reads every
  quotation out of the file it cites. Across 42 batch articles: **861 of 882 quotations verify
  character for character.** In the deeply audited three-article pilot: **81 of 81**, and all 81
  block locators resolve to the exact block named.
- The tiers are deliberately unequal. An exact match passes. A match once you remove line-wrapping
  passes — line breaks aren't part of the text. But a match that only works once you *also* strip
  the Tibetan punctuation **fails**. Because if the letters agree and the punctuation doesn't, the
  article is not quoting what the file says.
- The story on the slide: the gate once caught a model silently promoting a tsheg to a shad
  *inside* a quotation. String similarity 0.974. Completely invisible to a human skimming Tibetan
  prose. Exactly the drift that makes a quotation stop being a quotation.
- And the articles are therefore ***sic*-faithful**. A transcription error in the source is
  reproduced, not silently repaired. Correcting the text is an editorial act and it happens at the
  source layer, by a human, or it doesn't happen.
- **The meaning check.** Because a script can prove a cited claim *exists*; only a reader can prove
  it *says what you attributed to it*.
- And here's the finding I'd most want to travel out of this talk. We audited the pilot drafts
  twice. **The same model auditing its own work returned "publish, no findings" — three for
  three.** An independent, different model found **five blocking errors** on two of the three.
- Four were genuine on manual adjudication. The clearest: the draft said "many scholars agree"
  where the underlying claim says **three**.
- The lesson, stated as a rule: **never report a same-model audit as independent.** An agent
  auditing its own output re-reads its own intentions, not the text.
- Two honesty notes I always include. The auditor shows round-to-round variance — re-running it
  three times on the fixed articles gave pass rates of 0.67, 0.67, and 1.0 — so we report audit
  outcomes as pass *rates*, never single verdicts. And twice the auditor **misquoted the draft
  inside its own finding**, inventing typos that weren't there. Model-written finding text is
  itself untrusted. Which is exactly why the deterministic check — the one that cannot hallucinate
  — sits underneath the audit rather than beside it.
- And on the rails side: a fresh model re-checked **all 418 citations** across three consolidated
  pages. Zero fabricated claim IDs. One critical finding, one moderate, about sixteen minor. Every
  one of those error classes was then turned into an executable rule or a standing check.
- **The line to land on:** we've now had pages where every single quotation was character-perfect
  and the meaning audit still found four critical defects. A clean quote check is never, by itself,
  publication-ready.

### Slide 22 — The humans, and the gate · 16:15–17:40

- Last part, and it's the part that took the longest.
- **None of this was built in one sitting.** Every skill you've seen went back and forth with
  Buddhist scholars and Tibetan language experts, several rounds each. They read the output, told
  us what was wrong, and we changed the skill — not the output.
- The clearest example: our project's Tibetan linguist, later joined by a Tibetan-language expert,
  read the first batch and came back with six findings.
  - Three about register: statements carry far more citations than they need; the articles read
    like a **literature review** rather than an encyclopedia — visibly stitched together from
    claims; and the raw wikitext is unreadable because of inline reference tags.
  - Three about orthography and respect: every paragraph must close with the double shad །།; **the
    comma does not exist in Tibetan** and must not appear; and commentators must be named in prose
    by a respectful, human-curated form of their name.
- Every one of those became a rule in a **new versioned drafting skill.** Consensus statements move
  to plain encyclopedic voice with at most three supporting references, and the full attestation
  list migrates to the citation trail so nothing is lost. At most two verbatim quotations per
  article, spent only where the exact wording is the point. And a human-curated respectful-name
  field on every commentary — which the model may only **copy**. It may never invent, translate, or
  upgrade an honorific.
- **That's the loop that actually matters.** A human reader's objection became executable. It will
  apply to every article we ever generate, and it will still apply when I'm not the one running it.
- We also gated it: three revised articles are with the linguist now, and the corpus-wide redraft
  waits on that approval. We don't batch-redraft ahead of the human.
- **Publication.** Two paths. If no article exists — 19 subjects — we create one. If one already
  exists — 25 subjects — we **update** it with cited sections. One subject, one article. We never
  fork into "X according to the Tārā commentaries."
- Right now every publication step is manual. Later it's a bot, and it will publish only what has
  already passed review — the bot moves text, it never decides.
- **And: nothing has been published yet.** On purpose. The target wiki has no local policy on
  machine-assisted content, and we read that vacuum as *stop*, not as permission. Before any
  mainspace edit there'll be a public bilingual proposal on the community forum and an on-wiki
  project page listing every pipeline-assisted article with its reviewer and its sources. Every
  edit will disclose the machine assistance.
- There's also a debt I'll name: not one of our citations yet carries a public URL, so a reader
  can't check a quotation online yet. That's our single largest pre-publication task.
- **The economics, in one breath:** machine cost is about seventy cents an article. It is not the
  constraint. **Human review is the constraint, by design.** At 30–60 reviewer-minutes an article,
  100,000 articles is 24 to 48 person-years of review, spread across a community — against roughly
  285 years of *writing* at the current rate. That's the whole argument in one comparison:
  supervised automation turns a writing problem measured in generations into a reviewing problem
  measured in person-years. And reviewing parallelises across every fluent speaker you can recruit.
- **Close:** "The answer to the gap I opened with is neither refusal nor flood. It's verification,
  with a human hand on the gate."

---

## Q&A — prepared answers

**"Isn't this just going to flood the wiki with AI slop?"**
Throughput is bounded by human review capacity, not by model capacity — that's a design property,
not a promise. Nothing publishes without a named human. Every edit discloses machine assistance.
And nothing at all has been published yet, because the community hasn't been consulted. The wikis
that were damaged were damaged by unaccountable *volume*: content nobody fluent verified, at rates
nobody could review, with no disclosure. Every one of those properties is negated here.

**"Who takes responsibility for an error?"**
A named human editor, who is the sole publishing agent. The pipeline reduces the surface a reviewer
has to distrust. It does not abolish editorial responsibility, and it isn't meant to. I'll say the
residual risk out loud: a fluent reviewer can still wave through a subtly wrong article.

**"How do you handle sectarian bias?"**
Two ways. Divergences are never flattened — every position is recorded and attributed, and the page
adjudicates none of them. And a school with exactly one representative in the corpus has its
positions typed *school-position*, never *fringe* — sole representation is a fact about our
corpus, not about the tradition. That said, the corpus *is* skewed: seven of sixteen are Geluk.
I treat that as data the system must respect, not as noise.

**"Is this Wikipedia-notable? Aren't these primary sources?"**
Two gates. Corpus breadth proposes — a term explained across many commentaries is encyclopedic; a
term one commentator happens to use isn't. But breadth is salience *within the corpus*, not
notability in Wikipedia's sense. The publication layer disposes: no article without at least one
independent reliable secondary source, and a human curator makes that call.

**"What about copyright on the commentaries?"**
None of the major Tibetan digital libraries license their *text* for the CC BY-SA reuse Wikipedia
requires. That constraint is a design principle rather than an obstacle: we cite, we quote
minimally under a hard cap, and we never copy. At most two verbatim quotations per article.

**"Could I run this on my corpus?"**
It needs a root text, commentaries, and a curated registry. Nothing in the architecture is specific
to twenty-one homages — the machinery is already prepared over the Bodhicaryāvatāra with ten
commentaries, which is also where the reception/refutation machinery will actually get tested,
because a praise-commentary corpus produces zero contested claims. Sanskrit, Pāli and classical
Chinese scholasticism have the same shape: layered canon, commentarial tradition, school structure.

**"Which model do you use? Does it matter?"**
The library is model-agnostic. The reported runs used Claude Sonnet for drafting and Gemini Flash
for the cross-model audit. And I'd stress the *cross*-model part is the load-bearing bit, not which
two. The model asymmetry in Tibetan is real and we report it as a finding, not a design choice.

**"What was the hardest technical lesson?"**
Batch the question smaller. Measured directly: the same model on the same prompt returned ten
passages totalling 873 characters when we gave it 93,000 characters of context — and twenty
passages totalling 5,224 when we gave it 12,000. The model budgets its answer against the size of
the question. You cannot fix that by shouting louder in the prompt. It's architectural, and it's
why claims extraction now runs one isolated call per outline node.

**"Why Obsidian and markdown, rather than a database?"**
Because the review surface is the thing that has to work for humans. Sources, claims and drafted
articles are all plain files. A citation is an address that *renders* — a note can transclude the
block it cites, so the cited Tibetan appears inline inside the note citing it, and a reviewer
checks a quotation by reading down the page rather than by trusting our verification report.
Review state is a field in the file. And the whole review history is a git history, so every
reviewer edit is a commit you can diff against what the machine generated.
