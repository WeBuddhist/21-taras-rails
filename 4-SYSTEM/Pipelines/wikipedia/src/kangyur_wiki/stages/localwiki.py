"""Emit a verified article's material into the vault's own Local-Wiki format.

A term that has passed both gates — the deterministic quotation check (stage 7) and
the claims-grounded audit (stage 6b) — has, by that point, exactly what
``4-SYSTEM/Skills/local-wiki-article/SKILL.md`` asks a Local-Wiki article to contain:
a synthesised contextual definition and a set of verbatim, block-cited attestations
per commentary. This module is the renderer from the pipeline's own artifacts
(``draft.json``, ``citations.json``, ``claims.json``, the source registry) into that
format, so a verified article's grounding work is not stranded inside
``3-TRANSFORMATIONS/Wikipedia/`` when the vault's own rails folder is exactly where a
per-term monolingual reference belongs.

This is additive, never authoritative on its own: the emitted file is ``status:
draft`` like every other Local-Wiki article, because the skill it follows is explicit
that only a domain specialist promotes one to ``complete``. What this module buys is
that the promotion candidate already exists, cited, the moment an article verifies —
not a second manual pass over the same commentaries.
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml

from .pipeline import Claim, Passage, TermArtifacts, preserve_artifact

__all__ = ["LocalWikiResult", "emit_local_wiki"]


@dataclass
class LocalWikiResult:
    path: Path
    commentaries_cited: int
    attestations: int
    divergences: int
    warnings: list[str] = field(default_factory=list)


def _read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else None


def _load_passages(artifacts: TermArtifacts) -> list[Passage]:
    data = _read_json(artifacts.extract) or {}
    return [
        Passage(
            source_id=p.get("source_id", ""), quote=p.get("quote", ""),
            kind=p.get("kind", ""), segment_id=p.get("segment_id", ""), note=p.get("note", ""),
        )
        for p in data.get("passages", [])
        if p.get("quote")
    ]


def _load_claims(artifacts: TermArtifacts) -> list[Claim]:
    data = _read_json(artifacts.claims) or {}
    return [
        Claim(
            id=str(c.get("id") or ""), claim_bo=str(c.get("claim_bo") or ""),
            passage_indices=list(c.get("passage_indices", [])),
            claim_type=str(c.get("claim_type") or "single-commentator"),
            school=str(c.get("school") or ""), reception=str(c.get("reception") or ""),
            contested=bool(c.get("contested", False)),
            copyright_only=bool(c.get("copyright_only", False)),
        )
        for c in data.get("claims", [])
    ]


def _lead_text(artifacts: TermArtifacts) -> str:
    """The article's own Tibetan lead paragraph(s), joined into one synthesis block.

    Prefers ``draft_polished.json`` when a polish was accepted, exactly the same
    preference ``cli.verify`` and ``cli.audit`` use for "the current draft".
    """
    draft = _read_json(artifacts.polished) or _read_json(artifacts.draft) or {}
    return " ".join(p.get("text", "").strip() for p in draft.get("lead", []) if p.get("text", "").strip())


def _source_home(registry, source_id: str) -> tuple[str, str] | None:
    """``(registered_id, vault-relative file path)`` for one ``source_id``, or
    ``None`` if the registry has no usable entry — a source with no ``local_path``
    or no ``registered_id`` cannot be cited in a rails file (About Rails' §8 hard
    citation rule), so it is dropped from the emission with a warning rather than
    guessed at.
    """
    source = registry.source(source_id)
    if source is None or source.local_path is None or not source.registered_id:
        return None
    return source.registered_id, str(source.local_path)


def emit_local_wiki(
    term: str,
    corpus_id: str,
    artifacts: TermArtifacts,
    registry,
    out_dir: Path,
    *,
    model: str = "",
    run_at: str = "",
) -> LocalWikiResult:
    """Render ``2-RAILS/Local-Wiki/<term>.md`` from one term's finished article state.

    Groups every citation and every extract passage by the commentary it came from,
    resolved to that commentary's ``registered_id`` and vault file path via the
    registry — never invented, per ``local-wiki-article``'s own rule that everything
    in the file must trace to ``1-SOURCES/``. Contested claims (``claims.json``'s
    ``contested: true``) become the Divergences section, cited to their own
    supporting passages.

    ``model``/``run_at`` default to whatever ``kwiki article`` already recorded in
    ``model.json`` for the drafting stage — a standalone ``kwiki local-wiki`` run
    calls no model itself, but the provenance of the material it is rendering is
    already on disk and worth keeping rather than leaving blank.
    """
    warnings: list[str] = []
    if not model or not run_at:
        recorded = _read_json(artifacts.model) or {}
        model = model or str(recorded.get("model") or "")
        run_at = run_at or str(recorded.get("run_at") or "")
    citations = [c for c in (_read_json(artifacts.citations) or []) if isinstance(c, dict)]
    passages = _load_passages(artifacts)
    claims = _load_claims(artifacts)
    lead = _lead_text(artifacts)

    # Group verbatim attestations by commentary, in first-appearance order.
    by_source: dict[str, list[dict]] = {}
    order: list[str] = []
    for c in citations:
        source_id = c.get("source_id", "")
        home = _source_home(registry, source_id)
        if home is None:
            if source_id and source_id not in warnings:
                warnings.append(f"citation to {source_id!r} dropped: no registered_id/local_path in the registry")
            continue
        registered_id, _path = home
        by_source.setdefault(registered_id, [])
        if registered_id not in order:
            order.append(registered_id)
        quote = str(c.get("quote", "")).strip()
        segment_id = str(c.get("segment_id", "")).strip()
        if quote:
            by_source[registered_id].append({"quote": quote, "segment_id": segment_id})

    file_by_registered_id = {
        home[0]: home[1]
        for s_id in {c.get("source_id", "") for c in citations}
        if (home := _source_home(registry, s_id)) is not None
    }

    attested_blocks = sorted(
        f"{rid}:^{a['segment_id']}" if a["segment_id"] else rid
        for rid, atts in by_source.items()
        for a in atts
    )

    # Divergences: contested claims, cited to their own supporting passages.
    divergence_lines: list[str] = []
    for claim in claims:
        if not claim.contested:
            continue
        cites: list[str] = []
        for idx in claim.passage_indices:
            if not (0 <= idx < len(passages)):
                continue
            p = passages[idx]
            home = _source_home(registry, p.source_id)
            if home is None:
                continue
            rid, path = home
            locator = f"#^{p.segment_id}" if p.segment_id else ""
            cites.append(f"({path}{locator})")
        note = claim.reception or claim.school or claim.claim_type
        divergence_lines.append(
            f"- ⚑ {claim.claim_bo} — {note}\n  " + " ".join(cites) if cites else f"- ⚑ {claim.claim_bo} — {note}"
        )

    lines: list[str] = []
    frontmatter = {
        "term": term,
        "language": "bo",
        "text": corpus_id,
        "commentaries": order,
        "attested_blocks": attested_blocks,
        "status": "draft",
        "generated_by": {
            "pipeline": "kwiki",
            "stage": "local-wiki",
            "model": model,
            "run_at": run_at,
            "source_artifacts": f"3-TRANSFORMATIONS/Wikipedia/{corpus_id}/articles/{term.strip('།་')}/",
        },
    }
    lines.append("---")
    lines.append(
        yaml.safe_dump(
            frontmatter, allow_unicode=True, default_flow_style=False, sort_keys=False, width=4096,
        ).rstrip("\n")
    )
    lines.append("---")
    lines.append("")
    lines.append(f"## {term}")
    lines.append("")
    lines.append("### Contextual definition")
    lines.append("")
    if lead:
        lines.append(lead)
    else:
        lines.append("(no lead paragraph found in the drafted article)")
        warnings.append("no lead text found in draft.json/draft_polished.json")
    lines.append("")
    for rid in order:
        for a in by_source[rid]:
            locator = f"#^{a['segment_id']}" if a["segment_id"] else ""
            lines.append(f"({file_by_registered_id.get(rid, rid)}{locator})")
    lines.append("")
    lines.append("### Attestations")
    lines.append("")
    attestation_count = 0
    for rid in order:
        lines.append(f"#### {rid}")
        lines.append("")
        for a in by_source[rid]:
            attestation_count += 1
            locator = f"#^{a['segment_id']}" if a["segment_id"] else ""
            lines.append(f"> {a['quote']}")
            lines.append(f"> ({file_by_registered_id.get(rid, rid)}{locator})")
            lines.append("")

    lines.append("### Divergences")
    lines.append("")
    if divergence_lines:
        lines.extend(divergence_lines)
    else:
        lines.append("None observed in this article's claims.")
    lines.append("")
    lines.append("### Related terms")
    lines.append("")
    lines.append("(none recorded yet)")
    lines.append("")

    out_path = out_dir / f"{term.strip('།་')}.md"
    preserve_artifact(out_path)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text("\n".join(lines), encoding="utf-8")

    return LocalWikiResult(
        path=out_path,
        commentaries_cited=len(order),
        attestations=attestation_count,
        divergences=len(divergence_lines),
        warnings=warnings,
    )
