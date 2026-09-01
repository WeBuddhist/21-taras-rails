# bo.wikipedia.org — Technical Anatomy of a Well-Formed Article

**Method:** all findings below are from live calls to `https://bo.wikipedia.org/w/api.php` and `https://wikisource.org/w/api.php` on 2026-07-27 (MediaWiki `1.47.0-wmf.12`). Counts come from CirrusSearch `insource:` with **strict regex** (`insource:/.../`) — the quoted form `insource:"..."` is tokenizer-inflated and gave numbers 2–30× too high, so every count here is the regex form.

**Site baseline:** 8,072 articles, 22,734 pages, 161,834 edits, **31 active users**, 2 admins ([siteinfo](https://bo.wikipedia.org/w/api.php?action=query&meta=siteinfo&siprop=statistics&format=json)).

---

## 1. Citation templates: the hypothesis is WRONG — CS1 works fully

The premise that bo.wiki lacks cite templates is **false**. Full Lua CS1 is installed and functional.

| Page | Status | Size |
|---|---|---|
| `དཔེ་པང་།:Cite book` | **EXISTS** | 200 B |
| `དཔེ་པང་།:Cite web` | **EXISTS** | 122 B |
| `དཔེ་པང་།:Cite journal` | **EXISTS** | 126 B |
| `དཔེ་པང་།:Cite encyclopedia` | **EXISTS** | 166 B |
| `དཔེ་པང་།:Reflist` | **EXISTS** | 421 B |
| `Module:Citation/CS1` | **EXISTS** | 164,808 B |
| `Module:Citation/CS1/Configuration` | **EXISTS** | 48,860 B |
| `Module:Citation/CS1/Whitelist` | **EXISTS** | 18,946 B |
| `Module:Citation/CS1/Identifiers` | **EXISTS** | 46,446 B |
| `Module:Citation/CS1/Date validation` | **EXISTS** | 44,395 B |
| `Module:Citation/CS1/COinS` | **EXISTS** | 16,800 B |
| `Module:Citation/CS1/Utilities` | **EXISTS** | 13,878 B |
| `Template:Citation`, `Template:Sfn`, `Template:Harvnb`, `Template:Refbegin`, `Template:Cite wikisource` | **MISSING** | — |

`Template:Cite book` is the standard thin wrapper ([raw](https://bo.wikipedia.org/w/index.php?title=Template:Cite_book&action=raw)):

```wikitext
<includeonly>{{#invoke:citation/CS1|citation
|CitationClass=book
}}</includeonly><noinclude>
{{documentation}}
{{collapse top|TemplateData}}
{{Cite book/TemplateData}}
{{collapse bottom}}
</noinclude>
```

**Empirical render test** via `action=parse` on bo.wiki (not assumed — actually executed):

Input `<ref>{{Cite book |last=ཀློང་ཆེན་པ། |title=ཡིད་བཞིན་མཛོད། |publisher=x |year=1990 |pages=12-14 |edition=2 |location=ཟི་ལིང་། |chapter=ལེའུ་གསུམ་པ།}}</ref>` renders as:

```
↑ ཀློང་ཆེན་པ། (1990). "ལེའུ་གསུམ་པ།". ཡིད་བཞིན་མཛོད། (2 ed.). ཟི་ལིང་།: x. pp. 12–14.
```

Two things to note:

- **Ref markers auto-localize to Tibetan numerals.** The footnote marker renders as `༡` (U+0F21), not `1`: `<sup class="reference"><a href="#cite_note-1">[༡]</a></sup>`. This is free — no configuration needed.
- **CS1 furniture is NOT localized — it emits English.** `pp.`, `ed.`, `Retrieved`, `Archived from the original on` all render in English inside an otherwise Tibetan article. A `{{Cite web}}` with `access-date` and `archive-url` rendered: `"ཤེས་རབ་སྙིང་པོ།". Wikisource. Archived from the original on 2026-01-01. Retrieved 2026-07-20.`
- **ISBN checksums are validated.** A fake ISBN produced a visible inline error: `Check |isbn= value: checksum (help)`. Never let the generator invent ISBNs.

### The `{{Reflist}}` double-heading trap — highest-value gotcha

`Template:Reflist` on bo.wiki is **not** the enwiki version. It emits its own `== ཡོང་ཁུངས། ==` heading ([raw](https://bo.wikipedia.org/w/index.php?title=Template:Reflist&action=raw)):

```wikitext
== ཡོང་ཁུངས། ==
<div class="references-small" {{#if: {{{colwidth|}}}| style="...column-width:{{{colwidth}}};" | ... }}>
{{#tag:references||group={{{group|}}}}}</div><noinclude>[[Category:སྒྲོམ་གཞི།]]
</noinclude>
```

So the idiomatic enwiki pattern `== References ==\n{{Reflist}}` produces **two stacked headings** on bo.wiki. Either write `{{Reflist}}` bare, or use `== ལུང་ཁུངས། ==` + `<references />` and never touch Reflist. Note the template also silently adds `[[Category:སྒྲོམ་གཞི།]]` — that's inside `<noinclude>`, so it does *not* leak onto articles.

### Orphaned refs degrade gracefully

Tested: `<ref>` with **no** `<references/>` anywhere. MediaWiki auto-appends the footnote list at page bottom with **no error message and no tracking category**. Verified on the live article བྱང་ཆུབ་སེམས། — `cite-error` absent, tracking categories `[]`. So missing `<references/>` is a cosmetic defect (footnotes dangle with no heading), not a hard failure. This matters because it's happening at scale (§5).

---

## 2. Reference-section heading: `ལུང་ཁུངས།` wins, but read the numbers carefully

Strict-regex counts of `==[ ]?HEADING[ ]?==` in ns0:

| Heading | Strict count | What it actually is |
|---|---:|---|
| `ཟིན་ཐོ་འམ་དཔྱད་གཞི།` | **2,790** | Empty bot-stub skeleton — noise, not a model |
| `ལུང་ཁུངས།` | **738** | Real usage; OpenPecha house choice |
| `དཔྱད་གཞིའི་ཡིག་ཆ།` | **614** | Real usage; "reference materials" |
| `དཔྱད་གཞི།` | 35 | |
| `ཟུར་ལྟའི་ཡིག་ཆ།` | 4 | Pecha-Gade's personal variant |
| `ཡོང་ཁུངས།` | **2** literal | …but **554** pages render it via `{{Reflist}}` |
| `མཆན་འགྲེལ།` | 110 (loose) | "annotations" |
| `གཞན་ཡང་གཟིགས།` | **1** | Effectively unattested — do not use |

The 2,790 figure is an artifact: bot-created stubs ship a dead skeleton with all-empty sections. The live article `ཆོས།` (618 bytes, last touched 2017 by `Escarbot`) is the archetype:

```wikitext
[[File:MonWheel.jpg|right|thumb|300px|ཆོས།]]

'''ཆོས་'''


== གསལ་བཤད། ==

== པར་རིས་བར་འཁྱམས། ==
...
== ཟིན་ཐོ་འམ་དཔྱད་གཞི། ==
== དཔྱད་གཞིའི་དཀར་ཆག ==
== ད་དུང་གཟིགས། ==
== ཕྱི་ཕྱོགས་དྲ་མཐུད། ==

[[Category:ནང་པ་སངས་རྒྱས་ཆོས་ལུགས།]]
```

Same story for the "see also"/"external links" headings: `ད་དུང་གཟིགས།` (3,892) and `ཕྱི་ཕྱོགས་དྲ་མཐུད།` (3,851) are inflated by this same skeleton. `ད་དུང་གཟིགས།` is nonetheless the correct, genuinely-attested "see also".

**Recommendation: `== ལུང་ཁུངས། ==` + `<references />`.** It is the most-written real heading sitewide (738) *and* already the dominant OpenPecha choice (121 articles), so it needs no editorial re-litigation.

---

## 3. Actual article anatomy — two competing house styles

### 3a. The good model: `སངས་རྒྱས།` (Pecha-Gade, 10,414 B, updated 2026-03-23)

This is the single best format exemplar in the corpus. [Raw](https://bo.wikipedia.org/w/index.php?title=%E0%BD%A6%E0%BD%84%E0%BD%A6%E0%BC%8B%E0%BD%A2%E0%BE%92%E0%BE%B1%E0%BD%A6%E0%BC%8D&action=raw). Opening:

```wikitext
{{Databox}}

'''སངས་རྒྱས''' (ལེགས་སྦྱར་སྐད་དུ། बुद्ध Buddha) ཞེས་པ་ནི་ནང་པའི་ཆོས་ལུགས་སུ་མ་རིག་པའི་གཉིད་ལས་སད་ཅིང་ཆོས་རྣམས་ཀྱི་གནས་ལུགས་ཇི་བཞིན་རྟོགས་པའི་སྐྱེས་བུ་མཆོག་ལ་གོ་ཞིང་། ... སྟོན་པ་[[ཤཱཀྱ་ཐུབ་པ]]་ལ་འབོད་ཀྱི་ཡོད།

== སྒྲ་བཤད་དང་གོ་དོན། ==
... སློབ་དཔོན་ལེགས་ལྡན་འབྱེད་ཀྱིས། "མ་རིག་གཉིད་ལས་སངས་པ་དང་། །ཤེས་བྱ་ལ་བློ་རྒྱས་ཕྱིར་རོ། །"<ref>སློབ་དཔོན་ལེགས་ལྡན་འབྱེད། 《རྟོག་གེ་འབར་བ།》 (Tarkajvala) སྡེ་དགེ་བསྟན་འགྱུར། དབུ་མ།</ref> ཞེས་དང་།
```

and the tail:

```wikitext
'''ཐེག་པ་ཆེན་པོའི་ལུགས།''' (Mahayana) 
ཐེག་ཆེན་གྱི་མདོ་སྡེ་རྣམས་སུ་ ... 《མངོན་རྟོགས་རྒྱན》ལས། "ཐུབ་པའི་ངོ་བོ་ཉིད་སྐུ་ནི། །ཟག་པ་མེད་པའི་ཆོས་རྣམས་སོ། །"<ref>རྗེ་བཙུན་བྱམས་པ་མགོན་པོ། 《མངོན་རྟོགས་རྒྱན།》 (Abhisamayalankara) ལེའུ་བརྒྱད་པ། ཆོས་སྐུའི་སྐབས།</ref> ཞེས་གསུངས།

== སངས་རྒྱས་ཀྱི་ཡོན་ཏན། ==
...

== འབྲེལ་ཡོད་རྩོམ་ཡིག ==
* [[ཤཱཀྱ་ཐུབ་པ།]]
* [[བྱང་ཆུབ་སེམས་དཔའ།]]
* [[ནང་ཆོས།]]

== ཟུར་ལྟའི་ཡིག་ཆ། ==
<references />
```

Extractable conventions:
- **Lede:** `'''TERM'''` + Sanskrit in Devanagari + IAST/Latin in parens + `ཞེས་པ་ནི་ … ལ་གོ` definitional frame.
- **Citations are plain `<ref>` with hand-formatted Tibetan text** — author `།` *title in* `《…》` + Latin Sanskrit title in parens + edition/collection + chapter locus. **No CS1 templates.**
- **Text titles use CJK corner brackets `《…》`** (U+300A/300B). The other house style uses guillemets `«…»`. Both are attested; `《…》` is the more common in doctrinal articles.
- **Bold as pseudo-subheading** (`'''ཐེག་པ་ཆེན་པོའི་ལུགས།''' (Mahayana)`) for third-level divisions instead of `===`.
- **Quotation of verse keeps the shad-space `། །` line convention** inside straight double quotes.
- Wikilinks written `[[ཤཱཀྱ་ཐུབ་པ]]་ལ` — tsheg outside the brackets.
- **No categories.**

### 3b. The dominant skeleton: numbered Tengyur-commentary template (231 articles)

Example: `ཤེས་རབ་སྙིང་པོའི་རྣམ་བཤད་ཀླུ་སྒྲུབ་ཀྱི་དགོངས་པ་གསལ་བར་བསྟན་པ་`

```wikitext
{{databox}}
༄༅། །«ཤེས་རབ་སྙིང་པོའི་རྣམ་བཤད་ཀླུ་སྒྲུབ་ཀྱི་དགོངས་པ་»ཞེས་བྱ་བའི་གཞུང་འདི་ནི། ... མཛད་པ་ཞིག་ཡིན་ནོ༎

== ༡. མཚན་དོན། ==
== ༢. མཛད་པ་པོ། ==
== ༣. རྒྱབ་ལྗོངས་དང་མཛད་དགོས། ==
== ༤. གཞུང་ཚད་དང་བརྗོད་དོན། ==
=== '''༤.༡ ཀླད་ཀྱི་དོན།''' ===
=== '''༤.༢ གཞུང་གི་དོན།''' ===
=== '''༤.༣ མཇུག་གི་དོན།''' ===
== ༥. ལྟ་གྲུབ་གཙོ་བོ། ==
== ༦. གལ་གནད་དང་ཤུགས་རྐྱེན། ==
== ༧. ཟུར་ལྟའི་ནང་དོན། ==
== ༨. རྩ་འགྲེལ། ==
== ༩. དཔྱད་གཞིའི་ཡིག་ཆ། ==
=== ༡. ནང་ཁུལ་གྱི་དཔྱད་གཞིའི་ཡིག་ཆ། ===
=== ༢. ཕྱི་ཕྱོགས་ཀྱི་དཔྱད་གཞིའི་ཡིག་ཆ། ===

[[Category:ནང་ཆོས།]]
[[Category:བསྟན་བཅོས།]]
[[Category:བོད་གཞུང།]]
[[Category:ཤེར་ཕྱིན།]]
```

Notes: opens with the yig-mgo `༄༅། །`; uses double-shad `༎`; numbers headings with Tibetan digits; wraps `===` headings in redundant `'''`; and — critically — the "references" section holds **bare external links to BDRC** (`[https://library.bdrc.io/…&scope=bdr:UT10736_007_0006&openEtext=bdr:VE10736_007&startChar=195070#open-viewer TITLE] (IE10736)`) rather than `<ref>` footnotes.

### 3c. The negative example: raw LLM dump

`ཚོར་བ།` (1,914 chars, Pecha-Gade, 2025-12-22) is a Gemini response pasted verbatim — **zero wikitext**: no `==`, no `'''`, no `<ref>`, no links, no categories. Pseudo-headings are plain text `༡. ཚོར་བའི་གོ་དོན།`, `༢. ཚོར་བའི་དབྱེ་བ་གསུམ།`. `ལས་འབྲས།` (37,709 B) is the same failure at 20× the size. This is exactly the failure mode the new pipeline must prevent.

---

## 4. Categories

Namespace 14 is localized: **`རིགས་དབྱེ།`** (canonical `Category` also works). Template ns10 is `དཔེ་པང་།`, File ns6 is `ཡིག་ཆ།`.

Buddhist categories are badly fragmented, with near-duplicates and typos:

| Category | Pages |
|---|---:|
| `ནང་བསྟན།` | 95 |
| `ནང་པ་སངས་རྒྱས་ཆོས་ལུགས།` | 87 |
| `ནང་ཆོས།` | 85 |
| `ནང་པ་སངས་རྒྱས།` | 25 |
| `ནང་པ་སངས་རྒྱངས་ཀྱི་ལྷ།` | 36 | ← **typo** (`རྒྱངས` for `རྒྱས`) |
| `ནང་པ་སངས་རྒྱས།།` | 1 | ← **double shad typo** |
| `ཆོས་ལུགས།` | 138 |
| `ནང་པའི་བསྟན་བཅོས།` | 1 |
| `ནང་པའི་མཚན་ཉིད་རིག་པ།` | 1 |

**Every one of `སངས་རྒྱས།`, `སྟོང་པ་ཉིད།`, `བྱང་ཆུབ་སེམས།`, `ཤེས་རབ་སྙིང་པོ།`, `ཕར་ཕྱིན།`, `ལས་འབྲས།` has zero categories.** The category-typo variants mean a generator must select from a **pinned allowlist**, never free-generate a category name.

---

## 5. The OpenPecha corpus — 677 articles, measured

Accounts found via `list=allusers&auprefix=Pecha` — 15 accounts, 13 with edits, plus `Tsampaeater` (126 edits, reg. 2025-03-21):

`Pecha-G.Dhargyal` (860), `Pecha-pema` (606), `Pecha-Tsewang` (569), `Pecha-Alalamo` (422), `Pecha-Gade` (388), `Pecha-Jampa Tennor` (368), `Pecha-Dhondup` (314, reg. 2020), `Pecha-Choedup` (156), `Pecha-yashi 11` (166), `Pecha-lhujam gyal` (113).

I enumerated **all 677 ns0 page-creations** by these accounts and fetched every article's wikitext:

| Property | Count | % |
|---|---:|---:|
| has `<ref>` | 166 / 677 | **25%** |
| has `[[Category:]]` | 133 / 677 | 20% |
| has `<references/>` | 27 / 677 | 4% |
| has `{{Reflist}}` | 13 / 677 | 2% |
| has any `{{Cite*}}` | **4 / 677** | **1%** |
| has `{{Databox}}` | 16 / 677 | 2% |
| has `==` headings | 577 / 677 | 85% |
| **no headings at all (raw dump)** | **100 / 677** | **15%** |

Median article size **17,395 bytes**. At 677 articles against a site total of 8,072, **OpenPecha has authored ~8.4% of the entire Tibetan Wikipedia.**

The gap that matters: **166 articles carry `<ref>` but only ~40 carry a display mechanism** — roughly 126 articles have footnotes rendering headless at page bottom. And the project's stated goal ("a citation for every statement") is currently met by 25% of output.

Top headings across the corpus confirm the two styles coexist: `༡. མཚན་དོན།` (231), `༥. ལྟ་གྲུབ་གཙོ་བོ།` (231), `༦. གལ་གནད་དང་ཤུགས་རྐྱེན།` (230), `༧. ཟུར་ལྟའི་ནང་དོན།` (228), `༩. དཔྱད་གཞིའི་ཡིག་ཆ།` (202), `'''མཛད་པ་པོ།'''` (156), `ལུང་ཁུངས།` (121).

---

## 6. Tibetan wikitext gotchas — tested, not assumed

**The tsheg/bold claim is real, but it is an orthographic issue, not a parser bug.** I rendered five variants through bo.wiki's own parser:

| Wikitext | HTML output |
|---|---|
| `'''བྱང་ཆུབ་སེམས་'''ནི་…` | `<b>བྱང་ཆུབ་སེམས་</b>ནི་…` |
| `'''བྱང་ཆུབ་སེམས'''་ནི་…` | `<b>བྱང་ཆུབ་སེམས</b>་ནི་…` |
| `'''བྱང་ཆུབ་སེམས'''ནི་…` | `<b>བྱང་ཆུབ་སེམས</b>ནི་…` |
| `'''བྱང་ཆུབ་སེམས།''' ཐེག…` | `<b>བྱང་ཆུབ་སེམས།</b> ཐེག…` |
| `'''བྱང་ཆུབ་སེམས'''། ཐེག…` | `<b>བྱང་ཆུབ་སེམས</b>། ཐེག…` |

The parser is completely neutral — `'''` never interacts with `་` (U+0F0B) or `།` (U+0F0D). **The danger is variant 3**: the tsheg is *gone*. U+0F0B is the mandatory syllable separator, so `སེམས` + `ནི` fused without it is a **Tibetan spelling error**, and because U+0F0B carries Unicode line-break class `BA` (break-after), removing it also destroys the only line-wrap opportunity, producing an unbreakable run. An LLM asked to "bold the term" will naturally emit variant 3. Variants 1 and 2 are both correct and both attested in the live corpus (`'''སྟོང་པ་ཉིད་'''` in སྟོང་པ་ཉིད།; `'''བྱང་ཆུབ་སེམས'''་ནི་` in བྱང་ཆུབ་སེམས།). So: **the rule is "a tsheg must survive at the bold boundary", not "a tsheg must be outside the bold".**

**Section anchors keep the shad and the Tibetan digits.** Tested:

| Wikitext heading | `anchor` |
|---|---|
| `== མཚན་ཉིད། ==` | `མཚན་ཉིད།` |
| `== ༡. མཚན་དོན། ==` | `༡._མཚན་དོན།` |
| `=== '''༤.༡ ཀླད་ཀྱི་དོན།''' ===` | `༤.༡_ཀླད་ཀྱི་དོན།` (bold stripped) |

HTML is `<h2 id="མཚན་ཉིད།">` plus a legacy dot-encoded `<span id=".E0.BD.98.E0.BD.9A…">`. Spaces → `_`. **The shad `།` is part of the anchor**, so any deep link or section-targeted edit must include it. Note the `sections` API returns `line` **with** bold markup but `anchor` **without** — use `anchor` for links, and the integer `index` for `action=edit&section=N`.

---

## 7. Wikisource — real, citable, and the interwiki prefix is a trap

There is **no separate `bo.wikisource.org` wiki**; it 302-redirects to the multilingual `wikisource.org` (**title preserved** on deep links — I verified a deep link returns 302 → `wikisource.org/wiki/<same title>` → HTTP 200). Multilingual Wikisource holds 65,648 articles.

Tibetan Kangyur material is present and organized **by xylograph edition**, as subpages. Searching `ཤེས་རབ་སྙིང་པོ` returns 713 hits including `ཤེས་རབ་སྙིང་པོ། སྡེ་དགེ།/1`, `…/2`, `…/3` (Derge), `ཤེས་རབ་སྙིང་པོ། པེ་ཅིང་།` (Peking), `ཤེས་རབ་སྙིང་པོ། ཅོ་ནེ།` (Cone), `ཤེས་རབ་སྙིང་པོ། ལི་ཐང་།/མདོའི་གླེང་གཞི།` (Lithang, sectioned).

These are **ProofreadPage transclusions from scanned originals** — i.e. genuinely citable:

```wikitext
{{header
| title={{xx-larger|[[../ |ཤེས་རབ་སྙིང་པོ། སྡེ་དགེ།]]}}
| year= c. 1733
| previous=
| next=[[../2|རྗེས་མ།]]
| author=སངས་རྒྱས་བཅོམ་ལྡན་འདས།
| translator1=རྒྱ་གར་གྱི་མཁན་པོ་བི་མ་ལ་མི་ཏྲ།
| translator2=ལོཙྪ་བ་དགེ་སློང་རིན་ཆེན་སྡེ།
}}

<div style="margin-left: 3em; margin-right: 3em; text-align: justify;">
<pages index="ཤེས་རབ་སྙིང་པོ། སྡེ་དགེ།.pdf" include=1 onlysection="part1" />
</div>
...
[[Category:Ser ཤེར་ཕྱིན།]]
```

**Interwiki prefix test from bo.wiki** — this is a live trap:

| Wikitext | Resolves to | Verdict |
|---|---|---|
| `[[s:ཤེས་རབ་སྙིང་པོ། སྡེ་དགེ།/1]]` | `bo.wikisource.org/wiki/…` → 302 → `wikisource.org` | **works** (one redirect hop) |
| `[[wikisource:ཤེས་རབ་སྙིང་པོ། སྡེ་དགེ།/1]]` | **`en.wikisource.org`** | **BROKEN — wrong wiki** |
| `[[oldwikisource:ཤེས་རབ་སྙིང་པོ། སྡེ་དགེ།/1]]` | `wikisource.org/wiki/…` | **correct, direct** |

`Template:Cite wikisource` does **not** exist on bo.wiki, so Wikisource citations must be `<ref>[[oldwikisource:…|…]]</ref>` or a bare URL.

---

## 8. Write-path constraints

`writeapi=true`, `maxarticlesize=2,097,152` bytes, `case=first-letter`, article path `/wiki/$1`. Installed extensions include **`Abuse Filter`, `WikimediaAntiAbuse`, `FancyCaptcha`, `hCaptcha`**, plus `Cite`, `Scribunto`, `TemplateData`, `WikibaseClient`, `ContentTranslation`.

The existing bot group (`Alexbot`, `Escarbot`, `TXiKiBoT`, `AvicBot`, `BodhisattvaBot`…) is entirely legacy interwiki bots from the 2010s — **there is no active local bot-approval process**, and only 2 admins. Mass automated article creation without prior community notice is a real social risk on a wiki with 31 active users.

**Wikidata linkage is missing on new work.** `སངས་རྒྱས།`→`Q7055` and `བྱང་ཆུབ་སེམས།`→`Q838339` are linked, `སྟོང་པ་ཉིད།`→`Q546054`, but `ཚོར་བ།` and `ཕར་ཕྱིན།` have **no Wikidata item at all**, and only `སངས་རྒྱས།` has langlinks. Modern interwiki links live in Wikidata, not in wikitext — `[[en:…]]` in the article body is obsolete.

`{{Databox}}` is a Wikidata-driven infobox (`{{#invoke:Databox|databox|...}}`, `Module:Databox` exists). Its `<templatestyles src="Tɛmplet:Databox/styles.css" />` points at a **non-existent page** (leftover from another wiki), but it still renders — 4,104 bytes of HTML, no error class, styling inlined. Only useful when the article has a Wikidata item; on an item-less page it produces an empty box.

---

## Implementation implications

- **Emit CS1 templates — the "no cite templates" premise is false.** `{{Cite book}}`, `{{Cite web}}`, `{{Cite journal}}`, `{{Cite encyclopedia}}` all work via a complete 164 KB `Module:Citation/CS1`. Do *not* build a plain-`<ref>` fallback on the assumption they're missing.
- **But default to hand-formatted `<ref>` for Kangyur/Tengyur primary sources anyway**, because CS1 emits English furniture (`pp.`, `ed.`, `Retrieved`) inside Tibetan prose, and canonical Tibetan citation practice (`author། 《title།》 (Skt) སྡེ་དགེ་བསྟན་འགྱུར། section`) has no CS1 parameter mapping. Reserve `{{Cite book}}`/`{{Cite web}}` for modern secondary sources with real ISBNs/URLs. Make this a per-source-type switch in the citation formatter, not a global mode.
- **Never emit `== ལུང་ཁུངས། ==` immediately followed by `{{Reflist}}`.** bo.wiki's Reflist injects its own `== ཡོང་ཁུངས། ==`. Pin the pipeline to `== ལུང་ཁུངས། ==` + `<references />` and add a lint rule that rejects any `{{Reflist}}` preceded by a heading.
- **Standardize the reference heading as `ལུང་ཁུངས།`** (738 sitewide, 121 in-corpus). Ignore the 2,790 `ཟིན་ཐོ་འམ་དཔྱད་གཞི།` count — it is dead bot-stub skeleton. Never emit `གཞན་ཡང་གཟིགས།` (1 attestation); use `ད་དུང་གཟིགས།` for "see also".
- **Ship a post-generation wikitext validator as a hard gate, not a nicety.** The corpus proves the failure modes empirically: 15% of 677 articles are raw LLM dumps with zero markup, 75% have no citations, 80% have no categories, and ~126 articles have orphaned `<ref>` with no references section. Minimum blocking checks: has ≥1 `==` heading; every `<ref>` balanced and closed; `<references />` present iff `<ref>` present; ≥1 category from the allowlist; no bare `༡.`-style pseudo-headings in body text.
- **Add a tsheg-boundary lint on every bold/link/heading boundary.** The rule is *"a `་` (U+0F0B) must survive at the boundary"* — `'''X་'''Y` and `'''X'''་Y` are both fine; `'''X'''Y` is a spelling error and kills line-wrapping. Same check applies at `[[…]]` boundaries. This is not a parser bug (verified: bo.wiki's parser treats all variants identically), so it will never surface as a wiki error — only the linter can catch it.
- **Pin categories to a curated allowlist; never let Gemini generate a category name.** The namespace is `རིགས་དབྱེ།`, and live categories include misspellings (`ནང་པ་སངས་རྒྱངས་ཀྱི་ལྷ།`) and shad typos (`ནང་པ་སངས་རྒྱས།།`). Seed the allowlist from `ནང་ཆོས།`, `ནང་བསྟན།`, `ནང་པ་སངས་རྒྱས་ཆོས་ལུགས།`, `བསྟན་བཅོས།`, `ཤེར་ཕྱིན།`, `ཆོས་ལུགས།`.
- **Adopt `སངས་རྒྱས།` (Pecha-Gade, 2026-03) as the few-shot format exemplar, not the numbered Tengyur skeleton.** The `༡. མཚན་དོན།` skeleton (231 articles) is a *text-description* template for commentary works and carries bare BDRC external links instead of footnotes — wrong shape for a doctrinal-term encyclopedia article. Keep the two templates as separate prompt profiles keyed on entity type (term vs. work).
- **Use `oldwikisource:` for all Wikisource links.** `[[wikisource:…]]` silently resolves to **en**.wikisource. `[[s:…]]` works but takes a redirect hop. `Template:Cite wikisource` does not exist on bo.wiki, so wrap manually: `<ref>[[oldwikisource:ཤེས་རབ་སྙིང་པོ། སྡེ་དགེ།/1|…]]</ref>`.
- **Wikisource is a usable primary-source citation target for the root-text layer** — Kangyur editions are there as ProofreadPage scans, addressed as `TITLE EDITION།/N` (སྡེ་དགེ /པེ་ཅིང་/ཅོ་ནེ/ལི་ཐང་). Build an edition-aware resolver so a Derge citation links the Derge page. Fall back to BDRC `bdr:` IDs (already the in-corpus convention) where Wikisource lacks the text.
- **For the UPDATE path, target sections by `anchor`/`index` from `action=parse&prop=sections`, never by string-matching headings.** Anchors retain the shad and Tibetan digits (`༡._མཚན་དོན།`); `line` includes bold markup while `anchor` strips it. Prefer appending to `ལུང་ཁུངས།` + inserting inline `<ref>` over whole-page rewrites, to keep diffs reviewable.
- **Budget for anti-abuse and social review before any bulk run.** AbuseFilter, FancyCaptcha, and hCaptcha are live; the site has 31 active users and 2 admins, and no modern bot-approval process. Plan for an authenticated bot account with a bot flag request, conservative rate limiting, `maxlag`, and a human-in-the-loop approval queue — the pipeline is "semi-automatic" by necessity, not just by design preference.
- **Create/link a Wikidata item as a pipeline step.** `ཚོར་བ།` and `ཕར་ཕྱིན།` have no item, so they get no interwiki links and `{{Databox}}` renders empty. Do not emit `[[en:…]]` wikitext interwikis — they are obsolete.
- **Never let the model invent ISBNs.** CS1 validates checksums and renders a visible red inline error (`Check |isbn= value: checksum`) plus a maintenance category. Omit the parameter when the value isn't verified.