# Speaker notes — what to say on each slide

Talking points, not a script. The slides carry almost no text, so **the talk is the content**.
Timings are cumulative; if you're past time on a slide, skip ahead rather than compress.

## Working the 50/50 room

Half the audience knows Tibetan textual traditions cold and nothing about software. Half is the
reverse. **Don't average — layer.**

The move, on every technical point:
> **Name it plainly → give the analogy → then state the mechanism precisely.**

The first two sentences are for everyone. The third is where the engineers lean in — and the
humanities half still follows, because the analogy already did the work. Cues below are marked
**[HUM]** and **[TECH]**; say both, in that order.

**Two deliberate flips.** Give the technical half something they didn't expect from a
Tibetan-studies talk — the isolation architecture (slide 16), the context-size finding (12b), the
same-model audit result (22). Give the humanities half something that is *real philology* — the
divergence and the root-text variant (20). Those are the two things people will repeat afterwards.

**Never say** "pipeline stage," "orchestrator," or "gate" without the plain version first.
**Do say** the precise mechanism after it — this room can take it, and half of them want it.

**Three rhetorical moves carry the whole talk:**
1. The problem is not a lack of material. Tibetan has *more* classical literature than the
   languages doing this well.
2. The scary thing about AI on small wikis already happened, and it was a disaster. This is the
   opposite of that, and I'll show you why.
3. The machine has judgement everywhere in this system and **authority nowhere**.

---

# ACT I — The gap (0:00 → 4:00)

### 1 — Title · 0:00–0:20
- Name, project, one-line frame.
- "A talk about making Tibetan legible to machines — without letting machines decide what
  Tibetan says."

### 2 — Two numbers · 0:20–1:00
- Seven million speakers. One of the largest classical literatures in Asia.
- Eight thousand articles. *(Use the fresh count.)*
- ~36 active editors a month. Two administrators. ~350 new articles a year.
- Eighteen years after founding, the whole Tibetan Wikipedia is about the size of one
  English-language WikiProject.
- **Pause.** Don't explain it.

### 3 — Who does more with less · 1:00–1:40 *(cut 3rd)*
- Welsh, 2017: the Welsh Government made growing Wicipedia **explicit policy**, stated reason
  being to make Welsh visible to technology companies.
- 91,000 → 280,000+. Became the most-viewed Welsh-language website. Welsh machine translation
  improved on the back of it.
- That's this talk's argument, made a decade earlier, by a government, with results.
- **The chart's point:** every language here has *fewer speakers and a smaller classical corpus*
  than Tibetan. The constraint was never material. We have more material than almost anyone. What
  we lack is the conversion.

### 4 — The models can't read us · 1:40–2:30
- This used to be about visibility. It's now about capability.
- TLUE benchmark, Tibetan multiple-choice: most large models score **below random guessing**.
  GPT-4 at 17.5% against a 25% floor.
- The one to point at: **Qwen-2.5-72B, 84.7% in Chinese, 16.5% in Tibetan.** Same model, same
  week.
- Worse than a coin toss isn't "needs work." It means the language is effectively absent from
  training data.
- **[TECH]** And there's a tokenisation tax on top: byte-level tokenisers make Tibetan roughly
  **4× more expensive** to process than Chinese (Petrov et al. 2023). We pay more per word to be
  served worse. If you're building anything on top of these models in Tibetan, you feel both.
- The Wikipedia link: by Wikimedia's own account, Wikipedia is almost always the single largest
  source in a model's training corpus, and per-language performance tracks a language's share of
  pretraining text.
- So when an assistant fails a basic question about Tibetan culture asked *in Tibetan*, it isn't
  because the knowledge is obscure. The open text those systems learned from barely includes us.

### 5 — The loop has a sign · 2:30–3:15
- It's a loop, and it currently runs the wrong way: absence begetting absence.
- **Left:** no articles → little training text → tools can't serve the language → fewer people
  work in it online → still no articles. Kornai named the endpoint: *digital language death*.
- **Right:** cited articles → digital footprint → better tools → faster articles.
- **The thing to hold for the rest of the talk: it's the same loop.** Identical machinery. The
  only thing that sets the direction is whether anything was verified before publication.

### 6 — Three options · 3:15–4:00
- Only three ways to grow a small-language Wikipedia to useful size.
- **By hand.** Arithmetic in a moment.
- **Unsupervised.** Not hypothetical, and I'll name it before anyone else does. Scots: ~23,000
  articles by one enthusiastic non-speaker — credibility destroyed. Cebuano: six million bot
  stubs, repeated closure proposals. **Greenlandic: closed by the Language Committee in 2025**
  over machine-generated content. Inuktitut estimated two-thirds MT-contaminated. Several
  African-language wikis at 40–60% uncorrected machine translation.
- So "AI content for small Wikipedias" currently names a disaster, not a hope. I want to be very
  clear I know that.
- **Supervised** is the third option, and the rest of this talk is an existence proof.
- One counterweight: Content Translation — machine draft plus **mandatory** human edit — produces
  articles with **lower** deletion rates than from-scratch ones, across 2.4M+ creations. The
  failure mode and the working mode differ in exactly one variable.

---

# ACT II — How the work is done (4:00 → 8:00)

### 7 — The arithmetic of "by hand" · 4:00–4:35 *(cut 2nd)*
- Dzongkha Wikipedia Education Program, Bhutan — closest Tibetic-script precedent, fully manual.
  Institutional backing, dozens of trained participants, five months. **Eighty articles.**
- bo.wikipedia: ~350 articles a year.
- 100,000 articles — call that minimally serviceable — is **more than two centuries** away.
- **Say deliberately:** that is not a criticism of the editors. Some of the most committed
  volunteers in any language community. It's the measured capacity of the mode.

### 8 — Agent and harness · 4:35–5:10
- Two words I'll use throughout, defined plainly.
- **[HUM]** The model — Claude, in our case — reads Tibetan and makes judgements. It's the
  apprentice. The **harness** is everything around it: what files it can open, what it may write,
  which tools it can run, what rules are pinned above the bench. Workshop and apprentice. The
  workshop is what makes the work *reproducible* rather than *improvisational*.
- **[TECH]** Concretely, the harness is four things: the **tools** exposed to the model (read,
  write, run a script, search), the **context** — precisely what it is allowed to see on any given
  call — the **rules** loaded per task, and the **loop** that runs read → judge → write → check
  without a human between steps. That's all "agent" means here.
- No database. Everything is plain markdown in an Obsidian vault, and Claude Desktop reads and
  writes those files directly. Every intermediate stays human-readable and reviewable in place —
  which turns out to matter enormously at the review step, and I'll come back to it.

### 9 — Skills: the Matrix analogy · 5:10–5:50
- **[HUM]** The analogy I find most useful is from *The Matrix*. Neo needs to fight. He doesn't
  train for years. Someone loads a program — "I know kung fu."
- **A skill is exactly that.** A file of step-by-step instructions for one operation, loaded into
  the model immediately before it does that operation.
- The model does **not** know how to extract a sa-bcad tree from a Tibetan commentary. Nothing in
  its training taught it our conventions. The skill file says: here's what a sa-bcad announcement
  looks like, here are the five passes, here's the numbering scheme, here's what to do when the
  declared count doesn't match the children you found.
- **[TECH]** To be precise about what it is *not*: not fine-tuning, not a plugin, not code. It's a
  markdown procedure injected into context, versioned in git. When we change how something is
  done we write a **new version** and record what changed and why — never rewrite a shipped one in
  place, because then you can no longer say what produced last month's output.
- This vault has **62 of them. Eleven thousand lines** of written-down method.

### 10 — Anatomy of a skill · 5:50–6:30 *(technical-led)*
- Here's what's actually inside one. Six sections, and the order is deliberate.
- **"Why this skill exists, and what it is not"** — the reasoning, and usually the failure that
  produced it.
- **Inputs / Output / Output format** — the contract.
- **Rules**, numbered.
- **Procedure**, numbered steps.
- **A completion check** — how you know you're done.
- And about a third of them carry **scripts**: 21 of 62, 44 scripts total, that re-check
  mechanically whatever can be re-checked mechanically.
- **[HUM] — the line that matters most here:** a skill is a *text file*. A Buddhist scholar can
  open it, read it, disagree with it, and edit it. That is not true of a prompt buried inside
  code. It's the reason the domain experts on this project can actually govern the system rather
  than just receive its output.

### 11 — Why the rules exist · 6:30–7:20 *(protect this slide)*
- I want to show you three real rules and what produced each one, because this is the part I'd
  most want another project to copy.
- **Rule: "`claim_count` is computed by counting, at the end — never inherited."** That exists
  because we once ran what we believed was a second, independent extraction of a commentary. It
  wasn't. It was a re-bucketing of the first run: **114 of 118 Tibetan strings byte-identical**,
  counts copied rather than recomputed, transcription errors inherited unchanged. And because it
  looked like corroboration, it *hid* real defects — including a cross-document contamination and
  a fabricated mantra that had been promoted to canonical status.
- **Rule: "Corroboration must be re-read, not remembered."** From the adversarial audit. A "three
  flaws" framing of Tārā's face was attributed to a second commentary as independent
  corroboration. That commentary's cited claim contains no flaws framing at all. The consolidator
  had the right idea somewhere in the corpus and attached the wrong claim ID.
- **Rule: "Counts are computed, never hand-tallied."** On the worst pilot page, **five of five**
  "(N commentaries)" labels were wrong.
- **The generalisable point — say this slowly:** we don't fix a bad output by re-running with a
  better prompt. We identify the *class* of error, write it into the skill as a numbered rule,
  and where possible add a script that fails the build. **The fix outlives the person who found
  it.** A skill is institutional memory. Every rule in it is a scar.
- **[TECH]** Three principles repeat across all 62: *the model judges, the script verifies*;
  *isolation over context*; *nothing interpretive touches the source layer*.

### 12 — Scripts: the machine · 7:20–7:50
- The other half is scripts — small Python programs. The analogy is a machine. Something goes in
  the hopper, rules are bolted to the side, the same thing comes out every time. No judgement, no
  interpretation, no mood. **A machine cannot be persuaded.**
- **The single most important design decision in this project is one sentence:** *the model
  judges; the script verifies.*
- Judgement work: is this line a structural announcement or prose? Does this gloss say the flower
  is blue or clear-hued? Which commentaries actually disagree? That's a reader's job.
- Machine work: does this exact string appear, character for character, in the file it claims to
  come from? Do the counts recompute? Does every claim have exactly one disposition? That's a
  ruler's job.
- **[TECH] And the asymmetry is the load-bearing part: the script has the final say.** If the
  model says "publish" and the machine says the quotation doesn't match, the build fails. There
  is no override flag. We deliberately did not build one, and we've turned down asking for one
  twice.

### 12b — The context-size finding · 7:50–8:20 *(cut 4th — but the technical half will thank you)*
- One measured result I'd hand to anyone building something like this.
- Same model, same prompt, different amount of context. Given **93,000 characters**, it returned
  ten passages totalling **873 characters**. Given **12,000 characters**, it returned twenty
  passages totalling **5,224**.
- **The model budgets its answer against the size of the question.** Not against the task.
- Our capture rates in the pilot, measured against what the previous step actually offered:
  45%, 19%, and **1.1%**.
- You cannot fix that in the prompt. We tried. It's architectural — batch the question smaller —
  and it's exactly why claims extraction now runs **one isolated call per outline node** instead
  of one call per commentary.

---

# ACT III — One verse, all the way through (8:20 → 16:00)

### 13 — The corpus · 8:20–9:00
- The case study: *Praise to the Twenty-One Tārās*, Tohoku 438, in the Kangyur, attributed by
  tradition to Vairocana. Probably the most widely recited Tārā liturgy across every Tibetan
  tradition.
- **Sixteen commentaries. 582,332 Tibetan characters. 3,268 citable blocks. 580 outline nodes.
  2,975 claims.** Drakpa Gyaltsen, the First and Second Dalai Lamas, Tāranātha, Ngulchu
  Dharmabhadra, Khenchen Palden Sherab, living teachers. Sakya, Geluk, Jonang, Nyingma, Kagyü.
- Chosen because it's **bounded and heavily commented** — small enough to audit completely, rich
  enough that every generated sentence can be checked against a named human source.
- One note this room will care about: our root text is a **critical edition**, not an OCR export.
  The export we replaced had wrong verse segmentation and stopped mid-clause at the twenty-first
  homage, omitting the benefits section every commentary comments on. The edition's own apparatus
  records that its two witnesses differ at **17 of the 21 homages**.
- **The promise:** I'm going to take one verse — the third homage — and one commentary — Gendün
  Drub, the First Dalai Lama — and follow them to a finished article. Every screen from here is a
  real file.

### 14 — Getting the text in · 9:00–9:45
- Most of this exists as **images**. Scans from BDRC and elsewhere. So step one is OCR. Sometimes
  we get a text version off the internet instead, which needs a different kind of cleaning.
- **[TECH]** Cleaning runs under a rule worth stating: the script first builds a **profile** of
  the mechanical debris it found — page-number lines, running headers, the wrong tsheg character
  — shows that profile to a human, and only then runs a cleaner limited to *exactly* those fixes.
  It never interprets. A doubtful reading is a question for the editor.
- Then segmentation — cutting the commentary into citation-sized blocks by a rule engine over
  seven lexical boundary cues, with verse stanzas detected by their metre and peeled out whole.
  Behind a **no-loss gate**: if the segmented text differs from the original by one
  non-whitespace character once whitespace is squeezed out, the script aborts and writes nothing.
  Residue no cue can safely cut goes to a human under a stated bias — *over-long is safer than
  wrong*.
- **And then the thing everything depends on.** Every block gets a permanent address.
- **[HUM]** A footnote pointing at a *file* is a promise. A footnote pointing at a *block* is an
  address — somebody can open it. Every citation in every artifact I'm about to show resolves to
  one of these.

### 15 — The sa-bcad tree · 9:45–10:30
- Tibetan commentators announce their own structure. "This has two parts." "The second has six."
  That's the sa-bcad, and it's the architecture of the argument.
- We extract it as a nested outline with a pointer from every node into the source.
- This is Gendün Drub's: **37 nodes, seven levels.** Look at the leaves under "extended
  explanation" — exactly twenty-one. The tree recovered the praise's own architecture as the
  commentator declared it. Nobody imposed it.
- **[TECH]** Extraction runs as **five isolated passes** — chunk, extract candidates, copy the
  enumeration announcements verbatim, build, check — and the reason is a finding about prompt
  design that I think generalises: *a call that never sees the tree-building instructions cannot
  drift into tree-building*, and a verbatim-copy call that never sees the words "interpret and
  reconcile" stays literal. When we merged those jobs into one call, precision measurably
  dropped.
- The tree-builder treats the author's **own enumerations as more authoritative than individual
  candidates**: if he declares six parts, six children must appear, and the child count must
  match. Doctrinal lists — things enumerated as subject matter rather than as divisions of the
  text — never become nodes.
- The highlighted branch is where our verse lives: node 2.2.2.2.1.1.2, "praise by way of her body
  colour, hand-emblem, and cause."

### 16 — Claims · 10:30–11:30
- The step I think is genuinely the interesting one.
- We convert commentary prose into **atomic claims**. **[HUM]** The right analogy is the index
  card, or a Zettelkasten slip. One card, one fact.
- Each card carries: **verbatim Tibetan**, an English gloss, a **type**, what it's about, and a
  **block-level citation**.
- Five real claims from that one node. Point at the types. *Word-gloss:* "blue" refers to her body
  colour, "gold" indicates a clear hue. *Iconography:* her left ring-finger holds a water-born
  lotus at her heart, held so its opening faces her ear — the sign of the ten pure perfections.
  *Structural:* the commentator simply saying "secondly." That still gets a card, because knowing
  what's structure and what's content is itself information.
- Across sixteen commentaries: **2,975 claims.**
- **[TECH] Two invariants, both from failures.**
  - **Extract first, merge later.** Each commentary read in complete isolation — never alongside
    another commentary, never alongside an earlier extraction. Because merge decisions made while
    reading rest on incomplete information: the first commentary you read silently defines the
    topic space for all the rest.
  - **One isolated call per node.** Each call receives *only* the extraction rules, the file path
    and its own line range, and its node's decimal and title. Nothing else. It is never given the
    paths of other extractions, and never sees the merged file being built.
- **The consequence is the sentence I'd underline:** a call that only ever sees one node
  *cannot* file a claim under the wrong node, and *cannot* import content from a commentary it
  was never shown. **The guards are structural, not disciplinary.** We're not asking the model to
  behave. We removed its ability to misbehave.
- And underneath, a script re-checks every card: is this Tibetan actually a literal substring of
  the block it cites — testing ellipsis-joined fragments individually, which catches a claim
  quoting one real phrase and one invented one. Was the count computed by counting or inherited?
- **Worth saying:** even if we never published a single Wikipedia article, this claims database —
  typed, school-tagged, block-located, across sixteen commentaries — is a research object for
  Tibetan studies in its own right.

### 17 — Sixteen commentaries are not sixteen of the same thing · 11:30–12:10 *(cut 1st)*
- A finding the corpus produced by itself, which I didn't expect.
- **Claim density varies eightfold.** Karma Maitri: 181 claims per ten thousand characters.
  Khenpo Tsultrim Namdak: 23. Both are careful commentaries.
- **[HUM]** That's a genre fact. A word-commentary — *tshig 'grel* — is almost nothing but
  glosses, so it's dense. An expansive *rnam bshad* with sādhana sequences and ritual appendices
  is long, and much of its length isn't claim-bearing.
- **[TECH]** And it's the reason a uniform chunk size or a per-commentary token budget would have
  been wrong. The unit of work has to be the *outline node*, not a fixed slice of characters.
- The structural spread is even wider: outline nodes per commentary run from **2** — Drakpa
  Gyaltsen's word-commentary has almost no sa-bcad at all — to **120** for Khenchen Palden
  Sherab. Sixty-fold.
- Which sets up the next problem exactly.

### 18 — The spine map · 12:10–12:55
- Every commentary numbers itself differently. One nests the seventh homage at 1.1.7. Another has
  it at top level as node 7. One runs all twenty-one inside a single undivided node with no
  internal structure at all.
- Before you can compare them, you need a shared coordinate system.
- **[HUM]** Stephanus pagination for Plato. Bekker numbers for Aristotle. A fixed set of
  addresses every edition maps onto, so a citation means the same thing regardless of whose text
  you're holding.
- **[TECH]** One small routing table per commentary — which of *its* nodes hold which canonical
  slot. Built once, reused by every topic afterwards. The problem it solves is a complexity
  problem: answering that question inside every topic run meant roughly **400 full-file reads**
  over an unchanged multi-megabyte corpus. Sixteen judgements instead of four hundred — because
  "which node is Tārā 5" and "which node is Tārā 12" are the same act of reading the tree.
- The hard case, the one with all twenty-one homages in one undivided node, is routed by
  **claim-ID range** instead, using its own "verse N quoted" claims as boundary markers.
- **The invariant:** every claim gets **exactly one** disposition. Routed, flagged ambiguous, or
  logged unmapped. Never zero — that's silent loss. Never two — that's silent duplication. A
  script recomputes every count and refuses to finish if anything is undisposed.
- And "unmapped" is a **legitimate outcome**, not a failure. A commentary's own front matter,
  colophon, ritual appendices and story collections belong to no slot. Those claims are preserved;
  they just don't feed a topic page.

### 19 — Consolidation as viva · 12:55–13:45
- Now we bring the sixteen back together, and this is the part I'd most want to defend in a
  seminar.
- **We don't ask "what does each commentary say" and summarise.** We put the *same question* to
  all sixteen and record the answers.
- **[TECH]** The questions are **generated, not authored** — two free sources. Mechanically from
  the spine: twenty-one homages times the facets that recur across the corpus — name, colour,
  implements, stance, activity, mantra, benefit. And from the extractions themselves: every claim
  one commentary makes implies a question you can put to the other fifteen.
- So consolidation becomes a **derived completeness check**. Free reading first; generated
  questions then catch what free reading missed.
- Four outcomes per question:
  - **Consensus** — full attestation list, every commentary named.
  - **⚑ Divergence** — recorded, attributed, *never averaged*.
  - **Unique** — a single commentary's claim, attributed inline.
  - **Silence** — and I want to underline this one. If nobody addresses a question, it stays on
    the page marked "no commentary addresses this." Never quietly deleted. **A silence in the
    tradition is a finding about the tradition.**
- **[TECH]** Afterwards a script diffs the claims that went into the packet against every claim
  the page actually cites. Anything in the gap is folded in or logged with a one-line reason.
  There is no third state. That check caught real gaps in **5–12%** of a topic's claims per page —
  material that free reading had simply passed over.

### 20 — What it finds · 13:45–14:45 *(protect)*
- Concretely, the lotus page: ten generated questions, 120 claims, all sixteen commentaries.
- **Consensus:** wherever a commentary glosses the verse's own word པདྨ, it identifies the flower
  specifically as an **utpala** — a blue lotus — not a generic lotus. Four say it in so many
  words, and not one claim in the packet glosses it as any other species.
- **Divergence** — where the method earns its keep. On Tārā's origin, most commentaries narrate
  Avalokiteśvara weeping, a lotus growing from his tears, Tārā arising from its pollen.
- **But Tāranātha and Karma Maitri don't say that.** They say the pollen issues from
  Avalokiteśvara's "water-born face" — the face itself as a standing lotus epithet. No tears, no
  tear-event.
- **And how we established it:** the word སྤྱན་ཆབ — tears — **does not appear anywhere in either
  commentary's file.** Not "the model thinks they disagree." A checkable fact about two documents.
- We're careful about what we then assert: the page records it as a difference in *what these
  commentaries' captured claims state*, not as a positive denial — a fuller account may sit
  elsewhere in their text. That epistemic distinction is written into the output, not left to the
  reader.
- **And one I did not expect the system to produce.** It surfaced a **root-text variant**. Our
  critical edition reads གསེར་སྔོ at homage three. Gendün Drub's text quotes **སེར་སྔོ**. One
  syllable — and the two readings license different etymologies.
- Somewhere along the way this stopped being an aggregator. It's a philological instrument.

### 21 — The article · 14:45–15:40
- Here's the article. In Tibetan, on པདྨ, with footnotes.
- Trace one footnote: the sentence cites a named reference; the reference resolves to specific
  claim IDs; each claim carries verbatim Tibetan; that Tibetan cites a block; the block sits in a
  named commentary file. Five links, every one checkable by hand.
- **[TECH] Two rules govern drafting, and both are refusals.**
- **Claims-only drafting.** Once the claims table exists, **the drafting model never sees source
  wording again.** It writes from the claims list and cites *claim indices*. Code — not the model
  — expands each index back into its quotations and renders the references.
  - Why that's the crux: the model **cannot** smudge a quotation, because it was never shown one
    to smudge. It's what makes a character-exact check meaningful rather than decorative. And
    it's verified in code — the thing that builds the prompt passes nothing else.
- **No parametric knowledge.** No date, no Sanskrit form, no iconographic detail, no doctrinal
  framing that isn't in a claim — however standard it seems, however confident the model is.
- **The evidence the rule binds:** of 44 standalone subjects, **one was refused outright** —
  not enough citable claims. It has no article. A system that always produces an article isn't
  following a rule.
- Voice follows claim type: consensus may sit in the plain encyclopedic voice; anything below
  consensus takes **mandatory in-text attribution**.

---

# ACT IV — Trust and publication (15:40 → 18:40)

### 22 — Two checks · 15:40–16:40
- Two things check the work, and I want to be precise: **they check different things and neither
  replaces the other.**
- **The machine check.** Last in the chain, blocking, no AI at all. It re-reads every quotation
  out of the file it cites. Batch: **861 of 882 character-for-character.** Deeply audited pilot:
  **81 of 81**, and all 81 block locators resolve to the exact block named.
- **[TECH] The tiering is the policy, and it's deliberately unequal.** Exact match passes. Match
  once line-wrapping is removed passes — wrapping isn't part of the text. But a match that only
  works once you *also* strip Tibetan punctuation **fails**, because if the letters agree and the
  punctuation doesn't, you're not quoting what the file says. *Found is not the gate. Passed is
  the gate.*
- The story: the gate once caught a model silently promoting a **tsheg to a shad** inside a
  quotation. String similarity **0.974**. Invisible to a human skimming Tibetan prose. Exactly
  the drift that makes a quotation stop being a quotation.
- And the comparison runs through a **reading view** — the source with every layer we added
  stripped back off, not one Tibetan character touched — so a faithful quotation spanning a block
  boundary can never fail on a caret we wrote ourselves.
- Consequence: articles are ***sic*-faithful**. A transcription error in the source is reproduced,
  not silently repaired. Correcting the text is an editorial act; it happens at the source layer,
  by a human, or not at all.
- **The meaning check.** Because a script can prove a cited claim *exists*; only a reader can
  prove it *says what you attributed to it*.
- **And here's the finding I'd most want to leave this room.** We audited the pilot drafts twice.
  **The same model auditing its own work returned "publish, no findings" — three for three.** An
  independent, different model found **five blocking errors** on two of the three. Four genuine
  on manual adjudication. The clearest: the draft said "many scholars agree" where the underlying
  claim says **three**.
- **Never report a same-model audit as independent.** An agent auditing its own output re-reads
  its own intentions, not the text.

### 23 — What the audits measured · 16:40–17:20
- Walk the table quickly; don't read every row.
- Rails side: a fresh context re-checked **all 418 citations** across three consolidated pages.
  Zero fabricated claim IDs. One critical, one moderate, about sixteen minor. Every error class
  became an executable rule or a standing check.
- **Two honesty notes I always include.** Of 293 validator findings, **269** are one
  reference-format mismatch between two drafting routes — a mechanical reconciliation, not
  fabricated citations. And twice the auditor **misquoted the draft inside its own finding**,
  inventing typos that weren't there. Model-written finding text is itself untrusted — which is
  precisely why the deterministic check, which cannot hallucinate, sits *beneath* the audit
  rather than beside it.
- The auditor also shows round-to-round variance — three re-runs on fixed articles gave pass
  rates of 0.67, 0.67, 1.0 — so we report audit outcomes as pass **rates**, never single verdicts.
- **And the batch confirmed the division of labour the hard way:** on the first two keyword pages
  audited, **every quotation was character-perfect** and the meaning audit still found four
  critical defects — a divergence manufactured out of English-gloss noise over identical Tibetan,
  an inverted corpus fact, a citation corroborating content it doesn't contain, and a uniqueness
  claim pinned to the wrong ID.
- **A clean quote check is never, by itself, publication-ready.**

### 24 — The humans, and the loop that matters · 17:20–18:10
- Last part, and it took the longest.
- **None of this was built in one sitting.** Every skill went back and forth with Buddhist
  scholars and Tibetan language experts, several rounds each. They read the output, told us what
  was wrong, and **we changed the skill — not the output.**
- The clearest example: our Tibetan linguist, later joined by a Tibetan-language expert, read the
  first batch and returned six findings.
  - Register: statements carry far more citations than they need; the articles read like a
    **literature review** rather than an encyclopedia — visibly stitched together from claims;
    raw wikitext unreadable because of inline reference tags.
  - Orthography and respect: every paragraph must close with the double shad །།; **the comma does
    not exist in Tibetan** and must not appear; commentators must be named in prose by a
    respectful, human-curated form of their name.
- Every one became a rule in a **new versioned drafting skill**. Consensus statements move to
  plain encyclopedic voice with at most three supporting references, the full attestation list
  migrating to the citation trail so nothing is lost. At most two verbatim quotations per article,
  spent only where the exact wording is the point.
- **The respect rule is the one I'd dwell on:** a human-curated name field on every commentary
  that the model may only **copy**. It may never invent, translate, or upgrade an honorific.
- **That's the loop that actually matters.** A human reader's objection became executable. It
  applies to every article we will ever generate, and it will still apply when I'm not the one
  running it.
- And we gated it: three revised articles are with the linguist now; the corpus-wide redraft waits
  on that approval. We don't batch-redraft ahead of the human.

### 25 — Publication and economics · 18:10–18:40
- **Two paths.** If no article exists — 19 subjects — create. If one exists — 25 — **update** it
  with cited sections. One subject, one article. Never forked into "X according to the Tārā
  commentaries."
- Every publication step is manual now. Later it's a bot, and the bot publishes only what already
  passed review. **The bot moves text; it never decides.**
- **Nothing has been published yet. On purpose.** The wiki has no local policy on machine-assisted
  content, and we read that vacuum as *stop*, not permission. Before any mainspace edit: a public
  bilingual proposal on the community forum, an on-wiki project page listing every assisted
  article with its reviewer and sources, and disclosure on every edit.
- A debt I'll name: not one citation yet carries a public URL, so a reader can't check a quotation
  online. Our largest pre-publication task.
- **The economics in one breath:** machine cost is about **seventy cents an article**. Not the
  constraint. **Human review is the constraint, by design.** At 30–60 reviewer-minutes an article,
  100,000 articles is **24–48 person-years** of review spread across a community — against roughly
  **285 years of writing** at the current rate. Supervised automation turns a writing problem
  measured in generations into a reviewing problem measured in person-years. And reviewing
  parallelises across every fluent speaker you can recruit.
- **Close:** *"The answer to the gap I opened with is neither refusal nor flood. It's
  verification, with a human hand on the gate."*

---

# Q&A — prepared answers

**"Isn't this going to flood the wiki with AI slop?"**
Throughput is bounded by human review capacity, not model capacity — a design property, not a
promise. Nothing publishes without a named human. Every edit discloses machine assistance. Nothing
at all has been published yet, because the community hasn't been consulted. The wikis that were
damaged were damaged by unaccountable *volume*: content nobody fluent verified, at rates nobody
could review, with no disclosure. Every one of those properties is negated here.

**"Who takes responsibility for an error?"**
A named human editor, the sole publishing agent. The pipeline reduces the surface a reviewer must
distrust. It doesn't abolish editorial responsibility and isn't meant to. Residual risk, said out
loud: a fluent reviewer can still wave through a subtly wrong article.

**"How do you handle sectarian bias?"**
Divergences are never flattened — every position recorded and attributed, the page adjudicating
none. And a school with exactly one representative has its positions typed *school-position*,
never *fringe* — sole representation is a fact about our corpus, not about the tradition. That
said, the corpus *is* skewed: seven of sixteen are Geluk. That's data the system must respect, not
noise.

**"Is this Wikipedia-notable? Aren't these primary sources?"**
Double-gated. Corpus breadth *proposes* — a term explained across many commentaries is
encyclopedic; a term one commentator happens to use isn't. But breadth is salience *within the
corpus*, not notability in Wikipedia's sense. The publication layer *disposes*: no article without
at least one independent reliable secondary source, human curator making the call.

**"What about copyright on the commentaries?"**
None of the major Tibetan digital libraries license their *text* for the CC BY-SA reuse Wikipedia
requires. We treat that as a design principle: cite, quote minimally under a hard cap — at most
two verbatim quotations per article — never copy.

**"Which model, and does it matter?"**
Model-agnostic library. Reported runs used Claude Sonnet for drafting, Gemini Flash for the
cross-model audit. The load-bearing part is the *cross*, not which two. The model asymmetry in
Tibetan is real and we report it as a finding, not a design choice.

**"Why one call per node? Isn't that expensive?"** *(technical half will ask this)*
It's more calls but smaller ones, and it's cheaper in the way that matters — see the context-size
finding. Given 93k characters the model returned 873 characters of extraction; given 12k it
returned 5,224. Larger context bought us *less* output, not more. And the isolation is doing
double duty: it also makes several correctness guarantees structural rather than disciplinary.

**"Why Obsidian and markdown rather than a database?"**
Because the review surface has to work for humans. Sources, claims and drafted articles are all
plain files. A citation is an address that *renders* — a note transcludes the block it cites, so
the cited Tibetan appears inline inside the note citing it, and a reviewer checks a quotation by
reading down the page rather than trusting our verification report. Review state is a field in the
file, and only a domain specialist may set it to complete. And the whole review history is a git
history: every reviewer edit is a commit you can diff against what the machine generated.

**"What was the hardest lesson?"**
Two. Batch the question smaller — the context-size finding. And: an agent auditing its own work
re-reads its own intentions, not the text. Both cost us a rebuild to learn.

**"Could I run this on my corpus?"**
It needs a root text, commentaries, and a curated registry. Nothing in the architecture is
specific to twenty-one homages — the machinery is already prepared over the Bodhicaryāvatāra with
ten commentaries, which is also where the reception and refutation machinery finally gets tested,
because a praise-commentary corpus produces **zero** contested claims. Sanskrit, Pāli and
classical Chinese scholasticism have the same shape: layered canon, commentarial tradition, school
structure.
