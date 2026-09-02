# Gemini API for Tibetan Encyclopedia-Article Generation — Implementation Research (July 2026)

**Scope:** the article-generation stage only (term extraction → commentary excerpt selection → Tibetan article drafting with per-statement citations). Findings current as of 2026-07-27.

**Headline:** the Gemini API surface changed structurally in H1 2026. `generateContent` is now labelled **Legacy**, and the **Interactions API** is the front door. But the two features this project most needs — **explicit context caching** and the **Batch API** — are *only* available on the legacy path. This is the single biggest architectural decision the repo faces, and it is covered in §4/§5 and the implications list.

---

## 1. SDK: `google-genai` is current; `google-generativeai` is dead

| | |
|---|---|
| Package | `google-genai` |
| Latest version | **2.14.0**, released **2026-07-22** |
| Python | `>=3.10` (3.10–3.14 supported) |
| Install | `pip install -U google-genai` |
| Repo | [googleapis/python-genai](https://github.com/googleapis/python-genai) |

`google-generativeai` is **end-of-life, not merely deprecated**. Its repo has been renamed to [`google-gemini/deprecated-generative-ai-python`](https://github.com/google-gemini/deprecated-generative-ai-python) and states: *"All support for this repository ended permanently on November 30, 2025."* Only critical bug fixes; no new features. Do not use it, do not accept a PR that imports it, and pin `google-genai>=2.14.0` in the repo.

Note the SDK version floor for the current API shape: **v2.0.0+** for the post-May-2026 Interactions schema, and the Interactions API itself needs **2.3.0+** ([interactions overview](https://ai.google.dev/gemini-api/docs/interactions-overview)).

### Client init from `GEMINI_API_KEY`

The client reads `GEMINI_API_KEY` or `GOOGLE_API_KEY` from the environment automatically ([PyPI](https://pypi.org/project/google-genai/)):

```python
import os
from google import genai
from google.genai import types

# Implicit: picks up GEMINI_API_KEY (or GOOGLE_API_KEY) from env
client = genai.Client()

# Explicit, if you'd rather be loud about it:
client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
```

### Minimal generation — two valid call styles

**(a) Interactions API — current, recommended for new projects** ([quickstart](https://ai.google.dev/gemini-api/docs/quickstart)):

```python
interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="ཐེག་པ་ཆེན་པོ་ཞེས་པའི་གོ་དོན་གང་ཡིན་ནམ།",
    system_instruction="You are a Tibetan Buddhist lexicographer. Answer in Tibetan.",
)
print(interaction.output_text)
```

**(b) `generateContent` — Legacy but fully supported, and required for caching/batch** ([SDK docs](https://googleapis.github.io/python-genai/)):

```python
response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents="ཐེག་པ་ཆེན་པོ་ཞེས་པའི་གོ་དོན་གང་ཡིན་ནམ།",
    config=types.GenerateContentConfig(
        system_instruction="You are a Tibetan Buddhist lexicographer. Answer in Tibetan.",
    ),
)
print(response.text)
```

### Interactions API status and the May 2026 breaking change

The Interactions API went **GA in June 2026** and is "recommended for all new projects." `generateContent` "remains fully supported" with **no announced shutdown date** — the [deprecations page](https://ai.google.dev/gemini-api/docs/deprecations) lists model retirements only, no API retirement. The practical read from [API Evangelist](https://apievangelist.com/2026/06/22/google-makes-the-interactions-api-the-front-door-to-gemini/) and [Logicity](https://logicity.in/en/blog/google-replaces-gemini-s-generatecontent-with-interactions-api): generateContent is frozen, not dying — all *new agent* features ship to Interactions only.

If you write Interactions code, be aware of the [May 2026 breaking changes](https://ai.google.dev/gemini-api/docs/interactions-breaking-changes-may-2026) — legacy schema was **permanently removed June 8, 2026**. Any tutorial or LLM-generated snippet older than that is wrong:

- `interaction.outputs` → **`interaction.steps`** (with `type` discriminators: `model_output`, `function_call`, `file_search_call`, …)
- `response_mime_type` (top-level) → folded into **`response_format`**
- Streaming events renamed: `interaction.start` → `interaction.created`, `content.delta` → `step.delta`, `interaction.complete` → `interaction.completed`

---

## 2. Models (2026)

Full list from [ai.google.dev/gemini-api/docs/models](https://ai.google.dev/gemini-api/docs/models). Relevant text models:

| Model ID | Input ctx | Output | Notes |
|---|---|---|---|
| `gemini-3.6-flash` | **1,048,576** | 65,536 | Updated July 2026. Speed/cost-optimised frontier Flash. Default `thinking_level: medium` |
| `gemini-3.5-flash` | **1,048,576** | 65,536 | Updated May 2026. "Sustained frontier-level intelligence"; strongest general reasoning of the Flash line |
| `gemini-3.5-flash-lite` | 1M | 64k | Cheapest 3.5; default `thinking_level: minimal`; "high-volume data analysis and document extraction" |
| `gemini-3.1-flash-lite` | 1M | 64k | **Deprecated**, shutdown ≥ 2027-05-07 → migrate to `gemini-3.5-flash-lite` |
| `gemini-3.1-pro-preview` | — | — | Preview; default `thinking_level: high` |
| `gemini-2.5-pro` / `2.5-flash` / `2.5-flash-lite` | — | — | **Shutdown ≥ 2026-10-16.** Do not build on these |
| `gemini-embedding-2` | — | — | Multimodal embeddings; replaces `text-embedding-004` (shut down 2026-01-14) |

Both 3.6 Flash and 3.5 Flash support: **caching, batch API, structured outputs, file search, function calling, thinking, search/Maps grounding, URL context, flex + priority inference**. ([3.6 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.6-flash), [3.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash))

### Pricing (paid tier, per 1M tokens)

From [ai.google.dev/gemini-api/docs/pricing](https://ai.google.dev/gemini-api/docs/pricing):

| Model | In | Out | Cache read | Cache storage | Batch in | Batch out | Batch cache read |
|---|---|---|---|---|---|---|---|
| `gemini-3.6-flash` | $1.50 | $7.50 | $0.15 | $1.00/1M/hr | $0.75 | $3.75 | $0.075 |
| `gemini-3.5-flash` | $1.50 | $9.00 | $0.15 | $1.00/1M/hr | $0.75 | $4.50 | $0.075 |
| `gemini-3.5-flash-lite` | $0.30 | $2.50 | $0.03 | $1.00/1M/hr | $0.15 | $1.25 | $0.02 |
| `gemini-2.5-pro` | $1.25 / $2.50 (>200k) | $10 / $15 (>200k) | $0.125 / $0.25 | $4.50/1M/hr | $0.625 / $1.25 | $5.00 / $7.50 | — |

Also: `gemini-embedding-2` text $0.20/1M ($0.10 batch); File Search indexing billed at **$0.15/1M tokens**; Google Search grounding free for 5,000 prompts/month shared across Gemini 3, then **$14 per 1,000 search queries**.

**Free tier:** `gemini-3.6-flash` and `gemini-3.5-flash` have free input/output *and free context caching*, but **Batch is not available on free tier** for them. `gemini-3.5-flash-lite` and `gemini-3.1-flash-lite` do have free batch.

### Inference tiers

The [optimization page](https://ai.google.dev/gemini-api/docs/optimization) documents a `service_tier` parameter (also present in `CreateInteraction` per the [API reference](https://ai.google.dev/api/interactions-api)):

| Tier | Cost | Latency |
|---|---|---|
| `priority` | +75–100% | seconds |
| `standard` | 1× | seconds–minutes |
| `flex` | **−50%** | 1–15 min target, preemptible |
| batch | −50% | ≤24 h |
| caching | −90% on cached tokens + prorated storage | faster TTFT |

**Flex is a strong fit for this pipeline** — a semi-automatic offline article generator tolerates 1–15 minute latency, and it stacks the same 50% discount as batch without the JSONL round-trip.

### Which model for long-context Tibetan synthesis

**`gemini-3.5-flash`** for article drafting; **`gemini-3.5-flash-lite`** for term extraction and mechanical passes. Reasoning:

- 3.5 Flash is described as the "most intelligent model for sustained frontier performance," which matters for doctrinal synthesis where a plausible-but-wrong Tibetan sentence is a serious failure. 3.6 Flash is tuned for "code generation, agentic execution, and spatial reasoning" — not your workload — and is cheaper on output ($7.50 vs $9.00), so it's a reasonable A/B candidate but not the obvious default.
- Both give 1M input context, so a 100k+ token commentary payload is comfortable either way.
- Avoid `gemini-2.5-pro`: shutdown ≥ Oct 2026, before your Aug 2026 conference deadline is safely past, and its cache storage is $4.50/1M/hr — **4.5× more expensive** than the Flash line, which wrecks the caching strategy in §4.

### Tibetan / low-resource performance — read this before trusting output

The evidence is genuinely mixed and you should design for verification, not for trust.

**Positive:** Gemini 3 Flash is the strongest available frontier model on low-resource languages. [PolySpeech-100](https://arxiv.org/pdf/2606.01016) reports gemini-3-flash at 85.30% overall across 100+ languages with "consistent performance across both high-resource and low-resource settings." A [round-trip translation study](https://arxiv.org/pdf/2604.12911) puts Gemini-3-Flash at 79.4 average on low-resource sequences vs 64.4 for the next-best (Qwen3.5-397B). On tokenizer efficiency for non-Latin scripts, the Gemini tokenizer "consistently achieves the lowest fertility scores" among frontier tokenizers ([BrahmicTokenizer-131K](https://arxiv.org/abs/2605.29379)).

**Negative and directly relevant:** [TLUE (EMNLP 2025)](https://arxiv.org/abs/2503.12051), a 5-domain / 67-subdomain Tibetan understanding benchmark plus a 7-subdomain Tibetan safety benchmark, found that **most LLMs perform below the random baseline on Tibetan**. That is the single most important number in this section. TLUE is also a ready-made evaluation instrument you can cite in the IATS paper.

An earlier study found Gemini Pro 1.5 was the best of the models tested on Tibetan POS tagging ([Leveraging LLMs in Low-resourced Language NLP: spaCy for Modern Tibetan](https://www.researchgate.net/publication/389451316_Leveraging_Large_Language_Models_in_Low-resourced_Language_NLP_A_spaCy_Implementation_for_Modern_Tibetan)).

Practical conclusion: the model is good enough to *assemble and paraphrase* Tibetan commentary that you put in the context window, and not good enough to be trusted for unsourced Tibetan doctrinal assertion. That is exactly why the "citation for every statement" design is the right one — it converts the task from generation to grounded extraction, which is the regime where the model is strong.

---

## 3. Structured output

Two dialects, depending on which API you call. This is a common source of silent bugs.

**Legacy `generateContent`** — `response_mime_type` + `response_schema`, with **native Pydantic support** (pass the class itself, not `.model_json_schema()`):

```python
from pydantic import BaseModel, Field
from google import genai
from google.genai import types

client = genai.Client()

class KeyTerm(BaseModel):
    tibetan: str = Field(description="The term in Tibetan Unicode.")
    wylie: str = Field(description="EWTS Wylie transliteration.")
    sanskrit: str | None = Field(default=None, description="Sanskrit equivalent if known.")
    root_text_line_ids: list[str] = Field(description="IDs of root-text lines where the term occurs.")
    salience: int = Field(description="1-5; 5 = central doctrinal term.")

class TermList(BaseModel):
    terms: list[KeyTerm]

resp = client.models.generate_content(
    model="gemini-3.5-flash",
    contents=root_text_with_line_ids,
    config=types.GenerateContentConfig(
        system_instruction="Extract key doctrinal terms. Tibetan output only.",
        response_mime_type="application/json",
        response_schema=TermList,          # Pydantic class accepted directly
    ),
)
terms = TermList.model_validate_json(resp.text)
```

**Interactions API** — everything moves into `response_format`, and you pass the **JSON Schema dict**:

```python
interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input=root_text_with_line_ids,
    system_instruction="Extract key doctrinal terms. Tibetan output only.",
    response_format={
        "type": "text",
        "mime_type": "application/json",
        "schema": TermList.model_json_schema(),
    },
)
terms = TermList.model_validate_json(interaction.output_text)
```

Per the [breaking-changes guide](https://ai.google.dev/gemini-api/docs/interactions-breaking-changes-may-2026), top-level `response_mime_type` was **removed** from Interactions. The [structured output docs](https://ai.google.dev/gemini-api/docs/generate-content/structured-output) note `interaction.output_parsed` is **not** documented — parse manually with `model_validate_json`.

**Supported schema surface:** primitives (`string`, `number`, `integer`, `boolean`, `null`), composites (`object`, `array`), descriptors (`title`, `description`, `enum`, `format`, `minimum`, `maximum`), plus `$ref` for recursive structures and `anyOf` for variants. Structured output composes with Google Search, URL Context, Code Execution and **File Search** on Gemini 3+ models. `propertyOrdering` is only required on the 2.0 series.

**Reliability caveats, verbatim from the docs:** "Not all JSON Schema features are supported"; "Very large or deeply nested schemas may be rejected"; and critically, structured output "does not guarantee the values are semantically correct." For this project that means: the schema guarantees you get a `source_id` field, it does **not** guarantee the `source_id` refers to a real chunk. You must validate every emitted ID against your own chunk table and reject/retry the article on any miss. Treat that validator as a first-class repo component, not an afterthought.

---

## 4. Long context and caching — the money question

### Implicit vs explicit

**Implicit caching** is on by default for all Gemini 2.5+ models, no configuration, **no guaranteed savings** ([caching docs](https://ai.google.dev/gemini-api/docs/caching)). Minimum input before it can engage:

| Model | Min tokens |
|---|---|
| Gemini 3.5 Flash | **4,096** |
| Gemini 3.1 Pro Preview | 4,096 |
| Gemini 2.5 Flash / Pro | 2,048 |

To maximise implicit hits: put the large, stable content **at the very beginning of the prompt**, and send similar requests in quick succession. Check `interaction.usage.total_cached_tokens` to see whether it actually fired.

**Explicit caching** gives *guaranteed* cost reduction — and is **not available in the Interactions API**. From the [Interactions caching page](https://ai.google.dev/gemini-api/docs/caching): *"Explicit caching (manually creating and managing cache objects) is not supported in the Interactions API."* The [interactions overview](https://ai.google.dev/gemini-api/docs/interactions-overview) lists explicit caching, the Batch API, and Python automatic function calling as generateContent features "not yet available in the Interactions API."

### Explicit caching API (legacy path)

From [ai.google.dev/gemini-api/docs/generate-content/caching](https://ai.google.dev/gemini-api/docs/generate-content/caching):

```python
from google import genai
from google.genai import types

client = genai.Client()
MODEL = "gemini-3.5-flash"

# Build the cache once per commentary corpus.
# Chunk IDs must be baked into the text — they are what the model cites.
corpus_text = "\n\n".join(
    f"[[{c.id}]] {c.text}" for c in commentary_chunks
)

cache = client.caches.create(
    model=MODEL,
    config=types.CreateCachedContentConfig(
        display_name="madhyamakavatara-commentaries-v1",
        system_instruction=(
            "You are a Tibetan Buddhist lexicographer writing encyclopedia entries. "
            "Every factual sentence MUST end with one or more source markers of the "
            "form [[chunk_id]] copied verbatim from the corpus. Never invent an id. "
            "If the corpus does not support a claim, omit the claim."
        ),
        contents=[corpus_text],
        ttl="21600s",          # 6 hours
    ),
)
print(cache.name, cache.usage_metadata)

# Reuse across every term in the run
resp = client.models.generate_content(
    model=MODEL,
    contents=f"Write the encyclopedia article for the term: {term.tibetan}",
    config=types.GenerateContentConfig(cached_content=cache.name),
)

# Lifecycle
client.caches.update(name=cache.name, config=types.UpdateCachedContentConfig(ttl="3600s"))
for c in client.caches.list():
    print(c.name, c.display_name, c.expire_time)
client.caches.delete(cache.name)
```

**TTL:** defaults to **1 hour** if unset; the docs state there are **no minimum or maximum bounds**. `expire_time` is an absolute-timestamp alternative. `caches.update()` can only change `ttl`/`expire_time` — content is immutable, so a corpus edit means a new cache.

**Minimum tokens to create a cache:** same table as implicit — **4,096 for Gemini 3.5 Flash**. A 100k+ token commentary corpus clears this by 25×.

### Cost model for your actual workload

Assume a 300k-token commentary corpus and 200 term articles at ~4k output tokens each, on `gemini-3.5-flash`:

| Strategy | Input cost | Output cost | Total |
|---|---|---|---|
| Naive (resend corpus per term) | 60M × $1.50 = **$90.00** | 0.8M × $9.00 = $7.20 | **~$97** |
| Explicit cache, standard tier | 60M × $0.15 = $9.00 + storage (0.3M × $1.00 × 8h = $2.40) = **$11.40** | $7.20 | **~$19** |
| Explicit cache + Batch | 60M × $0.075 = $4.50 + $2.40 storage = **$6.90** | 0.8M × $4.50 = $3.60 | **~$11** |

Explicit caching is roughly an **8× cost reduction**; adding batch makes it ~9×. Two warnings: (a) **thinking tokens are billed as output tokens** (§ below), so with `thinking_level: high` the output column can be several times larger than the visible article length; (b) storage is billed per token-hour whether or not you're generating, so tear down caches at the end of a run — don't leave a 300k-token cache alive overnight for $0.30/hr × 12h = $3.60 of nothing.

### The alternative: File Search (native RAG with citations)

[File Search](https://ai.google.dev/gemini-api/docs/file-search) is Google-managed RAG and is arguably a better fit than caching for the *commentary-excerpt* stage, because it returns **native citations** rather than relying on the model to copy your IDs correctly.

```python
store = client.file_search_stores.create(
    config={"display_name": "kangyur-commentaries",
            "embedding_model": "models/gemini-embedding-2"}
)

op = client.file_search_stores.upload_to_file_search_store(
    file="commentary_01.txt",
    file_search_store_name=store.name,
    config={
        "display_name": "Candrakirti-autocommentary",
        "chunking_config": {
            "white_space_config": {"max_tokens_per_chunk": 200,
                                   "max_overlap_tokens": 20}
        },
    },
)
while not op.done:
    time.sleep(5)
    op = client.operations.get(op)

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input=f"ཐེག་པ་ཆེན་པོ། — write an encyclopedia article.",
    tools=[{"type": "file_search",
            "file_search_store_names": [store.name]}],
)

for step in interaction.steps:
    if step.type == "model_output":
        for block in step.content:
            if getattr(block, "annotations", None):
                for a in block.annotations:
                    if a.type == "file_citation":
                        print(a.file_name, a.source,
                              getattr(a, "page_number", None))
```

Stores persist indefinitely (raw Files API uploads are deleted after 48 h). Storage limits: **Free 1 GB / Tier 1 10 GB / Tier 2 100 GB / Tier 3 1 TB**; max 100 MB per document. Pricing: you pay **only for indexing embeddings ($0.15/1M tokens)**; storage and query-time embeddings are free; retrieved chunks bill as normal input tokens.

**Caveat for Tibetan:** `max_tokens_per_chunk: 200` is tuned for English. Given Tibetan's tokenization behaviour (§8), 200 tokens may be only a line or two of Tibetan. Calibrate chunk size empirically with `count_tokens` against actual Tibetan text before committing to a chunking config, and consider chunking on Tibetan structural boundaries (ཤད་ `།` / paragraph) rather than whitespace.

---

## 5. Batch API

Yes, **50% discount, 24-hour SLO** ([batch docs](https://ai.google.dev/gemini-api/docs/batch-api)). Note it is a **generateContent-shaped** API — batch is on the list of things not yet in Interactions.

```python
# Inline (< 20 MB)
inline_requests = [
    {"contents": [{"parts": [{"text": f"Article for term: {t}"}],
                   "role": "user"}],
     "config": {"cached_content": cache.name,
                "response_mime_type": "application/json",
                "response_schema": Article.model_json_schema()}}
    for t in terms
]

job = client.batches.create(
    model="gemini-3.5-flash",
    src=inline_requests,
    config={"display_name": "iats-terms-run-01"},
)

while job.state.name not in ("JOB_STATE_SUCCEEDED", "JOB_STATE_FAILED",
                             "JOB_STATE_CANCELLED", "JOB_STATE_EXPIRED"):
    time.sleep(30)
    job = client.batches.get(name=job.name)
```

For >20 MB, upload a **JSONL** file via the Files API (max 2 GB):

```json
{"key": "term-001", "request": {"contents": [{"parts": [{"text": "..."}]}]}}
{"key": "term-002", "request": {"contents": [{"parts": [{"text": "..."}]}]}}
```

The `key` is user-defined and is how you map results back to terms — use your term ID, not an array index.

**Confirmed working with batch:** context caching (pass `cached_content` in each request config) **and** structured output (`response_mime_type` + `response_schema`). That combination is what makes the ~$11 number in §4 reachable.

**Limits:** 100 concurrent batch jobs on every tier, 2 GB input file, 20 GB file storage, results retained **6 weeks**. Enqueued-token limits are per model per tier ([rate limits](https://ai.google.dev/gemini-api/docs/rate-limits)).

**Honest assessment:** for ~200 articles, `service_tier="flex"` gets you the same 50% discount with 1–15 minute latency and no JSONL/polling/result-mapping machinery. Reach for batch only if the term list grows into the thousands. Also remember batch is **not on the free tier** for 3.5/3.6 Flash.

---

## 6. Grounding and per-statement citations

### Turn Google Search grounding OFF

Google Search grounding is enabled purely by presence of the tool — **omit `tools` and it does not run** ([grounding docs](https://ai.google.dev/gemini-api/docs/google-search)). For this project it is actively harmful: it would let web content leak into articles that must be sourced to specific Tibetan commentaries, and it costs $14/1,000 queries after the free 5,000/month. Assert in code that `tools` contains no `google_search` for any article-generation call.

### Two viable citation architectures

**Architecture A — File Search native citations.** Highest integrity: annotations of `type: "file_citation"` carry `file_name`, `source`, and `page_number`/`media_id`, produced by the retrieval layer rather than by the model's token stream. The model cannot hallucinate a `file_citation` annotation the way it can hallucinate an inline `[[id]]` string. **Cost:** granularity is whatever your chunking produced, and Google's retriever decides what gets retrieved — you lose control over "cite this exact commentary line."

**Architecture B — inline ID markers over a cached corpus.** Full control of granularity and pairs with explicit caching. **Cost:** the IDs are model-generated text and *will* sometimes be fabricated or misattributed. Requires a hard validator.

For a project whose entire credibility rests on "a citation for every statement," the right answer is **both**: A for retrieval integrity, B for line-level granularity, with a deterministic validation gate between generation and any Wikipedia write.

### Prompt engineering for verifiable source IDs

Practices that measurably help:

1. **Put the ID adjacent to the text it labels**, on every chunk: `[[cmt3.f142a.l4]] <Tibetan text>`. Do not use a separate legend the model must cross-reference.
2. **Use opaque, high-entropy, copy-only IDs.** Sequential integers invite the model to interpolate `[[47]]` when it saw 46 and 48. A structured token like `cmt3.f142a.l4` is hard to fabricate plausibly and trivial to regex-validate.
3. **Force citation into the schema, not the prose.** Instead of asking for Markdown with inline brackets, make each statement an object:

```python
class Statement(BaseModel):
    tibetan: str = Field(description="One assertion, in Tibetan. No citations inline.")
    source_ids: list[str] = Field(description="Verbatim chunk ids supporting this exact sentence. Must be non-empty.")
    supporting_quote: str = Field(description="Verbatim Tibetan span copied from the cited chunk.")

class Article(BaseModel):
    term_tibetan: str
    summary: list[Statement]
    sections: list[Section]
```

The `supporting_quote` field is the highest-leverage trick here: it is **mechanically checkable**. Post-generation, assert `supporting_quote in chunk_table[source_id].text` (after Unicode NFC normalisation). A fabricated citation almost never survives this test, and it costs you nothing but output tokens. Statements failing the check get dropped or re-generated — never published.

4. **Instruct explicit abstention:** "If the corpus does not support a claim, omit the claim." Combined with a non-empty `source_ids` constraint, this is what keeps unsourced doctrinal assertion out of Tibetan Wikipedia.
5. **Set `thinking_level: "medium"` or `"high"`** for the drafting call. The [thinking docs](https://ai.google.dev/gemini-api/docs/thinking) note that low thinking causes premature termination in multi-step reasoning; faithful attribution across a 300k-token corpus is exactly that kind of task. Budget for it — thinking tokens bill as output.

---

## 7. Safety filters and Buddhist doctrinal content

**Good news, and it inverts the assumption in the brief:** per the [safety settings docs](https://ai.google.dev/gemini-api/docs/safety-settings), *"The default block threshold is Off for Gemini 2.5 and 3 models."* The four adjustable categories do not block by default on the models you'll use. Non-configurable core-harm protections (e.g. child safety) remain always on and cannot be disabled by any setting.

Adjustable categories: `HARM_CATEGORY_HARASSMENT`, `HARM_CATEGORY_HATE_SPEECH`, `HARM_CATEGORY_SEXUALLY_EXPLICIT`, `HARM_CATEGORY_DANGEROUS`.
Thresholds: `OFF`, `BLOCK_NONE`, `BLOCK_ONLY_HIGH`, `BLOCK_MEDIUM_AND_ABOVE`, `BLOCK_LOW_AND_ABOVE`, `HARM_BLOCK_THRESHOLD_UNSPECIFIED`.

**Residual risk is real but narrow.** `HARM_CATEGORY_HARASSMENT` covers content targeting protected attributes *including religion*, and academic or historical quotation can trip filters ([discussion](https://help.apiyi.com/en/gemini-api-safety-settings-block-none-guide-en.html)). Tibetan Buddhist commentarial literature contains wrathful-deity iconography, polemic against non-Buddhist schools (tīrthika refutation), tantric sexual symbolism, and Vinaya passages enumerating transgressions — all of which are plausible false-positive triggers. The [TLUE](https://arxiv.org/abs/2503.12051) authors thought Tibetan safety behaviour distinctive enough to build a 7-subdomain Tibetan safety benchmark, which is a signal in itself.

Set thresholds explicitly rather than relying on the default — defaults change, and an explicit setting is self-documenting:

```python
SAFETY = [
    types.SafetySetting(category=c, threshold=types.HarmBlockThreshold.OFF)
    for c in (
        types.HarmCategory.HARM_CATEGORY_HARASSMENT,
        types.HarmCategory.HARM_CATEGORY_HATE_SPEECH,
        types.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT,
        types.HarmCategory.HARM_CATEGORY_DANGEROUS,
    )
]

resp = client.models.generate_content(
    model="gemini-3.5-flash",
    contents=prompt,
    config=types.GenerateContentConfig(cached_content=cache.name,
                                       safety_settings=SAFETY),
)
```

`safety_settings` is also a top-level field on `CreateInteraction` ([reference](https://ai.google.dev/api/interactions-api)).

Always handle blocks rather than assuming `.text` exists — a silent `None` in a batch of 200 is easy to miss:

```python
if resp.prompt_feedback and resp.prompt_feedback.block_reason:
    log.error("prompt blocked: %s", resp.prompt_feedback.block_reason)
cand = resp.candidates[0]
if cand.finish_reason == "SAFETY":
    log.error("response blocked: %s", cand.safety_ratings)
```

A `SAFETY` block on a canonical Buddhist text is itself a publishable finding for the IATS paper — log every one with the triggering passage.

---

## 8. Token counting for Tibetan

`count_tokens` exists and is **input-only**. Note the method lives on `client.models` even when you're using the Interactions API — there is **no** `client.interactions.count_tokens()` ([tokens docs](https://ai.google.dev/gemini-api/docs/interactions/tokens)):

```python
n = client.models.count_tokens(model="gemini-3.5-flash", contents=tibetan_text)
print(n.total_tokens)
```

Post-hoc usage from an interaction: `total_input_tokens`, `total_output_tokens`, `total_thought_tokens`, `total_cached_tokens`, `total_tool_use_tokens`, `total_tokens`, plus `input_tokens_by_modality`. On the legacy path: `response.usage_metadata`.

**Tokens per Tibetan syllable — the honest answer is that Google does not publish it.** The [tokens docs](https://ai.google.dev/gemini-api/docs/tokens) give only "~4 characters per token" and "100 tokens ≈ 60–80 English words," and explicitly do not address non-Latin scripts.

What the literature says, with appropriate caution:

- Tokenizer **fertility** (mean sub-word tokens per word) across a set of low-resource languages ranges from **4.1 (Pashto) to 19.9 (Tibetan)** — Tibetan the worst measured. Reported in the low-resource benchmarking literature surfaced above; I could not extract the table from the PDF to confirm *which* tokenizer produced 19.9, so treat it as an order-of-magnitude signal, not a Gemini-specific constant. Contrast English at ~1.23 tokens/word for `o200k_base` ([BrahmicTokenizer-131K](https://arxiv.org/abs/2605.29379)).
- Gemini's tokenizer is the **best of the frontier tokenizers** on non-Latin scripts (e.g. F 1.76 on Bengali, 24% better than GPT-4.1 Mini, 36% better than Llama 4), so Gemini's Tibetan fertility is likely materially better than 19.9 — but still far above English.
- Mechanically: Tibetan occupies U+0F00–U+0FFF ([Unicode block](https://en.wikipedia.org/wiki/Tibetan_(Unicode_block))), **3 bytes per character in UTF-8**. A byte-level BPE with thin Tibetan vocabulary coverage degrades toward ~1 token per byte, i.e. **up to ~3 tokens per Tibetan character** in the worst case.

**Do not estimate — measure.** Ship a calibration script in the repo:

```python
import statistics
from google import genai

client = genai.Client()

def calibrate(samples: list[str], model="gemini-3.5-flash"):
    rows = []
    for s in samples:
        t = client.models.count_tokens(model=model, contents=s).total_tokens
        syllables = s.count("་") + s.count("།")   # tsheg + shad as syllable proxy
        rows.append({
            "chars": len(s),
            "utf8_bytes": len(s.encode("utf-8")),
            "syllables": syllables,
            "tokens": t,
            "tok_per_char": t / max(len(s), 1),
            "tok_per_syllable": t / max(syllables, 1),
        })
    print("median tokens/char:", statistics.median(r["tok_per_char"] for r in rows))
    print("median tokens/syllable:", statistics.median(r["tok_per_syllable"] for r in rows))
    return rows
```

Run it over representative Kangyur, Tengyur, and modern-Tibetan samples separately — classical orthography and modern prose will not have the same ratio, and the number determines your chunk sizes, your context budget, and your cost model. It is also a small, genuinely novel empirical contribution for the IATS paper: **published tokenization-efficiency figures for classical Tibetan on a frontier model do not appear to exist.**

---

## Implementation implications

- **Pin `google-genai>=2.14.0`; ban `google-generativeai` in CI.** The old SDK's support ended 2025-11-30. Add a lint rule or `pip-audit`-style check — LLM-assisted contributors will reach for the dead package because it dominates pre-2025 training data.
- **Choose the legacy `generateContent` path as the primary article-generation call, deliberately and with a comment explaining why.** Explicit caching and Batch — the two features that make a 300k-token corpus × 200 terms economically sane — are *not* in the Interactions API. Isolate all Gemini calls behind one `GeminiClient` wrapper module so the eventual Interactions migration is a single-file change, and re-check this decision before the Aug 2026 conference.
- **Adopt File Search for retrieval-with-citations *in addition to* the cached corpus**, not instead of it. Native `file_citation` annotations cannot be hallucinated; inline `[[id]]` markers can. Accept the two-API split (File Search requires Interactions, caching requires generateContent) as a deliberate stage boundary: File Search for excerpt selection, cached generateContent for drafting.
- **Make `supporting_quote` a required schema field on every statement, and gate publication on a verbatim substring match against the chunk table** (NFC-normalised). This is the mechanism that turns "citation for every statement" from a prompt request into an enforced invariant. Nothing reaches bo.wikipedia.org without passing it.
- **Use opaque structured chunk IDs (`cmt3.f142a.l4`), never sequential integers.** Sequential IDs are interpolatable; opaque ones are copy-only and regex-validatable.
- **Default `gemini-3.5-flash` for drafting, `gemini-3.5-flash-lite` for term extraction; make the model ID a config value.** Explicitly forbid `gemini-2.5-*` (shutdown ≥ 2026-10-16) and `gemini-3.1-flash-lite` (deprecated).
- **Strip `temperature`, `top_p`, `top_k`, and `candidate_count` from all configs.** They are ignored on Gemini 3.x today and will return HTTP 400 on future models. Use `system_instruction` for determinism instead. Also: never end a request with a model-role turn — prefilled model turns now 400.
- **Use `thinking_level` (`"minimal"`/`"low"`/`"medium"`/`"high"`), never `thinking_budget`** — sending both is an HTTP 400. Set `"medium"` or `"high"` for drafting, `"minimal"` for extraction. Budget for thinking tokens: they bill at output rates and are invisible in the article length.
- **Start with `service_tier="flex"` (50% off, 1–15 min) rather than building batch infrastructure.** Add the Batch API only if the term list exceeds ~1,000. Note batch is unavailable on the free tier for 3.5/3.6 Flash.
- **Treat cache lifecycle as owned state:** create per corpus version with an explicit `ttl` (default is only 1 hour), record `cache.name` in a run manifest, and `caches.delete()` in a `finally` block. Storage bills per token-hour whether or not you generate. Cache content is immutable — a corpus edit means a new cache.
- **Order every prompt as [cached corpus] → [term instruction]** so implicit caching can also engage, and assert `usage.total_cached_tokens > 0` in tests to catch the day a refactor silently breaks cache hits.
- **Set all four `safety_settings` explicitly to `OFF` rather than relying on the Gemini 3 default**, and log every `finish_reason == "SAFETY"` / `block_reason` with the triggering passage. Wrathful iconography, tīrthika polemic, tantric symbolism, and Vinaya enumerations are plausible false-positive triggers; each block is also a paper-worthy data point.
- **Assert that no article-generation call passes a `google_search` tool.** Web content must not leak into commentary-grounded articles, and it costs $14/1k queries past the free 5,000/month.
- **Ship a Tibetan tokenization calibration script and run it before fixing any chunk size or context budget.** Google publishes no Tibetan ratio; fertility for Tibetan is reported as the worst among low-resource languages (~19.9 vs ~1.23 for English), and UTF-8 Tibetan is 3 bytes/char. Chunking configs tuned on English (`max_tokens_per_chunk: 200`) will be badly wrong. Chunk on ཤད་/tsheg boundaries, not whitespace.
- **Require a paid-tier API key and fail fast if billing is not enabled.** Free-tier content may be used to improve Google's products; paid-tier content is not. Unpublished OpenPecha commentary corpora should never transit the free tier. Also set `store=False` on any Interactions call you don't want persisted server-side — it defaults to `true`.
- **Do not read rate limits from documentation.** Google no longer publishes per-model RPM/TPM/RPD tables; they are visible only in AI Studio for your project. Implement exponential backoff on 429 and make concurrency a config value discovered empirically.
- **Design the pipeline around TLUE's finding that most LLMs score below random baseline on Tibetan.** Human review by a Tibetan-literate reviewer is a required pipeline stage, not an optional one — and TLUE is a ready-made citable evaluation instrument for the IATS paper's methodology section.

**Sources:** [Gemini quickstart](https://ai.google.dev/gemini-api/docs/quickstart) · [google-genai on PyPI](https://pypi.org/project/google-genai/) · [python-genai SDK docs](https://googleapis.github.io/python-genai/) · [python-genai releases](https://github.com/googleapis/python-genai/releases) · [deprecated-generative-ai-python](https://github.com/google-gemini/deprecated-generative-ai-python) · [Models](https://ai.google.dev/gemini-api/docs/models) · [Gemini 3.6 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.6-flash) · [Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash) · [Pricing](https://ai.google.dev/gemini-api/docs/pricing) · [Changelog](https://ai.google.dev/gemini-api/docs/changelog) · [Deprecations](https://ai.google.dev/gemini-api/docs/deprecations) · [Interactions overview](https://ai.google.dev/gemini-api/docs/interactions-overview) · [Interactions API reference](https://ai.google.dev/api/interactions-api) · [May 2026 breaking changes](https://ai.google.dev/gemini-api/docs/interactions-breaking-changes-may-2026) · [Latest-model migration](https://ai.google.dev/gemini-api/docs/latest-model) · [Structured output (legacy)](https://ai.google.dev/gemini-api/docs/generate-content/structured-output) · [Structured output (Interactions)](https://ai.google.dev/gemini-api/docs/structured-output) · [Caching (Interactions)](https://ai.google.dev/gemini-api/docs/caching) · [Caching (legacy)](https://ai.google.dev/gemini-api/docs/generate-content/caching) · [Batch API](https://ai.google.dev/gemini-api/docs/batch-api) · [File Search](https://ai.google.dev/gemini-api/docs/file-search) · [Google Search grounding](https://ai.google.dev/gemini-api/docs/google-search) · [Thinking](https://ai.google.dev/gemini-api/docs/thinking) · [Safety settings](https://ai.google.dev/gemini-api/docs/safety-settings) · [Tokens](https://ai.google.dev/gemini-api/docs/tokens) · [Tokens (Interactions)](https://ai.google.dev/gemini-api/docs/interactions/tokens) · [Rate limits](https://ai.google.dev/gemini-api/docs/rate-limits) · [Optimization/inference tiers](https://ai.google.dev/gemini-api/docs/optimization) · [Files API](https://ai.google.dev/gemini-api/docs/files) · [TLUE benchmark](https://arxiv.org/abs/2503.12051) · [PolySpeech-100](https://arxiv.org/pdf/2606.01016) · [Round-Trip Translation](https://arxiv.org/pdf/2604.12911) · [BrahmicTokenizer-131K](https://arxiv.org/abs/2605.29379) · [Tibetan Unicode block](https://en.wikipedia.org/wiki/Tibetan_(Unicode_block)) · [Gemini 3.6 Flash dev guide](https://dev.to/googleai/gemini-36-flash-35-flash-lite-developer-guide-268i) · [API Evangelist on Interactions](https://apievangelist.com/2026/06/22/google-makes-the-interactions-api-the-front-door-to-gemini/)