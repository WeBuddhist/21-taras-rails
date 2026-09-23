# Does DharmaMitra honour a locked glossary? — probe, 2026-09-22

The question `dharmamitra-termlocked` is built on. Recorded here so the design can be
re-argued against evidence rather than re-guessed, and re-run when the endpoint changes.

- **Endpoint:** `POST https://dharmamitra.org/api-search/cat-translate/v1/translate`
- **Text:** `1-SOURCES/Text/bo-སྒྲོལ་མ་ཉེར་གཅིག་ལ་བསྟོད་པ།.md`, blocks `^1-3`, `^1-4`, `^1-6`
- **Style / context header:** this vault's committed `Dharmamitra/en/{style,context-header}.md`,
  verbatim, so the control arm reproduces the real baseline run's conditions
- **Rolling context:** none, so the only variable is the glossary
- **Script:** `probe.py` in this folder (run 1; run 2 is the batched variant described below)

## Design

Eleven locked renderings, **deliberately chosen to differ from what the zero-shot run
produces**, so that any effect is mechanically detectable rather than a judgment call:

| Block | Locked | (zero-shot baseline says) |
|---|---|---|
| `1-3` | དཀའ་ཐུབ་ → ascetic discipline · བསམ་གཏན་ → dhyāna · བརྩོན་འགྲུས་ → perseverance · བཟོད་པ་ → forbearance | austerity · meditative concentration · diligence · patience |
| `1-4` | རྒྱལ་བའི་སྲས་ → bodhisattvas · ཕ་རོལ་ཕྱིན་པ་ → pāramitās · གཙུག་ཏོར་ → uṣṇīṣa | children of the Victors · perfection · Uṣṇīṣa |
| `1-6` | རོ་ལངས་ → vetālas · འབྱུང་པོ་ → bhūtas · དབང་ཕྱུག་ → Īśvara · གནོད་སྦྱིན་ → yakṣas | Zombies · spirits · Īśvaras · yakṣas |

Four arms, identical but for where the glossary goes:

| Arm | Glossary in `context` | Glossary in `style_instruction` |
|---|---|---|
| A control | — | — |
| B | ✓ | — |
| C | — | ✓ |
| D | ✓ | ✓ |

## Results

**Run 1 — solo calls (one block per call), 12 calls**

| Block | A control | B context | C style | D both |
|---|---|---|---|---|
| `1-3` | 0/4 | 4/4 | 4/4 | 4/4 |
| `1-4` | 1/3 | 2/3 | 2/3 | 2/3 |
| `1-6` | 4/4 | 4/4 | 4/4 | 4/4 |
| **total** | **5/11** | **10/11** | **10/11** | **10/11** |

**Run 2 — one batched call for all three blocks, `[[1]]`–`[[3]]` markers, 3 calls**

| Arm | Locks landed | Markers returned |
|---|---|---|
| A control | 3/11 | `[[1]] [[2]] [[3]]` ✓ |
| B context | **10/11** | `[[1]] [[2]] [[3]]` ✓ |
| D both | **10/11** | `[[1]] [[2]] [[3]]` ✓ |

The one miss in every glossed arm of both runs is the same: locked `pāramitās` came back
as `pāramitā`.

## Conclusions

1. **The glossary works, and works harder under batching.** Batched control 3/11 → 10/11.
   Batching is where a zero-shot run's vocabulary drifts most, so it is where locking pays.
2. **Batching is safe.** Markers survived every glossed arm; `--batch 1` is not required,
   and forcing it would triple the call cost for nothing.
3. **Position is irrelevant.** B, C and D are indistinguishable. Use the existing `context`
   path; a second copy in `style_instruction` buys nothing measurable.
4. **The residual is inflection.** `pāramitā` for `pāramitās` is the target language
   behaving normally, not the lock failing — hence EXACT / **LOOSE** / MISSING in
   `check_locks.py`, with LOOSE counted as landed.
5. **Unlocked output is not stable run to run.** The control arm rendered རོ་ལངས་ as
   `vetālas`; the committed baseline file renders the same block as `Zombies`. Whatever the
   baseline happened to produce once is not a property to build on.

## Caveats

- Three blocks and eleven locks. Enough to settle *whether* the mechanism works and
  *whether* batching breaks it; not enough to estimate a lock-failure rate for the corpus.
  `check_locks.py` measures that rate on the real run, which is the number that matters.
- Blocks `^1-3`, `^1-4`, `^1-6` are dense homage stanzas. A prose block with 31 matching
  locks (`^1-13`) was not probed; that is the case the `--glossary-max-hits` cap is for.
- Run 1 was executed twice (a `probe.py` import re-ran its module-level loop). Both
  executions gave identical scores, which is a small free datum on determinism at this
  block/arm granularity.
