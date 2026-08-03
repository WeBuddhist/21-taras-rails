"""Stages 4–7: extract → claims → outline → draft [→ polish] → audit → verify, per term.

Each stage takes the previous stage's artifact off disk and writes its own, so a run is
resumable and every intermediate is inspectable. The ledger records where each term got to.

The claims stage (4b) is the canonical pipeline's hinge (docs/reference/cowork-pipeline.md,
load-bearing invariant 1): passages are converted to an atomic claims table — one verifiable
fact per row, own words, claim-typed and reception-tagged — and from then on **the claims
table is the only drafting input**. The drafting model never sees source wording again;
quotations enter the article only through code, which expands each cited claim to the
passages behind it. The audit stage (6b) is invariant 2: the drafted text is read back
sentence-by-sentence against the claims table, and added facts or attribution loss block
publication.

The division of labour between model and code is deliberate and is the whole safety argument:
the model decides *which* passages matter and *how* to arrange them — but it is never trusted.
Stage 7 re-reads every quotation from the commentary file it claims to come from, with no LLM
involved. A citation that cannot be found character-for-character fails the build, so the
worst a hallucinating model can do is stop the pipeline, never publish a fabricated source.
The LLM audit complements that gate (it reads meaning, which the gate cannot); it never
replaces it.
"""

from __future__ import annotations

import json
import shutil
from dataclasses import dataclass, asdict, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable, Sequence

from ..registry import Registry, find_term, resolve_citation_url
from ..tibetan.verify import check_quote
from ..wiki.merge import (
    MergeResult,
    MergeVerification,
    apply_operations,
    parse_operations,
    verify_merged,
)
from ..wiki.wikitext import Article, Citation, Section, render_article, render_ref
from ..wiki.validator import Finding, validate
from .align import AlignmentReport, AlignedSpan, TermSegment, segments_for_term

# Structured-output schemas. Gemini is told to return exactly these shapes, which removes a
# whole class of parsing failure and — more importantly — forces the model to attach a
# source_id and a quote to every claim rather than writing free prose we would have to
# reverse-engineer citations out of.

EXTRACT_SCHEMA: dict[str, Any] = {
    "type": "object",
    "properties": {
        "term": {"type": "string"},
        "passages": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "source_id": {"type": "string"},
                    "segment_id": {"type": "string"},
                    "quote": {"type": "string"},
                    "kind": {"type": "string"},
                    "note": {"type": "string"},
                },
                "required": ["source_id", "quote", "kind"],
            },
        },
        "no_explanation_in": {"type": "array", "items": {"type": "string"}},
    },
    "required": ["term", "passages"],
}

CLAIMS_SCHEMA: dict[str, Any] = {
    "type": "object",
    "properties": {
        "term": {"type": "string"},
        "claims": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "id": {"type": "string"},
                    "claim_bo": {"type": "string"},
                    "passage_indices": {"type": "array", "items": {"type": "integer"}},
                    "claim_type": {"type": "string"},
                    "school": {"type": "string"},
                    "reception": {"type": "string"},
                    "contested": {"type": "boolean"},
                    "copyright_only": {"type": "boolean"},
                },
                "required": ["id", "claim_bo", "passage_indices", "claim_type"],
            },
        },
        "forbidden_syntheses": {"type": "array", "items": {"type": "string"}},
    },
    "required": ["term", "claims"],
}

ORGANIZE_SCHEMA: dict[str, Any] = {
    "type": "object",
    "properties": {
        "term": {"type": "string"},
        "lead": {"type": "array", "items": {"type": "integer"}},
        "sections": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "heading": {"type": "string"},
                    "claim_indices": {"type": "array", "items": {"type": "integer"}},
                    "divergence": {"type": "boolean"},
                    "attribution_required": {"type": "boolean"},
                },
                "required": ["heading", "claim_indices"],
            },
        },
        "unused": {"type": "array", "items": {"type": "integer"}},
        "unused_reason": {"type": "string"},
        "gap_report": {"type": "array", "items": {"type": "string"}},
    },
    "required": ["term", "lead", "sections"],
}

AUDIT_SCHEMA: dict[str, Any] = {
    "type": "object",
    "properties": {
        "term": {"type": "string"},
        "findings": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "sentence": {"type": "string"},
                    "claim_indices": {"type": "array", "items": {"type": "integer"}},
                    "finding": {"type": "string"},
                    "severity": {"type": "string"},
                    "note": {"type": "string"},
                },
                "required": ["sentence", "finding", "severity"],
            },
        },
        "verdict": {"type": "string"},
    },
    "required": ["term", "findings", "verdict"],
}

DRAFT_SCHEMA: dict[str, Any] = {
    "type": "object",
    "properties": {
        "lead": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "text": {"type": "string"},
                    "citations": {"type": "array", "items": {"type": "integer"}},
                },
                "required": ["text", "citations"],
            },
        },
        "sections": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "heading": {"type": "string"},
                    "paragraphs": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "text": {"type": "string"},
                                "citations": {"type": "array", "items": {"type": "integer"}},
                            },
                            "required": ["text", "citations"],
                        },
                    },
                },
                "required": ["heading", "paragraphs"],
            },
        },
        "see_also": {"type": "array", "items": {"type": "string"}},
    },
    "required": ["lead", "sections"],
}


UPDATE_SCHEMA: dict[str, Any] = {
    "type": "object",
    "properties": {
        "term": {"type": "string"},
        "operations": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "kind": {"type": "string"},
                    "section_anchor": {"type": "string"},
                    "existing_text": {"type": "string"},
                    "new_text": {"type": "string"},
                    "citation": {
                        "type": "object",
                        "properties": {
                            "source_id": {"type": "string"},
                            "quote": {"type": "string"},
                            "page": {"type": "string"},
                        },
                        "required": ["source_id", "quote"],
                    },
                    "rationale": {"type": "string"},
                },
                "required": ["kind", "section_anchor"],
            },
        },
        "conflicts_for_human": {"type": "array", "items": {"type": "string"}},
    },
    "required": ["term", "operations"],
}


@dataclass
class Passage:
    """One cited stretch of commentary about a term."""

    source_id: str
    quote: str
    kind: str = ""
    segment_id: str = ""
    note: str = ""

    def to_dict(self) -> dict:
        return asdict(self)


@dataclass
class Claim:
    """One atomic claim — a single verifiable fact, in the pipeline's own words.

    ``passage_indices`` is the provenance link back into ``extract.json``: the passages
    whose wording the claim was distilled from, and therefore the quotations its citations
    will carry. A claim with no passages cannot be cited and is dropped at parse time —
    the claims table is the only drafting input, so an unsupported claim here would be an
    unsupported sentence in the article.
    """

    id: str
    claim_bo: str
    passage_indices: list[int] = field(default_factory=list)
    claim_type: str = "single-commentator"
    school: str = ""
    reception: str = ""
    contested: bool = False
    copyright_only: bool = False

    def to_dict(self) -> dict:
        return asdict(self)


@dataclass
class TermArtifacts:
    """Where one term's files live under ``corpora/<id>/articles/<term>/``."""

    root: Path

    @property
    def extract(self) -> Path:
        return self.root / "extract.json"

    @property
    def claims(self) -> Path:
        """The atomic claims table (stage 4b) — the only drafting input downstream."""
        return self.root / "claims.json"

    @property
    def sections(self) -> Path:
        return self.root / "sections.json"

    @property
    def draft(self) -> Path:
        return self.root / "draft.json"

    @property
    def polished(self) -> Path:
        """The literary rewrite (stage 6a), kept separate: per-stage outputs are
        immutable so the audit can say which stage introduced a drift."""
        return self.root / "draft_polished.json"

    @property
    def audit(self) -> Path:
        return self.root / "audit.json"

    @property
    def audit_report(self) -> Path:
        return self.root / "audit.md"

    @property
    def wikitext(self) -> Path:
        return self.root / "article.wiki"

    @property
    def citations(self) -> Path:
        return self.root / "citations.json"

    @property
    def report(self) -> Path:
        return self.root / "report.md"

    @property
    def model(self) -> Path:
        """Which model and which prompt versions produced these artifacts.

        Written on every run. An article directory that does not say what made it
        is a paper citation waiting to be wrong — the second session's articles
        were Claude standing in for a proxied-out Gemini, and only a file like
        this kept that from being reported as a Gemini result.
        """
        return self.root / "model.json"

    @property
    def existing_wiki(self) -> Path:
        """Snapshot of the live article an update ran against."""
        return self.root / "existing.wiki"

    @property
    def update_ops(self) -> Path:
        """The model's raw classification payload, for audit."""
        return self.root / "update_ops.json"

    @property
    def update_report(self) -> Path:
        """The merge report: applied/skipped ops, ⚑ conflicts, and the diff."""
        return self.root / "update_report.md"

    def ensure(self) -> None:
        self.root.mkdir(parents=True, exist_ok=True)


def preserve_artifact(path: Path) -> None:
    """Before a re-run overwrites a per-stage artifact, keep the outgoing version.

    Stages used to overwrite in place, which destroyed exactly the record the
    step-13 feedback loop and the paper's pass-rate reporting need — audit rounds,
    pre-fix drafts, superseded verification reports (the tara21 review lost the
    intermediate audit rounds this way; see corpora/tara21/REVIEW-2026-08-02.md).
    Every prior version now lands beside the artifact in
    ``history/<name>.<UTC-stamp>[-n].<ext>``, so a re-run can never silently
    discard evidence. ``model.json``'s *merge* writes are exempt — they accumulate
    rather than replace — but a full reset of it is preserved (see cli.article).
    """
    if not path.exists():
        return
    history = path.parent / "history"
    history.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    target = history / f"{path.stem}.{stamp}{path.suffix}"
    n = 1
    while target.exists():
        target = history / f"{path.stem}.{stamp}-{n}{path.suffix}"
        n += 1
    shutil.copy2(path, target)


def _write_json(path: Path, data: Any, *, preserve: bool = True) -> None:
    if preserve:
        preserve_artifact(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")


def _write_text(path: Path, text: str) -> None:
    """Artifact text writer — same preservation contract as :func:`_write_json`."""
    preserve_artifact(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def record_stage_model(
    artifacts: TermArtifacts, stage: str, *, model: str, prompt: str, run_at: str
) -> None:
    """Merge one stage's model id and prompt file into ``model.json``.

    Every entry point that runs a model stage calls this — the full chain, the
    standalone subcommands, and ``scripts/gemini_polish.py``. The canonical
    pipeline requires the model version to be pinned and logged *per run*
    precisely so the feedback loop can tell a prompt problem from model-version
    drift; a stage re-run through a different door must not leave that unrecorded.
    """
    data: dict[str, Any] = {}
    if artifacts.model.exists():
        try:
            data = json.loads(artifacts.model.read_text(encoding="utf-8"))
        except json.JSONDecodeError:  # a corrupt log must not stop a run
            data = {}
    data.setdefault("prompts", {})[stage] = prompt
    data.setdefault("stage_models", {})[stage] = {"model": model, "run_at": run_at}
    artifacts.ensure()
    artifacts.model.write_text(
        json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8"
    )


def _read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


# ---------------------------------------------------------------------------
# Stage 4 — extract
# ---------------------------------------------------------------------------


def build_extract_context(
    segments: Sequence[TermSegment | AlignedSpan], max_chars: int = 120_000
) -> str:
    """Format the aligned material as the model's input, most confident first.

    Bounded on purpose: the Bodhicaryāvatāra commentaries total ~16 MB, and sending all of
    it per term would be both ruinous and pointless. Only material that actually mentions
    the term reaches here, and this trims the tail if even that overflows.

    ``segment_id`` is the header the model is asked to echo back on every passage, so what
    goes in it decides how precise a citation can be. For a commentary that has been through
    stage 1b it is the block's own ID (``^1-1-2-1``) and the footnote can name the paragraph;
    for one that has not, it falls back to the root verse the span is anchored to, which is
    the best locator available and is what this stage used before block IDs existed.
    """
    parts: list[str] = []
    used = 0
    ordered = sorted(
        segments,
        key=lambda x: (-x.confidence, x.source_id, getattr(x, "block_id", "") or x.verse_id),
    )
    for s in ordered:
        block_id = getattr(s, "block_id", "") or s.verse_id
        header = (
            f"--- source_id: {s.source_id} | segment_id: {block_id} "
            f"| root_verse: {s.verse_id} | lines {s.start_line}-{s.end_line} ---"
        )
        chunk = f"{header}\n{s.text}\n"
        if used + len(chunk) > max_chars:
            break
        parts.append(chunk)
        used += len(chunk)
    return "\n".join(parts)


#: Characters of aligned material above which extraction is split into several
#: calls.  Measured on tara21: asked about སྒྲོལ་མ། with 93,000 characters of
#: context in one call, ``gemini-3.5-flash`` returned ten passages totalling 873
#: characters — from the corpus's own central term, across sixteen commentaries.
#: The same model on the same prompt with 12,000 characters returned twenty
#: passages totalling 5,224. The model is not ignoring the "omit nothing" rule so
#: much as budgeting its answer against the size of the question, so the fix is
#: to ask smaller questions rather than to shout louder in the prompt.
EXTRACT_BATCH_CHARS = 25_000


def batch_segments(
    segments: Sequence[TermSegment | AlignedSpan], max_chars: int = EXTRACT_BATCH_CHARS
) -> list[list[TermSegment | AlignedSpan]]:
    """Group segments into per-call batches, never splitting one commentary.

    Keeping a commentary whole matters for rule ༦ of the extract prompt: the model
    is asked which commentaries have *no* explanation of the term, and it can only
    answer that about a commentary it has seen all of. Batches are otherwise packed
    greedily, so a term with little material stays a single call.
    """
    by_source: dict[str, list] = {}
    for s in segments:
        by_source.setdefault(s.source_id, []).append(s)

    batches: list[list] = []
    current: list = []
    used = 0
    for source_id in sorted(by_source):
        group = by_source[source_id]
        size = sum(len(s.text) for s in group)
        if current and used + size > max_chars:
            batches.append(current)
            current, used = [], 0
        current.extend(group)
        used += size
    if current:
        batches.append(current)
    return batches


def run_extract(
    term: str,
    alignment: AlignmentReport,
    generate: Callable[..., Any],
    prompt_render: Callable[..., str],
    artifacts: TermArtifacts,
    source_loader: Callable[[str], str] | None = None,
    batch_chars: int = EXTRACT_BATCH_CHARS,
) -> list[Passage]:
    """Pull every passage explaining ``term`` out of the aligned commentaries.

    ``source_loader`` lets the aligned spans be narrowed to the individual
    commentary blocks that mention the term, so each passage the model returns
    can carry a block-level ``segment_id``. Omit it and the whole span is sent,
    which is the pre-block-ID behaviour.

    A term with a lot of material is extracted in several calls (see
    :data:`EXTRACT_BATCH_CHARS`); the passages are concatenated in source order
    and duplicates — the same quotation returned by two batches — are dropped.
    """
    segments = segments_for_term(alignment, term, source_loader)
    if not segments:
        artifacts.ensure()
        _write_json(artifacts.extract, {"term": term, "passages": [], "no_explanation_in": []})
        return []

    passages: list[Passage] = []
    silent: list[str] = []
    seen: set[tuple[str, str]] = set()

    for batch in batch_segments(segments, batch_chars):
        prompt = prompt_render(
            stage="04-extract", term=term, aligned_segments=build_extract_context(batch)
        )
        result = generate(prompt, schema=EXTRACT_SCHEMA)
        data = (result.parsed if hasattr(result, "parsed") else result) or {}
        for p in data.get("passages", []):
            quote = p.get("quote", "")
            key = (p.get("source_id", ""), quote)
            if not quote or key in seen:
                continue
            seen.add(key)
            passages.append(
                Passage(
                    source_id=p.get("source_id", ""),
                    quote=quote,
                    kind=p.get("kind", ""),
                    segment_id=p.get("segment_id", ""),
                    note=p.get("note", ""),
                )
            )
        silent.extend(s for s in data.get("no_explanation_in", []) if s not in silent)

    artifacts.ensure()
    _write_json(
        artifacts.extract,
        {
            "term": term,
            "passages": [p.to_dict() for p in passages],
            "no_explanation_in": silent,
        },
    )
    return passages


# ---------------------------------------------------------------------------
# Stage 4b — atomic claims (the hinge)
# ---------------------------------------------------------------------------


def _sources_payload(registry: Registry) -> str:
    """The registry as the model sees it: identity + attribution metadata only."""
    return json.dumps(
        [
            {
                "source_id": s.source_id,
                "author": s.author,
                "title": s.title,
                "school": s.school or "",
                "copyright": s.copyright or "",
            }
            for s in registry.sources
        ],
        ensure_ascii=False,
        indent=1,
    )


def glossary_for(term: str) -> str:
    """The locked-glossary string for a term.

    Today this is the term itself — the one word the polish stage must never
    paraphrase. When the team curates per-term technical glossaries (the canonical
    pipeline's ``{{GLOSSARY}}``), extend this rather than the call sites.
    """
    return term


def run_claims(
    term: str,
    passages: Sequence[Passage],
    registry: Registry,
    generate: Callable[..., Any],
    prompt_render: Callable[..., str],
    artifacts: TermArtifacts,
) -> list[Claim]:
    """Convert passages into the atomic claims table (``claims.json``).

    From here on the claims table is the only drafting input — the drafting stages never
    see source wording again (canonical pipeline, load-bearing invariant 1). Claims whose
    ``passage_indices`` are empty or out of range are dropped with a note in the artifact:
    a claim that cites no passage could never carry a verifiable citation.
    """
    payload = json.dumps(
        [{"index": i, **p.to_dict()} for i, p in enumerate(passages)],
        ensure_ascii=False,
        indent=1,
    )
    prompt = prompt_render(
        stage="04b-claims",
        term=term,
        passages_json=payload,
        sources_json=_sources_payload(registry),
        glossary=glossary_for(term),
    )
    result = generate(prompt, schema=CLAIMS_SCHEMA)
    data = (result.parsed if hasattr(result, "parsed") else result) or {}

    claims: list[Claim] = []
    dropped: list[str] = []
    for i, c in enumerate(data.get("claims", [])):
        indices = [
            idx for idx in c.get("passage_indices", [])
            if isinstance(idx, int) and 0 <= idx < len(passages)
        ]
        if not indices:
            dropped.append(f"{c.get('id') or f'#{i}'}: no valid passage_indices")
            continue
        claims.append(
            Claim(
                id=str(c.get("id") or f"C{len(claims) + 1}"),
                claim_bo=str(c.get("claim_bo") or ""),
                passage_indices=indices,
                claim_type=str(c.get("claim_type") or "single-commentator"),
                school=str(c.get("school") or ""),
                reception=str(c.get("reception") or ""),
                contested=bool(c.get("contested", False)),
                copyright_only=bool(c.get("copyright_only", False)),
            )
        )

    artifacts.ensure()
    _write_json(
        artifacts.claims,
        {
            "term": term,
            "claims": [c.to_dict() for c in claims],
            "forbidden_syntheses": data.get("forbidden_syntheses", []),
            "dropped": dropped,
        },
    )
    return claims


def load_claims(artifacts: TermArtifacts) -> list[Claim]:
    """Read ``claims.json`` back for a resumed run."""
    data = _read_json(artifacts.claims)
    return [
        Claim(
            id=str(c.get("id") or ""),
            claim_bo=str(c.get("claim_bo") or ""),
            passage_indices=list(c.get("passage_indices", [])),
            claim_type=str(c.get("claim_type") or "single-commentator"),
            school=str(c.get("school") or ""),
            reception=str(c.get("reception") or ""),
            contested=bool(c.get("contested", False)),
            copyright_only=bool(c.get("copyright_only", False)),
        )
        for c in data.get("claims", [])
    ]


def _claims_payload(claims: Sequence[Claim]) -> str:
    return json.dumps(
        [{"index": i, **c.to_dict()} for i, c in enumerate(claims)],
        ensure_ascii=False,
        indent=1,
    )


# ---------------------------------------------------------------------------
# Stage 5 — outline (from claims only)
# ---------------------------------------------------------------------------


def run_organize(
    term: str,
    claims: Sequence[Claim],
    generate: Callable[..., Any],
    prompt_render: Callable[..., str],
    artifacts: TermArtifacts,
) -> dict:
    """Structure the article from the claims table — and nothing else.

    Sections are weighted by breadth adjusted by reception, and sections carrying
    sub-consensus claims are marked ``attribution_required`` for the drafter.
    """
    prompt = prompt_render(stage="05-organize", term=term, claims_json=_claims_payload(claims))
    result = generate(prompt, schema=ORGANIZE_SCHEMA)
    data = result.parsed if hasattr(result, "parsed") else result
    artifacts.ensure()
    _write_json(artifacts.sections, data)
    return data or {}


# ---------------------------------------------------------------------------
# Stage 6 — draft
# ---------------------------------------------------------------------------


def _citation_for(
    passage: Passage, registry: Registry, index: int
) -> Citation:
    """Turn a passage into a Citation with a resolved, deep-linked URL.

    The URL comes from the registry — the team's own Wikisource links — never from the
    model. That is what closes the ``dummy.com`` gap the prompt's author flagged: the model
    supplies the ``source_id``, the registry supplies the address.
    """
    src = registry.source(passage.source_id)
    url = resolve_citation_url(registry, passage.source_id, passage.quote) or ""
    return Citation(
        source_id=passage.source_id,
        author=(src.author if src else "") or "",
        title=(src.title if src else "") or "",
        year="",
        page="",
        url=url,
        quote=passage.quote,
        segment_id=passage.segment_id,
    )


def render_draft_payload(
    term: str,
    data: dict,
    claims: Sequence[Claim],
    passages: Sequence[Passage],
    registry: Registry,
    categories: Sequence[str] = ("ནང་བསྟན།",),
) -> tuple[str, list[Citation]]:
    """Render a draft payload (claim-index citations) to wikitext.

    The model cites *claims*; this expands each claim to the passages behind it and
    renders the refs. Quotations therefore enter the article only from ``extract.json``,
    never from the drafting model — which is what keeps the stage-7 character-for-character
    gate meaningful under claims-only drafting. Shared by draft and polish so the two
    stages cannot render differently.
    """
    citations: list[Citation] = []
    seen: dict[int, Citation] = {}

    def _render_para(para: dict) -> str:
        text = (para.get("text") or "").strip()
        rendered: set[int] = set()  # two claims sharing a passage → one ref here
        for idx in para.get("citations", []):
            if not isinstance(idx, int) or not (0 <= idx < len(claims)):
                continue
            for pidx in claims[idx].passage_indices:
                if not (0 <= pidx < len(passages)) or pidx in rendered:
                    continue
                rendered.add(pidx)
                if pidx not in seen:
                    c = _citation_for(passages[pidx], registry, pidx)
                    seen[pidx] = c
                    citations.append(c)
                text += render_ref(seen[pidx])
        return text

    lead = [_render_para(p) for p in data.get("lead", []) if (p.get("text") or "").strip()]
    sections = []
    for s in data.get("sections", []):
        paras = [_render_para(p) for p in s.get("paragraphs", []) if (p.get("text") or "").strip()]
        if paras and (s.get("heading") or "").strip():
            sections.append(Section(heading=s["heading"], paragraphs=paras))

    article = Article(
        term=term,
        lead=lead,
        sections=sections,
        see_also=[t for t in data.get("see_also", []) if t],
        citations=citations,
        # One line per *source*, not per citation: a commentary quoted five times is still
        # one entry in དཔྱད་གཞིའི་ཡིག་ཆ།.
        bibliography=list(
            dict.fromkeys(
                f"{c.author} {c.title}".strip() for c in citations if (c.author or c.title)
            )
        ),
        categories=list(categories),
    )
    return render_article(article), citations


def run_draft(
    term: str,
    passages: Sequence[Passage],
    claims: Sequence[Claim],
    organization: dict,
    registry: Registry,
    generate: Callable[..., Any],
    prompt_render: Callable[..., str],
    artifacts: TermArtifacts,
    categories: Sequence[str] = ("ནང་བསྟན།",),
) -> tuple[str, list[Citation]]:
    """Write the article from the outline and the claims table — passages closed.

    The drafting model is shown claims only (invariant 1). It cites claim indices; the
    renderer expands them to the underlying passages, so ref rendering stays out of the
    model's hands and the output conforms to the spec by construction rather than by luck.
    """
    prompt = prompt_render(
        stage="06-draft",
        term=term,
        outline_json=json.dumps(organization, ensure_ascii=False, indent=1),
        claims_json=_claims_payload(claims),
        glossary=glossary_for(term),
    )
    result = generate(prompt, schema=DRAFT_SCHEMA)
    data = result.parsed if hasattr(result, "parsed") else result or {}

    wikitext, citations = render_draft_payload(
        term, data, claims, passages, registry, categories
    )

    artifacts.ensure()
    _write_json(artifacts.draft, data)
    # A new draft invalidates any earlier polish of the old one — leaving it would
    # make a later standalone audit prefer stale text. Preserved, not just removed.
    preserve_artifact(artifacts.polished)
    artifacts.polished.unlink(missing_ok=True)
    _write_text(artifacts.wikitext, wikitext)
    _write_json(artifacts.citations, [asdict(c) for c in citations])
    return wikitext, citations


# ---------------------------------------------------------------------------
# Stage 6a — polish (optional literary rewrite; the canonical gemini_polish.py)
# ---------------------------------------------------------------------------


@dataclass
class PolishResult:
    """What the polish pass did, and whether its output was accepted.

    ``structure_problems`` non-empty means the stylist broke a hard constraint —
    changed a citations array, dropped a paragraph, reordered sections — and the
    polished text was REJECTED: ``article.wiki`` still holds the unpolished draft.
    The stylist is never trusted with structure; that check is code, not prompt.
    """

    accepted: bool
    structure_problems: list[str] = field(default_factory=list)
    wikitext: str = ""
    citations: list[Citation] = field(default_factory=list)


def _polish_structure_diff(original: dict, polished: dict) -> list[str]:
    """Every way the polished payload deviates from the original's structure."""
    problems: list[str] = []

    def _cites(block: dict) -> list:
        return [p.get("citations", []) for p in block or []]

    if _cites(original.get("lead")) != _cites(polished.get("lead")):
        problems.append("lead: paragraph count or citations arrays changed")
    o_secs, p_secs = original.get("sections", []), polished.get("sections", [])
    if [s.get("heading") for s in o_secs] != [s.get("heading") for s in p_secs]:
        problems.append("sections: headings changed or reordered")
    for i, (o, p) in enumerate(zip(o_secs, p_secs)):
        if _cites(o.get("paragraphs")) != _cites(p.get("paragraphs")):
            problems.append(
                f"section {i} ({o.get('heading', '')!r}): paragraph count or citations changed"
            )
    if (original.get("see_also") or []) != (polished.get("see_also") or []):
        problems.append("see_also changed")
    return problems


def run_polish(
    term: str,
    passages: Sequence[Passage],
    claims: Sequence[Claim],
    registry: Registry,
    generate: Callable[..., Any],
    prompt_render: Callable[..., str],
    artifacts: TermArtifacts,
    categories: Sequence[str] = ("ནང་བསྟན།",),
) -> PolishResult:
    """Literary rewrite of the draft under hard constraints (stage 6a, optional).

    The draft artifact is left untouched either way — per-stage outputs are immutable so
    the audit can name the stage that introduced a drift. An accepted polish is written to
    ``draft_polished.json`` and re-rendered over ``article.wiki``; a rejected one changes
    nothing on disk except the recorded problems.
    """
    original = _read_json(artifacts.draft)
    prompt = prompt_render(
        stage="06a-polish",
        term=term,
        draft_json=json.dumps(original, ensure_ascii=False, indent=1),
        glossary=glossary_for(term),
    )
    result = generate(prompt, schema=DRAFT_SCHEMA)
    polished = result.parsed if hasattr(result, "parsed") else result or {}

    problems = _polish_structure_diff(original, polished)
    if problems:
        return PolishResult(accepted=False, structure_problems=problems)

    wikitext, citations = render_draft_payload(
        term, polished, claims, passages, registry, categories
    )
    _write_json(artifacts.polished, polished)
    _write_text(artifacts.wikitext, wikitext)
    _write_json(artifacts.citations, [asdict(c) for c in citations])
    return PolishResult(accepted=True, wikitext=wikitext, citations=citations)


# ---------------------------------------------------------------------------
# Stage 6b — audit (LLM reading check; invariant 2)
# ---------------------------------------------------------------------------

#: Finding kinds that block publication regardless of the model's verdict.
AUDIT_BLOCKING = frozenset({"added-fact", "attribution-loss"})


@dataclass
class AuditResult:
    term: str
    findings: list[dict] = field(default_factory=list)
    verdict: str = ""

    @property
    def blocking(self) -> list[dict]:
        return [
            f for f in self.findings
            if f.get("severity") == "blocking" or f.get("finding") in AUDIT_BLOCKING
        ]

    @property
    def passed(self) -> bool:
        """Publishable per the audit: a publish verdict and nothing blocking.

        Belt and braces on purpose — a model that lists an added fact and still
        says "publish" is overruled by its own finding.
        """
        return self.verdict == "publish" and not self.blocking

    def format_report(self) -> str:
        lines = [f"# Audit — {self.term}", ""]
        lines.append(f"**Verdict: {self.verdict or 'missing'}**"
                     + ("" if self.passed else " — **does not pass**"))
        lines.append("")
        if not self.findings:
            lines.append("No findings.")
        for f in self.findings:
            sev = f.get("severity", "?")
            mark = "⛔" if f in self.blocking else "•"
            lines.append(f"- {mark} [{sev}] **{f.get('finding', '?')}** — {f.get('note', '')}")
            if f.get("sentence"):
                lines.append(f"  > {f['sentence']}")
        lines.append("")
        return "\n".join(lines)


def run_audit(
    term: str,
    draft_data: dict,
    claims: Sequence[Claim],
    generate: Callable[..., Any],
    prompt_render: Callable[..., str],
    artifacts: TermArtifacts,
) -> AuditResult:
    """Read the drafted text back against the claims table, sentence by sentence.

    Load-bearing invariant 2: nothing is published that has not survived this audit.
    Added facts and attribution loss are blocking whatever the model's verdict says.
    The audit compares against claims, never against passages — and it complements the
    deterministic stage-7 quotation gate, which still runs after it.
    """
    prompt = prompt_render(
        stage="06b-audit",
        term=term,
        draft_json=json.dumps(draft_data, ensure_ascii=False, indent=1),
        claims_json=_claims_payload(claims),
        glossary=glossary_for(term),
    )
    result = generate(prompt, schema=AUDIT_SCHEMA)
    data = (result.parsed if hasattr(result, "parsed") else result) or {}

    audit = AuditResult(
        term=term,
        findings=[f for f in data.get("findings", []) if isinstance(f, dict)],
        verdict=str(data.get("verdict") or ""),
    )
    artifacts.ensure()
    _write_json(artifacts.audit, {"term": term, "findings": audit.findings, "verdict": audit.verdict})
    _write_text(artifacts.audit_report, audit.format_report())
    return audit


# ---------------------------------------------------------------------------
# Stage 7 — verify (the gate)
# ---------------------------------------------------------------------------


@dataclass
class VerifyResult:
    term: str
    findings: list[Finding] = field(default_factory=list)
    quote_failures: list[str] = field(default_factory=list)
    #: Quotations that are genuinely in their cited file but not in the block
    #: their ``segment_id`` names. Not a gate failure — the source attribution is
    #: correct and V1 is satisfied — but the locator is wrong, which sends a
    #: reviewer to the wrong paragraph, so it is reported.
    locator_failures: list[str] = field(default_factory=list)
    #: How many citations carry a resolvable block-level locator at all.
    located: int = 0
    total_citations: int = 0

    @property
    def passed(self) -> bool:
        return not any(f.severity == "error" for f in self.findings) and not self.quote_failures

    def format_report(self) -> str:
        lines = [f"# Verification — {self.term}", ""]
        lines.append("**PASS**" if self.passed else "**FAIL**")
        lines.append("")
        errs = [f for f in self.findings if f.severity == "error"]
        warns = [f for f in self.findings if f.severity != "error"]
        if self.quote_failures:
            lines += ["## Quotations not found in source", ""]
            lines += [f"- {q}" for q in self.quote_failures] + [""]
        if errs:
            lines += ["## Errors", ""] + [f"- `{f.rule}` {f.message}" for f in errs] + [""]
        if warns:
            lines += ["## Warnings", ""] + [f"- `{f.rule}` {f.message}" for f in warns] + [""]
        if self.total_citations:
            lines += [
                "## Segment provenance",
                "",
                f"{self.located} of {self.total_citations} citations name the commentary "
                f"block they came from.",
                "",
            ]
            if self.locator_failures:
                lines += [
                    "These quotations are in the file they cite, but not in the block their "
                    "`segment_id` names — the attribution is sound, the locator is not:",
                    "",
                ] + [f"- {q}" for q in self.locator_failures] + [""]
        return "\n".join(lines)


def _block_index(raw_text: str) -> dict[str, str]:
    """``{block id: block text}`` for one commentary, for locator checking.

    Takes the **raw** file, because block IDs are exactly what the reading view
    removes — indexing the reading view would find none and silently report every
    citation as unlocated. Each block's text is then put through the reading view
    itself, so the comparison is like-for-like with the whole-file check.

    Empty for a source with no block IDs, which turns the locator check into a
    no-op rather than a wall of false failures on a corpus that has not been
    through stage 1b.
    """
    from .commentary import parse_blocks, reading_view

    try:
        return {
            b.block_id: reading_view(b.text)
            for b in parse_blocks(raw_text)
            if b.block_id and not b.is_heading
        }
    except Exception:  # noqa: BLE001 - a locator check must never fail the gate
        return {}


def run_verify(
    term: str,
    wikitext: str,
    citations: Sequence[Citation],
    allowed_categories: Sequence[str],
    source_loader: Callable[[str], str] | None,
    artifacts: TermArtifacts,
    raw_loader: Callable[[str], str] | None = None,
) -> VerifyResult:
    """The blocking gate. No LLM, no network, no bypass.

    Runs the wikitext rules and, independently, re-reads every quotation from the file it
    claims to come from. Both must be clean.

    ``source_loader`` returns the commentary's **reading view** — the text with ingest
    scaffolding removed — because that is what a quotation is a quotation *of*. ``raw_loader``
    returns the same file untouched and is used only to find the block boundaries for the
    locator check; omit it and that check is skipped.
    """
    findings = validate(
        wikitext,
        citations=list(citations),
        allowed_categories=list(allowed_categories),
        source_loader=source_loader,
    )

    quote_failures: list[str] = []
    locator_failures: list[str] = []
    located = 0
    quoting = [c for c in citations if c.quote]
    if source_loader is not None:
        cache: dict[str, str] = {}
        blocks: dict[str, dict[str, str]] = {}
        for c in quoting:
            if c.source_id not in cache:
                try:
                    cache[c.source_id] = source_loader(c.source_id)
                except Exception as exc:  # a missing source is a failed citation, not a crash
                    quote_failures.append(f"{c.source_id}: source unreadable ({exc})")
                    cache[c.source_id] = ""
                try:
                    raw = raw_loader(c.source_id) if raw_loader else ""
                except Exception:  # noqa: BLE001 - no locators is not a gate failure
                    raw = ""
                blocks[c.source_id] = _block_index(raw) if raw else {}

            check = check_quote(c.quote, cache[c.source_id], c.source_id)
            if not check.passed:
                quote_failures.append(f"{c.locator}: [{check.method}] {c.quote[:60]}…")
                continue

            # The quotation is real. Now: is it where the citation says it is?
            block_text = blocks.get(c.source_id, {}).get(c.segment_id) if c.segment_id else None
            if block_text is None:
                continue
            located += 1
            if not check_quote(c.quote, block_text, c.locator).passed:
                locator_failures.append(f"{c.locator}: {c.quote[:60]}…")

    result = VerifyResult(
        term=term,
        findings=findings,
        quote_failures=quote_failures,
        locator_failures=locator_failures,
        located=located,
        total_citations=len(quoting),
    )
    artifacts.ensure()
    _write_text(artifacts.report, result.format_report())
    return result


# ---------------------------------------------------------------------------
# The update path — merge new material into an existing article
# ---------------------------------------------------------------------------
#
# 520 of the 545 སྤྱོད་འཇུག terms already have a bo.wikipedia article, so updating is the
# majority case. Division of labour matches the create path exactly: the model classifies
# each new passage against the existing article (duplicate / new / conflict) and names a
# section anchor; wiki.merge applies the operations deterministically, conflicts are never
# merged, and the verify gate re-reads every *new* quotation from its source file.


def update_citation_builder(registry: Registry):
    """Build the ``citation`` payload -> :class:`Citation` mapper for one registry.

    The model supplies ``source_id``, ``quote`` and optionally ``page``; author, title and
    the deep-linked URL come from the registry — the same ``dummy.com`` closure as
    :func:`_citation_for`. Returns ``None`` for a source the registry does not know, which
    :func:`~kangyur_wiki.wiki.merge.parse_operations` turns into a dropped-op message
    rather than a crash.
    """

    def build(raw: dict) -> Citation | None:
        source_id = str(raw.get("source_id") or "").strip()
        src = registry.source(source_id)
        if src is None:
            return None
        quote = str(raw.get("quote") or "")
        return Citation(
            source_id=source_id,
            author=src.author or "",
            title=src.title or "",
            year="",
            page=str(raw.get("page") or ""),
            url=resolve_citation_url(registry, source_id, quote) or "",
            quote=quote,
        )

    return build


def run_update(
    term: str,
    existing_wikitext: str,
    passages: Sequence[Passage],
    registry: Registry,
    generate: Callable[..., Any],
    prompt_render: Callable[..., str],
    artifacts: TermArtifacts,
    *,
    allowed_categories: Sequence[str] = ("ནང་བསྟན།",),
    source_loader: Callable[[str], str] | None = None,
) -> tuple[MergeResult, MergeVerification]:
    """Merge new cited material into ``existing_wikitext`` and verify the result.

    Writes the full audit trail: the existing-article snapshot, the model's raw
    operations, the merged wikitext (as ``article.wiki``, which is what publish ships),
    the new citations, the merge report with its diff, and the verification report. The
    merged text is written even on FAIL so a failure is diagnosable without re-running.
    """
    payload = json.dumps(
        [{"index": i, **p.to_dict()} for i, p in enumerate(passages)],
        ensure_ascii=False,
        indent=1,
    )
    prompt = prompt_render(
        stage="07-update",
        term=term,
        existing_wikitext=existing_wikitext,
        new_passages_json=payload,
    )
    result = generate(prompt, schema=UPDATE_SCHEMA)
    data = result.parsed if hasattr(result, "parsed") else result or {}

    operations, problems = parse_operations(
        data or {"operations": []}, citation_builder=update_citation_builder(registry)
    )
    merge_result = apply_operations(existing_wikitext, operations)
    merge_result.parse_problems.extend(problems)

    verification = verify_merged(
        merge_result.merged,
        merge_result.new_citations,
        allowed_categories,
        source_loader,
    )

    artifacts.ensure()
    _write_text(artifacts.existing_wiki, existing_wikitext)
    _write_json(artifacts.update_ops, data)
    _write_text(artifacts.wikitext, merge_result.merged)
    _write_json(artifacts.citations, [asdict(c) for c in merge_result.new_citations])
    _write_text(
        artifacts.update_report, merge_result.format_report(existing_wikitext)
    )
    _write_text(artifacts.report, verification.format_report())
    return merge_result, verification
