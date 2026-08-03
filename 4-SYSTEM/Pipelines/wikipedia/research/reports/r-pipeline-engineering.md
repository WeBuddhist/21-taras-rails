# Engineering research: a resumable, auditable Tibetan LLM → Wikipedia pipeline

Scope: repo/engineering patterns for OpenPecha's root-text → key-terms → commentary-evidence → Gemini-drafted Tibetan encyclopedia article → bo.wikipedia create/update pipeline. All findings verified live on 2026-07-29.

---

## 0. Recommended stack (one line each)

| Decision | Pick | Why |
|---|---|---|
| Tokenizer | `botok` 1.1.6 | Only actively maintained Tibetan word tokenizer; `pybo` is dead (last release 2021-04-20). |
| Reference frequencies | `tsikchen.tsv` from botok's `general` dialect pack (41,346,461 tokens) | Ships with the tool, has a real `freq` column, no extra download infra. |
| Keyness | Rayson & Garside log-likelihood + Hardie Log Ratio | Standard, 20 lines of Python, no dependencies. |
| Corpus/alignment source | OpenPecha API v2 (`https://api-aq25662yyq-uc.a.run.app`) | Live, unauthenticated GETs, has explicit `relationship: "commentary"` edges. |
| Local data model | `openpecha` 2.5.0 pinned, or vendor the pydantic models | Package is 9 months stale and pins `stam==0.9.0` against upstream 0.12.1. |
| CLI | `typer` 0.27.0 | Type-hint-driven, rich `--help`, shells out to click; scholars get discoverable subcommands. |
| Config | `pydantic-settings` 2.14.2 with `YamlConfigSettingsSource` + `.env` | One validated `Settings` object covering YAML config *and* secrets, with a documented precedence order. |
| Resumability | JSONL ledger, one record per (term × stage), content-hash keyed | Human-readable, git-diffable, no DB, trivially resumable. |
| HITL | File-based `drafts/ → approved/` + ledger status, git-reviewed | Zero new infrastructure; git *is* the audit trail the IATS paper will need. |
| Testing | `syrupy` 5.5.3 snapshots + `pytest-recording`/`vcrpy` cassettes + `--dry-run` writer | Snapshot the wikitext emitter, cassette the API calls, never touch live wiki in CI. |
| Packaging | `uv` 0.12.0, `uv sync` / `uv run` | One binary, installs Python itself, `uv.lock` gives byte-reproducible envs on macOS. |
| Prompts | `prompts/*.md` with YAML front-matter (Prompty-shaped subset) | Prompt text diffs in git; front-matter carries model + version + schema. |
| Wiki writer | MediaWiki REST `POST/PUT /w/rest.php/v1/page` via `httpx` + OAuth Bearer | Cleaner than `action=edit`; `latest.id` gives free optimistic-concurrency. |

---

## 1. Tibetan NLP tooling

### 1.1 botok — current state

- **PyPI**: `botok` **1.1.6**, uploaded **2026-07-22**, `requires_python >=3.8`, dependencies only `pyyaml` + `requests` ([PyPI JSON](https://pypi.org/pypi/botok/json)). Recent cadence is healthy: 1.1.1 (2025-12-15) → 1.1.6 (2026-07-22).
- **Repo**: [github.com/OpenPecha/Botok](https://github.com/OpenPecha/Botok), Apache 2.0.
- **API** ([README](https://github.com/OpenPecha/botok/blob/master/README.md)):

```python
from pathlib import Path
from botok import WordTokenizer
from botok.config import Config

config = Config(dialect_name="general", base_path=Path.home())
wt = WordTokenizer(config=config)
tokens = wt.tokenize("བཀྲ་ཤིས་བདེ་ལེགས་ཞུས་རྒྱུ་ཡིན།",
                     split_affixes=True, pos_tagging=True, lemmatize=True)
```

- **Token attributes** (verbatim from [`botok/tokenizers/token.py`](https://raw.githubusercontent.com/OpenPecha/Botok/master/botok/tokenizers/token.py)): `text`, `char_types`, `has_merged_dagdra`, `lemma`, `sense`, `chunk_type`, `start`, `len`, `syls_idx`, `syls_start_end`, `pos`, `affixation`, `senses`, `affix`, `affix_host`, `form_freq`, `freq`, `skrt`, `_`. Properties: `syls`, `text_cleaned`, `text_unaffixed`.
  - **`text_unaffixed` is the right key for frequency counting** — it strips the case/genitive affix from the host syllable, so ཆོས་ཀྱི → ཆོས་ counts as ཆོས་.
  - `token.freq` and `token.form_freq` come straight from the dictionary, i.e. botok hands you reference frequencies per token for free.
- Other entry points: `Text` class with `tokenize_words_raw_text`, `tokenize_chunks_plaintext`, `tokenize_on_spaces`.

### 1.2 ⚠️ The dialect-pack reproducibility trap (verified)

[`botok/config.py`](https://raw.githubusercontent.com/OpenPecha/Botok/master/botok/config.py) does this on first run:

```python
DEFAULT_BASE_PATH = Path.home() / "Documents" / "pybo" / "dialect_packs"
DEFAULT_DIALECT_PACK = "general"

def get_dialect_pack_url(dialect_name, version=None):
    attempts = 0
    while not version and attempts < 50:
        response = requests.get(
            "https://api.github.com/repos/Esukhia/botok-data/releases/latest", timeout=50)
        version = response.json()["tag_name"]
        ...
    return f"https://github.com/Esukhia/botok-data/releases/download/{version}/{dialect_name}.zip"
```

Three concrete problems for a "non-programmer runs it" repo:

1. It writes to `~/Documents/pybo/dialect_packs` — outside your repo, invisible, not versioned.
2. It hits **unauthenticated `api.github.com`** up to **50 times** in a loop; rate-limited macOS laptops on shared wifi will hang for minutes.
3. There is exactly **one** release in [Esukhia/botok-data](https://github.com/Esukhia/botok-data): `v0.0.1` (2020-07-27), assets `general.zip` (183,812 B) and `kangyur.zip` (2,612 B).

**And `kangyur.zip` is an empty skeleton.** I downloaded and unzipped it — every entry is a 0-byte `.keep` placeholder:

```
kangyur/adjustments/{remove,rules,words,words_skrt}/.keep
kangyur/dictionary/{adjustment,words}/.keep
```

So `Config(dialect_name="kangyur")` gives an **empty trie**. Despite the tempting name, you must use `dialect_name="general"`.

**Fix**: vendor the pack in-repo and pin the base path.

```python
config = Config(dialect_name="general", base_path=Path("data/dialect_packs"))
```

…with a `make setup` step that does `curl -L https://github.com/Esukhia/botok-data/releases/download/v0.0.1/general.zip` once, verifies a SHA-256 committed to the repo, and unzips into `data/dialect_packs/`. That kills the network call, the 50-retry loop, and version drift in one move.

### 1.3 `general` pack contents = your reference corpus (verified by inspection)

```
general/dictionary/words/tsikchen.tsv               873,326 B
general/dictionary/words/uncompound_lexicon.tsv      40,766 B
general/dictionary/words/exceptions.tsv               3,958 B
general/dictionary/words_non_inflected/particles.tsv  1,597 B
general/dictionary/words/ancient.tsv                    674 B
general/dictionary/words/dagdra.tsv                      79 B
general/dictionary/rules/rdr_basis.tsv                1,078 B
```

`tsikchen.tsv` header and format (matching the [botok-data](https://github.com/Esukhia/botok-data) spec `<form>\t<pos>\t<lemma>\t<sense>\t<freq>`):

```
# form	pos	lemma	sense	freq
ཀ	DET			
ཀ་ཁ	NOUN			98
ཀ་དག	OTHER			2137
```

I computed the aggregate: **31,059 entries, 19,540 with a frequency value, total frequency = 41,346,461**. Top forms by frequency:

```
4707770 ར ADP        678552 རྣམས DET     392115 ཆོས NOUN
1744352 ས ADP        532945 འདི DET      381810 ཉིད DET
 948982 མ PART       447936 ཐམས་ཅད DET   311255 རང PRON
 883801 མི PART      440570 དག DET       307198 དོན NOUN
```

Two things fall out of this:

- **You have a reference corpus already**, with N₂ = 41,346,461 — no separate download, no licensing question (botok-data is "public domain unless indicated otherwise").
- **You have an empirically derived stopword list**: take the top-K forms whose POS ∈ {ADP, PART, DET, PRON, CCONJ, SCONJ, PUNCT} and/or freq > threshold. This is better than a hand-curated list because it is derived from the same lexicon your tokenizer uses.

### 1.4 Tibetan stopwords — what actually exists

There is **no** `bo` entry in [stopwords-iso](https://github.com/stopwords-iso/stopwords-iso) and no botok-provided stoplist. The best hand-curated public list is [`pipeline/stopwords_bo.py`](https://huggingface.co/spaces/daniel-wojahn/ttm-webapp-hf/blob/main/pipeline/stopwords_bo.py) from Daniel Wojahn's **Tibetan Text Metrics** ([Zenodo 10.5281/zenodo.14992358](https://zenodo.org/records/14992358)) — ~4.9 KB, categorised into `PARTICLES_INITIAL`, `MARKERS_AND_PUNCTUATION`, `ORDINAL_NUMBERS`, `MORE_PARTICLES_SUFFIXES`, `PRONOUNS_DEMONSTRATIVES`, `VERBS_AUXILIARIES`, `ADVERBS_QUALIFIERS_INTENSIFIERS`, `QUANTIFIERS_DETERMINERS_COLLECTIVES`, `CONNECTORS_CONJUNCTIONS`, `INTERJECTIONS_EXCLAMATIONS`.

It contains a normalisation function you should copy verbatim, because it names a real botok footgun:

```python
def _normalize_tibetan_token(token: str) -> str:
    """Botok's behavior can vary, so we normalize both the stopwords
    and the tokens being compared."""
    return token.rstrip('་')
```

**Recommendation**: union of (a) that curated list, normalised, and (b) POS-based filtering from botok tags. Ship it as `data/stopwords_bo.txt` in your repo with a provenance header — don't take a runtime dependency on a HF Space.

### 1.5 Larger corpora, if you want a genre-contrastive reference

- **ACTib v2.0** (Annotated Corpus of Classical Tibetan), Meelen, Roux & Hill — **>185M tokens**, segmented + POS-tagged, **CC-BY-4.0**, DOI [10.5281/zenodo.3951503](https://zenodo.org/records/3951503). Distributed as per-collection ZIPs of XML: `SegPOS-eKangyur_July2020.zip` (79.0 MB), `SegPOS-eTengyur_July2020.zip` (192.9 MB), plus DharmaDownload, GuruLamaworks, KarmaDelek, Shechen, DrikungChetsang, PalriParkhang, TulkuSangag, VajraVidya, Various — 11 files, 844.9 MB total. Method paper: [Optimisation of the Largest Annotated Tibetan Corpus…, ACM TALLIP](https://dl.acm.org/doi/fullHtml/10.1145/3409488).
- Broader landscape survey: [Tibetan Language and AI: A Comprehensive Survey of Resources, Methods and Challenges](https://arxiv.org/html/2510.19144v1).

**Opinion**: start with `tsikchen.tsv` (zero-cost, ships with botok). Only add ACTib `eKangyur` if you find that canonical vocabulary fails to surface as "key" — which it will, because tsikchen is itself Buddhist-canon-weighted. That is the real methodological choice: *against a Buddhist-canon reference, canonical terms are not key.* For a Kangyur root text, the interesting reference is **eKangyur minus this text**, so terms specific to *this sūtra* pop.

### 1.6 Keyness: log-likelihood (Rayson & Garside) — exact formula

From [UCREL's log-likelihood and effect size calculator](https://ucrel.lancs.ac.uk/llwizard.html):

Contingency table:

```
                 Corpus 1    Corpus 2    Total
Word frequency       a           b        a+b
Other words        c-a         d-b     c+d-a-b
Total                c           d        c+d
```

Expected values: `E1 = c*(a+b)/(c+d)`, `E2 = d*(a+b)/(c+d)`
Log-likelihood: `G2 = 2*((a*ln(a/E1)) + (b*ln(b/E2)))`

Critical values: **3.84** (p<0.05), **6.63** (p<0.01), **10.83** (p<0.001), **15.13** (p<0.0001).

UCREL also documents **BIC** (Bayes factor: 0–2 "not worth more than a bare mention", 2–6 positive, 6–10 strong, >10 very strong) and **ELL** ("varies between 0 and 1 inclusive"). For effect size, [Hardie's Log Ratio](https://cass.lancs.ac.uk/log-ratio-an-informal-introduction/) is the more interpretable choice: binary log of the relative-frequency ratio, where each point is a doubling, and ~0 means a "lockword".

**Concrete implementation** — `src/<pkg>/keyness.py`:

```python
import math
from collections import Counter
from pathlib import Path

def log_likelihood(a: int, b: int, c: int, d: int) -> float:
    """Rayson & Garside G2. a=freq in target, b=freq in reference,
    c=target total tokens, d=reference total tokens.
    Sign convention: negative => under-used in target."""
    if a == 0 and b == 0:
        return 0.0
    e1 = c * (a + b) / (c + d)
    e2 = d * (a + b) / (c + d)
    g2 = 0.0
    if a > 0:
        g2 += a * math.log(a / e1)
    if b > 0:
        g2 += b * math.log(b / e2)
    g2 *= 2.0
    return g2 if (a / c) >= (b / d) else -g2

def log_ratio(a: int, b: int, c: int, d: int, smoothing: float = 0.5) -> float:
    """Hardie (2014) effect size, log2 of the relative-frequency ratio."""
    ra = (a if a else smoothing) / c
    rb = (b if b else smoothing) / d
    return math.log2(ra / rb)

def bic(g2: float, c: int, d: int) -> float:
    """Bayes factor approximation, df = 1."""
    return abs(g2) - math.log(c + d)

def load_reference(tsikchen: Path) -> tuple[Counter, int]:
    ref, total = Counter(), 0
    for line in tsikchen.read_text(encoding="utf-8").splitlines():
        if not line or line.lstrip("\ufeff").startswith("#"):
            continue
        cols = line.split("\t")
        form = cols[0].rstrip("་")
        freq = cols[4].strip() if len(cols) > 4 else ""
        if freq.isdigit():
            ref[form] += int(freq)
            total += int(freq)
    return ref, total   # total == 41_346_461 for v0.0.1 general
```

Driver:

```python
def key_terms(text: str, wt, ref: Counter, ref_total: int,
              stopwords: set[str], min_ll: float = 15.13,
              min_lr: float = 1.0, min_count: int = 3):
    toks = wt.tokenize(text, split_affixes=True, pos_tagging=True, lemmatize=True)
    obs = Counter(
        t.text_unaffixed.rstrip("་") or t.text.rstrip("་")
        for t in toks
        if t.chunk_type == "TEXT"
        and t.pos not in {"PUNCT", "PART", "ADP", "DET", "PRON", "CCONJ", "SCONJ", "NUM"}
    )
    c = sum(obs.values())
    out = []
    for form, a in obs.items():
        if a < min_count or form in stopwords or len(form) < 2:
            continue
        b = ref.get(form, 0)
        ll = log_likelihood(a, b, c, ref_total)
        lr = log_ratio(a, b, c, ref_total)
        if ll >= min_ll and lr >= min_lr:
            out.append({"term": form, "count": a, "ref_count": b,
                        "ll": round(ll, 2), "log_ratio": round(lr, 2),
                        "bic": round(bic(ll, c, ref_total), 2)})
    return sorted(out, key=lambda r: -r["ll"])
```

Thresholds to ship as defaults in `config.yaml`: `min_ll: 15.13` (p<0.0001), `min_log_ratio: 1.0` (at least 2× over-represented), `min_count: 3` (kills hapax noise). Emit **all** four numbers per term into the ledger — the IATS paper will want to report them, and a reviewer will want to re-rank without re-running.

---

## 2. OpenPecha data formats and APIs

### 2.1 Two generations of format — know which you're touching

**OPF (v1, legacy)**: an open folder format — plain-text base layer (`base/v001.txt`) plus `layers/<base>/<layer_name>.yml` standoff annotations, per the [Toolkit repo](https://github.com/OpenPecha/Toolkit). The base can be edited without invalidating annotations.

**STAM (v2, current)**: `openpecha` 2.5.0 ("toolkit v2") serialises annotations as STAM JSON. [STAM](https://github.com/annotation/stam) is a generic stand-off annotation model; the Python binding is [`stam` on PyPI](https://pypi.org/project/stam/), currently **0.12.1**.

### 2.2 `openpecha` PyPI package — real numbers and a real hazard

From [PyPI](https://pypi.org/pypi/openpecha/json):

- Latest **2.5.0**, uploaded **2025-10-29** (previous: 2.4.5 on 2025-09-24). **Nine months without a release; the [toolkit-v2 repo](https://github.com/OpenPecha/toolkit-v2) was last pushed 2025-10-29.**
- `requires_python >=3.10`.
- Dependencies: `pydantic>=2.7.4`, **`stam==0.9.0`**, `diff-match-patch==20230430`, `pyewts==0.2.0`, `botok>=0.8.12`, `python-docx>=1.1.2`, `fast_antx==0.0.1`, `bo_sent_tokenizer==0.0.1`, `docx2python==3.3.0`, `boto3>=1.34.0`, `botocore>=1.34.0`, `rdflib>=5.0.0`, `fonttools[unicode]>=4.37.3`, `beautifulsoup4>=4.12.0`.

**Hazard**: `stam==0.9.0` is an *exact* pin, three minor versions behind upstream 0.12.1 — any other dep wanting newer `stam` deadlocks the resolver. And `boto3`/`botocore`/`rdflib`/`fonttools`/`docx2python` are a heavy transitive tail you do not need to tokenize Tibetan and emit wikitext.

**Recommendation**: do **not** take `openpecha` as a runtime dependency. Its useful surface for you is ~120 lines of pydantic models. Vendor them into `src/<pkg>/opf_models.py` with a provenance comment, or pin `openpecha==2.5.0` in an *optional extra* used only by an `import-opf` subcommand.

### 2.3 The annotation model (verbatim from source)

From [`src/openpecha/pecha/layer.py`](https://raw.githubusercontent.com/OpenPecha/toolkit-v2/main/src/openpecha/pecha/layer.py):

```python
class AnnotationType(str, Enum):
    SEGMENTATION = "segmentation"
    ALIGNMENT = "alignment"
    VERSION = "version"
    FOOTNOTE = "footnote"
    CHAPTER = "chapter"
    PAGINATION = "pagination"
    DURCHEN = "durchen"
    SAPCHE = "sapche"
    OCR_CONFIDENCE = "ocr_confidence"
    LANGUAGE = "language"
    CITATION = "citation"
    BOOK_TITLE = "book_title"
```

From [`src/openpecha/pecha/annotations.py`](https://raw.githubusercontent.com/OpenPecha/toolkit-v2/main/src/openpecha/pecha/annotations.py) — **this is how root↔commentary alignment is represented**:

```python
class span(BaseModel):
    start: int = Field(..., ge=0)
    end: int = Field(..., ge=0)
    errors: Optional[Dict] = None

class AlignmentAnnotation(BaseAnnotation):
    id: str = Field(..., description="Annotation ID")
    alignment_index: list[int] = Field(
        description="Index of the alignment, which can be of translation or commentary"
    )
```

So: a commentary instance carries an `alignment` layer whose annotations each have a character `span` into the commentary base text plus an `alignment_index` list pointing at root segment indices. **Alignment is many-to-many by construction** (`list[int]`) — one commentary block can gloss several root segments. Your evidence-gathering step must handle fan-out, not assume 1:1.

On-disk layout from [`Pecha`](https://raw.githubusercontent.com/OpenPecha/toolkit-v2/main/src/openpecha/pecha/__init__.py): `<pecha_id>/base/<base_name>.txt` and `<pecha_id>/layers/<base_name>/<layer_type>-<annotation_id>.json`, loaded via `Pecha.from_path(path)`, each layer being a `stam.AnnotationStore`.

### 2.4 ✅ The live OpenPecha API v2 — this is the one to use

The old `OpenPecha-API` service (`openpecha.bdrc.io/api/v1/docs`) is **dead** — connection fails. The live backend is [OpenPecha/openpecha-backend](https://github.com/OpenPecha/openpecha-backend) (Firebase Cloud Functions + Neo4j + Cloud Storage), Swagger UI at `https://pecha-backend.web.app/swagger/`.

Resolved base URLs (from the site's own public `config.json`):

```
PROD  https://api-aq25662yyq-uc.a.run.app
DEV   https://api-l25bgmwqoa-uc.a.run.app
TEST  https://api-kwgjscy6gq-uc.a.run.app
```

OpenAPI 3.1.0 spec (`OpenPecha API v2`, version `2.1.0`) served as **YAML** at `GET {BASE}/v2/schema/openapi` — note it is YAML despite the `.json`-less path, so parse with `yaml.safe_load`, not `json.loads`. Endpoints:

```
GET  /v2/texts                                  ?limit&offset&type&language&author&title
GET  /v2/texts/{id}
GET  /v2/texts/{text_id}/instances               POST too
GET  /v2/texts/{texts_id}/group
GET  /v2/texts/{text_id}/related-by-work
GET  /v2/instances/{instance_id}                 ?annotation=bool&content=bool
PUT  /v2/instances/{instance_id}
GET  /v2/instances/{instance_id}/related
GET  /v2/instances/{instance_id}/segment-related ?segment_id | (span_start&span_end) &transform
POST /v2/instances/{instance_id}/segment-content
POST /v2/instances/{instance_id}/translation
POST /v2/instances/{instance_id}/commentary
GET  /v2/segments/{segment_id}/related
GET/PUT /v2/segments/{segment_id}/content
GET  /v2/segments/search
POST /v2/segments/batch-overlapping
GET  /v2/annotations/{annotation_id}
POST /v2/annotations/{instance_id}/annotation
PUT  /v2/annotations/{annotation_id}/annotation
GET/POST /v2/persons ; /v2/persons/{person_id}
GET/POST /v2/categories ; /v2/categories/{category_id}/texts
GET/POST /v2/enum
GET  /api/version
```

`GET /v2/texts` filters: `type` ∈ `[root, commentary, translation, translation_source, none]`; `language` from `GET /v2/enum` (includes `bo`, `sa`, `en`, `zh`, `lzh`, `pi`, `cmg`, `mn`, `tib`, `tibphono`, …); `title` is a case-insensitive substring match against primary *and* alternative titles. `limit` max 100, default 20 — so paginate.

**Live verification I ran** (unauthenticated GETs work; no `securitySchemes` block in the spec):

```
GET /v2/texts?type=root&language=bo&limit=3
  → 5rEYhuVjFRFnhviLcoLGU  ཚད་མ་རྣམ་འགྲེལ་གྱི་ཚིག་ལེའུར་བྱས་པ།   (Pramāṇavārttika)
  → zYCXcC08myjMoV2R5PwDL  …མངོན་པར་རྟོགས་པའི་རྒྱན་…             (Abhisamayālaṃkāra)

GET /v2/texts/zYCXcC08myjMoV2R5PwDL/instances
  → [{"id":"qEwXotY3V235i0PP7IwOm","type":"critical","source":"bdrc.io", ...}]

GET /v2/instances/qEwXotY3V235i0PP7IwOm?content=true&annotation=true
  → content: 34,269 chars, starts "ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པའི་མན་ངག་གི་བསྟན་བཅོས…"
  → annotations: [{"annotation_id":"hA1YtbnuTEiExp7CQUcgR","type":"segmentation"}]

GET /v2/instances/qEwXotY3V235i0PP7IwOm/related
  → [{"instance_id":"SSpIJ09KWHEvXT6xhuD4u",
      "metadata":{"text_id":"V6MU744VpOMgzIIyuAdDE",
                  "title":{"bo":"…འགྲེལ་བ་དོན་བསལ་བའི་རྣམ་བཤད་སྙིང་པོའི་རྒྱན།"}},
      "relationship":"commentary"}]
```

**That `relationship: "commentary"` edge is exactly the root→commentary discovery step of your pipeline, and it already works today with a plain `httpx.get`.**

`GET /v2/instances/{id}/segment-related` is the alignment workhorse. From the spec, verbatim:

> Exactly one of `segment_id` or (`span_start` and `span_end`) must be provided. If `segment_id` is provided, returns related segments across manifestations. If `span_start` and `span_end` are provided, returns manifestations with merged spans overlapping the given range.

and on `transform`:

> Whether to transfer alignments to segmentation layer. If false (default), returns alignment annotation segments. If true, returns segmentation annotation segments.

Response shape: `[{text: {...}, instance: {...}, segments: [{id, span: {start, end}}]}]`. Note I got `[]` for a bare `span_start=0&span_end=200` probe on both test instances — either those instances lack an alignment layer or spans must land on real segment boundaries. **Your fetch layer must treat an empty alignment result as a first-class "no evidence" ledger state, not a crash.**

Retrieval order for the pipeline: `/v2/texts?type=root` → `/v2/texts/{id}/instances` → `/v2/instances/{iid}?content=true` (root base text for term extraction) → `/v2/instances/{iid}/related` (find `relationship=="commentary"`) → `/v2/instances/{iid}/segment-related?segment_id=…` (map root segment → commentary segments) → `POST /v2/instances/{cid}/segment-content` (pull the commentary text for those segment IDs). Every hop returns stable IDs — **store them in the ledger; they are your citation anchors.**

**Caveat**: `/v2/texts` PROD data currently contains obvious test junk (I saw a text whose `wiki` field is `"ho how are youcom"`). Validate aggressively at the boundary with pydantic; do not trust free-text fields. Also note texts and instances already carry a **`wiki` field** — that is where a bo.wikipedia URL belongs, and it means the round-trip link back from Wikipedia to OpenPecha is already modelled.

### 2.5 Other OpenPecha repos worth knowing

| Repo | Language | Last push | Status |
|---|---|---|---|
| [Botok](https://github.com/OpenPecha/Botok) | Python | 2026-07-22 | **Active — use it** |
| [openpecha-backend](https://github.com/OpenPecha/openpecha-backend) | Python | 2026-07-05 | **Active — the live API** |
| [toolkit-v2](https://github.com/OpenPecha/toolkit-v2) | Python | 2025-10-29 | Stale but usable |
| [Toolkit](https://github.com/OpenPecha/Toolkit) (v1/OPF) | Python | 2026-04-02 | Legacy |
| [pybo](https://github.com/OpenPecha/pybo) | Python | 2026-04-02 | **Dead** — PyPI 0.8.0, 2021-04-20 |
| [pyewts](https://github.com/OpenPecha/pyewts) | Python | 2026-07-27 | 0.2.0 (2022-11-22); use for Wylie↔Unicode |
| [OpenPecha-API](https://github.com/OpenPecha/OpenPecha-API) | Python | 2026-03-26 | **Defunct** — `openpecha.bdrc.io` unreachable |
| [Alignment-Generator](https://github.com/OpenPecha/Alignment-Generator) | Python | 2026-03-26 | Text2Text alignment generation |
| [Openpecha-api-mcp](https://github.com/OpenPecha/Openpecha-api-mcp) | TypeScript | 2026-04-01 | MCP wrapper over the API |

---

## 3. CLI + config patterns

### 3.1 CLI: **typer 0.27.0** (released 2026-07-15, `requires_python >=3.10`)

Not argparse (no subcommand ergonomics, no completion), not raw click (decorator soup). Typer derives the interface from type hints, auto-generates `--help` with Rich formatting, and gives shell completion for free — which matters when the operator is a scholar typing `pipeline extract-terms --help` rather than reading your README. It's built on [click 8.4.2](https://pypi.org/project/click/), so you keep click's ecosystem.

Design the CLI as **one verb per pipeline stage, each independently re-runnable**:

```
pecha-wiki init          --config config.yaml       # scaffold run dir + ledger
pecha-wiki fetch         --root-text E65V1V… [--refresh]
pecha-wiki extract-terms --run 2026-08-01-abhisamaya [--top 40]
pecha-wiki gather        --run … [--term …]
pecha-wiki draft         --run … [--term …] [--model gemini-3.6-flash]
pecha-wiki review        --run …                     # opens drafts/ ; prints queue
pecha-wiki check-wiki    --run …                     # bo.wikipedia existence + revid
pecha-wiki publish       --run … --dry-run|--live [--sandbox]
pecha-wiki status        --run …                     # ledger summary table
```

Every command takes `--run <id>` and is idempotent: it reads the ledger, skips units already `done`, and only touches units in the states it owns. `--force` re-does; `--only <term>` narrows. This is the single most important property for a non-programmer operator — **any command can be re-run after any failure and it does the right thing.**

Wire it with `[project.scripts]` so `uv run pecha-wiki …` works with zero PATH fiddling ([uv docs](https://docs.astral.sh/uv/concepts/projects/init/)).

### 3.2 Config: **YAML for knobs, `.env` for secrets, unified by pydantic-settings 2.14.2**

Two files, one validated object:

```
config.yaml    # committed: models, thresholds, prompt paths, wiki target, rate limits
.env           # gitignored: GEMINI_API_KEY, WIKI_OAUTH_TOKEN
.env.example    # committed: same keys, empty values
```

[pydantic-settings](https://pydantic.dev/docs/validation/latest/concepts/pydantic_settings/) gives `YamlConfigSettingsSource` and `TomlConfigSettingsSource` alongside env/dotenv, with a documented precedence: CLI args → init args → env vars → dotenv → secrets dir → defaults. And `settings_customise_sources` lets you order them:

```python
from pydantic import SecretStr
from pydantic_settings import (BaseSettings, SettingsConfigDict,
                               YamlConfigSettingsSource)

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8",
        env_nested_delimiter="__", yaml_file="config.yaml", extra="forbid",
    )
    gemini_api_key: SecretStr
    wiki_oauth_token: SecretStr
    gemini: GeminiConfig
    keyness: KeynessConfig
    wiki: WikiConfig

    @classmethod
    def settings_customise_sources(cls, settings_cls, init_settings,
                                   env_settings, dotenv_settings,
                                   file_secret_settings):
        return (init_settings, env_settings, dotenv_settings,
                YamlConfigSettingsSource(settings_cls), file_secret_settings)
```

Use `SecretStr` for both keys — it prevents accidental leakage into logs and ledger dumps, which matters because your ledger is going to be committed to git. `extra="forbid"` turns a typo'd YAML key into a startup error instead of a silently ignored setting. Set `PYDANTIC_SETTINGS_DEBUG=1` to trace which source won.

Not dynaconf (3.3.4) — more machinery, no pydantic validation, and you'd still hand-roll type checks.

### 3.3 Ledger / run-manifest for resumability

**One JSONL file per run, one record per (term × stage) unit of work**, append-only, content-hash keyed.

```
runs/2026-08-01-abhisamaya/
├── run.yaml                  # frozen snapshot of resolved Settings + git SHA
├── ledger.jsonl              # append-only event log
├── ledger.json               # derived current-state index (regenerable)
├── raw/                      # API responses, cached verbatim by URL hash
├── evidence/<term>.json      # gathered commentary spans + IDs
├── drafts/<term>.wiki        # Gemini output, unreviewed
├── approved/<term>.wiki      # moved here by a human
└── published/<term>.json     # revid, timestamp, diff URL
```

Record schema:

```json
{
  "ts": "2026-08-01T09:14:22Z",
  "run_id": "2026-08-01-abhisamaya",
  "unit_id": "term:ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ",
  "stage": "draft",
  "status": "done",
  "attempt": 1,
  "input_hash": "sha256:9f2c…",
  "output_path": "drafts/ཤེས་རབ་….wiki",
  "model": "gemini-3.6-flash",
  "prompt_id": "draft_article",
  "prompt_version": "3",
  "prompt_hash": "sha256:41ab…",
  "usage": {"input_tokens": 18422, "output_tokens": 2103},
  "citations": ["SEG789", "SEG790"],
  "error": null,
  "duration_ms": 8412
}
```

Status vocabulary — keep it small and total: `pending → running → done | failed | skipped | needs_review → approved | rejected → published`.

Rules that make it actually work:

1. **`input_hash` is the resume key.** SHA-256 over (source text + prompt file bytes + model id + relevant config subtree). Same hash + `done` ⇒ skip. Any input changes ⇒ hash changes ⇒ re-run automatically. This is the "idempotent executor" pattern — check the store before executing, return the stored result if complete, resume if incomplete ([reliability patterns for AI pipelines](https://www.gmicloud.ai/en/blog/reliability-patterns-ai-pipelines)).
2. **Append-only JSONL, never mutate.** Current state = last record per `(unit_id, stage)`. This gives you a free audit trail: every retry, every failure, every prompt version that ever touched a term. For an IATS paper about a *semi-automatic* method, that log **is** the methods section.
3. **Write output file first, then append the ledger record.** Crash between the two ⇒ orphan file, harmless. Reverse order ⇒ ledger claims success with no artifact.
4. **Scope checkpoints to a run**, never share across runs — if the root text changes, mint a new `run_id` rather than trying to patch an old one.
5. `pecha-wiki status --run …` renders the JSONL as a Rich table: rows = terms, columns = stages, cells = coloured status. That single command is the operator's whole mental model.

Don't reach for Prefect/Dagster/Airflow. This is ~40 terms per run on one laptop; a JSONL file plus `--force` beats a scheduler you have to keep alive, and a JSONL file survives being emailed to a collaborator.

---

## 4. Human-in-the-loop checkpoints

You need **two** distinct gates, and they are not the same thing:

- **Gate A — evidence/term review** (before spending tokens): is this actually a key term, and is the gathered commentary material on-topic?
- **Gate B — publication review** (before touching bo.wikipedia): is the Tibetan prose correct, is every statement cited, is this an improvement over the existing article?

### Option comparison

| Pattern | Pros | Cons | Verdict |
|---|---|---|---|
| **File move `drafts/ → approved/`** | Zero infra; reviewer uses any editor; the move is atomic and unambiguous; works offline; git-diffable | No structured reviewer comments; no per-statement granularity; reviewer must find the files | **Pick this** |
| **Ledger `status: needs_review` + `pecha-wiki approve <term>`** | Structured, records who/when; scriptable | Requires the reviewer to use a terminal | **Add as a thin layer on top of the file move** |
| **Git branch + PR review** | Line-level comments, threaded discussion, full provenance, free hosting | Requires reviewers to have GitHub accounts and be comfortable with PRs | **Use for prompt changes and for the final published batch** |
| **Streamlit 1.60.0 local UI** | Nicest reviewer UX; side-by-side draft vs. evidence vs. live wiki; approve/reject buttons write the ledger | A second app to run, keep alive, and debug; `st.session_state` reruns bite; adds ~40 transitive deps | **Optional `[ui]` extra, phase 2** |
| **Gradio 6.20.0** | Fast to build, shareable link | Heavier still; sharing links is a liability for unreviewed content | Skip |

### Recommendation

**Gate A and Gate B both use the file-move pattern, with the ledger as the record of truth.** Concretely:

- `pecha-wiki gather` writes `evidence/<term>.json` and sets status `needs_review`.
- `pecha-wiki review --run …` prints the queue, opens the run directory (`open` on macOS), and shows a one-line summary per pending term.
- The reviewer edits the `.wiki` file **in place** (their edits are the correction signal) and moves it to `approved/`.
- `pecha-wiki publish` only ever reads `approved/`. It refuses to publish anything not in that directory. It computes the diff between `drafts/<term>.wiki` and `approved/<term>.wiki` and records it in the ledger — **that diff is your human-correction dataset, and it is the most publishable artifact of the whole project.**

Then add Streamlit later as a pure *view* over the same directories, so the file layout stays canonical and the UI is disposable. The literature on HITL review queues is consistent that the failure mode is stale queues and mixed rubrics — [keep review batches completable in one sitting](https://www.braintrust.dev/articles/best-human-in-the-loop-llm-evaluation-platforms-2026), so cap `--top 40` terms per run, not 400.

One more gate that is easy to forget: **`publish` must re-fetch the live page and re-verify the base revision immediately before writing**, because a human reviewed the draft against a version of the article that may have changed hours ago. The REST API's `latest.id` field handles this for you (§7).

---

## 5. Testing an LLM pipeline

### 5.1 Golden-file / snapshot testing: **syrupy 5.5.3**

The wikitext emitter is a **pure function** — `(article_json, citations) → wikitext` — and pure functions are exactly what snapshot testing is for.

```python
def test_emit_wikitext(snapshot):
    article = load_fixture("fixtures/article_sherab.json")
    assert emit_wikitext(article) == snapshot
```

First run fails; `pytest --snapshot-update` writes `__snapshots__/test_emit.ambr` (default `AmberSnapshotExtension`) and also **removes stale snapshots**. Use `JSONSnapshotExtension` for structured intermediates and `SingleFileSnapshotExtension` for wikitext so the snapshot is a readable `.raw` file a Tibetan-reading reviewer can inspect in a diff ([syrupy](https://github.com/syrupy-project/syrupy)):

```python
snapshot.with_defaults(extension_class=SingleFileSnapshotExtension)
```

Snapshot diffs in PRs are how you catch "the emitter silently dropped the `<ref>` tags" — which is the single most damaging regression this pipeline can have.

### 5.2 Never hit the Gemini API in tests

`google-genai` transports over **httpx** (`httpx<1.0.0,>=0.28.1` in its deps), which gives you two clean options:

- **`pytest-recording` 0.13.4 + `vcrpy` 8.3.0** — record real responses once into YAML cassettes, replay forever. Mark tests `@pytest.mark.vcr`; run `pytest --record-mode=once` to (re)record. **Filter `Authorization` and `x-goog-api-key` headers out of cassettes** — this is not optional, cassettes get committed. ([pytest-recording](https://github.com/kiwicom/pytest-recording), [vcrpy](https://github.com/kevin1024/vcrpy)). Be aware httpx cassette format has historically been finicky ([vcrpy#550](https://github.com/kevin1024/vcrpy/issues/550)) — verify replay works before committing to it.
- **`respx` 0.23.1** — hand-written httpx mocks, no cassettes. Better for error paths (429, 503, truncated JSON) where you *want* to fabricate a response you'll never record naturally.

Use both: cassettes for the happy path, respx for failure injection.

### 5.3 Determinism

LLM output is not reproducible, so **do not try to snapshot it**. Draw the line clearly:

- **Deterministic and snapshot-tested**: tokenization, keyness scores, evidence selection, prompt rendering, wikitext emission, citation formatting, diffing against existing articles.
- **Non-deterministic and contract-tested only**: the Gemini call. Test the *contract*, not the text — use structured output with a pydantic schema, then assert schema validity, that every `statement` has a non-empty `citation_ids` list, and that every `citation_id` resolves to a real segment ID from `evidence/<term>.json`.

That last assertion is the whole "citation for every statement" requirement, expressed as a test. Make it a hard gate in `draft`, not just a test: a draft whose citation IDs don't resolve gets status `failed`, never `needs_review`.

For as much determinism as the API allows, set `temperature: 0` and pin the exact model id (not an alias) in `config.yaml`, and record the model id + prompt hash in every ledger record so a non-reproducible output is at least *explainable*.

### 5.4 Testing the MediaWiki writer without editing live

Four layers, all of which you should build:

1. **`--dry-run` (default on).** The writer renders the exact HTTP request — method, URL, JSON body, headers with secrets redacted — writes it to `published/<term>.request.json`, and returns without sending. `--live` is the only way to send, and it should also require a non-empty `--reason` string that goes into the edit summary.
2. **Sandbox target.** `Wikipedia:Sandbox` **exists on bo.wikipedia** (verified — it's in the Project namespace listing). Config `wiki.target: sandbox|live` maps to `Wikipedia:Sandbox/<term>` vs. mainspace. Run the entire publish path against sandbox subpages first; the wikitext, templates, and refs all render identically.
3. **respx-mocked API in unit tests.** Assert the request shape: correct endpoint, `comment` present and containing the LLM disclosure, `latest.id` matching the fetched revision, `content_model: "wikitext"`.
4. **A local MediaWiki container for integration tests** (optional). Only worth it if you start touching templates or Lua modules.

Additionally: your CI must have **no** wiki credentials in the environment at all. Then a bug that would edit live simply 401s instead of publishing an AI draft to the Tibetan Wikipedia.

---

## 6. Packaging and prompt versioning

### 6.1 **uv 0.12.0** (released 2026-07-28), not pip/venv

For a macOS repo a non-programmer must set up, uv wins decisively: a single self-contained binary that **installs Python itself**, so the README is three lines and none of them are "first install Python 3.12 and make sure it's the right one".

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
uv sync            # creates .venv, installs exact locked versions, incl. Python
uv run pecha-wiki status --run 2026-08-01-abhisamaya
```

`uv.lock` is committed and gives byte-identical environments across machines — which for a conference-paper artifact means a reviewer can reproduce your run. `.python-version` pins the interpreter. `uv run` needs no manual `activate`, removing the single most common failure mode for non-programmer operators ("it says command not found").

### 6.2 pyproject.toml layout

```toml
[project]
name = "pecha-wiki"
version = "0.1.0"
description = "Semi-automatic Tibetan encyclopedia articles from root texts and aligned commentaries"
requires-python = ">=3.11"
dependencies = [
  "botok>=1.1.6,<2",
  "google-genai>=2.14.0,<3",
  "typer>=0.27.0,<1",
  "pydantic>=2.12,<3",
  "pydantic-settings>=2.14.2,<3",
  "httpx>=0.28.1,<1",
  "pyyaml>=6",
  "rich>=13",
  "jinja2>=3.1",
]

[project.optional-dependencies]
opf = ["openpecha==2.5.0"]        # heavy + stale; only for local OPF import
ui  = ["streamlit>=1.60.0"]        # phase-2 review UI

[dependency-groups]
dev  = ["pytest>=8", "syrupy>=5.5.3", "pytest-recording>=0.13.4", "respx>=0.23.1"]
lint = ["ruff", "mypy"]

[project.scripts]
pecha-wiki = "pecha_wiki.cli:app"

[build-system]
requires = ["uv_build>=0.12.0,<0.13"]
build-backend = "uv_build"

[tool.uv]
default-groups = ["dev"]
```

Note the split: `[dependency-groups]` (PEP 735) for dev-only tooling — **local-only, never published** — versus `[project.optional-dependencies]` for extras a consumer might want. `uv sync` includes the `dev` group by default; `uv add --dev pytest` maintains it ([uv dependencies docs](https://docs.astral.sh/uv/concepts/projects/dependencies/)).

Src layout (`src/pecha_wiki/`) is uv's default and isolates the package from stray `python` invocations in the repo root ([uv init docs](https://docs.astral.sh/uv/concepts/projects/init/)).

### 6.3 Shipping prompts as versioned files

Don't inline prompts in Python. Use `prompts/<id>.md` with YAML front-matter — a **subset** of the [Prompty](https://prompty.ai/core-concepts/file-format/) format ([microsoft/prompty](https://github.com/microsoft/prompty)). Take the *shape* (frontmatter + Jinja2 body + `system:` / `user:` role markers) but not the runtime dependency; parsing it is 20 lines and Prompty's model/connection block is Azure-shaped and irrelevant to Gemini.

`prompts/draft_article.md`:

```markdown
---
id: draft_article
version: 3
description: Draft a Tibetan encyclopedia article from commentary evidence, one citation per statement.
authors: [tashi.tsering@openpecha.org]
model:
  id: gemini-3.6-flash
  options:
    temperature: 0.0
    thinking_level: medium
inputs:
  - name: term
    kind: string
    required: true
  - name: evidence
    kind: array
    description: Commentary excerpts with segment_id, instance_id, author, text
    required: true
  - name: existing_article
    kind: string
    default: ""
outputs:
  - name: title
    kind: string
  - name: sections
    kind: array
template:
  format: jinja2
changelog: |
  v3 require citation_ids on every statement; forbid uncited claims
  v2 add existing_article for the update path
  v1 initial
---
system:
ཁྱེད་ནི་བོད་ཡིག་གི་རིག་གནས་ཀུན་བཏུས་ཀྱི་རྩོམ་པ་པོ་ཞིག་ཡིན། …

user:
Term: {{ term }}
{% for e in evidence %}
[{{ e.segment_id }}] {{ e.author }} — {{ e.text }}
{% endfor %}
```

Then:

- The loader computes `sha256` of the **raw file bytes** and writes both `prompt_version` and `prompt_hash` into every ledger record. Two runs with different outputs are always explainable by diffing two prompt files at two git SHAs.
- `version` is bumped by hand and enforced in CI: a pre-commit / CI check that fails if a `prompts/*.md` body changed without the `version` incrementing. This is the discipline that turns "we tested some prompts" into a reproducible method for the paper.
- Prompt changes go through a PR. The diff is the review.
- The `outputs` block is generated into (or validated against) the pydantic `response_schema` you hand Gemini, so prompt and schema can't drift.

### 6.4 Gemini API specifics

- **SDK**: `google-genai` **2.14.0**, uploaded **2026-07-22**, `requires_python >=3.10`. `from google import genai` ([PyPI](https://pypi.org/pypi/google-genai/json), [SDK docs](https://googleapis.github.io/python-genai/)).
- **Two API surfaces exist now.** The current docs lead with the **Interactions API** (`client.interactions.create(...)`, result at `interaction.output_text`), while the older `client.models.generate_content(...)` path is documented as [Generate Content API (Legacy)](https://ai.google.dev/gemini-api/docs/generate-content/structured-output). **Pick one and pin it in a single `src/pecha_wiki/llm.py` adapter** — this is exactly the kind of churn you do not want sprayed across the codebase.
- **Structured output** ([docs](https://ai.google.dev/gemini-api/docs/structured-output)):

```python
interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input=prompt,
    response_format={"type": "text", "mime_type": "application/json",
                     "schema": Article.model_json_schema()},
)
article = Article.model_validate_json(interaction.output_text)
```

  Gemini now supports JSON Schema directly, so Pydantic works out of the box including `anyOf` and `$ref` ([announcement](https://blog.google/innovation-and-ai/technology/developers-tools/gemini-api-structured-outputs/)).
- **Thinking**: `thinking_level` ∈ `minimal | low | medium | high`; cannot be combined with legacy `thinking_budget` ([Gemini 3 guide](https://ai.google.dev/gemini-api/docs/gemini-3)).
- **Model IDs** currently listed ([models page](https://ai.google.dev/gemini-api/docs/models)): stable — `gemini-3.6-flash`, `gemini-3.5-flash`, `gemini-3.5-flash-lite`, `gemini-3.1-flash-lite`, `gemini-2.5-pro`, `gemini-2.5-flash`, `gemini-2.5-flash-lite`; preview — `gemini-3.1-pro-preview`, `gemini-3-flash-preview`. Indicative pricing per 1M tokens: `gemini-3.1-pro-preview` $2/$12 (<200k ctx), `gemini-3-flash-preview` $0.50/$3, `gemini-3.1-flash-lite` $0.25/$1.50; 1M input / 64k output windows.
- **Recommendation**: default `gemini-3.6-flash` (stable, cheap, 1M context — an entire commentary fits), with `--model` override for spot-checking a Pro model on hard terms. **Never default to a `-preview` id** in a repo a scholar runs; preview ids get retired.

---

## 7. The bo.wikipedia write path (project-critical constraints)

I queried the wiki directly. These numbers change the design.

### 7.1 Site facts (live, 2026-07-29)

```
GET https://bo.wikipedia.org/w/api.php?action=query&meta=siteinfo&siprop=general|statistics

generator: MediaWiki 1.47.0-wmf.12   lang: bo
pages: 22,734   articles: 8,072   edits: 161,834
users: 35,567   activeusers: 31   admins: 2
cirrussearch-article-words: 13,644,030
```

**31 active users. 2 admins. 8,072 articles.** A bot that creates 40 articles in an afternoon is a measurable fraction of this wiki's entire content and will be noticed by essentially everyone active on it. Social process is a harder constraint than any technical one here.

Installed extensions relevant to you (of 128): `Cite`, `Scribunto`, `TemplateData`, `TemplateStyles`, `TemplateWizard`, `VisualEditor`, `WikibaseClient`, `WikibaseLexeme`.

Template existence check:

```
Template:Cite book  → EXISTS  (localised namespace: དཔེ་པང་།:)
Template:Cite web   → EXISTS
Template:Reflist    → EXISTS
Template:Infobox    → EXISTS
Template:Citation   → MISSING
```

So the emitter should use `{{Cite book|…}}` + `{{Reflist}}` inside `<ref>…</ref>`, and must **not** emit `{{Citation}}`. Ship a `test_templates_exist` integration test that queries `action=query&titles=…` for every template your emitter can produce — a red test is how you find out the wiki changed.

### 7.2 Bot policy: there isn't a local one

`Wikipedia:Bot policy` on bo.wikipedia is **a redirect to `Wikipedia:Community Portal`** (verified by fetching the page wikitext: `#redirect[[Wikipedia:Community Portal]]`). Therefore [meta's standard bot policy](https://meta.wikimedia.org/wiki/Bot_policy) governs: for wikis without a local policy, request the flag at **Steward requests/Bot status**, via global-bot status, automatic approval, or local community consensus. Requirements: separate account from the operator, user page clearly marking it as a bot, operator reachable. Speed limits: **unflagged bots max 1 edit/minute; flagged bots minimum 5-second intervals (12/min); 20-second intervals at peak.** Encode this as a config'd token-bucket rate limiter with a default of **1 edit / 60 s**, not as a `time.sleep` someone can delete.

There are already ~20+ flagged bot accounts on bo.wikipedia (Alexbot, AvicBot, BodhisattvaBot, ChuispastonBot, …), almost all legacy interwiki bots — precedent exists, but none of them write article prose.

### 7.3 ⚠️ LLM content policy — the biggest project risk

English Wikipedia's [Wikipedia:Large language models](https://en.wikipedia.org/wiki/Wikipedia:Large_language_models) now states plainly: **"Using LLMs to generate or rewrite article content is prohibited"**, with narrow exceptions for translation and basic copyediting of one's own work, and: **"LLMs used to generate or modify text should be mentioned in the edit summary, even if their terms of service do not require it."** A [March 2026 RfC](https://en.wikipedia.org/wiki/Wikipedia:Writing_articles_with_large_language_models/RfC) tightened this; [LLM use disclosure](https://en.wikipedia.org/wiki/Wikipedia:LLM_use_disclosure) remains unsettled on the mechanics.

This is **en.wikipedia policy and does not automatically bind bo.wikipedia** — policies are per-project, and bo.wikipedia has no local equivalent. But it is the strongest available signal of where the movement's consensus sits, and a project that lands 40 Gemini-drafted articles on a 31-active-user wiki without prior community consent is asking for a mass revert and a bad session at IATS.

**Design consequences, all of them non-negotiable:**

- **Every edit summary must disclose model name and version**, plus a link to a project page explaining the pipeline. Bake this into the writer so it is structurally impossible to omit: build the summary from the ledger record's `model` field, and refuse to publish if it's absent.
- **Human sign-off is the load-bearing control, not a nicety.** The `approved/` gate is what makes this "semi-automatic" rather than "an LLM bot". Record the approver identity in the ledger.
- **Open a discussion on `Wikipedia:Village pump` on bo.wikipedia before the first live edit**, and link that discussion from the bot's user page. Do this in parallel with building — consensus takes weeks, and there are 2 admins.
- **Every statement carries an inline `<ref>` to a real Tengyur/Kangyur passage with OpenPecha segment IDs.** This is the project's actual defence: the output is not "LLM-generated content", it is *sourced summary of primary texts, drafted with LLM assistance and human-verified*. Make the citation density visible in the wikitext.

### 7.4 Which API to write with

**Use the MediaWiki REST API, not `action=edit`** ([API:REST_API/Reference](https://www.mediawiki.org/wiki/API:REST_API/Reference)):

```
POST /w/rest.php/v1/page
  body: {source, title, comment, content_model?}      → 201
PUT  /w/rest.php/v1/page/{title}
  body: {source, comment, latest: {id}, content_model?} → 200
GET  /w/rest.php/v1/page/{title}         # metadata + wikitext source
GET  /w/rest.php/v1/page/{title}/bare    # metadata only
```

Auth: `Authorization: Bearer $TOKEN` via OAuth (and then you omit the `token` body field); cookie auth needs a CSRF token instead. **OAuth is recommended for applications.**

Why REST over `action=edit`:

- `latest.id` gives **built-in optimistic concurrency** — pass the revision the human reviewed, and the API rejects the write if someone edited in between. With `action=edit` you'd hand-roll `basetimestamp`/`starttimestamp`.
- The create/update split maps exactly onto your two cases (`POST` = new article, `PUT` = update existing), so `check-wiki` → `publish` is a clean branch rather than a `createonly`/`nocreate` flag dance.
- JSON bodies, no CSRF dance under OAuth, no `format=json&formatversion=2` boilerplate.

For the read side (existence check, current wikitext, search for near-miss titles) the Action API is still better: `action=query&titles=…`, `list=search`, `prop=revisions&rvslots=main`. Use both — they're the same wiki.

Library choice: **plain `httpx` + a thin `WikiClient` class**, not pywikibot, not mwclient.

- [`pywikibot` 11.6.0](https://pypi.org/project/pywikibot/) (2026-07-22) is actively maintained and battle-tested but is a *framework* — its own config system, its own family files, its own login flow, all of which fight your `Settings` object and your ledger. It also only supports OAuth 1.0a ([Manual:Pywikibot/OAuth](https://www.mediawiki.org/wiki/Manual:Pywikibot/OAuth)).
- [`mwclient` 0.11.0](https://pypi.org/project/mwclient/) was last released **2024-08-12** and [does not support OAuth 2](https://mwclient.readthedocs.io/en/latest/user/connecting.html).
- Your write surface is *two endpoints*. A 150-line client you fully control, that respects your rate limiter and dry-run flag and logs to your ledger, is less code than configuring either framework.

Two things you must get right regardless of library:

- **User-Agent.** Wikimedia's [User-Agent Policy](https://foundation.wikimedia.org/wiki/Policy:Wikimedia_Foundation_User-Agent_Policy) mandates a descriptive header; missing or generic (`python-requests/x`, `curl`) values get **HTTP 403**. Format: `<client>/<version> (<contact>) <library>/<version>`, e.g.
  `PechaWikiBot/0.1 (https://github.com/OpenPecha/pecha-wiki; openpecha@gmail.com) httpx/0.28`
  Include the word "bot". Set it once in the `httpx.Client(headers=…)` constructor.
- **maxlag.** Append `maxlag=5` to Action API requests ([Manual:Maxlag_parameter](https://www.mediawiki.org/wiki/Manual:Maxlag_parameter)). On lag you get HTTP 200 with `{"error":{"code":"maxlag",…}}` plus `Retry-After` and `X-Database-Lag` headers — honour `Retry-After`, sleep ≥5 s, and never busy-loop.

---

## Implementation implications

- **Vendor the botok `general` dialect pack into `data/dialect_packs/` with a committed SHA-256, and always pass `Config(base_path=…)`.** The default path writes to `~/Documents/pybo/`, and the default resolution loop hits `api.github.com` up to 50 times — unacceptable for a scholar-run repo.
- **Never use `dialect_name="kangyur"`.** Verified: that release asset is a 2,612-byte skeleton of empty `.keep` files and produces an empty trie. Only `"general"` is real.
- **Adopt `tsikchen.tsv` (31,059 entries, 19,540 with counts, N = 41,346,461) as the default keyness reference corpus**, shipped in-repo, with ACTib `SegPOS-eKangyur` (CC-BY-4.0, 79 MB) as an opt-in genre-contrastive alternative behind a config flag. Expect canonical Buddhist vocabulary to score *low* against tsikchen — that's a feature only if you pick the right reference.
- **Count on `token.text_unaffixed.rstrip("་")`, not `token.text`**, and normalise the stopword list the same way; botok's tsek handling is inconsistent enough that the TTM project ships a dedicated normaliser for it.
- **Emit all four keyness numbers (`ll`, `log_ratio`, `bic`, raw counts) per term into the ledger**, and set defaults `min_ll=15.13`, `min_log_ratio=1.0`, `min_count=3`, `top=40`. Reviewers must be able to re-rank without re-running, and the paper needs the statistics.
- **Build the corpus layer against the live OpenPecha API v2 at `https://api-aq25662yyq-uc.a.run.app`, not against local OPF files.** `GET /v2/instances/{id}/related` already returns `relationship: "commentary"` edges, and `?content=true` returns base text — verified working, unauthenticated.
- **Parse `GET /v2/schema/openapi` as YAML, not JSON**, and pin `PROD_API` in `config.yaml` with `DEV_API`/`TEST_API` as switchable profiles.
- **Do not depend on `openpecha` 2.5.0 at runtime.** It's nine months stale, exact-pins `stam==0.9.0` against upstream 0.12.1, and drags in boto3/rdflib/fonttools. Vendor the ~120 lines of `AlignmentAnnotation`/`span` pydantic models, or isolate it in an `[opf]` extra.
- **Model alignment as many-to-many from day one** — `AlignmentAnnotation.alignment_index` is `list[int]`, so one commentary block can gloss several root segments, and evidence gathering must fan out and de-duplicate.
- **Treat an empty `segment-related` result as a first-class ledger state (`skipped: no_alignment`), not an exception.** I hit empty results on live instances.
- **Ledger is append-only JSONL keyed by `input_hash = sha256(source + prompt_bytes + model_id + config_subtree)`; write the artifact file before appending the record.** Statuses: `pending → running → done|failed|skipped|needs_review → approved|rejected → published`.
- **Every CLI verb takes `--run` and is idempotent with `--force`/`--only` escapes**, and `pecha-wiki status` renders the ledger as a terms × stages table. That table is the operator's entire mental model.
- **Two human gates, both file-move based** (`evidence/` review before drafting, `drafts/ → approved/` before publishing); `publish` physically cannot read from `drafts/`. Record the draft↔approved diff — it is both your correction signal and your best paper artifact.
- **Make "citation for every statement" a hard runtime gate, not a test**: a draft whose `citation_ids` don't all resolve to segment IDs present in `evidence/<term>.json` gets status `failed` and never reaches a human.
- **Snapshot-test the emitter with syrupy `SingleFileSnapshotExtension`** so the `.wiki` snapshot is human-readable Tibetan in the PR diff; cassette Gemini with `pytest-recording` (filtering `Authorization` and `x-goog-api-key`) and inject failures with `respx`.
- **`--dry-run` is the default; `--live` requires an explicit `--reason`; CI has no wiki credentials at all.** Add a `test_templates_exist` integration test — `Cite book`, `Cite web`, `Reflist`, `Infobox` exist on bo.wikipedia; `Citation` does not.
- **Write via REST `POST /w/rest.php/v1/page` and `PUT /w/rest.php/v1/page/{title}` with `latest.id`**, using a ~150-line `httpx` client rather than pywikibot or mwclient, and re-fetch + re-verify the base revision immediately before every live write.
- **Hard-code the Wikimedia-compliant User-Agent in the client constructor and send `maxlag=5` on Action API reads**; a missing UA returns 403, and the default rate limit must be 1 edit / 60 s (meta's unflagged-bot ceiling) until a bot flag is granted at Steward requests/Bot status.
- **Construct every edit summary from the ledger's `model` field and refuse to publish without it.** en.wikipedia's LLM page now reads "Using LLMs to generate or rewrite article content is prohibited" with a summary-disclosure expectation; bo.wikipedia has no local policy (its `Wikipedia:Bot policy` is a redirect), so you are setting precedent on a wiki with 8,072 articles, 31 active users and 2 admins.
- **Open a `Wikipedia:Village pump` discussion on bo.wikipedia before the first live mainspace edit and link it from the bot's user page** — this is a build-time task with a multi-week lead, not a launch-day one.
- **Pin exactly one Gemini surface (Interactions vs. legacy generateContent) behind a single `llm.py` adapter, default `gemini-3.6-flash`, `temperature: 0`, never a `-preview` id**, and record `model`, `prompt_version`, `prompt_hash` and token usage on every call.
- **`uv` + committed `uv.lock` + `.python-version` + `[project.scripts]`**, so setup is `curl … | sh` → `uv sync` → `uv run pecha-wiki …` with no Python preinstalled and no venv activation.
- **Prompts live in `prompts/*.md` with YAML front-matter carrying `id`, `version`, `model`, `inputs`, `outputs`, `changelog`; CI fails any PR that changes a prompt body without bumping `version`.** The prompt file hash goes in every ledger record — that's what makes a run explainable nine months later at IATS.

**Sources:**
[botok PyPI](https://pypi.org/pypi/botok/json) · [OpenPecha/Botok](https://github.com/OpenPecha/Botok) · [botok config.py](https://raw.githubusercontent.com/OpenPecha/Botok/master/botok/config.py) · [botok token.py](https://raw.githubusercontent.com/OpenPecha/Botok/master/botok/tokenizers/token.py) · [Esukhia/botok-data](https://github.com/Esukhia/botok-data) · [OpenPecha/pybo](https://github.com/OpenPecha/pybo) · [openpecha PyPI](https://pypi.org/pypi/openpecha/json) · [toolkit-v2](https://github.com/OpenPecha/toolkit-v2) · [toolkit-v2 layer.py](https://raw.githubusercontent.com/OpenPecha/toolkit-v2/main/src/openpecha/pecha/layer.py) · [toolkit-v2 annotations.py](https://raw.githubusercontent.com/OpenPecha/toolkit-v2/main/src/openpecha/pecha/annotations.py) · [OpenPecha/Toolkit](https://github.com/OpenPecha/Toolkit) · [openpecha-backend](https://github.com/OpenPecha/openpecha-backend) · [annotation/stam](https://github.com/annotation/stam) · [stam PyPI](https://pypi.org/project/stam/) · [TTM stopwords_bo.py](https://huggingface.co/spaces/daniel-wojahn/ttm-webapp-hf/blob/main/pipeline/stopwords_bo.py) · [TibetanTextMetrics Zenodo](https://zenodo.org/records/14992358) · [ACTib v2.0 Zenodo](https://zenodo.org/records/3951503) · [ACM TALLIP Tibetan corpus](https://dl.acm.org/doi/fullHtml/10.1145/3409488) · [Tibetan Language and AI survey](https://arxiv.org/html/2510.19144v1) · [stopwords-iso](https://github.com/stopwords-iso/stopwords-iso) · [UCREL log-likelihood calculator](https://ucrel.lancs.ac.uk/llwizard.html) · [Hardie, Log Ratio](https://cass.lancs.ac.uk/log-ratio-an-informal-introduction/) · [typer PyPI](https://pypi.org/project/typer/) · [click PyPI](https://pypi.org/project/click/) · [pydantic-settings docs](https://pydantic.dev/docs/validation/latest/concepts/pydantic_settings/) · [uv init](https://docs.astral.sh/uv/concepts/projects/init/) · [uv dependencies](https://docs.astral.sh/uv/concepts/projects/dependencies/) · [syrupy](https://github.com/syrupy-project/syrupy) · [pytest-recording](https://github.com/kiwicom/pytest-recording) · [vcrpy](https://github.com/kevin1024/vcrpy) · [vcrpy httpx issue](https://github.com/kevin1024/vcrpy/issues/550) · [Prompty file format](https://prompty.ai/core-concepts/file-format/) · [microsoft/prompty](https://github.com/microsoft/prompty) · [google-genai PyPI](https://pypi.org/pypi/google-genai/json) · [Gemini 3 guide](https://ai.google.dev/gemini-api/docs/gemini-3) · [Gemini structured output](https://ai.google.dev/gemini-api/docs/structured-output) · [Gemini models](https://ai.google.dev/gemini-api/docs/models) · [Gemini JSON Schema announcement](https://blog.google/innovation-and-ai/technology/developers-tools/gemini-api-structured-outputs/) · [MediaWiki API:Edit](https://www.mediawiki.org/wiki/API:Edit) · [MediaWiki REST API Reference](https://www.mediawiki.org/wiki/API:REST_API/Reference) · [Manual:Maxlag](https://www.mediawiki.org/wiki/Manual:Maxlag_parameter) · [Wikimedia User-Agent Policy](https://foundation.wikimedia.org/wiki/Policy:Wikimedia_Foundation_User-Agent_Policy) · [meta Bot policy](https://meta.wikimedia.org/wiki/Bot_policy) · [Manual:Pywikibot/OAuth](https://www.mediawiki.org/wiki/Manual:Pywikibot/OAuth) · [mwclient connecting](https://mwclient.readthedocs.io/en/latest/user/connecting.html) · [WP:Large language models](https://en.wikipedia.org/wiki/Wikipedia:Large_language_models) · [WP:LLM use disclosure](https://en.wikipedia.org/wiki/Wikipedia:LLM_use_disclosure) · [WP:Writing articles with LLMs/RfC](https://en.wikipedia.org/wiki/Wikipedia:Writing_articles_with_large_language_models/RfC) · [HITL platforms 2026](https://www.braintrust.dev/articles/best-human-in-the-loop-llm-evaluation-platforms-2026) · [Reliability patterns for AI pipelines](https://www.gmicloud.ai/en/blog/reliability-patterns-ai-pipelines)