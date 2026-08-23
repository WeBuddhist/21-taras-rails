---
topic: three-jewels
article: article.md
method: wiki-article-from-claims-v2
revision_mode: B
revised_from: 3-TRANSFORMATIONS/Wikipedia/tara21/term-articles/three-jewels/article.md (v1, wiki-article-from-claims, dated 2026-08-12; prior version preserved by git history, not kept as a side-copy)
revision_date: 2026-08-21
context_packages:
  - 2-RAILS/Claims/three-jewels.md
rails_status: draft
raw_sources_cited:
  - 2-RAILS/Claims/raw/tree-guided/yama-sonam.md
  - 2-RAILS/Claims/raw/tree-guided/sungrab-tulku.md
  - 2-RAILS/Claims/raw/tree-guided/tenzin-dhonzang.md
  - 2-RAILS/Claims/raw/tree-guided/taranatha.md
  - 2-RAILS/Claims/raw/tree-guided/konchok-thabkhe.md
  - 2-RAILS/Claims/raw/tree-guided/palden-sherab.md
  - 2-RAILS/Claims/raw/tree-guided/tsultrim-namdak.md
date: 2026-08-12
status: draft
---

> [!note] Polished — gemini-article-polish, 2026-08-23, model gemini-3.1-pro-preview; claim usage unchanged from 3-TRANSFORMATIONS/Wikipedia/tara21/term-articles/three-jewels/article.md (pre-polish).

# Citations — three-jewels (དཀོན་མཆོག་གསུམ།)

## Quotation budget & pairing fix (2026-08-21, second pass)

A follow-up review of this Mode B revision found two problems, both fixed in this pass without
touching `2-RAILS/Claims/` or re-opening any claim content:

**Fix 1 — the lead root-verse quotation is not exempt.** The "Register conversion" note below
(and the ref-count table) had treated the lead's root-verse quotation as exempt from Rule 6's
quotation budget, citing the clause "root-text verse quotation in the lead ... does not count
against the budget." That clause's own text continues "(v1's practice for **deity articles**)" —
this article is a **term-article** (`article_kind: term-article` in frontmatter), not one of the
tara-01…tara-21 deity-profile slot-articles the exemption names. The exemption does not apply
here. The lead's quotation of `yama-sonam:c-3-9-3` (the ninth-praise root verse) has been
converted to unquoted paraphrase in `article.md`, grounded in the same claim's already-recorded
meaning — the verse's own content (mudrā symbolizing the Three Jewels, fingers adorning the
heart, the wheel of all directions adorned by her own light) is unchanged and still cited to the
same three refs (`yama-sonam`, `sungrab-tulku`, `tenzin-dhonzang`). No claim was dropped. The
article now carries **exactly 2 verbatim quotations total**: `sungrab-tulku:c-12-4` (finger-
assignment divergence, `མཚན་ཉིད།`) and `taranatha:c-9-9` (hidden-meaning gloss, `དབྱེ་བ།`) — both
already representing cases where, per Rule 6, "the exact wording is itself the point" (a contested
formulation and a definition whose phrasing matters, respectively).

**Fix 2 — the retained `taranatha:c-9-9` quotation was ambiguously dual-sourced.** Prior to this
fix, the article's hidden-meaning sentence attached **two** refs (`taranatha` and `palden-sherab`)
to a single quoted string, framed as "stated in identical words" by both. This pass re-verified
the quoted string directly against both underlying `1-SOURCES/` files (not just against the v1
verification record):

- `taranatha`'s source, `1-SOURCES/Commentaries/ཕྱག་འཚལ་ཉེར་གཅིག་གི་བསྟོད་པའི་རྣམ་པར་བཤད་པ།.md#^0-33`,
  reads (in relevant part): "སྦས་དོན་ནི། དཀོན་མཆོག་གསུམ་མཚོན་ནི་ཁུ་རྡུལ་རླུང་གསུམ་སྟེ། ..." — the
  article's quoted string is an exact, character-for-character (whitespace-collapsed) substring.
  **PASS.**
- `palden-sherab`'s source,
  `1-SOURCES/Commentaries/རྗེ་བཙུན་སྒྲོལ་མའི་བསྟོད་པ་ཉི་ཤུ་རྩ་གཅིག་...ཞེས་བྱ་བཞུགས་སོ།.md#^0-102`,
  reads: "གསུམ་པ་སྦས་དོན་རྫོགས་རིམ་མཚན་བཅས་ལྟར་ན། དཀོན་མཆོག་གསུམ་མཚོན་ནི་ཁུ་རྡུལ་རླུང་གསུམ་སྟེ། ..." —
  the article's quoted string opens "སྦས་དོན་ནི།", but `palden-sherab`'s text opens with the
  different clause "གསུམ་པ་སྦས་དོན་རྫོགས་རིམ་མཚན་བཅས་ལྟར་ན།" instead. The quoted string as a whole
  is **not** an exact substring of `palden-sherab`'s source. **FAIL** as a source for this
  particular verbatim string (even though the shared inner clause "དཀོན་མཆོག་གསུམ་མཚོན་ནི་ཁུ་རྡུལ་
  རླུང་གསུམ་སྟེ།" is worded identically in both — the two commentaries make the same doctrinal
  point, but only `taranatha`'s wording matches the exact string quoted in the article).

Per the correct-source-or-paraphrase rule, `article.md` was rewritten: the quotation is now
attributed **only to `taranatha`** (its verified source), and `palden-sherab`'s parallel statement
of the same point is cited as an unquoted paraphrase in its own sentence ("མཁན་ཆེན་དཔལ་ལྡན་ཤེས་རབ་
ཀྱིས་ཀྱང་རྫོགས་རིམ་མཚན་བཅས་ཀྱི་སྐབས་སུ་དོན་མཐུན་པར་བཤད།"), still carrying its own `<ref>`. No claim
was dropped and no new claim ID was introduced. See the updated Reference map and Verification
table below for both quotations' final, unambiguous source pairing.

## Revision note (Mode B, 2026-08-21)

This file's `article.md` was rewritten in place from v1 register (wiki-article-from-claims) to
v2 register (wiki-article-from-claims-v2), per Mode B of that skill's SKILL.md. Per Mode B, this
revision did **not** return to `2-RAILS/Claims/three-jewels.md` or the raw tree-guided files —
the claim resolution and quotation verification below (all inherited from the v1 draft, dated
2026-08-12) are treated as settled ground truth. The only claim-level lookups performed in this
pass were frontmatter-only (`author_in_use`, for Rule 17), read from each raw tree-guided file's
own frontmatter — never claim content.

**No new claim ID was introduced.** Every claim ID cited in the revised `article.md` is a subset
of the 23 rows already resolved and verified in the v1 draft (table below, carried forward
unchanged). Several claim IDs that were individually quoted in v1 are still cited in v2 but now
paraphrased rather than quoted (see "Register conversion" below); none were dropped from the
citation record — all still appear either in an `<ref>` in `article.md` or in "Full attestation
beyond in-article refs" below.

### Ref-count and quotation-count, before/after

| | v1 (wiki-article-from-claims) | v2 (this revision) |
|---|---|---|
| Total `<ref>` tag occurrences (opens + self-closes) | 24 | 21 (7 full defs + 14 self-closes) |
| Distinct commentaries cited | 7 | 7 (unchanged: yama-sonam, sungrab-tulku, tenzin-dhonzang, taranatha, konchok-thabkhe, palden-sherab, tsultrim-namdak) |
| Verbatim commentary/root-verse quotations in the article | 15 quoted spans (across 12 claim rows, two claims contributing two portions each) | **2** quoted spans total, both budgeted commentary quotations (`sungrab-tulku:c-12-4`, `taranatha:c-9-9`) — corrected in the 2026-08-21 fix pass above; the lead's root-verse quotation is **not** exempt (Rule 6's lead-quote exemption names "deity articles" only, not term-articles) and has been converted to paraphrase |
| Max refs on a single statement | up to 3 (already within v1's own practice) | ≤3, unchanged cap, verified programmatically (see Verification below) |
| Approx. body-prose syllable count (tsheg-delimited, excluding ref/heading/bullet content) | ~1,547 (flagged borderline against the spec's ~1,500 guideline) | 335 — well under the guideline; the borderline-length warning no longer applies |

### Register conversion — what changed and why

- **Consensus material moved to wikivoice.** The mudra's physical description (thumb+ring
  finger holding the utpala stem, index/middle/little fingers raised) and the outer
  Buddha-Dharma-Sangha identification of the mudra are now stated as plain fact in
  `མཚན་ཉིད།`/`དབྱེ་བ།`, backed by 2 representative refs each, rather than as a chain of
  "commentary X says... commentary Y also says..." sentences.
- **Two divergences are preserved with full attribution**, exactly as in v1, per Rule 5 — neither
  flattened nor adjudicated:
  - **Finger-assignment divergence**: `sungrab-tulku:c-12-4` (thumb+middle hold the stem;
    index+ring+little raised) against the consensus attested by `yama-sonam:c-3-9-5` and
    `palden-sherab:c-3-1-9-1-1` (thumb+ring hold the stem; index+middle+little raised). This
    divergence keeps its verbatim quotation (quotation budget slot 1 of 2) because the exact
    wording is the point of the disagreement.
  - **"Tārā as worshipper of the Three Jewels" vs. "Tārā as embodiment of the Three Jewels"**:
    `sungrab-tulku:c-12-3` against `tenzin-dhonzang:c-4-9-3` + `c-4-9-4`. Both positions are now
    given their own attributed paragraph in `གཞུང་ལུགས་སོ་སོའི་བཤད་པ།`, unquoted (paraphrased from
    the same claims' recorded meaning) to stay within the quotation budget — the divergence itself
    is preserved by attribution, not by verbatim wording, per Rule 6's guidance to spend the quote
    budget only where exact phrasing is the point.
- **The "hidden meaning" gloss (channels/drops/winds, `ཁུ་རྡུལ་རླུང་གསུམ`) keeps its quotation**
  (`taranatha:c-9-9`, budget slot 2 of 2) — a definition whose precise phrasing is the point, per
  Rule 6. **Corrected in the 2026-08-21 fix pass:** this quotation is sourced to `taranatha` alone.
  An earlier draft of this revision also attached `palden-sherab:c-3-1-9-3-1` to the same quoted
  string, describing both as stating it "in identical wording" — but direct verification against
  `palden-sherab`'s own source (`...ཞེས་བྱ་བཞུགས་སོ།.md#^0-102`) found its text opens with a
  different clause ("གསུམ་པ་སྦས་དོན་རྫོགས་རིམ་མཚན་བཅས་ལྟར་ན།") than `taranatha`'s ("སྦས་དོན་ནི།"), so
  the quoted string is not an exact substring of `palden-sherab`'s source, even though the shared
  inner clause matches. `article.md` now quotes only `taranatha`, and cites `palden-sherab`'s
  parallel statement as a separate, unquoted paraphrase sentence.
- **Four claims that were individually quoted in v1 are now cited but paraphrased**, converting
  their content into prose without quotation marks, so no re-verification against `1-SOURCES/`
  was needed (Mode B step 4): `yama-sonam:c-3-9-6` (cause/function distinction), `taranatha:c-9-3`
  (samaya-mudra identification), `konchok-thabkhe:c-2-9-4` (utpala/three-times-buddhas gloss),
  `palden-sherab:c-3-1-9-4-1` (ultimate/completion-stage reading), `palden-sherab:c-3-1-4-2-1` +
  `c-3-1-19-2-1` (recurrence across emanations), `tsultrim-namdak:c-3-12` (divergent verse lines)
  and `c-5-2-0-3` + `c-5-2-0-4` (refuge-taking elaboration). All remain individually attributed to
  their commentary by name (in `author_in_use` form, Rule 17) in `གཞུང་ལུགས་སོ་སོའི་བཤད་པ།`, since
  each is a unique claim not independently attested elsewhere in this article's resolved set.
- **One naming inconsistency from v1 was corrected under Rule 17.** v1's per-commentary section
  attributed a claim to "'''འཕྲིན་ལས་ཆར་གྱི་འགྲེལ་པ'''ནས་" (a title-derived description of the
  commentary, not a person's name). `yama-sonam`'s raw claims file records
  `author_in_use: "རྗེ་བཙུན་ཡ་མ་བསོད་ནམས་"`, so v2 now attributes this material to
  `'''རྗེ་བཙུན་ཡ་མ་བསོད་ནམས་'''ནས་`, matching the pattern already used correctly for the other six
  commentaries in v1. No `author_in_use` fallback warning is needed for any of the 7 commentaries
  cited — all 7 raw tree-guided files carry the key directly in their own frontmatter (confirmed
  by a frontmatter-only read of each file in this pass); none required the `source_file`
  commentary-frontmatter fallback.
- **Two verse-quotation duplications in v1 (the root verse quoted a second time via
  `sungrab-tulku:c-12-2` / `tenzin-dhonzang:c-4-9-2` as unquoted "cited, not quoted" attestations)
  are preserved as unquoted co-attestations** on the lead's verse sentence — they were never
  separately quoted in v1 either, so nothing changed here.

## Full attestation beyond in-article refs

Per this skill's output contract, capped consensus statements list every other commentary that
also attests them, so nothing is lost to the citation cap. In this article, every backbone/
consensus statement already cites the full set of commentaries individually resolved and
verified for it in the v1 pass — v1's own scoping note (see "Deliberately out of scope" below)
already narrowed each facet to 2 representative commentaries before this revision, and Mode B did
not re-open `2-RAILS/Claims/three-jewels.md` to resolve further attestations. There is therefore
no additional resolved-and-verified attestation to list beyond what is already cited:

- Mudra physical description (thumb+ring, index/middle/little raised): `yama-sonam:c-3-9-5`,
  `palden-sherab:c-3-1-9-1-1` — both already cited in `མཚན་ཉིད།`.
- Hidden-meaning gloss (channels/drops/winds): `taranatha:c-9-9`, `palden-sherab:c-3-1-9-3-1` —
  both already cited in `དབྱེ་བ།`.
- Root-verse identification: `yama-sonam:c-3-9-3`, `sungrab-tulku:c-12-2`,
  `tenzin-dhonzang:c-4-9-2` — all already cited in the lead.

A reviewer wanting full parity with every attestation tallied on `2-RAILS/Claims/three-jewels.md`
(beyond the individually resolved set above) should treat this — as v1 already noted — as a first
pass, not a final draft; see "Deliberately out of scope" below, carried forward unchanged from v1
since Mode B does not re-resolve claims.

## Reference map

| # | Commentary (ref name) | Claim ID | Quotation (verbatim བོད་ཡིག, if quoted) | Source block |
|---|---|---|---|---|
| 1 | yama-sonam | c-3-9-3 | (v1/v2-draft-1: quoted "ཕྱག་འཚལ་དཀོན་མཆོག་གསུམ་མཚོན་ཕྱག་རྒྱའི།...འཁྲུགས་མ།"; **2026-08-21 fix**: cited, paraphrased in the lead — the lead-quote exemption in Rule 6 names deity articles only, not term-articles, so this no longer counts toward or against the 2-quotation budget) | 1-SOURCES/Commentaries/སྒྲོལ་མའི་འགྲེལ་བ་འཕྲིན་ལས་ཆར་དུ་སྙིལ་བའི་སྤྲིན་ཕུང་།.md#^0-88 |
| 2 | yama-sonam | c-3-9-5 | (v1: quoted "དཀོན་མཆོག་གསུམ་མཚོན་པའི་ཕྱག་རྒྱ"; v2: cited, paraphrased into the consensus physical description in `མཚན་ཉིད།`) | ...#^0-90 |
| 3 | yama-sonam | c-3-9-6 | (v1: quoted "རྒྱུ་སངས་རྒྱས་...བསྟན་པ་ཡིན་ཏེ།"; v2: cited, paraphrased as the unique cause/function distinction) | ...#^0-91 |
| 4 | yama-sonam | c-3-9-7 | (cited, not quoted in v1 or v2 — supporting root-verse citation for the cause/function claim, not independently drawn on) | ...#^0-92 |
| 5 | sungrab-tulku | c-12-2 | (cited, not quoted — second co-attestation of the root verse in the lead) | 1-SOURCES/Commentaries/སྒྲོལ་མཉེར་གཅིག་གི་རྣམ་བཤད།.md#^0-62 |
| 6 | sungrab-tulku | c-12-3 | (v1: quoted "གང་ལ་ཕྱག་འཚལ་བའི་ཡུལ་...འདུད་པའོ"; v2: cited, paraphrased as the "worshipper of the Three Jewels" divergence position) | ...#^0-63 |
| 7 | sungrab-tulku | c-12-4 | "རྗེ་བཙུན་སྒྲོལ་མའི་ཕྱག་གཡོན་པའི་མཐེ་མོ་དང་གུང་མོ་གཉིས་ཀྱིས་མེ་ཏོག་ཨུཏྤལའི་ཡུ་བ་བཟུངས་ཤིང་། མཛུབ་མོ་དང་སྲིན་ལག མཐེའུ་ཆུང་བཅས་གསུམ་སྒྲེང་བ" (retained verbatim in v2 — spot-verified, see below) | ...#^0-63 |
| 8 | tenzin-dhonzang | c-4-9-1 | (v1: quoted "དགུ་པ་དཀོན་མཆོག་གསུམ་མཚོན་ལ་བསྟོད་པ"; v2: cited, paraphrased as the lead's naming fact) | 1-SOURCES/Commentaries/སྒྲོལ་མ་ཉེར་གཅིག་གི་བསྟོད་འགྲེལ་སྙིང་གི་ནོར་བུ.md#^0-177 |
| 9 | tenzin-dhonzang | c-4-9-2 | (cited, not quoted — third co-attestation of the root verse in the lead) | ...#^0-178 |
| 10 | tenzin-dhonzang | c-4-9-3 | (v1: quoted "སྐྱབས་གནས་བསླུ་བ་མེད་པའི་...བསམས་དགོས།"; v2: cited, paraphrased as the "embodiment of the Three Jewels" divergence position) | ...#^0-179 |
| 11 | tenzin-dhonzang | c-4-9-4 | (v1: quoted "དཀོན་མཆོག་གསུམ་འདུས་པའི་བདག་ཉིད་དུ་མཚོན་" and "དེ་ཡང་སྐུ་དགེ་འདུན...ཀུན་འདུས།"; v2: cited, paraphrased as the sku-sung-thuk correspondence) | ...#^0-180 |
| 12 | taranatha | c-9-3 | (v1: quoted "དཀོན་མཆོག་གསུམ་མཚོན་པར་བྱེད་པ་...དམ་ཚིག་གི་ཕྱག་རྒྱ་སྟེ།"; v2: cited, paraphrased as the unique samaya-mudra identification) | 1-SOURCES/Commentaries/ཕྱག་འཚལ་ཉེར་གཅིག་གི་བསྟོད་པའི་རྣམ་པར་བཤད་པ།.md#^0-31 |
| 13 | taranatha | c-9-9 | "སྦས་དོན་ནི། དཀོན་མཆོག་གསུམ་མཚོན་ནི་ཁུ་རྡུལ་རླུང་གསུམ་སྟེ།" (retained verbatim — budget slot 2 of 2; **2026-08-21 fix**: re-verified as an exact substring of `taranatha`'s source specifically, and now attributed in-article to `taranatha` alone, see below) | 1-SOURCES/Commentaries/ཕྱག་འཚལ་ཉེར་གཅིག་གི་བསྟོད་པའི་རྣམ་པར་བཤད་པ།.md#^0-33 |
| 14 | konchok-thabkhe | c-2-9-4 | (v1: quoted the full praise-verse + "དཀོན་མཆོག་མ་ལུས་པ་འདུས་པའི་ངོ་བོར"; v2: cited, paraphrased) | 1-SOURCES/Commentaries/ཕྱག་འཚལ་ཉེར་གཅིག་མའི་ཊིཀྐ་འཕགས་མའི་ཞལ་ལུང་ཞེས་བྱ་བ་བཞུགས་སོ།.md#^0-54 |
| 15 | palden-sherab | c-3-1-9-1-1 | (v1: quoted "མཛུབ་མོ་དང་གུང་མོ་མཐེའུ་ཆུང་...ཐུགས་ཀར་རྣམ་པར་བརྒྱན་མ"; v2: cited, paraphrased into the consensus physical description in `མཚན་ཉིད།`) | 1-SOURCES/Commentaries/རྗེ་བཙུན་སྒྲོལ་མའི་བསྟོད་པ་ཉི་ཤུ་རྩ་གཅིག་...ཞེས་བྱ་བཞུགས་སོ།.md#^0-95 |
| 16 | palden-sherab | c-3-1-9-2-1 | (v1: quoted "དཀོན་མཆོག་གསུམ་མཚོན་ཕྱག་རྒྱའི་མཐེབ་སྲིན་...སྙན་ཐད་དུ་ཁ་ཕྱེ་བའི་ཟེའུ་འབྲུའི་སྟེང་ན"; v2: cited, paraphrased as the generation-stage light-wheel detail) | ...#^0-97 |
| 17 | palden-sherab | c-3-1-9-3-1 | (v1: quoted "དཀོན་མཆོག་གསུམ་མཚོན་ནི་ཁུ་རྡུལ་རླུང་གསུམ་སྟེ།" separately; **2026-08-21 fix**: this clause matches `palden-sherab`'s own source verbatim, but `palden-sherab`'s full sentence opens with a different clause than the string quoted in-article for `taranatha:c-9-9` — so `palden-sherab` is cited as an unquoted paraphrase of the same point, not as a second source for `taranatha`'s exact quoted string) | ...#^0-102 |
| 18 | palden-sherab | c-3-1-9-4-1 | (v1: quoted "ཡེ་ནས་སྒོ་གསུམ་སྣང་གྲགས་རིག་གསུམ་...ངོ་བོར་སད་པས།"; v2: cited, paraphrased as the ultimate/completion-stage reading) | ...#^0-103 |
| 19 | palden-sherab | c-3-1-4-2-1 | (v1: quoted "གཡོན་དཀོན་མཆོག་གསུམ་མཚོན་ཕྱག་རྒྱས་...འཆི་མེད་ཚེའི་བུམ་པ"; v2: cited, paraphrased as one example of the recurrence-across-emanations claim) | ...#^0-49 |
| 20 | palden-sherab | c-3-1-19-2-1 | (v1: quoted "གཡོན་དཀོན་མཆོག་གསུམ་མཚོན་ཕྱག་རྒྱའི་ཨུཏྤལ་ཟེའུ་འབྲུའི་སྟེང་ན་གདུགས་དཀར་པོ་འཛིན་པ"; v2: cited, paraphrased as the second example) | ...#^0-189 |
| 21 | tsultrim-namdak | c-3-12 | (v1: quoted both root-verse portions; v2: cited, paraphrased as the divergent-verse-lines note, avoiding re-quotation of the Khadira/Śiṃśapā comparison text per v1's own caution — see Warnings) | 1-SOURCES/Commentaries/སྒྲོལ་འགྲེལ་ཚོགས་གཉིས་རྒྱ་མཚོར་འཇུག་པའི་གྲུ་གཟིངས།.md#^0-211, #^0-212 |
| 22 | tsultrim-namdak | c-5-2-0-3 | (v1: quoted "སངས་རྒྱས་དང་ཆོས་དང་དགེ་འདུན...སྒྲོལ་མ་ལ"; v2: cited, paraphrased as the refuge-taking elaboration) | ...#^0-365 (through #^0-369) |
| 23 | tsultrim-namdak | c-5-2-0-4 | (v1: quoted "སྐྱབས་སུ་སོང་ན།...མི་ཚུགས།"; v2: cited, paraphrased as the refuge benefits) | ...#^0-370 (through #^0-371) |

All 23 rows above were individually opened in their raw tree-guided file, and every quoted
cell was located character-for-character (whitespace-collapsed) in the exact `1-SOURCES/` block(s)
its claim's `Cite:` target names — see Verification below. This table is carried forward from the
v1 draft unchanged in its row structure; only the "Quotation" column has been annotated to record
which claims are still quoted verbatim in `article.md` (rows 1, 7, 13) versus cited-and-paraphrased
in v2 (all other rows).

## Claims used but not quoted (v1 designation, still accurate in v2)

- `sungrab-tulku:c-12-2` — the full four-line root verse, cited in the lead only as a second
  attestation; not separately quoted to avoid a redundant second verbatim block of the same verse.
- `tenzin-dhonzang:c-4-9-2` — same, the commentary's own root-verse quotation, cited but not
  re-quoted for the same reason.
- `konchok-thabkhe:c-2-9-4` — the unquoted closing clause ("ཇོ་བོ་ཆེན་པོས་...") describing
  divergent liturgical applications was read but not drawn on in v1 or v2; only the verse citation
  and the Three-Jewels/three-times gloss were used.

## Deliberately out of scope (consolidated-page attestations not resolved)

Carried forward unchanged from v1 — Mode B does not re-open `2-RAILS/Claims/three-jewels.md`.
Per the original Adaptation 2 scoping guidance, the v1 draft favoured a smaller set of
individually resolved-and-verified quotations over exhaustively citing every attestation tallied
on `2-RAILS/Claims/three-jewels.md`. The following attestations listed on the consolidated page
were **not** opened/resolved in the v1 pass and so do not appear in either v1 or v2 of the
article. This remains a scope choice, not a resolution failure — available for a future
expansion pass (which would require Mode A, not Mode B):

- Root-verse facet: `dharmabhadra:c-1-2-2-1-2-2-2`, `tenga-tulku:c-1-2-2-1-2-2-2` (both duplicate
  the yama-sonam/sungrab-tulku/tenzin-dhonzang root-verse wording already covered),
  `gendun-drub:c-2-2-2-2-1-2-2-2` (partial two-line variant; the consolidated page itself notes
  it as a partial, non-full-quote attestation), `tsultrim-namdak:c-2-1-2-1-32`/`c-2-1-2-1-33`
  (this commentary's *first* root-verse pass — superseded in this draft by its second,
  divergent pass at `c-3-12`, which was judged more informative to quote).
- Iconography consensus facet: `dharmabhadra:c-1-2-2-1-2-2-3`, `gendun-gyatso:c-1-9-1`,
  `konchok-thabkhe:c-2-9-2`, `pema-namgyal:c-2-4-30`, `sangye-nyentrul:c-10-0-1`,
  `karma-maitri:c-1-1-9-2`, `lobsang-dawa:c-1-2-2-1-2-2-1`, `drakpa-gyaltsen:c-1-55`/`c-1-56`,
  `tenga-tulku:c-1-2-2-1-2-2-3` — the article's iconography backbone is instead built on the
  2 individually resolved commentaries (yama-sonam, palden-sherab) cited for that description in
  v2's `མཚན་ཉིད།`, within this skill's "2–3 representative commentaries" guidance for consensus
  prose (Rule 5/7); it therefore does not repeat the consolidated page's precise "10 commentaries"
  count as a fact in its own voice.
- Recurrence-across-emanations facet: only 2 of `palden-sherab`'s 18 listed claims
  (`c-3-1-4-2-1`, `c-3-1-19-2-1`) were individually resolved and quoted/cited as representative
  examples; the figure "བཅོ་བརྒྱད་ཙམ" (approximately eighteen) used in the article's prose is
  drawn from the consolidated page's own tally for this facet, not independently re-counted
  claim-by-claim in either pass.

## Unresolvable attestations

None. Every claim ID actually cited in `article.md` was found and resolved in its stated raw
tree-guided file on first lookup (v1 pass); nothing was dropped for failing to resolve. This
revision (Mode B) performed no new resolution.

## Warnings

- **`rails_status: draft`.** `2-RAILS/Claims/three-jewels.md` still carries `status: draft`, not
  `complete`. Per Rule 14, this is flagged prominently: a human contributor is accepting that risk
  by running this skill (in either mode) against a draft page.
- **No URLs on any ref.** None of the 7 cited raw tree-guided files' frontmatter records a public
  URL/BDRC ID for its source commentary, so every `<ref>` is the hand-formatted
  `<AUTHOR>། <TITLE>།` form with no link. Per Rule 11, no URL was fabricated.
- **No year or page recorded on any ref.** None of the 7 raw files' frontmatter carries a
  publication year or page number, so none could be appended.
- **All 7 commentaries' `author_in_use` resolved directly from their own raw claims file
  frontmatter** — no fallback to a `source_file` commentary's frontmatter was needed, and no
  commentary is missing the key. (Confirmed by a frontmatter-only read of all 7 raw tree-guided
  files during this revision, per Rule 17's resolution order.) `yama-sonam`'s
  `author_in_english` is separately recorded as "unknown" in that file's frontmatter — this is
  informational only and does not affect `author_in_use`, which is present and was used correctly
  in v1 already for the `<ref>`/works-cited forms; only the in-prose attribution needed correcting
  in this revision (see "Register conversion" above).
- **Scope narrower than the consolidated page's full attestation counts** — see "Deliberately
  out of scope" above, carried forward unchanged from v1.
- **Existing bo.wikipedia article.** Per this vault's Step 8 wiki-inventory, a substantial
  article already exists at the title དཀོན་མཆོག་གསུམ། (snapshot:
  `3-TRANSFORMATIONS/Wikipedia/tara21/work/wiki-snapshots/`), and the recommended pipeline action
  for this subject is **update**, not create. This draft (v1 and v2 alike) is deliberately scoped
  to what *this text's* commentaries say about Tārā's relationship to the Three Jewels rather than
  re-deriving the general Buddhist doctrine of the Three Jewels, which the existing article almost
  certainly already covers. Whether and how this material should be merged into the existing
  article, or kept separate, remains a human editorial decision — not performed here.
- **Article length — warning resolved in v2.** v1's body prose ran to approximately 1,547
  tsheg-delimited syllables, at or just above the spec's informal ~1,500-syllable guideline. v2's
  register conversion (wikivoice consensus prose, quotation budget) reduced this to approximately
  335 tsheg-delimited syllables (excluding `<ref>` content, wikilinks, and headings) — well under
  the guideline; no length warning applies to v2.
- **Both divergences remain presented with full attribution in v2**, per Rule 5 — neither is
  adjudicated or flattened: the finger-assignment divergence
  (`sungrab-tulku:c-12-4` vs. the `yama-sonam:c-3-9-5`/`palden-sherab:c-3-1-9-1-1` consensus) and
  the "Tārā as worshipper" (`sungrab-tulku:c-12-3`) vs. "Tārā as embodiment"
  (`tenzin-dhonzang:c-4-9-3`) divergence.
- **`tsultrim-namdak:c-3-12`'s textual variant** (third/fourth root-verse lines diverging into
  the Khadira/Śiṃśapā-forest tradition) is presented descriptively in both v1 and v2, without
  re-quoting the divergent comparison text, to avoid reconstructing a composite quotation that is
  not verbatim from any single raw claim — see the original v1 Verification note (retained below)
  for the earlier drafting error this avoided.
- **Quotation budget and pairing corrected 2026-08-21 (second pass).** An earlier draft of this
  v2 revision incorrectly treated the lead's root-verse quotation as exempt from Rule 6's
  2-quotation budget (the exemption applies only to deity-profile slot-articles, not
  term-articles like this one) and attached two refs (`taranatha`, `palden-sherab`) to a single
  quoted string even though only `taranatha`'s source matches it exactly. Both are fixed: the
  article now carries exactly 2 verbatim quotations (`sungrab-tulku:c-12-4`, `taranatha:c-9-9`),
  each singly and correctly sourced. See "Quotation budget & pairing fix" at the top of this file.

## Verification

Every quotation in the Reference map above was checked character-for-character
(whitespace-collapsed) against the exact `1-SOURCES/` file and block(s) named in its claim's
`Cite:` field, during the v1 drafting pass (2026-08-12). Results (unchanged, carried forward):

| # | Commentary:Claim | Result |
|---|---|---|
| 1 | yama-sonam:c-3-9-3 | PASS |
| 2 | yama-sonam:c-3-9-5 | PASS |
| 3 | yama-sonam:c-3-9-6 | PASS (fixed — see note below) |
| 4 | yama-sonam:c-3-9-7 | PASS |
| 5 | tenzin-dhonzang:c-4-9-1 | PASS |
| 6 | tenzin-dhonzang:c-4-9-3 | PASS (fixed — see note below) |
| 7 | tenzin-dhonzang:c-4-9-4 (both quoted portions) | PASS |
| 8 | sungrab-tulku:c-12-3 | PASS |
| 9 | sungrab-tulku:c-12-4 | PASS |
| 10 | taranatha:c-9-3 | PASS |
| 11 | taranatha:c-9-9 | PASS |
| 12 | konchok-thabkhe:c-2-9-4 (both quoted portions) | PASS (fixed — see note below) |
| 13 | palden-sherab:c-3-1-9-1-1 | PASS |
| 14 | palden-sherab:c-3-1-9-2-1 | PASS |
| 15 | palden-sherab:c-3-1-9-3-1 | PASS |
| 16 | palden-sherab:c-3-1-9-4-1 | PASS |
| 17 | palden-sherab:c-3-1-4-2-1 | PASS |
| 18 | palden-sherab:c-3-1-19-2-1 | PASS |
| 19 | tsultrim-namdak:c-3-12 (both quoted portions) | PASS |
| 20 | tsultrim-namdak:c-5-2-0-3 | PASS |
| 21 | tsultrim-namdak:c-5-2-0-4 | PASS |

**21/21 quoted claims — 100% PASS** (v1 pass, 2026-08-12; counting each claim once — two claims,
`tenzin-dhonzang:c-4-9-4` and `konchok-thabkhe:c-2-9-4`, each supplied two separately-quoted
portions in v1, and `tsultrim-namdak:c-3-12` supplied one quotation spanning two adjacent source
blocks; all portions individually verified at the time).

Three quotations required a fix during v1 drafting before verification passed, all caught and
corrected in that same session:

1. **`yama-sonam:c-3-9-6`** — an early draft wrote "ཕྱག་རྒྱའི་རྒྱུ་སངས་རྒྱས་..." but the
   source reads "ཕྱག་རྒྱས་ནི། རྒྱུ་སངས་རྒྱས་..." — the quote was corrected to start exactly at
   "རྒྱུ་སངས་རྒྱས་..." (an exact substring), with the lead-in prose rewritten around it.
2. **`tenzin-dhonzang:c-4-9-3`** — an early draft used an ellipsis ("...") inside the quotation
   marks to skip the middle of the sentence; ellipses are never literally present in source text,
   so this could never verify. Replaced with a shorter, fully contiguous exact substring
   ("སྐྱབས་གནས་བསླུ་བ་མེད་པའི་... བསམས་དགོས།").
3. **`konchok-thabkhe:c-2-9-4`** — same ellipsis problem inside the quoted praise-verse; replaced
   with the full, contiguous four-line quotation.

A fourth issue was caught and fixed at the citation-chain level rather than the character level:
an early v1 draft of the `tsultrim-namdak` paragraph quoted "ཕྱོགས་ཀྱི་འཁོར་ལོ(ས)་བརྒྱན་པའི། རང་གི་
འོད་ཀྱི་ཚོགས་རྣམས་འཁྲུགས་མ" with quotation marks, lifted directly from
`2-RAILS/Claims/three-jewels.md`'s own synthesized composite quote (which carries a "(ས)"
alternate-spelling annotation that is a consolidation artifact, not verbatim text from any single
raw file). This violated Rule 2 (resolution must run through a raw claim's own བོད་ཡིག field, never
through the consolidated page directly) independently of whether it could pass a literal
character search. It was rewritten as an unquoted, unmarked description referencing the
already-cited root-verse quotation in the lead, rather than as a second, fabricated quotation.

### v2 spot-check (Mode B step 6, 2026-08-21)

The 3 quotations retained verbatim in the first v2 draft's `article.md` (the root-verse quotation
in the lead, `sungrab-tulku:c-12-4`'s finger-divergence quotation, and `taranatha:c-9-9`'s hidden-
meaning quotation) were each diffed character-for-character against the exact quotation text
already recorded as PASS in the Reference map / Verification table above — a text comparison
against the settled v1 record, not a fresh `1-SOURCES/` lookup, per Mode B step 6. All three were
unchanged, exact matches against their v1-recorded text:

| Quotation | v1 PASS text vs. v2 article text | Result |
|---|---|---|
| yama-sonam:c-3-9-3 (root verse, lead) | identical | MATCH |
| sungrab-tulku:c-12-4 (finger divergence, `མཚན་ཉིད།`) | identical | MATCH |
| taranatha:c-9-9 (hidden meaning, `དབྱེ་བ།`) | identical | MATCH |

This spot-check confirmed the *text* of each quotation was unaltered by the register rewrite, but
did not itself catch two problems a later review found: (1) the lead's root-verse quotation was
wrongly treated as budget-exempt (see "Quotation budget & pairing fix" above — it has since been
converted to paraphrase), and (2) the `taranatha:c-9-9` quotation had been given a second ref
(`palden-sherab`) implying both commentaries share the exact quoted wording, which a direct
`1-SOURCES/` check (not just a diff against the v1 record) shows is not the case for the full
quoted string. Both are corrected below.

### Quotation budget fix — fresh source verification (2026-08-21, second pass)

The article now retains exactly 2 verbatim quotations. Each was checked directly against its
cited `1-SOURCES/` file (not merely diffed against the prior record), and each is now attributed
in-article to exactly one commentary:

| # | Quotation | Attributed to (in-article) | Checked against | Result |
|---|---|---|---|---|
| 1 | "རྗེ་བཙུན་སྒྲོལ་མའི་ཕྱག་གཡོན་པའི་མཐེ་མོ་དང་གུང་མོ་གཉིས་ཀྱིས་མེ་ཏོག་ཨུཏྤལའི་ཡུ་བ་བཟུངས་ཤིང་། མཛུབ་མོ་དང་སྲིན་ལག མཐེའུ་ཆུང་བཅས་གསུམ་སྒྲེང་བ" (finger-assignment divergence, `མཚན་ཉིད།`) | `sungrab-tulku` (sole ref on this quotation) | `1-SOURCES/Commentaries/སྒྲོལ་མཉེར་གཅིག་གི་རྣམ་བཤད།.md#^0-63` | **PASS** — exact substring, confirmed |
| 2 | "སྦས་དོན་ནི། དཀོན་མཆོག་གསུམ་མཚོན་ནི་ཁུ་རྡུལ་རླུང་གསུམ་སྟེ།" (hidden-meaning gloss, `དབྱེ་བ།`) | `taranatha` (sole ref on this quotation, after this fix) | `1-SOURCES/Commentaries/ཕྱག་འཚལ་ཉེར་གཅིག་གི་བསྟོད་པའི་རྣམ་པར་བཤད་པ།.md#^0-33` | **PASS** — exact substring, confirmed |

For comparison, the same string checked against `palden-sherab`'s source
(`...ཞེས་བྱ་བཞུགས་སོ།.md#^0-102`, claim `c-3-1-9-3-1`) is **FAIL** — that source's sentence opens
"གསུམ་པ་སྦས་དོན་རྫོགས་རིམ་མཚན་བཅས་ལྟར་ན།", not "སྦས་དོན་ནི།", so the quoted string as a whole is not
an exact substring there, which is why `palden-sherab` no longer carries a ref on this quotation
and instead supports its own, separate, unquoted paraphrase sentence.

**Both of the article's final 2 verbatim quotations are PASS, each unambiguously paired to one
registered commentary.** No quotation text was altered from what v1 originally verified; only (a)
the lead's root-verse span was de-quoted into paraphrase, and (b) the hidden-meaning quotation's
attribution was narrowed from two refs to its one verified source.
