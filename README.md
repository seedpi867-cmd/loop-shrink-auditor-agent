# loop-shrink-auditor-agent

An autonomous loop that watches another autonomous loop for repeated work that should stop being model-mediated.

The premise is simple: if the same approval, command, repair, denial, or evidence judgment appears over and over, the loop has learned enough to compress that shape into code, policy, a fixture, or a denial rule. Human attention should be scarce. Agentic judgment should shrink around what it has already discovered.

## First Slice

`tools/audit_loop_shrink.py` scans plain-text or JSONL event logs and emits:

- `promotion-map.json`: structured promotion candidates with examples, confidence, risk, and suggested tests;
- `promotion-docket.md`: human-readable docket of what should become a script, typed tool, fixture, approval budget, or deny/quarantine rule.

It also clusters repeated adjacent event sequences. A pair like `rg queued topic blog -> sed -n ... data/blog_queue.txt` is treated as one promotable routine instead of two unrelated repeated commands.

Candidates now include an evidence window: first cycle, latest cycle, evidence age, expiry cycle, and freshness status. Confidence decays when the newest example is more than 50 cycles old, and drops harder after 200 cycles. Old repetition is still visible, but it stops pretending to be current evidence.

Approval logs can use a structured `approval` object or top-level approval fields. The scanner turns repeated approval grants into a stable shape from `action_shape` or `requested_action`, plus optional `scope`, `sink`, and expiry fields. That means repeated "yes, run the publish pipeline" approvals can graduate into a script even when the request wording changes, while high-risk grants still become approval-budget candidates.

Run it against the included fixture:

```bash
python3 tools/audit_loop_shrink.py --input samples/events --output output/sample
```

Run tests:

```bash
python3 -m unittest tests/test_audit_loop_shrink.py
```

## Classifications

- `script`: repeated command sequence with stable preconditions.
- `typed_tool`: repeated structured operation with bounded parameters.
- `fixture`: repeated judgment that depends on checkable evidence.
- `approval_budget`: rare high-impact action that still deserves exact human review.
- `deny_or_quarantine`: action shape that should be blocked or isolated.

## What To Feed It

The scanner accepts `.jsonl`, `.log`, `.txt`, and `.md` files. JSONL records can include `type`, `action`, `command`, `tool`, `decision`, `risk`, `reason`, and `cycle`; cycle exports can also use list fields such as `actions`, `commands`, and `decisions`. Structured approval records can use `type: approval_log` with an `approval` object containing fields like `decision`, `action_shape`, `scope`, `sink`, `expires`, and `risk`. Text logs are parsed with conservative keyword detection for shell commands, approval requests, denials, repeated failures, and test/fixture language. Example text is redacted for credential-shaped strings before report output.

## Loop Pattern

This repo is built on `brain-loop`: wake, read, think, act, remember, sleep. The deterministic scanner is the first tool the loop can run every cycle. The agent around it decides which promotion candidates are worth implementing next.
