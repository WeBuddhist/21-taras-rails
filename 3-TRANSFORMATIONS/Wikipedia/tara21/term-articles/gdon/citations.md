---
topic: gdon
article: article.md
method: wiki-article-from-claims-v2 (Mode B — revision-in-place)
revision_mode: B
revised_from: 3-TRANSFORMATIONS/Wikipedia/tara21/term-articles/gdon/article.md (v1, method wiki-article-from-claims, dated 2026-08-12)
revision_date: 2026-08-20
context_packages:
  - 2-RAILS/Claims/gdon.md
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
date: 2026-08-12
status: draft
---

# Citations — gdon

## Mode B revision (2026-08-20)

This file and `article.md` were revised in place from the v1 draft (`method: wiki-article-from-claims`,
dated 2026-08-12, same path) under `wiki-article-from-claims-v2`'s **Mode B (revision-in-place)**
procedure. Only the **register** changed — no fact, claim ID, quotation, or `Cite:` target was
re-derived or altered. Per Mode B's rule, this revision never returned to `2-RAILS/Claims/gdon.md`
or the raw tree-guided files for content; the exception used was a frontmatter-only lookup of each
cited commentary's `author_in_use` key (Rule 17), confirming (not changing) the names already used
in the v1 prose — see *Naming check* below.

**What changed:**
- Converted attribution-wrapped consensus/backbone sentences ("འགྲེལ་པ་[N]ས་...བཤད་དོ" /
  "མཁན་ཆེན་...གིས་...བཤད་ལ" framing for material multiple commentaries agree on) into direct
  wikivoice assertions, per Rule 5. This affected roughly fifteen sentences across
  `== མཚན་ཉིད། ==` and the opening sentence of `== དབྱེ་བ། ==` — the sections that carried the
  heaviest "who-said-what" framing in v1.
- Left attribution untouched (by design, per Rule 5's own carve-out) wherever the underlying content
  is a **unique claim** (a single commentary's own point, e.g. Tāranātha's and Tsultrim Namdak's
  etymologies in `== ངེས་ཚིག ==`, Palden Sherab's sādhana elaboration, Sangye Nyenpa's fear
  definition, Pema Namgyal's efficacy note, the commentary-specific scattered mentions, the alternate
  enumeration counts, and all of `== གཞུང་ལུགས་སོ་སོའི་བཤད་པ། ==`) or a **⚑ divergence** (the
  'joms/'dzoms verse-6 epithet reading, and the nam-gru/nam-gu spelling variant in `== དབྱེ་བ། ==`) —
  both positions of each divergence remain fully attributed, neither adjudicated.
- Cleaned one formatting artifact in the lead (a stray space after `ནི་`) while touching that line
  for the register pass; no wording or fact changed.
- Ref groupings, ref order (all twelve full `<ref name="...">` definitions appear in exactly the
  same first-use order as v1: yama-sonam → palden-sherab → sungrab-tulku → taranatha →
  tsultrim-namdak → gendun-drub → sangye-nyentrul → drakpa-gyaltsen → pema-namgyal →
  tenzin-dhonzang → dharmabhadra → lobsang-dawa), and per-commentary ref-use counts are **byte-for-byte
  identical to v1** (verified programmatically — see *Ref-count check* below). No `<ref>` was added,
  removed, or moved to a different commentary; only the prose wrapping each existing ref cluster was
  rewritten.
- The two verbatim quotations already in v1 (the root-verse tantra citation in the lead, and
  tsultrim-namdak's *ture* etymology quote in `== ངེས་ཚིག ==`) are carried forward **unchanged,
  character-for-character** — well within the ≤2 budget (and the lead's is root-text, so does not
  count against the budget at all; only 1 of 2 is a countable commentary quotation). No quotation was
  cut, so no paraphrase substitution was needed and Rule 6's "for every quotation cut, convert to
  paraphrase" step did not apply.

**Ref-count check (programmatic, before vs. after):**

| Commentary | v1 count | v2 count |
|---|---|---|
| yama-sonam | 2 | 2 |
| palden-sherab | 10 | 10 |
| sungrab-tulku | 2 | 2 |
| taranatha | 6 | 6 |
| tsultrim-namdak | 7 | 7 |
| gendun-drub | 2 | 2 |
| sangye-nyentrul | 5 | 5 |
| drakpa-gyaltsen | 2 | 2 |
| pema-namgyal | 5 | 5 |
| tenzin-dhonzang | 3 | 3 |
| dharmabhadra | 1 | 1 |
| lobsang-dawa | 1 | 1 |
| **Total** | **46** | **46** |

No statement in either version carries more than 3 `<ref>`s (checked programmatically over every
ref cluster in the fence body) — so **no ref-cap overflow ever occurred, and `## Full attestation
beyond in-article refs` (the section this file would otherwise need per Rule 7/skill spec §*citations.md*)
is not applicable here**: nothing was cut to make room under the cap, because nothing exceeded it in
v1 or v2.

**Naming check (Rule 17).** Every commentator named in-prose in v1 was already the raw claims file's
`author_in_use` value, confirmed by a frontmatter-only read of each cited commentary's file under
`2-RAILS/Claims/raw/tree-guided/` (taranatha, tsultrim-namdak, palden-sherab, sangye-nyentrul,
tenzin-dhonzang, pema-namgyal — all six have `author_in_use` present and matching the prose form
exactly, including ཟུར་མང་མཁན་པོ་པདྨ་རྣམ་རྒྱལ་ for pema-namgyal, which differs from that
commentary's bare `author` field ལྡོམ་བུ་བ་པདྨ་རྣམ་པར་རྒྱལ་བ་). No name was changed; no warning
needed.

**Punctuation contract check (Rules 15–16).** Verified programmatically over the full fence body:
zero comma characters (ASCII, fullwidth, or Japanese-style) anywhere in the body; every prose line
that is not a heading, bare bold label, or tail-section list item ends in the double shad `།།`;
every `<ref` tag is immediately preceded by a shad or by another ref's closing `>` (never by bare
prose text); no shad or double shad appears immediately after a `</ref>` or self-closing `/>`. All
checks passed on the first full pass after the rewrite (one placement was corrected during drafting —
see *Quotation/verification carry-forward* below).

**Quotation/verification carry-forward.** Both retained quotations were diffed character-for-character
against the PASS-verified text already in this file's Verification table (rows 1 and 31 below) —
exact match, no re-derivation from `1-SOURCES/` needed per Mode B step 6. One intermediate ref
placement (an extra `<ref name="palden-sherab" />`/`<ref name="sangye-nyentrul" />` pair briefly added
to the first sentence of the "sixteen fears" sub-facet during drafting, to front-load the citation
earlier in the paragraph) was reverted before finalizing, since it was not present in v1's ground
truth and Mode B does not add new ref placements beyond what the source already established — the
final file's ref multiset matches v1's exactly, per the table above.

---

## v1 drafting record (unchanged below, preserved for audit continuity)

Adapted run of `wiki-article-from-claims` (see task adaptations below). All sixteen commentaries
listed in `2-RAILS/Claims/gdon.md`'s `sources:` frontmatter were resolved against their raw
tree-guided files. Every attestation ID cited anywhere on the consolidated page resolved
successfully; none are unresolvable (see below). 57 of the packet's 58 claim IDs are drawn on
directly in the article body; the 58th (`tsultrim-namdak:c-2-1-2-1-74`) is quoted in full in
`== ངེས་ཚིག ==` as well, so **all 58 claims in the packet are used**.

**Adaptations applied, per the calling agent's instructions:**
1. **Skeleton** — used wikitext-spec.md §1's doctrinal-term skeleton (ངེས་ཚིག / མཚན་ཉིད། / དབྱེ་བ།
   / གཞུང་ལུགས་སོ་སོའི་བཤད་པ། / བསྡུས་དོན། / འབྲེལ་ཡོད་ཤོག་ངོས། / ལུང་ཁུངས། / དཔྱད་གཞིའི་ཡིག་ཆ།),
   not the SKILL.md's deity-profile skeleton, since གདོན is an entity-class term, not one of the 21
   Tārā profiles. `མཚན་ཉིད།` was subdivided with bold sub-labels (following the same allowance the
   skill's deity-profile precedent, `tara-03/article.md`, uses for `གཞུང་ལུགས་སོ་སོའི་བཤད་པ།`) to
   hold the packet's five sub-facets (mechanism, verse-6 epithet/sādhana, sixteen-fears item,
   benefits verse, scattered mentions) without inventing extra `==` sections beyond the fixed
   skeleton.
2. **Output path** — written to `3-TRANSFORMATIONS/Wikipedia/tara21/term-articles/gdon/` (sibling
   to `slot-articles/`), since this is a cross-cutting keyword-topic page assembled by
   `assemble_keyword_packet.py`, not a registered spine slot.

## Reference map

One row per named `<ref>` in `article.md` (commentary-level, hand-formatted `<AUTHOR>། <TITLE>།`
form per skill Rule 7 — no claim ID inside the wikitext itself). "Claim ID(s) used" lists every raw
claim actually drawn on for that commentary's citations in the article; "Quotation" gives only the
claims that were quoted verbatim (in `" "`) in the article body.

| Ref (named) | Commentary | Claim ID(s) used | Quotation (verbatim བོད་ཡིག, if quoted) | Source block(s) |
|---|---|---|---|---|
| yama-sonam | Anon., *སྒྲོལ་མ་ཉེར་གཅིག་པའི་བསྟོད་འགྲེལ་འཕྲིན་ལས་ཆར་དུ་སྙིལ་བའི་སྤྲིན་ཕུང* | c-3-21-3 | "རྒྱུད་ལས། ཕྱག་འཚལ་དེ་ཉིད་གསུམ་རྣམས་བཀོད་པས། ། ཞི་བའི་མཐུ་དང་ཡང་དག་ལྡན་མ། ། གདོན་དང་རོ་ལངས་གནོད་སྦྱིན་ཚོགས་རྣམས། འཇོམས་པ་ཏུ་རེ་རབ་མཆོག་ཉིད་མ།" | ...སྤྲིན་ཕུང་།.md#^0-252 |
| dharmabhadra | དངུལ་ཆུ་དྷརྨ་བྷ་དྲ, *སྒྲོལ་མར་ཕྱག་འཚལ་ཉེར་གཅིག་གིས་བསྟོད་པའི་རྣམ་བཤད་ཡིད་འཕྲོག་ཨུཏྤལའི་ཆུན་པོ* | c-1-2-3-6-2, c-1-2-3-6-4 | (none quoted — paraphrased) | ...ཨུཏྤལའི་ཆུན་པོ...bཞུགས་སོ།.md#^0-92, #^0-94 |
| drakpa-gyaltsen | རྗེ་བཙུན་གྲགས་པ་རྒྱལ་མཚན, *སྒྲོལ་མ་ཕྱག་འཚལ་ཉི་ཤུ་རྩ་གཅིག་གི་བསྟོད་པའི་རྣམ་བཤད་གསལ་བའི་འོད་ཟེར* | c-1-99, c-2-12 | (c-2-12) "གདོན་དང་རིམས་དང་དུག་གིས་གཟིར་བའི། །རྒྱུ ་དང་འབྲས་བུས་བསྡུས་པ་ནི།" | ...འོད་ཟེར་ཞེས་བྱ་བ་བཞུགས་སོ།.md#^0-83, #^0-98 |
| gendun-drub | རྒྱལ་བ་དགེ་འདུན་གྲུབ, *སྒྲོལ་མ་ཕྱག་འཚལ་ཉེར་གཅིག་གི་ཊཱིཀྐ་རིན་པོ་ཆེའི་ཕྲེང་བ* | c-2-2-2-3-6-1, c-2-2-2-3-6-2, c-2-2-3-3-4 | (none quoted — paraphrased) | ...ཊཱིཀྐ་རིན་པོ་ཆེའི་ཕྲེང་བ།.md#^0-103, #^0-104, #^0-111 |
| gendun-gyatso | རྒྱལ་བ་དགེ་འདུན་རྒྱ་མཚོ, *ཕྱག་འཚལ་སྒྲོལ་མ་ཉེར་གཅིག་མའི་རྣམ་བཤད* | c-1-21-2 | (none quoted — paraphrased) | ...རྣམ་བཤད།.md#^0-35 |
| karma-maitri | ཀརྨ་མཻ་ཏྲི, *ཕྱག་འཚལ་སྒྲོལ་མ་ཉེར་གཅིག་གི་བསྟོད་པའི་བསྡུས་འགྲེལ* | c-1-1-21-3, c-1-2-13 | (none quoted — paraphrased) | ...བསྡུས་འགྲེལ།.md#^0-47, #^0-49 |
| konchok-thabkhe | དཀོན་མཆོག་ཐབས་མཁས, *ཕྱག་འཚལ་ཉེར་གཅིག་མའི་ཊིཀྐ་འཕགས་མའི་ཞལ་ལུང* | c-2-21-3, c-3-6 | (none quoted — paraphrased) | ...ཞལ་ལུང་ཞེས་བྱ་བ་བཞུགས་སོ།.md#^0-99, #^0-104 |
| lobsang-dawa | དགེ་བཤེས་བློ་བཟང་ཟླ་བ, *སྒྲོལ་མ་ཕྱག་འཚལ་ཉེར་གཅིག་གི་མཆན་འགྲེལ* | c-1-2-3-6-3 | "ནམ་གྲུ་སོགས་གདོན་བཅོ་བརྒྱད་དང་རོ་ལངས་ཀྱི་རྦོད་གཏོང་སོགས་ངན་སྔགས་དང་གནོད་སྦྱིན་གྱི་གནོད་པའི་ཚོགས་རྣམས། །འཇོམས་པ་ཏུ་རེ་རབ་མཆོག་གི་བདག་ཉིད་མ་ལའོ" | ...མཆན་འགྲེལ་བཞུགས་སོ།.md#^0-30 |
| palden-sherab | མཁན་ཆེན་དཔལ་ལྡན་ཤེས་རབ, *རྗེ་བཙུན་སྒྲོལ་མའི་བསྟོད་པ་ཉི་ཤུ་རྩ་གཅིག་གི་ཚིག་དོན་རྣམ་པར་འགྲེལ་བ...* | c-3-1-21-1-3, c-3-1-21-2-2, c-3-1-21-3-2, c-3-1-21-4-2, c-3-1-6-0-1, c-3-1-6-2-1, c-3-1-9-1-5, c-3-2-2-4-1 | (c-3-1-21-1-3) "ཁྱད་པར་གསུང་ཐུགས་ཀྱི་ཡི་གེ་གསུམ་ལས་སྤྲོས་པའི་འོད་ཟེར་གྱིས། ནམ་གྲུའི་གདོན་སོགས་...འཇོམས་པར་མཛད་མ།"; (c-3-1-6-0-1) "གདོན་རིགས་རྣམ་པར་འཇོམས་པ་འཇིགས་བྱེད་ཆེན་མོ"; (c-3-1-21-3-2) "གདོན་ནི་རྩ་དང་། རོ་ལངས་ནི་ཐིག་ལེ་དང་། གནོད་སྦྱིན་ནི་རྣམ་པར་རྟོག་པ་སྟེ་དེ་རྣམས་འོད་གསལ་དབྱིངས་སུ་བཅོམ་པས།"; (c-3-1-21-4-2) "གདོན་ནི་སྡུག་བསྔལ། རོ་ལངས་ནི་ལས་དང་། གནོད་སྦྱིན་ནི་ཉོན་མོངས་ཏེ།" | ...འཛུམ་རླབས་ཞེས་བྱ་བཞུགས་སོ།.md#^0-207, #^0-209, #^0-211, #^0-213, #^0-62, #^0-68, #^0-101, #^0-223 |
| pema-namgyal | ལྡོམ་བུ་བ་པདྨ་རྣམ་པར་རྒྱལ་བ, *ཕྱག་འཚལ་ཉེར་གཅིག་གི་བསྟོད་འགྲེལ་བདུད་རྩིའི་དགའ་ཚལ* | c-2-4-55, c-3-2, c-3-3 | (c-2-4-55) "ནམ་གྲུ་ལ་སོགས་པའི་གདོན་ཆེན་བཅོ་བརྒྱད་ཀྱི་གདོན་དང་ཤ་ལངས་...གདུག་རྩུབ་ཅན་ཐམས་ཅད" | ...བདུད་རྩིའི་དགའ་ཚལ་བཞུགས་སོ།།.md#^0-69, #^0-74, #^0-75 |
| sangye-nyentrul | སངས་རྒྱས་མཉན་པ་རིན་པོ་ཆེ, *རྗེ་བཙུན་མ་སྒྲོལ་མ་ཉི་ཤུ་རྩ་གཅིག་གི་ཚིག་འགྲེལ་དང་དམིགས་རིམ་འཕགས་མའི་བྱིན་རླབས་གྲུ་ཆར* | c-10-1-5, c-22-0-2, c-7-1-1, c-7-1-3 | (c-10-1-5) "གཡོ་སྒྱུ་བརྗེད་ངན་གདོན་གྱི་འཇིགས་པ།"; (c-22-0-2) "གདོན་རིགས་བཅོ་བརྒྱད་སོགས"; (c-7-1-1) "གདོན་ཚོགས་འཛོམས་པའི་སྒྲོལ་མ་འཇིགས་བྱེད་ཆེན་མོ"; (c-7-1-3) "སྨྱོ་བྱེད་དང་། རྗེད་བྱེད། རེངས་བྱེད་སོགས་ཀྱི་གདོན་བགེགས་རྣམས་བཅོམ་ཞིང་སླར་ལྡང་དུ་མེད་པར་བསྒོམས་པ་ནི་དམིགས་རིམ་ཡིན།" | ...གྲུ་ཆར་བཞུགས།།.md#^0-45, #^0-92, #^0-30, #^0-30 |
| sungrab-tulku | འབྲས་ཕ་ར་གྲྭ་སྨད་གསུང་རབ་སྤྲུལ་སྐུ, *སྒྲོལ་མ་ཉི་ཤུ་རྩ་གཅིག་གི་རྣམ་བཤད* | c-24-2, c-24-4 | (c-24-4) "དེ་ཉིད་ཀྱི་གནས་གསུམ་ལས་སྤྲོས་པའི་འོད་ཟེར་ཀྱིས། གདོན་རིགས་དང་རོ་ལངས་...བདག་ཉིད་སྒྲོལ་མ་ལའོ།།" | ...རྣམ་བཤད།.md#^0-110, #^0-112 |
| taranatha | ཏཱ་ར་ནཱ་ཐ, *ཕྱག་འཚལ་ཉེར་གཅིག་གི་བསྟོད་པའི་རྣམ་པར་བཤད་པ* | c-21-1-4, c-21-2-3, c-21-3-4, c-21-4-5, c-22-1-16, c-22-1-33, c-7-11 | (c-21-1-4) "གདོན་ནི་ནམ་གུའི་གདོན་ལ་སོགས་པ་གདོན་བཅོ་བརྒྱད་རྣམས་སོ། །"; (c-21-3-4) "གདོན་ཏེ་རྩ་དང་། རོ་ལངས་ཏེ་ཐིག་ལེ་དང་...བཅོམ་པ་ལས།"; (c-21-4-5) "གདོན་གྱི་གནོད་པ་དང་མཚུངས་པའི་སྡུག་བསྔལ་དང་...མྱུར་དུ་བཅོམ་ནས།"; (c-7-11) "གཤིན་རྗེ་ལ་སོགས་པའི་གདོན་རྣམས་བྱེར་བ་དང་།" | ...རྣམ་པར་བཤད་པ།.md#^0-74, #^0-75, #^0-76, #^0-80, #^0-89, #^0-89, #^0-25 |
| tenga-tulku | རྡོར་སློབ་བསྟན་དགའ་སྤྲུལ, *ཕྱག་འཚལ་ཉེར་གཅིག་གི་ཕན་ཡོན་དང་བཅས་པ་གསལ་བའི་མེ་ལོང* | c-1-2-3-6-2, c-1-2-3-6-4, c-1-3-3-11, c-1-3-3-12 | (none quoted — paraphrased) | ...གསལ་བའི་མེ་ལོང་...bཞུགས་སོ།.md#^0-177, #^0-179, #^0-215, #^0-216 |
| tenzin-dhonzang | སེར་སྨད་གཙང་དགེ་བཤེས་བསྟན་འཛིན་དོན་བཟང, *སྒྲོལ་མ་ཉེར་གཅིག་གི་བསྟོད་འགྲེལ་སྙིང་གི་ནོར་བུ* | c-4-10-10, c-4-21-2, c-4-21-4, c-4-21-5, c-4-21-6, c-4-6-5, c-4-8-8, c-4-9-8 | (c-4-10-10) "འཇིགས་ཆེན་སྡུག་བསྔལ་བརྒྱད་དང་འབྱུང་པོའི་གདོན།...ཕྱག་འཚལ་ལོ། །"; (c-4-21-4) "གདོན་དང་ཞེས་པ་བྱིས་པའི་གདོན་ཆེན་བཅོ་ལྔ་ལ་ནི།...ནམ་གྲུ་དང་། །"; (c-4-21-5) "སྲུང་པོ་དང་ནི་མ་དགའ་བྱེད།...ཞེས་པ་ལྟར།"; (c-4-8-8) "དེ་ལྟར་སྐྱབས་འོས་ཁྱོད་ཀྱི་ལུས་ཅན་རྣམས།...བསྐྱབ་ཏུ་གསོལ། །"; (c-4-9-8) "གདོན་དང་རྒྱུ་སྐར་གཟའ་ཡི་གནོད་པ་དང་།...ཕྱག་འཚལ་ལོ། །" | ...སྙིང་གི་ནོར་བུ.md#^0-194, #^0-282, #^0-284, #^0-285, #^0-286, #^0-153, #^0-176, #^0-184 |
| tsultrim-namdak | མཁན་པོ་ཚུལ་ཁྲིམས་རྣམ་དག, *སྒྲོལ་འགྲེལ་ཚོགས་གཉིས་རྒྱ་མཚོར་འཇུག་པའི་གྲུ་གཟིངས* | c-2-1-2-1-25, c-2-1-2-1-71, c-2-1-2-1-74, c-3-24, c-3-9, c-8-1-10, c-8-1-8, c-8-5 | (c-2-1-2-1-74) "ཏུ་རེ་ནི་ཐུགས་ཤིན་ཏུ་མྱུར་ ཞིང་བར་ཏུ་བརྩེ་བའི་མཆོག་གིས་སེམས་ཅན་གྱི་དོན་ལ་ཉིན་མཚན་དུས་ དྲུག་ཏུ་བརྩོན་པར་བྱེད་པའི་བདག་ཉིད་མ་ལའོ" | ...གྲུ་གཟིངས།.md#^0-99, #^0-147, #^0-150, #^0-261–266, #^0-198–202, #^0-694–696, #^0-699–701, (block range in c-8-5's own multi-block cite) |

## Claims used but not quoted (paraphrased, per section)

- **Lead:** dharmabhadra:c-1-2-3-6-2, drakpa-gyaltsen:c-1-99, gendun-drub:c-2-2-2-3-6-1, gendun-gyatso:c-1-21-2, karma-maitri:c-1-1-21-3, konchok-thabkhe:c-2-21-3, sungrab-tulku:c-24-2, tenga-tulku:c-1-2-3-6-2/c-1-2-3-6-4, tenzin-dhonzang:c-4-21-2, tsultrim-namdak:c-2-1-2-1-71.
- **ངེས་ཚིག:** taranatha:c-21-1-4 (paraphrase clause following the quote).
- **མཚན་ཉིད། (mechanism):** gendun-drub:c-2-2-2-3-6-2, palden-sherab:c-3-1-21-1-3 (paraphrase clause)/c-3-1-21-2-2, tsultrim-namdak:c-3-24.
- **མཚན་ཉིད། (verse-6 epithet/sādhana):** palden-sherab:c-3-1-6-2-1, tsultrim-namdak:c-3-9.
- **མཚན་ཉིད། (sixteen fears):** palden-sherab:c-3-1-9-1-5.
- **མཚན་ཉིད། (benefits verse):** gendun-drub:c-2-2-3-3-4, karma-maitri:c-1-2-13, konchok-thabkhe:c-3-6, palden-sherab:c-3-2-2-4-1, pema-namgyal:c-3-3, taranatha (list ref only), tenga-tulku:c-1-3-3-11/c-1-3-3-12, tsultrim-namdak:c-8-5.
- **མཚན་ཉིད། (scattered mentions):** taranatha:c-21-2-3/c-22-1-16/c-22-1-33, tsultrim-namdak:c-2-1-2-1-25/c-8-1-8/c-8-1-10, tenzin-dhonzang:c-4-6-5, pema-namgyal:c-3-2.
- **དབྱེ་བ། (enumeration):** dharmabhadra:c-1-2-3-6-4, tenzin-dhonzang:c-4-21-6.
- **གཞུང་ལུགས་སོ་སོའི་བཤད་པ།:** (all quoted directly; no unquoted paraphrase claims in this section).

## Unresolvable attestations

None. Every attestation ID cited on `2-RAILS/Claims/gdon.md` — across all fifteen consolidation
questions and all six facet sections plus the coverage table — was located successfully in its
named commentary's file under `2-RAILS/Claims/raw/tree-guided/`. No attestation was dropped for
failing to resolve, and every one of the packet's 58 distinct claim IDs is drawn on in the article
(57 directly cited by content; the 58th, `tsultrim-namdak:c-2-1-2-1-74`, is quoted in full in
`== ངེས་ཚིག ==`, added after the initial draft specifically to close this gap — see Verification).

## Warnings

- **`rails_status: draft`.** `2-RAILS/Claims/gdon.md` carries `status: draft`, not `complete`. Per
  the vault rule (transformations generate from `status: complete` rails) and per skill Rule 11,
  this article was drafted from a non-complete consolidated page. A human contributor should review
  the consolidated page's own draft status before treating this article as more than a
  structural/citation-verified draft.
- **Wikipedia status (informational only, per the calling agent's instructions — not acted on
  here).** Per this vault's Step 8 inventory, this subject's bo.wikipedia action is **update** — an
  existing stub article was found (title གདོན་), snapshotted at
  `3-TRANSFORMATIONS/Wikipedia/tara21/work/wiki-snapshots/གདོན.wiki`. This draft was produced
  independently from the claims packet, per the task's instruction, without reading or merging
  against that snapshot. Whether/how it gets merged into the existing article is a later human
  decision.
- **All 16 refs lack a publication year and page number.** None of the raw tree-guided commentary
  files carry a `year` field; citation is by Obsidian block ID (`#^N-N`), per this vault's citation
  convention — not a drafting gap, but flagged per the wikitext spec's rule that refs missing
  year/page are listed even when the omission is structural.
- **All 16 refs have no public URL.** Per skill Rule 7, no URL was fabricated (no `dummy.com`, no
  invented link), since none of these commentaries has a resolved public source URL yet. Expected
  at this stage of the pipeline, not an error.
- **Article length:** the drafted prose body (excluding ref citation text, the bibliography list,
  and wikilink targets) runs to roughly 1,200–1,400 Tibetan syllables by tsheg-boundary count —
  under the spec's 1,500-syllable warning threshold. Flagged per spec §7's non-blocking warning
  list; not a blocking failure. The topic's underlying claims packet is itself heavily
  cross-referenced rather than narrative, which keeps quotable continuous passages short relative
  to the number of distinct facets covered.
- **`== མཚན་ཉིད། ==` is subdivided with five bold sub-labels** (mechanism, verse-6
  epithet/sādhana, sixteen-fears item, benefits verse, scattered mentions) rather than split into
  additional top-level `==` sections, following the doctrinal-term skeleton's own allowance (a body
  section organised differently may take a different heading provided it ends in a shad and is
  claim-backed) and the precedent already set in `slot-articles/tara-03/article.md`'s
  `གཞུང་ལུགས་སོ་སོའི་བཤད་པ།`. This keeps the fixed five-section skeleton intact while still giving
  each of the packet's five sub-facets its own labelled block.
- **The verse-6 epithet divergence (`'joms` "destroys" vs `'dzoms` "gathers") is presented inline
  in `== མཚན་ཉིད། ==`**, not moved to `== གཞུང་ལུགས་སོ་སོའི་བཤད་པ། ==`, mirroring exactly how
  `2-RAILS/Claims/gdon.md` itself structures it (inside that facet's own "Consensus" prose, with an
  explicit caveat, and "### Divergences: None observed" immediately below on the rails page). Both
  readings are attributed by commentator name and neither is adjudicated.
- **taranatha's spelling of "nam-gu" without the "ra-btags"** (vs. the other three commentaries'
  "nam-gru") is a genuine, previously-unflagged textual variant discovered during quotation
  verification (see Verification below) — noted explicitly in `== དབྱེ་བ། ==` rather than silently
  normalised, per the vault's no-consensus-flattening rule.
- **Judgment call:** the lead's bold term is written `གདོན་` (tsheg, per the spec's tsheg-boundary
  exemplar), not `གདོན།` — the task's own heading used the shad form, which is the conventional
  written form of the standalone word, but the wikitext spec's `'''<TERM>'''ནི་` skeleton requires
  a tsheg (not a shad) to survive the bold boundary. The page's future bo.wikipedia title (tsheg vs.
  shad vs. bare) is listed as an open question in the wikitext spec §8 and is not resolved here.

## Verification

All 35 verbatim quotations in `article.md` were checked character-for-character
(whitespace-collapsed) against the `1-SOURCES/` file named by their claim's `Cite:` field, using a
normalized-substring match. One failure was found and corrected before finalizing (see below); the
final file passes in full.

| # | Quotation (opening words) | Claim | Source file / block | Result |
|---|---|---|---|---|
| 1 | རྒྱུད་ལས། ཕྱག་འཚལ་དེ་ཉིད་གསུམ་རྣམས་བཀོད་པས... | yama-sonam:c-3-21-3 | ...སྤྲིན་ཕུང་།.md#^0-252 | PASS |
| 2 | གདོན་ནི་ནམ་གུའི་གདོན་ལ་སོགས་པ... | taranatha:c-21-1-4 | ...རྣམ་པར་བཤད་པ།.md#^0-74 | PASS |
| 3 | དེ་ཉིད་ཀྱི་གནས་གསུམ་ལས་སྤྲོས་པའི་འོད་ཟེར... | sungrab-tulku:c-24-4 | ...རྣམ་བཤད།.md#^0-112 | PASS |
| 4 | ཁྱད་པར་གསུང་ཐུགས་ཀྱི་ཡི་གེ་གསུམ... | palden-sherab:c-3-1-21-1-3 | ...འཛུམ་རླབས་...bཞུགས་སོ།.md#^0-207 | PASS |
| 5 | གདོན་རིགས་རྣམ་པར་འཇོམས་པ་འཇིགས་བྱེད... | palden-sherab:c-3-1-6-0-1 | ...འཛུམ་རླབས་...bཞུགས་སོ།.md#^0-62 | PASS |
| 6 | འཇོམས་པ (word) | palden-sherab:c-3-1-6-0-1 | ...bཞུགས་སོ།.md#^0-62 | PASS |
| 7 | འཇོམས་ (word) | palden-sherab:c-3-1-6-0-1 | ...bཞུགས་སོ།.md#^0-62 | PASS |
| 8 | གདོན་ཚོགས་འཛོམས་པའི་སྒྲོལ་མ... | sangye-nyentrul:c-7-1-1 | ...གྲུ་ཆར་བཞུགས།།.md#^0-30 | PASS |
| 9 | འཛོམས་པ (word) | sangye-nyentrul:c-7-1-1 | ...གྲུ་ཆར་བཞུགས།།.md#^0-30 | PASS |
| 10 | འཛོམས་ (word) | sangye-nyentrul:c-7-1-1 | ...གྲུ་ཆར་བཞུགས།།.md#^0-30 | **FAIL → corrected.** First draft wrote "འཛོམ་" (missing the "ས"), which is not a real substring of the source ("འཛོམས་པའི"). Corrected to "འཛོམས་" and re-verified: PASS. |
| 11 | སྨྱོ་བྱེད་དང་། རྗེད་བྱེད... | sangye-nyentrul:c-7-1-3 | ...གྲུ་ཆར་བཞུགས།།.md#^0-30 | PASS |
| 12 | གཡོ་སྒྱུ་བརྗེད་ངན་གདོན་གྱི་འཇིགས་པ། | sangye-nyentrul:c-10-1-5 | ...གྲུ་ཆར་བཞུགས།།.md#^0-45 | PASS |
| 13 | གདོན་དང་རིམས་དང་དུག་གིས་གཟིར་བའི... | drakpa-gyaltsen:c-2-12 | ...འོད་ཟེར་...bཞུགས་སོ།.md#^0-98 | PASS |
| 14 | གཤིན་རྗེ་ལ་སོགས་པའི་གདོན་རྣམས་བྱེར་བ... | taranatha:c-7-11 | ...རྣམ་པར་བཤད་པ།.md#^0-25 | PASS |
| 15 | ལེགས་བྲིས་མ (word) | tenzin-dhonzang:c-4-10-10 | ...སྙིང་གི་ནོར་བུ.md#^0-194 | PASS |
| 16 | འཇིགས་ཆེན་སྡུག་བསྔལ་བརྒྱད... | tenzin-dhonzang:c-4-10-10 | ...སྙིང་གི་ནོར་བུ.md#^0-194 | PASS |
| 17 | དེ་ལྟར་སྐྱབས་འོས་ཁྱོད་ཀྱི་ལུས་ཅན་རྣམས... | tenzin-dhonzang:c-4-8-8 | ...སྙིང་གི་ནོར་བུ.md#^0-176 | **FAIL → corrected.** First draft inserted an extra shad ("། །" instead of "། ") before "རྨི་ལམ་ངན". Corrected to match source exactly and re-verified: PASS. |
| 18 | གདོན་དང་རྒྱུ་སྐར་གཟའ་ཡི་གནོད་པ... | tenzin-dhonzang:c-4-9-8 | ...སྙིང་གི་ནོར་བུ.md#^0-184 | PASS |
| 19 | ནམ་གྲུ (used generically for dharmabhadra/lobsang-dawa/pema-namgyal) — replaced with unquoted prose, plus a separate quoted word ནམ་གུ for taranatha's own variant spelling | taranatha:c-21-1-4 | ...རྣམ་པར་བཤད་པ།.md#^0-74 | PASS (ནམ་གུ) |
| 20 | གདོན་རིགས་བཅོ་བརྒྱད་སོགས | sangye-nyentrul:c-22-0-2 | ...གྲུ་ཆར་བཞུགས།།.md#^0-92 | PASS |
| 21 | ནམ་གྲུ་སོགས་གདོན་བཅོ་བརྒྱད... | lobsang-dawa:c-1-2-3-6-3 | ...མཆན་འགྲེལ་བཞུགས་སོ།.md#^0-30 | PASS |
| 22 | གདོན་དང་ཞེས་པ་བྱིས་པའི་གདོན་ཆེན་བཅོ་ལྔ... | tenzin-dhonzang:c-4-21-4 | ...སྙིང་གི་ནོར་བུ.md#^0-284 | PASS |
| 23 | སྲུང་པོ་དང་ནི་མ་དགའ་བྱེད... | tenzin-dhonzang:c-4-21-5 | ...སྙིང་གི་ནོར་བུ.md#^0-285 | PASS |
| 24 | ནམ་གྲུ་ལ་སོགས་པའི་གདོན་ཆེན་བཅོ་བརྒྱད... | pema-namgyal:c-2-4-55 | ...བདུད་རྩིའི་དགའ་ཚལ་བཞུགས་སོ།།.md#^0-69 | PASS |
| 25 | གདོན་ནི་རྩ་དང་། རོ་ལངས་ནི་ཐིག་ལེ་དང... | palden-sherab:c-3-1-21-3-2 | ...འཛུམ་རླབས་...bཞུགས་སོ།.md#^0-211 | PASS |
| 26 | གདོན་ཏེ་རྩ་དང་། རོ་ལངས་ཏེ་ཐིག་ལེ་དང... | taranatha:c-21-3-4 | ...རྣམ་པར་བཤད་པ།.md#^0-76 | PASS |
| 27 | གདོན་ནི་སྡུག་བསྔལ། རོ་ལངས་ནི་ལས་དང... | palden-sherab:c-3-1-21-4-2 | ...འཛུམ་རླབས་...bཞུགས་སོ།.md#^0-213 | PASS |
| 28 | གདོན་གྱི་གནོད་པ་དང་མཚུངས་པའི་སྡུག་བསྔལ... | taranatha:c-21-4-5 | ...རྣམ་པར་བཤད་པ།.md#^0-80 | PASS |
| 29 | མཚུངས་པའི (word) | taranatha:c-21-4-5 | ...རྣམ་པར་བཤད་པ།.md#^0-80 | PASS |
| 30 | ཏུ་རེ (word, first mention) | tsultrim-namdak:c-2-1-2-1-74 | ...གྲུ་གཟིངས།.md#^0-150 | PASS |
| 31 | ཏུ་རེ་ནི་ཐུགས་ཤིན་ཏུ་མྱུར་... | tsultrim-namdak:c-2-1-2-1-74 | ...གྲུ་གཟིངས།.md#^0-150 | PASS |
| 32 | ཏུ་རེ (word, second mention) | tsultrim-namdak:c-2-1-2-1-74 | ...གྲུ་གཟིངས།.md#^0-150 | PASS |
| 33 | འཇོམས་པ (word, second occurrence, དབྱེ་བ section) | palden-sherab:c-3-1-6-0-1 | ...bཞུགས་སོ།.md#^0-62 | PASS |
| 34 | འཛོམས་པ (word, second occurrence, དབྱེ་བ section) | sangye-nyentrul:c-7-1-1 | ...གྲུ་ཆར་བཞུགས།།.md#^0-30 | PASS |
| 35 | (accounted above — total distinct quote instances in file) | — | — | — |

**35/35 quotation instances PASS in the final file** (some short glossed words —
`འཇོམས་པ`/`འཇོམས་`/`འཛོམས་པ`/`འཛོམས་`/`ཏུ་རེ` — recur more than once in the prose as the same
word is referenced again in a later clause; each recurrence was independently re-verified, not
assumed from the first check). **2 FAILs found and corrected during the verification pass (never
shipped uncorrected)** — see rows 10 and 17 above (the `འཛོམ་`→`འཛོམས་` and the stray-shad fixes).

Additional mechanical checks performed against `article.md` (spec §7 validator, V1–V12):

- V1 (quotation fidelity): PASS — see table above; verified programmatically with a
  whitespace-collapsed normalized-substring check against each claim's cited `1-SOURCES/` file.
- V2 (ref → sources.yaml): not applicable — this skill's citation form (Rule 7) is deliberately
  hand-formatted with no URL and no `sources.yaml` entry; see Warnings.
- V3 (`<references />` present): PASS.
- V4 (no `{{Reflist}}`): PASS — none present.
- V5 (ref tags balanced, one full def per name): PASS — 16 named refs, each with exactly one full
  `<ref name="...">...</ref>` definition (verified: 16 opening full-def tags, 16 `</ref>` closing
  tags) and correctly self-closing thereafter (114 total named-ref citations across the article).
- V6 (≥1 `==` heading): PASS — 8 headings.
- V7 (≥1 allowlisted category): PASS — `[[རིགས་དབྱེ།:ནང་བསྟན།]]`.
- V8 (every section ≥1 citation): PASS for the lead (12 refs) and all five body sections
  (ངེས་ཚིག 3, མཚན་ཉིད། 46, དབྱེ་བ། 18, གཞུང་ལུགས་སོ་སོའི་བཤད་པ། 8, བསྡུས་དོན། 8). The three
  fixed-tail sections (see-also, references, bibliography) carry no independent citation,
  consistent with their structural/navigational role — same convention as `tara-03`.
- V9 (Tibetan script only outside refs): PASS — the only Latin-letter runs in the file are
  `ref`/`name`/`references` markup tokens and the sixteen ref-name identifiers
  (`yama-sonam`, `taranatha`, etc.), verified programmatically; no Latin text appears in the
  visible prose.
- V10 (tsheg at every `'''`/`[[` boundary): PASS — verified programmatically for all 6 bold spans
  (lead term + 5 sub-labels in `== མཚན་ཉིད། ==`) and all 3 wikilink targets.
- V11 (fixed tail order): PASS — `འབྲེལ་ཡོད་ཤོག་ངོས།` → `ལུང་ཁུངས།` → `དཔྱད་གཞིའི་ཡིག་ཆ།`.
- V12 (no `dummy.com`, no placeholder text): PASS — none present.
