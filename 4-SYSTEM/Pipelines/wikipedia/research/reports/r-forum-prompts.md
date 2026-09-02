# OpenPecha Forum Harvest — Wiki Working Group (Category 35)

## 0. Access: what worked, what didn't

| Method | Result |
|---|---|
| **`https://forum.openpecha.org/raw/<topic_id>`** | ✅ **Best.** Public, no auth, returns **raw Markdown source** of every post concatenated, with `author \| timestamp \| #post_num` headers. This is the only endpoint that returns the *un-rendered* prompt text inside code fences. Used for all extractions below. |
| `https://forum.openpecha.org/c/wg/wiki-wg/35.json` | ✅ Works, public. Returns `topic_list.topics[]`. **Paginated at 30** — must add `?page=1` to get the 31st topic (id 206). |
| `https://forum.openpecha.org/t/<slug>/<id>.json` | ✅ Works, public — but posts come back as `cooked` (rendered HTML), **no `raw` key**. Fine for metadata (title/slug/created_at/views), worse for prompt fidelity. |
| Wrong slug + correct id, e.g. `/t/prompt-sample/324.json` | ⚠️ Returns **HTTP 301** → `/t/new-prompt-sample/324.json`. `curl` needs `-L`; WebFetch follows automatically. Note the task-supplied URL `t/prompt-sample/324` is a **stale slug** — the topic was renamed to `new-prompt-sample`. |
| HTML pages | Not needed; no login wall encountered. |

Nothing failed. No Google-cache fallback was required.

---

## 1. Complete topic enumeration — category `wg/wiki-wg/35` (31 topics)

| id | Title | Created | Posts |
|---|---|---|---|
| 284 | ℹ️ Homepage གཙོ་ངོས། | 2025-06-05 | 1 |
| 478 | PRD of Buddhist Knowledge WG | 2025-09-24 | 1 |
| 475 | How to Add Statements of Support/Opposition to a Discussion in Wikimedia | 2025-09-22 | 1 |
| 432 | OpenRefine for WikiMedia | 2025-08-20 | 1 |
| 425 | ཝི་ཀི་མི་ཌི་ཡ་ཁོ་མོན་སི་(Wikimedia Commons)ནང་ནོར་འཁྲུལ་གྱིས་བཞག་པའི་པར་རྣམས་བརྗེ་སྒྱུར་བྱེད་ཚུལ། | 2025-08-12 | 1 |
| 420 | བོད་སྐད་ཝེ་ཁེ་རིག་མཛོད་ཀྱི་བཀོད་འདོམས་པར་རེ་ཞུའི་རྒྱབ་སྐྱོར་བྱེད་ཕྱོགས་ཀྱི་ལམ་སྟོན། | 2025-08-01 | 1 |
| 418 | How to Nominate someone for Adminship in bo.wikipedia… | 2025-07-31 | 2 |
| 408 | Buddhist Knowledge from Tibetan Sources Project Page for Wikipedia | 2025-07-22 | 1 |
| 382 | Test minutes 2 | 2025-07-14 | 1 |
| 381 | Test Minutes | 2025-07-14 | 1 |
| 345 | How to Change the page name/title in Wikisource using the 'Move Tool' | 2025-07-08 | 1 |
| 343 | 📄 Buddhism on Wikipedia PRD | 2025-07-08 | 1 |
| 329 | Buddhism on Wikimedia WG | 2025-06-30 | 1 |
| **324** | **New Prompt Sample** | 2025-06-24 | 3 |
| **319** | **ཝེ་ཁེ་ལམ་སྟོན་ཡིག་ཆ། ལུང་འདྲེན། Citing Sources** | 2025-06-22 | 1 |
| **309** | **ཝེ་ཁེ་ཤོག་ངོས་གསར་བཟོའི་བརྡ་སྟོན་དང་། ལུང་འདྲེན་བྱེད་སྟངས།…** | 2025-06-15 | 1 |
| 303 | Pecha Apps WG | 2025-06-12 | 1 |
| 299 | Pecha AI Studio WG | 2025-06-12 | 1 |
| **295** | **2.2 གཞུང་སྤྱིའི་ཝེ་ཁེ་ཤོག་ངོ་བཟོ་བྱེད་ཀྱི་བརྡ་སྟོན།** | 2025-06-09 | 1 |
| 294 | Speech to Text Working Group | 2025-06-09 | 1 |
| **289** | **1.2 རྩ་འགྲེལ་མཉམ་སྦྱར་ལས་ཚིག་གནད་ཟུར་འདོན་གྱི་རིག་ནུས་བརྡ་སྟོན།** | 2025-06-06 | 1 |
| 262 | ཤེས་རབ་སྙིང་པོའི་ཐ་སྙད་གཅིག་གཞིར་བཞག་གིས་བརྡ་སྟོན་སྒྲིག་བཀོད། | 2025-05-26 | 3 (empty/spam) |
| **260** | **3.04 ཝེ་ཁེ་ཤོག་ངོ་བཟོ་བྱེད་ཀྱི་བརྡ་སྟོན།** | 2025-05-26 | 1 |
| 239 | ཝེ་ཁེ་རྩོམ་སྒྲིག་པའི་རྩ་འཛིན། | 2025-05-16 | 1 |
| 237 | 2.2 ཝེ་ཁེ་ཤོག་ངོས་བཟོ་དགོས་མིན་གྱི་ས་མཚམས་དབྱེ་ཚུལ། | 2025-05-16 | 1 (**stub, junk content**) |
| **236** | **2.1 ai རིག་ནུས་ལ་བརྟེན་ནས་རྩ་འགྲེལ་མཉམ་སྦྱོར་བྱེད་ཐབས།** | 2025-05-16 | 1 |
| 231 | How to Change Your Username on Wikipedia | 2025-05-13 | 4 |
| **223** | **Semi-automated Wikipedia Article Creation** | 2025-05-09 | 1 |
| 218 | Wikimedia projects | 2025-05-07 | 1 |
| 206 | Representing root texts and commentaries on Wikidata | 2025-04-09 | 4 |
| 71 | འབོད་རྟགས་དང་འབྲེལ་བའི་གནད་དོན་བགྲོ་གླེང་། | 2024-10-30 | 1 |

Bolded = contains prompts/guidelines/templates. Topics 237 and 262 are **empty placeholders** (237 reads only `1. སདངཇ / 2. 2.་དང`; 262 reads `55555\`Preformatted text\``) — do not treat their section numbers as real specs.

---

## 2. Topic 223 — the master pipeline spec (the repo's spine)

**Title:** Semi-automatic workflow to create Wikipedia articles in Tibetan · **Author:** Trinley · **Date:** 2025-05-09 (last edited 2025-08-12)
URL: https://forum.openpecha.org/t/semi-automated-wikipedia-article-creation/223

This is the canonical 4-stage decomposition, verbatim. Legend: 👨‍💻 = code/automated, ✨ = AI, 😓 = manual/human.

```
1. Selection of key terms/concepts in the Kangyur and Tengyur
* List texts in the Kangyur and Tengyur that have commentaries 😓
* Select key terms from the root texts by analysing word frequency and keyness 👨‍💻

2. Find authoritative explanatory material from commentaries
* Link root texts and commentaries at segment/verse level (google docs or pecha editor) ✨😓
* Design prompt to extract explanatory material ✨😓
* Extract explanatory material for each key term from all linked commentaries 👨‍💻✨
* QC extraction and improve prompts ✨😓

3. Draft new authoritative articles for each key term
* Design prompt to organize explanatory material ✨😓
* Organize the explanatory material into sections 👨‍💻✨
* QC section organization and improve prompts ✨😓
* Design prompt to draft articles ✨😓
* Draft article with a citation/source for each sentence/statement 👨‍💻✨
* QC articles and improve prompts ✨😓

4. Update existing articles with explanatory material from a new text
* Organize the explanatory material into sections (same as 3.)
* Design prompt to compare and update previous article ✨😓
* Compare content with previous article 👨‍💻✨
* For duplicate content, add new citation sources 👨‍💻✨
* For new information, add new content with citations 👨‍💻✨
* QC articles and improve prompts ✨😓
```

The Tibetan mirror (`བཀའ་བསྟན་རིག་མཛོད་ཀྱི་ལས་འཆར།`) numbers these 1.1–1.2, 2.1–2.4, 3.1–3.6, 4.1–4.6, plus a section 5 of editorial guidelines, and **hyperlinks each numbered step to its own forum topic** — this is the authoritative step→topic mapping:

- **1.2** → t/1-2/**289** (key-term selection)
- **2.1** → t/2-1-ai/**236** (root–commentary verse alignment)
- **3.4** → t/3-04/**260** (article-writing prompt)
- **5.1** → t/topic/**309** (citation markup)
- **5.2** → t/citing-sources/**319** (citing-sources guideline)
- **5.3** → t/prompt-sample/**324**
- **5.4** → t/…move-tool/**345**, **5.5** → **418**, **5.6** → **425**

Note steps **2.2 (extraction prompt), 3.1 (organize prompt), and 4.2 (compare/update prompt) have NO forum topic** — they are unwritten. Step 4 in particular (the UPDATE path) has zero published prompt.

---

## 3. Topic 289 — key-term extraction prompts (three iterations)

**Title:** 1.2 རྩ་འགྲེལ་མཉམ་སྦྱར་ལས་ཚིག་གནད་ཟུར་འདོན་གྱི་རིག་ནུས་བརྡ་སྟོན། · **Author:** `gade` · **Date:** 2025-06-06 (edited 2025-07-29)
URL: https://forum.openpecha.org/t/1-2/289

Author's own meta-notes: all three were **built and tested on Claude AI only** (`བརྡ་སྟོན་འདི་ནི་་Claude ai ཁོ་ནའི་ནང་ཚོད་བལྟ་བྱས་ནས་བཟོས་པ་ཞིག་ཡིན་པས། འདིས་མིས་བཟོས་རིག་ནུས་གཞན་གྱི་ནང་བཀོལ་སྤྱོད་ཀྱི་ནུས་པ་ཇི་བཞིན་ཐོན་དཀའ།` — "since this prompt was built and tested inside Claude AI only, it is hard to get equivalent performance in other AIs"). Known weakness: it over-returns, emitting fragments of phrases rather than clean single terms.

### 3a. Version 1 (verbatim)

```
1. རྩ་བ་དང་འགྲེལ་བ་གཉིས་ཀའི་ནང་ཡོད་པའི་གནད་ཚིག་(keywords)ཟུར་འདོན་བྱེད་དགོས།
2. འགྲེལ་པ་ལ་ཡོད་པ་དང་རྩ་བ་ལ་མེད་པ་ཡིན་ན་མི་འགྲིག
3. རྩ་བ་ལ་ཡོད་ལ་འགྲེལ་པ་ལ་མེད་ན་མི་འགྲིག
4. ངེས་པར་དུ་རྩ་འགྲེལ་གཉིས་ཀ་ལ་ཡོད་པའི་གནད་ཚིག་དགོས།
5. རྩ་བ་དང་འགྲེལ་བ་སོ་སོའི་ནང་ཇི་ལྟར་ཡོད་ཚུལ་བསྟན་དགོས།
6. གནད་ཚིག་རྐྱང་པ་ལས་དོན་འདྲ་བ་འདིར་ཟུར་འདོན་བྱེད་མི་དགོས།
7. ཐ་སྙད་རྐྱང་པ་ལས་བརྗོད་པ་ལྟ་བུ་འདིར་མི་དགོས།
8. ངས་ཕུལ་བའི་འགྲེལ་པ་དང་རྩ་བ་འདིའི་ནང་ཡོད་པ་ལས་གཞན་འདིར་མི་དགོས།
9. དོན་འདྲ་བ་དང་རིགས་འདྲ་བ་སོགས་སྡེ་ཚན་སོ་སོ་ནས་ཟུར་འདོན་བྱས་ཀྱང་ཆོག
10. གནད་ཚིག་མང་པོའི་ནང་ནས་གནད་འགག་ཆེ་ཤོས་ཉི་ཤུ་ཐམ་པ་ཟུར་འདོན་བྱེད་དགོས།
11. དབྱིན་ཡིག་སོགས་སྐད་ཡིག་གཞན་འདིར་འབྲི་མི་དགོས།
12. མིང་ཚིག་གམ་གནད་ཚིག་རྐྱང་པ་ལས་བརྗོད་པ་དང་འགྲེལ་བཤད་མི་དགོས།
13. གནད་ཚིག་གི་རྗེས་སུ་ངེས་པར་དུ་ཤད་ཡོ་དགོས།
14. གནད་ཚིག་ཟེར་དུས་དོན་ཟབ་མོ་སྟོན་མཁན་གང་ཞིག་གཞུང་ལུགས་ཀྱི་ཆ་ཤས་ཆེན་པོ་མཚོན་ཐུབ་པའི་མིང་ཚིག་རྣམས་ལ་ཟེར་བ་ཤེས་དགོས།
```

**English gloss:** Extract keywords present in *both* root and commentary. Reject any term found in only one of the two. Show how each appears in root and in commentary. No synonyms, no sentences — single terms only. Draw only from the supplied documents. Return exactly the **20** most important. Tibetan script only, no English. Every term must be followed by a *shad* (`།`). A "key term" = a word carrying deep doctrinal meaning that represents a major component of the treatise.

### 3b. Version 3 — the most refined; use this as the repo baseline (verbatim)

```
**བོད་ཀྱི་གཞུང་ལུགས་རྩ་འགྲེལ་གནད་ཚིག་ཟུར་འདོན་གྱི་ཆེད་ལས་པ**

**ཁྱེད་ཀྱི་འགན་ཁུར་དང་སྒེར་ལས**

ཁྱེད་ནི་བོད་ཀྱི་ནང་བསྟན་གཞུང་ལུགས་ཀྱི་རྩ་བ་དང་འགྲེལ་པ་ནས་གནད་ཚིག་ཟུར་འདོན་བྱེད་མཁན་གྱི་མཁས་པ་ཞིག་ཡིན། ཁྱེད་ཀྱི་ལས་འགན་གཙོ་བོ་ནི་གཞུང་ལུགས་ཀྱི་དོན་གནད་ཟབ་མོ་མཚོན་མཁན་གྱི་གནད་ཚིག་རྣམས་ཞིབ་འཇུག་གིས་ཟུར་འདོན་བྱས་ནས་ལེགས་པར་སྒྲིག་སྦྱོར་བྱེད་པ་ཡིན།

**གནད་ཚིག་ཟུར་འདོན་གྱི་ལམ་ལུགས**

**1.** **བརྟག་དཔྱད་ཀྱི་རིམ་པ**

* **རྩ་བ་དང་འགྲེལ་པ་གཉིས་ཀ་ལ་ཞིབ་འཇུག་དང་འདྲ་བསྡུར་བྱེད།**
* **གཞུང་ལུགས་ཀྱི་ལྟེ་གནད་མཚོན་ཐུབ་པའི་མིང་ཚིག་རྣམས་ལ་གཙོ་བོར་དམིགས།**
* **རྩ་འགྲེལ་གཉིས་ཀའི་ནང་དུ་གནད་ཚིག་གསལ་བ་རྣམས་ཟུར་འདོན་བྱེད།**
* **གནད་ཚིག་རེ་རེའི་ཆེད་དུ་འགྲེལ་བཤད་ཚེག་བར་བཅུ་ལས་ཉུང་བ་བཏོན་ཏེ་གསལ་བཤད་བྱེད།**
* **རྩ་བ་དང་འགྲེལ་པ་གང་དུ་གསལ་ཚུལ་རྟགས་ཀྱིས་གསལ་བོ་སྟོན།**

**2.** **ཟུར་འདོན་གྱི་ཚད་གཞི**

**རྩ་ཆེའི་འདེམས་ཚད**

* **ངེས་པར་དུ་རྩ་འགྲེལ་གཉིས་ཀ་ལ་ཡོད་དགོས།** (རྩ་བ་ལ་ཡོད་ལ་འགྲེལ་པ་ལ་མེད་ན་མི་འདེམས། འགྲེལ་པ་ལ་ཡོད་ལ་རྩ་བ་ལ་མེད་ན་མི་འདེམས།)
* **གནད་ཚིག་རེ་རེ་ལ་གཞུང་ལུགས་ཀྱི་ལྟེ་གནད་མཚོན་ཐུབ་དགོས།**
* **ཚེག་བར་གསུམ་ནས་བཞི་བར་གྱི་མིང་ཚིག་དགོས།** (ཧ་ཅང་རིང་ཞིང་ཧ་ཅང་ཐུང་མི་འགྲིག)
* **གནད་ཚིག་ཆ་ཚང་ལེན་དགོས་ཏེ་བར་ཆོད་མི་རུང་།** (དཔེར་ན། "བཀྲ་ཤིས་བདེ་ལེགས་" ཞེས་པའི་གནད་ཚིག་ལ་"བཀྲ་ཤིས་" ཙམ་ལེན་ན་མི་འགྲིག)

**གལ་ཆེའི་དོན་གནད་ཆེད་ལས**

གཞུང་ལུགས་ཀྱི་ལྟེ་གནད་ཆེན་པོ་མཚོན་མཁན་ཞེས་པ་ལ་འདི་ལྟ་བུ་རྣམས་ཡོད།

* **ལྟ་བ་དང་སྒོམ་པ་སྐོར།** ལྟ་བ། སྒོམ་པ། རྟོགས་པ། ཡེ་ཤེས། ཞི་གནས། ལྷག་མཐོང་སོགས།
* **སྤྱོད་པ་དང་ཚུལ་ཁྲིམས་སྐོར།** ཚུལ་ཁྲིམས། སྡོམ་པ། སྤྱོད་པ། བསླབ་པ་སོགས།
* **ཐབས་ཤེས་ཟུང་འཇུག་སྐོར།** ཐབས། ཤེས་རབ། ཟུང་འཇུག། སྐུ་གསུམ་སོགས།
* **འཁོར་བ་དང་ཐར་པ་སྐོར།** བར་དོ། འཕོ་བ། སྲིད་པ། ཐར་པ། མོས་པ་སོགས།

**ལན་སྤྲོད་ཀྱི་རྣམ་བཞག**

**ཨང་རིམ་དང་སྒྲིག་བཀོད**

**རྩ་བ་འགྲེལ་པ་གཉིས་ཀའི་ནང་ཡོད་པའི་གནད་ཚིག་ཉི་ཤུ།** (གནད་འགག་ཆེ་ཤོས་ནས་ཆུང་ཤོས་ཀྱི་གོ་རིམ་ལྟར།)

༡། [གནད་ཚིག་དང་པོ]།

* **རྩ་བ་ནང་ཡོད་ཚུལ།** "[གནད་ཚིག་ཇི་མ་ཇི་བཞིན་རྟགས་ཀྱིས་བསྐོར་ནས་འཁོད་ཚུལ]"
* **འགྲེལ་པ་ནང་ཡོད་ཚུལ།** "[གནད་ཚིག་གི་འགྲེལ་བཤད་ཚེག་བར་བཅུ་ལས་ཉུང་བ]"

༢། [གནད་ཚིག་གཉིས་པ]།

* **རྩ་བ་ནང་ཡོད་ཚུལ།** "[གནད་ཚིག་ཇི་མ་ཇི་བཞིན་རྟགས་ཀྱིས་བསྐོར་ནས་འཁོད་ཚུལ]"
* **འགྲེལ་པ་ནང་ཡོད་ཚུལ།** "[གནད་ཚིག་གི་འགྲེལ་བཤད་ཚེག་བར་བཅུ་ལས་ཉུང་བ]"

[དེ་བཞིན་ཉི་ཤུ་ཐམ་པ་ལ།]

**ལམ་སྟོན་གལ་ཆེ**

**⚠️** **ངེས་པར་དུ་སྲུང་དགོས་པ**

* **བོད་ཡིག་ཁོ་ན་བེད་སྤྱོད་བྱེད།** དབྱིན་ཡིག་སོགས་སྐད་ཡིག་གཞན་མི་འཇུག
* **མིང་ཚིག་རྐྱང་པ་ལས་འགྲེལ་བཤད་མི་བྱེད།** སྤྲད་པའི་ཡིག་ཆ་ཁོ་ན་ལས་ཟུར་འདོན་བྱེད།
* **གནད་ཚིག་གི་རྗེས་སུ་ངེས་པར་དུ་ཤད་ཡོ་(།)འཇུག**
* **ཟུར་འདོན་བྱས་པའི་གནད་ཚིག་རྣམས་རྩ་བའི་ནང་ཇི་མ་ཇི་བཞིན་ཡོད་དགོས།**
* **རྩ་འགྲེལ་གཉིས་ཀར་གསལ་བའི་གནད་ཚིག་རྣམས་ཇི་ལྟར་གསལ་ཚུལ་རྟགས་སྟོན་དགོས།**
**གནད་ཚིག་ཟུར་འདོན་བྱེད་སྐབས་ངེས་པར་དུ་རྩ་བའི་ནང་གནད་ཚིག་དེ་ཡོད་པ་གང་ཞིག འགྲེལ་པའི་ནང་གནད་ཚིག་དེར་འགྲེལ་བཤད་ཡོད་པ་དགོས་པ་དང་། འགྲེལ་བཤད་དེ་ཡང་ངེས་པར་དུ་འགྲེལ་པ་བཞི་པོ་རེ་རེའི་ནང་ཇི་ལྟར་གསལ་ཚུལ་གསལ་བོར་སྟོན་དགོས། གནད་ཚིག་ཡོད་ཚད་གཞུང་ལུགས་ཀྱི་ནང་དོན་ཆེན་པོ་མཚོན་ཐུབ་པ་དགོས།**
** དེ་ཡང་རྩ་བའི་ནང་གནད་ཚིག་དེ་ཇི་ལྟར་ཡོད་པ་དེ་ལྟར་ངོ་སྤྲོད་དང་། གནད་ཚིག་དེ་ཡང་འགྲེལ་པ་བཞི་པོ་སོ་སོའི་ནང་འགྲེལ་བཤད་ཇི་ལྟར་ཡོད་ཚུལ་གསལ་བོར་རྟགས་""འདིའི་ནང་བཅུག་ནས་ངོ་སྤྲོད་བྱེད་དགོས།**
**དཔེ་མཚོན**

"གནད་ལུགས་རྟོགས་པའི་**ཤེས་རབ་**མི་ལྡན་ན། །ངེས་འབྱུང་**བྱང་ཆུབ་སེམས་**ལ་གོམས་བྱས་ཀྱང་། །**སྲིད་པའི་རྩ་བ་**གཅོད་པར་མི་ནུས་པས། །དེ་ཕྱིར་**རྟེན་འབྲེལ་**རྟོགས་པའི་ཐབས་ལ་འབད། །"

ཚིགས་བཅད་འདི་ལྟ་བུ་ལ་ཆ་མཚོན་ན། གནད་ཚིག་གཙོ་བོ་ **ཤེས་རབ།** **བྱང་ཆུབ་སེམས།** **སྲིད་པའི་རྩ་བ།** **རྟེན་འབྲེལ།** སོགས་ཟུར་འདོན་བྱེད་དགོས། ཟུར་འདོན་བྱས་པའི་གནད་ཚིག་རེ་རེ་ལ་གོང་དུ་ཞུས་པ་ལྟར་འགྲེལ་བཤད་ཚེག་བར་བཅུ་ལས་ཉུང་བ་ངེས་པར་དུ་དགོས།

---

**སྤྱིར་བཏང་གི་བེད་སྤྱོད་ཐབས།** མི་འདུན་པས་ད་ལྟ་རྩ་བ་དང་འགྲེལ་པའི་ཡིག་ཆ་སྤྲད་ན། སྔ་གསལ་ལམ་ལུགས་ལྟར་དེ་གཉིས་ནས་གནད་ཚིག་ཉི་ཤུ་ཟུར་འདོན་ཞུ་རྒྱུ་ཡིན།
```

**English gloss:** Role = expert extractor of key terms from Tibetan Buddhist root+commentary. Method: compare root and commentary; target words expressing the treatise's core; for each term give a gloss of **fewer than 10 syllable-units (ཚེག་བར)**; mark where it appears in each. Selection criteria: must appear in **both** root and commentary (reject otherwise); each must represent a doctrinal core; term length **3–4 ཚེག་བར**; take the complete term, never a truncated prefix (`བཀྲ་ཤིས་བདེ་ལེགས་` must not be cut to `བཀྲ་ཤིས་`). Four supplied semantic domains seed what "core" means (view/meditation; conduct/vows; means-wisdom union; samsara/liberation). Output = numbered list of **20** terms, most→least important, each with a *root-occurrence* line (exact quoted text) and *commentary-occurrence* line, both inside `""`. Hard constraints: Tibetan only; terms not sentences; source-grounded only; every term followed by `།`; verbatim presence in root required; **explanation must show how the term appears in each of the four commentaries separately**.

Version 2 (also in this topic) is nearly identical but asks for **50** terms, allows glosses of "ten ཚེག་བར or more", and specifies term length "not more than 4 ཚེག་བར". The trend across versions: 50→20 terms, ≥10→<10 syllable glosses.

---

## 4. Topic 236 — root–commentary verse alignment prompts (three iterations)

**Title:** 2.1 ai རིག་ནུས་ལ་བརྟེན་ནས་རྩ་འགྲེལ་མཉམ་སྦྱོར་བྱེད་ཐབས། · **Author:** Tashi_Dhondup · **Date:** 2025-05-16 (edited 2025-07-12)
URL: https://forum.openpecha.org/t/2-1-ai/236

Working corpus throughout: root = **འཕགས་པ་སྡུད་པ** (*Ratnaguṇasaṃcayagāthā* / Prajñāpāramitā-saṃcaya), plus **four** named commentaries. Explicitly stated to work in **Claude AI or Gemini** (`Claude ai ནམ་ཡང་ན་geminiནང་ཡར་འཇུག་བྱས་ན`) — unlike topic 289, which is Claude-only. Known weakness of v1/v2: the model **summarizes instead of extracting verbatim**.

### 4a. Version 1 (verbatim)

```
གོང་གི་དཔྱད་གཞི་ལྔ་ལས་འཕགས་པ་སྡུད་པ་ནི་གཞུང་གི་རྩ་བ་ཡིན་ཞིང་གཞན་རྣམས་དེའི་འགྲེལ་པ་རེད། ངའི་ལས་ཀའི་ངོ་བོ་ནི་རྩ་བ་དེའི་འགྲེལ་པ་སོ་སོའི་འགྲེལ་ཚུལ་རྣམས་ཟུར་འདོན་བྱེད་རྒྱུ་དེ་ཡིན་ལ། ད་ཐེངས་དཔེ་མཚོན་གྱི་ཚུལ་དུ་རྩ་ཚིག་ཤོ་ལོ་ཀ་གཅིག་དང་། དེའི་འགྲེལ་བ་རྣམས་གོང་དེར་བཞག་ཡོད། དེར་བརྟེན་ཁྱོད་ཀྱིས་གཤམ་གྱི་དོན་ཚན་ལྟར་རོགས་པ་གནང་རོགས།
•	རྩ་ཚིག་དེའི་འགྲེལ་པ་བཞི་ཡི་འགྲེལ་ཚུལ་རྣམས་མ་ལུས་པར་ཟུར་འདོན་གནང་རོགས། 
•	གནད་ཚིག་ཟུར་འདོན་གཏན་ནས་མི་དགོས། འདི་ལ་ངེས་པར་དུ་དོ་སྣང་གནང་རོགས།
•	སྡེ་ཚན་མང་པོ་གཏན་ནས་བཟོ་མི་དགོས། སྡེ་ཚན་མང་པོ་བཟོས་ན་ཕན་མེད་དུ་འགྱུར་རྒྱུ་རེད།
•	དཔྱད་ཁུངས་ཁ་གསལ་འགོད་རོགས།
•	དཔྱད་གཞི་དང་མ་འབྲེལ་པའི་ཚིག་གཅིག་གསར་སྣོན་མི་དགོས།
```

**Gloss:** Of the five supplied documents, *Sanchayagatha* is the root and the rest are its commentaries. Extract each commentary's exposition of the root, in full. **Do not** extract key terms here. **Do not** create many sub-sections. State sources clearly. Add not one word that isn't in the source documents.

### 4b. Version 3 — the refined aligner; use this as the repo baseline (verbatim)

```
**ལས་དོན།**

ཁྱེད་ལ་འཕགས་པ་སྡུད་པའི་རྩ་གཞུང་གཅིག་དང་དེའི་འགྲེལ་གཞུང་བཞི་བཅས་ཁྱོན་ཡིག་ཆ་ལྔ་ཡོད། ཁྱེད་ཀྱིས་རྩ་གཞུང་གི་ཤོ་ལོ་ཀ་རེ་རེ་ལ་དེའི་འགྲེལ་གཞུང་བཞི་པོ་ནས་འགྲེལ་བཤད་གང་ཡོད་པ་ཚང་མ་ཤེས་དགོས་ཤིང་གོ་སྒྲིག་ཐུབ་དགོས།

**ཡིག་ཆ་རྣམས་ཀྱི་མིང་།**

**རྩ་གཞུང་** **：** འཕགས་པ་སྡུད་པ།

**འགྲེལ་གཞུང་རྣམས** **：**

1. སྡུད་པའི་འགྲེལ་པ་རྒྱལ་བའི་ཡུམ་གྱི་དགོངས་དོན་ལ་ཕྱིན་ཅི་མ་ལོག་པར་འཇུག་པའི་ལེགས་བཤད།
2. སྡུད་པའི་འགྲེལ་པ་ཡིད་བཞིན་གྱི་ནོར་བུ་རིན་པོ་ཆེ་ལྟ་བུ་ཕ་རོལ་ཏུ་ཕྱིན་པ་རྒྱ་མཚོའི་སྡེ།
3. སྡུད་པའི་འགྲེལ་པ་རྒྱལ་བའི་དགོངས་གསལ་བཞུགས་སོ།།
4. བཅོམ་ལྡན་འདས་ཡོན་ཏན་རིན་པོ་ཆེ་སྡུད་པའི་ཚིགས་སུ་བཅད་པའི་དཀའ་འགྲེལ།

**བྱ་བའི་ལམ་ཁྲིད།**

**གནད་འགག་ཅན་གྱི་ལས་རིམ།**

1. རྩ་གཞུང་འཕགས་པ་སྡུད་པ་ནས་ཤོ་ལོ་ཀ་རེ་རེ་ངོས་འཛིན་བྱེད་པ།
2. ཤོ་ལོ་ཀ་རེ་རེར་གྲངས་ཀ་སྦྱར། (དཔེར་ན་ཤོ་ལོ་ཀ་༡། ༢། ༣...)
3. འགྲེལ་གཞུང་བཞི་པོ་ནས་དེ་དང་འབྲེལ་བའི་འགྲེལ་བཤད་གང་ཡོད་པ་འཚོལ་བ།

**གལ་ཆེའི་དགོས་པ།**

* འགྲེལ་བཤད་རིང་ཐུང་ཇི་ལྟ་བུ་ཡིན་ཡང་ཚང་མ་འགོད་དགོས།
* ཚིག་ཅིག་ཀྱང་ལུས་ཐབས་མེད།
* འགྲེལ་གཞུང་གང་ནས་བྱུང་བ་གསལ་པོར་འབྲི་དགོས།

**བཀོད་སྒྲིག་གི་རྣམ་གཞག**

**རེ་རེའི་ཤོ་ལོ་ཀ་བཀོད་ཐབས།**

### ཤོ་ལོ་ཀ་༡: [རྩ་ཚིག་གི་ཤོ་ལོ་ཀ་དང་པོ།]

**རྩ་ཚིག：** [འདིར་རྩ་གཞུང་ལས་ཤོ་ལོ་ཀ་དང་པོ་འགོད]

**འགྲེལ་བཤད་རྣམས：**

**[འགྲེལ་གཞུང་གི་མིང་ཐུང་བ།]ལས：**

[འདིར་དེ་དང་འབྲེལ་བའི་འགྲེལ་བཤད་ཚང་མ་འགོད]

[མུ་མཐུད་དེ་འགྲེལ་གཞུང་བཞི་ཚང་མར་འགྲེལ་བཤད་འདེམས་འདེད་བྱེད།]

---

### ཤོ་ལོ་ཀ་༢: [རྩ་ཚིག་གི་ཤོ་ལོ་ཀ་གཉིས་པ།]

**རྩ་ཚིག：** [འདིར་རྩ་གཞུང་ལས་ཤོ་ལོ་ཀ་གཉིས་པ་འགོད]

[དེ་བཞིན་མུ་མཐུད།]

**དམིགས་བསལ་གྱི་བསམ་འཆར།**

* གལ་ཏེ་ཤོ་ལོ་ཀ་གཅིག་ལ་འགྲེལ་གཞུང་རེ་རེ་ནས་འགྲེལ་བཤད་མེད་ན་ "འགྲེལ་བཤད་མེད།" ཅེས་འགོད།
* འགྲེལ་བཤད་རིང་པོ་ཡིན་ན་ཚད་གཏུབ་མི་དགོས། མ་ལུས་པར་འགོད།
* འགྲེལ་གཞུང་གི་མིང་རང་འཇགས་སུ་བེད་སྤྱོད་གནང་ནས་ཀློག་སླ་བར་བྱེད་དགོས།

**བེད་སྤྱོད་ཐབས** **：** འདི་ལྟར་ཞུ་བ། "ཁྱེད་ཀྱིས་རྩ་གཞུང་གི་ཤོ་ལོ་ཀ་དང་པོ་ནས་བཟུང་གོ་རིམ་ལྟར་གྲངས་ཀ་སྦྱར་ཏེ་མ་རྫོགས་བར་འདིའི་སྟེང་གི་བཀོད་སྒྲིག་ལྟར་འགོད་རོགས།"
```

**Gloss:** Task: 5 documents = 1 root + 4 commentaries (named explicitly). For each root śloka, find and organize all commentary on it from all four. Steps: (1) identify each śloka in the root; (2) number them `ཤོ་ལོ་ཀ་༡། ༢། ༣...`; (3) find related exposition in each of the four commentaries. Hard requirements: **record all exposition regardless of length; not one word may be omitted; state clearly which commentary each came from.** Output template is an H3 per śloka: `### ཤོ་ལོ་ཀ་N: [root verse]`, then `རྩ་ཚིག：`, then `འགྲེལ་བཤད་རྣམས：` with a labelled block per commentary. Special notes: if a commentary has nothing for a śloka, write literally `འགྲེལ་བཤད་མེད།` ("no commentary"); never truncate long expositions; keep commentary names verbatim for readability. Suggested driving instruction: *"Starting from śloka 1, number them in order and lay them out per the above format until complete."*

Version 2 is a looser procedural variant with the same three phases (`༡. ཤོ་ལོ་ཀ་ངོས་འཛིན་ལས་ཀ།` / `༢. འགྲེལ་གཞུང་རེ་རེ་ནས་ཉེ་འདུ།` / `༣. འདུ་སྒྲིག་ལས་ཀ།`) and ends `ངས་མཁོ་སྤྲོད་བྱས་པའི་ཡིག་ཆ་གཞིར་བཟུ་རོགས་གནང་རོགས།`.

---

## 5. Topic 260 — article-writing prompts (the 3.4 step)

**Title:** 3.04 ཝེ་ཁེ་ཤོག་ངོ་བཟོ་བྱེད་ཀྱི་བརྡ་སྟོན། ("Table of wiki article-writing prompts") · **Author:** `gade` · **Date:** 2025-05-26 (edited 2025-07-29)
URL: https://forum.openpecha.org/t/3-04/260

Contains **three** prompts attributed to different authors. `[ ]` is the term slot.

### 5a. Prompt by ཡེ་ཤེས་བསམ་འགྲུབ། (verbatim)

```
གཤམ་གསལ་དཔྱད་གཞི་ཡིག་ཆ་བཞི་ལ་གཞིར་བཅོལ་ནས་ [ ] ཞེས་པའི་ཐ་སྙད་འདིའི་སྐོར་ཝེ་ཁེ་རིག་མཛོད་ནང་འཇོག་ཆོག་ཆོག་གི་རྩོམ་ཡིག་ཚད་ལྡན་ཞིག་འབྲི་རོགས། གཤམ་གསལ་ཆ་རྐྱེན་ཚང་མ་དང་མཐུན་པར་བཟོ་དགོས། དྲི་བའི་ནང་དུ་ཡོད་པ་ལས་ལྷག་པ་གང་ཡང་འདིར་འབྲི་མི་དགོས། ལུང་རྟགས་འགོད་སྟངས་ངེས་པར་དུ་ཡག་པོ་བཟོ་དགོས། གཤམ་མཆན་འགོད་སྟངས་དེ་བས་ཀྱང་གཤམ་དུ་ཡོད་དགོས་པ་ལས་རྩོམ་ཡིག་ཨ་མའི་ནང་ཡོད་ན་མི་འགྲིག ཤེས་སོང་ངམ།
ནང་དོན།
1.         ཐ་སྙད་  [ ]  གྱི་ནང་དོན་ལུང་ཁུངས་སོ་སོར་གསལ་བ་ཟུར་འདོན་བྱེད་དགོས།
2.         ཐ་སྙད་   [ ]     གྱི་ནང་དོན་གོ་དཀའ་བ་ལ་འགྲེལ་བཤད་ཁ་གསལ་གནད་བསྡུས་དགོས།
3.         ནང་དོན་ལ་ས་བཅད་ག་ཚོད་བཟོ་དགོས་མིན་གཟིགས་དགོས།
སྒྲ་བཤད།
1.         ཐ་སྙད་   [  ]   ལྟ་བའི་སྒྲ་ལ་བཤད་པ་ཟུར་རེ་རེ་ནས་བརྒྱག་དགོས།
2.         སྒྲ་བཤད་ཀྱང་ཡིག་ཆའི་ཁུངས་གང་ནས་ཇི་ལྟར་གསལ་བ་ལྟར་འབྲི་དགོས།
3.         ཐ་སྙད་[] ཆ་ཤས་རེ་རེ་ནས་རྟགས་ ‘‘‘’’’ འདིའི་ནང་འཇོག་དགོས།
4.         ས་བཅད་རེ་རེ་ལ་ཤད་ངེས་པར་དུ་འབྲི་དགོས།
ཀློག་ཚུལ།
1.         ཐ་སྙད་  [ ]  ལྟ་བུ་ཀློག་ཚུལ་གྱི་སྐོར་དཔྱད་གཞིའི་ཡིག་ཆའི་ནང་གང་གསལ་བ་རྣམས་ཟུར་འདོན་བྱེ་དགོས།
སྒྲོམ་གཞི།
2.         རྩ་བའི་ས་བཅད་ཚང་མར་རྟགས་== འདིའི་ནང་འབྲི་དགོས།
3.         ནང་གསེས་ས་བཅད་ཡིན་རུང་རྟགས་==འདིའི་ནང་འབྲི་དགོས།
4.         ས་བཅད་དབྱེ་ལུགས་གཞུང་གི་ནང་དོན་དང་ངེས་པར་དུ་འཚམ་པ་དགོས།
ལུང་འདྲེན།
1.         ལུང་འདྲེན་བྱས་པའི་མ་ཡིག་གི་ཚིག་ཚང་མར་རྟགས་ “འདི་འབྲི་དགོས།
2.         ལུང་རྟགས་དང་པོ་དང་གཉིས་པ་སོགས་ལ་རིམ་པ་བཞིན་ལུང་རྟགས་(Code)ལུགས་མཐུན་འབྲི་དགོས།
3.         ལུང་དེའི་རྩོམ་པ་པོ་དང་། བརྩམས་ཆོས། ཤོག་གྲངས་སོག་རྩོམ་ཡིག་གི་གཤམ་ལ་འབྲི་དགོས། 
4.         འདི་ཡིག་ཆའི་གཤམ་ལ་ཡོད་དགོས་པ་ལས་རྩོམ་ཡིག་ནང་མི་དགོས། <ref>སི་ཏུ་ཆོས་ཀྱི་འབྱུང་གནས། སི་ཏུ་ཆོས་ཀྱི་འབྱུང་གནས་ཀྱི་ཡིག་བརྒྱའི་འགྲེལ་བ།</ref>
མཐའ་བསྡོམས།
1.         མདོར་ན་ལུང་རྟགས་སོགས་རྟགས་Code རྒྱག་སྟངས་ཝེ་ཁེ་རིག་མཛོ་དང་མཐུན་དགོས།
2.         རྩོམ་ཡིག་ཁུངས་བཙན་པ་དང་གོ་བདེ་བའི་ཆ་རྐྱེན་ངེས་པར་དུ་དགོས།
3.         མདོར་ན་ཐ་སྙད་[ ]འདི་ཝེ་ཁེ་རིག་མཛོད་ནང་ཡང་བསྐྱར་ཞིབ་འཇུག་མི་དགོས་པར་འཇོག་ཆོག་ཆོག་བཟོ་དགོས།
```

**Gloss:** Write a publication-ready wiki article on term `[ ]` grounded in the four supplied reference documents. Nothing beyond the prompt's scope. Fixed rubric of sections: **ནང་དོན** (content — extract what each source says, gloss the hard parts, decide how many subsections), **སྒྲ་བཤད** (etymology — one per source, quoted as the source has it, each component wrapped in `'''…'''`, every heading ends with a shad), **ཀློག་ཚུལ** (readings/pronunciation variants), **སྒྲོམ་གཞི** (structure — all headings AND subheadings in `==`, division must match the treatise's own structure), **ལུང་འདྲེན** (citation — all quoted source text in `"`, sequential `<ref>` codes, author/work/page **below** the article not inline, sample given: `<ref>སི་ཏུ་ཆོས་ཀྱི་འབྱུང་གནས། སི་ཏུ་ཆོས་ཀྱི་འབྱུང་གནས་ཀྱི་ཡིག་བརྒྱའི་འགྲེལ་བ།</ref>`). Conclusion: markup must conform to Wikipedia; article must be verifiable and readable; must be good enough to publish **without further review**.

### 5b. Prompt by རབ་བརྟན། — 25 numbered rules (verbatim, working term = གཤེ་བཅས་)

```
གོང་གསལ་དཔྱད་གཞིའི་ཡིག་ཆ་ཁག་གཞིར་བཞག་ནས་གཤེ་བཅས་ཞེས་པའི་ཐ་སྙད་འདི་ཝེ་ཁེ་རིག་མཛོད་ནང་གི་ཐ་སྙད་ངོ་སྤྲོད་བྱེད་ལུགས་དང་མཐུན་པར་གཤམ་གྱི་དོན་གནད་ཁག་གཞི་ལ་བཟུང་ནས་ནན་ཏན་གྱིས་འབྲི་རོགས།
1. དཔྱད་གཞི་ཡིག་ཆ་ཁག་ཏུ་གསལ་བའི་[]ཞེས་པའི་ནང་དོན་ཁག་ཞིབ་འཚོལ་གྱིས་ཟུར་འདོན་བྱེད་དགོས།
2. '''[]'''ཅེས་པའི་འགྲེལ་བཤད་དེ་ཝེ་ཁེ་རིག་མཛོད་ནང་འཇོག་དགོས་པས་དེ་དང་མཐུན་པར་དཔྱད་གཞིའི་ཡིག་ཆར་དྲངས་པའི་ལུང་དང་སྦྲགས་ཏེ་འགྲེལ་བཤད་ཁ་གསལ་གོ་བདེའི་དུམ་ཚན་གཅིག་ཏུ་ངོ་སྤྲོད་བྱེད་རོགས།
3. གཤེ་བཅསཞེས་པ་ནི་ལྟ་བུ་མ་བྲིས་པར་གཤེ་བཅས་ཞེས་པ་ནི་ལྟ་བུ་བྲིས་ཏེ་འགྲེལ་བཤད་བྱེད་སྐབས་མཐར་ངེས་པར་ཚེག་དགོས་པ་དང་[]་ཐེངས་གཉིས་ལ་དྲངས་མི་དགོས།
4. ལུང་ཞེས་པ་ནི་དཔྱད་གཞི་སོ་སོའི་ནང་དུ་ཐ་སྙད་དེའི་འགྲེལ་བཤད་ཀྱི་སྒྲུབ་བྱེད་དུ་དྲངས་པའི་གཞུང་གཞན་གྱི་ཁུངས་དྲངས་པ་ལ་གོ་དགོས། དཔེར་ན། སྤྱོད་འཇུག་ལས། “  ” ཅེས་གསུངས་པ་ལྟ་བུ།
5. ནན་བཤད་བྱེད་རྒྱུར། []ས་པའི་ཐ་སྙད་གོ་བདེ་བའི་འགྲེལ་བཤད་བྱེད་སྐབས་དཔྱད་གཞིའི་ནང་དུ་དྲངས་པའི་གཞུང་གཞན་གྱི་ལུང་ཁུངས་དང་དྲངས་པའི་ཚིག་དང་བཅས་པ་ངེས་པར་འགོད་དགོས།
6. ཝེ་ཁེ་རིག་མཛོད་ཀྱི་ལུགས་ལྟར་ལུང་རྟགས་(Code)འགོད་སྟངས་སོགས་ཇི་མ་ཇི་བཞིན་ངེས་པར་དུ་དགོས། དཔེར་ན། ལུང་ཁུངས་དཔྱད་གཞིའི་ཡིག་ཆ་གང་ཡིན་<ref></ref>བར་དུ་འགོད་དགོས།
7. རྩ་བའི་ས་བཅད་རྣམས་རྟགས་==འདིའི་ནང་ངེས་པར་དུ་འགོད་དགོས་པ་དང་ས་བཅད་ཀྱི་ཡི་གེའི་རྗེས་ལ་ཤད་དགོས། 
8. ས་བཅད་རེ་རེའི་བརྗོད་པ་བཟོ་སྐབས་ཁ་གསལ་གོ་བདེའི་ངང་ནས་འགྲེལ་པ་གནད་ལ་འཁེལ་བ་ཡིན་དགོས།
9. ནང་གསེས་ཀྱི་ས་བཅད་རྣམས་ ''' '''རྟགས་འདིའི་བར་དུ་བཀོད་རོགས། དཔེར་ན། '''གསང་སྔགས་ཀྱི་སྒོ་ནས་འགྲེལ་པ།''' ལྟ་བུ།
10. []ཞེས་པའི་འགྲེལ་བཤད་ཀྱི་ནང་དོན་དང་། མཚན་ཉིད། སྒྲ་བཤད། ངེས་ཚིག དབྱེ་བ། རྩོད་སྤོང་སོགས་དཔྱད་གཞིར་ཁ་གསལ་དུ་ཡོད་ན་དྲངས་དགོས་པ་ལས་ཁྱེད་ཀྱིས་ས་བཅད་གསར་པ་གང་ཡང་གསར་བཟོ་བྱས་མི་ཆོག
11. དཔྱད་གཞི་ཡིག་ཆ་སོ་སོའི་ནང་གི་ནང་དོན་རྣམས་ལུང་རྟགས་དང་བཅས་རྩོམ་ཡིག་ཏུ་དྲངས་དགོས།
12. ལུང་ཁུངས་ཡིག་ཆའི་ནང་དུ་མ་གཏོགས་རྩོམ་ཡིག་གི་གཞུང་དུ་རྩོམ་པ་པོ་དང་བརྩམས་ཆོས་ཀྱི་མིང་དྲངས་མི་དགོས།
13. ལུང་ཁུངས་ཡིག་ཆའི་ནང་རྩོམ་པ་པོ་དང་བརྩམས་ཆོས་ཀྱི་མིང་། ཤོག་ངོས་སོགས་ཡོད་ན་གསལ་འཁོད་གནང་རོགས།
14. རྫོགས་ཚིག་གི་རྗེས་སུ་ངེས་པར་དུ་ཤད་གཉིས་འཇོག་རོགས། དཔེར་ན། མེད་དོ། །ཡིན་ནོ། ། ལྟ་བུ། 
15. ''' '''རྟགས་འདིའི་བར་དུ་དྲངས་པའི་ཡི་གེ་རྗེས་མའི་མཐར་ངེས་པར་དུ་ཚེག་དགོས། 
16. རྗེས་སུ་ཁྱེད་ཀྱིས་བསྡུས་དོན་ཞེས་པའི་ས་བཅད་ཅིག་བཟོས་ཏེ་རྩོམ་ཡིག་སྤྱི་ལ་འགྲེལ་བཤད་མདོར་བསྡུས་ཤིག་བྱེད་རོགས།
17. རྩོམ་ཡིག་གི་གཞུང་དུ་མཛད་པ་པོའི་མཚན་དྲངས་མི་དགོས་པར་ཁ་ཐུག་ལུང་ཁུངས་དྲངས་ན་ཧ་ཅང་ཡག་པོ་འདུག
18. ལུང་ཁུངས་དྲངས་པའི་སྔོན་ལ་ལུང་ཁུངས་ཞེས་པའི་ས་བཅད་གསར་པ་ཞིག་ངེས་པར་དགོས།
19. []ཞེས་པ་དཔྱད་གཞིར་གཞིར་བཞག་གིས་ཝེ་ཁེ་རིག་མཛོད་དུ་བཞག་ཆོག་ཆོག་བཟོ་རོགས།
20. ལུང་ཁུངས་གང་ཡིན་རྩོམ་ཡིག་གི་དངོས་གཞིར་འབྲི་དགོས་པ་ལས་འོག་གི་ལུང་ཁུངས་ཀྱི་ས་བཅད་འོག་ཏུ་གང་ཡང་མི་དགོས། 
21. ཁྱེད་ཀྱིས་དཔྱད་གཞི་ཁག་གཞི་ལ་བཟུང་སྟེ་ཐ་སྙད་དེ་ཁོ་ནའི་འགྲེལ་པ་མ་གཏོགས་དེ་ལས་འཕྲོས་པའི་འགྲེལ་བཤད་འབྲི་མི་དགོས། 
22. ཁྱེད་ཀྱིས་དཔྱད་གཞི་ལས་དྲངས་པའི་ལུང་ཚང་མ་" "རྟགས་འདིའི་ནང་དུ་ངེས་པར་འཇོག་དགོས། 
23. ཁྱེད་ཀྱིས་ངེས་པར་དུ་གོང་གི་ཆ་རྐྱེན་དག་དང་མཐུན་པ་ཞིག་བཟོ་དགོས་པ་ལས་དེ་ལས་འགལ་ན་གྲུབ་དོན་དེ་ང་ལ་ཕན་ཐོགས་གང་ཡང་མེད།
24. དཔྱད་གཞིར་ཡོད་པའི་ལུང་ཁུངས་ལེགས་པར་དྲངས་པ་དང་སྦྲགས་གཤེ་བཅས་ཞེས་པའི་ཐ་སྙད་ཀྱི་འགྲེལ་བཤད་ཁ་གསལ་གོ་བདེ་ཡོང་བ་ཁྱོད་ཀྱིས་གཙོ་འདོན་བྱེད་དགོས། 
25. དཔྱད་གཞི་ལས་ལུང་དྲངས་པ་རེ་རེའི་རྗེས་སུ་ཁ་གསལ་གོ་བདེའི་འགྲེལ་བཤད་དང་སྦྲགས་ཏེ་རྩོམ་ཡིག་ཡག་པོ་ཞིག་བྲིས་ཏེ་གཞི་རིམ་སློབ་མས་གོ་ཐུབ་པ་ཞིག་འབྲི་རོགས།
```

**Key gloss points (the load-bearing rules):**
- **#3** Write `གཤེ་བཅས་ཞེས་པ་ནི` (with tsheg), not `གཤེ་བཅསཞེས་པ་ནི`; don't repeat the term twice.
- **#4/#5** `ལུང་` means a quotation *from another treatise* cited inside the commentary as proof (e.g. `སྤྱོད་འཇུག་ལས། "…" ཅེས་གསུངས་པ་ལྟ་བུ།`) — these nested citations must be carried through with their source.
- **#6** `<ref></ref>` around the reference-document identity.
- **#7** Top-level headings in `==`, with a shad after the heading text.
- **#9** Sub-headings use `'''…'''` (bold), **not** `===`. Example given: `'''གསང་སྔགས་ཀྱི་སྒོ་ནས་འགྲེལ་པ།'''`
- **#10** Allowed section vocabulary is fixed — `ནང་དོན`, `མཚན་ཉིད`, `སྒྲ་བཤད`, `ངེས་ཚིག`, `དབྱེ་བ`, `རྩོད་སྤོང` — **and the model may not invent new sections.**
- **#12/#17** Author and work names must **not** appear in article prose, only in the reference; cite directly instead.
- **#14** Sentence-final double shad `། །` (e.g. `མེད་དོ། །ཡིན་ནོ། །`).
- **#16** Add a `བསྡུས་དོན` (summary) section at the end.
- **#18** A `ལུང་ཁུངས` heading must precede the references.
- **#20** Everything belongs in the article body; nothing goes under the references heading.
- **#21** Only explain the term itself, no digressions.
- **#22** All quotations in `" "`.
- **#25** Target reading level: **a primary/basic-level student** (`གཞི་རིམ་སློབ་མས་གོ་ཐུབ་པ`).

### 5c. Multi-source merge prompt (verbatim, working term = ཉན་ཐོས་)

Header: **ཐ་སྙད་གཅིག་གཞུང་མི་འདྲ་བ་གཉིས་ཀྱི་ནང་དུ་ཡོད་པ་རྣམས་ཕྱོགས་བསྡུས་ཀྱིས་ཝེ་ཁེ་ཤོག་ངོས་བཟོ་བའི་བརྡ་སྟོན།** ("prompt for building a wiki page by consolidating one term occurring across two different treatises") — this is the closest published thing to the merge/update logic of stage 4.

```
གོང་གསལ་དཔྱད་གཞིའི་ཡིག་ཆ་གཉིས་གཞིར་བཞག་ནས་ཉན་ཐོས་་ཞེས་པའི་ཐ་སྙད་འདི་ཝེ་ཁེ་རིག་མཛོད་ནང་གི་ཐ་སྙད་ངོ་སྤྲོད་བྱེད་ལུགས་དང་མཐུན་པར་གཤམ་གྱི་དོན་གནད་ཁག་གཞི་ལ་བཟུང་ནས་ནན་ཏན་གྱིས་འབྲི་རོགས།
1. དཔྱད་གཞི་གཉིས་ལས་ཉན་ཐོས་ཞེས་པའི་ཐ་སྙད་ཀྱི་འགྲེལ་བཤད་ཐད་ཀར་འབྲེལ་བ་ཡོད་པ་རྣམས་དྲངས་ཏེ་རྩོམ་ཡིག་གསར་པ་ཞིག་འབྲི་རོགས།
2. ཁྱེད་ཀྱིས་དཔྱད་གཞིར་དྲངས་པའི་ལུང་ཁག་ཀྱང་ཝེ་ཁེ་རིག་མཛོད་ཀྱི་རྩོམ་འབྲི་མཐུན་པར་code གང་ཡོད་རང་འཇགས་འཇོག་རོགས། 
3. དཔྱད་གཞི་གཉིས་སུ་ཡོད་པའི་ལུང་འདྲེན་རྣམས་ཉན་ཐོས་ཞེས་པའི་ཐ་སྙད་འགྲེལ་བཤད་ཀྱི་རྩོམ་ཡིག་འབྲི་སྐབས་ངེས་དགོས་ཁག་ཇི་བཞིན་དྲངས་རོགས། 
4. དཔྱད་གཞི་ཡིག་ཆ་དང་པོ་དང་གཉིས་པ་ཞེས་ལུང་དྲངས་མི་དགོས་པར་དཔྱད་གཞི་ཡིག་ཆ་རེ་རེའི་ནང་གི་ལུང་དྲངས་བཀོད་པ་རྣམས་ཇི་བཞིན་བཀོད་རོགས།  
7. ཁྱེད་ཀྱིས་དཔྱད་གཞིའི་ཡིག་ཆ་གཉིས་སུ་" "རྟགས་འདི་གཉིས་ཀྱི་བར་དུ་བཀོད་པ་རྣམས་ལུང་འདྲེན་གྱི་ཚིག་ཡིན་པས་དེ་དག་དང་མཉམ་དུ་</ref>.......</ref>རྟགས་འདི་གཉིས་བར་དུ་གང་ཡོད་ཇི་བཞིན་བཀོད་རོགས། 
8. ཁྱོད་ཀྱིས་ཉུང་དུ་བཏང་སྟེ་དཔྱད་གཞིའི་ཡིག་ཆ་གཉིས་ལས་ངེས་པར་དགོས་པ་ཁག་ལས་ལུང་དྲངས་མི་དགོས། མཁས་པ་རེ་རེ་འགྲེལ་པ་ལས་ལུང་རེ་རེ་ལས་དྲངས་མི་དགོས། དེ་བཞིན་རེད།  
9. མདོར་བསྡུས་སུ་བཏང་སྟེ་ལུང་འདྲེན་ཇི་བཞིན་དྲངས་རྗེས་ཁྱེད་ཀྱིས་གོ་བདེའི་འགྲེལ་བཤད་བྱས་ཏེ་གཞི་རིམ་སློབ་མའི་གོ་ཐུབ་པ་ཞིགབཟོ་རོགས།
```

**Gloss + note:** Merge two sources into one new article on the term. Preserve existing wiki markup/codes verbatim. Do **not** write "reference document one / two" — carry each source's own citations through as-is. Anything in `" "` in the sources is a quotation and must be carried with its `<ref>…</ref>` intact. **#8:** be economical — cite only what's necessary, **one quotation per scholar's commentary**. **#9:** after quoting, add a plain-language gloss at basic-student level. *Numbering is defective in the original: it runs 1,2,3,4,7,8,9 — items 5 and 6 are absent from the post.*

---

## 6. Topic 324 — "New Prompt Sample" (the flagship worked example)

**Title:** New Prompt Sample (⚠️ slug is `new-prompt-sample`, not `prompt-sample`) · **Author:** Tenzin Tsewang (`@Tsewang`) · **Date:** 2025-06-24, 3 posts, 46 views
URL: https://forum.openpecha.org/t/new-prompt-sample/324

Framing text before the prompt: the two things the human must fix afterwards are the **ལུང་ཁུངས།** section (add each citation's URL and page number) and the **དཔྱད་གཞིའི་ཡིག་ཆ།** section (add the full source's URL, author, title, publication year).

### 6a. The prompt (verbatim)

```
ཁྱེད་ཀྱིས་"སཏྭ་"ཞེས་པའི་ཐ་སྙད་འདིའི་ཐོག་ཝེ་ཁེ་རིག་མཛོད་ནང་འཇོག་པའི་དཔྱད་རྩོམ་གྱི་ཤོག་ངོས་གསར་པ་ཞིག་བཟོ་དགོས། 
དེའི་ཐོག་འོག་གི་ལམ་སྟོན་གྱི་དོན་ཚན་དེ་དག་ནང་གང་འཁོད་པ་དེ་ལྟར་ལག་བསྟར་བྱ་དགོས།

༡༽ ཝེ་ཁེ་ཤོག་ངོས་ཀྱི་དཔྱད་རྩོམ་དེའི་ཆེད་དུ་གནད་དོན་ཚང་མ་གོང་དུ་ uploadབྱས་པའི་དཔྱད་གཞིའི་ཡིག་ཆ་ག་ཚོད་ཡོད་པ་དེ་ཚོ་ཁོ་ན་ནས་ལེན་དགོས་ལ་གཞན་ཡོང་ཁུངས་གང་ནས་ཀྱང་ལེན་མི་ཆོག

༢༽ ཝེ་ཁེ་ཤོག་ངོས་ཀྱི་ཡིག་ཆའི་ནང་དོན་དེའི་དོན་ཚན་སོ་སོ་ == རྟགས་འདིའི་ནང་ངེས་པར་འཇོག་དགོས།

༣༽ དོན་ཚན་ཐོག་མ་དེ་ལ་བཙལ་བྱའི་ཐ་སྙད་དེའི་སྤྱི་ཡོངས་ཀྱི་གོ་དོན་མདོར་བསྡུས་ཤིག་འབྲི་དགོས་པ་དང་། དོན་ཚན་ཐོག་མ་དེ་ལ་དོན་ཚན་གྱི་མིང་ཟུར་དུ་མི་དགོས།

༤༽ དེའི་རྗེས་སུ་ཐ་སྙད་དེའི་ངེས་ཚིག་དང་། དབྱེ་བ། མཚན་ཉིད། གཞུང་ལུགས་སོ་སོའི་བཤད་པ། ལ་སོགས་དོན་ཚན་གང་དགོས་གོང་བཞིན་བཀོད་དགོས།

༥༽ དོན་ཚན་སོ་སོའི་ནང་དཔྱད་གཞིའི་ཡིག་ཆའི་ནང་ནས་ལུང་འདྲེན་བཀོད་དགོས་པ་དང་། ལུང་འདྲེན་གང་དུ་བྱས་ཀྱང་ལུང་དེ་ "'' རྟགས་འདིའི་ནང་ངེས་པར་འཇོག་དགོས།

༦༽ ལུང་འདྲེན་ཇི་ཙམ་བྱས་ཀྱང་ <ref></ref> འདིའི་ནང་འཇོག་དགོས་པ་དང་། དེའི་ནང་ལ་གནས་ཚུལ་བཞི་འཇོག་དགོས་པ་དང་། དེ་བཞི་ནི། རྩོམ་པ་པོའི་མིང་། དཔྱད་རྩོམ་གྱི་མིང་། པར་སྐྲུན་གྱི་ལོ། ཤོག་གྲངས། བཅས་ཡིན། གལ་སྲིད་པར་སྐྲུན་གྱི་ལོ་དང་ཤོག་གྲངས་གང་ཡིན་མི་ཤེས་ན་མི་འབྲི་ནའང་འགྲིག

༧༽ མཐའ་མའི་དོན་ཚན་གསུམ་ལས་དང་པོ་དེ་ ==འབྲེལ་ཡོད་ཤོག་ངོས།== ཞེས་བཀོད་དགོས་ལ། གཉིས་པ་དེ་ ==ལུང་ཁུངས།== གསུམ་པ་དེ་==དཔྱད་གཞིའི་ཡིག་ཆ།== ཞེས་བཀོད་དགོས།

༨༽ འབྲེལ་ཡོད་ཤོག་ངོས་ཞེས་པའི་དོན་ཚན་དེའི་ནང་། ཤོག་ངོས་འདིའི་ཐ་སྙད་གཙོ་བོ་དེ་དང་འབྲེལ་བའི་གལ་ཆེའི་ཐ་སྙད་གཞན་གང་ཡོད་པ་རྣམས་ Bullet དང་བཅས་བཀོད་དགོས་པ་དང་། གལ་ཆེའི་ཐ་སྙད་རྣམས་དཔེར་ན་ [[རྡོ་རྗེ།]] འདི་འདྲ་མིན་པར། [[རྡོ་རྗེ་]] འདི་ལྟར་ཐ་སྙད་ཀྱི་མཐའ་ལ་ཚེག་རྡོག་གཅིག་ངེས་པར་དུ་རྒྱག་ནས་རྟགས་འདིའི་ནང་འཇོག་དགོས་པ་དང་། དེའི་རྗེས་སུ་ཤད་རྒྱག་མི་དགོས།

༩༽ ལུང་ཁུངས་ཞེས་པའི་དོན་ཚན་དེའི་ནང་ལུང་འདྲེན་ག་ཚོད་བྱས་ཡོད་པ་དེ་ཚོ་རིམ་པས་བཀོད་དགོས།

༡༠༽ དཔྱད་གཞིའི་ཡིག་ཆ་ཞེས་པའི་དོན་ཚན་མཐའ་མ་དེར་དཔྱད་གཞིའི་ཡིག་ཆ་ག་ཚོད་བེད་སྤྱོད་བྱས་ཡོད་པའི་ཐོ་གཞུང་བཀོད་དགོས། དེའི་ནང་གནས་ཚུལ་གསུམ་བཀོད་དགོས་པ་ནི། རྩོམ་པ་པོའི་མིང་དང་། དཔྱད་རྩོམ་གྱི་མིང་། པར་སྐྲུན་གྱི་ལོ་བཅས་ཡིན། གལ་སྲིད་གནས་ཚུལ་ཁ་གསལ་མེད་ན་མ་འབྲི་ནའང་འགྲིག།

༡༡༽ དཔྱད་རྩོམ་ཆ་ཚང་ནང་བོད་ཡིག་ཁོ་ན་ལས་ཡི་གེ་དང་ཨང་ཀི་སོགས་སྐད་རིགས་གཞན་བེད་སྤྱོད་བྱ་མི་ཆོག

༡༢༽ འདིའི་སྒྲུབ་འབྲས་དེ་ཟུར་དུ་document ཞིག་བཟོ་རོགས།

14) All references should include a dummy link like this example; <ref> [[https://dummy.com](https://dummy.com/) མཁན་པོ་དཔལ་ལྡན་ཤེས་རབ། ཡིག་བརྒྱ་པའི་རྡོ་རྗེའི་ཚིག་འགྲེལ། ཤོགས་གྲངས་༣]</ref>, so that I could later replace the dummy link with an appropriate source link.
```

**Verified numbering defect:** the list runs `༡༽ ༢༽ ༣༽ ༤༽ ༥༽ ༦༽ ༧༽ ༨༽ ༩༽ ༡༠༽ ༡༡༽ ༡༢༽ 14)` — **there is no item 13**, and item 14 is the only one in English/Arabic numerals. Confirmed by grep against the raw source.

**Gloss:** Build a new wiki article page for term "སཏྭ་". (1) Draw everything **only** from the uploaded reference documents, no outside sources. (2) Each section wrapped in `==`. (3) First section = a general summary of the term, **with no section heading**. (4) Then sections as needed: ངེས་ཚིག (definition), དབྱེ་བ (divisions), མཚན་ཉིད (characteristics), གཞུང་ལུགས་སོ་སོའི་བཤད་པ (per-treatise exposition). (5) Every section must carry quotations from the sources, wrapped in `"''`. (6) Every quotation inside `<ref></ref>` carrying **four** fields — author, work title, publication year, page — year and page optional if unknown. (7) The **last three** sections must be `==འབྲེལ་ཡོད་ཤོག་ངོས།==`, `==ལུང་ཁུངས།==`, `==དཔྱད་གཞིའི་ཡིག་ཆ།==`. (8) Related-pages entries as bullets; wikilinks must be `[[རྡོ་རྗེ་]]` (**trailing tsheg, no shad**), *not* `[[རྡོ་རྗེ།]]`. (9) List citations in order. (10) Bibliography with author/title/year. (11) **Tibetan script and Tibetan numerals only** throughout. (12) Produce the output as a separate document. (14) Every ref must carry a **dummy link** in the form `<ref>[https://dummy.com མཁན་པོ་དཔལ་ལྡན་ཤེས་རབ། ཡིག་བརྒྱ་པའི་རྡོ་རྗེའི་ཚིག་འགྲེལ། ཤོགས་གྲངས་༣]</ref>` so a human can later swap in the real source URL.

### 6b. Result and the two manual fix-ups (verbatim)

Result labelled **`སྒྲུབ་འབྲས། Claude Opus4`**. The generated article on `སཏྭ་` has sections: (lead), `ངེས་ཚིག`, `རྡོ་རྗེ་སེམས་དཔའི་ངོ་བོ`, `ཡིག་བརྒྱ་པའི་སྔགས་དོན`, `དམ་ཚིག་སེམས་དཔའ`, `སློབ་དཔོན་ཆེན་པོའི་གསུང་ལས`, `འབྲེལ་ཡོད་ཤོག་ངོས།` (7 wikilinks), `ལུང་འདྲེན་གྱི་ཁུངས།` (10 refs), `དཔེ་ཁུངས།` (4 works). Sources used: མཁན་པོ་དཔལ་ལྡན་ཤེས་རབ།, སི་ཏུ་ཆོས་ཀྱི་འབྱུང་གནས།, པཎ་ཆེན་བློ་བཟང་ཆོས་རྒྱན།, ཨ་ཁུ་ཤེས་རབ་རྒྱ་མཚོ། — all commentaries on the ཡིག་བརྒྱ (hundred-syllable mantra).

The post then states **`སྒྲུབ་འབྲས་ལ་རང་ངོས་ནས་བཅོས་དགོས་པའི་གནད་དོན་གཉིས།`** ("two things you must fix yourself in the output") — verbatim:

```
ལུང་ཁུངས། དཔྱད་རྩོམ་གྱི་ཁ་ཐུག་དེར་བཟོ་བཅོས་བྱ་རྒྱུ། རང་རང་གི་ཤོག་གྲངས་དང་བཅས་དྲ་ཐག་སྣོན་རྒྱུ།

<ref>མཁན་པོ་དཔལ་ལྡན་ཤེས་རབ། གསང་སྔགས་ཡིག་བརྒྱའི་འགྲེལ་པ།</ref>

<ref>[https://www.wikisource.com མཁན་པོ་དཔལ་ལྡན་ཤེས་རབ། གསང་སྔགས་ཡིག་བརྒྱའི་འགྲེལ་པ། ཤོག་ངོས།༧]</ref>

དཔྱད་གཞིའི་ཡིག་ཆ། དཔྱད་རྩོམ་གྱི་མཐའ་ལ་ཡོད་པའི་ཐོ་གཞུང་ལས་བཟོ་བཅོས་བྱ་རྒྱུ། དཔྱད་གཞིའི་ཡིག་ཆ་ཆ་ཚང་གི་རྣམ་པའི་ཁུངས་གར་ཡོད་ཀྱི་དྲ་ཐག་བཀོད་རྒྱུ། པར་སྐྲུན་གྱི་ལོ་བཀོད་རྒྱུ།

མཁན་པོ་དཔལ་ལྡན་ཤེས་རབ། གསང་སྔགས་ཡིག་བརྒྱའི་འགྲེལ་པ།

[https://www.wikisource.com མཁན་པོ་དཔལ་ལྡན་ཤེས་རབ། གསང་སྔགས་ཡིག་བརྒྱའི་འགྲེལ་པ། ༡༩༥༥]
```

**This is the exact before→after transform the pipeline must automate:** bare `<ref>author. title.</ref>` → `<ref>[URL author. title. page]</ref>`.

**Author's own caveat (post #3, verbatim):** *"this sample is just for temporary use for a presentation purpose, (on how we have been working so far). Here one is needed to add a link to a reference manually. I'm sure you can get better prompts, with which you can let AI get the link address for you."* — i.e. **the author explicitly flags automatic source-link resolution as the missing piece.**

Companion Google Doc: `https://docs.google.com/document/d/1WOX6PG2GQ1Ct03QaNWIjeNiDPmmu906rilZK54AzuMQ/edit`

---

## 7. Topic 309 — citation markup conventions + the earlier prompt variant

**Title:** ཝེ་ཁེ་ཤོག་ངོས་གསར་བཟོའི་བརྡ་སྟོན་དང་། ལུང་འདྲེན་བྱེད་སྟངས། ལུང་ཁུངས་དྲ་ཐག་གི་བརྡ་ཡིག་ཁ་སྣོན་བྱེད་སྟངས། དཔེ་མཚོན་དང་བཅས་པ། · **Author:** Tsewang · **Date:** 2025-06-15
URL: https://forum.openpecha.org/t/topic/309

Explicit note: the result shown came from **Claude Opus 4** specifically, and *"if taken from Claude AI Sonnet 4 or other AIs the result may change"* (`Claude AI, Sonnet 4དང་། གཞན་ཡང་རིག་ནུས་གཞན་ནས་བླང་ན་སྒྲུབ་འབྲས་ལ་འགྱུར་བ་འགྲོ་སྲིད་པ་རེད།`).

This is the **11-item predecessor** of the topic-324 prompt. It is identical for items ༡–༤, then diverges on citations — this variant uses **named refs** where 324 uses dummy links:

```
༥༽ དོན་ཚན་སོ་སོའི་ནང་དཔྱད་གཞིའི་ཡིག་ཆའི་ནང་ནས་ལུང་འདྲེན་བཀོད་དགོས་པ་དང་། ལུང་འདྲེན་གང་དུ་བྱས་ཀྱང་ལུང་དེ་ "'' རྟགས་འདིའི་ནང་ངེས་པར་འཇོག་དགོས་པ་དང་། 
ལུང་འདྲེན་ཇི་ཙམ་བྱས་ཀྱང་ cite བྱ་དགོས། cite བྱེད་སྐབས་དཔེར་ན་ <ref name=”མཁན་པོ་དཔལ་ལྡན”/> code འདི་ལྟ་བུ་བེད་སྤྱོད་བྱ་དགོས།

༦༽ གལ་སྲིད་དཔྱད་གཞིའི་ཡིག་ཆ་ཞིག་ལས་ལུང་འདྲེན་ཚར་གཅིག་ལས་མང་བ་བྱས་ཡོད་ཚེ་གོང་གི་ལུང་འདྲེན་དེའི་འོག་ལ་ superscript གི་ཚུལ་དུ་འབྲི་དགོས་པ་ལས། འོག་གི་ལུང་འདྲེན་ཐོ་གཞུང་ནང་བསྐྱར་དུ་འབྲི་མི་དགོས།

༧༽ མཐའ་མའི་དོན་ཚན་གཉིས་ལས་དང་པོ་དེ་ ==འབྲེལ་ཡོད་ཤོག་ངོས།== ཞེས་བཀོད་དགོས་ལ། གཉིས་པ་དེ་ ==དཔེ་ཁུངས།== ཞེས་བཀོད་དགོས།

༩༽ དཔེ་ཁུངས་ཞེས་པའི་དོན་ཚན་མཐའ་མ་དེ་<reference>ཞེས་མགོ་བཙུག་རྗེས་དེའི་ནང་གོང་དུ་ལུང་འདྲེན་བྱས་པའི་ཐོ་གཞུང་བཀོད་རྗེས། </reference>ཞེས་མཇུག་བསྡུ་དགོས།
```

Note **`<reference>`/`</reference>` is a typo for MediaWiki's `<references>` / `<references />`** — a repo that copies this literally will emit broken wikitext.

### 7a. The wikilink rules (from the commentary, verbatim examples)

- `[[རྡོ་རྗེ་]]` — correct: trailing **tsheg**, no shad. If the page exists the link renders **blue**; if not, **red** (`ཡི་གེ་དེ་སྔོན་པོར་མ་གྱུར་བར་དམར་པོར་གྱུར་ཚེ། ཐ་སྙད་དེའི་སྐོར་ཤོག་ངོས་བཟོས་མེད་པའི་རྟགས་མཚན་རེད།`) — **this is the team's manual existence check**.
- `[[རྡོ་རྗེ་|རྡོ་རྗེ།]]` — piped form: first = the link target (must match the wiki page exactly), second = display text; use when you need a shad in the display.
- `[[ཡིག་བརྒྱ་|ཡི་གེ་བརྒྱ་པ།]]` — use when the wiki has `ཡིག་བརྒྱ་` but your prose wants `ཡི་གེ་བརྒྱ་པ།`, i.e. **synonym redirect handling**.

### 7b. The named-reference block (verbatim)

```
* ཐོག་མར་Edit Sourceནང་འགྲོ་དགོས།
* ཡིག་ཆའི་ཐོག་མ་ནས་རིམ་པས་ལྟ་དུས་<ref name=”མཁན་པོ་དཔལ་ལྡན”/> ཞེས་སོགས་ཡིག་ཆའི་ནང་ལུང་འདྲེན་གང་དུ་ཡོད་པ་དེའི་མཇུག་ཏུ་འཇོག་ཡོད། འདིའི་ནང་དྲ་ཐག་གི་ཁ་བྱང་གང་ཡང་བཀོད་མེད། དྲ་ཐག་ནི་ཡིག་ཆའི་མཐའ་མཇུག་ཏུ་བཀོད་དགོས་པ་རེད།
* ཡིག་ཆའི་མཐའ་ལ་བརྗོད་གཞི་ཐ་མའི་ཚུལ་དུ་ ==དཔེ་ཁུངས།== ཞེས་འཁོད་ཡོད་པ་དང་དེའི་འོག་ཏུ་

<references>

<ref name="མཁན་པོ་དཔལ་ལྡན">གསང་སྔགས་ཡིག་བརྒྱའི་འགྲེལ་པ། མཁན་པོ་དཔལ་ལྡན་ཤེས་རབ།</ref>

<ref name="པཎ་ཆེན་ཆོས་རྒྱན">པཎ་ཆེན་བློ་བཟང་ཆོས་རྒྱན་གྱི་ཡིག་བརྒྱའི་འགྲེལ་པ།</ref>

<ref name="སི་ཏུ་ཆོས་འབྱུང">སི་ཏུ་ཆོས་ཀྱི་འབྱུང་གནས་ཀྱི་ཡིག་བརྒྱའི་འགྲེལ་བ།</ref>

<ref name="ཨ་ཁུ་ཤེས་རབ">ཨ་ཁུ་ཤེས་རབ་རྒྱ་མཚོ།</ref>

</references>
```

### 7c. Adding per-quote source links (verbatim)

```
<ref name=”མཁན་པོ་དཔལ་ལྡན”>མཁན་པོ་དཔལ་ལྡན་ཤེས་རབ། གསང་སྔགས་ཡིག་བརྒྱའི་འགྲེལ་པ། </ref>འདི་ལྟར་ཡོད་པར། ཡི་གེ་ལྗང་ཁུའི་མཐའ་དེ་ནས་བརྡ་ཡིག་[[  ]]འདིའི་ནང་ལུང་འདྲེན་གྱི་ཁུངས་བསྟན་པའི་དྲ་ཐག་གང་ཡིན་པའི་ཁ་བྱང་དང་། དེའི་རྗེས་བར་སྟོང་གཅིག་བཞག་ནས་ ༡་༠ ༡་༡ ༡་༢ སོགས་རིམ་པས་བཀོད་དགོས། དཔེར་ན།

<ref name=”མཁན་པོ་དཔལ་ལྡན”>མཁན་པོ་དཔལ་ལྡན་ཤེས་རབ། གསང་སྔགས་ཡིག་བརྒྱའི་འགྲེལ་པ། [[https://www.wikisource.com/page/???? ༡་༠]]

[[https://www.wikisource.com/page/???? ༡་༡]]

[[https://www.wikisource.com/page/???? ༡་༢]]

</ref>
```

Rendering target:
```
1. ↑ ༡་༠ ༡་༡ ༡་༢ ༡་༣ མཁན་པོ་དཔལ་ལྡན་ཤེས་རབ། གསང་སྔགས་ཡིག་བརྒྱའི་འགྲེལ་པ། [༡་༠][༡་༡][༡་༢][༡་༣]
2. ↑ སི་ཏུ་ཆོས་ཀྱི་འབྱུང་གནས། ཡིག་བརྒྱའི་འགྲེལ་བ། [༢་༠]
```

**Note:** `[[url text]]` is doubled — MediaWiki external links take **single** brackets `[url text]`. Copying this verbatim produces broken markup. Companion Google Doc: `https://docs.google.com/document/d/1M3N85dIeUeGLZ1BPNumR5UI9wXtwPiT_NJuqUwDqD48/edit`

---

## 8. Topic 319 — the citing-sources guideline (Tibetan adaptation of WP:CITE)

**Title:** ཝེ་ཁེ་ལམ་སྟོན་ཡིག་ཆ། ལུང་འདྲེན། Citing Sources · **Author:** Tsewang · **Date:** 2025-06-22 · Source: adapted from https://en.wikipedia.org/wiki/Wikipedia:Citing_sources
URL: https://forum.openpecha.org/t/citing-sources/319

Key normative content, glossed (Tibetan original is a long prose guideline; the machine-actionable parts):

**Three citation types** (`ལུང་འདྲེན་གྱི་རིགས་གསུམ།`): *Inline Citation* (footnote adjacent to the claim, carrying author/work/year — **"the citation we use on our wiki pages belongs to this type"**); *In-text attribution*; *A general reference* (names the source but not a specific passage).

**Reuse / named references** (verbatim core):
```
<ref>ལུང་འདྲེན་གྱི་འབྱུང་ཁུངས་ཀྱི་གནས་ཚུལ།</ref>
<ref name="མིང་">ལུང་འདྲེན་གྱི་འབྱུང་ཁུངས་ཀྱི་གནས་ཚུལ།</ref>
<ref name="མིང་" />
<ref name="Smith 2005 p94">ལུང་འདྲེན་གྱི་འབྱུང་ཁུངས་ཀྱི་གནས་ཚུལ།</ref>
```
Rules: the name may be any text but **must not be digits alone**; if it contains spaces it **must be quoted**; the name should relate to the citation, e.g. `"སི་ཏུ། ༡༤༩༨"`.

**Required fields for a book citation:** author(s); title; volume if any; publisher; place of publication; date; chapter or page cited; edition if not first; ISBN if available.
**For a web page:** URL; author(s); article title; site name; publisher; publication date; page; **and the access date** (required when publication date is unknown).

**External-link form** (verbatim example): `<ref>[[www.wikisource.com](http://www.wikisource.com) སི་ཏུ། ཡིག་བརྒྱའི་འགྲེལ་པ། ༡༨༧༦]</ref>` — bracket, URL, space, title, close bracket, "so the URL is hidden and the title is clickable".

**Multi-edition example:** `བློ་བཟང་གྲགས་པ། (༡༨༨༡) ལམ་རིམ་ཆེན་མོ། མཚོ་སྔོན་མི་རིགས་དཔེ་སྐྲུན་ཁང་། བསྐྱར་སྐྲུན། བོད་ཀྱི་དཔེ་མཛོད་ཁང་།༢༠༢༥`

**Deletion risk (verbatim policy):** an article with no citations at all may be nominated for removal or tagged; maintenance templates named are `{{subst:prod blp}}`, `{sdelete}` (sic — should be `{{db-…}}`), and `{{unreferenced}}`. Also: **do not place citations in the lead section** (`སྤྱིར་ཝེ་ཁེ་རྩོམ་ཡིག་གི་མགོ་སྟོད་ལ་ལུང་འདྲེན་འཇོག་སྲོལ་མེད་པ་རེད།`) — the lead is an intro + summary before the TOC. **Wikilinks are not reliable sources** (`ཝེ་ཁེ་རིག་མཛོད་དེ་ཉིད་ཀྱི་ནང་གི་ཡིག་ཆ་(Wikilinks)དེ་དག་ནི་བརྗོད་གཞི་ཞིག་གི་ཡིད་ཆེས་རུང་བའི་ཁུངས་དག་པོ་ཞིག་ཏུ་རྩི་བ་མིན།`).

Companion Google Doc: `https://docs.google.com/document/d/1AlNyCSSPbxplZDH8A1nNg3hGSVHvhifuTSQOdP_dyqk/edit`

---

## 9. Topic 295 — text-level (not term-level) article prompts

**Title:** 2.2 གཞུང་སྤྱིའི་ཝེ་ཁེ་ཤོག་ངོ་བཟོ་བྱེད་ཀྱི་བརྡ་སྟོན། · **Author:** `gade` · **Date:** 2025-06-09 (edited 2025-07-29)
URL: https://forum.openpecha.org/t/2-2/295

Five prompts for articles **about texts/collections**, not key terms — complementary to the main pipeline (a term article links to text articles). Explicitly **"usable in either Claude AI or Gemini AI"** (`བརྡ་སྟོན་འདིས་Claude AI འམ་ Gemini AI གང་རུང་དུ་བེད་སྤྱོད་བྱེད་ཐུབ།`), and the last one is **Gemini-specific**: `བརྡ་སྟོན་འདིས་Gemini AI འམ་ Gemini Studioགང་རུང་དུ་བེད་སྤྱོད་བྱེད་ཐུབ།`.

Stated weakness, relevant to context budgeting (verbatim): `བརྡ་སྟོན་འདིས་ངོ་སྤྲོད་བཟོ་བར་གཞུང་ཡོངས་རྫོགས་རིག་ནུས་ལ་སྤྲོད་དགོས་སྟབས་Claude AIགྱི་ཡར་འཇུག་ཚིག་ཁྱིམ་གྱི་ཡ་མཐའི་ཚད་གཞི་ལས་བརྒལ་ཏེ་བེད་སྤྱོད་བྱེད་ཐུབ་ཀྱི་མེད།` — "because this prompt requires giving the whole text to the AI, it cannot be used beyond Claude AI's maximum upload token limit." **This is the team's documented reason for preferring Gemini on whole-text tasks.**

The most developed one, **གཞུང་ངོ་སྤྲོད་ཀྱི་བརྡ་སྟོན་གསར་པ།** (verbatim opening + skeleton):

```
ཝེ་ཁེ་རིག་མཛོད་ཀྱི་རྩོམ་ཡིག་བཟོ་བསྐྲུན་བྱེད་པའི་བརྡ་སྟོན་(prompt)
༡། དམིགས་ཡུལ་གཙོ་བོ།
མཁོ་འདོན་བྱས་པའི་བོད་ཀྱི་གཞུང་ལུགས་དཔེ་ཆ་ «གཞུང་གི་མཚན་» ལ་དབྱེ་ཞིབ་གནད་སྨིན་བྱས་ཏེ། ཝེ་ཁེ་རིག་མཛོད་ཀྱི་ཚད་གཞི་དང་མཐུན་པའི་ངོ་སྤྲོད་རྩོམ་ཡིག་སྤུས་ལེགས་ཤིག་འབྲི་དགོས། རྩོམ་ཡིག་འདི་བོད་ཀྱི་རིག་གཞུང་དང་ནང་དོན་རིག་པར་དོན་གཉེར་ཡོད་པའི་ཀློག་པ་པོ་རྣམས་ལ་དམིགས་པ་ཡིན།
༢། འཇུག་རྒྱུའི་ཡིག་ཆ།
[འདིར་ «གཞུང་གི་མཚན་» ཞེས་པའི་ཡིག་ཆ་ཆ་ཚང་འགོད་དགོས།]
༣། ལས་འགན་གྱི་རིམ་པ་དང་རྩོམ་ཡིག་གི་གྲུབ་ཆ།
གཤམ་གསལ་གྲུབ་ཆ་དང་གོ་རིམ་ལྟར་རྩོམ་ཡིག་འདི་འབྲི་དགོས།
ཀ) ངོ་སྤྲོད་སྤྱི་བསྡུས། (Lead Section)
ཁ) གཞུང་གི་རྒྱུ་ཆ་ཞིབ་ཕྲ།
ག) གཞུང་གི་བརྗོད་བྱ་གཙོ་བོ།
ང) ཐུན་མོང་མ་ཡིན་པའི་ཁྱད་ཆོས།
ཅ) དཔྱད་གཞིའི་ཡིག་ཆ་དང་འབྲེལ་ཡོད་དྲ་ཐག
༤། འབྲི་རྩོམ་གྱི་ལམ་སྟོན།
བར་གནས་ཀྱི་འབྲི་རྩོམ། ཝེ་ཁེ་རིག་མཛོད་ཀྱི་སྒྲིག་སྲོལ་ལྟར། རྩོམ་ཡིག་དེ་ཕྱོགས་ལྷུང་མེད་པའི་བར་གནས་ཀྱི་འདུ་ཤེས་ཐོག་ནས་འབྲི་དགོས།
ཚིག་སྦྱོར་གསལ་བ། ཚིག་སྦྱོར་གོ་བདེ་ཞིང་གསལ་པོ། བོད་ཀྱི་བརྡ་སྤྲོད་དང་མཐུན་པ་ཞིག་དགོས།
ས་བཅད་ཀྱི་བཀོད་པ། རྩོམ་ཡིག་གི་ནང་དོན་སྒྲིག་རིམ་ལྡན་པ་ཡོང་ཆེད་འགོ་བརྗོད་དང་འགོ་བརྗོད་ཕྲན་བུ་བེད་སྤྱོད་བྱེད་དགོས།
```
It names **BDRC** and **སྡེ་དགེ་པར་མ། / གསེར་བྲིས་མ།** as the expected edition/link sources, and requires the TOC be emitted as a **Wikitable** (`དཀར་ཆག་འདི་རྣམས་Wikitableནང་དུ་བཅུག་རོགས།`), with volumes named `པོད་ཀ་པ། པོད་ཁ་པ།` and page numbers as `ཤོག་གྲངས། ༡༧`.

---

## 10. Topic 239 — editor charter (`ཝེ་ཁེ་རྩོམ་སྒྲིག་པའི་རྩ་འཛིན།`)

**Author:** Tashi_Dhondup · **Date:** 2025-05-16 (edited 2025-07-16) · URL: https://forum.openpecha.org/t/topic/239

Two rules matter for the repo design:

- **Role definition (verbatim):** `རང་ཉིད་ནི་འཐུས་སྒོ་ཚང་བའི་ཝེ་ཁེ་ཤོག་ངོས་གང་མང་བཟོ་མཁན་ཞིག་ལ་ངོས་འཛིན་མི་རུང་བར་རང་ཉིད་ནི་AI རིག་ནུས་ལ་ཝེ་ཁེ་ཤོག་ངོས་འཐུས་ཚང་བཟོ་བར་སློབ་སྟོན་བྱེད་མཁན་ནམ་སྦྱོང་བརྡར་སྤྲོད་ཐུབ་མཁན་ཞིག་ཡིན།` — "do not regard yourself as someone who produces many complete wiki pages; regard yourself as someone who instructs/trains the AI to produce complete wiki pages."
- **Prompt-versioning duty (verbatim):** `བརྡ་སྟོན་ཡར་རྒྱས་ཕྱིན་པ་བཞིན་དུ་བརྡ་སྟོན་གསར་པ་དེ་གླེང་སྟེགས་སུ་གསར་སྣོན་ངེས་པར་དུ་བྱེད་དགོས།` — "as prompts improve, the new prompt **must** be posted to the forum." This is why 289/236/260 each carry 3 versions.
- Key-term QC threshold restated: `འགྲེལ་བ་དག་ལས་ཚིག་འགྲེལ་མ་མཐར་ཚེག་ཁྱིམ་བཅུ་ལས་མང་དགོས།` (gloss must be **more than 10** ཚེག་བར) — **contradicts** topic 289 v3 which demands **fewer than 10**.
- Output readability target restated: `གཞི་རིམ་སློབ་མས་གོ་བའི་གནས་ཚད་དང་མཉམ་པ་ཞིག་འབྲི་དགོས།`
- Cadence: 2-week sprints, ≥80% completion.

---

## 11. Wiki-operations topics (345, 418, 420, 425, 475, 432, 231)

- **345** — *Move Tool* (Tsewang, 2025-07-08). Steps: page → Toolbar `Move` → namespace dropdown (`Main`/`Talk`/`Index`) → new title → reason → optional `Watch source page and target page` → `Go`. **Gate: account must be `autoconfirm` = ≥4 days old AND ≥10 edits.** Move fails if the target title already exists or the page is protected. https://forum.openpecha.org/t/how-to-change-the-page-name-title-in-wikisource-using-the-move-tool/345
- **418 / 420** — RfA on bo.wikipedia (Tsewang, 2025-07-31 / 2025-08-01; 420 is the Tibetan version). Nominator needs **≥500 edits**. RfA page: `bo.wikipedia.org/wiki/Wikipedia:བཀོད་འདོམས་པར་རེ་ཞུ`. Template block (verbatim): `=== [[User:example]] ===` / `Replace with RfA text ~~~~` / `''' འདེམས་ཐོན་ངོས་ལེན། Nomination Acceptance'''` / `''' རྒྱབ་སྐྱོར། Support'''` / `'''འགག་པ། Oppose'''` / `'''དཔྱད་བརྗོད། Comments'''`. Support votes start with `#` and end with `~~~~`. Minimum discussion **7 days**; small wikis may pass on 3–5 supports. Post lists members with >500 edits as of 2025-08-01: Pecha-Gade (503), Pecha-Alalamo (791), Tsethar Dolma (668), Sonam gyal (541), Rekong Rabten (680), Kalsumsingmo (1563), Pecha-Jampa Tennor (787), Pecha-Dhondup (959). https://forum.openpecha.org/t/how-to-nominate-someone-for-adminship-in-bo-wikipedia-and-how-to-display-your-support-to-the-nominated-candidate/418
- **425** — Commons: replace a wrongly-uploaded file rather than deleting (deletion takes hours–a day). Path: file page → `Upload a new version of this file` (just above `File usage on Commons`) → `Source file` → `Choose File` → `File Changes` reason (**write it in English — admins likely don't read Tibetan**) → `Upload file`. https://forum.openpecha.org/t/wikimedia-commons/425
- **475** — Support/oppose markup (himalayanna, 2025-09-22), verbatim: `* {{icon|support}} REPLACE THIS TEXT WITH YOUR NOTE OF SUPPORT -[[User:NAME|NAME]] ([[User talk:NAME|talk]]) ~~~~~` and the `{{icon|oppose}}` variant. Note **five** tildes. https://forum.openpecha.org/t/how-to-add-statements-of-support-opposition-to-a-discussion-in-wikimedia/475
- **432** — OpenRefine → Wikidata/Commons (Ganga_Gyatso, 2025-08-20). Reconciliation type QIDs given: Religious text **Q179461**, Buddhist temple **Q4414081**, Buddhist concept **Q25341675**, Buddhist term **Q86691240**. Schema properties: `instance of (P31)`, `language of work (P407)`, `author (P50)`, `inception (P571)`, `part of (P361)`; references `stated in (P248)`, `retrieved (P813)`, `reference URL (P854)`. Export path: `Export → QuickStatements v1` → https://quickstatements.toolforge.org/#/. Autoconfirmed for batch = >4 days + ≥50 edits. Commons PDF limit **100MB**. https://forum.openpecha.org/t/openrefine-for-wikimedia/432
- **206** — Wikidata modelling (Tashi_Dhondup + Elie_Roux, 2025-04-09). **No "commentary on"/"has commentary" properties exist.** Interim: `Derivative work (P4969)` for commentary→root, `Main subject (P921)` for root→commentary. Elie Roux (BDRC) endorses proposing the new properties and offered to back the proposal. https://forum.openpecha.org/t/representing-root-texts-and-commentaries-on-wikidata/206

---

## 12. Governance / targets (284, 329, 343, 408, 478)

- **Mission (284, verbatim):** *"Adding authentic Buddhist facts and texts to Wikipedia to make sure WeBuddhist, ChatGPT and other AIs answer questions about Buddhism and Buddhist texts correctly."* WG meets **Tuesdays 14:00 UTC**. GitHub board: https://github.com/orgs/OpenPecha/projects/118. The 2026 planning section asks for **BO, EN, ZH articles about keywords with sources** — i.e. multilingual output is on the roadmap, not just Tibetan.
- **Target (343 & 478):** by end of 2025 — **1000+ texts on Wikisource, 1000+ concepts on Wikipedia, 1000+ Wikidata entities.** Q3 2025 actual (478): "over 30 foundational texts" and "over 30 articles" — **a ~30× gap between actual and target, which is precisely the automation case for this repo.**
- **408** — the on-wiki project page (`Buddhist Knowledge from Tibetan Sources`, https://meta.wikimedia.org/wiki/Buddhist_Knowledge_from_Tibetan_Sources_Project). Sourcing rule: *"All contributions must be supported by Tibetan source texts **available on Wikisource** (original language texts preferred)."* Article tag: `{{Buddhist Knowledge from Tibetan Sources|class=|importance=}}`. Categories defined: `Category:Tibetan Buddhist Grammar / Logic / Medicine / Arts & Technology / Inner Science / Synonyms / Mathematics & Astrology / Drama / Poetry / Composition`. Explicit exclusion: **Political Issues**.
- **478** explicitly puts **"Developing NLP Models"** and **"Translation"** out of scope; automation/bot development is **in** scope.

---

## 13. Ground truth: what is actually deployed on bo.wikipedia

Verified live via `bo.wikipedia.org/w/api.php?action=query&prop=revisions&rvslots=main`.

**Article `སཏྭ་`** (13,308 bytes, last edited by **Pecha-Alalamo**, 2025-08-20):

```
[[Category:ནང་བསྟན།]]
'''སཏྭ་'''ནི་རྡོ་རྗེ་སེམས་དཔའི་སྔགས་བརྒྱ་པའི་ནང་གི་གནད་ཀྱི་ཚིག་ཅིག་ཡིན་ཏེ།…

== གོ་དོན། ==
== ངེས་ཚིག ==
== དབྱེ་བ། ==
== དགག་བཞག་རྩོད་སྤོང་། ==
== གཞུང་ལུགས་སོ་སོའི་བཤད་པ། ==
== འབྲེལ་ཡོད་བརྗོད་གཞི། ==
== ཁུངས། ==
<references>
</references>
```

**Critical divergences between the forum prompts and the deployed reality:**

| Aspect | Forum prompt says | Live article does |
|---|---|---|
| Related-pages heading | `==འབྲེལ་ཡོད་ཤོག་ངོས།==` (309, 324) | `== འབྲེལ་ཡོད་བརྗོད་གཞི། ==` |
| References heading | `==དཔེ་ཁུངས།==` (309) / `==ལུང་ཁུངས།==` (324) / `ལུང་ཁུངས` (260) | `== ཁུངས། ==` |
| Third tail section | `==དཔྱད་གཞིའི་ཡིག་ཆ།==` (324) | **absent** |
| Ref style | named refs `<ref name="…"/>` (309) or dummy links (324) | plain `<ref>[URL caption]</ref>`, **8 refs, zero named refs** |
| Ref URL | `wikisource.com` placeholder | real `wikisource.org/wiki/<pct-encoded title>` **with `#:~:text=` text-fragment anchors** pointing at the exact quoted Tibetan |
| Category | not mentioned in any prompt | `[[Category:ནང་བསྟན།]]` required |

**Article `སྲས་`** (12,649 bytes) uses a *third* ref format: `<ref>མཁན་པོ་ཀུན་དཔལ། སྤྱོད་འཇུག་གི་ཚིག་འགྲེལ་འཇམ་དབྱངས་བླ་མའི་ཞལ་ལུང་། ཤིང་དཔར།[https://wikisource.org/wiki/…/55#:~:text=… ]</ref>` — bibliographic data **outside** the link, page number encoded as the wikisource subpage `/55`. Sections: (lead), `== སྒྲ་བཤད། ==`, `== ངེས་ཚིག ==`, …

**The UPDATE path is already running manually.** `Pecha-Alalamo` contributions, March 2026, are exactly stage-4 edits on pipeline key terms:

| Date | Article | Δbytes | Edit summary |
|---|---|---|---|
| 2026-03-29 | ཀུན་ཏུ་ཡི་མུག་གྱུར། | +724 | ནང་དོན་སྙིང་བསྡུས་གསར་བཟོ་བྱས། |
| 2026-03-29 | མ་འཚལ། | +416 | གནད་ཚིག་གི་ནང་དོན་སྙིང་བསྡུས་གསར་བཟོ་བྱས་པ་ཡིན། |
| 2026-03-28 | སློབ་དཔོན། | +430 | ནང་དོན་སྙིང་བསྡུས་ཁ་སྣོན་བྱས། |
| 2026-03-28 | སྟོང་གསུམ། | +302 | ནང་དོན་བསྡུས་པ་བཟོས་ཡིན |
| 2026-03-28 | སྲས། | +625 | སྲས་ཞེས་པའི་གནད་ཚིག་འདིའི་སྙིང་བསྡུས་བཟོས་པ་ཡིན། |

Typical update delta = **300–750 bytes**, and the operation is consistently "add/create the lead summary (`ནང་དོན་སྙིང་བསྡུས`)" — i.e. articles were first published *without* a lead and the lead was backfilled. That matches guideline 319's "no citations in the lead" rule and prompt 324's rule ༣ (unheaded opening summary).

---

## Implementation implications

- **Use `https://forum.openpecha.org/raw/<topic_id>` as the ingestion endpoint for prompt provenance.** It is the only public endpoint returning un-rendered Markdown. Vendor topics 289, 236, 260, 309, 319, 324, 295, 239 into `prompts/` as versioned files with the topic id + post timestamp as provenance. Do not use `.json` (returns `cooked` HTML) and always follow 301s (slugs change: `prompt-sample` → `new-prompt-sample`).
- **Adopt the topic-223 four-stage decomposition as the repo's module boundary** (`select_terms/`, `align/`, `extract/`, `draft/`, `update/`), and reproduce its 👨‍💻/✨/😓 markers as a per-step `automation: code|llm|human` field so the semi-automatic hand-off points are explicit in code, not just docs.
- **Three prompts are specified and three are missing.** Ship 289-v3 (key terms), 236-v3 (alignment), 260 (drafting) as tested baselines; the repo must *author* prompts for step **2.2** (extract explanatory material per term), **3.1** (organize into sections), and **4.2** (compare-and-update existing article). Do not pretend these exist upstream.
- **Model routing is not uniform and must be configurable per stage.** 289 is documented as Claude-only (`Claude ai ཁོ་ནའི་ནང་ཚོད་བལྟ་བྱས`); 236 and 295 say Claude *or* Gemini; 309/324's worked output is specifically **Claude Opus 4** and the author warns Sonnet 4 gives different results. Since this project mandates Gemini, treat all three published prompts as **unvalidated on Gemini** and budget a re-tuning + eval pass; keep a `model:` field per prompt file.
- **Whole-text stages must go to Gemini for context reasons, per the team's own finding** (295: the introduce-a-text prompt "cannot be used beyond Claude AI's maximum upload token limit"). Route root+4-commentary alignment and whole-text summarization to a long-context Gemini model; use short-context calls for per-term drafting.
- **Resolve the two direct contradictions in the corpus before coding validators.** (a) Gloss length: 289-v3 says **<10 ཚེག་བར**, 289-v2 and 239 say **≥10**. (b) Sub-heading markup: 260-རབ་བརྟན rule #9 says `'''bold'''`, 260-ཡེ་ཤེས rule 3 says `==` for subheadings too. Pick one, encode it in a linter, and record the decision.
- **Do not copy the forum's wikitext examples literally — three are malformed.** Topic 309 writes `<reference>…</reference>` (must be `<references />`) and `[[url text]]` for external links (must be single-bracket `[url text]`); topic 260-5c has `</ref>…</ref>` for an opening tag. A wikitext validator (parse before publish, reject unbalanced `<ref>`/`<references>`) is mandatory, not optional.
- **Take section names from the live wiki, not from the prompts.** Deployed articles use `== འབྲེལ་ཡོད་བརྗོད་གཞི། ==` and `== ཁུངས། ==`; the prompts say `འབྲེལ་ཡོད་ཤོག་ངོས།` / `དཔེ་ཁུངས།` / `ལུང་ཁུངས།` / `དཔྱད་གཞིའི་ཡིག་ཆ།`. Define one canonical section schema in the repo (suggest: lead → `གོ་དོན།` → `ངེས་ཚིག` → `སྒྲ་བཤད།` → `དབྱེ་བ།` → `མཚན་ཉིད།` → `དགག་བཞག་རྩོད་སྤོང་།` → `གཞུང་ལུགས་སོ་སོའི་བཤད་པ།` → `བསྡུས་དོན།` → `འབྲེལ་ཡོད་བརྗོད་གཞི།` → `ཁུངས།`) and make the drafting prompt emit exactly that, with 260 rule #10's ban on inventing new sections enforced by a validator.
- **Standardize on one citation form and normalize the three in the wild.** Recommend the deployed `སྲས་` form — `<ref>author. work. edition.[https://wikisource.org/wiki/<title>/<page>#:~:text=<encoded quote> ]</ref>` — because the `#:~:text=` fragment makes every citation independently verifiable, which is the project's whole point. Generate the fragment programmatically from the quoted string the LLM returns; this directly automates the manual step Tsewang flagged as missing in topic 324 post #3.
- **Make the LLM emit a `dummy.com` placeholder link per ref (324 rule 14) and resolve it in a separate deterministic pass.** Do not ask the model for URLs. The resolver should search bo.wikisource/wikisource.org for the source title, locate the quoted Tibetan string, and emit the subpage + text fragment; refs it cannot resolve get flagged for human QC rather than silently dropped.
- **Enforce the hard output constraints as post-generation checks, not prompt hopes:** Tibetan script and **Tibetan numerals only** (324 rule 11 — reject any ASCII digit or Latin letter in article body); every quotation inside `"` or `'''`; sentence-final `། །`; every section heading followed by a shad; wikilinks as `[[term་]]` with trailing tsheg and **no** shad (324 rule 8); `[[Category:ནང་བསྟན།]]` present; no `<ref>` in the lead (319).
- **Reading level is a spec, not a preference:** 260 rules #25/#9 and 239 both require output comprehensible to `གཞི་རིམ་སློབ་མ` (a basic-level student). Add this to the drafting prompt and to the QC rubric.
- **Term-extraction gate is a hard join:** a candidate term is valid only if it appears **verbatim in the root** *and* has a gloss in the commentary; length 3–4 ཚེག་བར; no truncated prefixes. This is checkable in code against the aligned segments — do it deterministically after the LLM proposes candidates, rather than trusting rule-following. Default N=20 per text (289-v3).
- **The aligner must be lossless and must emit an explicit null.** 236-v3 requires "not one word may be omitted" and literal `འགྲེལ་བཤད་མེད།` when a commentary is silent on a śloka. Represent alignment as `{sloka_id, root_text, commentaries: {name: text | null}}` and add a coverage assertion (concatenated extracted spans ≈ commentary length) to catch the documented summarization failure mode.
- **Existence check before create-vs-update is already solved by the team's red-link convention** (309) — implement it as `action=query&titles=<term>&prop=info` on bo.wikipedia rather than scraping link colors. For the update path, the observed real-world edit is a **+300–750 byte lead/summary insert**, so build stage 4 around section-level diff-and-merge (append new cited sentences, add a `<ref>` to an existing sentence when the claim duplicates), not whole-page replacement.
- **Publishing needs `action=edit` via MediaWiki API with a bot/OAuth identity, and account gating is real:** page moves need autoconfirmed (≥4 days, ≥10 edits), Wikidata batch needs ≥50 edits, RfA nomination needs ≥500 edits. Plan the bot account's warm-up, set a descriptive edit summary in Tibetan matching the team's style (`ནང་དོན་སྙིང་བསྡུས་གསར་བཟོ་བྱས།`), and default to a human-approval queue before any write — the whole workflow is explicitly *semi*-automatic.
- **Model root↔commentary in Wikidata with the documented interim properties** (`P4969` derivative work, `P921` main subject), not with a "commentary on" property — it does not exist (topic 206). Leave a TODO hook for the proposed property, since Elie Roux/BDRC agreed to back the proposal.
- **Wikisource availability is a hard precondition for a term article** (408: all contributions must be backed by Tibetan source texts *available on Wikisource*). The repo should refuse to draft an article whose commentaries aren't yet on Wikisource, or emit them to an "upload first" queue — otherwise the citation resolver will have nothing to point at.
- **Ignore forum topics 237 and 262** — they are empty placeholders despite carrying pipeline-looking section numbers (`2.2`), and treating them as specs will produce a phantom stage.
- **Scale target sets the throughput requirement:** 1000+ concepts vs. ~30 delivered in Q3 2025. Design for batch runs over a text's full 20-term set with resumable state and a QC queue, and instrument cost/latency per term — the IATS paper's headline result is most likely "N articles at M cost with human QC rate R", so capture those metrics from day one.