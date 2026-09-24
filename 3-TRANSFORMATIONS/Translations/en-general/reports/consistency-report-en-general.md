## Praise to the Twenty-One Taras — Consistency Report (general grade)

Measured 2026-09-24 across four versions of the English:

| Version | File |
|---|---|
| D0 | `3-TRANSFORMATIONS/Translations/Dharmamitra/en/…-en.md` — DharmaMitra zero-shot |
| D1 | `3-TRANSFORMATIONS/Translations/Dharmamitra/en-general/…-en.md` — DharmaMitra with the glossary hint |
| D2 | grade file `en_text` — after the locked-term pass |
| D3 | `3-TRANSFORMATIONS/Translations/en-general/…-en-general.md` — after the fact-check and your decisions |

### Summary

| | D0 | D1 | D2 | D3 |
|---|---|---|---|---|
| Locked-term adherence | 78.7% | 86.9% | 99.2% | 100.0% |
| Repeated words with more than one spelling (of 8 tracked) | 1 | 2 | 0 | 0 |
| Distinct Tibetan words merged into one English word (of 3 groups) | 2 | 1 | 1 | 0 |

**In plain terms:** DharmaMitra was already fairly consistent with itself — it mostly
used one spelling per word, just not the spelling we chose. Its real consistency
problems were (1) the tuttare/hum mantra spellings wandering from verse to verse, and
(2) three different Tibetan words (ནུས, དབང, མཐུ) all coming out as "power", with
the zero-shot draft also using "spirits" for both འབྱུང་པོ and གདོན. The glossary hint
helped a little (D0 → D1: +10 terms). The locked-term pass did most of the
work (D1 → D2: +15). The fact-check didn't break any locked term, and closed
the last gap — "might" for མཐུ (D2 → D3: +1).

### 1. Locked-term adherence

For each verse, the grade file lists the Tibetan words the termbase locks and their
required English. A pair counts as a hit when that English appears in the verse
(ignoring capitalisation, a leading "the", and ordinary endings such as -s, -ing and
-er). Spelling and diacritics must match exactly, so "Tārā" is not "Tara" and "HŪṂ"
is not "hum". 122 pairs are scored; 5 are excluded because another, longer locked
phrase in the same line covers them (for example "Tara" inside the Sanskrit title in
I-1, and "the Blessed Tārā" in a-1).

| Version | Hits | Adherence | Misses |
|---|---|---|---|
| D0 — DharmaMitra zero-shot | 96/122 | 78.7% | 26 |
| D1 — DharmaMitra + glossary | 106/122 | 86.9% | 16 |
| D2 — termbase pass | 121/122 | 99.2% | 1 |
| D3 — fact-checked (current) | 122/122 | 100.0% | 0 |

Misses by version:
- **D0:** 1-1 Tara, 1-10 tuttare, 1-11 ability, 1-11 hum, 1-11 the syllable hum, 1-14 hum, 1-14 the syllable hum, 1-16 hum, 1-17 hum, 1-18 phat, 1-19 joy, 1-20 tuttare, 1-21 demons, 1-21 might, 1-21 vetāla, 1-21 yaksas, 1-5 hum, 1-5 tuttare, 1-6 vetāla, 1-6 yaksas, 1-7 phat, 1-7 trat, 2-5 demons, I-2 Tara, I-3 Tara, a-1 the Blessed Tārā
- **D1:** 1-1 Tara, 1-11 ability, 1-14 hum, 1-14 the syllable hum, 1-16 hum, 1-17 hum, 1-20 tuttare, 1-21 might, 1-21 vetāla, 1-21 yaksas, 1-5 hum, 1-5 tuttare, 1-6 vetāla, 1-6 yaksas, I-2 Tara, I-3 Tara
- **D2:** 1-21 might
- **D3:** none

### 2. Drift — spellings per repeated Tibetan word

For each Tibetan word that recurs, the different English forms used across its verses
(capitalisation ignored — "Ture" is deliberately capitalised where she is addressed).
1 = fully consistent.

| Word | D0 | D1 | D2 | D3 |
|---|---|---|---|---|
| Tara | 1 — tārā ×3 | 1 — tārā ×3 | 1 — tara ×3 | 1 — tara ×3 |
| hum | 1 — hūṃ ×5 | 2 — hūṃ ×4, hum ×1 | 1 — hum ×5 | 1 — hum ×5 |
| tuttare | 2 — tuttāra ×1, tuttāre ×2 | 3 — tuttāra ×1, tuttare ×1, tuttāre ×1 | 1 — tuttare ×3 | 1 — tuttare ×3 |
| ture | 1 — ture ×3 | 1 — ture ×3 | 1 — ture ×3 | 1 — ture ×3 |
| phat | 1 — phaṭ ×2 | 1 — phat ×2 | 1 — phat ×2 | 1 — phat ×2 |
| yaksha | 1 — yakṣas ×2 | 1 — yakṣas ×2 | 1 — yaksas ×2 | 1 — yaksas ×2 |
| vetāla | 1 — zombies ×2 | 1 — zombies ×2 | 1 — vetālas ×2 | 1 — vetālas ×2 |
| demon (གདོན) | 1 — spirits ×2 | 1 — demons ×2 | 1 — demons ×2 | 1 — demons ×2 |

### 3. Distinctions — different Tibetan words kept apart

| Tibetan words (locked English) | D0 | D1 | D2 | D3 |
|---|---|---|---|---|
| ནུས / དབང / མཐུ (ability / power / might) | ❌ power / power / power | ❌ power / power / power | ❌ ability / power / power | ✅ ability / power / might |
| འབྱུང་པོ / གདོན (spirits / demons) | ❌ spirits / spirits | ✅ spirits / demons | ✅ spirits / demons | ✅ spirits / demons |
| བཅོམ་ལྡན་འདས་མ / ལྷ་མོ (Blessed One / goddess) | ✅ blessed / goddess | ✅ blessed / goddess | ✅ blessed / goddess | ✅ blessed / goddess |

### Caveats

- The yardstick is our own termbase, which D2 and D3 were edited to follow, so their
  high scores are expected. What the numbers show is how far DharmaMitra was from the
  locked vocabulary, that the enforcement took, and that the fact-check didn't
  undo it.
- The termbase was built from D0's own English keywords, so D0 starts high partly by
  construction. Its misses are exactly where we deliberately chose differently.
- Only the 8 words whose forms can be listed reliably (names, mantra syllables,
  classes of beings) are counted in section 2. Common words (light, moon, world, joy)
  are covered by section 1 only.
- This measures consistency, not correctness. Correctness is what the commentary
  fact-check covered.
