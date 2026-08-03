---
title: "Claims extraction — three-method comparison"
scope: "2-RAILS/Claims/{opus, sonnet, toc-scaffolded} × {gendun-gyatso, karma-maitri, lobsang-dawa}"
date: 2026-08-03
method: "Full read of all 9 claim files + 3 sources + 3 TOC trees; machine verification of every quoted Tibetan string against its cited segment"
status: review
---

# Claims extraction — three-method comparison

Nine files were compared: three extraction methods run over the same three Tārā commentaries. Every claim's quoted Tibetan was machine-checked for literal presence in the segment it cites, and the substantive divergences were adjudicated against the source text.

## The headline finding

**The third method is not a third extraction.** `toc-scaffolded` is the `sonnet` output re-bucketed under each commentary's TOC tree, with a Grounding index and per-claim Referent tags added. All three files say so in their own header notes, and three independent lines of evidence confirm it: 114 of 118 Tibetan strings in `toc/karma-maitri` are byte-identical to sonnet's, including sonnet's idiosyncratic ellipsis spans and sonnet's own transcription errors; the frontmatter `claim_count` in all three toc files (133 / 122 / 122) is sonnet's number copied verbatim rather than recomputed; and every one of sonnet's peculiar misquotations reappears in toc unchanged.

So the comparison is really two questions, not three. First, **opus vs. sonnet as extractors**. Second, **does the TOC scaffolding improve on the A–I category schema as an organising layer** — and what did the re-bucketing cost.

Both answers turn out to be clearer than the raw numbers suggest.

## Verified counts

| Commentary | opus | sonnet | toc-scaffolded |
|---|---|---|---|
| gendun-gyatso | 130 (declared 135) | 128 (declared 133) | 125 (declared 133) |
| karma-maitri | 132 (declared 134) | 120 (declared 122) | 118 (declared 122) |
| lobsang-dawa | 124 (declared 127) | 119 (declared 122) | 118 (declared 122) |
| **total** | **386** | **367** | **361** |

The `claim_count` field is wrong in all nine files, but wrong in two different ways. In opus and sonnet it is exactly `claims + internal-tension entries` — 130+5=135, 132+2=134, 124+3=127, and the same for all three sonnet files. That is a consistent convention error: tension entries are cross-references to claims already counted (gendun-gyatso's I2 restates B14 and B15), so they are double-counted. Fix the definition or exclude section I.

The toc files are different. They have zero tension entries of their own, so under the same convention they should declare 125 / 118 / 118. They declare 133 / 122 / 122 — sonnet's values, unchanged. No count was run against the re-bucketed file at all, which is also why the defects listed below went unnoticed.

## Quotation fidelity

Every claim's `བོད་ཡིག` string was normalised (NFC, tsheg and shad stripped) and tested for literal containment in the cited segment. Ellipsis-joined fragments were tested individually.

| Method | Claims | Quotes not present in source | Rate |
|---|---|---|---|
| opus | 386 | 4 | **1.0 %** |
| sonnet | 367 | 6 | **1.6 %** |
| toc-scaffolded | 361 | 10 | **2.8 %** |

More important than the rate: **every `§n` and `L<n>` pointer in all nine files is correct.** Not one claim cites a segment that doesn't contain its subject matter. That is a strong result and the best thing about the pipeline as a whole. The failures are all transcription failures, and they are cumulative — sonnet inherits none of opus's, but toc inherits all of sonnet's and adds its own.

The one systematic pointer problem is shared by all three methods on `gendun-gyatso`: the closing block spans two physical lines, and seven claims per run (the colophon, the dedication, the `རང་བཟོ་སྤངས` methodological claim, the sādhana lineage, and three others) are cited to L176 when their text is on L177. That is a 58 % error rate on that single citation target, mechanically fixable, and identical in all three.

## Three defects that need action

**1. Cross-document contamination in `toc-scaffolded/karma-maitri.md`, claim 1.1.20.e.** The claim asserts `གསོ་བར་དཀའ་བའི་རིམས་ནད་སེལ་མ` ("cures epidemics difficult to treat") under karma-maitri §44. That string appears zero times in the karma-maitri source. It appears verbatim at line 171 of the **lobsang-dawa** commentary — at *its* §44. This is same-segment-number contamination between two of the three texts the run names as comparison targets, and it displaced the correct claim: karma-maitri §44 actually reads `རིམས་ནད་ཐམས་ཅད་སེལ་བར་མཛད་པ` ("removes *all* epidemic fevers"), which sonnet captured correctly as E27 and toc dropped. It also violates the file's own stated guarantee that no claim originates in another commentary. The `(paraphrase of §44)` hedge in the `བོད་ཡིག` slot appears nowhere else in any of the nine files.

**2. A fabricated mantra promoted to canonical status in `toc-scaffolded/gendun-gyatso.md`, TXT-3.** The source at §36 reads `ཨོཾ་ནཱ་མཿཏཱ་རེ་ན་མོ་ཧཱ་རོ་ཧཱུ་ཧཱ་རེ་སྦཱ་ཧཱ` — OCR-corrupt, but that is what is there. Opus quotes it verbatim. Sonnet silently normalised it to a plausible standard form, `ཨོཾ་ན་མོ་ཏ་རེ། ན་མོ་ཧ་རེ་ཧཱུཾ་ཧ་རེ་སྭཧཱ`, a string that occurs nowhere in the source — and did so under a header pledging that "Tibetan is transcribed exactly as it stands, without silent correction." Toc inherited that string and entered it in the Grounding index as `TXT-3`, under a header promising that every index entry resolves to a verbatim string in the source. This is the only place in the nine files where an unattested string has been given reference status.

**3. A structural misquotation in `lobsang-dawa`, inherited.** At L45 the source reads `གཉིས་པ་ལ་གཉིས། ལོངས་སྐུའི་...` — "the *second* [of the three modes of praise] has two parts." Sonnet's A5 quotes it as `དང་པོ་ལ་གཉིས།` — "the *first* has two parts," an opening lifted from the following sentence — which would put the two kāyas under the history section rather than the bodily-form section. Toc inherited it. Opus has it right. On the load-bearing structural claim of the commentary whose ས་བཅད is its distinguishing feature, opus is correct and the other two are not.

## opus vs. sonnet

The raw set-difference numbers overstate the gap badly. On `karma-maitri` the sets diverge 31/20, which looks like a substantial coverage difference; hand-classifying all 52 non-shared strings shows that 13 and 12 are the same claim with a different quotation boundary, 18 and 8 are the same source material split differently, and exactly **one** is genuinely additional content — an opus claim that duplicates its own B8. Sonnet has zero content opus lacks on that text. The pattern repeats on the other two.

What opus actually has over sonnet is not more claims but **more of each claim**, and better discipline. Concretely:

Opus preserves the instrument or setting where sonnet trims it — that the mountains at karma-maitri §38 stand *outside the trichiliocosm*, that poison-removal at §40 is by twice-uttered TĀRA sealed with PHAṬ, that sin-destruction at §34 is by the SVĀHĀ+OṂ mantra. Sonnet reduces each of these to the bare effect. Opus splits where splitting is right: the `བདེ་མ / དགེ་མ / ཞི་མ` triad at §33 is three distinct etymological derivations with three distinct bases, and merging them means a query for `ཞི་མ` returns a blob. Opus reads plurals correctly where sonnet flattens them (gendun-gyatso §14's `དེ་དག་གིས` resumes a list of five gods; sonnet turns it into "one of"), and decodes `ཉི་མ་ལན་གསུམ་མཚན་ལན་གསུམ` as "three times by day and three by night" where sonnet gives "three times each." On `lobsang-dawa` opus alone names all seven ས་འོག levels at §32 and alone records that the divine-lake simile at §39 supplies *roundness* as well as whiteness.

Opus is also the only run that flags an OCR emendation as an emendation — bracketing `[lightning]` where the source has the corrupt `ཚིག` — though it does so exactly once, and all three runs silently restore half a dozen other OCR corruptions in the English without marking them.

Sonnet's advantages are real but few. It is right where opus over-commits: `མཁས་གྲུབ` in the karma-maitri colophon is generic ("what a master taught"), not the proper name Khedrub, and the plural `དག` on `གསུངས་པ` supports sonnet's hedge. It reads karma-maitri §43 correctly (`རབ་ཏུ་རྒྱས་པ` governs sun *and* moon, not just the moon) and §2 correctly (`ཉོན་མོངས་བདུད་སྡེ` is one compound, "māra-hordes of affliction," not two co-ordinated items). On `lobsang-dawa` it alone records the compiler credit at L23 — which opus's coverage log falsely claims to cover — and it alone notices that the commentary's own outline contains *two separate* `དབུ་རྒྱན` headings, a genuine oddity.

Sonnet also carries two errors opus does not: the fabricated §36 mantra above, and an invented doctrinal claim at karma-maitri §8 ("five of six pāramitās named, the sixth unstated") which is both unsupported and self-contradicting, since sonnet's own adjacent B11 correctly identifies the `ཞི་བ` gloss that fills the sixth slot. That invention was enabled by a fabricated particle in the same quote (`ཚུལ་ཁྲིམས་དང་།` for the source's `ཚུལ་ཁྲིམས་དེས`).

Opus's one rule violation is a cross-commentary aside in gendun-gyatso E20 — "a single verse covering both, where other commentaries split them" — which its own header forbids.

**On defensibility of content, opus wins on all three texts**, and the margin is widest exactly where the source is hardest (the OCR-corrupt gendun-gyatso).

## The TOC scaffolding

The scaffolding is worth keeping, but not in its current form, and the case for it is different on each commentary.

**Where it genuinely adds something.** On `lobsang-dawa` the aspect anchoring is real information the flat schema cannot express: the commentary's own outline distinguishes a peaceful form (`ཞི་བའི་རྣམ་པ`) from a wrathful one (`ཁྲོ་མོའི་རྣམ་པ`) and gives each a subtree, so tagging a crown-ornament claim to FIG-4 rather than to "Tārā" records *which aspect* is being described. Opus and sonnet say only "her jewel crown." On `gendun-gyatso` the Grounding index unifies `རྗེ་བཙུན་གྲགས་པ་རྒྱལ་མཆེན` and `རྗེ་བཙུན་གྲགས་རྒྱལ` — the same figure under two OCR variants — into a single PER-1; no flat run can do that. And on all three the node layout surfaces redundancy that the A–I bucketing hides: roughly 5 % of every file is one Tibetan string claimed twice under two type labels, and under TOC nodes those pairs sit as adjacent siblings where before they were in different sections. That is an unadvertised benefit worth naming.

The scaffolding also did good detective work on the trees. The karma-maitri tree has seven of twenty-one leaf pointers wrong, with a value-collision signature (`130` four times, `61` twice) that says the extractor lost its cursor; the toc run detected all seven, re-derived them from the source's own ordinal markers, and documented the method. On lobsang-dawa exactly one of twenty-one pointers is wrong and the toc run caught that one too.

**Where it cost something.** The re-bucketing lost claims. Karma-maitri lost three (§26's "establishes all beings in supreme bliss," §26's "liberates all frightened and destitute beings," §44's `རིམས་ནད་ཐམས་ཅད་སེལ་བར་མཛད་པ`), which is why homage 11's node is anomalously thin. Lobsang-dawa lost one — the `ཏུ་རེ` etymology at §18, one of only three mantra-syllable etymologies in that text. Gendun-gyatso lost the four doxographic attribution claims: the *information* survives as `Attributed to:` fields, but a query on `Type: attribution` now returns 1 instead of 5, and this is the vault's only doxographic witness. That last is a schema decision rather than a lapse, but it makes the very feature the text is prized for invisible to type-filtered retrieval.

The scaffolding introduced placement errors that did not exist before. On lobsang-dawa two claims moved to the wrong node relative to sonnet's own coverage log, and one of them is diagnosable: node 1.2.2.1.1.4 is titled `མི་མཐུན་ཕྱོགས་གནོན་པ` and §10 contains the string `མི་མཐུན་ཕྱོགས་མཐའ་ཡས`, so **title-keyword attraction pulled a claim across a homage boundary**. That is the characteristic failure mode of this approach and it is worth guarding against explicitly. On karma-maitri a §26 claim (homage 11) is filed under homage 20 with the rationalisation "cited here as part of the same descriptive run" — nine homages apart. Opus and sonnet both file it correctly.

**The trees themselves are uneven, and the QC pass is not working.** All three `toc-tree-qc-*.md` files report `issues_before: 0, issues_after: 0`. On gendun-gyatso the tree attaches all twenty-one homages to node `1.2 དེའི་ཕན་ཡོན་བཤདཔའོ` — the *benefits* section — instead of `1.1 བསྟོད་པ་དངོས་`, because line 26 carries two nested `དང་པོ` divisions and the builder picked the wrong one; it also leaves node `2` unresolved as `[[?]]` when `གཉིས་པ་ནི་།` is plainly at line 176. The toc run diagnosed the misattribution correctly and flagged it in prose, but *inherited the numbering*, so all twenty-one homages remain formally children of "explaining the benefits." A human reading the file gets a correct narrative; anything keying on node IDs gets the corrupt taxonomy. On karma-maitri, seven of twenty-one pointers are wrong. The QC step caught none of this on any of the three.

Two tree "defects" turned out not to be. Gendun-gyatso's twenty children for twenty-one homages, and its jump from 19th to 21st, are faithful — the source genuinely gives homage 20 no ordinal header, opening §43 with a bare `ཕྱག་འཚལ།`, and the toc run diagnosed that correctly. Lobsang-dawa's suspicious `[[141]]` on node 1.2.3 is legitimate; only 1.2.2.1.2.6 is actually mispointed.

**The Referent apparatus is the weakest part.** Two problems. First, the `stated` / `node` distinction — the apparatus's main value-add — is applied at segment scope, not fragment scope, so it does not mean what a reader would assume. On karma-maitri, 7 of 14 claims tagged `FIG-1 (stated)` contain no form of `སྒྲོལ་མ` in their quoted Tibetan at all; two of them look like a prefix match on the *verb* `སྒྲོལ་བ` ("liberate"). Second, roughly 6 % of anchors point at the wrong entity: gendun-gyatso's §40 and §44 mantra claims are both anchored to `TXT-2`, the root mantra, which is attested only at L176; lobsang-dawa's ten-pāramitās claim is anchored to Tārā's peaceful form when the source makes the attainers `རྒྱལ་བའི་སྲས`, bodhisattvas. In several places the anchor asserts more than the prose does — at lobsang-dawa §28 the English is agentless ("constant light for beings' sake") while the Referent tag makes Amitābha the emitter, though the feminine `མཛད་མ` and the ablative `ལས` make Tārā the agent and Amitābha the source.

The Grounding indexes also conflate what should be separate: karma-maitri's FIG-5 gives one ID to three separately named figures (`ཚོགས་བདག`, `ཟུར་ཕུད་ལྔ`, `སྨུག་འཛིན`) and invents a fourth chief the source doesn't supply; PLC-1 lumps three mountains into one ID; a heaven (Paranirmitavaśavartin) is filed under Figures. And on gendun-gyatso, four gods named verbatim at §14 (Indra, Agni, Brahmā, Vāyu) appear in no index at all — an index whose stated job is to enumerate attested figures is missing five named gods.

One structural problem affects all three toc files: **node IDs and claim IDs collide.** `1.1` denotes both a claim and a section; `1.2.1` denotes both a placeholder note and the Homage-1 node. Lobsang-dawa has five such collisions. Unique addressability is precisely the property the scaffold exists to provide.

**Does the scaffolding earn its keep?** It depends on the commentary, and the deciding factor is whether the text already states its own outline. On `lobsang-dawa`, which carries a fully articulated ས་བཅད in the text, the tree reproduces it essentially perfectly — zero invented nodes, zero omitted nodes, five levels, verbatim titles — but that is also exactly the information opus's A1–A9 and sonnet's A3–A11 already record, with correct citations. The structural contribution is nil there; the aspect anchoring is the real gain. On `karma-maitri` and `gendun-gyatso`, where the outline is thin or the tree is broken, the scaffolding contributes less structure and more risk.

## What all three miss

Worth noting because it is invisible in any pairwise comparison. On gendun-gyatso, §14 names four gods (`ལྷའི་དབང་པོ་བརྒྱ་བྱིན`, `མེ་ལྷ`, `ཚངས་འདང`, `རླུང་ལྷ`) that no run captures; §41 names Brahmā and Indra, uncaptured; §10's "acts victorious over limitless māras and opposing disputants" is taken by all three as a bare grammar note; two wrathful-form iconography statements at §26 and §32 are captured by none. On karma-maitri, §21 names *which* three fingers form the refuge mudrā (index, middle, little) and all three runs quote the string but gloss it only as "three fingers," losing the identifying content. All three also share a misreading at karma-maitri §42, where `སྟེ` attaches to `དགའ་བའི` — the commentary is glossing *joy* as splendour, not armour.

Two coverage-log claims are false in every run. Lobsang-dawa's §35 yields no claim in any file, yet all three logs assert "Segments yielding no claim: None." And all three explain the missing §20 as a numbering skip with continuous text; in fact every homage head in that commentary carries a running ordinal except wrathful head 2, whose `གཉིས་པ་ནི།` marker is exactly where §20 should be — so §20 is a **lost segment carrying real text**, not a skipped number. That is worth chasing in the segmentation pipeline.

## Recommendation

**Keep opus as the extractor.** It is more accurate on all three commentaries, quotes longer and better-evidenced spans, splits at the right granularity for downstream querying, and is the only run that handles OCR corruption honestly. The cost is roughly 5 % more claims, some of which are redundant splits.

**Keep the TOC scaffolding as a layer, but re-run it over opus rather than sonnet**, and treat it as a re-organisation step with its own verification rather than a second extraction. Specifically:

The `claim_count` field should be recomputed after re-bucketing, not inherited — that single check would have caught most of what went wrong. Add a containment assertion: every claim in the re-bucketed file must appear in the source file, and no claim may be added that isn't in it. Both the karma-maitri contamination and the gendun-gyatso fabricated mantra fail that assertion trivially. Add a node-boundary check against the source's own ordinal markers, which would have caught the three misplacements and the title-keyword attraction. Separate node IDs from claim IDs. And redefine `stated` to mean "the referent's verbatim name occurs in *this claim's* quoted Tibetan," which is what a reader assumes and what makes the tag worth having.

**Fix the TOC tree QC pass before trusting any tree.** It reported zero issues on three trees carrying, between them, a top-level misattribution, an unresolved node with an obvious anchor, seven collided line pointers, and one mispointed node. Reporting zero is worse than reporting nothing.

**Fix the L176/L177 boundary** in all three gendun-gyatso files — seven claims each, same seven, mechanical.

If you want a single canonical file per commentary rather than a method choice: opus's claim set, plus sonnet's `lobsang-dawa` A2 (compiler credit) and its two-crown-headings observation, plus the toc runs' Referent anchoring for `lobsang-dawa`'s peaceful/wrathful aspects and `gendun-gyatso`'s PER-1 OCR merge — with opus's gendun-gyatso E20 cross-commentary clause struck, opus's lobsang-dawa "three kāyas" header claim struck (the outline's top tier is history / bodily form / activity, and only two kāyas appear anywhere in it), and the §20 explanation corrected.
