# Claims-consolidation pilot — audit findings (2026-08-07, unfixed)

Retrospective adversarial audit of the three pilot topic pages (one fresh agent per
page, every citation checked against `2-RAILS/Claims/raw/tree-guided/`). **418 unique
citations, zero fabricated claim IDs.** Per the human contributor's decision the pages
were left unfixed; the effort went into guardrails instead (`claims-consolidation`
Rules 9–16 + two verification gates). **Fix this list before any transformation
consumes these pages.** Deterministic findings are also independently reproducible:
`python3 4-SYSTEM/Skills/claims-consolidation/verify_consolidation.py <page>`.

---

## tara-02.md — 70/78 verified, 1 CRITICAL

1. **CRITICAL — `gendun-gyatso:c-1-2-1` (Face section).** Cited as independently
   corroborating anon-trinle-char's "three flaws" framing (dust, mist/haze, cloud).
   The raw claim contains no flaws framing — only "face supremely white and beautiful
   like stacked full autumn moons." Correct attestation is almost certainly
   `gendun-drub:c-2-2-2-2-1-1-1-3` (clouds, mist, dust) or
   `anon-utpala:c-1-2-2-1-1-1-5` (dust-clouds, sheep-wool clouds).
2. **Moderate — `tsultrim-namdak:c-3-5` (Implements ⚑).** Credited with the full
   simple-form scheme (one face, two hands, supreme-giving mudrā). Raw claim attests
   only: white body, utpala with HRĪḤ-marked mirror, wisdom-light activity. The
   mudrā/face-count detail belongs to palden-sherab and sangye-nyentrul only.
3. Minor — `anon-trinle-char:c-3-2-6` cited under Light reading 1 ("surpasses") when
   it explicitly *rejects* that reading (it belongs with reading 3 only).
4. Minor — `anon-trinle-char:c-3-2-7` (Colour ⚑): page says three masters "all
   describe her as white"; only Nyima Sbaspa's quote does; Drakpa Shedrub's cited
   name has no colour term.
5. Minor — `anon-trinle-char:c-3-2-11`: "Nyima Sepa's sādhana" — raw says only
   "Nyima Sbaspa states"; no sādhana named.
6. Minor — `taranatha:c-2-7` (Doctrinal consensus): "bliss-emptiness wisdom" and
   "central-channel cakras" are palden-sherab-only; taranatha has neither.
7. Minor — Implements arithmetic: "nine of sixteen give no hand detail" → correct
   figure is **twelve**.
8. Minor — Light ⚑ omission: the "adorned by" (བརྒྱན་པ) reading is attested
   in-corpus by `gendun-gyatso:c-1-2-2` and `tenzin-dhonzang:c-4-2-4`, but presented
   only as anon-trinle-char's report of unnamed others; the blanket "all sixteen"
   Light consensus flattens this.
- Quote mismatches: `gendun-drub:c-2-2-2-2-1-1-1-4` "བརྒྱད་གཉིས་སྒྲིགས" → raw
  བརྒྱད་གཉིས་**པ་**སྒྲིགས; `tenzin-dhonzang:c-4-2-8` "ལེགས་བྲི་མ" → raw ལེགས་བྲི**ས་**མ;
  `palden-sherab:c-3-1-2-2-1` དཀོན་མཆོག་ → raw spells དཀོན་**ཅོག་**;
  `palden-sherab:c-3-1-2-1-2` name ends ལྷ་མོ, not མ.
- Coverage rows for sangye-nyentrul and tsultrim-namdak mislabel their Name
  contribution as "Consensus" when both attest the *divergent* name Dbyangs-can-ma.
- Typo: "Svift Heroine" (line ~63).

## tara-01.md — 140/143 verified, 0 critical

1. Moderate — `sangye-nyentrul:c-2-1-1` cited under the knowledge/love/power
   framework Consensus; the raw claim ("increases bodhicitta and draws appearances
   under control") has no connection to that framework. With it removed, the
   framework rests on **2** commentaries (anon-trinle-char, taranatha), not the
   labeled 5 — the section's breadth is meaningfully overstated.
2. Minor — `tsultrim-namdak:c-2-1-2-1-4` listed in the "Tārā" etymology-proper list;
   it etymologizes Swift/Heroine, not "Tārā" (correctly cited elsewhere).
3. Minor — `anon-trinle-char:c-3-1-4` cited as Pamo etymological reasoning; it is a
   generic three-greatnesses framing (the reasoning is c-3-1-10/11).
4. Count labels (all recomputable by the script): etymology-proper "(11)"→10,
   Pamo "(13)"→12, Wisdom-Eyes "(12)"→11, lotus-seat "(4)"→3, Quality-Framework
   "(5)"→3 cited / 2 solid.
5. Raw-file flag for a human: `tenzin-dhonzang:c-4-1-3`'s own quoted Tibetan reads
   མྱུར་མ་**དཔལ་མོ** against the same commentary's c-4-1-2/c-4-1-6 (དཔའ་མོ) — likely
   transcription artifact, but it weakens the page's "no other commentary attests
   [Dpal-mo]" statement; check the source.
6. Low-confidence lead: `anon-utpala:c-1-2-1-1` may be a third attestation of the
   "praise by way of history" classification (page credits two).

## benefits.md — ~195/197 verified, 0 critical

1. Minor (most systematic) — Timing consensus bundles "recite at dusk/dawn" +
   "wrathful at dusk / peaceful at dawn"; 7 of its 11 attestations
   (`konchok-thabkhe:c-3-3`, `palden-sherab:c-3-2-1-1`, `c-3-2-1-2`,
   `pema-namgyal:c-3-1`, `taranatha:c-22-1-12`, `tsultrim-namdak:c-8-5`,
   `sungrab-tulku:c-2-7`) support only the timing. The pairing has 6 real attesters.
2. Minor — Spang Lo Position 2: "of day and night" frame is Bu ston's (Position 3),
   not in `gendun-drub:c-2-2-3-4-3`.
3. Minor — `karma-maitri:c-1-2-15` folded into the 7×7=49 Position 5; its own gloss
   says only "cycles of seven" — the arithmetic is explicit only in
   `gendun-gyatso:c-2-6`.
4. Trivial — `gendun-gyatso:c-2-1` "endorsed by the author" → raw is a tentative
   སྙམ་མོ ("likely correct, I think").
5. Trivial — gendun-drub allegorical poison: `c-2-2-3-3-2`'s "wrong view" (ལོག་ལྟ)
   term dropped from the joint gloss.
6. Trivial — Structure consensus four part-labels are verbatim only for drakpa and
   gendun-drub; `tenga-tulku:c-1-3-1` uses variant wording.
7. Trivial — `sungrab-tulku:c-2-12`: "empowered **into** Mother Prajñāpāramitā";
   "three times" detail is in uncited `c-2-11`.
- Quote mismatch: `gendun-drub:c-2-2-3-2-2` — མལ་ནས་ ("from bed") silently dropped
  mid-quote (translation keeps it).
- Undispositioned (in Coverage, no disposition anywhere): `taranatha:c-22-1-26`,
  `c-22-1-28`, `c-22-1-32`, and `tsultrim-namdak:c-8-4` (the last found by the
  script, missed by the human audit).

---

Verified clean everywhere: all ⚑ divergence positions sit in their cited claims under
the right authorities (incl. the five-position recitation-count divergence and the
Pamo/Dpal-mo split); the dusk-wrathful/dawn-peaceful pairing is never reversed; all
28 tsultrim-namdak narrative rows match; all "reviewed, not separately cited" reasons
are accurate on all three pages.
