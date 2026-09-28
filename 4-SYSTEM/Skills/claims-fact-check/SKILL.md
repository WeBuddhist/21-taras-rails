---
name: claims-fact-check
description: >
  Fact-check a translation one block at a time against the WHOLE commentary corpus
  at once — every verse-aligned commentary's prose for that block, plus the
  consolidated claims page for its spine slot — and grade each finding as ERROR
  (contradicts consensus), ⚑ TRADITION-SPECIFIC (follows one attested side of a
  recorded divergence), UNSUPPORTED (asserts what no commentary says), or OK.

  Trigger on "fact-check against the claims", "check this translation against all
  the commentaries", "is this rendering supported by anyone", "run the claims fact
  check", "check block ^1-6 against the corpus".

  Vault-local: it depends on `2-RAILS/Claims/<slot>.md` existing, which is true here
  and in no other vault yet. Where there are no claims, use `commentary-fact-check`.
  Reports; never edits the translation.
---

# claims-fact-check

`commentary-fact-check` grades a translation against **one** commentary per run, and
that restriction is deliberate and correct: mixing two commentaries in one reading is
how an auditor ends up inventing a composite tradition that nobody taught. But it has
a cost on a corpus like this one. This praise has seventeen independent commentaries
from five schools and no root commentary ranking them, so a rendering that faithfully
follows Tāranātha will be flagged as wrong when the run happens to be against Gendun
Drub. The finding is then noise, and worse, noise that looks like a finding.

This skill asks the question the corpus actually supports: **is this rendering
supported by the tradition, and if the tradition is split, which side is it on?** It
can ask that safely because `2-RAILS/Claims/<slot>.md` has already done the hard part
— consolidating all sixteen commentaries' claims into Consensus / ⚑ Divergences /
Unique, with every statement citing a raw claim ID that cites `1-SOURCES/`. The claims
page is what stops "all the commentaries at once" from becoming "blend them".

Use both skills. They answer different questions and neither replaces the other.

| | `commentary-fact-check` | `claims-fact-check` |
|---|---|---|
| Ground truth | one commentary's own prose | all verse-aligned commentaries + the consolidated claims page |
| Answers | does this match **this** authority? | is this supported by **anyone**, and is the corpus split? |
| Divergence | invisible — the other side is not in the room | a first-class verdict |
| Portable | yes, any vault | no — needs `2-RAILS/Claims/` |

This skill **reports**. It never edits the translation. Fixes are a separate pass
(`commentary-fact-check` Phase 2 applies mechanical ones), and a fix that requires a
re-translation goes back through `dharmamitra-termlocked` Step 4, not through a hand
edit.

---

## Inputs

| Input | Required | Description |
|---|---|---|
| **Translation** | ✓ | The file to audit, normally `3-TRANSFORMATIONS/Translations/Dharmamitra-termlocked/<tag>/<stem>-<tag>.md`. |
| **Scope** | ✓ | Block IDs or a bounded range. **Never "the whole text"** — every block gets a full term alignment, and a scope that cannot be done properly will be done badly. |
| **Root text** | ✓ | `1-SOURCES/Text/bo-སྒྲོལ་མ་ཉེར་གཅིག་ལ་བསྟོད་པ།.md`. |
| **Commentaries** | derived | `1-SOURCES/Commentaries/New raw data/` — the ten files carrying `![[…#^id]]` anchors. The seventeen in `used for wiki/` have none and cannot be split by block. |
| **Claims** | derived | `2-RAILS/Claims/<slot>.md`. Slot IDs per `vault-annex.md` §2a; the mapping is `^1-1`–`^1-21` → `tara-01`–`tara-21`, and `^1-22` / `^2-*` / `^a-*` → `benefits` (see caveat 3 — the annex's own anchor column was wrong). |

Report: `<translation-dir>/claims-fact-check-report.md`, appended to, never overwritten.

## Corpus caveats — read before trusting a packet

Three facts about this vault's commentary files that will otherwise be mistaken for
findings:

1. **Ten of seventeen commentaries are verse-aligned.** Only `New raw data/` carries
   transclusion anchors. The claims pages draw on all sixteen, so the claims section of
   a packet is broader than its commentary-prose section. That asymmetry is fine and
   must be stated in the report — never described as "the corpus says", only as "the
   commentaries in the packet say" versus "the claims page records".
2. **Two files in `New raw data/` have no anchors** (`bo-མཁན་པོ་ཚུལ་རྣམ།_*`, i.e.
   `tsultrim-namdak`). The packet lists them under *Not read*. They are absent, not silent.
3. **The benefits section is fine — the warning about it is not.** These files anchor the
   closing ཕན་ཡོན material at `^1-22` and `^2-1`–`^2-6`, and their own frontmatter warns that
   this "predates the 2026-08-07 resegmentation (current scheme: `^a-0`–`^a-7`)". That warning
   is wrong, and so is `vault-annex.md` §2: **the root text has no `^a-2`…`^a-7` run.** Its
   actual IDs are `^I-0`–`^I-3`, `^1-0`–`^1-22`, `^2-0`–`^2-6`, `^a-0`–`^a-1`, which is exactly
   what the commentaries anchor to. Verified 2026-09-22 by reading both files: a packet for
   `^2-3` returns seven commentaries with prose. Audit the benefits section like any other.

Also: some files in `New raw data/` carry no `registered_id`, and the packet falls back
to the filename (`bo-བསྟན་དགའ་སྤྲུལ་སྐུ།` is `tenga-tulku`). Cite the registered ID in the
report, not the filename.

---

## Verdicts

The grading scheme is the whole point of the skill. Four verdicts, and the middle two
are the ones a single-commentary audit cannot produce:

| Verdict | Means | Action |
|---|---|---|
| **⚠ ERROR** | The English names something the claims page records as **consensus** against, or no commentary supports and the Tibetan does not bear. | Re-translate the block. |
| **⚑ TRADITION-SPECIFIC** | The rendering follows one side of a divergence the claims page records under ⚑. | **Not an error.** Record which position, and which commentaries hold it. If the track must commit to a tradition, that is a `requirements.md` decision, not a translation bug. |
| **◇ UNSUPPORTED** | The English asserts something specific that neither the commentary prose nor the claims page attests — typically an over-specification the Tibetan leaves open. | Human judgment: usually loosen the English. |
| **OK** | Attested by consensus, or a neutral rendering the corpus does not adjudicate. | — |

**A finding is graded against what the claims page says, not against the first
commentary that disagrees.** Opening the ⚑ Divergences section before writing a verdict
is what keeps ERROR meaning something.

---

## Procedure

### Step 1 — Assemble the packet

```bash
python3 4-SYSTEM/Skills/claims-fact-check/scripts/assemble_block_packet.py \
  --block 1-6 \
  --root "1-SOURCES/Text/bo-སྒྲོལ་མ་ཉེར་གཅིག་ལ་བསྟོད་པ།.md" \
  --translation "<translation>.md" \
  --out 0-INBOX/temp/fact-check/packet-1-6.md
```

Read the summary line before reading the packet: how many commentaries had prose, how
many were silent, how many were unreadable, and whether the claims page exists. A block
with two witnesses and no claims page does not support the same confidence as one with
eight and a page, and the report must say which it was.

### Step 2 — Build the alignment table before any verdict

Same discipline as `commentary-fact-check`, with the claims page added as a column.
For the block in scope:

1. **List the anchors.** Every content word the commentaries explicitly gloss, define,
   etymologise, name, count or illustrate. The commentaries' own glosses are the
   checklist — not your sense of what matters in the verse.
2. **One row per anchor:** `Tibetan (+Wylie) | commentary gloss(es), by registered ID | what the claims page says (Consensus / ⚑ / Unique) | English used | verdict | one-line reason`.
3. **No verdict before the table is complete.** A verse is not cleared until every
   anchor has a row.

Scan specifically for the classes that read fluently and still name the wrong thing:
kāya vs dharma vs mind; a precise term softened to a vague near-synonym; wrong named
entity; wrong number or scope (*only / all / each / even*); wrong simile tenor; wrong
agent; wrong enumeration order.

Do **not** flag elaboration the commentary adds that the verse needn't carry —
etymologies, citations, sub-classifications, narrative illustration. Dropping
supplementary detail is fine; renaming the referent is not.

### Step 3 — Second sweep on the divergence axis

After the first pass, re-read the claims page's **⚑ Divergences** sections alone and
ask, for each: *which side did this translation land on, and did it land there by
choice or by accident?* This sweep is the one that produces findings no
single-commentary run can produce, and it is regularly where the real content is.

### Step 4 — Write the report

Append (never overwrite) to `<translation-dir>/claims-fact-check-report.md`:

```markdown
### Block ^1-6 — <date>

Witnesses: 8 commentaries with prose, 2 unreadable · claims page: `2-RAILS/Claims/tara-06.md`

| Anchor | Commentary gloss | Claims page | English | Verdict | Note |
|---|---|---|---|---|---|
| རོ་ལངས་ (ro langs) | `karma-maitri`: charnel-ground dwelling vetāla; `taranatha`: rākṣasa-class, mantra-powered | Consensus: a class of beings in Tārā's retinue | "Zombies" | ⚠ ERROR | vetāla — a named class of being, not a modern horror trope |

**Result: <k>/<n> anchors clean · <e> ERROR · <t> ⚑ tradition-specific · <u> unsupported.**
```

Report only ERROR / ⚑ / ◇ rows in the file — the full alignment table stays in the
session. Keep the progress row at the top of the file extended.

### Step 5 — Report back and hand off

Give the user, in chat, every ERROR row with its Tibetan and the commentary gloss
behind it, so they can act without opening the file. State the witness count. Say
plainly that this is a preliminary self-check, not a scholarly sign-off — a domain
specialist reviews before anything is treated as final, and an LLM never marks its own
output complete.

Blocks with an ERROR go back to `dharmamitra-termlocked` Step 4 for a re-translation of
that block, or — where the fix is a vocabulary decision rather than a rendering slip —
to the track's `termbase.md` first, since a termbase fix repairs every block at once.

---

## Completion check

- [ ] Scope was bounded, not "the whole text"
- [ ] Packet assembled per block; witness counts read before the packet
- [ ] Every anchor got a table row before any verdict was assigned
- [ ] ⚑ Divergences sections re-read in a dedicated second sweep
- [ ] ERROR reserved for contradicting consensus — not for disagreeing with one commentary
- [ ] Commentaries cited by `registered_id`, not filename
- [ ] Asymmetry stated: ten commentaries in the prose, sixteen behind the claims page
- [ ] Report appended, never overwritten; every ERROR also surfaced in chat
- [ ] Translation file not edited by this skill

---

## Provenance

Written 2026-09-22 for this vault, after `commentary-fact-check` was re-imported from
the consolidated `Webuddhist-Skills` library. It reuses that skill's
`extract_commentary.py` for the per-block split rather than reimplementing it, and its
term-alignment discipline verbatim; what is new here is the multi-witness packet and
the four-verdict scheme that the claims layer makes possible. If another vault ever
grows a `2-RAILS/Claims/` layer, this skill generalises to it by replacing the slot
mapping in `assemble_block_packet.py` — nothing else in it is specific to twenty-one
homages.
