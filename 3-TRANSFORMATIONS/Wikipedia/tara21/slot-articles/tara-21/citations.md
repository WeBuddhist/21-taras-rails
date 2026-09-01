---
topic: tara-21
article: article.md
method: wiki-article-from-claims-v2
revision_mode: B
source_article: 3-TRANSFORMATIONS/Wikipedia/tara21/slot-articles/tara-21/article.md (v1, wiki-article-from-claims, dated 2026-08-11)
revision_date: 2026-08-21
context_packages:
  - 2-RAILS/Claims/tara-21.md
rails_status: draft
raw_sources_cited:
  - 2-RAILS/Claims/raw/tree-guided/yama-sonam.md
  - 2-RAILS/Claims/raw/tree-guided/dharmabhadra.md
  - 2-RAILS/Claims/raw/tree-guided/drakpa-gyaltsen.md
  - 2-RAILS/Claims/raw/tree-guided/gendun-drub.md
  - 2-RAILS/Claims/raw/tree-guided/gendun-gyatso.md
  - 2-RAILS/Claims/raw/tree-guided/karma-maitri.md
  - 2-RAILS/Claims/raw/tree-guided/konchok-thabkhe.md
  - 2-RAILS/Claims/raw/tree-guided/lobsang-dawa.md
  - 2-RAILS/Claims/raw/tree-guided/palden-sherab.md
  - 2-RAILS/Claims/raw/tree-guided/pema-namgyal.md
  - 2-RAILS/Claims/raw/tree-guided/sangye-nyentrul.md
  - 2-RAILS/Claims/raw/tree-guided/sungrab-tulku.md
  - 2-RAILS/Claims/raw/tree-guided/taranatha.md
  - 2-RAILS/Claims/raw/tree-guided/tenga-tulku.md
  - 2-RAILS/Claims/raw/tree-guided/tenzin-dhonzang.md
  - 2-RAILS/Claims/raw/tree-guided/tsultrim-namdak.md
date: 2026-08-11
status: draft
---

> [!note] Polished — gemini-article-polish, 2026-08-23, model gemini-3.1-pro-preview; claim usage unchanged from 3-TRANSFORMATIONS/Wikipedia/tara21/slot-articles/tara-21/article.md (pre-polish).

# Citations — tara-21

**Revision note (2026-08-21, Mode B):** this file and `article.md` were rewritten in place
from the v1 draft (`wiki-article-from-claims`, dated 2026-08-11) per
`4-SYSTEM/Skills/wiki-article-from-claims-v2/SKILL.md`'s Mode B procedure. Mode B does not
return to `2-RAILS/Claims/` or the raw tree-guided files — every claim ID, quotation, and
`Cite:` target below is carried forward unchanged from the v1 file, which is treated as
settled ground truth. No new claim ID was introduced. The only research-adjacent step taken
was a frontmatter-only lookup of each commentary's `author_in_use` value (already present in
every one of the sixteen raw files, so no fallback was needed — see Warnings).

All sixteen commentaries listed in `2-RAILS/Claims/tara-21.md`'s `sources:` frontmatter contribute
claims to this slot, and all sixteen remain cited by `<ref>` in the revised `article.md` (verified
by ref-count sweep; see Verification below).

## Reference map

Unchanged from the v1 file for every retained claim ID — reproduced here for continuity. The
claim IDs, བོད་ཡིག quotations, English glosses, and source blocks are identical to v1's table;
only which refs are attached to which sentence, and how many quotations are rendered verbatim
versus paraphrased, changed in the rewrite (see "Full attestation beyond in-article refs" and
"Quotation budget" below).

| Ref (`<ref name>`) | Commentary | Claim ID(s) drawn on | Quotation retained verbatim in v2? | Source block |
|---|---|---|---|---|
| `yama-sonam` | yama-sonam | c-3-21-1, c-3-21-2, c-3-21-3 (root verse), c-3-21-4, c-3-21-5, c-3-21-6, c-3-21-7, c-3-21-8, c-3-21-9, c-3-21-10 | Yes — root verse (c-3-21-3, lead, exempt) and whose-three-places rejection (c-3-21-5, divergence section, budget quote 2 of 2) | `1-SOURCES/Commentaries/སྒྲོལ་མའི་འགྲེལ་བ་འཕྲིན་ལས་ཆར་དུ་སྙིལ་བའི་སྤྲིན་ཕུང་།.md#^0-252, #^0-254, #^0-260, #^0-261, #^0-263` |
| `palden-sherab` | palden-sherab | c-3-1-21-0-1, c-3-1-21-1-1…1-3, c-3-1-21-2-1…2-2, c-3-1-21-3-1…3-2, c-3-1-21-4-1…4-2 | No — all paraphrased in v2 (name, iconography, benefit, hidden-meaning equation) | `...#^0-203, #^0-207, #^0-211` |
| `sungrab-tulku` | sungrab-tulku | c-24-1, c-24-2, c-24-3, c-24-4 | No — practitioner-self quote paraphrased in v2 | `1-SOURCES/Commentaries/སྒྲོལ་མཉེར་གཅིག་གི་རྣམ་བཤད།.md#^0-111` |
| `tenzin-dhonzang` | tenzin-dhonzang | c-4-21-1…c-4-21-11 | No — name and mantra quotes paraphrased/de-quoted in v2 | `1-SOURCES/Commentaries/སྒྲོལ་མ་ཉེར་གཅིག་གི་བསྟོད་འགྲེལ་སྙིང་གི་ནོར་བུ.md#^0-281, #^0-287` |
| `dharmabhadra` | dharmabhadra | c-1-2-3-6-1…6-4 | No — seed-syllable and "eighteen" quotes paraphrased/de-quoted in v2 | `.../ཨུཏྤལའི་ཆུན་པོ་ཞེས་བྱ་བ་བཞུགས་སོ།.md#^0-93, #^0-94` |
| `gendun-drub` | gendun-drub | c-2-2-2-3-6-1…6-3 | No — name quote paraphrased in v2 | `1-SOURCES/Commentaries/སྒྲོལ་མ་ཕྱག་འཚལ་ཉེར་གཅིག་གི་ཊཱིཀྐ་རིན་པོ་ཆེའི་ཕྲེང་བ།.md#^0-105` |
| `lobsang-dawa` | lobsang-dawa | c-1-2-3-6-1…6-3 | No — "eighteen" de-quoted in v2 | `1-SOURCES/Commentaries/སྒྲོལ་མ་ཕྱག་འཚལ་ཉེར་གཅིག་གི་མཆན་འགྲེལ་བཞུགས་སོ།.md#^0-30` |
| `tenga-tulku` | tenga-tulku | c-1-2-3-6-1…6-4 | No — was already unquoted in v1 | `1-SOURCES/Commentaries/ཕྱག་འཚལ་ཉེར་གཅིག་གི་ཕན་ཡོན་དང་བཅས་པ་གསལ་བའི་མེ་ལོང་ཞེས་བྱ་བ་བཞུགས་སོ།། །།.md#^0-172` |
| `sangye-nyentrul` | sangye-nyentrul | c-22-0-1…0-3, c-22-1-1…1-3 | No — etymology, name-variant, iconography, benefit quotes all paraphrased/de-quoted in v2 | `.../འཕགས་མའི་བྱིན་རླབས་གྲུ་ཆར་བཞུགས།།.md#^0-92, #^0-93` |
| `konchok-thabkhe` | konchok-thabkhe | c-2-21-1…21-4, c-2-22-1…22-3 | No — classification and alt.-count quotes de-quoted in v2 | `.../ཞལ་ལུང་ཞེས་བྱ་བ་བཞུགས་སོ།.md#^0-97, #^0-103` |
| `drakpa-gyaltsen` | drakpa-gyaltsen | c-1-97…100 | No — "ten-syllable" de-quoted in v2 | `.../གསལ་བའི་འོད་ཟེར་ཞེས་བྱ་བ་བཞུགས་སོ།.md#^0-84` |
| `karma-maitri` | karma-maitri | c-1-1-21-1…21-6 | No — 21-emanations and "ten-syllable" de-quoted/paraphrased in v2 | `1-SOURCES/Commentaries/ཕྱག་འཚལ་སྒྲོལ་མ་ཉེར་གཅིག་གི་བསྟོད་པའི་བསྡུས་འགྲེལ།.md#^0-47, #^0-48` |
| `pema-namgyal` | pema-namgyal | c-2-4-54…56 | No — "eighteen" de-quoted in v2 | `.../ཕྱག་འཚལ་ཉེར་གཅིག་གི་བསྟོད་འགྲེལ་བདུད་རྩིའི་དགའ་ཚལ་བཞུགས་སོ།།.md#^0-69` |
| `taranatha` | taranatha | c-21-1-1…1-8, c-21-2-1…2-3, c-21-3-1…3-9, c-21-4-1…4-22 | Yes — Ture-emendation quote (c-21-1-8, name section, budget quote 1 of 2) retained; hidden-meaning equation (c-21-3-4) and "eighteen" (c-21-1-4) paraphrased/de-quoted | `1-SOURCES/Commentaries/ཕྱག་འཚལ་ཉེར་གཅིག་གི་བསྟོད་པའི་རྣམ་པར་བཤད་པ།.md#^0-74, #^0-76` |
| `gendun-gyatso` | gendun-gyatso | c-1-21-1…21-3 | No — "ten-syllable" de-quoted in v2 | `1-SOURCES/Commentaries/ཕྱག་འཚལ་སྒྲོལ་མ་ཉེར་གཅིག་མའི་རྣམ་བཤད།.md#^0-35` |
| `tsultrim-namdak` | tsultrim-namdak | c-2-1-2-1-71…74, c-3-24, c-8-4 | No — name quote paraphrased in v2 | `1-SOURCES/Commentaries/སྒྲོལ་འགྲེལ་ཚོགས་གཉིས་རྒྱ་མཚོར་འཇུག་པའི་གྲུ་གཟིངས།.md#^0-262` |

## Quotation budget (Rule 6)

v1 carried 33 verified quotations. v2 retains exactly **2** verbatim commentary quotations
(plus the lead's root-text verse quotation, which is exempt from the budget per Rule 6 for
deity-profile articles):

1. **Lead (exempt):** root verse, `yama-sonam:c-3-21-3` — "ཕྱག་འཚལ་དེ་ཉིད་གསུམ་རྣམས་བཀོད་པས།
   ...འཇོམས་པ་ཏུ་རེ་རབ་མཆོག་ཉིད་མ།"
2. **Budget quote 1/2**, `མཚན་གྱི་ངེས་ཚིག` section: `taranatha:c-21-1-8`, the *tu re* root-verse
   emendation — "ཡང་ན་ཏུ་རེ་ནི་མྱུར་མ་སྟེ། ...བཅོས་ན་བདེའོ།" Retained because the exact
   proposed reformulation of the root verse's wording is itself the content of the divergence
   being reported.
3. **Budget quote 2/2**, `གཞུང་ལུགས་སོ་སོའི་བཤད་པ།` section: `yama-sonam:c-3-21-5`, the
   whose-three-places rejection — "འགྲེལ་པ་འགའ་ཞིག་ལས་ཡི་གེ་གསུམ་སྒྲུབ་པ་པའི་གནས་གསུམ་ལ་
   བཀོད་པའི་དོན་དུ་སྦྱར་སྣང་ཡང་འདི་ལྷ་མོ་ལ་བསྟོད་པའི་སྐབས་ཡིན་པས་ལྷ་མོའི་གནས་གསུམ་ལ་
   བྱ་དགོས་ཤིང་།" Retained because this is the sharpest doctrinal disagreement in the article
   (two schools directly conflict) and the exact phrasing establishes what is being rejected.

All 31 other v1 quotations were converted to unquoted wikivoice or attributed paraphrase,
grounded in the same claim's already-recorded བོད་ཡིག/English gloss — no new wording was
invented. Short technical terms and counts (e.g. བཅོ་བརྒྱད, ཡི་གེ་བཅུ་པ, བར་བྱེད, བླུ་བྱེད,
the mantra ཨོཾ་ཏཱ་རེ་ཏུ་ཏྟཱ་རེ་ཏུ་རེ་སྭ་ཧཱ) are now presented as plain unquoted labels inline —
consistent with Rule 3's intent (verbatim *sentence* quotations) rather than as budgeted
quotations, since they are single terms/counts/mantra-syllables being named, not interpretive
prose being quoted.

## Citation cap (Rule 7) and full attestation beyond in-article refs

Every statement in the revised article carries at most 3 `<ref>` tags (swept mechanically;
max cluster size = 3). Where a v1 statement carried more attestations than the cap allows, the
excess refs were dropped from that specific sentence and the underlying claim IDs are listed
below by statement. Every dropped commentary remains cited by `<ref>` elsewhere in the article
(confirmed — all sixteen commentaries have ≥1 `<ref>` tag in `article.md`), so nothing drops out
of the bibliography.

- **Lead, ordinal/final-homage statement** ("...ཕྱག་འཚལ་ཡིན་པར་...མཚོན།"): v1 cited
  yama-sonam, palden-sherab, sungrab-tulku, tenzin-dhonzang (4). v2 caps to yama-sonam,
  sungrab-tulku, tenzin-dhonzang (3). Dropped: `palden-sherab` (its ordinal/name attestation,
  `c-3-1-21-0-1`) — still cited elsewhere (name section, iconography, activity, divergence).
- **Lead, sixth-by-activity statement** ("འགྲེལ་པ་བཞིས་ནི་...དྲུག་པར་ངོས་འཛིན་བྱེད།"): v1
  cited dharmabhadra, gendun-drub, lobsang-dawa, tenga-tulku (4). v2 caps to dharmabhadra,
  gendun-drub, tenga-tulku (3). Dropped: `lobsang-dawa` (`c-1-2-3-6-1`) — still cited elsewhere
  (activity section, "eighteen" spirits group).
- **Name section, "decline new name, characterize by activity" statement**: v1 cited
  dharmabhadra, gendun-drub, tenga-tulku, sungrab-tulku (4). v2 caps to dharmabhadra,
  gendun-drub, tenga-tulku (3). Dropped: `sungrab-tulku` (`c-24-4`) — still cited elsewhere
  (lead, activity section, divergence section).
- **Name section, "no name given" statement**: v1 cited drakpa-gyaltsen, gendun-gyatso,
  lobsang-dawa, pema-namgyal (4). v2 caps to drakpa-gyaltsen, gendun-gyatso, pema-namgyal (3).
  Dropped: `lobsang-dawa` (`c-1-2-3-6-1`, no-name variant) — still cited elsewhere.
- **Activity section, "eighteen spirits" statement**: v1 cited dharmabhadra, lobsang-dawa,
  palden-sherab, pema-namgyal, taranatha (5). v2 caps to dharmabhadra, lobsang-dawa, taranatha
  (3). Dropped: `palden-sherab` (`c-3-1-21-1-3`), `pema-namgyal` (`c-2-4-55`) — both still cited
  elsewhere.
- **Activity section, "general destruction, no count given" statement**: v1 cited yama-sonam,
  gendun-drub, karma-maitri, konchok-thabkhe, sungrab-tulku, tsultrim-namdak (6). v2 caps to
  yama-sonam, gendun-drub, konchok-thabkhe (3). Dropped: `karma-maitri` (`c-1-1-21-5`),
  `sungrab-tulku` (`c-24-2`), `tsultrim-namdak` (`c-2-1-2-1-71…74`) — all three still cited
  elsewhere.
- **Activity section, "ten-syllable mantra" statement**: v1 cited drakpa-gyaltsen,
  gendun-gyatso, karma-maitri, tenzin-dhonzang (4). v2 caps to drakpa-gyaltsen, gendun-gyatso,
  tenzin-dhonzang (3). Dropped: `karma-maitri` (`c-1-1-21-4`) — still cited elsewhere.

No claim ID was dropped from the article's evidentiary basis — every excess ref named above
still supports the same sentence in substance (the sentence's prose asserts the same
attestation breadth, e.g. "འགྲེལ་པ་བཞིས"/"འགྲེལ་པ་ལྔས"/"འགྲེལ་པ་ལྔས" wording is retained even
where only 3 refs are attached), per Rule 7's allowance that "attestation breadth may be
asserted in prose... backed by 2–3 refs."

## Claims used but not quoted

Unchanged in substance from v1 (see v1's note on `taranatha`'s condensed ultimate-meaning
material, `tenzin-dhonzang`'s condensed spirit-enumerations, and `tsultrim-namdak`'s
single-word-only quotation practice) — all of that material remains paraphrased, not quoted,
in v2 as well. Additionally in v2: all name-section naming statements, all short technical
terms/counts, and the mantra transliteration are now presented unquoted (see Quotation budget
above) — these were quoted in v1 but are paraphrased/de-quoted in v2 to meet the 2-quotation
budget.

## Unresolvable attestations

None (unchanged from v1). Mode B did not re-resolve any claim ID against
`2-RAILS/Claims/raw/tree-guided/`; every claim ID used in v2 already appears, resolved, in v1's
citations table.

## Warnings

- **`rails_status` is `draft`, not `complete`** (unchanged from v1; carried forward as a known,
  accepted risk for this hand-run skill invocation).
- **No `sources.yaml` / URLs** (unchanged from v1 — not applicable to this hand-run skill).
- **`yama-sonam`'s author is རྗེ་བཙུན་ཡ་མ་བསོད་ནམས་** (unchanged from v1's note).
- **`author_in_use` resolution (Rule 17): no fallback needed.** All sixteen raw tree-guided
  files' frontmatter already carry an `author_in_use` key (verified 2026-08-21 via a
  frontmatter-only read of each `2-RAILS/Claims/raw/tree-guided/<id>.md`), and the v1 article's
  in-prose names already matched those values exactly (e.g. `taranatha` → ཇོ་ནང་ཏཱ་ར་ནཱ་ཐ་,
  `pema-namgyal` → ཟུར་མང་མཁན་པོ་པདྨ་རྣམ་རྒྱལ་, `gendun-drub` → རྒྱལ་བ་དགེ་འདུན་གྲུབ་,
  `gendun-gyatso` → རྒྱལ་བ་དགེ་འདུན་རྒྱ་མཚོ་). No warning-worthy fallback occurred; v2 carries
  the same in-prose names forward unchanged (with trailing shad/tsheg adjusted where the name
  now sits mid-sentence rather than before a quotation mark). The bibliography and `<ref>`
  content continue to use each commentary's formal `author` + `title` (e.g. `pema-namgyal`'s
  bibliography line keeps ལྡོམ་བུ་བ་པདྨ་རྣམ་པར་རྒྱལ་བ, not the prose `author_in_use` form),
  per Rule 17's instruction that `author_in_use` is for prose mentions only.
- **Punctuation contract applied throughout (Rules 15–16).** Every comma in v1's fence body
  (22 instances, mostly the `<ref .../>,` pattern Rule 16 names as "always wrong") was removed.
  Every sentence now ends in a single shad before any trailing `<ref>` tags; every paragraph's
  final sentence ends in a double shad (ཉིས་ཤད, `།།`), placed before trailing `<ref>` tags where
  present. Verified by an automated sweep of the fence body: zero comma characters (ASCII,
  fullwidth, or ideographic), zero instances of punctuation immediately following a `</ref>` or
  `/>` close, and every one of the article's paragraph blocks (split on blank lines, excluding
  headings/tail sections) ends in `།།`.
- **Register conversion (Rules 5, 8–9).** The `མཚན་གྱི་ངེས་ཚིག` and
  `གཞུང་ལུགས་སོ་སོའི་བཤད་པ།` sections remain attributed prose throughout, since neither
  qualifies as "majority-attested and uncontested": naming is genuinely divergent across all
  sixteen commentaries (no majority position), and the tradition-specific section is by
  definition ⚑ divergence material (Rule 5's carve-out). The `སྐུ་ཡི་རྣམ་པ།` section documents
  two competing iconographic accounts (yama-sonam's vs. the palden-sherab/sangye-nyentrul/
  tsultrim-namdak group's) and stays attributed for the same reason. The
  `ཕྲིན་ལས་དང་ནུས་མཐུ།` section's fifteen-commentary seed-syllable/three-place mechanism and
  its four-color elaboration were converted to wikivoice (no commentator names, capped refs) as
  genuine majority-attested, uncontested consensus; the spirit-count and mantra-syllable-count
  material keeps a wikivoice majority clause plus an attributed minority/unique clause where the
  consolidated page itself records a split. `བསྡུས་དོན།` is wikivoice throughout.
- **One judgment call carried forward from v1 on V8** ("every section contains ≥1 citation"):
  the tail sections (`འབྲེལ་ཡོད་ཤོག་ངོས།`, `ལུང་ཁུངས།`, `དཔྱད་གཞིའི་ཡིག་ཆ།`) carry no `<ref>`
  tags, matching the wikitext spec's own doctrinal-term skeleton and v1's precedent. Every
  substantive body section carries multiple citations.
- **No `ལོ་རྒྱུས།` section** (unchanged from v1 — no origin narrative attested for this slot).
- **Related-pages and bibliography content unchanged from v1** — same three related-page
  targets, same sixteen-commentary bibliography (all sixteen remain cited by `<ref>` in the
  v2 body; see the citation-cap sweep above and the ref-count-per-commentary check in
  Verification).

## Verification

**Quote spot-check (Mode B step 6 — text diff against v1's already-PASS quotations, not a
fresh `1-SOURCES/` lookup):**

| # | Commentary | Claim ID | v2 quotation | Exact match to v1's PASS-verified quotation? |
|---|---|---|---|---|
| 1 | yama-sonam | c-3-21-3 (root verse, lead, exempt) | ཕྱག་འཚལ་དེ་ཉིད་གསུམ་རྣམས་བཀོད་པས།...འཇོམས་པ་ཏུ་རེ་རབ་མཆོག་ཉིད་མ། | PASS — extracted programmatically from v1's fence body via exact substring match, byte-identical |
| 2 | taranatha | c-21-1-8 (budget quote 1/2) | ཡང་ན་ཏུ་རེ་ནི་མྱུར་མ་སྟེ།...ཞེས་བཅོས་ན་བདེའོ། | PASS — extracted programmatically from v1's fence body via exact substring match, byte-identical (includes v1's already-corrected འགྱུར་པས, not the original misquote འགྱུར་བས) |
| 3 | yama-sonam | c-3-21-5 (budget quote 2/2) | འགྲེལ་པ་འགའ་ཞིག་ལས་ཡི་གེ་གསུམ་སྒྲུབ་པ་པའི་གནས་གསུམ་ལ་བཀོད་པའི་དོན་དུ་སྦྱར་སྣང་ཡང་འདི་ལྷ་མོ་ལ་བསྟོད་པའི་སྐབས་ཡིན་པས་ལྷ་མོའི་གནས་གསུམ་ལ་བྱ་དགོས་ཤིང་། | PASS — extracted programmatically from v1's fence body via exact substring match, byte-identical |

All 2 retained non-exempt quotations plus the exempt lead root-verse quotation are unchanged,
exact substrings of what v1's citations.md already recorded as PASS. No quotation in v2 was
freshly checked against `1-SOURCES/`, per Mode B's instruction to spot-verify against the prior
PASS record rather than re-deriving.

**Mechanical sweeps (this revision):**

- Comma characters (ASCII `,`, fullwidth `，`, ideographic `、`) in the fence body: **0**.
- Punctuation immediately following a `</ref>` or self-closing `<ref .../>`: **0** instances.
- Maximum `<ref>` tags attached to one statement (consecutive-cluster sweep): **3** (cap holds
  everywhere).
- `<ref name="...">` full definitions: **16**, each commentary defined exactly once (the v1→v2
  edit also fixed one accidental duplicate full-definition of `sungrab-tulku` introduced during
  drafting, before this citations.md was finalized).
- Every one of the sixteen commentaries has ≥1 `<ref name="...">` tag (self-closing or full) in
  the revised article body — counts range from 1 (`karma-maitri`, `lobsang-dawa`) to 12
  (`palden-sherab`).
- `article-preview.md` regenerated via
  `4-SYSTEM/Skills/wiki-article-from-claims-v2/scripts/make_preview.py`: exits `OK`; contains no
  `<ref>` tags and no `[[...]]` wikitext links; all sixteen footnotes present, keyed by each
  commentary's `author_in_english`-derived slug.
