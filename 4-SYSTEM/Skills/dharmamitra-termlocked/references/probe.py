#!/usr/bin/env python3
"""A/B probe: does DharmaMitra cat-translate honour a locked glossary,
and does injection position (context vs style_instruction) matter?

Four arms per block, identical otherwise:
  A control  — no glossary anywhere
  B context  — glossary in `context` (what dm_translate.py does today)
  C style    — glossary appended to `style_instruction`
  D both     — glossary in both
"""
import json, sys, time, urllib.request, urllib.error

ENDPOINT = "https://dharmamitra.org/api-search/cat-translate/v1/translate"
HEADER = ("A canonical Tibetan Buddhist text, translated block by block from the "
          "critical edition in this vault. The blocks below are being translated in order.")
STYLE = ("Translate this Tibetan verse of praise line by line: render each Tibetan line as "
         "one line of the target language, in the same order, and keep the same number of "
         "lines as the source. Devotional but clear register. Keep mantra syllables and "
         "proper names in transliteration rather than translating them. Do not add "
         "commentary, notes, or explanation.")

BLOCKS = {
 "1-3": "ཕྱག་འཚལ་གསེར་སྔོ་ཆུ་ནས་སྐྱེས་ཀྱི། །\nཔདྨས་ཕྱག་ནི་རྣམ་པར་བརྒྱན་མ། །\nསྦྱིན་པ་བརྩོན་འགྲུས་དཀའ་ཐུབ་ཞི་བ། །\nབཟོད་པ་བསམ་གཏན་སྤྱོད་ཡུལ་ཉིད་མ། །",
 "1-4": "ཕྱག་འཚལ་དེ་བཞིན་གཤེགས་པའི་གཙུག་ཏོར། །\nམཐའ་ཡས་རྣམ་པར་རྒྱལ་བར་སྤྱོད་མ། །\nམ་ལུས་ཕ་རོལ་ཕྱིན་པ་ཐོབ་པའི། །\nརྒྱལ་བའི་སྲས་ཀྱིས་ཤིན་ཏུ་བསྟེན་མ། །",
 "1-6": "ཕྱག་འཚལ་བརྒྱ་བྱིན་མེ་ལྷ་ཚངས་པ། །\nརླུང་ལྷ་སྣ་ཚོགས་དབང་ཕྱུག་མཆོད་མ། །\nའབྱུང་པོ་རོ་ལངས་དྲི་ཟ་རྣམས་དང་། །\nགནོད་སྦྱིན་ཚོགས་ཀྱིས་མདུན་ནས་བསྟོད་མ། །",
}

# Locked renderings deliberately DIFFERENT from the zero-shot baseline,
# so any effect is mechanically detectable.
GLOSS = {
 "1-3": [("དཀའ་ཐུབ་", "ascetic discipline"), ("བསམ་གཏན་", "dhyāna"),
         ("བརྩོན་འགྲུས་", "perseverance"), ("བཟོད་པ་", "forbearance")],
 "1-4": [("རྒྱལ་བའི་སྲས་", "bodhisattvas"), ("ཕ་རོལ་ཕྱིན་པ་", "pāramitās"),
         ("གཙུག་ཏོར་", "uṣṇīṣa")],
 "1-6": [("རོ་ལངས་", "vetālas"), ("འབྱུང་པོ་", "bhūtas"),
         ("དབང་ཕྱུག་", "Īśvara"), ("གནོད་སྦྱིན་", "yakṣas")],
}
EXPECT = {k: [t for _, t in v] for k, v in GLOSS.items()}


def gloss_lines(bid):
    return "\n".join(f"{s} → {t}" for s, t in GLOSS[bid])


def body_for(arm, bid):
    ctx, style = HEADER, STYLE
    g = gloss_lines(bid)
    if arm in ("B", "D"):
        ctx = HEADER + "\n\nTerminology already fixed for this text:\n" + g
    if arm in ("C", "D"):
        style = STYLE + (
            "\n\nUse exactly these renderings for these Tibetan terms, without "
            "substituting synonyms:\n" + g)
    b = {"input_tibetan": BLOCKS[bid], "input_chinese": "", "input_pali": "",
         "input_sanskrit": "", "context": ctx, "focus": "tibetan",
         "target_language": "english", "style_instruction": style}
    return b


def call(body, retries=4):
    data = json.dumps(body, ensure_ascii=False).encode()
    for a in range(retries):
        req = urllib.request.Request(ENDPOINT, data=data, method="POST",
              headers={"Content-Type": "application/json", "Accept": "application/json"})
        try:
            with urllib.request.urlopen(req, timeout=90) as r:
                return json.loads(r.read().decode()).get("translation", "").strip()
        except urllib.error.HTTPError as e:
            if e.code == 429:
                w = 20 * (a + 1)
                print(f"    429 → sleep {w}s", file=sys.stderr); time.sleep(w); continue
            return f"<HTTP {e.code}>"
        except Exception as e:  # noqa: BLE001
            return f"<ERR {type(e).__name__}: {e}>"
    return "<gave up after 429s>"


out = {}
for bid in BLOCKS:
    out[bid] = {}
    for arm in ("A", "B", "C", "D"):
        t = call(body_for(arm, bid))
        hits = [e for e in EXPECT[bid] if e.lower() in t.lower()]
        out[bid][arm] = {"translation": t, "hits": hits,
                         "score": f"{len(hits)}/{len(EXPECT[bid])}"}
        print(f"[{bid} arm {arm}] {len(hits)}/{len(EXPECT[bid])} {hits}", flush=True)
        time.sleep(6)

print(json.dumps(out, ensure_ascii=False, indent=2))
