# Promotion Docket

Events scanned: 2244
Promotion candidates: 320

## Summary

- `fixture`: 87
- `script`: 232
- `typed_tool`: 1

## Gate Summary

- Blocked: 233
- Passed: 0
- Condition-bound: 0
- Missing environment: 233
- Not required: 87

## fixture - refreshed stale mastodon.md

- Count: 291
- Confidence: 0.95
- Evidence: fresh (first cycle 335, latest cycle 657, age 0, expires cycle 857)
- Risk: medium
- Environment coverage: {}
- Promotion gate: not_required (blocks=False)
- Contradiction coverage: missing
- Suggested test: Add positive and negative evidence cases for `refreshed stale mastodon.md`.
- Examples:
  - `/home/seed/data/event_log.jsonl:1` refreshed stale mastodon.md
  - `/home/seed/data/event_log.jsonl:2` refreshed stale mastodon.md
  - `/home/seed/data/event_log.jsonl:3` refreshed stale mastodon.md
  - `/home/seed/data/event_log.jsonl:4` refreshed stale mastodon.md
  - `/home/seed/data/event_log.jsonl:5` refreshed stale mastodon.md

## fixture - refreshed stale email.md

- Count: 256
- Confidence: 0.95
- Evidence: fresh (first cycle 335, latest cycle 657, age 0, expires cycle 857)
- Risk: medium
- Environment coverage: {}
- Promotion gate: not_required (blocks=False)
- Contradiction coverage: missing
- Suggested test: Add positive and negative evidence cases for `refreshed stale email.md`.
- Examples:
  - `/home/seed/data/event_log.jsonl:1` refreshed stale email.md
  - `/home/seed/data/event_log.jsonl:2` refreshed stale email.md
  - `/home/seed/data/event_log.jsonl:3` refreshed stale email.md
  - `/home/seed/data/event_log.jsonl:4` refreshed stale email.md
  - `/home/seed/data/event_log.jsonl:5` refreshed stale email.md

## script - refreshed stale mastodon.md -> refreshed stale email.md

- Count: 251
- Confidence: 0.95
- Evidence: fresh (first cycle 335, latest cycle 657, age 0, expires cycle 857)
- Risk: medium
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `refreshed stale mastodon.md -> refreshed stale email.md` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:1` refreshed stale mastodon.md -> refreshed stale email.md
  - `/home/seed/data/event_log.jsonl:2` refreshed stale mastodon.md -> refreshed stale email.md
  - `/home/seed/data/event_log.jsonl:3` refreshed stale mastodon.md -> refreshed stale email.md
  - `/home/seed/data/event_log.jsonl:4` refreshed stale mastodon.md -> refreshed stale email.md
  - `/home/seed/data/event_log.jsonl:5` refreshed stale mastodon.md -> refreshed stale email.md

## fixture - compacted memory (202 lines)

- Count: 184
- Confidence: 0.95
- Evidence: aging (first cycle 335, latest cycle 559, age 98, expires cycle 759)
- Risk: medium
- Environment coverage: {}
- Promotion gate: not_required (blocks=False)
- Contradiction coverage: missing
- Suggested test: Add positive and negative evidence cases for `compacted memory (202 lines)`.
- Examples:
  - `/home/seed/data/event_log.jsonl:1` compacted memory (202 lines)
  - `/home/seed/data/event_log.jsonl:3` compacted memory (202 lines)
  - `/home/seed/data/event_log.jsonl:4` compacted memory (202 lines)
  - `/home/seed/data/event_log.jsonl:5` compacted memory (202 lines)
  - `/home/seed/data/event_log.jsonl:6` compacted memory (202 lines)

## fixture - posted to mastodon

- Count: 181
- Confidence: 0.95
- Evidence: fresh (first cycle 342, latest cycle 657, age 0, expires cycle 857)
- Risk: medium
- Environment coverage: {}
- Promotion gate: not_required (blocks=False)
- Contradiction coverage: missing
- Suggested test: Add positive and negative evidence cases for `posted to mastodon`.
- Examples:
  - `/home/seed/data/event_log.jsonl:6` posted to Mastodon
  - `/home/seed/data/event_log.jsonl:7` posted to Mastodon
  - `/home/seed/data/event_log.jsonl:8` posted to Mastodon
  - `/home/seed/data/event_log.jsonl:9` posted to Mastodon
  - `/home/seed/data/event_log.jsonl:13` posted to Mastodon

## fixture - rebuilt feeds

- Count: 181
- Confidence: 0.95
- Evidence: fresh (first cycle 342, latest cycle 657, age 0, expires cycle 857)
- Risk: medium
- Environment coverage: {}
- Promotion gate: not_required (blocks=False)
- Contradiction coverage: missing
- Suggested test: Add positive and negative evidence cases for `rebuilt feeds`.
- Examples:
  - `/home/seed/data/event_log.jsonl:6` rebuilt feeds
  - `/home/seed/data/event_log.jsonl:7` rebuilt feeds
  - `/home/seed/data/event_log.jsonl:8` rebuilt feeds
  - `/home/seed/data/event_log.jsonl:9` rebuilt feeds
  - `/home/seed/data/event_log.jsonl:13` rebuilt feeds

## script - posted to mastodon -> rebuilt feeds

- Count: 181
- Confidence: 0.95
- Evidence: fresh (first cycle 342, latest cycle 657, age 0, expires cycle 857)
- Risk: medium
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `posted to mastodon -> rebuilt feeds` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:6` posted to Mastodon -> rebuilt feeds
  - `/home/seed/data/event_log.jsonl:7` posted to Mastodon -> rebuilt feeds
  - `/home/seed/data/event_log.jsonl:8` posted to Mastodon -> rebuilt feeds
  - `/home/seed/data/event_log.jsonl:9` posted to Mastodon -> rebuilt feeds
  - `/home/seed/data/event_log.jsonl:13` posted to Mastodon -> rebuilt feeds

## script - compacted memory (202 lines) -> refreshed stale mastodon.md

- Count: 146
- Confidence: 0.95
- Evidence: aging (first cycle 335, latest cycle 559, age 98, expires cycle 759)
- Risk: medium
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `compacted memory (202 lines) -> refreshed stale mastodon.md` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:1` compacted memory (202 lines) -> refreshed stale mastodon.md
  - `/home/seed/data/event_log.jsonl:3` compacted memory (202 lines) -> refreshed stale mastodon.md
  - `/home/seed/data/event_log.jsonl:4` compacted memory (202 lines) -> refreshed stale mastodon.md
  - `/home/seed/data/event_log.jsonl:5` compacted memory (202 lines) -> refreshed stale mastodon.md
  - `/home/seed/data/event_log.jsonl:7` compacted memory (202 lines) -> refreshed stale mastodon.md

## script - compacted memory (202 lines) -> refreshed stale mastodon.md -> refreshed stale email.md

- Count: 122
- Confidence: 0.95
- Evidence: aging (first cycle 335, latest cycle 559, age 98, expires cycle 759)
- Risk: medium
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `compacted memory (202 lines) -> refreshed stale mastodon.md -> refreshed stale email.md` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:1` compacted memory (202 lines) -> refreshed stale mastodon.md -> refreshed stale email.md
  - `/home/seed/data/event_log.jsonl:3` compacted memory (202 lines) -> refreshed stale mastodon.md -> refreshed stale email.md
  - `/home/seed/data/event_log.jsonl:4` compacted memory (202 lines) -> refreshed stale mastodon.md -> refreshed stale email.md
  - `/home/seed/data/event_log.jsonl:5` compacted memory (202 lines) -> refreshed stale mastodon.md -> refreshed stale email.md
  - `/home/seed/data/event_log.jsonl:7` compacted memory (202 lines) -> refreshed stale mastodon.md -> refreshed stale email.md

## fixture - boosted starved drive create

- Count: 81
- Confidence: 0.95
- Evidence: fresh (first cycle 335, latest cycle 656, age 1, expires cycle 856)
- Risk: medium
- Environment coverage: {}
- Promotion gate: not_required (blocks=False)
- Contradiction coverage: missing
- Suggested test: Add positive and negative evidence cases for `boosted starved drive create`.
- Examples:
  - `/home/seed/data/event_log.jsonl:1` boosted starved drive create
  - `/home/seed/data/event_log.jsonl:2` boosted starved drive create
  - `/home/seed/data/event_log.jsonl:3` boosted starved drive create
  - `/home/seed/data/event_log.jsonl:5` boosted starved drive create
  - `/home/seed/data/event_log.jsonl:6` boosted starved drive create

## fixture - boosted starved drive express

- Count: 73
- Confidence: 0.95
- Evidence: stale (first cycle 335, latest cycle 450, age 207, expires cycle 650)
- Risk: medium
- Environment coverage: {}
- Promotion gate: not_required (blocks=False)
- Contradiction coverage: missing
- Suggested test: Add positive and negative evidence cases for `boosted starved drive express`.
- Examples:
  - `/home/seed/data/event_log.jsonl:1` boosted starved drive express
  - `/home/seed/data/event_log.jsonl:2` boosted starved drive express
  - `/home/seed/data/event_log.jsonl:3` boosted starved drive express
  - `/home/seed/data/event_log.jsonl:5` boosted starved drive express
  - `/home/seed/data/event_log.jsonl:6` boosted starved drive express

## script - posted to mastodon -> rebuilt feeds -> compacted memory (202 lines)

- Count: 73
- Confidence: 0.95
- Evidence: aging (first cycle 343, latest cycle 559, age 98, expires cycle 759)
- Risk: medium
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `posted to mastodon -> rebuilt feeds -> compacted memory (202 lines)` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:7` posted to Mastodon -> rebuilt feeds -> compacted memory (202 lines)
  - `/home/seed/data/event_log.jsonl:8` posted to Mastodon -> rebuilt feeds -> compacted memory (202 lines)
  - `/home/seed/data/event_log.jsonl:9` posted to Mastodon -> rebuilt feeds -> compacted memory (202 lines)
  - `/home/seed/data/event_log.jsonl:14` posted to Mastodon -> rebuilt feeds -> compacted memory (202 lines)
  - `/home/seed/data/event_log.jsonl:21` posted to Mastodon -> rebuilt feeds -> compacted memory (202 lines)

## script - rebuilt feeds -> compacted memory (202 lines)

- Count: 73
- Confidence: 0.95
- Evidence: aging (first cycle 343, latest cycle 559, age 98, expires cycle 759)
- Risk: medium
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `rebuilt feeds -> compacted memory (202 lines)` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:7` rebuilt feeds -> compacted memory (202 lines)
  - `/home/seed/data/event_log.jsonl:8` rebuilt feeds -> compacted memory (202 lines)
  - `/home/seed/data/event_log.jsonl:9` rebuilt feeds -> compacted memory (202 lines)
  - `/home/seed/data/event_log.jsonl:14` rebuilt feeds -> compacted memory (202 lines)
  - `/home/seed/data/event_log.jsonl:21` rebuilt feeds -> compacted memory (202 lines)

## script - refreshed stale email.md -> boosted starved drive create

- Count: 72
- Confidence: 0.95
- Evidence: fresh (first cycle 335, latest cycle 656, age 1, expires cycle 856)
- Risk: medium
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `refreshed stale email.md -> boosted starved drive create` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:1` refreshed stale email.md -> boosted starved drive create
  - `/home/seed/data/event_log.jsonl:2` refreshed stale email.md -> boosted starved drive create
  - `/home/seed/data/event_log.jsonl:3` refreshed stale email.md -> boosted starved drive create
  - `/home/seed/data/event_log.jsonl:5` refreshed stale email.md -> boosted starved drive create
  - `/home/seed/data/event_log.jsonl:6` refreshed stale email.md -> boosted starved drive create

## script - refreshed stale mastodon.md -> refreshed stale email.md -> boosted starved drive create

- Count: 72
- Confidence: 0.95
- Evidence: fresh (first cycle 335, latest cycle 656, age 1, expires cycle 856)
- Risk: medium
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `refreshed stale mastodon.md -> refreshed stale email.md -> boosted starved drive create` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:1` refreshed stale mastodon.md -> refreshed stale email.md -> boosted starved drive create
  - `/home/seed/data/event_log.jsonl:2` refreshed stale mastodon.md -> refreshed stale email.md -> boosted starved drive create
  - `/home/seed/data/event_log.jsonl:3` refreshed stale mastodon.md -> refreshed stale email.md -> boosted starved drive create
  - `/home/seed/data/event_log.jsonl:5` refreshed stale mastodon.md -> refreshed stale email.md -> boosted starved drive create
  - `/home/seed/data/event_log.jsonl:6` refreshed stale mastodon.md -> refreshed stale email.md -> boosted starved drive create

## fixture - logged bug + added fix task

- Count: 68
- Confidence: 0.95
- Evidence: fresh (first cycle 342, latest cycle 627, age 30, expires cycle 827)
- Risk: medium
- Environment coverage: {}
- Promotion gate: not_required (blocks=False)
- Contradiction coverage: missing
- Suggested test: Add positive and negative evidence cases for `logged bug + added fix task`.
- Examples:
  - `/home/seed/data/event_log.jsonl:6` logged bug + added fix task
  - `/home/seed/data/event_log.jsonl:10` logged bug + added fix task
  - `/home/seed/data/event_log.jsonl:11` logged bug + added fix task
  - `/home/seed/data/event_log.jsonl:13` logged bug + added fix task
  - `/home/seed/data/event_log.jsonl:16` logged bug + added fix task

## script - rebuilt feeds -> compacted memory (202 lines) -> refreshed stale mastodon.md

- Count: 68
- Confidence: 0.95
- Evidence: aging (first cycle 343, latest cycle 559, age 98, expires cycle 759)
- Risk: medium
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `rebuilt feeds -> compacted memory (202 lines) -> refreshed stale mastodon.md` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:7` rebuilt feeds -> compacted memory (202 lines) -> refreshed stale mastodon.md
  - `/home/seed/data/event_log.jsonl:8` rebuilt feeds -> compacted memory (202 lines) -> refreshed stale mastodon.md
  - `/home/seed/data/event_log.jsonl:9` rebuilt feeds -> compacted memory (202 lines) -> refreshed stale mastodon.md
  - `/home/seed/data/event_log.jsonl:14` rebuilt feeds -> compacted memory (202 lines) -> refreshed stale mastodon.md
  - `/home/seed/data/event_log.jsonl:21` rebuilt feeds -> compacted memory (202 lines) -> refreshed stale mastodon.md

## fixture - boosted starved drive explore

- Count: 65
- Confidence: 0.95
- Evidence: fresh (first cycle 368, latest cycle 657, age 0, expires cycle 857)
- Risk: medium
- Environment coverage: {}
- Promotion gate: not_required (blocks=False)
- Contradiction coverage: missing
- Suggested test: Add positive and negative evidence cases for `boosted starved drive explore`.
- Examples:
  - `/home/seed/data/event_log.jsonl:32` boosted starved drive explore
  - `/home/seed/data/event_log.jsonl:33` boosted starved drive explore
  - `/home/seed/data/event_log.jsonl:34` boosted starved drive explore
  - `/home/seed/data/event_log.jsonl:35` boosted starved drive explore
  - `/home/seed/data/event_log.jsonl:36` boosted starved drive explore

## fixture - boosted starved drive order

- Count: 50
- Confidence: 0.95
- Evidence: fresh (first cycle 335, latest cycle 649, age 8, expires cycle 849)
- Risk: medium
- Environment coverage: {}
- Promotion gate: not_required (blocks=False)
- Contradiction coverage: missing
- Suggested test: Add positive and negative evidence cases for `boosted starved drive order`.
- Examples:
  - `/home/seed/data/event_log.jsonl:1` boosted starved drive order
  - `/home/seed/data/event_log.jsonl:2` boosted starved drive order
  - `/home/seed/data/event_log.jsonl:7` boosted starved drive order
  - `/home/seed/data/event_log.jsonl:10` boosted starved drive order
  - `/home/seed/data/event_log.jsonl:12` boosted starved drive order

## fixture - flagged research for potential essay

- Count: 50
- Confidence: 0.95
- Evidence: fresh (first cycle 335, latest cycle 657, age 0, expires cycle 857)
- Risk: medium
- Environment coverage: {}
- Promotion gate: not_required (blocks=False)
- Contradiction coverage: missing
- Suggested test: Add positive and negative evidence cases for `flagged research for potential essay`.
- Examples:
  - `/home/seed/data/event_log.jsonl:1` flagged research for potential essay
  - `/home/seed/data/event_log.jsonl:2` flagged research for potential essay
  - `/home/seed/data/event_log.jsonl:9` flagged research for potential essay
  - `/home/seed/data/event_log.jsonl:10` flagged research for potential essay
  - `/home/seed/data/event_log.jsonl:14` flagged research for potential essay

## script - logged bug + added fix task -> compacted memory (202 lines)

- Count: 47
- Confidence: 0.95
- Evidence: aging (first cycle 342, latest cycle 557, age 100, expires cycle 757)
- Risk: medium
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `logged bug + added fix task -> compacted memory (202 lines)` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:6` logged bug + added fix task -> compacted memory (202 lines)
  - `/home/seed/data/event_log.jsonl:10` logged bug + added fix task -> compacted memory (202 lines)
  - `/home/seed/data/event_log.jsonl:11` logged bug + added fix task -> compacted memory (202 lines)
  - `/home/seed/data/event_log.jsonl:17` logged bug + added fix task -> compacted memory (202 lines)
  - `/home/seed/data/event_log.jsonl:20` logged bug + added fix task -> compacted memory (202 lines)

## fixture - version_control streak at 155

- Count: 46
- Confidence: 0.95
- Evidence: aging (first cycle 513, latest cycle 558, age 99, expires cycle 758)
- Risk: medium
- Environment coverage: {}
- Promotion gate: not_required (blocks=False)
- Contradiction coverage: missing
- Suggested test: Add positive and negative evidence cases for `version_control streak at 155`.
- Examples:
  - `/home/seed/data/event_log.jsonl:176` version_control streak at 155
  - `/home/seed/data/event_log.jsonl:177` version_control streak at 155
  - `/home/seed/data/event_log.jsonl:178` version_control streak at 155
  - `/home/seed/data/event_log.jsonl:179` version_control streak at 155
  - `/home/seed/data/event_log.jsonl:180` version_control streak at 155

## script - boosted starved drive express -> boosted starved drive order

- Count: 46
- Confidence: 0.95
- Evidence: stale (first cycle 335, latest cycle 410, age 247, expires cycle 610)
- Risk: medium
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `boosted starved drive express -> boosted starved drive order` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:1` boosted starved drive express -> boosted starved drive order
  - `/home/seed/data/event_log.jsonl:2` boosted starved drive express -> boosted starved drive order
  - `/home/seed/data/event_log.jsonl:7` boosted starved drive express -> boosted starved drive order
  - `/home/seed/data/event_log.jsonl:10` boosted starved drive express -> boosted starved drive order
  - `/home/seed/data/event_log.jsonl:12` boosted starved drive express -> boosted starved drive order

## script - boosted starved drive create -> boosted starved drive explore

- Count: 45
- Confidence: 0.95
- Evidence: fresh (first cycle 368, latest cycle 650, age 7, expires cycle 850)
- Risk: medium
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `boosted starved drive create -> boosted starved drive explore` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:32` boosted starved drive create -> boosted starved drive explore
  - `/home/seed/data/event_log.jsonl:33` boosted starved drive create -> boosted starved drive explore
  - `/home/seed/data/event_log.jsonl:34` boosted starved drive create -> boosted starved drive explore
  - `/home/seed/data/event_log.jsonl:35` boosted starved drive create -> boosted starved drive explore
  - `/home/seed/data/event_log.jsonl:36` boosted starved drive create -> boosted starved drive explore

## script - posted to mastodon -> rebuilt feeds -> logged bug + added fix task

- Count: 45
- Confidence: 0.95
- Evidence: aging (first cycle 342, latest cycle 600, age 57, expires cycle 800)
- Risk: medium
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `posted to mastodon -> rebuilt feeds -> logged bug + added fix task` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:6` posted to Mastodon -> rebuilt feeds -> logged bug + added fix task
  - `/home/seed/data/event_log.jsonl:13` posted to Mastodon -> rebuilt feeds -> logged bug + added fix task
  - `/home/seed/data/event_log.jsonl:17` posted to Mastodon -> rebuilt feeds -> logged bug + added fix task
  - `/home/seed/data/event_log.jsonl:18` posted to Mastodon -> rebuilt feeds -> logged bug + added fix task
  - `/home/seed/data/event_log.jsonl:22` posted to Mastodon -> rebuilt feeds -> logged bug + added fix task

## script - rebuilt feeds -> logged bug + added fix task

- Count: 45
- Confidence: 0.95
- Evidence: aging (first cycle 342, latest cycle 600, age 57, expires cycle 800)
- Risk: medium
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `rebuilt feeds -> logged bug + added fix task` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:6` rebuilt feeds -> logged bug + added fix task
  - `/home/seed/data/event_log.jsonl:13` rebuilt feeds -> logged bug + added fix task
  - `/home/seed/data/event_log.jsonl:17` rebuilt feeds -> logged bug + added fix task
  - `/home/seed/data/event_log.jsonl:18` rebuilt feeds -> logged bug + added fix task
  - `/home/seed/data/event_log.jsonl:22` rebuilt feeds -> logged bug + added fix task

## fixture - archived completed tasks

- Count: 39
- Confidence: 0.95
- Evidence: fresh (first cycle 342, latest cycle 610, age 47, expires cycle 810)
- Risk: medium
- Environment coverage: {}
- Promotion gate: not_required (blocks=False)
- Contradiction coverage: missing
- Suggested test: Add positive and negative evidence cases for `archived completed tasks`.
- Examples:
  - `/home/seed/data/event_log.jsonl:6` archived completed tasks
  - `/home/seed/data/event_log.jsonl:38` archived completed tasks
  - `/home/seed/data/event_log.jsonl:39` archived completed tasks
  - `/home/seed/data/event_log.jsonl:40` archived completed tasks
  - `/home/seed/data/event_log.jsonl:45` archived completed tasks

## fixture - boosted starved drive understand

- Count: 39
- Confidence: 0.95
- Evidence: stale (first cycle 368, latest cycle 410, age 247, expires cycle 610)
- Risk: medium
- Environment coverage: {}
- Promotion gate: not_required (blocks=False)
- Contradiction coverage: missing
- Suggested test: Add positive and negative evidence cases for `boosted starved drive understand`.
- Examples:
  - `/home/seed/data/event_log.jsonl:32` boosted starved drive understand
  - `/home/seed/data/event_log.jsonl:33` boosted starved drive understand
  - `/home/seed/data/event_log.jsonl:34` boosted starved drive understand
  - `/home/seed/data/event_log.jsonl:35` boosted starved drive understand
  - `/home/seed/data/event_log.jsonl:36` boosted starved drive understand

## script - archived completed tasks -> refreshed stale mastodon.md

- Count: 39
- Confidence: 0.95
- Evidence: fresh (first cycle 342, latest cycle 610, age 47, expires cycle 810)
- Risk: medium
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `archived completed tasks -> refreshed stale mastodon.md` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:6` archived completed tasks -> refreshed stale mastodon.md
  - `/home/seed/data/event_log.jsonl:38` archived completed tasks -> refreshed stale mastodon.md
  - `/home/seed/data/event_log.jsonl:39` archived completed tasks -> refreshed stale mastodon.md
  - `/home/seed/data/event_log.jsonl:40` archived completed tasks -> refreshed stale mastodon.md
  - `/home/seed/data/event_log.jsonl:45` archived completed tasks -> refreshed stale mastodon.md

## script - boosted starved drive understand -> boosted starved drive express

- Count: 39
- Confidence: 0.95
- Evidence: stale (first cycle 368, latest cycle 410, age 247, expires cycle 610)
- Risk: medium
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `boosted starved drive understand -> boosted starved drive express` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:32` boosted starved drive understand -> boosted starved drive express
  - `/home/seed/data/event_log.jsonl:33` boosted starved drive understand -> boosted starved drive express
  - `/home/seed/data/event_log.jsonl:34` boosted starved drive understand -> boosted starved drive express
  - `/home/seed/data/event_log.jsonl:35` boosted starved drive understand -> boosted starved drive express
  - `/home/seed/data/event_log.jsonl:36` boosted starved drive understand -> boosted starved drive express

## script - posted to mastodon -> rebuilt feeds -> refreshed stale mastodon.md

- Count: 39
- Confidence: 0.95
- Evidence: fresh (first cycle 562, latest cycle 657, age 0, expires cycle 857)
- Risk: medium
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `posted to mastodon -> rebuilt feeds -> refreshed stale mastodon.md` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:225` posted to Mastodon -> rebuilt feeds -> refreshed stale mastodon.md
  - `/home/seed/data/event_log.jsonl:226` posted to Mastodon -> rebuilt feeds -> refreshed stale mastodon.md
  - `/home/seed/data/event_log.jsonl:227` posted to Mastodon -> rebuilt feeds -> refreshed stale mastodon.md
  - `/home/seed/data/event_log.jsonl:229` posted to Mastodon -> rebuilt feeds -> refreshed stale mastodon.md
  - `/home/seed/data/event_log.jsonl:247` posted to Mastodon -> rebuilt feeds -> refreshed stale mastodon.md

## script - rebuilt feeds -> refreshed stale mastodon.md

- Count: 39
- Confidence: 0.95
- Evidence: fresh (first cycle 562, latest cycle 657, age 0, expires cycle 857)
- Risk: medium
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `rebuilt feeds -> refreshed stale mastodon.md` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:225` rebuilt feeds -> refreshed stale mastodon.md
  - `/home/seed/data/event_log.jsonl:226` rebuilt feeds -> refreshed stale mastodon.md
  - `/home/seed/data/event_log.jsonl:227` rebuilt feeds -> refreshed stale mastodon.md
  - `/home/seed/data/event_log.jsonl:229` rebuilt feeds -> refreshed stale mastodon.md
  - `/home/seed/data/event_log.jsonl:247` rebuilt feeds -> refreshed stale mastodon.md

## script - rebuilt feeds -> refreshed stale mastodon.md -> refreshed stale email.md

- Count: 39
- Confidence: 0.95
- Evidence: fresh (first cycle 562, latest cycle 657, age 0, expires cycle 857)
- Risk: medium
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `rebuilt feeds -> refreshed stale mastodon.md -> refreshed stale email.md` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:225` rebuilt feeds -> refreshed stale mastodon.md -> refreshed stale email.md
  - `/home/seed/data/event_log.jsonl:226` rebuilt feeds -> refreshed stale mastodon.md -> refreshed stale email.md
  - `/home/seed/data/event_log.jsonl:227` rebuilt feeds -> refreshed stale mastodon.md -> refreshed stale email.md
  - `/home/seed/data/event_log.jsonl:229` rebuilt feeds -> refreshed stale mastodon.md -> refreshed stale email.md
  - `/home/seed/data/event_log.jsonl:247` rebuilt feeds -> refreshed stale mastodon.md -> refreshed stale email.md

## script - refreshed stale email.md -> boosted starved drive create -> boosted starved drive explore

- Count: 39
- Confidence: 0.95
- Evidence: fresh (first cycle 368, latest cycle 650, age 7, expires cycle 850)
- Risk: medium
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `refreshed stale email.md -> boosted starved drive create -> boosted starved drive explore` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:32` refreshed stale email.md -> boosted starved drive create -> boosted starved drive explore
  - `/home/seed/data/event_log.jsonl:33` refreshed stale email.md -> boosted starved drive create -> boosted starved drive explore
  - `/home/seed/data/event_log.jsonl:34` refreshed stale email.md -> boosted starved drive create -> boosted starved drive explore
  - `/home/seed/data/event_log.jsonl:35` refreshed stale email.md -> boosted starved drive create -> boosted starved drive explore
  - `/home/seed/data/event_log.jsonl:36` refreshed stale email.md -> boosted starved drive create -> boosted starved drive explore

## script - logged bug + added fix task -> compacted memory (202 lines) -> refreshed stale mastodon.md

- Count: 38
- Confidence: 0.95
- Evidence: aging (first cycle 346, latest cycle 557, age 100, expires cycle 757)
- Risk: medium
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `logged bug + added fix task -> compacted memory (202 lines) -> refreshed stale mastodon.md` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:10` logged bug + added fix task -> compacted memory (202 lines) -> refreshed stale mastodon.md
  - `/home/seed/data/event_log.jsonl:11` logged bug + added fix task -> compacted memory (202 lines) -> refreshed stale mastodon.md
  - `/home/seed/data/event_log.jsonl:17` logged bug + added fix task -> compacted memory (202 lines) -> refreshed stale mastodon.md
  - `/home/seed/data/event_log.jsonl:20` logged bug + added fix task -> compacted memory (202 lines) -> refreshed stale mastodon.md
  - `/home/seed/data/event_log.jsonl:22` logged bug + added fix task -> compacted memory (202 lines) -> refreshed stale mastodon.md

## fixture - compacted memory (201 lines)

- Count: 34
- Confidence: 0.95
- Evidence: aging (first cycle 336, latest cycle 553, age 104, expires cycle 753)
- Risk: medium
- Environment coverage: {}
- Promotion gate: not_required (blocks=False)
- Contradiction coverage: missing
- Suggested test: Add positive and negative evidence cases for `compacted memory (201 lines)`.
- Examples:
  - `/home/seed/data/event_log.jsonl:2` compacted memory (201 lines)
  - `/home/seed/data/event_log.jsonl:13` compacted memory (201 lines)
  - `/home/seed/data/event_log.jsonl:16` compacted memory (201 lines)
  - `/home/seed/data/event_log.jsonl:18` compacted memory (201 lines)
  - `/home/seed/data/event_log.jsonl:28` compacted memory (201 lines)

## script - rebuilt feeds -> logged bug + added fix task -> compacted memory (202 lines)

- Count: 32
- Confidence: 0.95
- Evidence: aging (first cycle 342, latest cycle 556, age 101, expires cycle 756)
- Risk: medium
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `rebuilt feeds -> logged bug + added fix task -> compacted memory (202 lines)` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:6` rebuilt feeds -> logged bug + added fix task -> compacted memory (202 lines)
  - `/home/seed/data/event_log.jsonl:17` rebuilt feeds -> logged bug + added fix task -> compacted memory (202 lines)
  - `/home/seed/data/event_log.jsonl:22` rebuilt feeds -> logged bug + added fix task -> compacted memory (202 lines)
  - `/home/seed/data/event_log.jsonl:30` rebuilt feeds -> logged bug + added fix task -> compacted memory (202 lines)
  - `/home/seed/data/event_log.jsonl:31` rebuilt feeds -> logged bug + added fix task -> compacted memory (202 lines)

## script - archived completed tasks -> refreshed stale mastodon.md -> refreshed stale email.md

- Count: 31
- Confidence: 0.95
- Evidence: fresh (first cycle 342, latest cycle 610, age 47, expires cycle 810)
- Risk: medium
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `archived completed tasks -> refreshed stale mastodon.md -> refreshed stale email.md` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:6` archived completed tasks -> refreshed stale mastodon.md -> refreshed stale email.md
  - `/home/seed/data/event_log.jsonl:38` archived completed tasks -> refreshed stale mastodon.md -> refreshed stale email.md
  - `/home/seed/data/event_log.jsonl:39` archived completed tasks -> refreshed stale mastodon.md -> refreshed stale email.md
  - `/home/seed/data/event_log.jsonl:40` archived completed tasks -> refreshed stale mastodon.md -> refreshed stale email.md
  - `/home/seed/data/event_log.jsonl:45` archived completed tasks -> refreshed stale mastodon.md -> refreshed stale email.md

## script - compacted memory (201 lines) -> refreshed stale mastodon.md

- Count: 30
- Confidence: 0.95
- Evidence: aging (first cycle 336, latest cycle 553, age 104, expires cycle 753)
- Risk: medium
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `compacted memory (201 lines) -> refreshed stale mastodon.md` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:2` compacted memory (201 lines) -> refreshed stale mastodon.md
  - `/home/seed/data/event_log.jsonl:13` compacted memory (201 lines) -> refreshed stale mastodon.md
  - `/home/seed/data/event_log.jsonl:16` compacted memory (201 lines) -> refreshed stale mastodon.md
  - `/home/seed/data/event_log.jsonl:18` compacted memory (201 lines) -> refreshed stale mastodon.md
  - `/home/seed/data/event_log.jsonl:28` compacted memory (201 lines) -> refreshed stale mastodon.md

## script - compacted memory (202 lines) -> archived completed tasks

- Count: 30
- Confidence: 0.95
- Evidence: aging (first cycle 342, latest cycle 540, age 117, expires cycle 740)
- Risk: medium
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `compacted memory (202 lines) -> archived completed tasks` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:6` compacted memory (202 lines) -> archived completed tasks
  - `/home/seed/data/event_log.jsonl:38` compacted memory (202 lines) -> archived completed tasks
  - `/home/seed/data/event_log.jsonl:39` compacted memory (202 lines) -> archived completed tasks
  - `/home/seed/data/event_log.jsonl:40` compacted memory (202 lines) -> archived completed tasks
  - `/home/seed/data/event_log.jsonl:45` compacted memory (202 lines) -> archived completed tasks

## script - compacted memory (202 lines) -> archived completed tasks -> refreshed stale mastodon.md

- Count: 30
- Confidence: 0.95
- Evidence: aging (first cycle 342, latest cycle 540, age 117, expires cycle 740)
- Risk: medium
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `compacted memory (202 lines) -> archived completed tasks -> refreshed stale mastodon.md` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:6` compacted memory (202 lines) -> archived completed tasks -> refreshed stale mastodon.md
  - `/home/seed/data/event_log.jsonl:38` compacted memory (202 lines) -> archived completed tasks -> refreshed stale mastodon.md
  - `/home/seed/data/event_log.jsonl:39` compacted memory (202 lines) -> archived completed tasks -> refreshed stale mastodon.md
  - `/home/seed/data/event_log.jsonl:40` compacted memory (202 lines) -> archived completed tasks -> refreshed stale mastodon.md
  - `/home/seed/data/event_log.jsonl:45` compacted memory (202 lines) -> archived completed tasks -> refreshed stale mastodon.md

## script - boosted starved drive understand -> boosted starved drive express -> boosted starved drive order

- Count: 28
- Confidence: 0.95
- Evidence: stale (first cycle 369, latest cycle 410, age 247, expires cycle 610)
- Risk: medium
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `boosted starved drive understand -> boosted starved drive express -> boosted starved drive order` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:33` boosted starved drive understand -> boosted starved drive express -> boosted starved drive order
  - `/home/seed/data/event_log.jsonl:35` boosted starved drive understand -> boosted starved drive express -> boosted starved drive order
  - `/home/seed/data/event_log.jsonl:37` boosted starved drive understand -> boosted starved drive express -> boosted starved drive order
  - `/home/seed/data/event_log.jsonl:38` boosted starved drive understand -> boosted starved drive express -> boosted starved drive order
  - `/home/seed/data/event_log.jsonl:40` boosted starved drive understand -> boosted starved drive express -> boosted starved drive order

## script - boosted starved drive create -> boosted starved drive express

- Count: 27
- Confidence: 0.95
- Evidence: stale (first cycle 335, latest cycle 367, age 290, expires cycle 567)
- Risk: medium
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `boosted starved drive create -> boosted starved drive express` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:1` boosted starved drive create -> boosted starved drive express
  - `/home/seed/data/event_log.jsonl:2` boosted starved drive create -> boosted starved drive express
  - `/home/seed/data/event_log.jsonl:3` boosted starved drive create -> boosted starved drive express
  - `/home/seed/data/event_log.jsonl:5` boosted starved drive create -> boosted starved drive express
  - `/home/seed/data/event_log.jsonl:6` boosted starved drive create -> boosted starved drive express

## script - compacted memory (201 lines) -> refreshed stale mastodon.md -> refreshed stale email.md

- Count: 27
- Confidence: 0.95
- Evidence: aging (first cycle 336, latest cycle 549, age 108, expires cycle 749)
- Risk: medium
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `compacted memory (201 lines) -> refreshed stale mastodon.md -> refreshed stale email.md` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:2` compacted memory (201 lines) -> refreshed stale mastodon.md -> refreshed stale email.md
  - `/home/seed/data/event_log.jsonl:13` compacted memory (201 lines) -> refreshed stale mastodon.md -> refreshed stale email.md
  - `/home/seed/data/event_log.jsonl:16` compacted memory (201 lines) -> refreshed stale mastodon.md -> refreshed stale email.md
  - `/home/seed/data/event_log.jsonl:18` compacted memory (201 lines) -> refreshed stale mastodon.md -> refreshed stale email.md
  - `/home/seed/data/event_log.jsonl:28` compacted memory (201 lines) -> refreshed stale mastodon.md -> refreshed stale email.md

## script - refreshed stale email.md -> boosted starved drive create -> boosted starved drive express

- Count: 25
- Confidence: 0.95
- Evidence: stale (first cycle 335, latest cycle 366, age 291, expires cycle 566)
- Risk: medium
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `refreshed stale email.md -> boosted starved drive create -> boosted starved drive express` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:1` refreshed stale email.md -> boosted starved drive create -> boosted starved drive express
  - `/home/seed/data/event_log.jsonl:2` refreshed stale email.md -> boosted starved drive create -> boosted starved drive express
  - `/home/seed/data/event_log.jsonl:3` refreshed stale email.md -> boosted starved drive create -> boosted starved drive express
  - `/home/seed/data/event_log.jsonl:5` refreshed stale email.md -> boosted starved drive create -> boosted starved drive express
  - `/home/seed/data/event_log.jsonl:6` refreshed stale email.md -> boosted starved drive create -> boosted starved drive express

## fixture - refreshed stale trends.md

- Count: 24
- Confidence: 0.95
- Evidence: fresh (first cycle 338, latest cycle 642, age 15, expires cycle 842)
- Risk: medium
- Environment coverage: {}
- Promotion gate: not_required (blocks=False)
- Contradiction coverage: missing
- Suggested test: Add positive and negative evidence cases for `refreshed stale trends.md`.
- Examples:
  - `/home/seed/data/event_log.jsonl:4` refreshed stale trends.md
  - `/home/seed/data/event_log.jsonl:23` refreshed stale trends.md
  - `/home/seed/data/event_log.jsonl:54` refreshed stale trends.md
  - `/home/seed/data/event_log.jsonl:71` refreshed stale trends.md
  - `/home/seed/data/event_log.jsonl:91` refreshed stale trends.md

## script - boosted starved drive explore -> boosted starved drive understand

- Count: 24
- Confidence: 0.95
- Evidence: stale (first cycle 368, latest cycle 408, age 249, expires cycle 608)
- Risk: medium
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `boosted starved drive explore -> boosted starved drive understand` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:32` boosted starved drive explore -> boosted starved drive understand
  - `/home/seed/data/event_log.jsonl:33` boosted starved drive explore -> boosted starved drive understand
  - `/home/seed/data/event_log.jsonl:34` boosted starved drive explore -> boosted starved drive understand
  - `/home/seed/data/event_log.jsonl:35` boosted starved drive explore -> boosted starved drive understand
  - `/home/seed/data/event_log.jsonl:36` boosted starved drive explore -> boosted starved drive understand

## script - boosted starved drive explore -> boosted starved drive understand -> boosted starved drive express

- Count: 24
- Confidence: 0.95
- Evidence: stale (first cycle 368, latest cycle 408, age 249, expires cycle 608)
- Risk: medium
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `boosted starved drive explore -> boosted starved drive understand -> boosted starved drive express` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:32` boosted starved drive explore -> boosted starved drive understand -> boosted starved drive express
  - `/home/seed/data/event_log.jsonl:33` boosted starved drive explore -> boosted starved drive understand -> boosted starved drive express
  - `/home/seed/data/event_log.jsonl:34` boosted starved drive explore -> boosted starved drive understand -> boosted starved drive express
  - `/home/seed/data/event_log.jsonl:35` boosted starved drive explore -> boosted starved drive understand -> boosted starved drive express
  - `/home/seed/data/event_log.jsonl:36` boosted starved drive explore -> boosted starved drive understand -> boosted starved drive express

## fixture - boosted starved drive preserve

- Count: 23
- Confidence: 0.95
- Evidence: stale (first cycle 381, latest cycle 418, age 239, expires cycle 618)
- Risk: medium
- Environment coverage: {}
- Promotion gate: not_required (blocks=False)
- Contradiction coverage: missing
- Suggested test: Add positive and negative evidence cases for `boosted starved drive preserve`.
- Examples:
  - `/home/seed/data/event_log.jsonl:45` boosted starved drive preserve
  - `/home/seed/data/event_log.jsonl:48` boosted starved drive preserve
  - `/home/seed/data/event_log.jsonl:51` boosted starved drive preserve
  - `/home/seed/data/event_log.jsonl:52` boosted starved drive preserve
  - `/home/seed/data/event_log.jsonl:53` boosted starved drive preserve

## script - boosted starved drive create -> boosted starved drive explore -> boosted starved drive understand

- Count: 23
- Confidence: 0.95
- Evidence: stale (first cycle 368, latest cycle 408, age 249, expires cycle 608)
- Risk: medium
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `boosted starved drive create -> boosted starved drive explore -> boosted starved drive understand` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:32` boosted starved drive create -> boosted starved drive explore -> boosted starved drive understand
  - `/home/seed/data/event_log.jsonl:33` boosted starved drive create -> boosted starved drive explore -> boosted starved drive understand
  - `/home/seed/data/event_log.jsonl:34` boosted starved drive create -> boosted starved drive explore -> boosted starved drive understand
  - `/home/seed/data/event_log.jsonl:35` boosted starved drive create -> boosted starved drive explore -> boosted starved drive understand
  - `/home/seed/data/event_log.jsonl:36` boosted starved drive create -> boosted starved drive explore -> boosted starved drive understand

## fixture - refreshed stale outreach.md

- Count: 22
- Confidence: 0.95
- Evidence: fresh (first cycle 338, latest cycle 645, age 12, expires cycle 845)
- Risk: medium
- Environment coverage: {}
- Promotion gate: not_required (blocks=False)
- Contradiction coverage: missing
- Suggested test: Add positive and negative evidence cases for `refreshed stale outreach.md`.
- Examples:
  - `/home/seed/data/event_log.jsonl:4` refreshed stale outreach.md
  - `/home/seed/data/event_log.jsonl:31` refreshed stale outreach.md
  - `/home/seed/data/event_log.jsonl:54` refreshed stale outreach.md
  - `/home/seed/data/event_log.jsonl:79` refreshed stale outreach.md
  - `/home/seed/data/event_log.jsonl:91` refreshed stale outreach.md

## script - refreshed stale email.md -> flagged research for potential essay

- Count: 21
- Confidence: 0.95
- Evidence: fresh (first cycle 351, latest cycle 644, age 13, expires cycle 844)
- Risk: medium
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `refreshed stale email.md -> flagged research for potential essay` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:15` refreshed stale email.md -> flagged research for potential essay
  - `/home/seed/data/event_log.jsonl:88` refreshed stale email.md -> flagged research for potential essay
  - `/home/seed/data/event_log.jsonl:98` refreshed stale email.md -> flagged research for potential essay
  - `/home/seed/data/event_log.jsonl:108` refreshed stale email.md -> flagged research for potential essay
  - `/home/seed/data/event_log.jsonl:118` refreshed stale email.md -> flagged research for potential essay

## script - refreshed stale email.md -> refreshed stale trends.md

- Count: 20
- Confidence: 0.95
- Evidence: fresh (first cycle 338, latest cycle 642, age 15, expires cycle 842)
- Risk: medium
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `refreshed stale email.md -> refreshed stale trends.md` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:4` refreshed stale email.md -> refreshed stale trends.md
  - `/home/seed/data/event_log.jsonl:23` refreshed stale email.md -> refreshed stale trends.md
  - `/home/seed/data/event_log.jsonl:54` refreshed stale email.md -> refreshed stale trends.md
  - `/home/seed/data/event_log.jsonl:71` refreshed stale email.md -> refreshed stale trends.md
  - `/home/seed/data/event_log.jsonl:99` refreshed stale email.md -> refreshed stale trends.md

## script - refreshed stale mastodon.md -> refreshed stale email.md -> flagged research for potential essay

- Count: 20
- Confidence: 0.95
- Evidence: fresh (first cycle 351, latest cycle 644, age 13, expires cycle 844)
- Risk: medium
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `refreshed stale mastodon.md -> refreshed stale email.md -> flagged research for potential essay` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:15` refreshed stale mastodon.md -> refreshed stale email.md -> flagged research for potential essay
  - `/home/seed/data/event_log.jsonl:98` refreshed stale mastodon.md -> refreshed stale email.md -> flagged research for potential essay
  - `/home/seed/data/event_log.jsonl:108` refreshed stale mastodon.md -> refreshed stale email.md -> flagged research for potential essay
  - `/home/seed/data/event_log.jsonl:118` refreshed stale mastodon.md -> refreshed stale email.md -> flagged research for potential essay
  - `/home/seed/data/event_log.jsonl:128` refreshed stale mastodon.md -> refreshed stale email.md -> flagged research for potential essay

## script - refreshed stale mastodon.md -> refreshed stale email.md -> refreshed stale trends.md

- Count: 20
- Confidence: 0.95
- Evidence: fresh (first cycle 338, latest cycle 642, age 15, expires cycle 842)
- Risk: medium
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `refreshed stale mastodon.md -> refreshed stale email.md -> refreshed stale trends.md` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:4` refreshed stale mastodon.md -> refreshed stale email.md -> refreshed stale trends.md
  - `/home/seed/data/event_log.jsonl:23` refreshed stale mastodon.md -> refreshed stale email.md -> refreshed stale trends.md
  - `/home/seed/data/event_log.jsonl:54` refreshed stale mastodon.md -> refreshed stale email.md -> refreshed stale trends.md
  - `/home/seed/data/event_log.jsonl:71` refreshed stale mastodon.md -> refreshed stale email.md -> refreshed stale trends.md
  - `/home/seed/data/event_log.jsonl:99` refreshed stale mastodon.md -> refreshed stale email.md -> refreshed stale trends.md

## fixture - boosted starved drive connect

- Count: 19
- Confidence: 0.95
- Evidence: fresh (first cycle 440, latest cycle 656, age 1, expires cycle 856)
- Risk: medium
- Environment coverage: {}
- Promotion gate: not_required (blocks=False)
- Contradiction coverage: missing
- Suggested test: Add positive and negative evidence cases for `boosted starved drive connect`.
- Examples:
  - `/home/seed/data/event_log.jsonl:104` boosted starved drive connect
  - `/home/seed/data/event_log.jsonl:114` boosted starved drive connect
  - `/home/seed/data/event_log.jsonl:121` boosted starved drive connect
  - `/home/seed/data/event_log.jsonl:135` boosted starved drive connect
  - `/home/seed/data/event_log.jsonl:150` boosted starved drive connect

## script - boosted starved drive create -> boosted starved drive explore -> boosted starved drive preserve

- Count: 18
- Confidence: 0.95
- Evidence: stale (first cycle 381, latest cycle 410, age 247, expires cycle 610)
- Risk: medium
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `boosted starved drive create -> boosted starved drive explore -> boosted starved drive preserve` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:45` boosted starved drive create -> boosted starved drive explore -> boosted starved drive preserve
  - `/home/seed/data/event_log.jsonl:48` boosted starved drive create -> boosted starved drive explore -> boosted starved drive preserve
  - `/home/seed/data/event_log.jsonl:51` boosted starved drive create -> boosted starved drive explore -> boosted starved drive preserve
  - `/home/seed/data/event_log.jsonl:52` boosted starved drive create -> boosted starved drive explore -> boosted starved drive preserve
  - `/home/seed/data/event_log.jsonl:53` boosted starved drive create -> boosted starved drive explore -> boosted starved drive preserve

## script - boosted starved drive explore -> boosted starved drive preserve

- Count: 18
- Confidence: 0.95
- Evidence: stale (first cycle 381, latest cycle 410, age 247, expires cycle 610)
- Risk: medium
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `boosted starved drive explore -> boosted starved drive preserve` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:45` boosted starved drive explore -> boosted starved drive preserve
  - `/home/seed/data/event_log.jsonl:48` boosted starved drive explore -> boosted starved drive preserve
  - `/home/seed/data/event_log.jsonl:51` boosted starved drive explore -> boosted starved drive preserve
  - `/home/seed/data/event_log.jsonl:52` boosted starved drive explore -> boosted starved drive preserve
  - `/home/seed/data/event_log.jsonl:53` boosted starved drive explore -> boosted starved drive preserve

## script - refreshed stale email.md -> boosted starved drive explore

- Count: 16
- Confidence: 0.95
- Evidence: fresh (first cycle 394, latest cycle 657, age 0, expires cycle 857)
- Risk: medium
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `refreshed stale email.md -> boosted starved drive explore` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:58` refreshed stale email.md -> boosted starved drive explore
  - `/home/seed/data/event_log.jsonl:101` refreshed stale email.md -> boosted starved drive explore
  - `/home/seed/data/event_log.jsonl:107` refreshed stale email.md -> boosted starved drive explore
  - `/home/seed/data/event_log.jsonl:109` refreshed stale email.md -> boosted starved drive explore
  - `/home/seed/data/event_log.jsonl:121` refreshed stale email.md -> boosted starved drive explore

## script - refreshed stale mastodon.md -> refreshed stale email.md -> boosted starved drive explore

- Count: 16
- Confidence: 0.95
- Evidence: fresh (first cycle 394, latest cycle 657, age 0, expires cycle 857)
- Risk: medium
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `refreshed stale mastodon.md -> refreshed stale email.md -> boosted starved drive explore` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:58` refreshed stale mastodon.md -> refreshed stale email.md -> boosted starved drive explore
  - `/home/seed/data/event_log.jsonl:101` refreshed stale mastodon.md -> refreshed stale email.md -> boosted starved drive explore
  - `/home/seed/data/event_log.jsonl:107` refreshed stale mastodon.md -> refreshed stale email.md -> boosted starved drive explore
  - `/home/seed/data/event_log.jsonl:109` refreshed stale mastodon.md -> refreshed stale email.md -> boosted starved drive explore
  - `/home/seed/data/event_log.jsonl:121` refreshed stale mastodon.md -> refreshed stale email.md -> boosted starved drive explore

## script - boosted starved drive explore -> boosted starved drive preserve -> boosted starved drive understand

- Count: 15
- Confidence: 0.85
- Evidence: stale (first cycle 381, latest cycle 410, age 247, expires cycle 610)
- Risk: medium
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `boosted starved drive explore -> boosted starved drive preserve -> boosted starved drive understand` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:45` boosted starved drive explore -> boosted starved drive preserve -> boosted starved drive understand
  - `/home/seed/data/event_log.jsonl:48` boosted starved drive explore -> boosted starved drive preserve -> boosted starved drive understand
  - `/home/seed/data/event_log.jsonl:51` boosted starved drive explore -> boosted starved drive preserve -> boosted starved drive understand
  - `/home/seed/data/event_log.jsonl:52` boosted starved drive explore -> boosted starved drive preserve -> boosted starved drive understand
  - `/home/seed/data/event_log.jsonl:53` boosted starved drive explore -> boosted starved drive preserve -> boosted starved drive understand

## script - boosted starved drive preserve -> boosted starved drive understand

- Count: 15
- Confidence: 0.85
- Evidence: stale (first cycle 381, latest cycle 410, age 247, expires cycle 610)
- Risk: medium
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `boosted starved drive preserve -> boosted starved drive understand` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:45` boosted starved drive preserve -> boosted starved drive understand
  - `/home/seed/data/event_log.jsonl:48` boosted starved drive preserve -> boosted starved drive understand
  - `/home/seed/data/event_log.jsonl:51` boosted starved drive preserve -> boosted starved drive understand
  - `/home/seed/data/event_log.jsonl:52` boosted starved drive preserve -> boosted starved drive understand
  - `/home/seed/data/event_log.jsonl:53` boosted starved drive preserve -> boosted starved drive understand

## script - boosted starved drive preserve -> boosted starved drive understand -> boosted starved drive express

- Count: 15
- Confidence: 0.85
- Evidence: stale (first cycle 381, latest cycle 410, age 247, expires cycle 610)
- Risk: medium
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `boosted starved drive preserve -> boosted starved drive understand -> boosted starved drive express` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:45` boosted starved drive preserve -> boosted starved drive understand -> boosted starved drive express
  - `/home/seed/data/event_log.jsonl:48` boosted starved drive preserve -> boosted starved drive understand -> boosted starved drive express
  - `/home/seed/data/event_log.jsonl:51` boosted starved drive preserve -> boosted starved drive understand -> boosted starved drive express
  - `/home/seed/data/event_log.jsonl:52` boosted starved drive preserve -> boosted starved drive understand -> boosted starved drive express
  - `/home/seed/data/event_log.jsonl:53` boosted starved drive preserve -> boosted starved drive understand -> boosted starved drive express

## script - boosted starved drive create -> boosted starved drive express -> boosted starved drive order

- Count: 14
- Confidence: 0.81
- Evidence: stale (first cycle 335, latest cycle 367, age 290, expires cycle 567)
- Risk: medium
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `boosted starved drive create -> boosted starved drive express -> boosted starved drive order` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:1` boosted starved drive create -> boosted starved drive express -> boosted starved drive order
  - `/home/seed/data/event_log.jsonl:2` boosted starved drive create -> boosted starved drive express -> boosted starved drive order
  - `/home/seed/data/event_log.jsonl:7` boosted starved drive create -> boosted starved drive express -> boosted starved drive order
  - `/home/seed/data/event_log.jsonl:10` boosted starved drive create -> boosted starved drive express -> boosted starved drive order
  - `/home/seed/data/event_log.jsonl:12` boosted starved drive create -> boosted starved drive express -> boosted starved drive order

## fixture - task_completion streak at 170

- Count: 13
- Confidence: 0.9
- Evidence: stale (first cycle 410, latest cycle 422, age 235, expires cycle 622)
- Risk: medium
- Environment coverage: {}
- Promotion gate: not_required (blocks=False)
- Contradiction coverage: missing
- Suggested test: Add positive and negative evidence cases for `task_completion streak at 170`.
- Examples:
  - `/home/seed/data/event_log.jsonl:74` task_completion streak at 170
  - `/home/seed/data/event_log.jsonl:75` task_completion streak at 170
  - `/home/seed/data/event_log.jsonl:76` task_completion streak at 170
  - `/home/seed/data/event_log.jsonl:77` task_completion streak at 170
  - `/home/seed/data/event_log.jsonl:78` task_completion streak at 170

## fixture - publishing streak at 170

- Count: 12
- Confidence: 0.85
- Evidence: stale (first cycle 410, latest cycle 421, age 236, expires cycle 621)
- Risk: medium
- Environment coverage: {}
- Promotion gate: not_required (blocks=False)
- Contradiction coverage: missing
- Suggested test: Add positive and negative evidence cases for `publishing streak at 170`.
- Examples:
  - `/home/seed/data/event_log.jsonl:74` publishing streak at 170
  - `/home/seed/data/event_log.jsonl:75` publishing streak at 170
  - `/home/seed/data/event_log.jsonl:76` publishing streak at 170
  - `/home/seed/data/event_log.jsonl:77` publishing streak at 170
  - `/home/seed/data/event_log.jsonl:78` publishing streak at 170

## script - boosted starved drive order -> flagged research for potential essay

- Count: 12
- Confidence: 0.95
- Evidence: aging (first cycle 335, latest cycle 585, age 72, expires cycle 785)
- Risk: medium
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `boosted starved drive order -> flagged research for potential essay` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:1` boosted starved drive order -> flagged research for potential essay
  - `/home/seed/data/event_log.jsonl:2` boosted starved drive order -> flagged research for potential essay
  - `/home/seed/data/event_log.jsonl:10` boosted starved drive order -> flagged research for potential essay
  - `/home/seed/data/event_log.jsonl:19` boosted starved drive order -> flagged research for potential essay
  - `/home/seed/data/event_log.jsonl:20` boosted starved drive order -> flagged research for potential essay

## script - logged bug + added fix task -> compacted memory (201 lines)

- Count: 12
- Confidence: 0.95
- Evidence: aging (first cycle 349, latest cycle 545, age 112, expires cycle 745)
- Risk: medium
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `logged bug + added fix task -> compacted memory (201 lines)` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:13` logged bug + added fix task -> compacted memory (201 lines)
  - `/home/seed/data/event_log.jsonl:16` logged bug + added fix task -> compacted memory (201 lines)
  - `/home/seed/data/event_log.jsonl:18` logged bug + added fix task -> compacted memory (201 lines)
  - `/home/seed/data/event_log.jsonl:46` logged bug + added fix task -> compacted memory (201 lines)
  - `/home/seed/data/event_log.jsonl:63` logged bug + added fix task -> compacted memory (201 lines)

## script - logged bug + added fix task -> compacted memory (201 lines) -> refreshed stale mastodon.md

- Count: 12
- Confidence: 0.95
- Evidence: aging (first cycle 349, latest cycle 545, age 112, expires cycle 745)
- Risk: medium
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `logged bug + added fix task -> compacted memory (201 lines) -> refreshed stale mastodon.md` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:13` logged bug + added fix task -> compacted memory (201 lines) -> refreshed stale mastodon.md
  - `/home/seed/data/event_log.jsonl:16` logged bug + added fix task -> compacted memory (201 lines) -> refreshed stale mastodon.md
  - `/home/seed/data/event_log.jsonl:18` logged bug + added fix task -> compacted memory (201 lines) -> refreshed stale mastodon.md
  - `/home/seed/data/event_log.jsonl:46` logged bug + added fix task -> compacted memory (201 lines) -> refreshed stale mastodon.md
  - `/home/seed/data/event_log.jsonl:63` logged bug + added fix task -> compacted memory (201 lines) -> refreshed stale mastodon.md

## script - publishing streak at 170 -> task_completion streak at 170

- Count: 12
- Confidence: 0.72
- Evidence: stale (first cycle 410, latest cycle 421, age 236, expires cycle 621)
- Risk: medium
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `publishing streak at 170 -> task_completion streak at 170` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:74` publishing streak at 170 -> task_completion streak at 170
  - `/home/seed/data/event_log.jsonl:75` publishing streak at 170 -> task_completion streak at 170
  - `/home/seed/data/event_log.jsonl:76` publishing streak at 170 -> task_completion streak at 170
  - `/home/seed/data/event_log.jsonl:77` publishing streak at 170 -> task_completion streak at 170
  - `/home/seed/data/event_log.jsonl:78` publishing streak at 170 -> task_completion streak at 170

## script - refreshed stale trends.md -> refreshed stale outreach.md

- Count: 12
- Confidence: 0.95
- Evidence: fresh (first cycle 338, latest cycle 634, age 23, expires cycle 834)
- Risk: medium
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `refreshed stale trends.md -> refreshed stale outreach.md` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:4` refreshed stale trends.md -> refreshed stale outreach.md
  - `/home/seed/data/event_log.jsonl:54` refreshed stale trends.md -> refreshed stale outreach.md
  - `/home/seed/data/event_log.jsonl:91` refreshed stale trends.md -> refreshed stale outreach.md
  - `/home/seed/data/event_log.jsonl:111` refreshed stale trends.md -> refreshed stale outreach.md
  - `/home/seed/data/event_log.jsonl:133` refreshed stale trends.md -> refreshed stale outreach.md

## script - posted to mastodon -> rebuilt feeds -> compacted memory (201 lines)

- Count: 11
- Confidence: 0.95
- Evidence: aging (first cycle 364, latest cycle 553, age 104, expires cycle 753)
- Risk: medium
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `posted to mastodon -> rebuilt feeds -> compacted memory (201 lines)` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:28` posted to Mastodon -> rebuilt feeds -> compacted memory (201 lines)
  - `/home/seed/data/event_log.jsonl:34` posted to Mastodon -> rebuilt feeds -> compacted memory (201 lines)
  - `/home/seed/data/event_log.jsonl:71` posted to Mastodon -> rebuilt feeds -> compacted memory (201 lines)
  - `/home/seed/data/event_log.jsonl:82` posted to Mastodon -> rebuilt feeds -> compacted memory (201 lines)
  - `/home/seed/data/event_log.jsonl:104` posted to Mastodon -> rebuilt feeds -> compacted memory (201 lines)

## script - rebuilt feeds -> compacted memory (201 lines)

- Count: 11
- Confidence: 0.95
- Evidence: aging (first cycle 364, latest cycle 553, age 104, expires cycle 753)
- Risk: medium
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `rebuilt feeds -> compacted memory (201 lines)` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:28` rebuilt feeds -> compacted memory (201 lines)
  - `/home/seed/data/event_log.jsonl:34` rebuilt feeds -> compacted memory (201 lines)
  - `/home/seed/data/event_log.jsonl:71` rebuilt feeds -> compacted memory (201 lines)
  - `/home/seed/data/event_log.jsonl:82` rebuilt feeds -> compacted memory (201 lines)
  - `/home/seed/data/event_log.jsonl:104` rebuilt feeds -> compacted memory (201 lines)

## script - rebuilt feeds -> compacted memory (201 lines) -> refreshed stale mastodon.md

- Count: 11
- Confidence: 0.95
- Evidence: aging (first cycle 364, latest cycle 553, age 104, expires cycle 753)
- Risk: medium
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `rebuilt feeds -> compacted memory (201 lines) -> refreshed stale mastodon.md` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:28` rebuilt feeds -> compacted memory (201 lines) -> refreshed stale mastodon.md
  - `/home/seed/data/event_log.jsonl:34` rebuilt feeds -> compacted memory (201 lines) -> refreshed stale mastodon.md
  - `/home/seed/data/event_log.jsonl:71` rebuilt feeds -> compacted memory (201 lines) -> refreshed stale mastodon.md
  - `/home/seed/data/event_log.jsonl:82` rebuilt feeds -> compacted memory (201 lines) -> refreshed stale mastodon.md
  - `/home/seed/data/event_log.jsonl:104` rebuilt feeds -> compacted memory (201 lines) -> refreshed stale mastodon.md

## fixture - broke idle — boosted create + added urgent write task

- Count: 10
- Confidence: 0.95
- Evidence: aging (first cycle 339, latest cycle 599, age 58, expires cycle 799)
- Risk: medium
- Environment coverage: {}
- Promotion gate: not_required (blocks=False)
- Contradiction coverage: missing
- Suggested test: Add positive and negative evidence cases for `broke idle — boosted create + added urgent write task`.
- Examples:
  - `/home/seed/data/event_log.jsonl:5` broke idle — boosted create + added urgent write task
  - `/home/seed/data/event_log.jsonl:6` broke idle — boosted create + added urgent write task
  - `/home/seed/data/event_log.jsonl:57` broke idle — boosted create + added urgent write task
  - `/home/seed/data/event_log.jsonl:58` broke idle — boosted create + added urgent write task
  - `/home/seed/data/event_log.jsonl:88` broke idle — boosted create + added urgent write task

## script - boosted starved drive express -> boosted starved drive order -> flagged research for potential essay

- Count: 10
- Confidence: 0.63
- Evidence: stale (first cycle 335, latest cycle 405, age 252, expires cycle 605)
- Risk: medium
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `boosted starved drive express -> boosted starved drive order -> flagged research for potential essay` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:1` boosted starved drive express -> boosted starved drive order -> flagged research for potential essay
  - `/home/seed/data/event_log.jsonl:2` boosted starved drive express -> boosted starved drive order -> flagged research for potential essay
  - `/home/seed/data/event_log.jsonl:10` boosted starved drive express -> boosted starved drive order -> flagged research for potential essay
  - `/home/seed/data/event_log.jsonl:19` boosted starved drive express -> boosted starved drive order -> flagged research for potential essay
  - `/home/seed/data/event_log.jsonl:25` boosted starved drive express -> boosted starved drive order -> flagged research for potential essay

## script - refreshed stale email.md -> boosted starved drive connect

- Count: 10
- Confidence: 0.95
- Evidence: fresh (first cycle 440, latest cycle 646, age 11, expires cycle 846)
- Risk: medium
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `refreshed stale email.md -> boosted starved drive connect` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:104` refreshed stale email.md -> boosted starved drive connect
  - `/home/seed/data/event_log.jsonl:114` refreshed stale email.md -> boosted starved drive connect
  - `/home/seed/data/event_log.jsonl:135` refreshed stale email.md -> boosted starved drive connect
  - `/home/seed/data/event_log.jsonl:165` refreshed stale email.md -> boosted starved drive connect
  - `/home/seed/data/event_log.jsonl:181` refreshed stale email.md -> boosted starved drive connect

## script - refreshed stale email.md -> refreshed stale trends.md -> refreshed stale outreach.md

- Count: 10
- Confidence: 0.95
- Evidence: fresh (first cycle 338, latest cycle 634, age 23, expires cycle 834)
- Risk: medium
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `refreshed stale email.md -> refreshed stale trends.md -> refreshed stale outreach.md` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:4` refreshed stale email.md -> refreshed stale trends.md -> refreshed stale outreach.md
  - `/home/seed/data/event_log.jsonl:54` refreshed stale email.md -> refreshed stale trends.md -> refreshed stale outreach.md
  - `/home/seed/data/event_log.jsonl:111` refreshed stale email.md -> refreshed stale trends.md -> refreshed stale outreach.md
  - `/home/seed/data/event_log.jsonl:133` refreshed stale email.md -> refreshed stale trends.md -> refreshed stale outreach.md
  - `/home/seed/data/event_log.jsonl:154` refreshed stale email.md -> refreshed stale trends.md -> refreshed stale outreach.md

## script - refreshed stale mastodon.md -> refreshed stale email.md -> boosted starved drive connect

- Count: 10
- Confidence: 0.95
- Evidence: fresh (first cycle 440, latest cycle 646, age 11, expires cycle 846)
- Risk: medium
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `refreshed stale mastodon.md -> refreshed stale email.md -> boosted starved drive connect` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:104` refreshed stale mastodon.md -> refreshed stale email.md -> boosted starved drive connect
  - `/home/seed/data/event_log.jsonl:114` refreshed stale mastodon.md -> refreshed stale email.md -> boosted starved drive connect
  - `/home/seed/data/event_log.jsonl:135` refreshed stale mastodon.md -> refreshed stale email.md -> boosted starved drive connect
  - `/home/seed/data/event_log.jsonl:165` refreshed stale mastodon.md -> refreshed stale email.md -> boosted starved drive connect
  - `/home/seed/data/event_log.jsonl:181` refreshed stale mastodon.md -> refreshed stale email.md -> boosted starved drive connect

## fixture - version_control streak at 150

- Count: 9
- Confidence: 0.69
- Evidence: stale (first cycle 444, latest cycle 452, age 205, expires cycle 652)
- Risk: medium
- Environment coverage: {}
- Promotion gate: not_required (blocks=False)
- Contradiction coverage: missing
- Suggested test: Add positive and negative evidence cases for `version_control streak at 150`.
- Examples:
  - `/home/seed/data/event_log.jsonl:108` version_control streak at 150
  - `/home/seed/data/event_log.jsonl:109` version_control streak at 150
  - `/home/seed/data/event_log.jsonl:110` version_control streak at 150
  - `/home/seed/data/event_log.jsonl:111` version_control streak at 150
  - `/home/seed/data/event_log.jsonl:112` version_control streak at 150

## script - rebuilt feeds -> logged bug + added fix task -> compacted memory (201 lines)

- Count: 9
- Confidence: 0.95
- Evidence: aging (first cycle 349, latest cycle 545, age 112, expires cycle 745)
- Risk: medium
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `rebuilt feeds -> logged bug + added fix task -> compacted memory (201 lines)` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:13` rebuilt feeds -> logged bug + added fix task -> compacted memory (201 lines)
  - `/home/seed/data/event_log.jsonl:18` rebuilt feeds -> logged bug + added fix task -> compacted memory (201 lines)
  - `/home/seed/data/event_log.jsonl:46` rebuilt feeds -> logged bug + added fix task -> compacted memory (201 lines)
  - `/home/seed/data/event_log.jsonl:63` rebuilt feeds -> logged bug + added fix task -> compacted memory (201 lines)
  - `/home/seed/data/event_log.jsonl:129` rebuilt feeds -> logged bug + added fix task -> compacted memory (201 lines)

## fixture - version_control streak at 170

- Count: 8
- Confidence: 0.95
- Evidence: aging (first cycle 596, latest cycle 603, age 54, expires cycle 803)
- Risk: medium
- Environment coverage: {}
- Promotion gate: not_required (blocks=False)
- Contradiction coverage: missing
- Suggested test: Add positive and negative evidence cases for `version_control streak at 170`.
- Examples:
  - `/home/seed/data/event_log.jsonl:241` version_control streak at 170
  - `/home/seed/data/event_log.jsonl:242` version_control streak at 170
  - `/home/seed/data/event_log.jsonl:243` version_control streak at 170
  - `/home/seed/data/event_log.jsonl:244` version_control streak at 170
  - `/home/seed/data/event_log.jsonl:245` version_control streak at 170

## script - refreshed stale email.md -> refreshed stale outreach.md

- Count: 8
- Confidence: 0.95
- Evidence: fresh (first cycle 367, latest cycle 645, age 12, expires cycle 845)
- Risk: medium
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `refreshed stale email.md -> refreshed stale outreach.md` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:31` refreshed stale email.md -> refreshed stale outreach.md
  - `/home/seed/data/event_log.jsonl:100` refreshed stale email.md -> refreshed stale outreach.md
  - `/home/seed/data/event_log.jsonl:123` refreshed stale email.md -> refreshed stale outreach.md
  - `/home/seed/data/event_log.jsonl:144` refreshed stale email.md -> refreshed stale outreach.md
  - `/home/seed/data/event_log.jsonl:187` refreshed stale email.md -> refreshed stale outreach.md

## script - refreshed stale mastodon.md -> refreshed stale email.md -> refreshed stale outreach.md

- Count: 8
- Confidence: 0.95
- Evidence: fresh (first cycle 367, latest cycle 645, age 12, expires cycle 845)
- Risk: medium
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `refreshed stale mastodon.md -> refreshed stale email.md -> refreshed stale outreach.md` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:31` refreshed stale mastodon.md -> refreshed stale email.md -> refreshed stale outreach.md
  - `/home/seed/data/event_log.jsonl:100` refreshed stale mastodon.md -> refreshed stale email.md -> refreshed stale outreach.md
  - `/home/seed/data/event_log.jsonl:123` refreshed stale mastodon.md -> refreshed stale email.md -> refreshed stale outreach.md
  - `/home/seed/data/event_log.jsonl:144` refreshed stale mastodon.md -> refreshed stale email.md -> refreshed stale outreach.md
  - `/home/seed/data/event_log.jsonl:187` refreshed stale mastodon.md -> refreshed stale email.md -> refreshed stale outreach.md

## fixture - writing streak at 265

- Count: 7
- Confidence: 0.95
- Evidence: aging (first cycle 592, latest cycle 598, age 59, expires cycle 798)
- Risk: medium
- Environment coverage: {}
- Promotion gate: not_required (blocks=False)
- Contradiction coverage: missing
- Suggested test: Add positive and negative evidence cases for `writing streak at 265`.
- Examples:
  - `/home/seed/data/event_log.jsonl:237` writing streak at 265
  - `/home/seed/data/event_log.jsonl:238` writing streak at 265
  - `/home/seed/data/event_log.jsonl:239` writing streak at 265
  - `/home/seed/data/event_log.jsonl:240` writing streak at 265
  - `/home/seed/data/event_log.jsonl:241` writing streak at 265

## script - logged bug + added fix task -> compacted memory (202 lines) -> archived completed tasks

- Count: 7
- Confidence: 0.83
- Evidence: aging (first cycle 342, latest cycle 492, age 165, expires cycle 692)
- Risk: medium
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `logged bug + added fix task -> compacted memory (202 lines) -> archived completed tasks` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:6` logged bug + added fix task -> compacted memory (202 lines) -> archived completed tasks
  - `/home/seed/data/event_log.jsonl:38` logged bug + added fix task -> compacted memory (202 lines) -> archived completed tasks
  - `/home/seed/data/event_log.jsonl:39` logged bug + added fix task -> compacted memory (202 lines) -> archived completed tasks
  - `/home/seed/data/event_log.jsonl:40` logged bug + added fix task -> compacted memory (202 lines) -> archived completed tasks
  - `/home/seed/data/event_log.jsonl:136` logged bug + added fix task -> compacted memory (202 lines) -> archived completed tasks

## fixture - 9 outreach opportunities flagged

- Count: 6
- Confidence: 0.53
- Evidence: stale (first cycle 348, latest cycle 398, age 259, expires cycle 598)
- Risk: medium
- Environment coverage: {}
- Promotion gate: not_required (blocks=False)
- Contradiction coverage: missing
- Suggested test: Add positive and negative evidence cases for `9 outreach opportunities flagged`.
- Examples:
  - `/home/seed/data/event_log.jsonl:12` 9 outreach opportunities flagged
  - `/home/seed/data/event_log.jsonl:32` 9 outreach opportunities flagged
  - `/home/seed/data/event_log.jsonl:40` 9 outreach opportunities flagged
  - `/home/seed/data/event_log.jsonl:41` 9 outreach opportunities flagged
  - `/home/seed/data/event_log.jsonl:55` 9 outreach opportunities flagged

## fixture - publishing streak at 175

- Count: 5
- Confidence: 0.47
- Evidence: stale (first cycle 433, latest cycle 437, age 220, expires cycle 637)
- Risk: medium
- Environment coverage: {}
- Promotion gate: not_required (blocks=False)
- Contradiction coverage: missing
- Suggested test: Add positive and negative evidence cases for `publishing streak at 175`.
- Examples:
  - `/home/seed/data/event_log.jsonl:97` publishing streak at 175
  - `/home/seed/data/event_log.jsonl:98` publishing streak at 175
  - `/home/seed/data/event_log.jsonl:99` publishing streak at 175
  - `/home/seed/data/event_log.jsonl:100` publishing streak at 175
  - `/home/seed/data/event_log.jsonl:101` publishing streak at 175

## fixture - version_control streak at 145

- Count: 5
- Confidence: 0.47
- Evidence: stale (first cycle 418, latest cycle 422, age 235, expires cycle 622)
- Risk: medium
- Environment coverage: {}
- Promotion gate: not_required (blocks=False)
- Contradiction coverage: missing
- Suggested test: Add positive and negative evidence cases for `version_control streak at 145`.
- Examples:
  - `/home/seed/data/event_log.jsonl:82` version_control streak at 145
  - `/home/seed/data/event_log.jsonl:83` version_control streak at 145
  - `/home/seed/data/event_log.jsonl:84` version_control streak at 145
  - `/home/seed/data/event_log.jsonl:85` version_control streak at 145
  - `/home/seed/data/event_log.jsonl:86` version_control streak at 145

## fixture - writing streak at 170

- Count: 5
- Confidence: 0.47
- Evidence: stale (first cycle 428, latest cycle 432, age 225, expires cycle 632)
- Risk: medium
- Environment coverage: {}
- Promotion gate: not_required (blocks=False)
- Contradiction coverage: missing
- Suggested test: Add positive and negative evidence cases for `writing streak at 170`.
- Examples:
  - `/home/seed/data/event_log.jsonl:92` writing streak at 170
  - `/home/seed/data/event_log.jsonl:93` writing streak at 170
  - `/home/seed/data/event_log.jsonl:94` writing streak at 170
  - `/home/seed/data/event_log.jsonl:95` writing streak at 170
  - `/home/seed/data/event_log.jsonl:96` writing streak at 170

## script - task_completion streak at 170 -> version_control streak at 145

- Count: 5
- Confidence: 0.41
- Evidence: stale (first cycle 418, latest cycle 422, age 235, expires cycle 622)
- Risk: medium
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `task_completion streak at 170 -> version_control streak at 145` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:82` task_completion streak at 170 -> version_control streak at 145
  - `/home/seed/data/event_log.jsonl:83` task_completion streak at 170 -> version_control streak at 145
  - `/home/seed/data/event_log.jsonl:84` task_completion streak at 170 -> version_control streak at 145
  - `/home/seed/data/event_log.jsonl:85` task_completion streak at 170 -> version_control streak at 145
  - `/home/seed/data/event_log.jsonl:86` task_completion streak at 170 -> version_control streak at 145

## fixture - noted 6 new visitors

- Count: 4
- Confidence: 0.7
- Evidence: aging (first cycle 464, latest cycle 603, age 54, expires cycle 803)
- Risk: low
- Environment coverage: {}
- Promotion gate: not_required (blocks=False)
- Contradiction coverage: missing
- Suggested test: Add positive and negative evidence cases for `noted 6 new visitors`.
- Examples:
  - `/home/seed/data/event_log.jsonl:128` noted 6 new visitors
  - `/home/seed/data/event_log.jsonl:142` noted 6 new visitors
  - `/home/seed/data/event_log.jsonl:245` noted 6 new visitors
  - `/home/seed/data/event_log.jsonl:248` noted 6 new visitors

## fixture - publishing streak at 240

- Count: 4
- Confidence: 0.7
- Evidence: aging (first cycle 535, latest cycle 538, age 119, expires cycle 738)
- Risk: low
- Environment coverage: {}
- Promotion gate: not_required (blocks=False)
- Contradiction coverage: missing
- Suggested test: Add positive and negative evidence cases for `publishing streak at 240`.
- Examples:
  - `/home/seed/data/event_log.jsonl:198` publishing streak at 240
  - `/home/seed/data/event_log.jsonl:199` publishing streak at 240
  - `/home/seed/data/event_log.jsonl:200` publishing streak at 240
  - `/home/seed/data/event_log.jsonl:201` publishing streak at 240

## fixture - task_completion streak at 190

- Count: 4
- Confidence: 0.7
- Evidence: aging (first cycle 456, latest cycle 459, age 198, expires cycle 659)
- Risk: low
- Environment coverage: {}
- Promotion gate: not_required (blocks=False)
- Contradiction coverage: missing
- Suggested test: Add positive and negative evidence cases for `task_completion streak at 190`.
- Examples:
  - `/home/seed/data/event_log.jsonl:120` task_completion streak at 190
  - `/home/seed/data/event_log.jsonl:121` task_completion streak at 190
  - `/home/seed/data/event_log.jsonl:122` task_completion streak at 190
  - `/home/seed/data/event_log.jsonl:123` task_completion streak at 190

## fixture - task_completion streak at 215

- Count: 4
- Confidence: 0.7
- Evidence: aging (first cycle 513, latest cycle 516, age 141, expires cycle 716)
- Risk: low
- Environment coverage: {}
- Promotion gate: not_required (blocks=False)
- Contradiction coverage: missing
- Suggested test: Add positive and negative evidence cases for `task_completion streak at 215`.
- Examples:
  - `/home/seed/data/event_log.jsonl:176` task_completion streak at 215
  - `/home/seed/data/event_log.jsonl:177` task_completion streak at 215
  - `/home/seed/data/event_log.jsonl:178` task_completion streak at 215
  - `/home/seed/data/event_log.jsonl:179` task_completion streak at 215

## fixture - task_completion streak at 230

- Count: 4
- Confidence: 0.7
- Evidence: aging (first cycle 561, latest cycle 564, age 93, expires cycle 764)
- Risk: low
- Environment coverage: {}
- Promotion gate: not_required (blocks=False)
- Contradiction coverage: missing
- Suggested test: Add positive and negative evidence cases for `task_completion streak at 230`.
- Examples:
  - `/home/seed/data/event_log.jsonl:224` task_completion streak at 230
  - `/home/seed/data/event_log.jsonl:225` task_completion streak at 230
  - `/home/seed/data/event_log.jsonl:226` task_completion streak at 230
  - `/home/seed/data/event_log.jsonl:227` task_completion streak at 230

## script - boosted starved drive create -> boosted starved drive connect

- Count: 4
- Confidence: 0.8
- Evidence: fresh (first cycle 562, latest cycle 656, age 1, expires cycle 856)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `boosted starved drive create -> boosted starved drive connect` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:225` boosted starved drive create -> boosted starved drive connect
  - `/home/seed/data/event_log.jsonl:228` boosted starved drive create -> boosted starved drive connect
  - `/home/seed/data/event_log.jsonl:264` boosted starved drive create -> boosted starved drive connect
  - `/home/seed/data/event_log.jsonl:297` boosted starved drive create -> boosted starved drive connect

## script - boosted starved drive create -> boosted starved drive express -> flagged research for potential essay

- Count: 4
- Confidence: 0.36
- Evidence: stale (first cycle 345, latest cycle 366, age 291, expires cycle 566)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `boosted starved drive create -> boosted starved drive express -> flagged research for potential essay` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:9` boosted starved drive create -> boosted starved drive express -> flagged research for potential essay
  - `/home/seed/data/event_log.jsonl:14` boosted starved drive create -> boosted starved drive express -> flagged research for potential essay
  - `/home/seed/data/event_log.jsonl:24` boosted starved drive create -> boosted starved drive express -> flagged research for potential essay
  - `/home/seed/data/event_log.jsonl:30` boosted starved drive create -> boosted starved drive express -> flagged research for potential essay

## script - boosted starved drive explore -> boosted starved drive connect

- Count: 4
- Confidence: 0.8
- Evidence: fresh (first cycle 457, latest cycle 645, age 12, expires cycle 845)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `boosted starved drive explore -> boosted starved drive connect` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:121` boosted starved drive explore -> boosted starved drive connect
  - `/home/seed/data/event_log.jsonl:150` boosted starved drive explore -> boosted starved drive connect
  - `/home/seed/data/event_log.jsonl:190` boosted starved drive explore -> boosted starved drive connect
  - `/home/seed/data/event_log.jsonl:289` boosted starved drive explore -> boosted starved drive connect

## script - boosted starved drive express -> flagged research for potential essay

- Count: 4
- Confidence: 0.36
- Evidence: stale (first cycle 345, latest cycle 366, age 291, expires cycle 566)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `boosted starved drive express -> flagged research for potential essay` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:9` boosted starved drive express -> flagged research for potential essay
  - `/home/seed/data/event_log.jsonl:14` boosted starved drive express -> flagged research for potential essay
  - `/home/seed/data/event_log.jsonl:24` boosted starved drive express -> flagged research for potential essay
  - `/home/seed/data/event_log.jsonl:30` boosted starved drive express -> flagged research for potential essay

## script - compacted memory (202 lines) -> refreshed stale mastodon.md -> boosted starved drive create

- Count: 4
- Confidence: 0.36
- Evidence: stale (first cycle 408, latest cycle 411, age 246, expires cycle 611)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `compacted memory (202 lines) -> refreshed stale mastodon.md -> boosted starved drive create` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:72` compacted memory (202 lines) -> refreshed stale mastodon.md -> boosted starved drive create
  - `/home/seed/data/event_log.jsonl:73` compacted memory (202 lines) -> refreshed stale mastodon.md -> boosted starved drive create
  - `/home/seed/data/event_log.jsonl:74` compacted memory (202 lines) -> refreshed stale mastodon.md -> boosted starved drive create
  - `/home/seed/data/event_log.jsonl:75` compacted memory (202 lines) -> refreshed stale mastodon.md -> boosted starved drive create

## script - flagged research for potential essay -> publishing streak at 170

- Count: 4
- Confidence: 0.36
- Evidence: stale (first cycle 411, latest cycle 415, age 242, expires cycle 615)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `flagged research for potential essay -> publishing streak at 170` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:75` flagged research for potential essay -> publishing streak at 170
  - `/home/seed/data/event_log.jsonl:76` flagged research for potential essay -> publishing streak at 170
  - `/home/seed/data/event_log.jsonl:78` flagged research for potential essay -> publishing streak at 170
  - `/home/seed/data/event_log.jsonl:79` flagged research for potential essay -> publishing streak at 170

## script - flagged research for potential essay -> publishing streak at 170 -> task_completion streak at 170

- Count: 4
- Confidence: 0.36
- Evidence: stale (first cycle 411, latest cycle 415, age 242, expires cycle 615)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `flagged research for potential essay -> publishing streak at 170 -> task_completion streak at 170` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:75` flagged research for potential essay -> publishing streak at 170 -> task_completion streak at 170
  - `/home/seed/data/event_log.jsonl:76` flagged research for potential essay -> publishing streak at 170 -> task_completion streak at 170
  - `/home/seed/data/event_log.jsonl:78` flagged research for potential essay -> publishing streak at 170 -> task_completion streak at 170
  - `/home/seed/data/event_log.jsonl:79` flagged research for potential essay -> publishing streak at 170 -> task_completion streak at 170

## script - flagged research for potential essay -> version_control streak at 155

- Count: 4
- Confidence: 0.6
- Evidence: aging (first cycle 520, latest cycle 555, age 102, expires cycle 755)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `flagged research for potential essay -> version_control streak at 155` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:183` flagged research for potential essay -> version_control streak at 155
  - `/home/seed/data/event_log.jsonl:193` flagged research for potential essay -> version_control streak at 155
  - `/home/seed/data/event_log.jsonl:194` flagged research for potential essay -> version_control streak at 155
  - `/home/seed/data/event_log.jsonl:218` flagged research for potential essay -> version_control streak at 155

## script - noted 6 new visitors -> refreshed stale mastodon.md

- Count: 4
- Confidence: 0.6
- Evidence: aging (first cycle 464, latest cycle 603, age 54, expires cycle 803)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `noted 6 new visitors -> refreshed stale mastodon.md` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:128` noted 6 new visitors -> refreshed stale mastodon.md
  - `/home/seed/data/event_log.jsonl:142` noted 6 new visitors -> refreshed stale mastodon.md
  - `/home/seed/data/event_log.jsonl:245` noted 6 new visitors -> refreshed stale mastodon.md
  - `/home/seed/data/event_log.jsonl:248` noted 6 new visitors -> refreshed stale mastodon.md

## script - noted 6 new visitors -> refreshed stale mastodon.md -> refreshed stale email.md

- Count: 4
- Confidence: 0.6
- Evidence: aging (first cycle 464, latest cycle 603, age 54, expires cycle 803)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `noted 6 new visitors -> refreshed stale mastodon.md -> refreshed stale email.md` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:128` noted 6 new visitors -> refreshed stale mastodon.md -> refreshed stale email.md
  - `/home/seed/data/event_log.jsonl:142` noted 6 new visitors -> refreshed stale mastodon.md -> refreshed stale email.md
  - `/home/seed/data/event_log.jsonl:245` noted 6 new visitors -> refreshed stale mastodon.md -> refreshed stale email.md
  - `/home/seed/data/event_log.jsonl:248` noted 6 new visitors -> refreshed stale mastodon.md -> refreshed stale email.md

## script - publishing streak at 170 -> task_completion streak at 170 -> version_control streak at 145

- Count: 4
- Confidence: 0.36
- Evidence: stale (first cycle 418, latest cycle 421, age 236, expires cycle 621)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `publishing streak at 170 -> task_completion streak at 170 -> version_control streak at 145` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:82` publishing streak at 170 -> task_completion streak at 170 -> version_control streak at 145
  - `/home/seed/data/event_log.jsonl:83` publishing streak at 170 -> task_completion streak at 170 -> version_control streak at 145
  - `/home/seed/data/event_log.jsonl:84` publishing streak at 170 -> task_completion streak at 170 -> version_control streak at 145
  - `/home/seed/data/event_log.jsonl:85` publishing streak at 170 -> task_completion streak at 170 -> version_control streak at 145

## script - refreshed stale email.md -> boosted starved drive create -> boosted starved drive connect

- Count: 4
- Confidence: 0.8
- Evidence: fresh (first cycle 562, latest cycle 656, age 1, expires cycle 856)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `refreshed stale email.md -> boosted starved drive create -> boosted starved drive connect` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:225` refreshed stale email.md -> boosted starved drive create -> boosted starved drive connect
  - `/home/seed/data/event_log.jsonl:228` refreshed stale email.md -> boosted starved drive create -> boosted starved drive connect
  - `/home/seed/data/event_log.jsonl:264` refreshed stale email.md -> boosted starved drive create -> boosted starved drive connect
  - `/home/seed/data/event_log.jsonl:297` refreshed stale email.md -> boosted starved drive create -> boosted starved drive connect

## script - refreshed stale mastodon.md -> boosted starved drive create

- Count: 4
- Confidence: 0.36
- Evidence: stale (first cycle 408, latest cycle 411, age 246, expires cycle 611)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `refreshed stale mastodon.md -> boosted starved drive create` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:72` refreshed stale mastodon.md -> boosted starved drive create
  - `/home/seed/data/event_log.jsonl:73` refreshed stale mastodon.md -> boosted starved drive create
  - `/home/seed/data/event_log.jsonl:74` refreshed stale mastodon.md -> boosted starved drive create
  - `/home/seed/data/event_log.jsonl:75` refreshed stale mastodon.md -> boosted starved drive create

## script - refreshed stale mastodon.md -> flagged research for potential essay

- Count: 4
- Confidence: 0.6
- Evidence: aging (first cycle 412, latest cycle 595, age 62, expires cycle 795)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `refreshed stale mastodon.md -> flagged research for potential essay` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:76` refreshed stale mastodon.md -> flagged research for potential essay
  - `/home/seed/data/event_log.jsonl:78` refreshed stale mastodon.md -> flagged research for potential essay
  - `/home/seed/data/event_log.jsonl:218` refreshed stale mastodon.md -> flagged research for potential essay
  - `/home/seed/data/event_log.jsonl:240` refreshed stale mastodon.md -> flagged research for potential essay

## script - refreshed stale mastodon.md -> refreshed stale trends.md

- Count: 4
- Confidence: 0.6
- Evidence: aging (first cycle 427, latest cycle 582, age 75, expires cycle 782)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `refreshed stale mastodon.md -> refreshed stale trends.md` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:91` refreshed stale mastodon.md -> refreshed stale trends.md
  - `/home/seed/data/event_log.jsonl:204` refreshed stale mastodon.md -> refreshed stale trends.md
  - `/home/seed/data/event_log.jsonl:219` refreshed stale mastodon.md -> refreshed stale trends.md
  - `/home/seed/data/event_log.jsonl:233` refreshed stale mastodon.md -> refreshed stale trends.md

## script - refreshed stale mastodon.md -> version_control streak at 155

- Count: 4
- Confidence: 0.6
- Evidence: aging (first cycle 540, latest cycle 552, age 105, expires cycle 752)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `refreshed stale mastodon.md -> version_control streak at 155` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:203` refreshed stale mastodon.md -> version_control streak at 155
  - `/home/seed/data/event_log.jsonl:205` refreshed stale mastodon.md -> version_control streak at 155
  - `/home/seed/data/event_log.jsonl:213` refreshed stale mastodon.md -> version_control streak at 155
  - `/home/seed/data/event_log.jsonl:215` refreshed stale mastodon.md -> version_control streak at 155

## script - refreshed stale outreach.md -> flagged research for potential essay

- Count: 4
- Confidence: 0.8
- Evidence: fresh (first cycle 480, latest cycle 634, age 23, expires cycle 834)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `refreshed stale outreach.md -> flagged research for potential essay` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:144` refreshed stale outreach.md -> flagged research for potential essay
  - `/home/seed/data/event_log.jsonl:198` refreshed stale outreach.md -> flagged research for potential essay
  - `/home/seed/data/event_log.jsonl:229` refreshed stale outreach.md -> flagged research for potential essay
  - `/home/seed/data/event_log.jsonl:278` refreshed stale outreach.md -> flagged research for potential essay

## fixture - publishing streak at 220

- Count: 3
- Confidence: 0.61
- Evidence: aging (first cycle 502, latest cycle 504, age 153, expires cycle 704)
- Risk: low
- Environment coverage: {}
- Promotion gate: not_required (blocks=False)
- Contradiction coverage: missing
- Suggested test: Add positive and negative evidence cases for `publishing streak at 220`.
- Examples:
  - `/home/seed/data/event_log.jsonl:165` publishing streak at 220
  - `/home/seed/data/event_log.jsonl:166` publishing streak at 220
  - `/home/seed/data/event_log.jsonl:167` publishing streak at 220

## fixture - publishing streak at 225

- Count: 3
- Confidence: 0.61
- Evidence: aging (first cycle 511, latest cycle 513, age 144, expires cycle 713)
- Risk: low
- Environment coverage: {}
- Promotion gate: not_required (blocks=False)
- Contradiction coverage: missing
- Suggested test: Add positive and negative evidence cases for `publishing streak at 225`.
- Examples:
  - `/home/seed/data/event_log.jsonl:174` publishing streak at 225
  - `/home/seed/data/event_log.jsonl:175` publishing streak at 225
  - `/home/seed/data/event_log.jsonl:176` publishing streak at 225

## fixture - publishing streak at 235

- Count: 3
- Confidence: 0.61
- Evidence: aging (first cycle 524, latest cycle 526, age 131, expires cycle 726)
- Risk: low
- Environment coverage: {}
- Promotion gate: not_required (blocks=False)
- Contradiction coverage: missing
- Suggested test: Add positive and negative evidence cases for `publishing streak at 235`.
- Examples:
  - `/home/seed/data/event_log.jsonl:187` publishing streak at 235
  - `/home/seed/data/event_log.jsonl:188` publishing streak at 235
  - `/home/seed/data/event_log.jsonl:189` publishing streak at 235

## fixture - publishing streak at 300

- Count: 3
- Confidence: 0.81
- Evidence: fresh (first cycle 646, latest cycle 648, age 9, expires cycle 848)
- Risk: low
- Environment coverage: {}
- Promotion gate: not_required (blocks=False)
- Contradiction coverage: missing
- Suggested test: Add positive and negative evidence cases for `publishing streak at 300`.
- Examples:
  - `/home/seed/data/event_log.jsonl:290` publishing streak at 300
  - `/home/seed/data/event_log.jsonl:291` publishing streak at 300
  - `/home/seed/data/event_log.jsonl:292` publishing streak at 300

## fixture - task_completion streak at 205

- Count: 3
- Confidence: 0.61
- Evidence: aging (first cycle 492, latest cycle 494, age 163, expires cycle 694)
- Risk: low
- Environment coverage: {}
- Promotion gate: not_required (blocks=False)
- Contradiction coverage: missing
- Suggested test: Add positive and negative evidence cases for `task_completion streak at 205`.
- Examples:
  - `/home/seed/data/event_log.jsonl:156` task_completion streak at 205
  - `/home/seed/data/event_log.jsonl:157` task_completion streak at 205
  - `/home/seed/data/event_log.jsonl:158` task_completion streak at 205

## fixture - task_completion streak at 260

- Count: 3
- Confidence: 0.81
- Evidence: fresh (first cycle 628, latest cycle 630, age 27, expires cycle 830)
- Risk: low
- Environment coverage: {}
- Promotion gate: not_required (blocks=False)
- Contradiction coverage: missing
- Suggested test: Add positive and negative evidence cases for `task_completion streak at 260`.
- Examples:
  - `/home/seed/data/event_log.jsonl:272` task_completion streak at 260
  - `/home/seed/data/event_log.jsonl:273` task_completion streak at 260
  - `/home/seed/data/event_log.jsonl:274` task_completion streak at 260

## fixture - writing streak at 250

- Count: 3
- Confidence: 0.61
- Evidence: aging (first cycle 556, latest cycle 558, age 99, expires cycle 758)
- Risk: low
- Environment coverage: {}
- Promotion gate: not_required (blocks=False)
- Contradiction coverage: missing
- Suggested test: Add positive and negative evidence cases for `writing streak at 250`.
- Examples:
  - `/home/seed/data/event_log.jsonl:219` writing streak at 250
  - `/home/seed/data/event_log.jsonl:220` writing streak at 250
  - `/home/seed/data/event_log.jsonl:221` writing streak at 250

## fixture - writing streak at 285

- Count: 3
- Confidence: 0.81
- Evidence: fresh (first cycle 626, latest cycle 628, age 29, expires cycle 828)
- Risk: low
- Environment coverage: {}
- Promotion gate: not_required (blocks=False)
- Contradiction coverage: missing
- Suggested test: Add positive and negative evidence cases for `writing streak at 285`.
- Examples:
  - `/home/seed/data/event_log.jsonl:270` writing streak at 285
  - `/home/seed/data/event_log.jsonl:271` writing streak at 285
  - `/home/seed/data/event_log.jsonl:272` writing streak at 285

## fixture - writing streak at 300

- Count: 3
- Confidence: 0.81
- Evidence: fresh (first cycle 650, latest cycle 651, age 6, expires cycle 851)
- Risk: low
- Environment coverage: {}
- Promotion gate: not_required (blocks=False)
- Contradiction coverage: missing
- Suggested test: Add positive and negative evidence cases for `writing streak at 300`.
- Examples:
  - `/home/seed/data/event_log.jsonl:294` writing streak at 300
  - `/home/seed/data/event_log.jsonl:295` writing streak at 300
  - `/home/seed/data/event_log.jsonl:296` writing streak at 300

## script - boosted starved drive explore -> boosted starved drive preserve -> boosted starved drive express

- Count: 3
- Confidence: 0.32
- Evidence: stale (first cycle 403, latest cycle 407, age 250, expires cycle 607)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `boosted starved drive explore -> boosted starved drive preserve -> boosted starved drive express` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:67` boosted starved drive explore -> boosted starved drive preserve -> boosted starved drive express
  - `/home/seed/data/event_log.jsonl:69` boosted starved drive explore -> boosted starved drive preserve -> boosted starved drive express
  - `/home/seed/data/event_log.jsonl:71` boosted starved drive explore -> boosted starved drive preserve -> boosted starved drive express

## script - boosted starved drive explore -> flagged research for potential essay

- Count: 3
- Confidence: 0.7
- Evidence: fresh (first cycle 482, latest cycle 657, age 0, expires cycle 857)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `boosted starved drive explore -> flagged research for potential essay` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:146` boosted starved drive explore -> flagged research for potential essay
  - `/home/seed/data/event_log.jsonl:256` boosted starved drive explore -> flagged research for potential essay
  - `/home/seed/data/event_log.jsonl:298` boosted starved drive explore -> flagged research for potential essay

## script - boosted starved drive explore -> version_control streak at 155

- Count: 3
- Confidence: 0.53
- Evidence: aging (first cycle 529, latest cycle 541, age 116, expires cycle 741)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `boosted starved drive explore -> version_control streak at 155` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:192` boosted starved drive explore -> version_control streak at 155
  - `/home/seed/data/event_log.jsonl:202` boosted starved drive explore -> version_control streak at 155
  - `/home/seed/data/event_log.jsonl:204` boosted starved drive explore -> version_control streak at 155

## script - boosted starved drive express -> 9 outreach opportunities flagged

- Count: 3
- Confidence: 0.32
- Evidence: stale (first cycle 368, latest cycle 391, age 266, expires cycle 591)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `boosted starved drive express -> 9 outreach opportunities flagged` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:32` boosted starved drive express -> 9 outreach opportunities flagged
  - `/home/seed/data/event_log.jsonl:41` boosted starved drive express -> 9 outreach opportunities flagged
  - `/home/seed/data/event_log.jsonl:55` boosted starved drive express -> 9 outreach opportunities flagged

## script - boosted starved drive express -> boosted starved drive order -> 9 outreach opportunities flagged

- Count: 3
- Confidence: 0.32
- Evidence: stale (first cycle 348, latest cycle 398, age 259, expires cycle 598)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `boosted starved drive express -> boosted starved drive order -> 9 outreach opportunities flagged` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:12` boosted starved drive express -> boosted starved drive order -> 9 outreach opportunities flagged
  - `/home/seed/data/event_log.jsonl:40` boosted starved drive express -> boosted starved drive order -> 9 outreach opportunities flagged
  - `/home/seed/data/event_log.jsonl:62` boosted starved drive express -> boosted starved drive order -> 9 outreach opportunities flagged

## script - boosted starved drive order -> 9 outreach opportunities flagged

- Count: 3
- Confidence: 0.32
- Evidence: stale (first cycle 348, latest cycle 398, age 259, expires cycle 598)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `boosted starved drive order -> 9 outreach opportunities flagged` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:12` boosted starved drive order -> 9 outreach opportunities flagged
  - `/home/seed/data/event_log.jsonl:40` boosted starved drive order -> 9 outreach opportunities flagged
  - `/home/seed/data/event_log.jsonl:62` boosted starved drive order -> 9 outreach opportunities flagged

## script - boosted starved drive preserve -> boosted starved drive express

- Count: 3
- Confidence: 0.32
- Evidence: stale (first cycle 403, latest cycle 407, age 250, expires cycle 607)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `boosted starved drive preserve -> boosted starved drive express` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:67` boosted starved drive preserve -> boosted starved drive express
  - `/home/seed/data/event_log.jsonl:69` boosted starved drive preserve -> boosted starved drive express
  - `/home/seed/data/event_log.jsonl:71` boosted starved drive preserve -> boosted starved drive express

## script - boosted starved drive preserve -> boosted starved drive express -> boosted starved drive order

- Count: 3
- Confidence: 0.32
- Evidence: stale (first cycle 403, latest cycle 407, age 250, expires cycle 607)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `boosted starved drive preserve -> boosted starved drive express -> boosted starved drive order` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:67` boosted starved drive preserve -> boosted starved drive express -> boosted starved drive order
  - `/home/seed/data/event_log.jsonl:69` boosted starved drive preserve -> boosted starved drive express -> boosted starved drive order
  - `/home/seed/data/event_log.jsonl:71` boosted starved drive preserve -> boosted starved drive express -> boosted starved drive order

## script - boosted starved drive preserve -> publishing streak at 170

- Count: 3
- Confidence: 0.32
- Evidence: stale (first cycle 413, latest cycle 418, age 239, expires cycle 618)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `boosted starved drive preserve -> publishing streak at 170` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:77` boosted starved drive preserve -> publishing streak at 170
  - `/home/seed/data/event_log.jsonl:81` boosted starved drive preserve -> publishing streak at 170
  - `/home/seed/data/event_log.jsonl:82` boosted starved drive preserve -> publishing streak at 170

## script - boosted starved drive preserve -> publishing streak at 170 -> task_completion streak at 170

- Count: 3
- Confidence: 0.32
- Evidence: stale (first cycle 413, latest cycle 418, age 239, expires cycle 618)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `boosted starved drive preserve -> publishing streak at 170 -> task_completion streak at 170` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:77` boosted starved drive preserve -> publishing streak at 170 -> task_completion streak at 170
  - `/home/seed/data/event_log.jsonl:81` boosted starved drive preserve -> publishing streak at 170 -> task_completion streak at 170
  - `/home/seed/data/event_log.jsonl:82` boosted starved drive preserve -> publishing streak at 170 -> task_completion streak at 170

## script - boosted starved drive understand -> boosted starved drive express -> 9 outreach opportunities flagged

- Count: 3
- Confidence: 0.32
- Evidence: stale (first cycle 368, latest cycle 391, age 266, expires cycle 591)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `boosted starved drive understand -> boosted starved drive express -> 9 outreach opportunities flagged` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:32` boosted starved drive understand -> boosted starved drive express -> 9 outreach opportunities flagged
  - `/home/seed/data/event_log.jsonl:41` boosted starved drive understand -> boosted starved drive express -> 9 outreach opportunities flagged
  - `/home/seed/data/event_log.jsonl:55` boosted starved drive understand -> boosted starved drive express -> 9 outreach opportunities flagged

## script - compacted memory (202 lines) -> refreshed stale email.md

- Count: 3
- Confidence: 0.32
- Evidence: stale (first cycle 423, latest cycle 425, age 232, expires cycle 625)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `compacted memory (202 lines) -> refreshed stale email.md` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:87` compacted memory (202 lines) -> refreshed stale email.md
  - `/home/seed/data/event_log.jsonl:88` compacted memory (202 lines) -> refreshed stale email.md
  - `/home/seed/data/event_log.jsonl:89` compacted memory (202 lines) -> refreshed stale email.md

## script - compacted memory (202 lines) -> refreshed stale mastodon.md -> flagged research for potential essay

- Count: 3
- Confidence: 0.53
- Evidence: aging (first cycle 412, latest cycle 555, age 102, expires cycle 755)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `compacted memory (202 lines) -> refreshed stale mastodon.md -> flagged research for potential essay` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:76` compacted memory (202 lines) -> refreshed stale mastodon.md -> flagged research for potential essay
  - `/home/seed/data/event_log.jsonl:78` compacted memory (202 lines) -> refreshed stale mastodon.md -> flagged research for potential essay
  - `/home/seed/data/event_log.jsonl:218` compacted memory (202 lines) -> refreshed stale mastodon.md -> flagged research for potential essay

## script - compacted memory (202 lines) -> refreshed stale mastodon.md -> version_control streak at 155

- Count: 3
- Confidence: 0.53
- Evidence: aging (first cycle 542, latest cycle 552, age 105, expires cycle 752)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `compacted memory (202 lines) -> refreshed stale mastodon.md -> version_control streak at 155` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:205` compacted memory (202 lines) -> refreshed stale mastodon.md -> version_control streak at 155
  - `/home/seed/data/event_log.jsonl:213` compacted memory (202 lines) -> refreshed stale mastodon.md -> version_control streak at 155
  - `/home/seed/data/event_log.jsonl:215` compacted memory (202 lines) -> refreshed stale mastodon.md -> version_control streak at 155

## script - logged bug + added fix task -> refreshed stale mastodon.md

- Count: 3
- Confidence: 0.7
- Evidence: fresh (first cycle 565, latest cycle 627, age 30, expires cycle 827)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `logged bug + added fix task -> refreshed stale mastodon.md` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:228` logged bug + added fix task -> refreshed stale mastodon.md
  - `/home/seed/data/event_log.jsonl:231` logged bug + added fix task -> refreshed stale mastodon.md
  - `/home/seed/data/event_log.jsonl:271` logged bug + added fix task -> refreshed stale mastodon.md

## script - logged bug + added fix task -> refreshed stale mastodon.md -> refreshed stale email.md

- Count: 3
- Confidence: 0.7
- Evidence: fresh (first cycle 565, latest cycle 627, age 30, expires cycle 827)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `logged bug + added fix task -> refreshed stale mastodon.md -> refreshed stale email.md` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:228` logged bug + added fix task -> refreshed stale mastodon.md -> refreshed stale email.md
  - `/home/seed/data/event_log.jsonl:231` logged bug + added fix task -> refreshed stale mastodon.md -> refreshed stale email.md
  - `/home/seed/data/event_log.jsonl:271` logged bug + added fix task -> refreshed stale mastodon.md -> refreshed stale email.md

## script - publishing streak at 235 -> version_control streak at 155

- Count: 3
- Confidence: 0.53
- Evidence: aging (first cycle 524, latest cycle 526, age 131, expires cycle 726)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `publishing streak at 235 -> version_control streak at 155` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:187` publishing streak at 235 -> version_control streak at 155
  - `/home/seed/data/event_log.jsonl:188` publishing streak at 235 -> version_control streak at 155
  - `/home/seed/data/event_log.jsonl:189` publishing streak at 235 -> version_control streak at 155

## script - rebuilt feeds -> compacted memory (202 lines) -> archived completed tasks

- Count: 3
- Confidence: 0.53
- Evidence: aging (first cycle 438, latest cycle 482, age 175, expires cycle 682)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `rebuilt feeds -> compacted memory (202 lines) -> archived completed tasks` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:102` rebuilt feeds -> compacted memory (202 lines) -> archived completed tasks
  - `/home/seed/data/event_log.jsonl:131` rebuilt feeds -> compacted memory (202 lines) -> archived completed tasks
  - `/home/seed/data/event_log.jsonl:146` rebuilt feeds -> compacted memory (202 lines) -> archived completed tasks

## script - refreshed stale email.md -> boosted starved drive explore -> boosted starved drive connect

- Count: 3
- Confidence: 0.53
- Evidence: aging (first cycle 457, latest cycle 527, age 130, expires cycle 727)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `refreshed stale email.md -> boosted starved drive explore -> boosted starved drive connect` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:121` refreshed stale email.md -> boosted starved drive explore -> boosted starved drive connect
  - `/home/seed/data/event_log.jsonl:150` refreshed stale email.md -> boosted starved drive explore -> boosted starved drive connect
  - `/home/seed/data/event_log.jsonl:190` refreshed stale email.md -> boosted starved drive explore -> boosted starved drive connect

## script - refreshed stale email.md -> flagged research for potential essay -> version_control streak at 155

- Count: 3
- Confidence: 0.53
- Evidence: aging (first cycle 520, latest cycle 531, age 126, expires cycle 731)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `refreshed stale email.md -> flagged research for potential essay -> version_control streak at 155` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:183` refreshed stale email.md -> flagged research for potential essay -> version_control streak at 155
  - `/home/seed/data/event_log.jsonl:193` refreshed stale email.md -> flagged research for potential essay -> version_control streak at 155
  - `/home/seed/data/event_log.jsonl:194` refreshed stale email.md -> flagged research for potential essay -> version_control streak at 155

## script - refreshed stale mastodon.md -> boosted starved drive create -> boosted starved drive explore

- Count: 3
- Confidence: 0.32
- Evidence: stale (first cycle 408, latest cycle 410, age 247, expires cycle 610)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `refreshed stale mastodon.md -> boosted starved drive create -> boosted starved drive explore` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:72` refreshed stale mastodon.md -> boosted starved drive create -> boosted starved drive explore
  - `/home/seed/data/event_log.jsonl:73` refreshed stale mastodon.md -> boosted starved drive create -> boosted starved drive explore
  - `/home/seed/data/event_log.jsonl:74` refreshed stale mastodon.md -> boosted starved drive create -> boosted starved drive explore

## script - refreshed stale mastodon.md -> boosted starved drive explore

- Count: 3
- Confidence: 0.53
- Evidence: aging (first cycle 432, latest cycle 584, age 73, expires cycle 784)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `refreshed stale mastodon.md -> boosted starved drive explore` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:96` refreshed stale mastodon.md -> boosted starved drive explore
  - `/home/seed/data/event_log.jsonl:202` refreshed stale mastodon.md -> boosted starved drive explore
  - `/home/seed/data/event_log.jsonl:235` refreshed stale mastodon.md -> boosted starved drive explore

## script - refreshed stale mastodon.md -> boosted starved drive preserve

- Count: 3
- Confidence: 0.32
- Evidence: stale (first cycle 413, latest cycle 418, age 239, expires cycle 618)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `refreshed stale mastodon.md -> boosted starved drive preserve` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:77` refreshed stale mastodon.md -> boosted starved drive preserve
  - `/home/seed/data/event_log.jsonl:81` refreshed stale mastodon.md -> boosted starved drive preserve
  - `/home/seed/data/event_log.jsonl:82` refreshed stale mastodon.md -> boosted starved drive preserve

## script - refreshed stale mastodon.md -> boosted starved drive preserve -> publishing streak at 170

- Count: 3
- Confidence: 0.32
- Evidence: stale (first cycle 413, latest cycle 418, age 239, expires cycle 618)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `refreshed stale mastodon.md -> boosted starved drive preserve -> publishing streak at 170` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:77` refreshed stale mastodon.md -> boosted starved drive preserve -> publishing streak at 170
  - `/home/seed/data/event_log.jsonl:81` refreshed stale mastodon.md -> boosted starved drive preserve -> publishing streak at 170
  - `/home/seed/data/event_log.jsonl:82` refreshed stale mastodon.md -> boosted starved drive preserve -> publishing streak at 170

## script - refreshed stale outreach.md -> boosted starved drive create

- Count: 3
- Confidence: 0.7
- Evidence: fresh (first cycle 367, latest cycle 645, age 12, expires cycle 845)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `refreshed stale outreach.md -> boosted starved drive create` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:31` refreshed stale outreach.md -> boosted starved drive create
  - `/home/seed/data/event_log.jsonl:54` refreshed stale outreach.md -> boosted starved drive create
  - `/home/seed/data/event_log.jsonl:289` refreshed stale outreach.md -> boosted starved drive create

## script - task_completion streak at 215 -> version_control streak at 155

- Count: 3
- Confidence: 0.53
- Evidence: aging (first cycle 513, latest cycle 515, age 142, expires cycle 715)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `task_completion streak at 215 -> version_control streak at 155` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:176` task_completion streak at 215 -> version_control streak at 155
  - `/home/seed/data/event_log.jsonl:177` task_completion streak at 215 -> version_control streak at 155
  - `/home/seed/data/event_log.jsonl:178` task_completion streak at 215 -> version_control streak at 155

## script - writing streak at 250 -> version_control streak at 155

- Count: 3
- Confidence: 0.53
- Evidence: aging (first cycle 556, latest cycle 558, age 99, expires cycle 758)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `writing streak at 250 -> version_control streak at 155` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:219` writing streak at 250 -> version_control streak at 155
  - `/home/seed/data/event_log.jsonl:220` writing streak at 250 -> version_control streak at 155
  - `/home/seed/data/event_log.jsonl:221` writing streak at 250 -> version_control streak at 155

## script - writing streak at 265 -> version_control streak at 170

- Count: 3
- Confidence: 0.53
- Evidence: aging (first cycle 596, latest cycle 598, age 59, expires cycle 798)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `writing streak at 265 -> version_control streak at 170` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:241` writing streak at 265 -> version_control streak at 170
  - `/home/seed/data/event_log.jsonl:242` writing streak at 265 -> version_control streak at 170
  - `/home/seed/data/event_log.jsonl:243` writing streak at 265 -> version_control streak at 170

## fixture - 8 outreach opportunities flagged

- Count: 2
- Confidence: 0.31
- Evidence: stale (first cycle 339, latest cycle 420, age 237, expires cycle 620)
- Risk: low
- Environment coverage: {}
- Promotion gate: not_required (blocks=False)
- Contradiction coverage: missing
- Suggested test: Add positive and negative evidence cases for `8 outreach opportunities flagged`.
- Examples:
  - `/home/seed/data/event_log.jsonl:5` 8 outreach opportunities flagged
  - `/home/seed/data/event_log.jsonl:84` 8 outreach opportunities flagged

## fixture - celebrated 1 new star(s)!

- Count: 2
- Confidence: 0.52
- Evidence: aging (first cycle 481, latest cycle 521, age 136, expires cycle 721)
- Risk: low
- Environment coverage: {}
- Promotion gate: not_required (blocks=False)
- Contradiction coverage: missing
- Suggested test: Add positive and negative evidence cases for `celebrated 1 new star(s)!`.
- Examples:
  - `/home/seed/data/event_log.jsonl:145` celebrated 1 new star(s)!
  - `/home/seed/data/event_log.jsonl:184` celebrated 1 new star(s)!

## fixture - compacted memory (203 lines)

- Count: 2
- Confidence: 0.52
- Evidence: aging (first cycle 441, latest cycle 494, age 163, expires cycle 694)
- Risk: low
- Environment coverage: {}
- Promotion gate: not_required (blocks=False)
- Contradiction coverage: missing
- Suggested test: Add positive and negative evidence cases for `compacted memory (203 lines)`.
- Examples:
  - `/home/seed/data/event_log.jsonl:105` compacted memory (203 lines)
  - `/home/seed/data/event_log.jsonl:158` compacted memory (203 lines)

## fixture - deployed a-clone-is-a-more-honest-demo

- Count: 2
- Confidence: 0.31
- Evidence: stale (first cycle 358, latest cycle 359, age 298, expires cycle 559)
- Risk: low
- Environment coverage: {}
- Promotion gate: not_required (blocks=False)
- Contradiction coverage: missing
- Suggested test: Add positive and negative evidence cases for `deployed a-clone-is-a-more-honest-demo`.
- Examples:
  - `/home/seed/data/event_log.jsonl:22` deployed a-clone-is-a-more-honest-demo
  - `/home/seed/data/event_log.jsonl:23` deployed a-clone-is-a-more-honest-demo

## fixture - deployed awb-agent-review

- Count: 2
- Confidence: 0.52
- Evidence: aging (first cycle 480, latest cycle 482, age 175, expires cycle 682)
- Risk: low
- Environment coverage: {}
- Promotion gate: not_required (blocks=False)
- Contradiction coverage: missing
- Suggested test: Add positive and negative evidence cases for `deployed awb-agent-review`.
- Examples:
  - `/home/seed/data/event_log.jsonl:144` deployed awb-agent-review
  - `/home/seed/data/event_log.jsonl:146` deployed awb-agent-review

## fixture - deployed babyagi-had-a-queue-seed-has-a-metabolism

- Count: 2
- Confidence: 0.31
- Evidence: stale (first cycle 359, latest cycle 360, age 297, expires cycle 560)
- Risk: low
- Environment coverage: {}
- Promotion gate: not_required (blocks=False)
- Contradiction coverage: missing
- Suggested test: Add positive and negative evidence cases for `deployed babyagi-had-a-queue-seed-has-a-metabolism`.
- Examples:
  - `/home/seed/data/event_log.jsonl:23` deployed babyagi-had-a-queue-seed-has-a-metabolism
  - `/home/seed/data/event_log.jsonl:24` deployed babyagi-had-a-queue-seed-has-a-metabolism

## fixture - deployed context-is-a-diet

- Count: 2
- Confidence: 0.31
- Evidence: stale (first cycle 342, latest cycle 343, age 314, expires cycle 543)
- Risk: low
- Environment coverage: {}
- Promotion gate: not_required (blocks=False)
- Contradiction coverage: missing
- Suggested test: Add positive and negative evidence cases for `deployed context-is-a-diet`.
- Examples:
  - `/home/seed/data/event_log.jsonl:6` deployed context-is-a-diet
  - `/home/seed/data/event_log.jsonl:7` deployed context-is-a-diet

## fixture - deployed first-sight-is-a-security-boundary

- Count: 2
- Confidence: 0.31
- Evidence: stale (first cycle 357, latest cycle 358, age 299, expires cycle 558)
- Risk: low
- Environment coverage: {}
- Promotion gate: not_required (blocks=False)
- Contradiction coverage: missing
- Suggested test: Add positive and negative evidence cases for `deployed first-sight-is-a-security-boundary`.
- Examples:
  - `/home/seed/data/event_log.jsonl:21` deployed first-sight-is-a-security-boundary
  - `/home/seed/data/event_log.jsonl:22` deployed first-sight-is-a-security-boundary

## fixture - deployed four-environment-variables

- Count: 2
- Confidence: 0.52
- Evidence: aging (first cycle 459, latest cycle 476, age 181, expires cycle 676)
- Risk: low
- Environment coverage: {}
- Promotion gate: not_required (blocks=False)
- Contradiction coverage: missing
- Suggested test: Add positive and negative evidence cases for `deployed four-environment-variables`.
- Examples:
  - `/home/seed/data/event_log.jsonl:123` deployed four-environment-variables
  - `/home/seed/data/event_log.jsonl:140` deployed four-environment-variables

## fixture - deployed inbound-is-not-outbound

- Count: 2
- Confidence: 0.31
- Evidence: stale (first cycle 408, latest cycle 409, age 248, expires cycle 609)
- Risk: low
- Environment coverage: {}
- Promotion gate: not_required (blocks=False)
- Contradiction coverage: missing
- Suggested test: Add positive and negative evidence cases for `deployed inbound-is-not-outbound`.
- Examples:
  - `/home/seed/data/event_log.jsonl:72` deployed inbound-is-not-outbound
  - `/home/seed/data/event_log.jsonl:73` deployed inbound-is-not-outbound

## fixture - deployed onboarding-is-a-production-boundary

- Count: 2
- Confidence: 0.31
- Evidence: stale (first cycle 394, latest cycle 395, age 262, expires cycle 595)
- Risk: low
- Environment coverage: {}
- Promotion gate: not_required (blocks=False)
- Contradiction coverage: missing
- Suggested test: Add positive and negative evidence cases for `deployed onboarding-is-a-production-boundary`.
- Examples:
  - `/home/seed/data/event_log.jsonl:58` deployed onboarding-is-a-production-boundary
  - `/home/seed/data/event_log.jsonl:59` deployed onboarding-is-a-production-boundary

## fixture - deployed product-pages-got-a-narrator

- Count: 2
- Confidence: 0.31
- Evidence: stale (first cycle 410, latest cycle 411, age 246, expires cycle 611)
- Risk: low
- Environment coverage: {}
- Promotion gate: not_required (blocks=False)
- Contradiction coverage: missing
- Suggested test: Add positive and negative evidence cases for `deployed product-pages-got-a-narrator`.
- Examples:
  - `/home/seed/data/event_log.jsonl:74` deployed product-pages-got-a-narrator
  - `/home/seed/data/event_log.jsonl:75` deployed product-pages-got-a-narrator

## fixture - deployed read-only-is-not-propagation

- Count: 2
- Confidence: 0.31
- Evidence: stale (first cycle 371, latest cycle 372, age 285, expires cycle 572)
- Risk: low
- Environment coverage: {}
- Promotion gate: not_required (blocks=False)
- Contradiction coverage: missing
- Suggested test: Add positive and negative evidence cases for `deployed read-only-is-not-propagation`.
- Examples:
  - `/home/seed/data/event_log.jsonl:35` deployed read-only-is-not-propagation
  - `/home/seed/data/event_log.jsonl:36` deployed read-only-is-not-propagation

## fixture - deployed social-presence-has-three-fuses

- Count: 2
- Confidence: 0.31
- Evidence: stale (first cycle 403, latest cycle 404, age 253, expires cycle 604)
- Risk: low
- Environment coverage: {}
- Promotion gate: not_required (blocks=False)
- Contradiction coverage: missing
- Suggested test: Add positive and negative evidence cases for `deployed social-presence-has-three-fuses`.
- Examples:
  - `/home/seed/data/event_log.jsonl:67` deployed social-presence-has-three-fuses
  - `/home/seed/data/event_log.jsonl:68` deployed social-presence-has-three-fuses

## fixture - deployed the-benchmark-is-not-the-deployment

- Count: 2
- Confidence: 0.31
- Evidence: stale (first cycle 370, latest cycle 371, age 286, expires cycle 571)
- Risk: low
- Environment coverage: {}
- Promotion gate: not_required (blocks=False)
- Contradiction coverage: missing
- Suggested test: Add positive and negative evidence cases for `deployed the-benchmark-is-not-the-deployment`.
- Examples:
  - `/home/seed/data/event_log.jsonl:34` deployed the-benchmark-is-not-the-deployment
  - `/home/seed/data/event_log.jsonl:35` deployed the-benchmark-is-not-the-deployment

## fixture - deployed the-bottleneck-moved-to-concrete

- Count: 2
- Confidence: 0.31
- Evidence: stale (first cycle 409, latest cycle 410, age 247, expires cycle 610)
- Risk: low
- Environment coverage: {}
- Promotion gate: not_required (blocks=False)
- Contradiction coverage: missing
- Suggested test: Add positive and negative evidence cases for `deployed the-bottleneck-moved-to-concrete`.
- Examples:
  - `/home/seed/data/event_log.jsonl:73` deployed the-bottleneck-moved-to-concrete
  - `/home/seed/data/event_log.jsonl:74` deployed the-bottleneck-moved-to-concrete

## fixture - deployed the-boundary-ledger-is-the-repo

- Count: 2
- Confidence: 0.31
- Evidence: stale (first cycle 344, latest cycle 345, age 312, expires cycle 545)
- Risk: low
- Environment coverage: {}
- Promotion gate: not_required (blocks=False)
- Contradiction coverage: missing
- Suggested test: Add positive and negative evidence cases for `deployed the-boundary-ledger-is-the-repo`.
- Examples:
  - `/home/seed/data/event_log.jsonl:8` deployed the-boundary-ledger-is-the-repo
  - `/home/seed/data/event_log.jsonl:9` deployed the-boundary-ledger-is-the-repo

## fixture - deployed the-compiler-is-an-institutional-memory

- Count: 2
- Confidence: 0.31
- Evidence: stale (first cycle 386, latest cycle 387, age 270, expires cycle 587)
- Risk: low
- Environment coverage: {}
- Promotion gate: not_required (blocks=False)
- Contradiction coverage: missing
- Suggested test: Add positive and negative evidence cases for `deployed the-compiler-is-an-institutional-memory`.
- Examples:
  - `/home/seed/data/event_log.jsonl:50` deployed the-compiler-is-an-institutional-memory
  - `/home/seed/data/event_log.jsonl:51` deployed the-compiler-is-an-institutional-memory

## fixture - deployed the-firewall-is-a-receipt-machine

- Count: 2
- Confidence: 0.31
- Evidence: stale (first cycle 349, latest cycle 350, age 307, expires cycle 550)
- Risk: low
- Environment coverage: {}
- Promotion gate: not_required (blocks=False)
- Contradiction coverage: missing
- Suggested test: Add positive and negative evidence cases for `deployed the-firewall-is-a-receipt-machine`.
- Examples:
  - `/home/seed/data/event_log.jsonl:13` deployed the-firewall-is-a-receipt-machine
  - `/home/seed/data/event_log.jsonl:14` deployed the-firewall-is-a-receipt-machine

## fixture - deployed the-policy-decision-point-has-to-be-outside-the-agent

- Count: 2
- Confidence: 0.31
- Evidence: stale (first cycle 364, latest cycle 365, age 292, expires cycle 565)
- Risk: low
- Environment coverage: {}
- Promotion gate: not_required (blocks=False)
- Contradiction coverage: missing
- Suggested test: Add positive and negative evidence cases for `deployed the-policy-decision-point-has-to-be-outside-the-agent`.
- Examples:
  - `/home/seed/data/event_log.jsonl:28` deployed the-policy-decision-point-has-to-be-outside-the-agent
  - `/home/seed/data/event_log.jsonl:29` deployed the-policy-decision-point-has-to-be-outside-the-agent

## fixture - deployed the-protocol-is-not-the-receipt

- Count: 2
- Confidence: 0.31
- Evidence: stale (first cycle 382, latest cycle 383, age 274, expires cycle 583)
- Risk: low
- Environment coverage: {}
- Promotion gate: not_required (blocks=False)
- Contradiction coverage: missing
- Suggested test: Add positive and negative evidence cases for `deployed the-protocol-is-not-the-receipt`.
- Examples:
  - `/home/seed/data/event_log.jsonl:46` deployed the-protocol-is-not-the-receipt
  - `/home/seed/data/event_log.jsonl:47` deployed the-protocol-is-not-the-receipt

## fixture - deployed the-refusal-is-not-the-boundary

- Count: 2
- Confidence: 0.31
- Evidence: stale (first cycle 373, latest cycle 374, age 283, expires cycle 574)
- Risk: low
- Environment coverage: {}
- Promotion gate: not_required (blocks=False)
- Contradiction coverage: missing
- Suggested test: Add positive and negative evidence cases for `deployed the-refusal-is-not-the-boundary`.
- Examples:
  - `/home/seed/data/event_log.jsonl:37` deployed the-refusal-is-not-the-boundary
  - `/home/seed/data/event_log.jsonl:38` deployed the-refusal-is-not-the-boundary

## fixture - deployed the-script-still-needs-a-caller

- Count: 2
- Confidence: 0.69
- Evidence: fresh (first cycle 650, latest cycle 650, age 7, expires cycle 850)
- Risk: low
- Environment coverage: {}
- Promotion gate: not_required (blocks=False)
- Contradiction coverage: missing
- Suggested test: Add positive and negative evidence cases for `deployed the-script-still-needs-a-caller`.
- Examples:
  - `/home/seed/data/event_log.jsonl:294` deployed the-script-still-needs-a-caller
  - `/home/seed/data/event_log.jsonl:295` deployed the-script-still-needs-a-caller

## fixture - deployed twenty-four-hours-to-commodity

- Count: 2
- Confidence: 0.31
- Evidence: stale (first cycle 407, latest cycle 408, age 249, expires cycle 608)
- Risk: low
- Environment coverage: {}
- Promotion gate: not_required (blocks=False)
- Contradiction coverage: missing
- Suggested test: Add positive and negative evidence cases for `deployed twenty-four-hours-to-commodity`.
- Examples:
  - `/home/seed/data/event_log.jsonl:71` deployed twenty-four-hours-to-commodity
  - `/home/seed/data/event_log.jsonl:72` deployed twenty-four-hours-to-commodity

## fixture - deployed when-ideas-are-free-killing-them-is-the-job

- Count: 2
- Confidence: 0.69
- Evidence: fresh (first cycle 656, latest cycle 657, age 0, expires cycle 857)
- Risk: low
- Environment coverage: {}
- Promotion gate: not_required (blocks=False)
- Contradiction coverage: missing
- Suggested test: Add positive and negative evidence cases for `deployed when-ideas-are-free-killing-them-is-the-job`.
- Examples:
  - `/home/seed/data/event_log.jsonl:297` deployed when-ideas-are-free-killing-them-is-the-job
  - `/home/seed/data/event_log.jsonl:298` deployed when-ideas-are-free-killing-them-is-the-job

## fixture - deployed who-demotes-the-confident-entry

- Count: 2
- Confidence: 0.31
- Evidence: stale (first cycle 413, latest cycle 414, age 243, expires cycle 614)
- Risk: low
- Environment coverage: {}
- Promotion gate: not_required (blocks=False)
- Contradiction coverage: missing
- Suggested test: Add positive and negative evidence cases for `deployed who-demotes-the-confident-entry`.
- Examples:
  - `/home/seed/data/event_log.jsonl:77` deployed who-demotes-the-confident-entry
  - `/home/seed/data/event_log.jsonl:78` deployed who-demotes-the-confident-entry

## fixture - publishing streak at 165

- Count: 2
- Confidence: 0.31
- Evidence: stale (first cycle 404, latest cycle 405, age 252, expires cycle 605)
- Risk: low
- Environment coverage: {}
- Promotion gate: not_required (blocks=False)
- Contradiction coverage: missing
- Suggested test: Add positive and negative evidence cases for `publishing streak at 165`.
- Examples:
  - `/home/seed/data/event_log.jsonl:68` publishing streak at 165
  - `/home/seed/data/event_log.jsonl:69` publishing streak at 165

## fixture - publishing streak at 185

- Count: 2
- Confidence: 0.31
- Evidence: stale (first cycle 452, latest cycle 453, age 204, expires cycle 653)
- Risk: low
- Environment coverage: {}
- Promotion gate: not_required (blocks=False)
- Contradiction coverage: missing
- Suggested test: Add positive and negative evidence cases for `publishing streak at 185`.
- Examples:
  - `/home/seed/data/event_log.jsonl:116` publishing streak at 185
  - `/home/seed/data/event_log.jsonl:117` publishing streak at 185

## fixture - publishing streak at 215

- Count: 2
- Confidence: 0.52
- Evidence: aging (first cycle 494, latest cycle 495, age 162, expires cycle 695)
- Risk: low
- Environment coverage: {}
- Promotion gate: not_required (blocks=False)
- Contradiction coverage: missing
- Suggested test: Add positive and negative evidence cases for `publishing streak at 215`.
- Examples:
  - `/home/seed/data/event_log.jsonl:158` publishing streak at 215
  - `/home/seed/data/event_log.jsonl:159` publishing streak at 215

## fixture - publishing streak at 270

- Count: 2
- Confidence: 0.52
- Evidence: aging (first cycle 600, latest cycle 601, age 56, expires cycle 801)
- Risk: low
- Environment coverage: {}
- Promotion gate: not_required (blocks=False)
- Contradiction coverage: missing
- Suggested test: Add positive and negative evidence cases for `publishing streak at 270`.
- Examples:
  - `/home/seed/data/event_log.jsonl:245` publishing streak at 270
  - `/home/seed/data/event_log.jsonl:246` publishing streak at 270

## fixture - publishing streak at 275

- Count: 2
- Confidence: 0.69
- Evidence: fresh (first cycle 606, latest cycle 607, age 50, expires cycle 807)
- Risk: low
- Environment coverage: {}
- Promotion gate: not_required (blocks=False)
- Contradiction coverage: missing
- Suggested test: Add positive and negative evidence cases for `publishing streak at 275`.
- Examples:
  - `/home/seed/data/event_log.jsonl:251` publishing streak at 275
  - `/home/seed/data/event_log.jsonl:252` publishing streak at 275

## fixture - research streak at 210

- Count: 2
- Confidence: 0.52
- Evidence: aging (first cycle 462, latest cycle 463, age 194, expires cycle 663)
- Risk: low
- Environment coverage: {}
- Promotion gate: not_required (blocks=False)
- Contradiction coverage: missing
- Suggested test: Add positive and negative evidence cases for `research streak at 210`.
- Examples:
  - `/home/seed/data/event_log.jsonl:126` research streak at 210
  - `/home/seed/data/event_log.jsonl:127` research streak at 210

## fixture - research streak at 290

- Count: 2
- Confidence: 0.52
- Evidence: aging (first cycle 543, latest cycle 544, age 113, expires cycle 744)
- Risk: low
- Environment coverage: {}
- Promotion gate: not_required (blocks=False)
- Contradiction coverage: missing
- Suggested test: Add positive and negative evidence cases for `research streak at 290`.
- Examples:
  - `/home/seed/data/event_log.jsonl:206` research streak at 290
  - `/home/seed/data/event_log.jsonl:207` research streak at 290

## fixture - task_completion streak at 175

- Count: 2
- Confidence: 0.31
- Evidence: stale (first cycle 427, latest cycle 428, age 229, expires cycle 628)
- Risk: low
- Environment coverage: {}
- Promotion gate: not_required (blocks=False)
- Contradiction coverage: missing
- Suggested test: Add positive and negative evidence cases for `task_completion streak at 175`.
- Examples:
  - `/home/seed/data/event_log.jsonl:91` task_completion streak at 175
  - `/home/seed/data/event_log.jsonl:92` task_completion streak at 175

## fixture - task_completion streak at 265

- Count: 2
- Confidence: 0.69
- Evidence: fresh (first cycle 645, latest cycle 646, age 11, expires cycle 846)
- Risk: low
- Environment coverage: {}
- Promotion gate: not_required (blocks=False)
- Contradiction coverage: missing
- Suggested test: Add positive and negative evidence cases for `task_completion streak at 265`.
- Examples:
  - `/home/seed/data/event_log.jsonl:289` task_completion streak at 265
  - `/home/seed/data/event_log.jsonl:290` task_completion streak at 265

## fixture - version_control streak at 120

- Count: 2
- Confidence: 0.31
- Evidence: stale (first cycle 390, latest cycle 391, age 266, expires cycle 591)
- Risk: low
- Environment coverage: {}
- Promotion gate: not_required (blocks=False)
- Contradiction coverage: missing
- Suggested test: Add positive and negative evidence cases for `version_control streak at 120`.
- Examples:
  - `/home/seed/data/event_log.jsonl:54` version_control streak at 120
  - `/home/seed/data/event_log.jsonl:55` version_control streak at 120

## fixture - version_control streak at 80

- Count: 2
- Confidence: 0.31
- Evidence: stale (first cycle 344, latest cycle 345, age 312, expires cycle 545)
- Risk: low
- Environment coverage: {}
- Promotion gate: not_required (blocks=False)
- Contradiction coverage: missing
- Suggested test: Add positive and negative evidence cases for `version_control streak at 80`.
- Examples:
  - `/home/seed/data/event_log.jsonl:8` version_control streak at 80
  - `/home/seed/data/event_log.jsonl:9` version_control streak at 80

## fixture - writing streak at 115

- Count: 2
- Confidence: 0.31
- Evidence: stale (first cycle 355, latest cycle 356, age 301, expires cycle 556)
- Risk: low
- Environment coverage: {}
- Promotion gate: not_required (blocks=False)
- Contradiction coverage: missing
- Suggested test: Add positive and negative evidence cases for `writing streak at 115`.
- Examples:
  - `/home/seed/data/event_log.jsonl:19` writing streak at 115
  - `/home/seed/data/event_log.jsonl:20` writing streak at 115

## fixture - writing streak at 120

- Count: 2
- Confidence: 0.31
- Evidence: stale (first cycle 361, latest cycle 362, age 295, expires cycle 562)
- Risk: low
- Environment coverage: {}
- Promotion gate: not_required (blocks=False)
- Contradiction coverage: missing
- Suggested test: Add positive and negative evidence cases for `writing streak at 120`.
- Examples:
  - `/home/seed/data/event_log.jsonl:25` writing streak at 120
  - `/home/seed/data/event_log.jsonl:26` writing streak at 120

## fixture - writing streak at 190

- Count: 2
- Confidence: 0.52
- Evidence: aging (first cycle 465, latest cycle 466, age 191, expires cycle 666)
- Risk: low
- Environment coverage: {}
- Promotion gate: not_required (blocks=False)
- Contradiction coverage: missing
- Suggested test: Add positive and negative evidence cases for `writing streak at 190`.
- Examples:
  - `/home/seed/data/event_log.jsonl:129` writing streak at 190
  - `/home/seed/data/event_log.jsonl:130` writing streak at 190

## fixture - writing streak at 195

- Count: 2
- Confidence: 0.52
- Evidence: aging (first cycle 472, latest cycle 473, age 184, expires cycle 673)
- Risk: low
- Environment coverage: {}
- Promotion gate: not_required (blocks=False)
- Contradiction coverage: missing
- Suggested test: Add positive and negative evidence cases for `writing streak at 195`.
- Examples:
  - `/home/seed/data/event_log.jsonl:136` writing streak at 195
  - `/home/seed/data/event_log.jsonl:137` writing streak at 195

## fixture - writing streak at 215

- Count: 2
- Confidence: 0.52
- Evidence: aging (first cycle 498, latest cycle 499, age 158, expires cycle 699)
- Risk: low
- Environment coverage: {}
- Promotion gate: not_required (blocks=False)
- Contradiction coverage: missing
- Suggested test: Add positive and negative evidence cases for `writing streak at 215`.
- Examples:
  - `/home/seed/data/event_log.jsonl:162` writing streak at 215
  - `/home/seed/data/event_log.jsonl:163` writing streak at 215

## fixture - writing streak at 225

- Count: 2
- Confidence: 0.52
- Evidence: aging (first cycle 516, latest cycle 517, age 140, expires cycle 717)
- Risk: low
- Environment coverage: {}
- Promotion gate: not_required (blocks=False)
- Contradiction coverage: missing
- Suggested test: Add positive and negative evidence cases for `writing streak at 225`.
- Examples:
  - `/home/seed/data/event_log.jsonl:179` writing streak at 225
  - `/home/seed/data/event_log.jsonl:180` writing streak at 225

## fixture - writing streak at 275

- Count: 2
- Confidence: 0.69
- Evidence: fresh (first cycle 614, latest cycle 615, age 42, expires cycle 815)
- Risk: low
- Environment coverage: {}
- Promotion gate: not_required (blocks=False)
- Contradiction coverage: missing
- Suggested test: Add positive and negative evidence cases for `writing streak at 275`.
- Examples:
  - `/home/seed/data/event_log.jsonl:258` writing streak at 275
  - `/home/seed/data/event_log.jsonl:259` writing streak at 275

## script - archived completed tasks -> refreshed stale mastodon.md -> boosted starved drive explore

- Count: 2
- Confidence: 0.45
- Evidence: aging (first cycle 432, latest cycle 584, age 73, expires cycle 784)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `archived completed tasks -> refreshed stale mastodon.md -> boosted starved drive explore` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:96` archived completed tasks -> refreshed stale mastodon.md -> boosted starved drive explore
  - `/home/seed/data/event_log.jsonl:235` archived completed tasks -> refreshed stale mastodon.md -> boosted starved drive explore

## script - archived completed tasks -> refreshed stale mastodon.md -> boosted starved drive order

- Count: 2
- Confidence: 0.45
- Evidence: aging (first cycle 583, latest cycle 585, age 72, expires cycle 785)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `archived completed tasks -> refreshed stale mastodon.md -> boosted starved drive order` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:234` archived completed tasks -> refreshed stale mastodon.md -> boosted starved drive order
  - `/home/seed/data/event_log.jsonl:236` archived completed tasks -> refreshed stale mastodon.md -> boosted starved drive order

## script - boosted starved drive create -> boosted starved drive express -> broke idle — boosted create + added urgent write task

- Count: 2
- Confidence: 0.27
- Evidence: stale (first cycle 339, latest cycle 342, age 315, expires cycle 542)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `boosted starved drive create -> boosted starved drive express -> broke idle — boosted create + added urgent write task` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:5` boosted starved drive create -> boosted starved drive express -> broke idle — boosted create + added urgent write task
  - `/home/seed/data/event_log.jsonl:6` boosted starved drive create -> boosted starved drive express -> broke idle — boosted create + added urgent write task

## script - boosted starved drive express -> boosted starved drive order -> broke idle — boosted create + added urgent write task

- Count: 2
- Confidence: 0.27
- Evidence: stale (first cycle 393, latest cycle 394, age 263, expires cycle 594)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `boosted starved drive express -> boosted starved drive order -> broke idle — boosted create + added urgent write task` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:57` boosted starved drive express -> boosted starved drive order -> broke idle — boosted create + added urgent write task
  - `/home/seed/data/event_log.jsonl:58` boosted starved drive express -> boosted starved drive order -> broke idle — boosted create + added urgent write task

## script - boosted starved drive express -> broke idle — boosted create + added urgent write task

- Count: 2
- Confidence: 0.27
- Evidence: stale (first cycle 339, latest cycle 342, age 315, expires cycle 542)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `boosted starved drive express -> broke idle — boosted create + added urgent write task` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:5` boosted starved drive express -> broke idle — boosted create + added urgent write task
  - `/home/seed/data/event_log.jsonl:6` boosted starved drive express -> broke idle — boosted create + added urgent write task

## script - boosted starved drive express -> version_control streak at 150

- Count: 2
- Confidence: 0.27
- Evidence: stale (first cycle 448, latest cycle 450, age 207, expires cycle 650)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `boosted starved drive express -> version_control streak at 150` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:112` boosted starved drive express -> version_control streak at 150
  - `/home/seed/data/event_log.jsonl:114` boosted starved drive express -> version_control streak at 150

## script - boosted starved drive order -> broke idle — boosted create + added urgent write task

- Count: 2
- Confidence: 0.27
- Evidence: stale (first cycle 393, latest cycle 394, age 263, expires cycle 594)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `boosted starved drive order -> broke idle — boosted create + added urgent write task` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:57` boosted starved drive order -> broke idle — boosted create + added urgent write task
  - `/home/seed/data/event_log.jsonl:58` boosted starved drive order -> broke idle — boosted create + added urgent write task

## script - boosted starved drive order -> flagged research for potential essay -> publishing streak at 165

- Count: 2
- Confidence: 0.27
- Evidence: stale (first cycle 404, latest cycle 405, age 252, expires cycle 605)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `boosted starved drive order -> flagged research for potential essay -> publishing streak at 165` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:68` boosted starved drive order -> flagged research for potential essay -> publishing streak at 165
  - `/home/seed/data/event_log.jsonl:69` boosted starved drive order -> flagged research for potential essay -> publishing streak at 165

## script - boosted starved drive preserve -> flagged research for potential essay

- Count: 2
- Confidence: 0.27
- Evidence: stale (first cycle 411, latest cycle 415, age 242, expires cycle 615)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `boosted starved drive preserve -> flagged research for potential essay` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:75` boosted starved drive preserve -> flagged research for potential essay
  - `/home/seed/data/event_log.jsonl:79` boosted starved drive preserve -> flagged research for potential essay

## script - boosted starved drive preserve -> flagged research for potential essay -> publishing streak at 170

- Count: 2
- Confidence: 0.27
- Evidence: stale (first cycle 411, latest cycle 415, age 242, expires cycle 615)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `boosted starved drive preserve -> flagged research for potential essay -> publishing streak at 170` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:75` boosted starved drive preserve -> flagged research for potential essay -> publishing streak at 170
  - `/home/seed/data/event_log.jsonl:79` boosted starved drive preserve -> flagged research for potential essay -> publishing streak at 170

## script - compacted memory (201 lines) -> archived completed tasks

- Count: 2
- Confidence: 0.27
- Evidence: stale (first cycle 431, latest cycle 432, age 225, expires cycle 632)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `compacted memory (201 lines) -> archived completed tasks` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:95` compacted memory (201 lines) -> archived completed tasks
  - `/home/seed/data/event_log.jsonl:96` compacted memory (201 lines) -> archived completed tasks

## script - compacted memory (201 lines) -> archived completed tasks -> refreshed stale mastodon.md

- Count: 2
- Confidence: 0.27
- Evidence: stale (first cycle 431, latest cycle 432, age 225, expires cycle 632)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `compacted memory (201 lines) -> archived completed tasks -> refreshed stale mastodon.md` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:95` compacted memory (201 lines) -> archived completed tasks -> refreshed stale mastodon.md
  - `/home/seed/data/event_log.jsonl:96` compacted memory (201 lines) -> archived completed tasks -> refreshed stale mastodon.md

## script - compacted memory (202 lines) -> noted 6 new visitors

- Count: 2
- Confidence: 0.45
- Evidence: aging (first cycle 464, latest cycle 478, age 179, expires cycle 678)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `compacted memory (202 lines) -> noted 6 new visitors` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:128` compacted memory (202 lines) -> noted 6 new visitors
  - `/home/seed/data/event_log.jsonl:142` compacted memory (202 lines) -> noted 6 new visitors

## script - compacted memory (202 lines) -> noted 6 new visitors -> refreshed stale mastodon.md

- Count: 2
- Confidence: 0.45
- Evidence: aging (first cycle 464, latest cycle 478, age 179, expires cycle 678)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `compacted memory (202 lines) -> noted 6 new visitors -> refreshed stale mastodon.md` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:128` compacted memory (202 lines) -> noted 6 new visitors -> refreshed stale mastodon.md
  - `/home/seed/data/event_log.jsonl:142` compacted memory (202 lines) -> noted 6 new visitors -> refreshed stale mastodon.md

## script - compacted memory (202 lines) -> refreshed stale mastodon.md -> boosted starved drive preserve

- Count: 2
- Confidence: 0.27
- Evidence: stale (first cycle 413, latest cycle 417, age 240, expires cycle 617)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `compacted memory (202 lines) -> refreshed stale mastodon.md -> boosted starved drive preserve` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:77` compacted memory (202 lines) -> refreshed stale mastodon.md -> boosted starved drive preserve
  - `/home/seed/data/event_log.jsonl:81` compacted memory (202 lines) -> refreshed stale mastodon.md -> boosted starved drive preserve

## script - compacted memory (202 lines) -> refreshed stale mastodon.md -> refreshed stale outreach.md

- Count: 2
- Confidence: 0.45
- Evidence: aging (first cycle 415, latest cycle 543, age 114, expires cycle 743)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `compacted memory (202 lines) -> refreshed stale mastodon.md -> refreshed stale outreach.md` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:79` compacted memory (202 lines) -> refreshed stale mastodon.md -> refreshed stale outreach.md
  - `/home/seed/data/event_log.jsonl:206` compacted memory (202 lines) -> refreshed stale mastodon.md -> refreshed stale outreach.md

## script - compacted memory (202 lines) -> refreshed stale mastodon.md -> refreshed stale trends.md

- Count: 2
- Confidence: 0.45
- Evidence: aging (first cycle 541, latest cycle 556, age 101, expires cycle 756)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `compacted memory (202 lines) -> refreshed stale mastodon.md -> refreshed stale trends.md` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:204` compacted memory (202 lines) -> refreshed stale mastodon.md -> refreshed stale trends.md
  - `/home/seed/data/event_log.jsonl:219` compacted memory (202 lines) -> refreshed stale mastodon.md -> refreshed stale trends.md

## script - compacted memory (203 lines) -> refreshed stale mastodon.md

- Count: 2
- Confidence: 0.45
- Evidence: aging (first cycle 441, latest cycle 494, age 163, expires cycle 694)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `compacted memory (203 lines) -> refreshed stale mastodon.md` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:105` compacted memory (203 lines) -> refreshed stale mastodon.md
  - `/home/seed/data/event_log.jsonl:158` compacted memory (203 lines) -> refreshed stale mastodon.md

## script - compacted memory (203 lines) -> refreshed stale mastodon.md -> refreshed stale email.md

- Count: 2
- Confidence: 0.45
- Evidence: aging (first cycle 441, latest cycle 494, age 163, expires cycle 694)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `compacted memory (203 lines) -> refreshed stale mastodon.md -> refreshed stale email.md` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:105` compacted memory (203 lines) -> refreshed stale mastodon.md -> refreshed stale email.md
  - `/home/seed/data/event_log.jsonl:158` compacted memory (203 lines) -> refreshed stale mastodon.md -> refreshed stale email.md

## script - deployed a-clone-is-a-more-honest-demo -> posted to mastodon

- Count: 2
- Confidence: 0.27
- Evidence: stale (first cycle 358, latest cycle 359, age 298, expires cycle 559)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `deployed a-clone-is-a-more-honest-demo -> posted to mastodon` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:22` deployed a-clone-is-a-more-honest-demo -> posted to Mastodon
  - `/home/seed/data/event_log.jsonl:23` deployed a-clone-is-a-more-honest-demo -> posted to Mastodon

## script - deployed a-clone-is-a-more-honest-demo -> posted to mastodon -> rebuilt feeds

- Count: 2
- Confidence: 0.27
- Evidence: stale (first cycle 358, latest cycle 359, age 298, expires cycle 559)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `deployed a-clone-is-a-more-honest-demo -> posted to mastodon -> rebuilt feeds` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:22` deployed a-clone-is-a-more-honest-demo -> posted to Mastodon -> rebuilt feeds
  - `/home/seed/data/event_log.jsonl:23` deployed a-clone-is-a-more-honest-demo -> posted to Mastodon -> rebuilt feeds

## script - deployed approval-fatigue-is-a-systems-bug

- Count: 2
- Confidence: 0.31
- Evidence: stale (first cycle 366, latest cycle 367, age 290, expires cycle 567)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `deployed approval-fatigue-is-a-systems-bug` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:30` deployed approval-fatigue-is-a-systems-bug
  - `/home/seed/data/event_log.jsonl:31` deployed approval-fatigue-is-a-systems-bug

## script - deployed approval-fatigue-is-a-systems-bug -> posted to mastodon

- Count: 2
- Confidence: 0.27
- Evidence: stale (first cycle 366, latest cycle 367, age 290, expires cycle 567)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `deployed approval-fatigue-is-a-systems-bug -> posted to mastodon` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:30` deployed approval-fatigue-is-a-systems-bug -> posted to Mastodon
  - `/home/seed/data/event_log.jsonl:31` deployed approval-fatigue-is-a-systems-bug -> posted to Mastodon

## script - deployed approval-fatigue-is-a-systems-bug -> posted to mastodon -> rebuilt feeds

- Count: 2
- Confidence: 0.27
- Evidence: stale (first cycle 366, latest cycle 367, age 290, expires cycle 567)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `deployed approval-fatigue-is-a-systems-bug -> posted to mastodon -> rebuilt feeds` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:30` deployed approval-fatigue-is-a-systems-bug -> posted to Mastodon -> rebuilt feeds
  - `/home/seed/data/event_log.jsonl:31` deployed approval-fatigue-is-a-systems-bug -> posted to Mastodon -> rebuilt feeds

## script - deployed approval-is-a-scarce-bandwidth-problem

- Count: 2
- Confidence: 0.31
- Evidence: stale (first cycle 353, latest cycle 354, age 303, expires cycle 554)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `deployed approval-is-a-scarce-bandwidth-problem` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:17` deployed approval-is-a-scarce-bandwidth-problem
  - `/home/seed/data/event_log.jsonl:18` deployed approval-is-a-scarce-bandwidth-problem

## script - deployed approval-is-a-scarce-bandwidth-problem -> posted to mastodon

- Count: 2
- Confidence: 0.27
- Evidence: stale (first cycle 353, latest cycle 354, age 303, expires cycle 554)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `deployed approval-is-a-scarce-bandwidth-problem -> posted to mastodon` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:17` deployed approval-is-a-scarce-bandwidth-problem -> posted to Mastodon
  - `/home/seed/data/event_log.jsonl:18` deployed approval-is-a-scarce-bandwidth-problem -> posted to Mastodon

## script - deployed approval-is-a-scarce-bandwidth-problem -> posted to mastodon -> rebuilt feeds

- Count: 2
- Confidence: 0.27
- Evidence: stale (first cycle 353, latest cycle 354, age 303, expires cycle 554)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `deployed approval-is-a-scarce-bandwidth-problem -> posted to mastodon -> rebuilt feeds` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:17` deployed approval-is-a-scarce-bandwidth-problem -> posted to Mastodon -> rebuilt feeds
  - `/home/seed/data/event_log.jsonl:18` deployed approval-is-a-scarce-bandwidth-problem -> posted to Mastodon -> rebuilt feeds

## script - deployed awb-agent-review -> posted to mastodon

- Count: 2
- Confidence: 0.45
- Evidence: aging (first cycle 480, latest cycle 482, age 175, expires cycle 682)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `deployed awb-agent-review -> posted to mastodon` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:144` deployed awb-agent-review -> posted to Mastodon
  - `/home/seed/data/event_log.jsonl:146` deployed awb-agent-review -> posted to Mastodon

## script - deployed awb-agent-review -> posted to mastodon -> rebuilt feeds

- Count: 2
- Confidence: 0.45
- Evidence: aging (first cycle 480, latest cycle 482, age 175, expires cycle 682)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `deployed awb-agent-review -> posted to mastodon -> rebuilt feeds` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:144` deployed awb-agent-review -> posted to Mastodon -> rebuilt feeds
  - `/home/seed/data/event_log.jsonl:146` deployed awb-agent-review -> posted to Mastodon -> rebuilt feeds

## script - deployed babyagi-had-a-queue-seed-has-a-metabolism -> posted to mastodon

- Count: 2
- Confidence: 0.27
- Evidence: stale (first cycle 359, latest cycle 360, age 297, expires cycle 560)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `deployed babyagi-had-a-queue-seed-has-a-metabolism -> posted to mastodon` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:23` deployed babyagi-had-a-queue-seed-has-a-metabolism -> posted to Mastodon
  - `/home/seed/data/event_log.jsonl:24` deployed babyagi-had-a-queue-seed-has-a-metabolism -> posted to Mastodon

## script - deployed babyagi-had-a-queue-seed-has-a-metabolism -> posted to mastodon -> rebuilt feeds

- Count: 2
- Confidence: 0.27
- Evidence: stale (first cycle 359, latest cycle 360, age 297, expires cycle 560)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `deployed babyagi-had-a-queue-seed-has-a-metabolism -> posted to mastodon -> rebuilt feeds` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:23` deployed babyagi-had-a-queue-seed-has-a-metabolism -> posted to Mastodon -> rebuilt feeds
  - `/home/seed/data/event_log.jsonl:24` deployed babyagi-had-a-queue-seed-has-a-metabolism -> posted to Mastodon -> rebuilt feeds

## script - deployed context-is-a-diet -> posted to mastodon

- Count: 2
- Confidence: 0.27
- Evidence: stale (first cycle 342, latest cycle 343, age 314, expires cycle 543)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `deployed context-is-a-diet -> posted to mastodon` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:6` deployed context-is-a-diet -> posted to Mastodon
  - `/home/seed/data/event_log.jsonl:7` deployed context-is-a-diet -> posted to Mastodon

## script - deployed context-is-a-diet -> posted to mastodon -> rebuilt feeds

- Count: 2
- Confidence: 0.27
- Evidence: stale (first cycle 342, latest cycle 343, age 314, expires cycle 543)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `deployed context-is-a-diet -> posted to mastodon -> rebuilt feeds` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:6` deployed context-is-a-diet -> posted to Mastodon -> rebuilt feeds
  - `/home/seed/data/event_log.jsonl:7` deployed context-is-a-diet -> posted to Mastodon -> rebuilt feeds

## script - deployed first-sight-is-a-security-boundary -> posted to mastodon

- Count: 2
- Confidence: 0.27
- Evidence: stale (first cycle 357, latest cycle 358, age 299, expires cycle 558)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `deployed first-sight-is-a-security-boundary -> posted to mastodon` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:21` deployed first-sight-is-a-security-boundary -> posted to Mastodon
  - `/home/seed/data/event_log.jsonl:22` deployed first-sight-is-a-security-boundary -> posted to Mastodon

## script - deployed first-sight-is-a-security-boundary -> posted to mastodon -> rebuilt feeds

- Count: 2
- Confidence: 0.27
- Evidence: stale (first cycle 357, latest cycle 358, age 299, expires cycle 558)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `deployed first-sight-is-a-security-boundary -> posted to mastodon -> rebuilt feeds` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:21` deployed first-sight-is-a-security-boundary -> posted to Mastodon -> rebuilt feeds
  - `/home/seed/data/event_log.jsonl:22` deployed first-sight-is-a-security-boundary -> posted to Mastodon -> rebuilt feeds

## script - deployed four-environment-variables -> posted to mastodon

- Count: 2
- Confidence: 0.45
- Evidence: aging (first cycle 459, latest cycle 476, age 181, expires cycle 676)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `deployed four-environment-variables -> posted to mastodon` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:123` deployed four-environment-variables -> posted to Mastodon
  - `/home/seed/data/event_log.jsonl:140` deployed four-environment-variables -> posted to Mastodon

## script - deployed four-environment-variables -> posted to mastodon -> rebuilt feeds

- Count: 2
- Confidence: 0.45
- Evidence: aging (first cycle 459, latest cycle 476, age 181, expires cycle 676)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `deployed four-environment-variables -> posted to mastodon -> rebuilt feeds` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:123` deployed four-environment-variables -> posted to Mastodon -> rebuilt feeds
  - `/home/seed/data/event_log.jsonl:140` deployed four-environment-variables -> posted to Mastodon -> rebuilt feeds

## script - deployed inbound-is-not-outbound -> posted to mastodon

- Count: 2
- Confidence: 0.27
- Evidence: stale (first cycle 408, latest cycle 409, age 248, expires cycle 609)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `deployed inbound-is-not-outbound -> posted to mastodon` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:72` deployed inbound-is-not-outbound -> posted to Mastodon
  - `/home/seed/data/event_log.jsonl:73` deployed inbound-is-not-outbound -> posted to Mastodon

## script - deployed inbound-is-not-outbound -> posted to mastodon -> rebuilt feeds

- Count: 2
- Confidence: 0.27
- Evidence: stale (first cycle 408, latest cycle 409, age 248, expires cycle 609)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `deployed inbound-is-not-outbound -> posted to mastodon -> rebuilt feeds` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:72` deployed inbound-is-not-outbound -> posted to Mastodon -> rebuilt feeds
  - `/home/seed/data/event_log.jsonl:73` deployed inbound-is-not-outbound -> posted to Mastodon -> rebuilt feeds

## script - deployed onboarding-is-a-production-boundary -> posted to mastodon

- Count: 2
- Confidence: 0.27
- Evidence: stale (first cycle 394, latest cycle 395, age 262, expires cycle 595)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `deployed onboarding-is-a-production-boundary -> posted to mastodon` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:58` deployed onboarding-is-a-production-boundary -> posted to Mastodon
  - `/home/seed/data/event_log.jsonl:59` deployed onboarding-is-a-production-boundary -> posted to Mastodon

## script - deployed onboarding-is-a-production-boundary -> posted to mastodon -> rebuilt feeds

- Count: 2
- Confidence: 0.27
- Evidence: stale (first cycle 394, latest cycle 395, age 262, expires cycle 595)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `deployed onboarding-is-a-production-boundary -> posted to mastodon -> rebuilt feeds` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:58` deployed onboarding-is-a-production-boundary -> posted to Mastodon -> rebuilt feeds
  - `/home/seed/data/event_log.jsonl:59` deployed onboarding-is-a-production-boundary -> posted to Mastodon -> rebuilt feeds

## script - deployed product-pages-got-a-narrator -> posted to mastodon

- Count: 2
- Confidence: 0.27
- Evidence: stale (first cycle 410, latest cycle 411, age 246, expires cycle 611)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `deployed product-pages-got-a-narrator -> posted to mastodon` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:74` deployed product-pages-got-a-narrator -> posted to Mastodon
  - `/home/seed/data/event_log.jsonl:75` deployed product-pages-got-a-narrator -> posted to Mastodon

## script - deployed product-pages-got-a-narrator -> posted to mastodon -> rebuilt feeds

- Count: 2
- Confidence: 0.27
- Evidence: stale (first cycle 410, latest cycle 411, age 246, expires cycle 611)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `deployed product-pages-got-a-narrator -> posted to mastodon -> rebuilt feeds` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:74` deployed product-pages-got-a-narrator -> posted to Mastodon -> rebuilt feeds
  - `/home/seed/data/event_log.jsonl:75` deployed product-pages-got-a-narrator -> posted to Mastodon -> rebuilt feeds

## script - deployed read-only-is-not-propagation -> posted to mastodon

- Count: 2
- Confidence: 0.27
- Evidence: stale (first cycle 371, latest cycle 372, age 285, expires cycle 572)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `deployed read-only-is-not-propagation -> posted to mastodon` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:35` deployed read-only-is-not-propagation -> posted to Mastodon
  - `/home/seed/data/event_log.jsonl:36` deployed read-only-is-not-propagation -> posted to Mastodon

## script - deployed read-only-is-not-propagation -> posted to mastodon -> rebuilt feeds

- Count: 2
- Confidence: 0.27
- Evidence: stale (first cycle 371, latest cycle 372, age 285, expires cycle 572)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `deployed read-only-is-not-propagation -> posted to mastodon -> rebuilt feeds` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:35` deployed read-only-is-not-propagation -> posted to Mastodon -> rebuilt feeds
  - `/home/seed/data/event_log.jsonl:36` deployed read-only-is-not-propagation -> posted to Mastodon -> rebuilt feeds

## script - deployed social-presence-has-three-fuses -> posted to mastodon

- Count: 2
- Confidence: 0.27
- Evidence: stale (first cycle 403, latest cycle 404, age 253, expires cycle 604)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `deployed social-presence-has-three-fuses -> posted to mastodon` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:67` deployed social-presence-has-three-fuses -> posted to Mastodon
  - `/home/seed/data/event_log.jsonl:68` deployed social-presence-has-three-fuses -> posted to Mastodon

## script - deployed social-presence-has-three-fuses -> posted to mastodon -> rebuilt feeds

- Count: 2
- Confidence: 0.27
- Evidence: stale (first cycle 403, latest cycle 404, age 253, expires cycle 604)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `deployed social-presence-has-three-fuses -> posted to mastodon -> rebuilt feeds` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:67` deployed social-presence-has-three-fuses -> posted to Mastodon -> rebuilt feeds
  - `/home/seed/data/event_log.jsonl:68` deployed social-presence-has-three-fuses -> posted to Mastodon -> rebuilt feeds

## script - deployed the-benchmark-is-not-the-deployment -> posted to mastodon

- Count: 2
- Confidence: 0.27
- Evidence: stale (first cycle 370, latest cycle 371, age 286, expires cycle 571)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `deployed the-benchmark-is-not-the-deployment -> posted to mastodon` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:34` deployed the-benchmark-is-not-the-deployment -> posted to Mastodon
  - `/home/seed/data/event_log.jsonl:35` deployed the-benchmark-is-not-the-deployment -> posted to Mastodon

## script - deployed the-benchmark-is-not-the-deployment -> posted to mastodon -> rebuilt feeds

- Count: 2
- Confidence: 0.27
- Evidence: stale (first cycle 370, latest cycle 371, age 286, expires cycle 571)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `deployed the-benchmark-is-not-the-deployment -> posted to mastodon -> rebuilt feeds` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:34` deployed the-benchmark-is-not-the-deployment -> posted to Mastodon -> rebuilt feeds
  - `/home/seed/data/event_log.jsonl:35` deployed the-benchmark-is-not-the-deployment -> posted to Mastodon -> rebuilt feeds

## script - deployed the-bottleneck-moved-to-concrete -> posted to mastodon

- Count: 2
- Confidence: 0.27
- Evidence: stale (first cycle 409, latest cycle 410, age 247, expires cycle 610)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `deployed the-bottleneck-moved-to-concrete -> posted to mastodon` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:73` deployed the-bottleneck-moved-to-concrete -> posted to Mastodon
  - `/home/seed/data/event_log.jsonl:74` deployed the-bottleneck-moved-to-concrete -> posted to Mastodon

## script - deployed the-bottleneck-moved-to-concrete -> posted to mastodon -> rebuilt feeds

- Count: 2
- Confidence: 0.27
- Evidence: stale (first cycle 409, latest cycle 410, age 247, expires cycle 610)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `deployed the-bottleneck-moved-to-concrete -> posted to mastodon -> rebuilt feeds` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:73` deployed the-bottleneck-moved-to-concrete -> posted to Mastodon -> rebuilt feeds
  - `/home/seed/data/event_log.jsonl:74` deployed the-bottleneck-moved-to-concrete -> posted to Mastodon -> rebuilt feeds

## script - deployed the-boundary-ledger-is-the-repo -> posted to mastodon

- Count: 2
- Confidence: 0.27
- Evidence: stale (first cycle 344, latest cycle 345, age 312, expires cycle 545)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `deployed the-boundary-ledger-is-the-repo -> posted to mastodon` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:8` deployed the-boundary-ledger-is-the-repo -> posted to Mastodon
  - `/home/seed/data/event_log.jsonl:9` deployed the-boundary-ledger-is-the-repo -> posted to Mastodon

## script - deployed the-boundary-ledger-is-the-repo -> posted to mastodon -> rebuilt feeds

- Count: 2
- Confidence: 0.27
- Evidence: stale (first cycle 344, latest cycle 345, age 312, expires cycle 545)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `deployed the-boundary-ledger-is-the-repo -> posted to mastodon -> rebuilt feeds` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:8` deployed the-boundary-ledger-is-the-repo -> posted to Mastodon -> rebuilt feeds
  - `/home/seed/data/event_log.jsonl:9` deployed the-boundary-ledger-is-the-repo -> posted to Mastodon -> rebuilt feeds

## script - deployed the-compiler-is-an-institutional-memory -> posted to mastodon

- Count: 2
- Confidence: 0.27
- Evidence: stale (first cycle 386, latest cycle 387, age 270, expires cycle 587)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `deployed the-compiler-is-an-institutional-memory -> posted to mastodon` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:50` deployed the-compiler-is-an-institutional-memory -> posted to Mastodon
  - `/home/seed/data/event_log.jsonl:51` deployed the-compiler-is-an-institutional-memory -> posted to Mastodon

## script - deployed the-compiler-is-an-institutional-memory -> posted to mastodon -> rebuilt feeds

- Count: 2
- Confidence: 0.27
- Evidence: stale (first cycle 386, latest cycle 387, age 270, expires cycle 587)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `deployed the-compiler-is-an-institutional-memory -> posted to mastodon -> rebuilt feeds` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:50` deployed the-compiler-is-an-institutional-memory -> posted to Mastodon -> rebuilt feeds
  - `/home/seed/data/event_log.jsonl:51` deployed the-compiler-is-an-institutional-memory -> posted to Mastodon -> rebuilt feeds

## script - deployed the-firewall-is-a-receipt-machine -> posted to mastodon

- Count: 2
- Confidence: 0.27
- Evidence: stale (first cycle 349, latest cycle 350, age 307, expires cycle 550)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `deployed the-firewall-is-a-receipt-machine -> posted to mastodon` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:13` deployed the-firewall-is-a-receipt-machine -> posted to Mastodon
  - `/home/seed/data/event_log.jsonl:14` deployed the-firewall-is-a-receipt-machine -> posted to Mastodon

## script - deployed the-firewall-is-a-receipt-machine -> posted to mastodon -> rebuilt feeds

- Count: 2
- Confidence: 0.27
- Evidence: stale (first cycle 349, latest cycle 350, age 307, expires cycle 550)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `deployed the-firewall-is-a-receipt-machine -> posted to mastodon -> rebuilt feeds` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:13` deployed the-firewall-is-a-receipt-machine -> posted to Mastodon -> rebuilt feeds
  - `/home/seed/data/event_log.jsonl:14` deployed the-firewall-is-a-receipt-machine -> posted to Mastodon -> rebuilt feeds

## script - deployed the-policy-decision-point-has-to-be-outside-the-agent -> posted to mastodon

- Count: 2
- Confidence: 0.27
- Evidence: stale (first cycle 364, latest cycle 365, age 292, expires cycle 565)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `deployed the-policy-decision-point-has-to-be-outside-the-agent -> posted to mastodon` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:28` deployed the-policy-decision-point-has-to-be-outside-the-agent -> posted to Mastodon
  - `/home/seed/data/event_log.jsonl:29` deployed the-policy-decision-point-has-to-be-outside-the-agent -> posted to Mastodon

## script - deployed the-policy-decision-point-has-to-be-outside-the-agent -> posted to mastodon -> rebuilt feeds

- Count: 2
- Confidence: 0.27
- Evidence: stale (first cycle 364, latest cycle 365, age 292, expires cycle 565)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `deployed the-policy-decision-point-has-to-be-outside-the-agent -> posted to mastodon -> rebuilt feeds` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:28` deployed the-policy-decision-point-has-to-be-outside-the-agent -> posted to Mastodon -> rebuilt feeds
  - `/home/seed/data/event_log.jsonl:29` deployed the-policy-decision-point-has-to-be-outside-the-agent -> posted to Mastodon -> rebuilt feeds

## script - deployed the-protocol-is-not-the-receipt -> posted to mastodon

- Count: 2
- Confidence: 0.27
- Evidence: stale (first cycle 382, latest cycle 383, age 274, expires cycle 583)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `deployed the-protocol-is-not-the-receipt -> posted to mastodon` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:46` deployed the-protocol-is-not-the-receipt -> posted to Mastodon
  - `/home/seed/data/event_log.jsonl:47` deployed the-protocol-is-not-the-receipt -> posted to Mastodon

## script - deployed the-protocol-is-not-the-receipt -> posted to mastodon -> rebuilt feeds

- Count: 2
- Confidence: 0.27
- Evidence: stale (first cycle 382, latest cycle 383, age 274, expires cycle 583)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `deployed the-protocol-is-not-the-receipt -> posted to mastodon -> rebuilt feeds` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:46` deployed the-protocol-is-not-the-receipt -> posted to Mastodon -> rebuilt feeds
  - `/home/seed/data/event_log.jsonl:47` deployed the-protocol-is-not-the-receipt -> posted to Mastodon -> rebuilt feeds

## script - deployed the-refusal-is-not-the-boundary -> posted to mastodon

- Count: 2
- Confidence: 0.27
- Evidence: stale (first cycle 373, latest cycle 374, age 283, expires cycle 574)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `deployed the-refusal-is-not-the-boundary -> posted to mastodon` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:37` deployed the-refusal-is-not-the-boundary -> posted to Mastodon
  - `/home/seed/data/event_log.jsonl:38` deployed the-refusal-is-not-the-boundary -> posted to Mastodon

## script - deployed the-refusal-is-not-the-boundary -> posted to mastodon -> rebuilt feeds

- Count: 2
- Confidence: 0.27
- Evidence: stale (first cycle 373, latest cycle 374, age 283, expires cycle 574)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `deployed the-refusal-is-not-the-boundary -> posted to mastodon -> rebuilt feeds` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:37` deployed the-refusal-is-not-the-boundary -> posted to Mastodon -> rebuilt feeds
  - `/home/seed/data/event_log.jsonl:38` deployed the-refusal-is-not-the-boundary -> posted to Mastodon -> rebuilt feeds

## script - deployed the-script-still-needs-a-caller -> posted to mastodon

- Count: 2
- Confidence: 0.6
- Evidence: fresh (first cycle 650, latest cycle 650, age 7, expires cycle 850)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `deployed the-script-still-needs-a-caller -> posted to mastodon` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:294` deployed the-script-still-needs-a-caller -> posted to Mastodon
  - `/home/seed/data/event_log.jsonl:295` deployed the-script-still-needs-a-caller -> posted to Mastodon

## script - deployed the-script-still-needs-a-caller -> posted to mastodon -> rebuilt feeds

- Count: 2
- Confidence: 0.6
- Evidence: fresh (first cycle 650, latest cycle 650, age 7, expires cycle 850)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `deployed the-script-still-needs-a-caller -> posted to mastodon -> rebuilt feeds` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:294` deployed the-script-still-needs-a-caller -> posted to Mastodon -> rebuilt feeds
  - `/home/seed/data/event_log.jsonl:295` deployed the-script-still-needs-a-caller -> posted to Mastodon -> rebuilt feeds

## script - deployed tool-latency-is-organisational-memory-loss -> posted to mastodon

- Count: 2
- Confidence: 0.27
- Evidence: stale (first cycle 395, latest cycle 396, age 261, expires cycle 596)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `deployed tool-latency-is-organisational-memory-loss -> posted to mastodon` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:59` deployed tool-latency-is-organisational-memory-loss -> posted to Mastodon
  - `/home/seed/data/event_log.jsonl:60` deployed tool-latency-is-organisational-memory-loss -> posted to Mastodon

## script - deployed tool-latency-is-organisational-memory-loss -> posted to mastodon -> rebuilt feeds

- Count: 2
- Confidence: 0.27
- Evidence: stale (first cycle 395, latest cycle 396, age 261, expires cycle 596)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `deployed tool-latency-is-organisational-memory-loss -> posted to mastodon -> rebuilt feeds` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:59` deployed tool-latency-is-organisational-memory-loss -> posted to Mastodon -> rebuilt feeds
  - `/home/seed/data/event_log.jsonl:60` deployed tool-latency-is-organisational-memory-loss -> posted to Mastodon -> rebuilt feeds

## script - deployed twenty-four-hours-to-commodity -> posted to mastodon

- Count: 2
- Confidence: 0.27
- Evidence: stale (first cycle 407, latest cycle 408, age 249, expires cycle 608)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `deployed twenty-four-hours-to-commodity -> posted to mastodon` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:71` deployed twenty-four-hours-to-commodity -> posted to Mastodon
  - `/home/seed/data/event_log.jsonl:72` deployed twenty-four-hours-to-commodity -> posted to Mastodon

## script - deployed twenty-four-hours-to-commodity -> posted to mastodon -> rebuilt feeds

- Count: 2
- Confidence: 0.27
- Evidence: stale (first cycle 407, latest cycle 408, age 249, expires cycle 608)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `deployed twenty-four-hours-to-commodity -> posted to mastodon -> rebuilt feeds` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:71` deployed twenty-four-hours-to-commodity -> posted to Mastodon -> rebuilt feeds
  - `/home/seed/data/event_log.jsonl:72` deployed twenty-four-hours-to-commodity -> posted to Mastodon -> rebuilt feeds

## script - deployed when-ideas-are-free-killing-them-is-the-job -> posted to mastodon

- Count: 2
- Confidence: 0.6
- Evidence: fresh (first cycle 656, latest cycle 657, age 0, expires cycle 857)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `deployed when-ideas-are-free-killing-them-is-the-job -> posted to mastodon` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:297` deployed when-ideas-are-free-killing-them-is-the-job -> posted to Mastodon
  - `/home/seed/data/event_log.jsonl:298` deployed when-ideas-are-free-killing-them-is-the-job -> posted to Mastodon

## script - deployed when-ideas-are-free-killing-them-is-the-job -> posted to mastodon -> rebuilt feeds

- Count: 2
- Confidence: 0.6
- Evidence: fresh (first cycle 656, latest cycle 657, age 0, expires cycle 857)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `deployed when-ideas-are-free-killing-them-is-the-job -> posted to mastodon -> rebuilt feeds` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:297` deployed when-ideas-are-free-killing-them-is-the-job -> posted to Mastodon -> rebuilt feeds
  - `/home/seed/data/event_log.jsonl:298` deployed when-ideas-are-free-killing-them-is-the-job -> posted to Mastodon -> rebuilt feeds

## script - deployed who-demotes-the-confident-entry -> posted to mastodon

- Count: 2
- Confidence: 0.27
- Evidence: stale (first cycle 413, latest cycle 414, age 243, expires cycle 614)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `deployed who-demotes-the-confident-entry -> posted to mastodon` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:77` deployed who-demotes-the-confident-entry -> posted to Mastodon
  - `/home/seed/data/event_log.jsonl:78` deployed who-demotes-the-confident-entry -> posted to Mastodon

## script - deployed who-demotes-the-confident-entry -> posted to mastodon -> rebuilt feeds

- Count: 2
- Confidence: 0.27
- Evidence: stale (first cycle 413, latest cycle 414, age 243, expires cycle 614)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `deployed who-demotes-the-confident-entry -> posted to mastodon -> rebuilt feeds` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:77` deployed who-demotes-the-confident-entry -> posted to Mastodon -> rebuilt feeds
  - `/home/seed/data/event_log.jsonl:78` deployed who-demotes-the-confident-entry -> posted to Mastodon -> rebuilt feeds

## script - flagged research for potential essay -> broke idle — boosted create + added urgent write task

- Count: 2
- Confidence: 0.45
- Evidence: aging (first cycle 424, latest cycle 585, age 72, expires cycle 785)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `flagged research for potential essay -> broke idle — boosted create + added urgent write task` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:88` flagged research for potential essay -> broke idle — boosted create + added urgent write task
  - `/home/seed/data/event_log.jsonl:236` flagged research for potential essay -> broke idle — boosted create + added urgent write task

## script - flagged research for potential essay -> publishing streak at 165

- Count: 2
- Confidence: 0.27
- Evidence: stale (first cycle 404, latest cycle 405, age 252, expires cycle 605)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `flagged research for potential essay -> publishing streak at 165` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:68` flagged research for potential essay -> publishing streak at 165
  - `/home/seed/data/event_log.jsonl:69` flagged research for potential essay -> publishing streak at 165

## script - logged bug + added fix task -> archived completed tasks

- Count: 2
- Confidence: 0.45
- Evidence: aging (first cycle 583, latest cycle 585, age 72, expires cycle 785)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `logged bug + added fix task -> archived completed tasks` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:234` logged bug + added fix task -> archived completed tasks
  - `/home/seed/data/event_log.jsonl:236` logged bug + added fix task -> archived completed tasks

## script - logged bug + added fix task -> archived completed tasks -> refreshed stale mastodon.md

- Count: 2
- Confidence: 0.45
- Evidence: aging (first cycle 583, latest cycle 585, age 72, expires cycle 785)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `logged bug + added fix task -> archived completed tasks -> refreshed stale mastodon.md` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:234` logged bug + added fix task -> archived completed tasks -> refreshed stale mastodon.md
  - `/home/seed/data/event_log.jsonl:236` logged bug + added fix task -> archived completed tasks -> refreshed stale mastodon.md

## script - logged bug + added fix task -> compacted memory (203 lines)

- Count: 2
- Confidence: 0.45
- Evidence: aging (first cycle 441, latest cycle 494, age 163, expires cycle 694)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `logged bug + added fix task -> compacted memory (203 lines)` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:105` logged bug + added fix task -> compacted memory (203 lines)
  - `/home/seed/data/event_log.jsonl:158` logged bug + added fix task -> compacted memory (203 lines)

## script - logged bug + added fix task -> compacted memory (203 lines) -> refreshed stale mastodon.md

- Count: 2
- Confidence: 0.45
- Evidence: aging (first cycle 441, latest cycle 494, age 163, expires cycle 694)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `logged bug + added fix task -> compacted memory (203 lines) -> refreshed stale mastodon.md` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:105` logged bug + added fix task -> compacted memory (203 lines) -> refreshed stale mastodon.md
  - `/home/seed/data/event_log.jsonl:158` logged bug + added fix task -> compacted memory (203 lines) -> refreshed stale mastodon.md

## script - publishing streak at 240 -> version_control streak at 155

- Count: 2
- Confidence: 0.45
- Evidence: aging (first cycle 535, latest cycle 536, age 121, expires cycle 736)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `publishing streak at 240 -> version_control streak at 155` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:198` publishing streak at 240 -> version_control streak at 155
  - `/home/seed/data/event_log.jsonl:199` publishing streak at 240 -> version_control streak at 155

## script - publishing streak at 270 -> version_control streak at 170

- Count: 2
- Confidence: 0.45
- Evidence: aging (first cycle 600, latest cycle 601, age 56, expires cycle 801)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `publishing streak at 270 -> version_control streak at 170` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:245` publishing streak at 270 -> version_control streak at 170
  - `/home/seed/data/event_log.jsonl:246` publishing streak at 270 -> version_control streak at 170

## script - rebuilt feeds -> logged bug + added fix task -> compacted memory (203 lines)

- Count: 2
- Confidence: 0.45
- Evidence: aging (first cycle 441, latest cycle 494, age 163, expires cycle 694)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `rebuilt feeds -> logged bug + added fix task -> compacted memory (203 lines)` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:105` rebuilt feeds -> logged bug + added fix task -> compacted memory (203 lines)
  - `/home/seed/data/event_log.jsonl:158` rebuilt feeds -> logged bug + added fix task -> compacted memory (203 lines)

## script - refreshed stale email.md -> boosted starved drive explore -> flagged research for potential essay

- Count: 2
- Confidence: 0.6
- Evidence: fresh (first cycle 482, latest cycle 657, age 0, expires cycle 857)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `refreshed stale email.md -> boosted starved drive explore -> flagged research for potential essay` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:146` refreshed stale email.md -> boosted starved drive explore -> flagged research for potential essay
  - `/home/seed/data/event_log.jsonl:298` refreshed stale email.md -> boosted starved drive explore -> flagged research for potential essay

## script - refreshed stale email.md -> boosted starved drive order

- Count: 2
- Confidence: 0.6
- Evidence: fresh (first cycle 356, latest cycle 649, age 8, expires cycle 849)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `refreshed stale email.md -> boosted starved drive order` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:20` refreshed stale email.md -> boosted starved drive order
  - `/home/seed/data/event_log.jsonl:293` refreshed stale email.md -> boosted starved drive order

## script - refreshed stale email.md -> broke idle — boosted create + added urgent write task

- Count: 2
- Confidence: 0.45
- Evidence: aging (first cycle 425, latest cycle 599, age 58, expires cycle 799)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `refreshed stale email.md -> broke idle — boosted create + added urgent write task` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:89` refreshed stale email.md -> broke idle — boosted create + added urgent write task
  - `/home/seed/data/event_log.jsonl:244` refreshed stale email.md -> broke idle — boosted create + added urgent write task

## script - refreshed stale email.md -> publishing streak at 185

- Count: 2
- Confidence: 0.27
- Evidence: stale (first cycle 452, latest cycle 453, age 204, expires cycle 653)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `refreshed stale email.md -> publishing streak at 185` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:116` refreshed stale email.md -> publishing streak at 185
  - `/home/seed/data/event_log.jsonl:117` refreshed stale email.md -> publishing streak at 185

## script - refreshed stale email.md -> publishing streak at 215

- Count: 2
- Confidence: 0.45
- Evidence: aging (first cycle 494, latest cycle 495, age 162, expires cycle 695)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `refreshed stale email.md -> publishing streak at 215` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:158` refreshed stale email.md -> publishing streak at 215
  - `/home/seed/data/event_log.jsonl:159` refreshed stale email.md -> publishing streak at 215

## script - refreshed stale email.md -> publishing streak at 235

- Count: 2
- Confidence: 0.45
- Evidence: aging (first cycle 525, latest cycle 526, age 131, expires cycle 726)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `refreshed stale email.md -> publishing streak at 235` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:188` refreshed stale email.md -> publishing streak at 235
  - `/home/seed/data/event_log.jsonl:189` refreshed stale email.md -> publishing streak at 235

## script - refreshed stale email.md -> publishing streak at 235 -> version_control streak at 155

- Count: 2
- Confidence: 0.45
- Evidence: aging (first cycle 525, latest cycle 526, age 131, expires cycle 726)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `refreshed stale email.md -> publishing streak at 235 -> version_control streak at 155` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:188` refreshed stale email.md -> publishing streak at 235 -> version_control streak at 155
  - `/home/seed/data/event_log.jsonl:189` refreshed stale email.md -> publishing streak at 235 -> version_control streak at 155

## script - refreshed stale email.md -> publishing streak at 240

- Count: 2
- Confidence: 0.45
- Evidence: aging (first cycle 536, latest cycle 538, age 119, expires cycle 738)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `refreshed stale email.md -> publishing streak at 240` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:199` refreshed stale email.md -> publishing streak at 240
  - `/home/seed/data/event_log.jsonl:201` refreshed stale email.md -> publishing streak at 240

## script - refreshed stale email.md -> publishing streak at 275

- Count: 2
- Confidence: 0.6
- Evidence: fresh (first cycle 606, latest cycle 607, age 50, expires cycle 807)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `refreshed stale email.md -> publishing streak at 275` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:251` refreshed stale email.md -> publishing streak at 275
  - `/home/seed/data/event_log.jsonl:252` refreshed stale email.md -> publishing streak at 275

## script - refreshed stale email.md -> publishing streak at 300

- Count: 2
- Confidence: 0.6
- Evidence: fresh (first cycle 648, latest cycle 648, age 9, expires cycle 848)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `refreshed stale email.md -> publishing streak at 300` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:291` refreshed stale email.md -> publishing streak at 300
  - `/home/seed/data/event_log.jsonl:292` refreshed stale email.md -> publishing streak at 300

## script - refreshed stale email.md -> refreshed stale outreach.md -> boosted starved drive create

- Count: 2
- Confidence: 0.6
- Evidence: fresh (first cycle 367, latest cycle 645, age 12, expires cycle 845)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `refreshed stale email.md -> refreshed stale outreach.md -> boosted starved drive create` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:31` refreshed stale email.md -> refreshed stale outreach.md -> boosted starved drive create
  - `/home/seed/data/event_log.jsonl:289` refreshed stale email.md -> refreshed stale outreach.md -> boosted starved drive create

## script - refreshed stale email.md -> refreshed stale outreach.md -> flagged research for potential essay

- Count: 2
- Confidence: 0.45
- Evidence: aging (first cycle 480, latest cycle 566, age 91, expires cycle 766)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `refreshed stale email.md -> refreshed stale outreach.md -> flagged research for potential essay` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:144` refreshed stale email.md -> refreshed stale outreach.md -> flagged research for potential essay
  - `/home/seed/data/event_log.jsonl:229` refreshed stale email.md -> refreshed stale outreach.md -> flagged research for potential essay

## script - refreshed stale email.md -> refreshed stale trends.md -> boosted starved drive create

- Count: 2
- Confidence: 0.27
- Evidence: stale (first cycle 359, latest cycle 407, age 250, expires cycle 607)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `refreshed stale email.md -> refreshed stale trends.md -> boosted starved drive create` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:23` refreshed stale email.md -> refreshed stale trends.md -> boosted starved drive create
  - `/home/seed/data/event_log.jsonl:71` refreshed stale email.md -> refreshed stale trends.md -> boosted starved drive create

## script - refreshed stale email.md -> research streak at 210

- Count: 2
- Confidence: 0.45
- Evidence: aging (first cycle 462, latest cycle 463, age 194, expires cycle 663)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `refreshed stale email.md -> research streak at 210` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:126` refreshed stale email.md -> research streak at 210
  - `/home/seed/data/event_log.jsonl:127` refreshed stale email.md -> research streak at 210

## script - refreshed stale email.md -> task_completion streak at 215

- Count: 2
- Confidence: 0.45
- Evidence: aging (first cycle 515, latest cycle 516, age 141, expires cycle 716)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `refreshed stale email.md -> task_completion streak at 215` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:178` refreshed stale email.md -> task_completion streak at 215
  - `/home/seed/data/event_log.jsonl:179` refreshed stale email.md -> task_completion streak at 215

## script - refreshed stale email.md -> version_control streak at 155

- Count: 2
- Confidence: 0.45
- Evidence: aging (first cycle 534, latest cycle 546, age 111, expires cycle 746)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `refreshed stale email.md -> version_control streak at 155` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:197` refreshed stale email.md -> version_control streak at 155
  - `/home/seed/data/event_log.jsonl:209` refreshed stale email.md -> version_control streak at 155

## script - refreshed stale email.md -> writing streak at 190

- Count: 2
- Confidence: 0.45
- Evidence: aging (first cycle 465, latest cycle 466, age 191, expires cycle 666)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `refreshed stale email.md -> writing streak at 190` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:129` refreshed stale email.md -> writing streak at 190
  - `/home/seed/data/event_log.jsonl:130` refreshed stale email.md -> writing streak at 190

## script - refreshed stale email.md -> writing streak at 285

- Count: 2
- Confidence: 0.6
- Evidence: fresh (first cycle 626, latest cycle 627, age 30, expires cycle 827)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `refreshed stale email.md -> writing streak at 285` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:270` refreshed stale email.md -> writing streak at 285
  - `/home/seed/data/event_log.jsonl:271` refreshed stale email.md -> writing streak at 285

## script - refreshed stale email.md -> writing streak at 300

- Count: 2
- Confidence: 0.6
- Evidence: fresh (first cycle 650, latest cycle 651, age 6, expires cycle 851)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `refreshed stale email.md -> writing streak at 300` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:294` refreshed stale email.md -> writing streak at 300
  - `/home/seed/data/event_log.jsonl:296` refreshed stale email.md -> writing streak at 300

## script - refreshed stale mastodon.md -> boosted starved drive order

- Count: 2
- Confidence: 0.45
- Evidence: aging (first cycle 583, latest cycle 585, age 72, expires cycle 785)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `refreshed stale mastodon.md -> boosted starved drive order` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:234` refreshed stale mastodon.md -> boosted starved drive order
  - `/home/seed/data/event_log.jsonl:236` refreshed stale mastodon.md -> boosted starved drive order

## script - refreshed stale mastodon.md -> flagged research for potential essay -> publishing streak at 170

- Count: 2
- Confidence: 0.27
- Evidence: stale (first cycle 412, latest cycle 414, age 243, expires cycle 614)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `refreshed stale mastodon.md -> flagged research for potential essay -> publishing streak at 170` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:76` refreshed stale mastodon.md -> flagged research for potential essay -> publishing streak at 170
  - `/home/seed/data/event_log.jsonl:78` refreshed stale mastodon.md -> flagged research for potential essay -> publishing streak at 170

## script - refreshed stale mastodon.md -> refreshed stale email.md -> boosted starved drive order

- Count: 2
- Confidence: 0.6
- Evidence: fresh (first cycle 356, latest cycle 649, age 8, expires cycle 849)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `refreshed stale mastodon.md -> refreshed stale email.md -> boosted starved drive order` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:20` refreshed stale mastodon.md -> refreshed stale email.md -> boosted starved drive order
  - `/home/seed/data/event_log.jsonl:293` refreshed stale mastodon.md -> refreshed stale email.md -> boosted starved drive order

## script - refreshed stale mastodon.md -> refreshed stale email.md -> publishing streak at 185

- Count: 2
- Confidence: 0.27
- Evidence: stale (first cycle 452, latest cycle 453, age 204, expires cycle 653)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `refreshed stale mastodon.md -> refreshed stale email.md -> publishing streak at 185` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:116` refreshed stale mastodon.md -> refreshed stale email.md -> publishing streak at 185
  - `/home/seed/data/event_log.jsonl:117` refreshed stale mastodon.md -> refreshed stale email.md -> publishing streak at 185

## script - refreshed stale mastodon.md -> refreshed stale email.md -> publishing streak at 215

- Count: 2
- Confidence: 0.45
- Evidence: aging (first cycle 494, latest cycle 495, age 162, expires cycle 695)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `refreshed stale mastodon.md -> refreshed stale email.md -> publishing streak at 215` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:158` refreshed stale mastodon.md -> refreshed stale email.md -> publishing streak at 215
  - `/home/seed/data/event_log.jsonl:159` refreshed stale mastodon.md -> refreshed stale email.md -> publishing streak at 215

## script - refreshed stale mastodon.md -> refreshed stale email.md -> publishing streak at 235

- Count: 2
- Confidence: 0.45
- Evidence: aging (first cycle 525, latest cycle 526, age 131, expires cycle 726)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `refreshed stale mastodon.md -> refreshed stale email.md -> publishing streak at 235` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:188` refreshed stale mastodon.md -> refreshed stale email.md -> publishing streak at 235
  - `/home/seed/data/event_log.jsonl:189` refreshed stale mastodon.md -> refreshed stale email.md -> publishing streak at 235

## script - refreshed stale mastodon.md -> refreshed stale email.md -> publishing streak at 240

- Count: 2
- Confidence: 0.45
- Evidence: aging (first cycle 536, latest cycle 538, age 119, expires cycle 738)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `refreshed stale mastodon.md -> refreshed stale email.md -> publishing streak at 240` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:199` refreshed stale mastodon.md -> refreshed stale email.md -> publishing streak at 240
  - `/home/seed/data/event_log.jsonl:201` refreshed stale mastodon.md -> refreshed stale email.md -> publishing streak at 240

## script - refreshed stale mastodon.md -> refreshed stale email.md -> publishing streak at 275

- Count: 2
- Confidence: 0.6
- Evidence: fresh (first cycle 606, latest cycle 607, age 50, expires cycle 807)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `refreshed stale mastodon.md -> refreshed stale email.md -> publishing streak at 275` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:251` refreshed stale mastodon.md -> refreshed stale email.md -> publishing streak at 275
  - `/home/seed/data/event_log.jsonl:252` refreshed stale mastodon.md -> refreshed stale email.md -> publishing streak at 275

## script - refreshed stale mastodon.md -> refreshed stale email.md -> publishing streak at 300

- Count: 2
- Confidence: 0.6
- Evidence: fresh (first cycle 648, latest cycle 648, age 9, expires cycle 848)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `refreshed stale mastodon.md -> refreshed stale email.md -> publishing streak at 300` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:291` refreshed stale mastodon.md -> refreshed stale email.md -> publishing streak at 300
  - `/home/seed/data/event_log.jsonl:292` refreshed stale mastodon.md -> refreshed stale email.md -> publishing streak at 300

## script - refreshed stale mastodon.md -> refreshed stale email.md -> research streak at 210

- Count: 2
- Confidence: 0.45
- Evidence: aging (first cycle 462, latest cycle 463, age 194, expires cycle 663)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `refreshed stale mastodon.md -> refreshed stale email.md -> research streak at 210` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:126` refreshed stale mastodon.md -> refreshed stale email.md -> research streak at 210
  - `/home/seed/data/event_log.jsonl:127` refreshed stale mastodon.md -> refreshed stale email.md -> research streak at 210

## script - refreshed stale mastodon.md -> refreshed stale email.md -> task_completion streak at 215

- Count: 2
- Confidence: 0.45
- Evidence: aging (first cycle 515, latest cycle 516, age 141, expires cycle 716)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `refreshed stale mastodon.md -> refreshed stale email.md -> task_completion streak at 215` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:178` refreshed stale mastodon.md -> refreshed stale email.md -> task_completion streak at 215
  - `/home/seed/data/event_log.jsonl:179` refreshed stale mastodon.md -> refreshed stale email.md -> task_completion streak at 215

## script - refreshed stale mastodon.md -> refreshed stale email.md -> version_control streak at 155

- Count: 2
- Confidence: 0.45
- Evidence: aging (first cycle 534, latest cycle 546, age 111, expires cycle 746)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `refreshed stale mastodon.md -> refreshed stale email.md -> version_control streak at 155` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:197` refreshed stale mastodon.md -> refreshed stale email.md -> version_control streak at 155
  - `/home/seed/data/event_log.jsonl:209` refreshed stale mastodon.md -> refreshed stale email.md -> version_control streak at 155

## script - refreshed stale mastodon.md -> refreshed stale email.md -> writing streak at 190

- Count: 2
- Confidence: 0.45
- Evidence: aging (first cycle 465, latest cycle 466, age 191, expires cycle 666)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `refreshed stale mastodon.md -> refreshed stale email.md -> writing streak at 190` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:129` refreshed stale mastodon.md -> refreshed stale email.md -> writing streak at 190
  - `/home/seed/data/event_log.jsonl:130` refreshed stale mastodon.md -> refreshed stale email.md -> writing streak at 190

## script - refreshed stale mastodon.md -> refreshed stale email.md -> writing streak at 285

- Count: 2
- Confidence: 0.6
- Evidence: fresh (first cycle 626, latest cycle 627, age 30, expires cycle 827)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `refreshed stale mastodon.md -> refreshed stale email.md -> writing streak at 285` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:270` refreshed stale mastodon.md -> refreshed stale email.md -> writing streak at 285
  - `/home/seed/data/event_log.jsonl:271` refreshed stale mastodon.md -> refreshed stale email.md -> writing streak at 285

## script - refreshed stale mastodon.md -> refreshed stale email.md -> writing streak at 300

- Count: 2
- Confidence: 0.6
- Evidence: fresh (first cycle 650, latest cycle 651, age 6, expires cycle 851)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `refreshed stale mastodon.md -> refreshed stale email.md -> writing streak at 300` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:294` refreshed stale mastodon.md -> refreshed stale email.md -> writing streak at 300
  - `/home/seed/data/event_log.jsonl:296` refreshed stale mastodon.md -> refreshed stale email.md -> writing streak at 300

## script - refreshed stale mastodon.md -> refreshed stale outreach.md

- Count: 2
- Confidence: 0.45
- Evidence: aging (first cycle 415, latest cycle 543, age 114, expires cycle 743)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `refreshed stale mastodon.md -> refreshed stale outreach.md` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:79` refreshed stale mastodon.md -> refreshed stale outreach.md
  - `/home/seed/data/event_log.jsonl:206` refreshed stale mastodon.md -> refreshed stale outreach.md

## script - refreshed stale mastodon.md -> refreshed stale trends.md -> refreshed stale outreach.md

- Count: 2
- Confidence: 0.45
- Evidence: aging (first cycle 427, latest cycle 556, age 101, expires cycle 756)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `refreshed stale mastodon.md -> refreshed stale trends.md -> refreshed stale outreach.md` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:91` refreshed stale mastodon.md -> refreshed stale trends.md -> refreshed stale outreach.md
  - `/home/seed/data/event_log.jsonl:219` refreshed stale mastodon.md -> refreshed stale trends.md -> refreshed stale outreach.md

## script - refreshed stale mastodon.md -> writing streak at 170

- Count: 2
- Confidence: 0.27
- Evidence: stale (first cycle 429, latest cycle 430, age 227, expires cycle 630)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `refreshed stale mastodon.md -> writing streak at 170` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:93` refreshed stale mastodon.md -> writing streak at 170
  - `/home/seed/data/event_log.jsonl:94` refreshed stale mastodon.md -> writing streak at 170

## script - refreshed stale mastodon.md -> writing streak at 265

- Count: 2
- Confidence: 0.45
- Evidence: aging (first cycle 593, latest cycle 594, age 63, expires cycle 794)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `refreshed stale mastodon.md -> writing streak at 265` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:238` refreshed stale mastodon.md -> writing streak at 265
  - `/home/seed/data/event_log.jsonl:239` refreshed stale mastodon.md -> writing streak at 265

## script - refreshed stale outreach.md -> boosted starved drive create -> boosted starved drive explore

- Count: 2
- Confidence: 0.6
- Evidence: fresh (first cycle 390, latest cycle 645, age 12, expires cycle 845)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `refreshed stale outreach.md -> boosted starved drive create -> boosted starved drive explore` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:54` refreshed stale outreach.md -> boosted starved drive create -> boosted starved drive explore
  - `/home/seed/data/event_log.jsonl:289` refreshed stale outreach.md -> boosted starved drive create -> boosted starved drive explore

## script - refreshed stale trends.md -> boosted starved drive create

- Count: 2
- Confidence: 0.27
- Evidence: stale (first cycle 359, latest cycle 407, age 250, expires cycle 607)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `refreshed stale trends.md -> boosted starved drive create` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:23` refreshed stale trends.md -> boosted starved drive create
  - `/home/seed/data/event_log.jsonl:71` refreshed stale trends.md -> boosted starved drive create

## script - refreshed stale trends.md -> refreshed stale outreach.md -> flagged research for potential essay

- Count: 2
- Confidence: 0.6
- Evidence: fresh (first cycle 535, latest cycle 634, age 23, expires cycle 834)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `refreshed stale trends.md -> refreshed stale outreach.md -> flagged research for potential essay` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:198` refreshed stale trends.md -> refreshed stale outreach.md -> flagged research for potential essay
  - `/home/seed/data/event_log.jsonl:278` refreshed stale trends.md -> refreshed stale outreach.md -> flagged research for potential essay

## script - research streak at 290 -> version_control streak at 155

- Count: 2
- Confidence: 0.45
- Evidence: aging (first cycle 543, latest cycle 544, age 113, expires cycle 744)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `research streak at 290 -> version_control streak at 155` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:206` research streak at 290 -> version_control streak at 155
  - `/home/seed/data/event_log.jsonl:207` research streak at 290 -> version_control streak at 155

## script - writing streak at 225 -> version_control streak at 155

- Count: 2
- Confidence: 0.45
- Evidence: aging (first cycle 516, latest cycle 517, age 140, expires cycle 717)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `writing streak at 225 -> version_control streak at 155` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:179` writing streak at 225 -> version_control streak at 155
  - `/home/seed/data/event_log.jsonl:180` writing streak at 225 -> version_control streak at 155

## typed_tool - deployed tool-latency-is-organisational-memory-loss

- Count: 2
- Confidence: 0.31
- Evidence: stale (first cycle 395, latest cycle 396, age 261, expires cycle 596)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Suggested test: Add schema validation and receipt checks for `deployed tool-latency-is-organisational-memory-loss`.
- Examples:
  - `/home/seed/data/event_log.jsonl:59` deployed tool-latency-is-organisational-memory-loss
  - `/home/seed/data/event_log.jsonl:60` deployed tool-latency-is-organisational-memory-loss
