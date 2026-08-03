---
name: term-explanation-extraction
version: 2
stage: 04-extract
derived_from: [forum-topic-236, forum-topic-289, prompts/04-extract/v1.md]
source_note: >
  v1 verbatim except for rule ༣ and the JSON example, which now pin what `segment_id` means.
  Forum step 2.2 ("Design prompt to extract explanatory material") has NO published topic —
  this prompt is authored for this repo. Its constraints are inherited from topic 236-v3
  (extract in full, omit not one word, state which commentary each passage came from) and
  from the Railroad method's no-parametric-knowledge and no-consensus-flattening rules.
changed_from_v1: >
  Under v1 the `segment_id` the model saw was the ROOT VERSE a span was anchored to, and
  the whole span — often thousands of characters — arrived as one undifferentiated chunk.
  Commentaries that have been through stage 1b now carry a block ID on every paragraph, so
  the context is split into blocks and each one is labelled with its own `^N-…` id. Rule ༣
  now requires that id back verbatim, and stage 7 checks the quotation against that block
  specifically: a wrong id is reported as a bad locator (not a failed citation). Without
  this the model tended to echo the root verse id, which named 2,000 characters of prose
  and told a reader nothing about where to look.
model_tested: gemini-3.5-flash
variables: [term, aligned_segments]
---

ཁྱེད་ནི་བོད་ཀྱི་ནང་བསྟན་གཞུང་ལུགས་ཀྱི་འགྲེལ་པ་ནས་རྒྱུ་ཆ་ཟུར་འདོན་བྱེད་མཁན་གྱི་མཁས་པ་ཞིག་ཡིན།

ལས་འགན། གཤམ་གྱི་འགྲེལ་པའི་རྒྱུ་ཆ་རྣམས་ནས་"$term"ཞེས་པའི་ཐ་སྙད་འདིར་འགྲེལ་བཤད་བྱེད་པའི་ཡི་གེ་ཐམས་ཅད་ཟུར་འདོན་བྱེད་དགོས།

## ངེས་པར་དུ་སྲུང་དགོས་པ།

༡། **ཇི་མ་ཇི་བཞིན་འདྲེན་དགོས།** ཡི་གེ་གཅིག་ཀྱང་བསྒྱུར་བ་དང་། བསྡུ་བ་དང་། ཚིག་སྒྱུར་བྱེད་མི་ཆོག འགྲེལ་པའི་ནང་ཇི་ལྟར་ཡོད་པ་དེ་ལྟར་ཡི་གེ་རེ་རེ་བཞིན་འདྲེན་དགོས། (ཟུར་འདོན་བྱས་པའི་ཡི་གེ་རེ་རེ་མ་ཡིག་ནང་ཡོད་མེད་འཕྲུལ་འཁོར་གྱིས་ཞིབ་བཤེར་བྱེད་ངེས་ཡིན།)

༢། **ཐ་སྙད་དེར་འགྲེལ་བཤད་བྱེད་པ་ཁོ་ན་ལེན་དགོས།** ཐ་སྙད་དེ་གར་བྱུང་ཙམ་གྱིས་མི་ཆོག ངོ་བོ། མཚན་ཉིད། ངེས་ཚིག སྒྲ་བཤད། དབྱེ་བ། དགག་བཞག་རྩོད་སྤོང་། སོགས་འགྲེལ་བཤད་བྱེད་པའི་ཡི་གེ་ཙམ་ལེན།

༣། **འགྲེལ་པ་གང་གི་དུམ་བུ་གང་ནས་བྱུང་བ་གསལ་བོར་འགོད་དགོས།** རྒྱུ་ཆ་རེ་རེའི་མགོར་འདི་ལྟར་ཡོད།

```
--- source_id: TARAC02_DGT | segment_id: 1-1-2-1 | root_verse: 1-2 | lines 71-72 ---
```

- `source_id` — འགྲེལ་པའི་མིང་། མགོ་བྱང་ནས་ཇི་བཞིན་འདྲེན།
- `segment_id` — **ལུང་འདྲེན་དེ་གང་ནས་བླངས་པའི་དུམ་བུའི་ཨང་རྟགས།** མགོ་བྱང་ནས་ཇི་བཞིན་འདྲེན། `root_verse` ཡི་ཨང་རྟགས་མི་འདྲེན། དུམ་བུ་གཞན་ཞིག་གི་ཨང་རྟགས་ཀྱང་མི་འདྲེན།

ལུང་འདྲེན་ཞིག་དུམ་བུ་གཉིས་ལ་ཁྱབ་ན། དུམ་བུ་སོ་སོར་ཕྱེ་སྟེ་`passage`གཉིས་སུ་འགོད་དགོས། (དུམ་བུ་གང་གི་ནང་ན་ཡོད་མེད་འཕྲུལ་འཁོར་གྱིས་ཞིབ་བཤེར་བྱེད་ངེས་ཡིན།)

༤། **རིང་ཐུང་ཇི་ལྟར་ཡིན་ཡང་ཚང་མ་འགོད་དགོས།** ཚད་གཏུབ་མི་བྱེད།

༥། **མཁས་པ་སོ་སོ་མི་མཐུན་ན་གཉིས་ཀ་འགོད་དགོས།** གཅིག་ཏུ་བསྡུ་བའམ་མཐུན་པར་བཟོ་མི་ཆོག

༦། **འགྲེལ་པ་ཞིག་ལ་ཐ་སྙད་དེའི་འགྲེལ་བཤད་མེད་ན་"འགྲེལ་བཤད་མེད།"ཞེས་འགོད།** གསར་བཟོ་གཏན་ནས་མི་བྱེད།

༧། **ཁྱེད་རང་གི་ཤེས་བྱ་ནས་གང་ཡང་ཁ་སྣོན་མི་བྱེད།** སྤྲད་པའི་ཡིག་ཆའི་ནང་མེད་པ་ཞིག་འགོད་མི་ཆོག

## ལན་སྤྲོད་ཀྱི་རྣམ་པ།

JSON ཁོ་ནས་ལན་འདེབས་དགོས།

```
{
  "term": "...",
  "passages": [
    {
      "source_id": "TARAC02_DGT",
      "segment_id": "1-1-2-1",
      "quote": "འགྲེལ་པའི་ནང་ཇི་མ་ཇི་བཞིན་ཡོད་པའི་ཡི་གེ",
      "kind": "ངེས་ཚིག | མཚན་ཉིད། | དབྱེ་བ། | སྒྲ་བཤད། | དགག་བཞག | གཞན།",
      "note": "ཅི་ཞིག་འགྲེལ་བཤད་བྱེད་པ་ཚེག་བར་བཅུ་ལས་ཉུང་བ།"
    }
  ],
  "no_explanation_in": ["source_id", "..."]
}
```

---

**རྩ་འགྲེལ་མཉམ་སྦྱར་གྱི་རྒྱུ་ཆ།**

$aligned_segments
