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
from typing import Iterable


PROMOTION_THRESHOLD = 2


@dataclass(frozen=True)
class Event:
    source: str
    line: int
    kind: str
    shape: str
    text: str
    risk: str = "unknown"
    cycle: str = ""


def normalize(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"https?://\\S+", "<url>", value)
    value = re.sub(r"\\b\\d{4}-\\d{2}-\\d{2}(?:[ t]\\d{2}:\\d{2}(?::\\d{2})?)?\\b", "<time>", value)
    value = re.sub(r"\\b\\d+\\b", "<n>", value)
    value = re.sub(r"\\s+", " ", value)
    return value[:220]


def iter_input_files(root: Path) -> Iterable[Path]:
    if root.is_file():
        yield root
        return
    for path in sorted(root.rglob("*")):
        if path.suffix.lower() in {".jsonl", ".log", ".txt", ".md"} and path.is_file():
            yield path


def event_from_record(record: dict, source: Path, line_number: int) -> Event | None:
    text = str(
        record.get("action")
        or record.get("command")
        or record.get("tool")
        or record.get("decision")
        or record.get("message")
        or ""
    ).strip()
    if not text:
        return None

    kind = str(record.get("type") or record.get("kind") or infer_kind(text)).lower()
    risk = str(record.get("risk") or "unknown").lower()
    cycle = str(record.get("cycle") or "")
    return Event(str(source), line_number, kind, normalize(text), text, risk, cycle)


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
    text = line.strip()
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
                    else:
                        event = event_from_record(record, path, line_number)
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
    for event in events:
        groups[(event.kind, event.shape)].append(event)

    candidates: list[dict] = []
    for (kind, shape), grouped in groups.items():
        if len(grouped) < PROMOTION_THRESHOLD:
            continue
        texts = [event.text for event in grouped]
        risks = [event.risk for event in grouped]
        classification = classify(kind, texts, risks)
        confidence = min(0.95, 0.45 + 0.12 * len(grouped))
        candidate_id = hashlib.sha256(f"{kind}:{shape}".encode("utf-8")).hexdigest()[:12]
        candidates.append(
            {
                "id": candidate_id,
                "classification": classification,
                "kind": kind,
                "shape": shape,
                "count": len(grouped),
                "confidence": round(confidence, 2),
                "risk": risk_for(classification, len(grouped)),
                "suggested_test": suggested_test(classification, shape),
                "examples": [
                    {
                        "source": event.source,
                        "line": event.line,
                        "cycle": event.cycle,
                        "text": event.text,
                    }
                    for event in grouped[:5]
                ],
            }
        )

    return sorted(candidates, key=lambda item: (-item["count"], item["classification"], item["shape"]))


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
                f"- Risk: {candidate['risk']}",
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
