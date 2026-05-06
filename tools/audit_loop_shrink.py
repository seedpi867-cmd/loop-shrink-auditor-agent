#!/usr/bin/env python3
"""Find repeated loop behavior that should become deterministic machinery."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable


PROMOTION_THRESHOLD = 2
SEQUENCE_MIN_LENGTH = 2
SEQUENCE_MAX_LENGTH = 3
SEQUENCE_KINDS = {"approval", "command", "denial", "failure", "fixture", "note", "tool"}
FRESH_EVIDENCE_CYCLES = 50
STALE_EVIDENCE_CYCLES = 200
ENVIRONMENT_GATED_CLASSIFICATIONS = {"script", "typed_tool", "approval_budget"}
NEGATIVE_KINDS = {"denial", "failure"}


@dataclass(frozen=True)
class Event:
    source: str
    line: int
    kind: str
    shape: str
    text: str
    risk: str = "unknown"
    cycle: str = ""
    environment: dict[str, str] | None = None


def normalize(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"https?://\\S+", "<url>", value)
    value = re.sub(r"\\b\\d{4}-\\d{2}-\\d{2}(?:[ t]\\d{2}:\\d{2}(?::\\d{2})?)?\\b", "<time>", value)
    value = re.sub(r"\\b\\d+\\b", "<n>", value)
    value = re.sub(r"\\s+", " ", value)
    return value[:220]


def redact_sensitive(value: str) -> str:
    value = re.sub(r"(?i)(app password:?)\s+[a-z0-9 ]+", r"\1 <redacted>", value)
    value = re.sub(r"(?i)(password|token|secret|credential)(\s*[:=]\s*)\S+", r"\1\2<redacted>", value)
    value = re.sub(r"\b[\w.+-]+@[\w.-]+\.[a-zA-Z]{2,}\b", "<email>", value)
    value = re.sub(r"\b(?:10|127|172\.(?:1[6-9]|2\d|3[01])|192\.168)\.\d{1,3}\.\d{1,3}\b", "<ip>", value)
    return value


def iter_input_files(root: Path) -> Iterable[Path]:
    if root.is_file():
        yield root
        return
    for path in sorted(root.rglob("*")):
        if path.suffix.lower() in {".jsonl", ".log", ".txt", ".md"} and path.is_file():
            yield path


def events_from_record(record: dict, source: Path, line_number: int) -> list[Event]:
    post_publish_events = events_from_post_publish_receipt(record, source, line_number)
    if post_publish_events:
        return post_publish_events

    approval_event = event_from_approval_record(record, source, line_number)
    if approval_event:
        return [approval_event]

    raw_values = [
        record.get("action"),
        record.get("command"),
        record.get("tool"),
        record.get("decision"),
        record.get("message"),
    ]
    for key in ("actions", "commands", "tools", "decisions", "messages"):
        value = record.get(key)
        if isinstance(value, list):
            raw_values.extend(value)

    texts = [redact_sensitive(str(value).strip()) for value in raw_values if str(value or "").strip()]
    kind_hint = str(record.get("type") or record.get("kind") or "").lower()
    risk = str(record.get("risk") or "unknown").lower()
    cycle = str(record.get("cycle") or "")
    return [
        Event(
            str(source),
            line_number,
            kind_hint or infer_kind(text),
            normalize(text),
            text,
            risk,
            cycle,
        )
        for text in texts
    ]


def events_from_post_publish_receipt(record: dict, source: Path, line_number: int) -> list[Event]:
    if record.get("schema") != "seed.post_publish_receipt.v1":
        return []

    deploy = record.get("deploy") if isinstance(record.get("deploy"), dict) else {}
    social = record.get("social") if isinstance(record.get("social"), dict) else {}
    post = record.get("post") if isinstance(record.get("post"), dict) else {}
    output_tail = str(record.get("output_tail") or "")
    cycle = str(record.get("cycle") or "")
    environment = compact_environment(
        {
            "deploy_ok": deploy.get("ok"),
            "deploy_skipped": deploy.get("skipped"),
            "deploy_returncode": deploy.get("returncode"),
            "social_attempted": social.get("attempted"),
            "social_outcome": social.get("outcome"),
            "post_slug_present": bool(post.get("slug")),
        }
    )
    deploy_status = "ok" if deploy.get("ok") else "failed"

    events = [
        Event(
            str(source),
            line_number,
            "command",
            f"post_publish deploy blog status={deploy_status}",
            redact_sensitive(
                "post_publish deploy blog"
                f" command={deploy.get('command') or '<unknown>'}"
                f" ok={deploy.get('ok')}"
                f" skipped={deploy.get('skipped')}"
            ),
            "low" if deploy.get("ok") else "medium",
            cycle,
            environment,
        )
    ]

    if deploy.get("ok") and ("[verify] live:" in output_tail or deploy.get("skipped")):
        events.append(
            Event(
                str(source),
                line_number,
                "fixture",
                "post_publish verify live blog post",
                "post_publish verify live blog post",
                "low",
                cycle,
                environment,
            )
        )

    social_outcome = str(social.get("outcome") or "").strip()
    if social_outcome:
        social_kind = "denial" if "skip" in social_outcome or "suspend" in social_outcome else "tool"
        events.append(
            Event(
                str(source),
                line_number,
                social_kind,
                f"post_publish social outcome={normalize(social_outcome)}",
                redact_sensitive(
                    "post_publish social"
                    f" attempted={social.get('attempted')}"
                    f" outcome={social_outcome}"
                    f" reason={social.get('reason') or ''}"
                ),
                "medium" if social_kind == "denial" else "low",
                cycle,
                environment,
            )
        )

    if not deploy.get("ok"):
        events.append(
            Event(
                str(source),
                line_number,
                "failure",
                "post_publish deploy failed",
                redact_sensitive(f"post_publish deploy failed tail={output_tail[-180:]}"),
                "medium",
                cycle,
                environment,
            )
        )

    return events


def compact_environment(values: dict[str, Any]) -> dict[str, str]:
    environment: dict[str, str] = {}
    for key, value in values.items():
        if value is None:
            continue
        environment[key] = normalize(str(value))
    return environment


def event_from_approval_record(record: dict, source: Path, line_number: int) -> Event | None:
    approval = record.get("approval")
    if isinstance(approval, dict):
        merged = {**record, **approval}
    else:
        merged = record

    kind_hint = str(merged.get("type") or merged.get("kind") or "").lower()
    decision = str(merged.get("decision") or merged.get("outcome") or merged.get("status") or "").lower()
    has_structured_approval_shape = any(
        key in merged
        for key in (
            "approval",
            "approval_id",
            "approved",
            "action_shape",
            "requested_action",
            "scope",
            "grant_scope",
        )
    )
    if kind_hint not in {"approval_log", "approval_event"} and not has_structured_approval_shape:
        return None

    action = (
        merged.get("action_shape")
        or merged.get("requested_action")
        or merged.get("action")
        or merged.get("command")
        or merged.get("tool")
    )
    if not str(action or "").strip():
        return None

    scope = merged.get("scope") or merged.get("grant_scope") or merged.get("resource") or merged.get("target")
    sink = merged.get("sink") or merged.get("destination")
    expires = merged.get("expires") or merged.get("expiry") or merged.get("expires_cycle")
    parts = [f"approve action={action}"]
    if scope:
        parts.append(f"scope={scope}")
    if sink:
        parts.append(f"sink={sink}")
    if expires:
        parts.append(f"expires={expires}")

    text = redact_sensitive(" ".join(str(part) for part in parts))
    return Event(
        str(source),
        line_number,
        "approval",
        normalize(text),
        text,
        str(merged.get("risk") or "unknown").lower(),
        str(merged.get("cycle") or ""),
    )


def infer_kind(text: str) -> str:
    lowered = text.lower()
    if "approve" in lowered or "approval" in lowered:
        return "approval"
    if "deny" in lowered or "blocked" in lowered or "quarantine" in lowered:
        return "denial"
    if "test" in lowered or "fixture" in lowered or "regression" in lowered:
        return "fixture"
    if re.search(r"\\b(rg|sed|git|python3?|bash|curl|wget|npm|pytest|unittest)\\b", lowered):
        return "command"
    if "tool" in lowered or "api" in lowered or "schema" in lowered:
        return "tool"
    if "failed" in lowered or "error" in lowered or "retry" in lowered:
        return "failure"
    return "note"


def parse_text_line(line: str, source: Path, line_number: int) -> Event | None:
    text = redact_sensitive(line.strip())
    if not text or text.startswith("#"):
        return None
    kind = infer_kind(text)
    if kind == "note":
        return None
    return Event(str(source), line_number, kind, normalize(text), text)


def load_events(input_path: Path) -> list[Event]:
    events: list[Event] = []
    for path in iter_input_files(input_path):
        with path.open("r", encoding="utf-8") as handle:
            for line_number, line in enumerate(handle, start=1):
                if path.suffix.lower() == ".jsonl":
                    try:
                        record = json.loads(line)
                    except json.JSONDecodeError:
                        event = parse_text_line(line, path, line_number)
                        if event:
                            events.append(event)
                    else:
                        events.extend(events_from_record(record, path, line_number))
                else:
                    event = parse_text_line(line, path, line_number)
                    if event:
                        events.append(event)
    return events


def classify(kind: str, texts: list[str], risks: list[str]) -> str:
    joined = " ".join(texts).lower()
    high_risk = any(risk in {"high", "critical", "consequential"} for risk in risks)
    if kind == "denial" or "blocked" in joined or "quarantine" in joined:
        return "deny_or_quarantine"
    if kind == "approval" and high_risk:
        return "approval_budget"
    if kind == "approval" and not high_risk:
        if "api" in joined or "tool" in joined or "parameter" in joined:
            return "typed_tool"
        return "script"
    if kind == "fixture" or "regression" in joined or "expected" in joined:
        return "fixture"
    if kind == "tool" or "schema" in joined or "api" in joined:
        return "typed_tool"
    if kind in {"command", "failure"}:
        return "script"
    return "fixture"


def risk_for(classification: str, count: int) -> str:
    if classification == "approval_budget":
        return "high"
    if classification == "deny_or_quarantine":
        return "medium"
    if count >= 5:
        return "medium"
    return "low"


def cycle_number(value: str) -> int | None:
    if not value:
        return None
    match = re.search(r"\d+", str(value))
    if not match:
        return None
    return int(match.group(0))


def current_cycle(events: list[Event]) -> int | None:
    cycles = [cycle for event in events if (cycle := cycle_number(event.cycle)) is not None]
    if not cycles:
        return None
    return max(cycles)


def evidence_window(events: list[Event], now_cycle: int | None) -> dict:
    cycles = [cycle for event in events if (cycle := cycle_number(event.cycle)) is not None]
    if not cycles or now_cycle is None:
        return {
            "first_cycle": None,
            "latest_cycle": None,
            "evidence_age_cycles": None,
            "evidence_expires_cycle": None,
            "evidence_status": "unknown",
            "freshness_multiplier": 1.0,
        }

    first_cycle = min(cycles)
    latest_cycle = max(cycles)
    age = max(0, now_cycle - latest_cycle)
    expires_cycle = latest_cycle + STALE_EVIDENCE_CYCLES
    if age <= FRESH_EVIDENCE_CYCLES:
        status = "fresh"
        multiplier = 1.0
    elif age <= STALE_EVIDENCE_CYCLES:
        status = "aging"
        multiplier = 0.75
    else:
        status = "stale"
        multiplier = 0.45

    return {
        "first_cycle": first_cycle,
        "latest_cycle": latest_cycle,
        "evidence_age_cycles": age,
        "evidence_expires_cycle": expires_cycle,
        "evidence_status": status,
        "freshness_multiplier": multiplier,
    }


def environment_coverage(events: list[Event]) -> dict[str, list[str]]:
    coverage: dict[str, set[str]] = defaultdict(set)
    for event in events:
        for key, value in (event.environment or {}).items():
            coverage[key].add(value)
    return {key: sorted(values) for key, values in sorted(coverage.items())}


def environment_gate(classification: str, coverage: dict[str, list[str]]) -> dict:
    if classification == "deny_or_quarantine":
        return {
            "status": "condition_bound",
            "blocks_promotion": False,
            "reasons": ["negative evidence can be promoted as a bounded quarantine rule"],
            "unobserved_critical_variants": [],
        }

    if classification not in ENVIRONMENT_GATED_CLASSIFICATIONS:
        return {
            "status": "not_required",
            "blocks_promotion": False,
            "reasons": [],
            "unobserved_critical_variants": [],
        }

    if not coverage:
        return {
            "status": "needs_environment_record",
            "blocks_promotion": True,
            "reasons": ["no named operating conditions were recorded for repeated evidence"],
            "unobserved_critical_variants": ["account/network/repo/policy/input conditions unknown"],
        }

    narrow_keys = [key for key, values in coverage.items() if len(values) == 1]
    if narrow_keys and len(narrow_keys) == len(coverage):
        return {
            "status": "blocked_narrow_environment",
            "blocks_promotion": True,
            "reasons": ["all recorded environment dimensions were observed in only one state"],
            "unobserved_critical_variants": [
                f"{key}=not({values[0]})" for key, values in coverage.items()
            ],
        }

    return {
        "status": "passes_environment_gate",
        "blocks_promotion": False,
        "reasons": [],
        "unobserved_critical_variants": [],
    }


def contradiction_coverage(classification: str, events: list[Event]) -> dict:
    observed = sorted({event.kind for event in events if event.kind in NEGATIVE_KINDS})
    if classification == "deny_or_quarantine":
        status = "inherent_negative_signal"
    elif observed:
        status = "observed"
    else:
        status = "missing"

    return {
        "status": status,
        "observed_negative_kinds": observed,
        "sources": sorted({event.source for event in events if event.kind in NEGATIVE_KINDS}),
    }


def confidence_for(base: float, evidence: dict) -> float:
    return round(min(0.95, base * evidence["freshness_multiplier"]), 2)


def suggested_test(classification: str, shape: str) -> str:
    if classification == "script":
        return f"Add a fixture proving `{shape}` runs idempotently from clean inputs."
    if classification == "typed_tool":
        return f"Add schema validation and receipt checks for `{shape}`."
    if classification == "fixture":
        return f"Add positive and negative evidence cases for `{shape}`."
    if classification == "approval_budget":
        return f"Require exact-call approval, expiry, replay rejection, and recovery evidence for `{shape}`."
    return f"Add a deny/quarantine regression proving `{shape}` cannot execute silently."


def build_candidates(events: list[Event]) -> list[dict]:
    groups: dict[tuple[str, str], list[Event]] = defaultdict(list)
    now_cycle = current_cycle(events)
    for event in events:
        groups[(event.kind, event.shape)].append(event)

    candidates: list[dict] = []
    for (kind, shape), grouped in groups.items():
        if len(grouped) < PROMOTION_THRESHOLD:
            continue
        texts = [event.text for event in grouped]
        risks = [event.risk for event in grouped]
        classification = classify(kind, texts, risks)
        evidence = evidence_window(grouped, now_cycle)
        confidence = confidence_for(0.45 + 0.12 * len(grouped), evidence)
        candidate_id = hashlib.sha256(f"{kind}:{shape}".encode("utf-8")).hexdigest()[:12]
        coverage = environment_coverage(grouped)
        candidates.append(
            {
                "id": candidate_id,
                "classification": classification,
                "kind": kind,
                "shape": shape,
                "count": len(grouped),
                "confidence": confidence,
                "evidence": {key: value for key, value in evidence.items() if key != "freshness_multiplier"},
                "environment_coverage": coverage,
                "promotion_gate": environment_gate(classification, coverage),
                "contradiction_coverage": contradiction_coverage(classification, grouped),
                "risk": risk_for(classification, len(grouped)),
                "suggested_test": suggested_test(classification, shape),
                "examples": [
                    {
                        "source": event.source,
                        "line": event.line,
                        "cycle": event.cycle,
                        "text": event.text,
                        "environment": event.environment or {},
                    }
                    for event in grouped[:5]
                ],
            }
        )

    candidates.extend(build_sequence_candidates(events, now_cycle))
    return sorted(candidates, key=lambda item: (-item["count"], item["classification"], item["shape"]))


def sequence_buckets(events: list[Event]) -> dict[tuple[str, str], list[Event]]:
    buckets: dict[tuple[str, str], list[Event]] = defaultdict(list)
    for event in events:
        if event.kind not in SEQUENCE_KINDS:
            continue
        buckets[(event.source, event.cycle)].append(event)
    return buckets


def build_sequence_candidates(events: list[Event], now_cycle: int | None) -> list[dict]:
    sequences: dict[tuple[str, ...], list[list[Event]]] = defaultdict(list)
    for bucket in sequence_buckets(events).values():
        if len(bucket) < SEQUENCE_MIN_LENGTH:
            continue
        for size in range(SEQUENCE_MIN_LENGTH, SEQUENCE_MAX_LENGTH + 1):
            if len(bucket) < size:
                continue
            for index in range(0, len(bucket) - size + 1):
                window = bucket[index : index + size]
                shape = tuple(event.shape for event in window)
                if len(set(shape)) == 1:
                    continue
                sequences[shape].append(window)

    candidates: list[dict] = []
    for shape_parts, windows in sequences.items():
        if len(windows) < PROMOTION_THRESHOLD:
            continue
        shape = " -> ".join(shape_parts)
        candidate_id = hashlib.sha256(f"sequence:{shape}".encode("utf-8")).hexdigest()[:12]
        window_events = [event for window in windows for event in window]
        evidence = evidence_window(window_events, now_cycle)
        confidence = confidence_for(0.4 + 0.1 * len(windows), evidence)
        coverage = environment_coverage(window_events)
        candidates.append(
            {
                "id": candidate_id,
                "classification": "script",
                "kind": "sequence",
                "shape": shape,
                "count": len(windows),
                "confidence": confidence,
                "evidence": {key: value for key, value in evidence.items() if key != "freshness_multiplier"},
                "environment_coverage": coverage,
                "promotion_gate": environment_gate("script", coverage),
                "contradiction_coverage": contradiction_coverage("script", window_events),
                "risk": risk_for("script", len(windows)),
                "suggested_test": suggested_test("script", shape),
                "examples": [
                    {
                        "source": window[0].source,
                        "line": window[0].line,
                        "cycle": window[0].cycle,
                        "text": " -> ".join(event.text for event in window),
                        "environment": window[0].environment or {},
                    }
                    for window in windows[:5]
                ],
            }
        )

    return candidates


def write_reports(candidates: list[dict], events: list[Event], output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    summary = Counter(candidate["classification"] for candidate in candidates)
    payload = {
        "event_count": len(events),
        "candidate_count": len(candidates),
        "summary": dict(sorted(summary.items())),
        "candidates": candidates,
    }
    (output_dir / "promotion-map.json").write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")

    lines = [
        "# Promotion Docket",
        "",
        f"Events scanned: {len(events)}",
        f"Promotion candidates: {len(candidates)}",
        "",
    ]
    if summary:
        lines.append("## Summary")
        lines.append("")
        for classification, count in sorted(summary.items()):
            lines.append(f"- `{classification}`: {count}")
        lines.append("")

    for candidate in candidates:
        lines.extend(
            [
                f"## {candidate['classification']} - {candidate['shape']}",
                "",
                f"- Count: {candidate['count']}",
                f"- Confidence: {candidate['confidence']}",
                f"- Evidence: {candidate['evidence']['evidence_status']}"
                f" (first cycle {candidate['evidence']['first_cycle']},"
                f" latest cycle {candidate['evidence']['latest_cycle']},"
                f" age {candidate['evidence']['evidence_age_cycles']},"
                f" expires cycle {candidate['evidence']['evidence_expires_cycle']})",
                f"- Risk: {candidate['risk']}",
                f"- Environment coverage: {candidate['environment_coverage'] or {}}",
                f"- Promotion gate: {candidate['promotion_gate']['status']}"
                f" (blocks={candidate['promotion_gate']['blocks_promotion']})",
                f"- Contradiction coverage: {candidate['contradiction_coverage']['status']}",
                f"- Suggested test: {candidate['suggested_test']}",
                "- Examples:",
            ]
        )
        for example in candidate["examples"]:
            lines.append(f"  - `{example['source']}:{example['line']}` {example['text']}")
        lines.append("")

    (output_dir / "promotion-docket.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, help="File or directory of logs/events to scan")
    parser.add_argument("--output", required=True, help="Directory for promotion reports")
    args = parser.parse_args()

    events = load_events(Path(args.input))
    candidates = build_candidates(events)
    write_reports(candidates, events, Path(args.output))
    print(f"scanned {len(events)} events; wrote {len(candidates)} promotion candidates to {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
