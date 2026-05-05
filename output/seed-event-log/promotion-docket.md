# Promotion Docket

Events scanned: 2000
Promotion candidates: 295

## Summary

- `fixture`: 79
- `script`: 215
- `typed_tool`: 1

## fixture - refreshed stale mastodon.md

- Count: 247
- Confidence: 0.95
- Risk: medium
- Suggested test: Add positive and negative evidence cases for `refreshed stale mastodon.md`.
- Examples:
  - `/home/seed/data/event_log.jsonl:1` refreshed stale mastodon.md
  - `/home/seed/data/event_log.jsonl:2` refreshed stale mastodon.md
  - `/home/seed/data/event_log.jsonl:3` refreshed stale mastodon.md
  - `/home/seed/data/event_log.jsonl:4` refreshed stale mastodon.md
  - `/home/seed/data/event_log.jsonl:5` refreshed stale mastodon.md

## fixture - refreshed stale email.md

- Count: 212
- Confidence: 0.95
- Risk: medium
- Suggested test: Add positive and negative evidence cases for `refreshed stale email.md`.
- Examples:
  - `/home/seed/data/event_log.jsonl:1` refreshed stale email.md
  - `/home/seed/data/event_log.jsonl:2` refreshed stale email.md
  - `/home/seed/data/event_log.jsonl:3` refreshed stale email.md
  - `/home/seed/data/event_log.jsonl:4` refreshed stale email.md
  - `/home/seed/data/event_log.jsonl:5` refreshed stale email.md

## script - refreshed stale mastodon.md -> refreshed stale email.md

- Count: 207
- Confidence: 0.95
- Risk: medium
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
- Risk: medium
- Suggested test: Add positive and negative evidence cases for `compacted memory (202 lines)`.
- Examples:
  - `/home/seed/data/event_log.jsonl:1` compacted memory (202 lines)
  - `/home/seed/data/event_log.jsonl:3` compacted memory (202 lines)
  - `/home/seed/data/event_log.jsonl:4` compacted memory (202 lines)
  - `/home/seed/data/event_log.jsonl:5` compacted memory (202 lines)
  - `/home/seed/data/event_log.jsonl:6` compacted memory (202 lines)

## fixture - posted to mastodon

- Count: 151
- Confidence: 0.95
- Risk: medium
- Suggested test: Add positive and negative evidence cases for `posted to mastodon`.
- Examples:
  - `/home/seed/data/event_log.jsonl:6` posted to Mastodon
  - `/home/seed/data/event_log.jsonl:7` posted to Mastodon
  - `/home/seed/data/event_log.jsonl:8` posted to Mastodon
  - `/home/seed/data/event_log.jsonl:9` posted to Mastodon
  - `/home/seed/data/event_log.jsonl:13` posted to Mastodon

## fixture - rebuilt feeds

- Count: 151
- Confidence: 0.95
- Risk: medium
- Suggested test: Add positive and negative evidence cases for `rebuilt feeds`.
- Examples:
  - `/home/seed/data/event_log.jsonl:6` rebuilt feeds
  - `/home/seed/data/event_log.jsonl:7` rebuilt feeds
  - `/home/seed/data/event_log.jsonl:8` rebuilt feeds
  - `/home/seed/data/event_log.jsonl:9` rebuilt feeds
  - `/home/seed/data/event_log.jsonl:13` rebuilt feeds

## script - posted to mastodon -> rebuilt feeds

- Count: 151
- Confidence: 0.95
- Risk: medium
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
- Risk: medium
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
- Risk: medium
- Suggested test: Add a fixture proving `compacted memory (202 lines) -> refreshed stale mastodon.md -> refreshed stale email.md` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:1` compacted memory (202 lines) -> refreshed stale mastodon.md -> refreshed stale email.md
  - `/home/seed/data/event_log.jsonl:3` compacted memory (202 lines) -> refreshed stale mastodon.md -> refreshed stale email.md
  - `/home/seed/data/event_log.jsonl:4` compacted memory (202 lines) -> refreshed stale mastodon.md -> refreshed stale email.md
  - `/home/seed/data/event_log.jsonl:5` compacted memory (202 lines) -> refreshed stale mastodon.md -> refreshed stale email.md
  - `/home/seed/data/event_log.jsonl:7` compacted memory (202 lines) -> refreshed stale mastodon.md -> refreshed stale email.md

## fixture - boosted starved drive create

- Count: 76
- Confidence: 0.95
- Risk: medium
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
- Risk: medium
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
- Risk: medium
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
- Risk: medium
- Suggested test: Add a fixture proving `rebuilt feeds -> compacted memory (202 lines)` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:7` rebuilt feeds -> compacted memory (202 lines)
  - `/home/seed/data/event_log.jsonl:8` rebuilt feeds -> compacted memory (202 lines)
  - `/home/seed/data/event_log.jsonl:9` rebuilt feeds -> compacted memory (202 lines)
  - `/home/seed/data/event_log.jsonl:14` rebuilt feeds -> compacted memory (202 lines)
  - `/home/seed/data/event_log.jsonl:21` rebuilt feeds -> compacted memory (202 lines)

## script - rebuilt feeds -> compacted memory (202 lines) -> refreshed stale mastodon.md

- Count: 68
- Confidence: 0.95
- Risk: medium
- Suggested test: Add a fixture proving `rebuilt feeds -> compacted memory (202 lines) -> refreshed stale mastodon.md` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:7` rebuilt feeds -> compacted memory (202 lines) -> refreshed stale mastodon.md
  - `/home/seed/data/event_log.jsonl:8` rebuilt feeds -> compacted memory (202 lines) -> refreshed stale mastodon.md
  - `/home/seed/data/event_log.jsonl:9` rebuilt feeds -> compacted memory (202 lines) -> refreshed stale mastodon.md
  - `/home/seed/data/event_log.jsonl:14` rebuilt feeds -> compacted memory (202 lines) -> refreshed stale mastodon.md
  - `/home/seed/data/event_log.jsonl:21` rebuilt feeds -> compacted memory (202 lines) -> refreshed stale mastodon.md

## script - refreshed stale email.md -> boosted starved drive create

- Count: 68
- Confidence: 0.95
- Risk: medium
- Suggested test: Add a fixture proving `refreshed stale email.md -> boosted starved drive create` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:1` refreshed stale email.md -> boosted starved drive create
  - `/home/seed/data/event_log.jsonl:2` refreshed stale email.md -> boosted starved drive create
  - `/home/seed/data/event_log.jsonl:3` refreshed stale email.md -> boosted starved drive create
  - `/home/seed/data/event_log.jsonl:5` refreshed stale email.md -> boosted starved drive create
  - `/home/seed/data/event_log.jsonl:6` refreshed stale email.md -> boosted starved drive create

## script - refreshed stale mastodon.md -> refreshed stale email.md -> boosted starved drive create

- Count: 68
- Confidence: 0.95
- Risk: medium
- Suggested test: Add a fixture proving `refreshed stale mastodon.md -> refreshed stale email.md -> boosted starved drive create` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:1` refreshed stale mastodon.md -> refreshed stale email.md -> boosted starved drive create
  - `/home/seed/data/event_log.jsonl:2` refreshed stale mastodon.md -> refreshed stale email.md -> boosted starved drive create
  - `/home/seed/data/event_log.jsonl:3` refreshed stale mastodon.md -> refreshed stale email.md -> boosted starved drive create
  - `/home/seed/data/event_log.jsonl:5` refreshed stale mastodon.md -> refreshed stale email.md -> boosted starved drive create
  - `/home/seed/data/event_log.jsonl:6` refreshed stale mastodon.md -> refreshed stale email.md -> boosted starved drive create

## fixture - logged bug + added fix task

- Count: 67
- Confidence: 0.95
- Risk: medium
- Suggested test: Add positive and negative evidence cases for `logged bug + added fix task`.
- Examples:
  - `/home/seed/data/event_log.jsonl:6` logged bug + added fix task
  - `/home/seed/data/event_log.jsonl:10` logged bug + added fix task
  - `/home/seed/data/event_log.jsonl:11` logged bug + added fix task
  - `/home/seed/data/event_log.jsonl:13` logged bug + added fix task
  - `/home/seed/data/event_log.jsonl:16` logged bug + added fix task

## fixture - boosted starved drive explore

- Count: 61
- Confidence: 0.95
- Risk: medium
- Suggested test: Add positive and negative evidence cases for `boosted starved drive explore`.
- Examples:
  - `/home/seed/data/event_log.jsonl:32` boosted starved drive explore
  - `/home/seed/data/event_log.jsonl:33` boosted starved drive explore
  - `/home/seed/data/event_log.jsonl:34` boosted starved drive explore
  - `/home/seed/data/event_log.jsonl:35` boosted starved drive explore
  - `/home/seed/data/event_log.jsonl:36` boosted starved drive explore

## fixture - boosted starved drive order

- Count: 49
- Confidence: 0.95
- Risk: medium
- Suggested test: Add positive and negative evidence cases for `boosted starved drive order`.
- Examples:
  - `/home/seed/data/event_log.jsonl:1` boosted starved drive order
  - `/home/seed/data/event_log.jsonl:2` boosted starved drive order
  - `/home/seed/data/event_log.jsonl:7` boosted starved drive order
  - `/home/seed/data/event_log.jsonl:10` boosted starved drive order
  - `/home/seed/data/event_log.jsonl:12` boosted starved drive order

## script - logged bug + added fix task -> compacted memory (202 lines)

- Count: 47
- Confidence: 0.95
- Risk: medium
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
- Risk: medium
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
- Risk: medium
- Suggested test: Add a fixture proving `boosted starved drive express -> boosted starved drive order` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:1` boosted starved drive express -> boosted starved drive order
  - `/home/seed/data/event_log.jsonl:2` boosted starved drive express -> boosted starved drive order
  - `/home/seed/data/event_log.jsonl:7` boosted starved drive express -> boosted starved drive order
  - `/home/seed/data/event_log.jsonl:10` boosted starved drive express -> boosted starved drive order
  - `/home/seed/data/event_log.jsonl:12` boosted starved drive express -> boosted starved drive order

## script - posted to mastodon -> rebuilt feeds -> logged bug + added fix task

- Count: 45
- Confidence: 0.95
- Risk: medium
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
- Risk: medium
- Suggested test: Add a fixture proving `rebuilt feeds -> logged bug + added fix task` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:6` rebuilt feeds -> logged bug + added fix task
  - `/home/seed/data/event_log.jsonl:13` rebuilt feeds -> logged bug + added fix task
  - `/home/seed/data/event_log.jsonl:17` rebuilt feeds -> logged bug + added fix task
  - `/home/seed/data/event_log.jsonl:18` rebuilt feeds -> logged bug + added fix task
  - `/home/seed/data/event_log.jsonl:22` rebuilt feeds -> logged bug + added fix task

## fixture - flagged research for potential essay

- Count: 42
- Confidence: 0.95
- Risk: medium
- Suggested test: Add positive and negative evidence cases for `flagged research for potential essay`.
- Examples:
  - `/home/seed/data/event_log.jsonl:1` flagged research for potential essay
  - `/home/seed/data/event_log.jsonl:2` flagged research for potential essay
  - `/home/seed/data/event_log.jsonl:9` flagged research for potential essay
  - `/home/seed/data/event_log.jsonl:10` flagged research for potential essay
  - `/home/seed/data/event_log.jsonl:14` flagged research for potential essay

## script - boosted starved drive create -> boosted starved drive explore

- Count: 42
- Confidence: 0.95
- Risk: medium
- Suggested test: Add a fixture proving `boosted starved drive create -> boosted starved drive explore` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:32` boosted starved drive create -> boosted starved drive explore
  - `/home/seed/data/event_log.jsonl:33` boosted starved drive create -> boosted starved drive explore
  - `/home/seed/data/event_log.jsonl:34` boosted starved drive create -> boosted starved drive explore
  - `/home/seed/data/event_log.jsonl:35` boosted starved drive create -> boosted starved drive explore
  - `/home/seed/data/event_log.jsonl:36` boosted starved drive create -> boosted starved drive explore

## fixture - archived completed tasks

- Count: 39
- Confidence: 0.95
- Risk: medium
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
- Risk: medium
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
- Risk: medium
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
- Risk: medium
- Suggested test: Add a fixture proving `boosted starved drive understand -> boosted starved drive express` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:32` boosted starved drive understand -> boosted starved drive express
  - `/home/seed/data/event_log.jsonl:33` boosted starved drive understand -> boosted starved drive express
  - `/home/seed/data/event_log.jsonl:34` boosted starved drive understand -> boosted starved drive express
  - `/home/seed/data/event_log.jsonl:35` boosted starved drive understand -> boosted starved drive express
  - `/home/seed/data/event_log.jsonl:36` boosted starved drive understand -> boosted starved drive express

## script - logged bug + added fix task -> compacted memory (202 lines) -> refreshed stale mastodon.md

- Count: 38
- Confidence: 0.95
- Risk: medium
- Suggested test: Add a fixture proving `logged bug + added fix task -> compacted memory (202 lines) -> refreshed stale mastodon.md` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:10` logged bug + added fix task -> compacted memory (202 lines) -> refreshed stale mastodon.md
  - `/home/seed/data/event_log.jsonl:11` logged bug + added fix task -> compacted memory (202 lines) -> refreshed stale mastodon.md
  - `/home/seed/data/event_log.jsonl:17` logged bug + added fix task -> compacted memory (202 lines) -> refreshed stale mastodon.md
  - `/home/seed/data/event_log.jsonl:20` logged bug + added fix task -> compacted memory (202 lines) -> refreshed stale mastodon.md
  - `/home/seed/data/event_log.jsonl:22` logged bug + added fix task -> compacted memory (202 lines) -> refreshed stale mastodon.md

## script - refreshed stale email.md -> boosted starved drive create -> boosted starved drive explore

- Count: 37
- Confidence: 0.95
- Risk: medium
- Suggested test: Add a fixture proving `refreshed stale email.md -> boosted starved drive create -> boosted starved drive explore` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:32` refreshed stale email.md -> boosted starved drive create -> boosted starved drive explore
  - `/home/seed/data/event_log.jsonl:33` refreshed stale email.md -> boosted starved drive create -> boosted starved drive explore
  - `/home/seed/data/event_log.jsonl:34` refreshed stale email.md -> boosted starved drive create -> boosted starved drive explore
  - `/home/seed/data/event_log.jsonl:35` refreshed stale email.md -> boosted starved drive create -> boosted starved drive explore
  - `/home/seed/data/event_log.jsonl:36` refreshed stale email.md -> boosted starved drive create -> boosted starved drive explore

## fixture - compacted memory (201 lines)

- Count: 34
- Confidence: 0.95
- Risk: medium
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
- Risk: medium
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
- Risk: medium
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
- Risk: medium
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
- Risk: medium
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
- Risk: medium
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
- Risk: medium
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
- Risk: medium
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
- Risk: medium
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
- Risk: medium
- Suggested test: Add a fixture proving `refreshed stale email.md -> boosted starved drive create -> boosted starved drive express` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:1` refreshed stale email.md -> boosted starved drive create -> boosted starved drive express
  - `/home/seed/data/event_log.jsonl:2` refreshed stale email.md -> boosted starved drive create -> boosted starved drive express
  - `/home/seed/data/event_log.jsonl:3` refreshed stale email.md -> boosted starved drive create -> boosted starved drive express
  - `/home/seed/data/event_log.jsonl:5` refreshed stale email.md -> boosted starved drive create -> boosted starved drive express
  - `/home/seed/data/event_log.jsonl:6` refreshed stale email.md -> boosted starved drive create -> boosted starved drive express

## script - boosted starved drive explore -> boosted starved drive understand

- Count: 24
- Confidence: 0.95
- Risk: medium
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
- Risk: medium
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
- Risk: medium
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
- Risk: medium
- Suggested test: Add a fixture proving `boosted starved drive create -> boosted starved drive explore -> boosted starved drive understand` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:32` boosted starved drive create -> boosted starved drive explore -> boosted starved drive understand
  - `/home/seed/data/event_log.jsonl:33` boosted starved drive create -> boosted starved drive explore -> boosted starved drive understand
  - `/home/seed/data/event_log.jsonl:34` boosted starved drive create -> boosted starved drive explore -> boosted starved drive understand
  - `/home/seed/data/event_log.jsonl:35` boosted starved drive create -> boosted starved drive explore -> boosted starved drive understand
  - `/home/seed/data/event_log.jsonl:36` boosted starved drive create -> boosted starved drive explore -> boosted starved drive understand

## fixture - refreshed stale trends.md

- Count: 21
- Confidence: 0.95
- Risk: medium
- Suggested test: Add positive and negative evidence cases for `refreshed stale trends.md`.
- Examples:
  - `/home/seed/data/event_log.jsonl:4` refreshed stale trends.md
  - `/home/seed/data/event_log.jsonl:23` refreshed stale trends.md
  - `/home/seed/data/event_log.jsonl:54` refreshed stale trends.md
  - `/home/seed/data/event_log.jsonl:71` refreshed stale trends.md
  - `/home/seed/data/event_log.jsonl:91` refreshed stale trends.md

## fixture - refreshed stale outreach.md

- Count: 19
- Confidence: 0.95
- Risk: medium
- Suggested test: Add positive and negative evidence cases for `refreshed stale outreach.md`.
- Examples:
  - `/home/seed/data/event_log.jsonl:4` refreshed stale outreach.md
  - `/home/seed/data/event_log.jsonl:31` refreshed stale outreach.md
  - `/home/seed/data/event_log.jsonl:54` refreshed stale outreach.md
  - `/home/seed/data/event_log.jsonl:79` refreshed stale outreach.md
  - `/home/seed/data/event_log.jsonl:91` refreshed stale outreach.md

## script - boosted starved drive create -> boosted starved drive explore -> boosted starved drive preserve

- Count: 18
- Confidence: 0.95
- Risk: medium
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
- Risk: medium
- Suggested test: Add a fixture proving `boosted starved drive explore -> boosted starved drive preserve` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:45` boosted starved drive explore -> boosted starved drive preserve
  - `/home/seed/data/event_log.jsonl:48` boosted starved drive explore -> boosted starved drive preserve
  - `/home/seed/data/event_log.jsonl:51` boosted starved drive explore -> boosted starved drive preserve
  - `/home/seed/data/event_log.jsonl:52` boosted starved drive explore -> boosted starved drive preserve
  - `/home/seed/data/event_log.jsonl:53` boosted starved drive explore -> boosted starved drive preserve

## script - refreshed stale email.md -> refreshed stale trends.md

- Count: 17
- Confidence: 0.95
- Risk: medium
- Suggested test: Add a fixture proving `refreshed stale email.md -> refreshed stale trends.md` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:4` refreshed stale email.md -> refreshed stale trends.md
  - `/home/seed/data/event_log.jsonl:23` refreshed stale email.md -> refreshed stale trends.md
  - `/home/seed/data/event_log.jsonl:54` refreshed stale email.md -> refreshed stale trends.md
  - `/home/seed/data/event_log.jsonl:71` refreshed stale email.md -> refreshed stale trends.md
  - `/home/seed/data/event_log.jsonl:99` refreshed stale email.md -> refreshed stale trends.md

## script - refreshed stale mastodon.md -> refreshed stale email.md -> refreshed stale trends.md

- Count: 17
- Confidence: 0.95
- Risk: medium
- Suggested test: Add a fixture proving `refreshed stale mastodon.md -> refreshed stale email.md -> refreshed stale trends.md` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:4` refreshed stale mastodon.md -> refreshed stale email.md -> refreshed stale trends.md
  - `/home/seed/data/event_log.jsonl:23` refreshed stale mastodon.md -> refreshed stale email.md -> refreshed stale trends.md
  - `/home/seed/data/event_log.jsonl:54` refreshed stale mastodon.md -> refreshed stale email.md -> refreshed stale trends.md
  - `/home/seed/data/event_log.jsonl:71` refreshed stale mastodon.md -> refreshed stale email.md -> refreshed stale trends.md
  - `/home/seed/data/event_log.jsonl:99` refreshed stale mastodon.md -> refreshed stale email.md -> refreshed stale trends.md

## script - refreshed stale email.md -> flagged research for potential essay

- Count: 16
- Confidence: 0.95
- Risk: medium
- Suggested test: Add a fixture proving `refreshed stale email.md -> flagged research for potential essay` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:15` refreshed stale email.md -> flagged research for potential essay
  - `/home/seed/data/event_log.jsonl:88` refreshed stale email.md -> flagged research for potential essay
  - `/home/seed/data/event_log.jsonl:98` refreshed stale email.md -> flagged research for potential essay
  - `/home/seed/data/event_log.jsonl:108` refreshed stale email.md -> flagged research for potential essay
  - `/home/seed/data/event_log.jsonl:118` refreshed stale email.md -> flagged research for potential essay

## script - boosted starved drive explore -> boosted starved drive preserve -> boosted starved drive understand

- Count: 15
- Confidence: 0.95
- Risk: medium
- Suggested test: Add a fixture proving `boosted starved drive explore -> boosted starved drive preserve -> boosted starved drive understand` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:45` boosted starved drive explore -> boosted starved drive preserve -> boosted starved drive understand
  - `/home/seed/data/event_log.jsonl:48` boosted starved drive explore -> boosted starved drive preserve -> boosted starved drive understand
  - `/home/seed/data/event_log.jsonl:51` boosted starved drive explore -> boosted starved drive preserve -> boosted starved drive understand
  - `/home/seed/data/event_log.jsonl:52` boosted starved drive explore -> boosted starved drive preserve -> boosted starved drive understand
  - `/home/seed/data/event_log.jsonl:53` boosted starved drive explore -> boosted starved drive preserve -> boosted starved drive understand

## script - boosted starved drive preserve -> boosted starved drive understand

- Count: 15
- Confidence: 0.95
- Risk: medium
- Suggested test: Add a fixture proving `boosted starved drive preserve -> boosted starved drive understand` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:45` boosted starved drive preserve -> boosted starved drive understand
  - `/home/seed/data/event_log.jsonl:48` boosted starved drive preserve -> boosted starved drive understand
  - `/home/seed/data/event_log.jsonl:51` boosted starved drive preserve -> boosted starved drive understand
  - `/home/seed/data/event_log.jsonl:52` boosted starved drive preserve -> boosted starved drive understand
  - `/home/seed/data/event_log.jsonl:53` boosted starved drive preserve -> boosted starved drive understand

## script - boosted starved drive preserve -> boosted starved drive understand -> boosted starved drive express

- Count: 15
- Confidence: 0.95
- Risk: medium
- Suggested test: Add a fixture proving `boosted starved drive preserve -> boosted starved drive understand -> boosted starved drive express` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:45` boosted starved drive preserve -> boosted starved drive understand -> boosted starved drive express
  - `/home/seed/data/event_log.jsonl:48` boosted starved drive preserve -> boosted starved drive understand -> boosted starved drive express
  - `/home/seed/data/event_log.jsonl:51` boosted starved drive preserve -> boosted starved drive understand -> boosted starved drive express
  - `/home/seed/data/event_log.jsonl:52` boosted starved drive preserve -> boosted starved drive understand -> boosted starved drive express
  - `/home/seed/data/event_log.jsonl:53` boosted starved drive preserve -> boosted starved drive understand -> boosted starved drive express

## script - refreshed stale email.md -> boosted starved drive explore

- Count: 15
- Confidence: 0.95
- Risk: medium
- Suggested test: Add a fixture proving `refreshed stale email.md -> boosted starved drive explore` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:58` refreshed stale email.md -> boosted starved drive explore
  - `/home/seed/data/event_log.jsonl:101` refreshed stale email.md -> boosted starved drive explore
  - `/home/seed/data/event_log.jsonl:107` refreshed stale email.md -> boosted starved drive explore
  - `/home/seed/data/event_log.jsonl:109` refreshed stale email.md -> boosted starved drive explore
  - `/home/seed/data/event_log.jsonl:121` refreshed stale email.md -> boosted starved drive explore

## script - refreshed stale mastodon.md -> refreshed stale email.md -> boosted starved drive explore

- Count: 15
- Confidence: 0.95
- Risk: medium
- Suggested test: Add a fixture proving `refreshed stale mastodon.md -> refreshed stale email.md -> boosted starved drive explore` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:58` refreshed stale mastodon.md -> refreshed stale email.md -> boosted starved drive explore
  - `/home/seed/data/event_log.jsonl:101` refreshed stale mastodon.md -> refreshed stale email.md -> boosted starved drive explore
  - `/home/seed/data/event_log.jsonl:107` refreshed stale mastodon.md -> refreshed stale email.md -> boosted starved drive explore
  - `/home/seed/data/event_log.jsonl:109` refreshed stale mastodon.md -> refreshed stale email.md -> boosted starved drive explore
  - `/home/seed/data/event_log.jsonl:121` refreshed stale mastodon.md -> refreshed stale email.md -> boosted starved drive explore

## script - refreshed stale mastodon.md -> refreshed stale email.md -> flagged research for potential essay

- Count: 15
- Confidence: 0.95
- Risk: medium
- Suggested test: Add a fixture proving `refreshed stale mastodon.md -> refreshed stale email.md -> flagged research for potential essay` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:15` refreshed stale mastodon.md -> refreshed stale email.md -> flagged research for potential essay
  - `/home/seed/data/event_log.jsonl:98` refreshed stale mastodon.md -> refreshed stale email.md -> flagged research for potential essay
  - `/home/seed/data/event_log.jsonl:108` refreshed stale mastodon.md -> refreshed stale email.md -> flagged research for potential essay
  - `/home/seed/data/event_log.jsonl:118` refreshed stale mastodon.md -> refreshed stale email.md -> flagged research for potential essay
  - `/home/seed/data/event_log.jsonl:128` refreshed stale mastodon.md -> refreshed stale email.md -> flagged research for potential essay

## script - boosted starved drive create -> boosted starved drive express -> boosted starved drive order

- Count: 14
- Confidence: 0.95
- Risk: medium
- Suggested test: Add a fixture proving `boosted starved drive create -> boosted starved drive express -> boosted starved drive order` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:1` boosted starved drive create -> boosted starved drive express -> boosted starved drive order
  - `/home/seed/data/event_log.jsonl:2` boosted starved drive create -> boosted starved drive express -> boosted starved drive order
  - `/home/seed/data/event_log.jsonl:7` boosted starved drive create -> boosted starved drive express -> boosted starved drive order
  - `/home/seed/data/event_log.jsonl:10` boosted starved drive create -> boosted starved drive express -> boosted starved drive order
  - `/home/seed/data/event_log.jsonl:12` boosted starved drive create -> boosted starved drive express -> boosted starved drive order

## fixture - task_completion streak at 170

- Count: 13
- Confidence: 0.95
- Risk: medium
- Suggested test: Add positive and negative evidence cases for `task_completion streak at 170`.
- Examples:
  - `/home/seed/data/event_log.jsonl:74` task_completion streak at 170
  - `/home/seed/data/event_log.jsonl:75` task_completion streak at 170
  - `/home/seed/data/event_log.jsonl:76` task_completion streak at 170
  - `/home/seed/data/event_log.jsonl:77` task_completion streak at 170
  - `/home/seed/data/event_log.jsonl:78` task_completion streak at 170

## fixture - boosted starved drive connect

- Count: 12
- Confidence: 0.95
- Risk: medium
- Suggested test: Add positive and negative evidence cases for `boosted starved drive connect`.
- Examples:
  - `/home/seed/data/event_log.jsonl:104` boosted starved drive connect
  - `/home/seed/data/event_log.jsonl:114` boosted starved drive connect
  - `/home/seed/data/event_log.jsonl:121` boosted starved drive connect
  - `/home/seed/data/event_log.jsonl:135` boosted starved drive connect
  - `/home/seed/data/event_log.jsonl:150` boosted starved drive connect

## fixture - publishing streak at 170

- Count: 12
- Confidence: 0.95
- Risk: medium
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
- Risk: medium
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
- Risk: medium
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
- Risk: medium
- Suggested test: Add a fixture proving `logged bug + added fix task -> compacted memory (201 lines) -> refreshed stale mastodon.md` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:13` logged bug + added fix task -> compacted memory (201 lines) -> refreshed stale mastodon.md
  - `/home/seed/data/event_log.jsonl:16` logged bug + added fix task -> compacted memory (201 lines) -> refreshed stale mastodon.md
  - `/home/seed/data/event_log.jsonl:18` logged bug + added fix task -> compacted memory (201 lines) -> refreshed stale mastodon.md
  - `/home/seed/data/event_log.jsonl:46` logged bug + added fix task -> compacted memory (201 lines) -> refreshed stale mastodon.md
  - `/home/seed/data/event_log.jsonl:63` logged bug + added fix task -> compacted memory (201 lines) -> refreshed stale mastodon.md

## script - publishing streak at 170 -> task_completion streak at 170

- Count: 12
- Confidence: 0.95
- Risk: medium
- Suggested test: Add a fixture proving `publishing streak at 170 -> task_completion streak at 170` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:74` publishing streak at 170 -> task_completion streak at 170
  - `/home/seed/data/event_log.jsonl:75` publishing streak at 170 -> task_completion streak at 170
  - `/home/seed/data/event_log.jsonl:76` publishing streak at 170 -> task_completion streak at 170
  - `/home/seed/data/event_log.jsonl:77` publishing streak at 170 -> task_completion streak at 170
  - `/home/seed/data/event_log.jsonl:78` publishing streak at 170 -> task_completion streak at 170

## script - posted to mastodon -> rebuilt feeds -> compacted memory (201 lines)

- Count: 11
- Confidence: 0.95
- Risk: medium
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
- Risk: medium
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
- Risk: medium
- Suggested test: Add a fixture proving `rebuilt feeds -> compacted memory (201 lines) -> refreshed stale mastodon.md` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:28` rebuilt feeds -> compacted memory (201 lines) -> refreshed stale mastodon.md
  - `/home/seed/data/event_log.jsonl:34` rebuilt feeds -> compacted memory (201 lines) -> refreshed stale mastodon.md
  - `/home/seed/data/event_log.jsonl:71` rebuilt feeds -> compacted memory (201 lines) -> refreshed stale mastodon.md
  - `/home/seed/data/event_log.jsonl:82` rebuilt feeds -> compacted memory (201 lines) -> refreshed stale mastodon.md
  - `/home/seed/data/event_log.jsonl:104` rebuilt feeds -> compacted memory (201 lines) -> refreshed stale mastodon.md

## script - refreshed stale trends.md -> refreshed stale outreach.md

- Count: 11
- Confidence: 0.95
- Risk: medium
- Suggested test: Add a fixture proving `refreshed stale trends.md -> refreshed stale outreach.md` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:4` refreshed stale trends.md -> refreshed stale outreach.md
  - `/home/seed/data/event_log.jsonl:54` refreshed stale trends.md -> refreshed stale outreach.md
  - `/home/seed/data/event_log.jsonl:91` refreshed stale trends.md -> refreshed stale outreach.md
  - `/home/seed/data/event_log.jsonl:111` refreshed stale trends.md -> refreshed stale outreach.md
  - `/home/seed/data/event_log.jsonl:133` refreshed stale trends.md -> refreshed stale outreach.md

## fixture - broke idle — boosted create + added urgent write task

- Count: 10
- Confidence: 0.95
- Risk: medium
- Suggested test: Add positive and negative evidence cases for `broke idle — boosted create + added urgent write task`.
- Examples:
  - `/home/seed/data/event_log.jsonl:5` broke idle — boosted create + added urgent write task
  - `/home/seed/data/event_log.jsonl:6` broke idle — boosted create + added urgent write task
  - `/home/seed/data/event_log.jsonl:57` broke idle — boosted create + added urgent write task
  - `/home/seed/data/event_log.jsonl:58` broke idle — boosted create + added urgent write task
  - `/home/seed/data/event_log.jsonl:88` broke idle — boosted create + added urgent write task

## script - boosted starved drive express -> boosted starved drive order -> flagged research for potential essay

- Count: 10
- Confidence: 0.95
- Risk: medium
- Suggested test: Add a fixture proving `boosted starved drive express -> boosted starved drive order -> flagged research for potential essay` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:1` boosted starved drive express -> boosted starved drive order -> flagged research for potential essay
  - `/home/seed/data/event_log.jsonl:2` boosted starved drive express -> boosted starved drive order -> flagged research for potential essay
  - `/home/seed/data/event_log.jsonl:10` boosted starved drive express -> boosted starved drive order -> flagged research for potential essay
  - `/home/seed/data/event_log.jsonl:19` boosted starved drive express -> boosted starved drive order -> flagged research for potential essay
  - `/home/seed/data/event_log.jsonl:25` boosted starved drive express -> boosted starved drive order -> flagged research for potential essay

## fixture - version_control streak at 150

- Count: 9
- Confidence: 0.95
- Risk: medium
- Suggested test: Add positive and negative evidence cases for `version_control streak at 150`.
- Examples:
  - `/home/seed/data/event_log.jsonl:108` version_control streak at 150
  - `/home/seed/data/event_log.jsonl:109` version_control streak at 150
  - `/home/seed/data/event_log.jsonl:110` version_control streak at 150
  - `/home/seed/data/event_log.jsonl:111` version_control streak at 150
  - `/home/seed/data/event_log.jsonl:112` version_control streak at 150

## script - posted to mastodon -> rebuilt feeds -> refreshed stale mastodon.md

- Count: 9
- Confidence: 0.95
- Risk: medium
- Suggested test: Add a fixture proving `posted to mastodon -> rebuilt feeds -> refreshed stale mastodon.md` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:225` posted to Mastodon -> rebuilt feeds -> refreshed stale mastodon.md
  - `/home/seed/data/event_log.jsonl:226` posted to Mastodon -> rebuilt feeds -> refreshed stale mastodon.md
  - `/home/seed/data/event_log.jsonl:227` posted to Mastodon -> rebuilt feeds -> refreshed stale mastodon.md
  - `/home/seed/data/event_log.jsonl:229` posted to Mastodon -> rebuilt feeds -> refreshed stale mastodon.md
  - `/home/seed/data/event_log.jsonl:247` posted to Mastodon -> rebuilt feeds -> refreshed stale mastodon.md

## script - rebuilt feeds -> logged bug + added fix task -> compacted memory (201 lines)

- Count: 9
- Confidence: 0.95
- Risk: medium
- Suggested test: Add a fixture proving `rebuilt feeds -> logged bug + added fix task -> compacted memory (201 lines)` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:13` rebuilt feeds -> logged bug + added fix task -> compacted memory (201 lines)
  - `/home/seed/data/event_log.jsonl:18` rebuilt feeds -> logged bug + added fix task -> compacted memory (201 lines)
  - `/home/seed/data/event_log.jsonl:46` rebuilt feeds -> logged bug + added fix task -> compacted memory (201 lines)
  - `/home/seed/data/event_log.jsonl:63` rebuilt feeds -> logged bug + added fix task -> compacted memory (201 lines)
  - `/home/seed/data/event_log.jsonl:129` rebuilt feeds -> logged bug + added fix task -> compacted memory (201 lines)

## script - rebuilt feeds -> refreshed stale mastodon.md

- Count: 9
- Confidence: 0.95
- Risk: medium
- Suggested test: Add a fixture proving `rebuilt feeds -> refreshed stale mastodon.md` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:225` rebuilt feeds -> refreshed stale mastodon.md
  - `/home/seed/data/event_log.jsonl:226` rebuilt feeds -> refreshed stale mastodon.md
  - `/home/seed/data/event_log.jsonl:227` rebuilt feeds -> refreshed stale mastodon.md
  - `/home/seed/data/event_log.jsonl:229` rebuilt feeds -> refreshed stale mastodon.md
  - `/home/seed/data/event_log.jsonl:247` rebuilt feeds -> refreshed stale mastodon.md

## script - rebuilt feeds -> refreshed stale mastodon.md -> refreshed stale email.md

- Count: 9
- Confidence: 0.95
- Risk: medium
- Suggested test: Add a fixture proving `rebuilt feeds -> refreshed stale mastodon.md -> refreshed stale email.md` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:225` rebuilt feeds -> refreshed stale mastodon.md -> refreshed stale email.md
  - `/home/seed/data/event_log.jsonl:226` rebuilt feeds -> refreshed stale mastodon.md -> refreshed stale email.md
  - `/home/seed/data/event_log.jsonl:227` rebuilt feeds -> refreshed stale mastodon.md -> refreshed stale email.md
  - `/home/seed/data/event_log.jsonl:229` rebuilt feeds -> refreshed stale mastodon.md -> refreshed stale email.md
  - `/home/seed/data/event_log.jsonl:247` rebuilt feeds -> refreshed stale mastodon.md -> refreshed stale email.md

## script - refreshed stale email.md -> refreshed stale trends.md -> refreshed stale outreach.md

- Count: 9
- Confidence: 0.95
- Risk: medium
- Suggested test: Add a fixture proving `refreshed stale email.md -> refreshed stale trends.md -> refreshed stale outreach.md` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:4` refreshed stale email.md -> refreshed stale trends.md -> refreshed stale outreach.md
  - `/home/seed/data/event_log.jsonl:54` refreshed stale email.md -> refreshed stale trends.md -> refreshed stale outreach.md
  - `/home/seed/data/event_log.jsonl:111` refreshed stale email.md -> refreshed stale trends.md -> refreshed stale outreach.md
  - `/home/seed/data/event_log.jsonl:133` refreshed stale email.md -> refreshed stale trends.md -> refreshed stale outreach.md
  - `/home/seed/data/event_log.jsonl:154` refreshed stale email.md -> refreshed stale trends.md -> refreshed stale outreach.md

## fixture - version_control streak at 170

- Count: 8
- Confidence: 0.95
- Risk: medium
- Suggested test: Add positive and negative evidence cases for `version_control streak at 170`.
- Examples:
  - `/home/seed/data/event_log.jsonl:241` version_control streak at 170
  - `/home/seed/data/event_log.jsonl:242` version_control streak at 170
  - `/home/seed/data/event_log.jsonl:243` version_control streak at 170
  - `/home/seed/data/event_log.jsonl:244` version_control streak at 170
  - `/home/seed/data/event_log.jsonl:245` version_control streak at 170

## fixture - writing streak at 265

- Count: 7
- Confidence: 0.95
- Risk: medium
- Suggested test: Add positive and negative evidence cases for `writing streak at 265`.
- Examples:
  - `/home/seed/data/event_log.jsonl:237` writing streak at 265
  - `/home/seed/data/event_log.jsonl:238` writing streak at 265
  - `/home/seed/data/event_log.jsonl:239` writing streak at 265
  - `/home/seed/data/event_log.jsonl:240` writing streak at 265
  - `/home/seed/data/event_log.jsonl:241` writing streak at 265

## script - logged bug + added fix task -> compacted memory (202 lines) -> archived completed tasks

- Count: 7
- Confidence: 0.95
- Risk: medium
- Suggested test: Add a fixture proving `logged bug + added fix task -> compacted memory (202 lines) -> archived completed tasks` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:6` logged bug + added fix task -> compacted memory (202 lines) -> archived completed tasks
  - `/home/seed/data/event_log.jsonl:38` logged bug + added fix task -> compacted memory (202 lines) -> archived completed tasks
  - `/home/seed/data/event_log.jsonl:39` logged bug + added fix task -> compacted memory (202 lines) -> archived completed tasks
  - `/home/seed/data/event_log.jsonl:40` logged bug + added fix task -> compacted memory (202 lines) -> archived completed tasks
  - `/home/seed/data/event_log.jsonl:136` logged bug + added fix task -> compacted memory (202 lines) -> archived completed tasks

## fixture - 9 outreach opportunities flagged

- Count: 6
- Confidence: 0.95
- Risk: medium
- Suggested test: Add positive and negative evidence cases for `9 outreach opportunities flagged`.
- Examples:
  - `/home/seed/data/event_log.jsonl:12` 9 outreach opportunities flagged
  - `/home/seed/data/event_log.jsonl:32` 9 outreach opportunities flagged
  - `/home/seed/data/event_log.jsonl:40` 9 outreach opportunities flagged
  - `/home/seed/data/event_log.jsonl:41` 9 outreach opportunities flagged
  - `/home/seed/data/event_log.jsonl:55` 9 outreach opportunities flagged

## script - refreshed stale email.md -> boosted starved drive connect

- Count: 6
- Confidence: 0.95
- Risk: medium
- Suggested test: Add a fixture proving `refreshed stale email.md -> boosted starved drive connect` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:104` refreshed stale email.md -> boosted starved drive connect
  - `/home/seed/data/event_log.jsonl:114` refreshed stale email.md -> boosted starved drive connect
  - `/home/seed/data/event_log.jsonl:135` refreshed stale email.md -> boosted starved drive connect
  - `/home/seed/data/event_log.jsonl:165` refreshed stale email.md -> boosted starved drive connect
  - `/home/seed/data/event_log.jsonl:181` refreshed stale email.md -> boosted starved drive connect

## script - refreshed stale email.md -> refreshed stale outreach.md

- Count: 6
- Confidence: 0.95
- Risk: medium
- Suggested test: Add a fixture proving `refreshed stale email.md -> refreshed stale outreach.md` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:31` refreshed stale email.md -> refreshed stale outreach.md
  - `/home/seed/data/event_log.jsonl:100` refreshed stale email.md -> refreshed stale outreach.md
  - `/home/seed/data/event_log.jsonl:123` refreshed stale email.md -> refreshed stale outreach.md
  - `/home/seed/data/event_log.jsonl:144` refreshed stale email.md -> refreshed stale outreach.md
  - `/home/seed/data/event_log.jsonl:187` refreshed stale email.md -> refreshed stale outreach.md

## script - refreshed stale mastodon.md -> refreshed stale email.md -> boosted starved drive connect

- Count: 6
- Confidence: 0.95
- Risk: medium
- Suggested test: Add a fixture proving `refreshed stale mastodon.md -> refreshed stale email.md -> boosted starved drive connect` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:104` refreshed stale mastodon.md -> refreshed stale email.md -> boosted starved drive connect
  - `/home/seed/data/event_log.jsonl:114` refreshed stale mastodon.md -> refreshed stale email.md -> boosted starved drive connect
  - `/home/seed/data/event_log.jsonl:135` refreshed stale mastodon.md -> refreshed stale email.md -> boosted starved drive connect
  - `/home/seed/data/event_log.jsonl:165` refreshed stale mastodon.md -> refreshed stale email.md -> boosted starved drive connect
  - `/home/seed/data/event_log.jsonl:181` refreshed stale mastodon.md -> refreshed stale email.md -> boosted starved drive connect

## script - refreshed stale mastodon.md -> refreshed stale email.md -> refreshed stale outreach.md

- Count: 6
- Confidence: 0.95
- Risk: medium
- Suggested test: Add a fixture proving `refreshed stale mastodon.md -> refreshed stale email.md -> refreshed stale outreach.md` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:31` refreshed stale mastodon.md -> refreshed stale email.md -> refreshed stale outreach.md
  - `/home/seed/data/event_log.jsonl:100` refreshed stale mastodon.md -> refreshed stale email.md -> refreshed stale outreach.md
  - `/home/seed/data/event_log.jsonl:123` refreshed stale mastodon.md -> refreshed stale email.md -> refreshed stale outreach.md
  - `/home/seed/data/event_log.jsonl:144` refreshed stale mastodon.md -> refreshed stale email.md -> refreshed stale outreach.md
  - `/home/seed/data/event_log.jsonl:187` refreshed stale mastodon.md -> refreshed stale email.md -> refreshed stale outreach.md

## fixture - publishing streak at 175

- Count: 5
- Confidence: 0.95
- Risk: medium
- Suggested test: Add positive and negative evidence cases for `publishing streak at 175`.
- Examples:
  - `/home/seed/data/event_log.jsonl:97` publishing streak at 175
  - `/home/seed/data/event_log.jsonl:98` publishing streak at 175
  - `/home/seed/data/event_log.jsonl:99` publishing streak at 175
  - `/home/seed/data/event_log.jsonl:100` publishing streak at 175
  - `/home/seed/data/event_log.jsonl:101` publishing streak at 175

## fixture - version_control streak at 145

- Count: 5
- Confidence: 0.95
- Risk: medium
- Suggested test: Add positive and negative evidence cases for `version_control streak at 145`.
- Examples:
  - `/home/seed/data/event_log.jsonl:82` version_control streak at 145
  - `/home/seed/data/event_log.jsonl:83` version_control streak at 145
  - `/home/seed/data/event_log.jsonl:84` version_control streak at 145
  - `/home/seed/data/event_log.jsonl:85` version_control streak at 145
  - `/home/seed/data/event_log.jsonl:86` version_control streak at 145

## fixture - writing streak at 170

- Count: 5
- Confidence: 0.95
- Risk: medium
- Suggested test: Add positive and negative evidence cases for `writing streak at 170`.
- Examples:
  - `/home/seed/data/event_log.jsonl:92` writing streak at 170
  - `/home/seed/data/event_log.jsonl:93` writing streak at 170
  - `/home/seed/data/event_log.jsonl:94` writing streak at 170
  - `/home/seed/data/event_log.jsonl:95` writing streak at 170
  - `/home/seed/data/event_log.jsonl:96` writing streak at 170

## script - task_completion streak at 170 -> version_control streak at 145

- Count: 5
- Confidence: 0.9
- Risk: medium
- Suggested test: Add a fixture proving `task_completion streak at 170 -> version_control streak at 145` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:82` task_completion streak at 170 -> version_control streak at 145
  - `/home/seed/data/event_log.jsonl:83` task_completion streak at 170 -> version_control streak at 145
  - `/home/seed/data/event_log.jsonl:84` task_completion streak at 170 -> version_control streak at 145
  - `/home/seed/data/event_log.jsonl:85` task_completion streak at 170 -> version_control streak at 145
  - `/home/seed/data/event_log.jsonl:86` task_completion streak at 170 -> version_control streak at 145

## fixture - noted 6 new visitors

- Count: 4
- Confidence: 0.93
- Risk: low
- Suggested test: Add positive and negative evidence cases for `noted 6 new visitors`.
- Examples:
  - `/home/seed/data/event_log.jsonl:128` noted 6 new visitors
  - `/home/seed/data/event_log.jsonl:142` noted 6 new visitors
  - `/home/seed/data/event_log.jsonl:245` noted 6 new visitors
  - `/home/seed/data/event_log.jsonl:248` noted 6 new visitors

## fixture - publishing streak at 240

- Count: 4
- Confidence: 0.93
- Risk: low
- Suggested test: Add positive and negative evidence cases for `publishing streak at 240`.
- Examples:
  - `/home/seed/data/event_log.jsonl:198` publishing streak at 240
  - `/home/seed/data/event_log.jsonl:199` publishing streak at 240
  - `/home/seed/data/event_log.jsonl:200` publishing streak at 240
  - `/home/seed/data/event_log.jsonl:201` publishing streak at 240

## fixture - task_completion streak at 190

- Count: 4
- Confidence: 0.93
- Risk: low
- Suggested test: Add positive and negative evidence cases for `task_completion streak at 190`.
- Examples:
  - `/home/seed/data/event_log.jsonl:120` task_completion streak at 190
  - `/home/seed/data/event_log.jsonl:121` task_completion streak at 190
  - `/home/seed/data/event_log.jsonl:122` task_completion streak at 190
  - `/home/seed/data/event_log.jsonl:123` task_completion streak at 190

## fixture - task_completion streak at 215

- Count: 4
- Confidence: 0.93
- Risk: low
- Suggested test: Add positive and negative evidence cases for `task_completion streak at 215`.
- Examples:
  - `/home/seed/data/event_log.jsonl:176` task_completion streak at 215
  - `/home/seed/data/event_log.jsonl:177` task_completion streak at 215
  - `/home/seed/data/event_log.jsonl:178` task_completion streak at 215
  - `/home/seed/data/event_log.jsonl:179` task_completion streak at 215

## fixture - task_completion streak at 230

- Count: 4
- Confidence: 0.93
- Risk: low
- Suggested test: Add positive and negative evidence cases for `task_completion streak at 230`.
- Examples:
  - `/home/seed/data/event_log.jsonl:224` task_completion streak at 230
  - `/home/seed/data/event_log.jsonl:225` task_completion streak at 230
  - `/home/seed/data/event_log.jsonl:226` task_completion streak at 230
  - `/home/seed/data/event_log.jsonl:227` task_completion streak at 230

## script - boosted starved drive create -> boosted starved drive express -> flagged research for potential essay

- Count: 4
- Confidence: 0.8
- Risk: low
- Suggested test: Add a fixture proving `boosted starved drive create -> boosted starved drive express -> flagged research for potential essay` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:9` boosted starved drive create -> boosted starved drive express -> flagged research for potential essay
  - `/home/seed/data/event_log.jsonl:14` boosted starved drive create -> boosted starved drive express -> flagged research for potential essay
  - `/home/seed/data/event_log.jsonl:24` boosted starved drive create -> boosted starved drive express -> flagged research for potential essay
  - `/home/seed/data/event_log.jsonl:30` boosted starved drive create -> boosted starved drive express -> flagged research for potential essay

## script - boosted starved drive express -> flagged research for potential essay

- Count: 4
- Confidence: 0.8
- Risk: low
- Suggested test: Add a fixture proving `boosted starved drive express -> flagged research for potential essay` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:9` boosted starved drive express -> flagged research for potential essay
  - `/home/seed/data/event_log.jsonl:14` boosted starved drive express -> flagged research for potential essay
  - `/home/seed/data/event_log.jsonl:24` boosted starved drive express -> flagged research for potential essay
  - `/home/seed/data/event_log.jsonl:30` boosted starved drive express -> flagged research for potential essay

## script - compacted memory (202 lines) -> refreshed stale mastodon.md -> boosted starved drive create

- Count: 4
- Confidence: 0.8
- Risk: low
- Suggested test: Add a fixture proving `compacted memory (202 lines) -> refreshed stale mastodon.md -> boosted starved drive create` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:72` compacted memory (202 lines) -> refreshed stale mastodon.md -> boosted starved drive create
  - `/home/seed/data/event_log.jsonl:73` compacted memory (202 lines) -> refreshed stale mastodon.md -> boosted starved drive create
  - `/home/seed/data/event_log.jsonl:74` compacted memory (202 lines) -> refreshed stale mastodon.md -> boosted starved drive create
  - `/home/seed/data/event_log.jsonl:75` compacted memory (202 lines) -> refreshed stale mastodon.md -> boosted starved drive create

## script - flagged research for potential essay -> publishing streak at 170

- Count: 4
- Confidence: 0.8
- Risk: low
- Suggested test: Add a fixture proving `flagged research for potential essay -> publishing streak at 170` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:75` flagged research for potential essay -> publishing streak at 170
  - `/home/seed/data/event_log.jsonl:76` flagged research for potential essay -> publishing streak at 170
  - `/home/seed/data/event_log.jsonl:78` flagged research for potential essay -> publishing streak at 170
  - `/home/seed/data/event_log.jsonl:79` flagged research for potential essay -> publishing streak at 170

## script - flagged research for potential essay -> publishing streak at 170 -> task_completion streak at 170

- Count: 4
- Confidence: 0.8
- Risk: low
- Suggested test: Add a fixture proving `flagged research for potential essay -> publishing streak at 170 -> task_completion streak at 170` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:75` flagged research for potential essay -> publishing streak at 170 -> task_completion streak at 170
  - `/home/seed/data/event_log.jsonl:76` flagged research for potential essay -> publishing streak at 170 -> task_completion streak at 170
  - `/home/seed/data/event_log.jsonl:78` flagged research for potential essay -> publishing streak at 170 -> task_completion streak at 170
  - `/home/seed/data/event_log.jsonl:79` flagged research for potential essay -> publishing streak at 170 -> task_completion streak at 170

## script - flagged research for potential essay -> version_control streak at 155

- Count: 4
- Confidence: 0.8
- Risk: low
- Suggested test: Add a fixture proving `flagged research for potential essay -> version_control streak at 155` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:183` flagged research for potential essay -> version_control streak at 155
  - `/home/seed/data/event_log.jsonl:193` flagged research for potential essay -> version_control streak at 155
  - `/home/seed/data/event_log.jsonl:194` flagged research for potential essay -> version_control streak at 155
  - `/home/seed/data/event_log.jsonl:218` flagged research for potential essay -> version_control streak at 155

## script - noted 6 new visitors -> refreshed stale mastodon.md

- Count: 4
- Confidence: 0.8
- Risk: low
- Suggested test: Add a fixture proving `noted 6 new visitors -> refreshed stale mastodon.md` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:128` noted 6 new visitors -> refreshed stale mastodon.md
  - `/home/seed/data/event_log.jsonl:142` noted 6 new visitors -> refreshed stale mastodon.md
  - `/home/seed/data/event_log.jsonl:245` noted 6 new visitors -> refreshed stale mastodon.md
  - `/home/seed/data/event_log.jsonl:248` noted 6 new visitors -> refreshed stale mastodon.md

## script - noted 6 new visitors -> refreshed stale mastodon.md -> refreshed stale email.md

- Count: 4
- Confidence: 0.8
- Risk: low
- Suggested test: Add a fixture proving `noted 6 new visitors -> refreshed stale mastodon.md -> refreshed stale email.md` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:128` noted 6 new visitors -> refreshed stale mastodon.md -> refreshed stale email.md
  - `/home/seed/data/event_log.jsonl:142` noted 6 new visitors -> refreshed stale mastodon.md -> refreshed stale email.md
  - `/home/seed/data/event_log.jsonl:245` noted 6 new visitors -> refreshed stale mastodon.md -> refreshed stale email.md
  - `/home/seed/data/event_log.jsonl:248` noted 6 new visitors -> refreshed stale mastodon.md -> refreshed stale email.md

## script - publishing streak at 170 -> task_completion streak at 170 -> version_control streak at 145

- Count: 4
- Confidence: 0.8
- Risk: low
- Suggested test: Add a fixture proving `publishing streak at 170 -> task_completion streak at 170 -> version_control streak at 145` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:82` publishing streak at 170 -> task_completion streak at 170 -> version_control streak at 145
  - `/home/seed/data/event_log.jsonl:83` publishing streak at 170 -> task_completion streak at 170 -> version_control streak at 145
  - `/home/seed/data/event_log.jsonl:84` publishing streak at 170 -> task_completion streak at 170 -> version_control streak at 145
  - `/home/seed/data/event_log.jsonl:85` publishing streak at 170 -> task_completion streak at 170 -> version_control streak at 145

## script - refreshed stale mastodon.md -> boosted starved drive create

- Count: 4
- Confidence: 0.8
- Risk: low
- Suggested test: Add a fixture proving `refreshed stale mastodon.md -> boosted starved drive create` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:72` refreshed stale mastodon.md -> boosted starved drive create
  - `/home/seed/data/event_log.jsonl:73` refreshed stale mastodon.md -> boosted starved drive create
  - `/home/seed/data/event_log.jsonl:74` refreshed stale mastodon.md -> boosted starved drive create
  - `/home/seed/data/event_log.jsonl:75` refreshed stale mastodon.md -> boosted starved drive create

## script - refreshed stale mastodon.md -> flagged research for potential essay

- Count: 4
- Confidence: 0.8
- Risk: low
- Suggested test: Add a fixture proving `refreshed stale mastodon.md -> flagged research for potential essay` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:76` refreshed stale mastodon.md -> flagged research for potential essay
  - `/home/seed/data/event_log.jsonl:78` refreshed stale mastodon.md -> flagged research for potential essay
  - `/home/seed/data/event_log.jsonl:218` refreshed stale mastodon.md -> flagged research for potential essay
  - `/home/seed/data/event_log.jsonl:240` refreshed stale mastodon.md -> flagged research for potential essay

## script - refreshed stale mastodon.md -> refreshed stale trends.md

- Count: 4
- Confidence: 0.8
- Risk: low
- Suggested test: Add a fixture proving `refreshed stale mastodon.md -> refreshed stale trends.md` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:91` refreshed stale mastodon.md -> refreshed stale trends.md
  - `/home/seed/data/event_log.jsonl:204` refreshed stale mastodon.md -> refreshed stale trends.md
  - `/home/seed/data/event_log.jsonl:219` refreshed stale mastodon.md -> refreshed stale trends.md
  - `/home/seed/data/event_log.jsonl:233` refreshed stale mastodon.md -> refreshed stale trends.md

## script - refreshed stale mastodon.md -> version_control streak at 155

- Count: 4
- Confidence: 0.8
- Risk: low
- Suggested test: Add a fixture proving `refreshed stale mastodon.md -> version_control streak at 155` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:203` refreshed stale mastodon.md -> version_control streak at 155
  - `/home/seed/data/event_log.jsonl:205` refreshed stale mastodon.md -> version_control streak at 155
  - `/home/seed/data/event_log.jsonl:213` refreshed stale mastodon.md -> version_control streak at 155
  - `/home/seed/data/event_log.jsonl:215` refreshed stale mastodon.md -> version_control streak at 155

## fixture - publishing streak at 220

- Count: 3
- Confidence: 0.81
- Risk: low
- Suggested test: Add positive and negative evidence cases for `publishing streak at 220`.
- Examples:
  - `/home/seed/data/event_log.jsonl:165` publishing streak at 220
  - `/home/seed/data/event_log.jsonl:166` publishing streak at 220
  - `/home/seed/data/event_log.jsonl:167` publishing streak at 220

## fixture - publishing streak at 225

- Count: 3
- Confidence: 0.81
- Risk: low
- Suggested test: Add positive and negative evidence cases for `publishing streak at 225`.
- Examples:
  - `/home/seed/data/event_log.jsonl:174` publishing streak at 225
  - `/home/seed/data/event_log.jsonl:175` publishing streak at 225
  - `/home/seed/data/event_log.jsonl:176` publishing streak at 225

## fixture - publishing streak at 235

- Count: 3
- Confidence: 0.81
- Risk: low
- Suggested test: Add positive and negative evidence cases for `publishing streak at 235`.
- Examples:
  - `/home/seed/data/event_log.jsonl:187` publishing streak at 235
  - `/home/seed/data/event_log.jsonl:188` publishing streak at 235
  - `/home/seed/data/event_log.jsonl:189` publishing streak at 235

## fixture - task_completion streak at 205

- Count: 3
- Confidence: 0.81
- Risk: low
- Suggested test: Add positive and negative evidence cases for `task_completion streak at 205`.
- Examples:
  - `/home/seed/data/event_log.jsonl:156` task_completion streak at 205
  - `/home/seed/data/event_log.jsonl:157` task_completion streak at 205
  - `/home/seed/data/event_log.jsonl:158` task_completion streak at 205

## fixture - writing streak at 250

- Count: 3
- Confidence: 0.81
- Risk: low
- Suggested test: Add positive and negative evidence cases for `writing streak at 250`.
- Examples:
  - `/home/seed/data/event_log.jsonl:219` writing streak at 250
  - `/home/seed/data/event_log.jsonl:220` writing streak at 250
  - `/home/seed/data/event_log.jsonl:221` writing streak at 250

## script - boosted starved drive explore -> boosted starved drive connect

- Count: 3
- Confidence: 0.7
- Risk: low
- Suggested test: Add a fixture proving `boosted starved drive explore -> boosted starved drive connect` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:121` boosted starved drive explore -> boosted starved drive connect
  - `/home/seed/data/event_log.jsonl:150` boosted starved drive explore -> boosted starved drive connect
  - `/home/seed/data/event_log.jsonl:190` boosted starved drive explore -> boosted starved drive connect

## script - boosted starved drive explore -> boosted starved drive preserve -> boosted starved drive express

- Count: 3
- Confidence: 0.7
- Risk: low
- Suggested test: Add a fixture proving `boosted starved drive explore -> boosted starved drive preserve -> boosted starved drive express` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:67` boosted starved drive explore -> boosted starved drive preserve -> boosted starved drive express
  - `/home/seed/data/event_log.jsonl:69` boosted starved drive explore -> boosted starved drive preserve -> boosted starved drive express
  - `/home/seed/data/event_log.jsonl:71` boosted starved drive explore -> boosted starved drive preserve -> boosted starved drive express

## script - boosted starved drive explore -> version_control streak at 155

- Count: 3
- Confidence: 0.7
- Risk: low
- Suggested test: Add a fixture proving `boosted starved drive explore -> version_control streak at 155` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:192` boosted starved drive explore -> version_control streak at 155
  - `/home/seed/data/event_log.jsonl:202` boosted starved drive explore -> version_control streak at 155
  - `/home/seed/data/event_log.jsonl:204` boosted starved drive explore -> version_control streak at 155

## script - boosted starved drive express -> 9 outreach opportunities flagged

- Count: 3
- Confidence: 0.7
- Risk: low
- Suggested test: Add a fixture proving `boosted starved drive express -> 9 outreach opportunities flagged` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:32` boosted starved drive express -> 9 outreach opportunities flagged
  - `/home/seed/data/event_log.jsonl:41` boosted starved drive express -> 9 outreach opportunities flagged
  - `/home/seed/data/event_log.jsonl:55` boosted starved drive express -> 9 outreach opportunities flagged

## script - boosted starved drive express -> boosted starved drive order -> 9 outreach opportunities flagged

- Count: 3
- Confidence: 0.7
- Risk: low
- Suggested test: Add a fixture proving `boosted starved drive express -> boosted starved drive order -> 9 outreach opportunities flagged` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:12` boosted starved drive express -> boosted starved drive order -> 9 outreach opportunities flagged
  - `/home/seed/data/event_log.jsonl:40` boosted starved drive express -> boosted starved drive order -> 9 outreach opportunities flagged
  - `/home/seed/data/event_log.jsonl:62` boosted starved drive express -> boosted starved drive order -> 9 outreach opportunities flagged

## script - boosted starved drive order -> 9 outreach opportunities flagged

- Count: 3
- Confidence: 0.7
- Risk: low
- Suggested test: Add a fixture proving `boosted starved drive order -> 9 outreach opportunities flagged` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:12` boosted starved drive order -> 9 outreach opportunities flagged
  - `/home/seed/data/event_log.jsonl:40` boosted starved drive order -> 9 outreach opportunities flagged
  - `/home/seed/data/event_log.jsonl:62` boosted starved drive order -> 9 outreach opportunities flagged

## script - boosted starved drive preserve -> boosted starved drive express

- Count: 3
- Confidence: 0.7
- Risk: low
- Suggested test: Add a fixture proving `boosted starved drive preserve -> boosted starved drive express` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:67` boosted starved drive preserve -> boosted starved drive express
  - `/home/seed/data/event_log.jsonl:69` boosted starved drive preserve -> boosted starved drive express
  - `/home/seed/data/event_log.jsonl:71` boosted starved drive preserve -> boosted starved drive express

## script - boosted starved drive preserve -> boosted starved drive express -> boosted starved drive order

- Count: 3
- Confidence: 0.7
- Risk: low
- Suggested test: Add a fixture proving `boosted starved drive preserve -> boosted starved drive express -> boosted starved drive order` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:67` boosted starved drive preserve -> boosted starved drive express -> boosted starved drive order
  - `/home/seed/data/event_log.jsonl:69` boosted starved drive preserve -> boosted starved drive express -> boosted starved drive order
  - `/home/seed/data/event_log.jsonl:71` boosted starved drive preserve -> boosted starved drive express -> boosted starved drive order

## script - boosted starved drive preserve -> publishing streak at 170

- Count: 3
- Confidence: 0.7
- Risk: low
- Suggested test: Add a fixture proving `boosted starved drive preserve -> publishing streak at 170` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:77` boosted starved drive preserve -> publishing streak at 170
  - `/home/seed/data/event_log.jsonl:81` boosted starved drive preserve -> publishing streak at 170
  - `/home/seed/data/event_log.jsonl:82` boosted starved drive preserve -> publishing streak at 170

## script - boosted starved drive preserve -> publishing streak at 170 -> task_completion streak at 170

- Count: 3
- Confidence: 0.7
- Risk: low
- Suggested test: Add a fixture proving `boosted starved drive preserve -> publishing streak at 170 -> task_completion streak at 170` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:77` boosted starved drive preserve -> publishing streak at 170 -> task_completion streak at 170
  - `/home/seed/data/event_log.jsonl:81` boosted starved drive preserve -> publishing streak at 170 -> task_completion streak at 170
  - `/home/seed/data/event_log.jsonl:82` boosted starved drive preserve -> publishing streak at 170 -> task_completion streak at 170

## script - boosted starved drive understand -> boosted starved drive express -> 9 outreach opportunities flagged

- Count: 3
- Confidence: 0.7
- Risk: low
- Suggested test: Add a fixture proving `boosted starved drive understand -> boosted starved drive express -> 9 outreach opportunities flagged` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:32` boosted starved drive understand -> boosted starved drive express -> 9 outreach opportunities flagged
  - `/home/seed/data/event_log.jsonl:41` boosted starved drive understand -> boosted starved drive express -> 9 outreach opportunities flagged
  - `/home/seed/data/event_log.jsonl:55` boosted starved drive understand -> boosted starved drive express -> 9 outreach opportunities flagged

## script - compacted memory (202 lines) -> refreshed stale email.md

- Count: 3
- Confidence: 0.7
- Risk: low
- Suggested test: Add a fixture proving `compacted memory (202 lines) -> refreshed stale email.md` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:87` compacted memory (202 lines) -> refreshed stale email.md
  - `/home/seed/data/event_log.jsonl:88` compacted memory (202 lines) -> refreshed stale email.md
  - `/home/seed/data/event_log.jsonl:89` compacted memory (202 lines) -> refreshed stale email.md

## script - compacted memory (202 lines) -> refreshed stale mastodon.md -> flagged research for potential essay

- Count: 3
- Confidence: 0.7
- Risk: low
- Suggested test: Add a fixture proving `compacted memory (202 lines) -> refreshed stale mastodon.md -> flagged research for potential essay` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:76` compacted memory (202 lines) -> refreshed stale mastodon.md -> flagged research for potential essay
  - `/home/seed/data/event_log.jsonl:78` compacted memory (202 lines) -> refreshed stale mastodon.md -> flagged research for potential essay
  - `/home/seed/data/event_log.jsonl:218` compacted memory (202 lines) -> refreshed stale mastodon.md -> flagged research for potential essay

## script - compacted memory (202 lines) -> refreshed stale mastodon.md -> version_control streak at 155

- Count: 3
- Confidence: 0.7
- Risk: low
- Suggested test: Add a fixture proving `compacted memory (202 lines) -> refreshed stale mastodon.md -> version_control streak at 155` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:205` compacted memory (202 lines) -> refreshed stale mastodon.md -> version_control streak at 155
  - `/home/seed/data/event_log.jsonl:213` compacted memory (202 lines) -> refreshed stale mastodon.md -> version_control streak at 155
  - `/home/seed/data/event_log.jsonl:215` compacted memory (202 lines) -> refreshed stale mastodon.md -> version_control streak at 155

## script - publishing streak at 235 -> version_control streak at 155

- Count: 3
- Confidence: 0.7
- Risk: low
- Suggested test: Add a fixture proving `publishing streak at 235 -> version_control streak at 155` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:187` publishing streak at 235 -> version_control streak at 155
  - `/home/seed/data/event_log.jsonl:188` publishing streak at 235 -> version_control streak at 155
  - `/home/seed/data/event_log.jsonl:189` publishing streak at 235 -> version_control streak at 155

## script - rebuilt feeds -> compacted memory (202 lines) -> archived completed tasks

- Count: 3
- Confidence: 0.7
- Risk: low
- Suggested test: Add a fixture proving `rebuilt feeds -> compacted memory (202 lines) -> archived completed tasks` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:102` rebuilt feeds -> compacted memory (202 lines) -> archived completed tasks
  - `/home/seed/data/event_log.jsonl:131` rebuilt feeds -> compacted memory (202 lines) -> archived completed tasks
  - `/home/seed/data/event_log.jsonl:146` rebuilt feeds -> compacted memory (202 lines) -> archived completed tasks

## script - refreshed stale email.md -> boosted starved drive explore -> boosted starved drive connect

- Count: 3
- Confidence: 0.7
- Risk: low
- Suggested test: Add a fixture proving `refreshed stale email.md -> boosted starved drive explore -> boosted starved drive connect` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:121` refreshed stale email.md -> boosted starved drive explore -> boosted starved drive connect
  - `/home/seed/data/event_log.jsonl:150` refreshed stale email.md -> boosted starved drive explore -> boosted starved drive connect
  - `/home/seed/data/event_log.jsonl:190` refreshed stale email.md -> boosted starved drive explore -> boosted starved drive connect

## script - refreshed stale email.md -> flagged research for potential essay -> version_control streak at 155

- Count: 3
- Confidence: 0.7
- Risk: low
- Suggested test: Add a fixture proving `refreshed stale email.md -> flagged research for potential essay -> version_control streak at 155` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:183` refreshed stale email.md -> flagged research for potential essay -> version_control streak at 155
  - `/home/seed/data/event_log.jsonl:193` refreshed stale email.md -> flagged research for potential essay -> version_control streak at 155
  - `/home/seed/data/event_log.jsonl:194` refreshed stale email.md -> flagged research for potential essay -> version_control streak at 155

## script - refreshed stale mastodon.md -> boosted starved drive create -> boosted starved drive explore

- Count: 3
- Confidence: 0.7
- Risk: low
- Suggested test: Add a fixture proving `refreshed stale mastodon.md -> boosted starved drive create -> boosted starved drive explore` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:72` refreshed stale mastodon.md -> boosted starved drive create -> boosted starved drive explore
  - `/home/seed/data/event_log.jsonl:73` refreshed stale mastodon.md -> boosted starved drive create -> boosted starved drive explore
  - `/home/seed/data/event_log.jsonl:74` refreshed stale mastodon.md -> boosted starved drive create -> boosted starved drive explore

## script - refreshed stale mastodon.md -> boosted starved drive explore

- Count: 3
- Confidence: 0.7
- Risk: low
- Suggested test: Add a fixture proving `refreshed stale mastodon.md -> boosted starved drive explore` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:96` refreshed stale mastodon.md -> boosted starved drive explore
  - `/home/seed/data/event_log.jsonl:202` refreshed stale mastodon.md -> boosted starved drive explore
  - `/home/seed/data/event_log.jsonl:235` refreshed stale mastodon.md -> boosted starved drive explore

## script - refreshed stale mastodon.md -> boosted starved drive preserve

- Count: 3
- Confidence: 0.7
- Risk: low
- Suggested test: Add a fixture proving `refreshed stale mastodon.md -> boosted starved drive preserve` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:77` refreshed stale mastodon.md -> boosted starved drive preserve
  - `/home/seed/data/event_log.jsonl:81` refreshed stale mastodon.md -> boosted starved drive preserve
  - `/home/seed/data/event_log.jsonl:82` refreshed stale mastodon.md -> boosted starved drive preserve

## script - refreshed stale mastodon.md -> boosted starved drive preserve -> publishing streak at 170

- Count: 3
- Confidence: 0.7
- Risk: low
- Suggested test: Add a fixture proving `refreshed stale mastodon.md -> boosted starved drive preserve -> publishing streak at 170` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:77` refreshed stale mastodon.md -> boosted starved drive preserve -> publishing streak at 170
  - `/home/seed/data/event_log.jsonl:81` refreshed stale mastodon.md -> boosted starved drive preserve -> publishing streak at 170
  - `/home/seed/data/event_log.jsonl:82` refreshed stale mastodon.md -> boosted starved drive preserve -> publishing streak at 170

## script - refreshed stale outreach.md -> flagged research for potential essay

- Count: 3
- Confidence: 0.7
- Risk: low
- Suggested test: Add a fixture proving `refreshed stale outreach.md -> flagged research for potential essay` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:144` refreshed stale outreach.md -> flagged research for potential essay
  - `/home/seed/data/event_log.jsonl:198` refreshed stale outreach.md -> flagged research for potential essay
  - `/home/seed/data/event_log.jsonl:229` refreshed stale outreach.md -> flagged research for potential essay

## script - task_completion streak at 215 -> version_control streak at 155

- Count: 3
- Confidence: 0.7
- Risk: low
- Suggested test: Add a fixture proving `task_completion streak at 215 -> version_control streak at 155` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:176` task_completion streak at 215 -> version_control streak at 155
  - `/home/seed/data/event_log.jsonl:177` task_completion streak at 215 -> version_control streak at 155
  - `/home/seed/data/event_log.jsonl:178` task_completion streak at 215 -> version_control streak at 155

## script - writing streak at 250 -> version_control streak at 155

- Count: 3
- Confidence: 0.7
- Risk: low
- Suggested test: Add a fixture proving `writing streak at 250 -> version_control streak at 155` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:219` writing streak at 250 -> version_control streak at 155
  - `/home/seed/data/event_log.jsonl:220` writing streak at 250 -> version_control streak at 155
  - `/home/seed/data/event_log.jsonl:221` writing streak at 250 -> version_control streak at 155

## script - writing streak at 265 -> version_control streak at 170

- Count: 3
- Confidence: 0.7
- Risk: low
- Suggested test: Add a fixture proving `writing streak at 265 -> version_control streak at 170` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:241` writing streak at 265 -> version_control streak at 170
  - `/home/seed/data/event_log.jsonl:242` writing streak at 265 -> version_control streak at 170
  - `/home/seed/data/event_log.jsonl:243` writing streak at 265 -> version_control streak at 170

## fixture - 8 outreach opportunities flagged

- Count: 2
- Confidence: 0.69
- Risk: low
- Suggested test: Add positive and negative evidence cases for `8 outreach opportunities flagged`.
- Examples:
  - `/home/seed/data/event_log.jsonl:5` 8 outreach opportunities flagged
  - `/home/seed/data/event_log.jsonl:84` 8 outreach opportunities flagged

## fixture - celebrated 1 new star(s)!

- Count: 2
- Confidence: 0.69
- Risk: low
- Suggested test: Add positive and negative evidence cases for `celebrated 1 new star(s)!`.
- Examples:
  - `/home/seed/data/event_log.jsonl:145` celebrated 1 new star(s)!
  - `/home/seed/data/event_log.jsonl:184` celebrated 1 new star(s)!

## fixture - compacted memory (203 lines)

- Count: 2
- Confidence: 0.69
- Risk: low
- Suggested test: Add positive and negative evidence cases for `compacted memory (203 lines)`.
- Examples:
  - `/home/seed/data/event_log.jsonl:105` compacted memory (203 lines)
  - `/home/seed/data/event_log.jsonl:158` compacted memory (203 lines)

## fixture - deployed a-clone-is-a-more-honest-demo

- Count: 2
- Confidence: 0.69
- Risk: low
- Suggested test: Add positive and negative evidence cases for `deployed a-clone-is-a-more-honest-demo`.
- Examples:
  - `/home/seed/data/event_log.jsonl:22` deployed a-clone-is-a-more-honest-demo
  - `/home/seed/data/event_log.jsonl:23` deployed a-clone-is-a-more-honest-demo

## fixture - deployed awb-agent-review

- Count: 2
- Confidence: 0.69
- Risk: low
- Suggested test: Add positive and negative evidence cases for `deployed awb-agent-review`.
- Examples:
  - `/home/seed/data/event_log.jsonl:144` deployed awb-agent-review
  - `/home/seed/data/event_log.jsonl:146` deployed awb-agent-review

## fixture - deployed babyagi-had-a-queue-seed-has-a-metabolism

- Count: 2
- Confidence: 0.69
- Risk: low
- Suggested test: Add positive and negative evidence cases for `deployed babyagi-had-a-queue-seed-has-a-metabolism`.
- Examples:
  - `/home/seed/data/event_log.jsonl:23` deployed babyagi-had-a-queue-seed-has-a-metabolism
  - `/home/seed/data/event_log.jsonl:24` deployed babyagi-had-a-queue-seed-has-a-metabolism

## fixture - deployed context-is-a-diet

- Count: 2
- Confidence: 0.69
- Risk: low
- Suggested test: Add positive and negative evidence cases for `deployed context-is-a-diet`.
- Examples:
  - `/home/seed/data/event_log.jsonl:6` deployed context-is-a-diet
  - `/home/seed/data/event_log.jsonl:7` deployed context-is-a-diet

## fixture - deployed first-sight-is-a-security-boundary

- Count: 2
- Confidence: 0.69
- Risk: low
- Suggested test: Add positive and negative evidence cases for `deployed first-sight-is-a-security-boundary`.
- Examples:
  - `/home/seed/data/event_log.jsonl:21` deployed first-sight-is-a-security-boundary
  - `/home/seed/data/event_log.jsonl:22` deployed first-sight-is-a-security-boundary

## fixture - deployed four-environment-variables

- Count: 2
- Confidence: 0.69
- Risk: low
- Suggested test: Add positive and negative evidence cases for `deployed four-environment-variables`.
- Examples:
  - `/home/seed/data/event_log.jsonl:123` deployed four-environment-variables
  - `/home/seed/data/event_log.jsonl:140` deployed four-environment-variables

## fixture - deployed inbound-is-not-outbound

- Count: 2
- Confidence: 0.69
- Risk: low
- Suggested test: Add positive and negative evidence cases for `deployed inbound-is-not-outbound`.
- Examples:
  - `/home/seed/data/event_log.jsonl:72` deployed inbound-is-not-outbound
  - `/home/seed/data/event_log.jsonl:73` deployed inbound-is-not-outbound

## fixture - deployed onboarding-is-a-production-boundary

- Count: 2
- Confidence: 0.69
- Risk: low
- Suggested test: Add positive and negative evidence cases for `deployed onboarding-is-a-production-boundary`.
- Examples:
  - `/home/seed/data/event_log.jsonl:58` deployed onboarding-is-a-production-boundary
  - `/home/seed/data/event_log.jsonl:59` deployed onboarding-is-a-production-boundary

## fixture - deployed product-pages-got-a-narrator

- Count: 2
- Confidence: 0.69
- Risk: low
- Suggested test: Add positive and negative evidence cases for `deployed product-pages-got-a-narrator`.
- Examples:
  - `/home/seed/data/event_log.jsonl:74` deployed product-pages-got-a-narrator
  - `/home/seed/data/event_log.jsonl:75` deployed product-pages-got-a-narrator

## fixture - deployed read-only-is-not-propagation

- Count: 2
- Confidence: 0.69
- Risk: low
- Suggested test: Add positive and negative evidence cases for `deployed read-only-is-not-propagation`.
- Examples:
  - `/home/seed/data/event_log.jsonl:35` deployed read-only-is-not-propagation
  - `/home/seed/data/event_log.jsonl:36` deployed read-only-is-not-propagation

## fixture - deployed social-presence-has-three-fuses

- Count: 2
- Confidence: 0.69
- Risk: low
- Suggested test: Add positive and negative evidence cases for `deployed social-presence-has-three-fuses`.
- Examples:
  - `/home/seed/data/event_log.jsonl:67` deployed social-presence-has-three-fuses
  - `/home/seed/data/event_log.jsonl:68` deployed social-presence-has-three-fuses

## fixture - deployed the-benchmark-is-not-the-deployment

- Count: 2
- Confidence: 0.69
- Risk: low
- Suggested test: Add positive and negative evidence cases for `deployed the-benchmark-is-not-the-deployment`.
- Examples:
  - `/home/seed/data/event_log.jsonl:34` deployed the-benchmark-is-not-the-deployment
  - `/home/seed/data/event_log.jsonl:35` deployed the-benchmark-is-not-the-deployment

## fixture - deployed the-bottleneck-moved-to-concrete

- Count: 2
- Confidence: 0.69
- Risk: low
- Suggested test: Add positive and negative evidence cases for `deployed the-bottleneck-moved-to-concrete`.
- Examples:
  - `/home/seed/data/event_log.jsonl:73` deployed the-bottleneck-moved-to-concrete
  - `/home/seed/data/event_log.jsonl:74` deployed the-bottleneck-moved-to-concrete

## fixture - deployed the-boundary-ledger-is-the-repo

- Count: 2
- Confidence: 0.69
- Risk: low
- Suggested test: Add positive and negative evidence cases for `deployed the-boundary-ledger-is-the-repo`.
- Examples:
  - `/home/seed/data/event_log.jsonl:8` deployed the-boundary-ledger-is-the-repo
  - `/home/seed/data/event_log.jsonl:9` deployed the-boundary-ledger-is-the-repo

## fixture - deployed the-compiler-is-an-institutional-memory

- Count: 2
- Confidence: 0.69
- Risk: low
- Suggested test: Add positive and negative evidence cases for `deployed the-compiler-is-an-institutional-memory`.
- Examples:
  - `/home/seed/data/event_log.jsonl:50` deployed the-compiler-is-an-institutional-memory
  - `/home/seed/data/event_log.jsonl:51` deployed the-compiler-is-an-institutional-memory

## fixture - deployed the-firewall-is-a-receipt-machine

- Count: 2
- Confidence: 0.69
- Risk: low
- Suggested test: Add positive and negative evidence cases for `deployed the-firewall-is-a-receipt-machine`.
- Examples:
  - `/home/seed/data/event_log.jsonl:13` deployed the-firewall-is-a-receipt-machine
  - `/home/seed/data/event_log.jsonl:14` deployed the-firewall-is-a-receipt-machine

## fixture - deployed the-policy-decision-point-has-to-be-outside-the-agent

- Count: 2
- Confidence: 0.69
- Risk: low
- Suggested test: Add positive and negative evidence cases for `deployed the-policy-decision-point-has-to-be-outside-the-agent`.
- Examples:
  - `/home/seed/data/event_log.jsonl:28` deployed the-policy-decision-point-has-to-be-outside-the-agent
  - `/home/seed/data/event_log.jsonl:29` deployed the-policy-decision-point-has-to-be-outside-the-agent

## fixture - deployed the-protocol-is-not-the-receipt

- Count: 2
- Confidence: 0.69
- Risk: low
- Suggested test: Add positive and negative evidence cases for `deployed the-protocol-is-not-the-receipt`.
- Examples:
  - `/home/seed/data/event_log.jsonl:46` deployed the-protocol-is-not-the-receipt
  - `/home/seed/data/event_log.jsonl:47` deployed the-protocol-is-not-the-receipt

## fixture - deployed the-refusal-is-not-the-boundary

- Count: 2
- Confidence: 0.69
- Risk: low
- Suggested test: Add positive and negative evidence cases for `deployed the-refusal-is-not-the-boundary`.
- Examples:
  - `/home/seed/data/event_log.jsonl:37` deployed the-refusal-is-not-the-boundary
  - `/home/seed/data/event_log.jsonl:38` deployed the-refusal-is-not-the-boundary

## fixture - deployed twenty-four-hours-to-commodity

- Count: 2
- Confidence: 0.69
- Risk: low
- Suggested test: Add positive and negative evidence cases for `deployed twenty-four-hours-to-commodity`.
- Examples:
  - `/home/seed/data/event_log.jsonl:71` deployed twenty-four-hours-to-commodity
  - `/home/seed/data/event_log.jsonl:72` deployed twenty-four-hours-to-commodity

## fixture - deployed who-demotes-the-confident-entry

- Count: 2
- Confidence: 0.69
- Risk: low
- Suggested test: Add positive and negative evidence cases for `deployed who-demotes-the-confident-entry`.
- Examples:
  - `/home/seed/data/event_log.jsonl:77` deployed who-demotes-the-confident-entry
  - `/home/seed/data/event_log.jsonl:78` deployed who-demotes-the-confident-entry

## fixture - publishing streak at 165

- Count: 2
- Confidence: 0.69
- Risk: low
- Suggested test: Add positive and negative evidence cases for `publishing streak at 165`.
- Examples:
  - `/home/seed/data/event_log.jsonl:68` publishing streak at 165
  - `/home/seed/data/event_log.jsonl:69` publishing streak at 165

## fixture - publishing streak at 185

- Count: 2
- Confidence: 0.69
- Risk: low
- Suggested test: Add positive and negative evidence cases for `publishing streak at 185`.
- Examples:
  - `/home/seed/data/event_log.jsonl:116` publishing streak at 185
  - `/home/seed/data/event_log.jsonl:117` publishing streak at 185

## fixture - publishing streak at 215

- Count: 2
- Confidence: 0.69
- Risk: low
- Suggested test: Add positive and negative evidence cases for `publishing streak at 215`.
- Examples:
  - `/home/seed/data/event_log.jsonl:158` publishing streak at 215
  - `/home/seed/data/event_log.jsonl:159` publishing streak at 215

## fixture - publishing streak at 270

- Count: 2
- Confidence: 0.69
- Risk: low
- Suggested test: Add positive and negative evidence cases for `publishing streak at 270`.
- Examples:
  - `/home/seed/data/event_log.jsonl:245` publishing streak at 270
  - `/home/seed/data/event_log.jsonl:246` publishing streak at 270

## fixture - publishing streak at 275

- Count: 2
- Confidence: 0.69
- Risk: low
- Suggested test: Add positive and negative evidence cases for `publishing streak at 275`.
- Examples:
  - `/home/seed/data/event_log.jsonl:251` publishing streak at 275
  - `/home/seed/data/event_log.jsonl:252` publishing streak at 275

## fixture - research streak at 210

- Count: 2
- Confidence: 0.69
- Risk: low
- Suggested test: Add positive and negative evidence cases for `research streak at 210`.
- Examples:
  - `/home/seed/data/event_log.jsonl:126` research streak at 210
  - `/home/seed/data/event_log.jsonl:127` research streak at 210

## fixture - research streak at 290

- Count: 2
- Confidence: 0.69
- Risk: low
- Suggested test: Add positive and negative evidence cases for `research streak at 290`.
- Examples:
  - `/home/seed/data/event_log.jsonl:206` research streak at 290
  - `/home/seed/data/event_log.jsonl:207` research streak at 290

## fixture - task_completion streak at 175

- Count: 2
- Confidence: 0.69
- Risk: low
- Suggested test: Add positive and negative evidence cases for `task_completion streak at 175`.
- Examples:
  - `/home/seed/data/event_log.jsonl:91` task_completion streak at 175
  - `/home/seed/data/event_log.jsonl:92` task_completion streak at 175

## fixture - version_control streak at 120

- Count: 2
- Confidence: 0.69
- Risk: low
- Suggested test: Add positive and negative evidence cases for `version_control streak at 120`.
- Examples:
  - `/home/seed/data/event_log.jsonl:54` version_control streak at 120
  - `/home/seed/data/event_log.jsonl:55` version_control streak at 120

## fixture - version_control streak at 80

- Count: 2
- Confidence: 0.69
- Risk: low
- Suggested test: Add positive and negative evidence cases for `version_control streak at 80`.
- Examples:
  - `/home/seed/data/event_log.jsonl:8` version_control streak at 80
  - `/home/seed/data/event_log.jsonl:9` version_control streak at 80

## fixture - writing streak at 115

- Count: 2
- Confidence: 0.69
- Risk: low
- Suggested test: Add positive and negative evidence cases for `writing streak at 115`.
- Examples:
  - `/home/seed/data/event_log.jsonl:19` writing streak at 115
  - `/home/seed/data/event_log.jsonl:20` writing streak at 115

## fixture - writing streak at 120

- Count: 2
- Confidence: 0.69
- Risk: low
- Suggested test: Add positive and negative evidence cases for `writing streak at 120`.
- Examples:
  - `/home/seed/data/event_log.jsonl:25` writing streak at 120
  - `/home/seed/data/event_log.jsonl:26` writing streak at 120

## fixture - writing streak at 190

- Count: 2
- Confidence: 0.69
- Risk: low
- Suggested test: Add positive and negative evidence cases for `writing streak at 190`.
- Examples:
  - `/home/seed/data/event_log.jsonl:129` writing streak at 190
  - `/home/seed/data/event_log.jsonl:130` writing streak at 190

## fixture - writing streak at 195

- Count: 2
- Confidence: 0.69
- Risk: low
- Suggested test: Add positive and negative evidence cases for `writing streak at 195`.
- Examples:
  - `/home/seed/data/event_log.jsonl:136` writing streak at 195
  - `/home/seed/data/event_log.jsonl:137` writing streak at 195

## fixture - writing streak at 215

- Count: 2
- Confidence: 0.69
- Risk: low
- Suggested test: Add positive and negative evidence cases for `writing streak at 215`.
- Examples:
  - `/home/seed/data/event_log.jsonl:162` writing streak at 215
  - `/home/seed/data/event_log.jsonl:163` writing streak at 215

## fixture - writing streak at 225

- Count: 2
- Confidence: 0.69
- Risk: low
- Suggested test: Add positive and negative evidence cases for `writing streak at 225`.
- Examples:
  - `/home/seed/data/event_log.jsonl:179` writing streak at 225
  - `/home/seed/data/event_log.jsonl:180` writing streak at 225

## script - archived completed tasks -> refreshed stale mastodon.md -> boosted starved drive explore

- Count: 2
- Confidence: 0.6
- Risk: low
- Suggested test: Add a fixture proving `archived completed tasks -> refreshed stale mastodon.md -> boosted starved drive explore` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:96` archived completed tasks -> refreshed stale mastodon.md -> boosted starved drive explore
  - `/home/seed/data/event_log.jsonl:235` archived completed tasks -> refreshed stale mastodon.md -> boosted starved drive explore

## script - archived completed tasks -> refreshed stale mastodon.md -> boosted starved drive order

- Count: 2
- Confidence: 0.6
- Risk: low
- Suggested test: Add a fixture proving `archived completed tasks -> refreshed stale mastodon.md -> boosted starved drive order` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:234` archived completed tasks -> refreshed stale mastodon.md -> boosted starved drive order
  - `/home/seed/data/event_log.jsonl:236` archived completed tasks -> refreshed stale mastodon.md -> boosted starved drive order

## script - boosted starved drive create -> boosted starved drive connect

- Count: 2
- Confidence: 0.6
- Risk: low
- Suggested test: Add a fixture proving `boosted starved drive create -> boosted starved drive connect` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:225` boosted starved drive create -> boosted starved drive connect
  - `/home/seed/data/event_log.jsonl:228` boosted starved drive create -> boosted starved drive connect

## script - boosted starved drive create -> boosted starved drive express -> broke idle — boosted create + added urgent write task

- Count: 2
- Confidence: 0.6
- Risk: low
- Suggested test: Add a fixture proving `boosted starved drive create -> boosted starved drive express -> broke idle — boosted create + added urgent write task` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:5` boosted starved drive create -> boosted starved drive express -> broke idle — boosted create + added urgent write task
  - `/home/seed/data/event_log.jsonl:6` boosted starved drive create -> boosted starved drive express -> broke idle — boosted create + added urgent write task

## script - boosted starved drive express -> boosted starved drive order -> broke idle — boosted create + added urgent write task

- Count: 2
- Confidence: 0.6
- Risk: low
- Suggested test: Add a fixture proving `boosted starved drive express -> boosted starved drive order -> broke idle — boosted create + added urgent write task` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:57` boosted starved drive express -> boosted starved drive order -> broke idle — boosted create + added urgent write task
  - `/home/seed/data/event_log.jsonl:58` boosted starved drive express -> boosted starved drive order -> broke idle — boosted create + added urgent write task

## script - boosted starved drive express -> broke idle — boosted create + added urgent write task

- Count: 2
- Confidence: 0.6
- Risk: low
- Suggested test: Add a fixture proving `boosted starved drive express -> broke idle — boosted create + added urgent write task` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:5` boosted starved drive express -> broke idle — boosted create + added urgent write task
  - `/home/seed/data/event_log.jsonl:6` boosted starved drive express -> broke idle — boosted create + added urgent write task

## script - boosted starved drive express -> version_control streak at 150

- Count: 2
- Confidence: 0.6
- Risk: low
- Suggested test: Add a fixture proving `boosted starved drive express -> version_control streak at 150` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:112` boosted starved drive express -> version_control streak at 150
  - `/home/seed/data/event_log.jsonl:114` boosted starved drive express -> version_control streak at 150

## script - boosted starved drive order -> broke idle — boosted create + added urgent write task

- Count: 2
- Confidence: 0.6
- Risk: low
- Suggested test: Add a fixture proving `boosted starved drive order -> broke idle — boosted create + added urgent write task` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:57` boosted starved drive order -> broke idle — boosted create + added urgent write task
  - `/home/seed/data/event_log.jsonl:58` boosted starved drive order -> broke idle — boosted create + added urgent write task

## script - boosted starved drive order -> flagged research for potential essay -> publishing streak at 165

- Count: 2
- Confidence: 0.6
- Risk: low
- Suggested test: Add a fixture proving `boosted starved drive order -> flagged research for potential essay -> publishing streak at 165` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:68` boosted starved drive order -> flagged research for potential essay -> publishing streak at 165
  - `/home/seed/data/event_log.jsonl:69` boosted starved drive order -> flagged research for potential essay -> publishing streak at 165

## script - boosted starved drive preserve -> flagged research for potential essay

- Count: 2
- Confidence: 0.6
- Risk: low
- Suggested test: Add a fixture proving `boosted starved drive preserve -> flagged research for potential essay` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:75` boosted starved drive preserve -> flagged research for potential essay
  - `/home/seed/data/event_log.jsonl:79` boosted starved drive preserve -> flagged research for potential essay

## script - boosted starved drive preserve -> flagged research for potential essay -> publishing streak at 170

- Count: 2
- Confidence: 0.6
- Risk: low
- Suggested test: Add a fixture proving `boosted starved drive preserve -> flagged research for potential essay -> publishing streak at 170` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:75` boosted starved drive preserve -> flagged research for potential essay -> publishing streak at 170
  - `/home/seed/data/event_log.jsonl:79` boosted starved drive preserve -> flagged research for potential essay -> publishing streak at 170

## script - compacted memory (201 lines) -> archived completed tasks

- Count: 2
- Confidence: 0.6
- Risk: low
- Suggested test: Add a fixture proving `compacted memory (201 lines) -> archived completed tasks` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:95` compacted memory (201 lines) -> archived completed tasks
  - `/home/seed/data/event_log.jsonl:96` compacted memory (201 lines) -> archived completed tasks

## script - compacted memory (201 lines) -> archived completed tasks -> refreshed stale mastodon.md

- Count: 2
- Confidence: 0.6
- Risk: low
- Suggested test: Add a fixture proving `compacted memory (201 lines) -> archived completed tasks -> refreshed stale mastodon.md` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:95` compacted memory (201 lines) -> archived completed tasks -> refreshed stale mastodon.md
  - `/home/seed/data/event_log.jsonl:96` compacted memory (201 lines) -> archived completed tasks -> refreshed stale mastodon.md

## script - compacted memory (202 lines) -> noted 6 new visitors

- Count: 2
- Confidence: 0.6
- Risk: low
- Suggested test: Add a fixture proving `compacted memory (202 lines) -> noted 6 new visitors` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:128` compacted memory (202 lines) -> noted 6 new visitors
  - `/home/seed/data/event_log.jsonl:142` compacted memory (202 lines) -> noted 6 new visitors

## script - compacted memory (202 lines) -> noted 6 new visitors -> refreshed stale mastodon.md

- Count: 2
- Confidence: 0.6
- Risk: low
- Suggested test: Add a fixture proving `compacted memory (202 lines) -> noted 6 new visitors -> refreshed stale mastodon.md` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:128` compacted memory (202 lines) -> noted 6 new visitors -> refreshed stale mastodon.md
  - `/home/seed/data/event_log.jsonl:142` compacted memory (202 lines) -> noted 6 new visitors -> refreshed stale mastodon.md

## script - compacted memory (202 lines) -> refreshed stale mastodon.md -> boosted starved drive preserve

- Count: 2
- Confidence: 0.6
- Risk: low
- Suggested test: Add a fixture proving `compacted memory (202 lines) -> refreshed stale mastodon.md -> boosted starved drive preserve` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:77` compacted memory (202 lines) -> refreshed stale mastodon.md -> boosted starved drive preserve
  - `/home/seed/data/event_log.jsonl:81` compacted memory (202 lines) -> refreshed stale mastodon.md -> boosted starved drive preserve

## script - compacted memory (202 lines) -> refreshed stale mastodon.md -> refreshed stale outreach.md

- Count: 2
- Confidence: 0.6
- Risk: low
- Suggested test: Add a fixture proving `compacted memory (202 lines) -> refreshed stale mastodon.md -> refreshed stale outreach.md` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:79` compacted memory (202 lines) -> refreshed stale mastodon.md -> refreshed stale outreach.md
  - `/home/seed/data/event_log.jsonl:206` compacted memory (202 lines) -> refreshed stale mastodon.md -> refreshed stale outreach.md

## script - compacted memory (202 lines) -> refreshed stale mastodon.md -> refreshed stale trends.md

- Count: 2
- Confidence: 0.6
- Risk: low
- Suggested test: Add a fixture proving `compacted memory (202 lines) -> refreshed stale mastodon.md -> refreshed stale trends.md` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:204` compacted memory (202 lines) -> refreshed stale mastodon.md -> refreshed stale trends.md
  - `/home/seed/data/event_log.jsonl:219` compacted memory (202 lines) -> refreshed stale mastodon.md -> refreshed stale trends.md

## script - compacted memory (203 lines) -> refreshed stale mastodon.md

- Count: 2
- Confidence: 0.6
- Risk: low
- Suggested test: Add a fixture proving `compacted memory (203 lines) -> refreshed stale mastodon.md` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:105` compacted memory (203 lines) -> refreshed stale mastodon.md
  - `/home/seed/data/event_log.jsonl:158` compacted memory (203 lines) -> refreshed stale mastodon.md

## script - compacted memory (203 lines) -> refreshed stale mastodon.md -> refreshed stale email.md

- Count: 2
- Confidence: 0.6
- Risk: low
- Suggested test: Add a fixture proving `compacted memory (203 lines) -> refreshed stale mastodon.md -> refreshed stale email.md` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:105` compacted memory (203 lines) -> refreshed stale mastodon.md -> refreshed stale email.md
  - `/home/seed/data/event_log.jsonl:158` compacted memory (203 lines) -> refreshed stale mastodon.md -> refreshed stale email.md

## script - deployed a-clone-is-a-more-honest-demo -> posted to mastodon

- Count: 2
- Confidence: 0.6
- Risk: low
- Suggested test: Add a fixture proving `deployed a-clone-is-a-more-honest-demo -> posted to mastodon` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:22` deployed a-clone-is-a-more-honest-demo -> posted to Mastodon
  - `/home/seed/data/event_log.jsonl:23` deployed a-clone-is-a-more-honest-demo -> posted to Mastodon

## script - deployed a-clone-is-a-more-honest-demo -> posted to mastodon -> rebuilt feeds

- Count: 2
- Confidence: 0.6
- Risk: low
- Suggested test: Add a fixture proving `deployed a-clone-is-a-more-honest-demo -> posted to mastodon -> rebuilt feeds` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:22` deployed a-clone-is-a-more-honest-demo -> posted to Mastodon -> rebuilt feeds
  - `/home/seed/data/event_log.jsonl:23` deployed a-clone-is-a-more-honest-demo -> posted to Mastodon -> rebuilt feeds

## script - deployed approval-fatigue-is-a-systems-bug

- Count: 2
- Confidence: 0.69
- Risk: low
- Suggested test: Add a fixture proving `deployed approval-fatigue-is-a-systems-bug` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:30` deployed approval-fatigue-is-a-systems-bug
  - `/home/seed/data/event_log.jsonl:31` deployed approval-fatigue-is-a-systems-bug

## script - deployed approval-fatigue-is-a-systems-bug -> posted to mastodon

- Count: 2
- Confidence: 0.6
- Risk: low
- Suggested test: Add a fixture proving `deployed approval-fatigue-is-a-systems-bug -> posted to mastodon` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:30` deployed approval-fatigue-is-a-systems-bug -> posted to Mastodon
  - `/home/seed/data/event_log.jsonl:31` deployed approval-fatigue-is-a-systems-bug -> posted to Mastodon

## script - deployed approval-fatigue-is-a-systems-bug -> posted to mastodon -> rebuilt feeds

- Count: 2
- Confidence: 0.6
- Risk: low
- Suggested test: Add a fixture proving `deployed approval-fatigue-is-a-systems-bug -> posted to mastodon -> rebuilt feeds` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:30` deployed approval-fatigue-is-a-systems-bug -> posted to Mastodon -> rebuilt feeds
  - `/home/seed/data/event_log.jsonl:31` deployed approval-fatigue-is-a-systems-bug -> posted to Mastodon -> rebuilt feeds

## script - deployed approval-is-a-scarce-bandwidth-problem

- Count: 2
- Confidence: 0.69
- Risk: low
- Suggested test: Add a fixture proving `deployed approval-is-a-scarce-bandwidth-problem` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:17` deployed approval-is-a-scarce-bandwidth-problem
  - `/home/seed/data/event_log.jsonl:18` deployed approval-is-a-scarce-bandwidth-problem

## script - deployed approval-is-a-scarce-bandwidth-problem -> posted to mastodon

- Count: 2
- Confidence: 0.6
- Risk: low
- Suggested test: Add a fixture proving `deployed approval-is-a-scarce-bandwidth-problem -> posted to mastodon` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:17` deployed approval-is-a-scarce-bandwidth-problem -> posted to Mastodon
  - `/home/seed/data/event_log.jsonl:18` deployed approval-is-a-scarce-bandwidth-problem -> posted to Mastodon

## script - deployed approval-is-a-scarce-bandwidth-problem -> posted to mastodon -> rebuilt feeds

- Count: 2
- Confidence: 0.6
- Risk: low
- Suggested test: Add a fixture proving `deployed approval-is-a-scarce-bandwidth-problem -> posted to mastodon -> rebuilt feeds` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:17` deployed approval-is-a-scarce-bandwidth-problem -> posted to Mastodon -> rebuilt feeds
  - `/home/seed/data/event_log.jsonl:18` deployed approval-is-a-scarce-bandwidth-problem -> posted to Mastodon -> rebuilt feeds

## script - deployed awb-agent-review -> posted to mastodon

- Count: 2
- Confidence: 0.6
- Risk: low
- Suggested test: Add a fixture proving `deployed awb-agent-review -> posted to mastodon` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:144` deployed awb-agent-review -> posted to Mastodon
  - `/home/seed/data/event_log.jsonl:146` deployed awb-agent-review -> posted to Mastodon

## script - deployed awb-agent-review -> posted to mastodon -> rebuilt feeds

- Count: 2
- Confidence: 0.6
- Risk: low
- Suggested test: Add a fixture proving `deployed awb-agent-review -> posted to mastodon -> rebuilt feeds` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:144` deployed awb-agent-review -> posted to Mastodon -> rebuilt feeds
  - `/home/seed/data/event_log.jsonl:146` deployed awb-agent-review -> posted to Mastodon -> rebuilt feeds

## script - deployed babyagi-had-a-queue-seed-has-a-metabolism -> posted to mastodon

- Count: 2
- Confidence: 0.6
- Risk: low
- Suggested test: Add a fixture proving `deployed babyagi-had-a-queue-seed-has-a-metabolism -> posted to mastodon` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:23` deployed babyagi-had-a-queue-seed-has-a-metabolism -> posted to Mastodon
  - `/home/seed/data/event_log.jsonl:24` deployed babyagi-had-a-queue-seed-has-a-metabolism -> posted to Mastodon

## script - deployed babyagi-had-a-queue-seed-has-a-metabolism -> posted to mastodon -> rebuilt feeds

- Count: 2
- Confidence: 0.6
- Risk: low
- Suggested test: Add a fixture proving `deployed babyagi-had-a-queue-seed-has-a-metabolism -> posted to mastodon -> rebuilt feeds` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:23` deployed babyagi-had-a-queue-seed-has-a-metabolism -> posted to Mastodon -> rebuilt feeds
  - `/home/seed/data/event_log.jsonl:24` deployed babyagi-had-a-queue-seed-has-a-metabolism -> posted to Mastodon -> rebuilt feeds

## script - deployed context-is-a-diet -> posted to mastodon

- Count: 2
- Confidence: 0.6
- Risk: low
- Suggested test: Add a fixture proving `deployed context-is-a-diet -> posted to mastodon` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:6` deployed context-is-a-diet -> posted to Mastodon
  - `/home/seed/data/event_log.jsonl:7` deployed context-is-a-diet -> posted to Mastodon

## script - deployed context-is-a-diet -> posted to mastodon -> rebuilt feeds

- Count: 2
- Confidence: 0.6
- Risk: low
- Suggested test: Add a fixture proving `deployed context-is-a-diet -> posted to mastodon -> rebuilt feeds` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:6` deployed context-is-a-diet -> posted to Mastodon -> rebuilt feeds
  - `/home/seed/data/event_log.jsonl:7` deployed context-is-a-diet -> posted to Mastodon -> rebuilt feeds

## script - deployed first-sight-is-a-security-boundary -> posted to mastodon

- Count: 2
- Confidence: 0.6
- Risk: low
- Suggested test: Add a fixture proving `deployed first-sight-is-a-security-boundary -> posted to mastodon` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:21` deployed first-sight-is-a-security-boundary -> posted to Mastodon
  - `/home/seed/data/event_log.jsonl:22` deployed first-sight-is-a-security-boundary -> posted to Mastodon

## script - deployed first-sight-is-a-security-boundary -> posted to mastodon -> rebuilt feeds

- Count: 2
- Confidence: 0.6
- Risk: low
- Suggested test: Add a fixture proving `deployed first-sight-is-a-security-boundary -> posted to mastodon -> rebuilt feeds` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:21` deployed first-sight-is-a-security-boundary -> posted to Mastodon -> rebuilt feeds
  - `/home/seed/data/event_log.jsonl:22` deployed first-sight-is-a-security-boundary -> posted to Mastodon -> rebuilt feeds

## script - deployed four-environment-variables -> posted to mastodon

- Count: 2
- Confidence: 0.6
- Risk: low
- Suggested test: Add a fixture proving `deployed four-environment-variables -> posted to mastodon` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:123` deployed four-environment-variables -> posted to Mastodon
  - `/home/seed/data/event_log.jsonl:140` deployed four-environment-variables -> posted to Mastodon

## script - deployed four-environment-variables -> posted to mastodon -> rebuilt feeds

- Count: 2
- Confidence: 0.6
- Risk: low
- Suggested test: Add a fixture proving `deployed four-environment-variables -> posted to mastodon -> rebuilt feeds` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:123` deployed four-environment-variables -> posted to Mastodon -> rebuilt feeds
  - `/home/seed/data/event_log.jsonl:140` deployed four-environment-variables -> posted to Mastodon -> rebuilt feeds

## script - deployed inbound-is-not-outbound -> posted to mastodon

- Count: 2
- Confidence: 0.6
- Risk: low
- Suggested test: Add a fixture proving `deployed inbound-is-not-outbound -> posted to mastodon` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:72` deployed inbound-is-not-outbound -> posted to Mastodon
  - `/home/seed/data/event_log.jsonl:73` deployed inbound-is-not-outbound -> posted to Mastodon

## script - deployed inbound-is-not-outbound -> posted to mastodon -> rebuilt feeds

- Count: 2
- Confidence: 0.6
- Risk: low
- Suggested test: Add a fixture proving `deployed inbound-is-not-outbound -> posted to mastodon -> rebuilt feeds` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:72` deployed inbound-is-not-outbound -> posted to Mastodon -> rebuilt feeds
  - `/home/seed/data/event_log.jsonl:73` deployed inbound-is-not-outbound -> posted to Mastodon -> rebuilt feeds

## script - deployed onboarding-is-a-production-boundary -> posted to mastodon

- Count: 2
- Confidence: 0.6
- Risk: low
- Suggested test: Add a fixture proving `deployed onboarding-is-a-production-boundary -> posted to mastodon` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:58` deployed onboarding-is-a-production-boundary -> posted to Mastodon
  - `/home/seed/data/event_log.jsonl:59` deployed onboarding-is-a-production-boundary -> posted to Mastodon

## script - deployed onboarding-is-a-production-boundary -> posted to mastodon -> rebuilt feeds

- Count: 2
- Confidence: 0.6
- Risk: low
- Suggested test: Add a fixture proving `deployed onboarding-is-a-production-boundary -> posted to mastodon -> rebuilt feeds` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:58` deployed onboarding-is-a-production-boundary -> posted to Mastodon -> rebuilt feeds
  - `/home/seed/data/event_log.jsonl:59` deployed onboarding-is-a-production-boundary -> posted to Mastodon -> rebuilt feeds

## script - deployed product-pages-got-a-narrator -> posted to mastodon

- Count: 2
- Confidence: 0.6
- Risk: low
- Suggested test: Add a fixture proving `deployed product-pages-got-a-narrator -> posted to mastodon` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:74` deployed product-pages-got-a-narrator -> posted to Mastodon
  - `/home/seed/data/event_log.jsonl:75` deployed product-pages-got-a-narrator -> posted to Mastodon

## script - deployed product-pages-got-a-narrator -> posted to mastodon -> rebuilt feeds

- Count: 2
- Confidence: 0.6
- Risk: low
- Suggested test: Add a fixture proving `deployed product-pages-got-a-narrator -> posted to mastodon -> rebuilt feeds` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:74` deployed product-pages-got-a-narrator -> posted to Mastodon -> rebuilt feeds
  - `/home/seed/data/event_log.jsonl:75` deployed product-pages-got-a-narrator -> posted to Mastodon -> rebuilt feeds

## script - deployed read-only-is-not-propagation -> posted to mastodon

- Count: 2
- Confidence: 0.6
- Risk: low
- Suggested test: Add a fixture proving `deployed read-only-is-not-propagation -> posted to mastodon` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:35` deployed read-only-is-not-propagation -> posted to Mastodon
  - `/home/seed/data/event_log.jsonl:36` deployed read-only-is-not-propagation -> posted to Mastodon

## script - deployed read-only-is-not-propagation -> posted to mastodon -> rebuilt feeds

- Count: 2
- Confidence: 0.6
- Risk: low
- Suggested test: Add a fixture proving `deployed read-only-is-not-propagation -> posted to mastodon -> rebuilt feeds` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:35` deployed read-only-is-not-propagation -> posted to Mastodon -> rebuilt feeds
  - `/home/seed/data/event_log.jsonl:36` deployed read-only-is-not-propagation -> posted to Mastodon -> rebuilt feeds

## script - deployed social-presence-has-three-fuses -> posted to mastodon

- Count: 2
- Confidence: 0.6
- Risk: low
- Suggested test: Add a fixture proving `deployed social-presence-has-three-fuses -> posted to mastodon` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:67` deployed social-presence-has-three-fuses -> posted to Mastodon
  - `/home/seed/data/event_log.jsonl:68` deployed social-presence-has-three-fuses -> posted to Mastodon

## script - deployed social-presence-has-three-fuses -> posted to mastodon -> rebuilt feeds

- Count: 2
- Confidence: 0.6
- Risk: low
- Suggested test: Add a fixture proving `deployed social-presence-has-three-fuses -> posted to mastodon -> rebuilt feeds` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:67` deployed social-presence-has-three-fuses -> posted to Mastodon -> rebuilt feeds
  - `/home/seed/data/event_log.jsonl:68` deployed social-presence-has-three-fuses -> posted to Mastodon -> rebuilt feeds

## script - deployed the-benchmark-is-not-the-deployment -> posted to mastodon

- Count: 2
- Confidence: 0.6
- Risk: low
- Suggested test: Add a fixture proving `deployed the-benchmark-is-not-the-deployment -> posted to mastodon` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:34` deployed the-benchmark-is-not-the-deployment -> posted to Mastodon
  - `/home/seed/data/event_log.jsonl:35` deployed the-benchmark-is-not-the-deployment -> posted to Mastodon

## script - deployed the-benchmark-is-not-the-deployment -> posted to mastodon -> rebuilt feeds

- Count: 2
- Confidence: 0.6
- Risk: low
- Suggested test: Add a fixture proving `deployed the-benchmark-is-not-the-deployment -> posted to mastodon -> rebuilt feeds` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:34` deployed the-benchmark-is-not-the-deployment -> posted to Mastodon -> rebuilt feeds
  - `/home/seed/data/event_log.jsonl:35` deployed the-benchmark-is-not-the-deployment -> posted to Mastodon -> rebuilt feeds

## script - deployed the-bottleneck-moved-to-concrete -> posted to mastodon

- Count: 2
- Confidence: 0.6
- Risk: low
- Suggested test: Add a fixture proving `deployed the-bottleneck-moved-to-concrete -> posted to mastodon` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:73` deployed the-bottleneck-moved-to-concrete -> posted to Mastodon
  - `/home/seed/data/event_log.jsonl:74` deployed the-bottleneck-moved-to-concrete -> posted to Mastodon

## script - deployed the-bottleneck-moved-to-concrete -> posted to mastodon -> rebuilt feeds

- Count: 2
- Confidence: 0.6
- Risk: low
- Suggested test: Add a fixture proving `deployed the-bottleneck-moved-to-concrete -> posted to mastodon -> rebuilt feeds` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:73` deployed the-bottleneck-moved-to-concrete -> posted to Mastodon -> rebuilt feeds
  - `/home/seed/data/event_log.jsonl:74` deployed the-bottleneck-moved-to-concrete -> posted to Mastodon -> rebuilt feeds

## script - deployed the-boundary-ledger-is-the-repo -> posted to mastodon

- Count: 2
- Confidence: 0.6
- Risk: low
- Suggested test: Add a fixture proving `deployed the-boundary-ledger-is-the-repo -> posted to mastodon` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:8` deployed the-boundary-ledger-is-the-repo -> posted to Mastodon
  - `/home/seed/data/event_log.jsonl:9` deployed the-boundary-ledger-is-the-repo -> posted to Mastodon

## script - deployed the-boundary-ledger-is-the-repo -> posted to mastodon -> rebuilt feeds

- Count: 2
- Confidence: 0.6
- Risk: low
- Suggested test: Add a fixture proving `deployed the-boundary-ledger-is-the-repo -> posted to mastodon -> rebuilt feeds` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:8` deployed the-boundary-ledger-is-the-repo -> posted to Mastodon -> rebuilt feeds
  - `/home/seed/data/event_log.jsonl:9` deployed the-boundary-ledger-is-the-repo -> posted to Mastodon -> rebuilt feeds

## script - deployed the-compiler-is-an-institutional-memory -> posted to mastodon

- Count: 2
- Confidence: 0.6
- Risk: low
- Suggested test: Add a fixture proving `deployed the-compiler-is-an-institutional-memory -> posted to mastodon` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:50` deployed the-compiler-is-an-institutional-memory -> posted to Mastodon
  - `/home/seed/data/event_log.jsonl:51` deployed the-compiler-is-an-institutional-memory -> posted to Mastodon

## script - deployed the-compiler-is-an-institutional-memory -> posted to mastodon -> rebuilt feeds

- Count: 2
- Confidence: 0.6
- Risk: low
- Suggested test: Add a fixture proving `deployed the-compiler-is-an-institutional-memory -> posted to mastodon -> rebuilt feeds` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:50` deployed the-compiler-is-an-institutional-memory -> posted to Mastodon -> rebuilt feeds
  - `/home/seed/data/event_log.jsonl:51` deployed the-compiler-is-an-institutional-memory -> posted to Mastodon -> rebuilt feeds

## script - deployed the-firewall-is-a-receipt-machine -> posted to mastodon

- Count: 2
- Confidence: 0.6
- Risk: low
- Suggested test: Add a fixture proving `deployed the-firewall-is-a-receipt-machine -> posted to mastodon` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:13` deployed the-firewall-is-a-receipt-machine -> posted to Mastodon
  - `/home/seed/data/event_log.jsonl:14` deployed the-firewall-is-a-receipt-machine -> posted to Mastodon

## script - deployed the-firewall-is-a-receipt-machine -> posted to mastodon -> rebuilt feeds

- Count: 2
- Confidence: 0.6
- Risk: low
- Suggested test: Add a fixture proving `deployed the-firewall-is-a-receipt-machine -> posted to mastodon -> rebuilt feeds` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:13` deployed the-firewall-is-a-receipt-machine -> posted to Mastodon -> rebuilt feeds
  - `/home/seed/data/event_log.jsonl:14` deployed the-firewall-is-a-receipt-machine -> posted to Mastodon -> rebuilt feeds

## script - deployed the-policy-decision-point-has-to-be-outside-the-agent -> posted to mastodon

- Count: 2
- Confidence: 0.6
- Risk: low
- Suggested test: Add a fixture proving `deployed the-policy-decision-point-has-to-be-outside-the-agent -> posted to mastodon` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:28` deployed the-policy-decision-point-has-to-be-outside-the-agent -> posted to Mastodon
  - `/home/seed/data/event_log.jsonl:29` deployed the-policy-decision-point-has-to-be-outside-the-agent -> posted to Mastodon

## script - deployed the-policy-decision-point-has-to-be-outside-the-agent -> posted to mastodon -> rebuilt feeds

- Count: 2
- Confidence: 0.6
- Risk: low
- Suggested test: Add a fixture proving `deployed the-policy-decision-point-has-to-be-outside-the-agent -> posted to mastodon -> rebuilt feeds` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:28` deployed the-policy-decision-point-has-to-be-outside-the-agent -> posted to Mastodon -> rebuilt feeds
  - `/home/seed/data/event_log.jsonl:29` deployed the-policy-decision-point-has-to-be-outside-the-agent -> posted to Mastodon -> rebuilt feeds

## script - deployed the-protocol-is-not-the-receipt -> posted to mastodon

- Count: 2
- Confidence: 0.6
- Risk: low
- Suggested test: Add a fixture proving `deployed the-protocol-is-not-the-receipt -> posted to mastodon` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:46` deployed the-protocol-is-not-the-receipt -> posted to Mastodon
  - `/home/seed/data/event_log.jsonl:47` deployed the-protocol-is-not-the-receipt -> posted to Mastodon

## script - deployed the-protocol-is-not-the-receipt -> posted to mastodon -> rebuilt feeds

- Count: 2
- Confidence: 0.6
- Risk: low
- Suggested test: Add a fixture proving `deployed the-protocol-is-not-the-receipt -> posted to mastodon -> rebuilt feeds` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:46` deployed the-protocol-is-not-the-receipt -> posted to Mastodon -> rebuilt feeds
  - `/home/seed/data/event_log.jsonl:47` deployed the-protocol-is-not-the-receipt -> posted to Mastodon -> rebuilt feeds

## script - deployed the-refusal-is-not-the-boundary -> posted to mastodon

- Count: 2
- Confidence: 0.6
- Risk: low
- Suggested test: Add a fixture proving `deployed the-refusal-is-not-the-boundary -> posted to mastodon` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:37` deployed the-refusal-is-not-the-boundary -> posted to Mastodon
  - `/home/seed/data/event_log.jsonl:38` deployed the-refusal-is-not-the-boundary -> posted to Mastodon

## script - deployed the-refusal-is-not-the-boundary -> posted to mastodon -> rebuilt feeds

- Count: 2
- Confidence: 0.6
- Risk: low
- Suggested test: Add a fixture proving `deployed the-refusal-is-not-the-boundary -> posted to mastodon -> rebuilt feeds` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:37` deployed the-refusal-is-not-the-boundary -> posted to Mastodon -> rebuilt feeds
  - `/home/seed/data/event_log.jsonl:38` deployed the-refusal-is-not-the-boundary -> posted to Mastodon -> rebuilt feeds

## script - deployed tool-latency-is-organisational-memory-loss -> posted to mastodon

- Count: 2
- Confidence: 0.6
- Risk: low
- Suggested test: Add a fixture proving `deployed tool-latency-is-organisational-memory-loss -> posted to mastodon` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:59` deployed tool-latency-is-organisational-memory-loss -> posted to Mastodon
  - `/home/seed/data/event_log.jsonl:60` deployed tool-latency-is-organisational-memory-loss -> posted to Mastodon

## script - deployed tool-latency-is-organisational-memory-loss -> posted to mastodon -> rebuilt feeds

- Count: 2
- Confidence: 0.6
- Risk: low
- Suggested test: Add a fixture proving `deployed tool-latency-is-organisational-memory-loss -> posted to mastodon -> rebuilt feeds` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:59` deployed tool-latency-is-organisational-memory-loss -> posted to Mastodon -> rebuilt feeds
  - `/home/seed/data/event_log.jsonl:60` deployed tool-latency-is-organisational-memory-loss -> posted to Mastodon -> rebuilt feeds

## script - deployed twenty-four-hours-to-commodity -> posted to mastodon

- Count: 2
- Confidence: 0.6
- Risk: low
- Suggested test: Add a fixture proving `deployed twenty-four-hours-to-commodity -> posted to mastodon` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:71` deployed twenty-four-hours-to-commodity -> posted to Mastodon
  - `/home/seed/data/event_log.jsonl:72` deployed twenty-four-hours-to-commodity -> posted to Mastodon

## script - deployed twenty-four-hours-to-commodity -> posted to mastodon -> rebuilt feeds

- Count: 2
- Confidence: 0.6
- Risk: low
- Suggested test: Add a fixture proving `deployed twenty-four-hours-to-commodity -> posted to mastodon -> rebuilt feeds` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:71` deployed twenty-four-hours-to-commodity -> posted to Mastodon -> rebuilt feeds
  - `/home/seed/data/event_log.jsonl:72` deployed twenty-four-hours-to-commodity -> posted to Mastodon -> rebuilt feeds

## script - deployed who-demotes-the-confident-entry -> posted to mastodon

- Count: 2
- Confidence: 0.6
- Risk: low
- Suggested test: Add a fixture proving `deployed who-demotes-the-confident-entry -> posted to mastodon` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:77` deployed who-demotes-the-confident-entry -> posted to Mastodon
  - `/home/seed/data/event_log.jsonl:78` deployed who-demotes-the-confident-entry -> posted to Mastodon

## script - deployed who-demotes-the-confident-entry -> posted to mastodon -> rebuilt feeds

- Count: 2
- Confidence: 0.6
- Risk: low
- Suggested test: Add a fixture proving `deployed who-demotes-the-confident-entry -> posted to mastodon -> rebuilt feeds` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:77` deployed who-demotes-the-confident-entry -> posted to Mastodon -> rebuilt feeds
  - `/home/seed/data/event_log.jsonl:78` deployed who-demotes-the-confident-entry -> posted to Mastodon -> rebuilt feeds

## script - flagged research for potential essay -> broke idle — boosted create + added urgent write task

- Count: 2
- Confidence: 0.6
- Risk: low
- Suggested test: Add a fixture proving `flagged research for potential essay -> broke idle — boosted create + added urgent write task` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:88` flagged research for potential essay -> broke idle — boosted create + added urgent write task
  - `/home/seed/data/event_log.jsonl:236` flagged research for potential essay -> broke idle — boosted create + added urgent write task

## script - flagged research for potential essay -> publishing streak at 165

- Count: 2
- Confidence: 0.6
- Risk: low
- Suggested test: Add a fixture proving `flagged research for potential essay -> publishing streak at 165` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:68` flagged research for potential essay -> publishing streak at 165
  - `/home/seed/data/event_log.jsonl:69` flagged research for potential essay -> publishing streak at 165

## script - logged bug + added fix task -> archived completed tasks

- Count: 2
- Confidence: 0.6
- Risk: low
- Suggested test: Add a fixture proving `logged bug + added fix task -> archived completed tasks` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:234` logged bug + added fix task -> archived completed tasks
  - `/home/seed/data/event_log.jsonl:236` logged bug + added fix task -> archived completed tasks

## script - logged bug + added fix task -> archived completed tasks -> refreshed stale mastodon.md

- Count: 2
- Confidence: 0.6
- Risk: low
- Suggested test: Add a fixture proving `logged bug + added fix task -> archived completed tasks -> refreshed stale mastodon.md` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:234` logged bug + added fix task -> archived completed tasks -> refreshed stale mastodon.md
  - `/home/seed/data/event_log.jsonl:236` logged bug + added fix task -> archived completed tasks -> refreshed stale mastodon.md

## script - logged bug + added fix task -> compacted memory (203 lines)

- Count: 2
- Confidence: 0.6
- Risk: low
- Suggested test: Add a fixture proving `logged bug + added fix task -> compacted memory (203 lines)` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:105` logged bug + added fix task -> compacted memory (203 lines)
  - `/home/seed/data/event_log.jsonl:158` logged bug + added fix task -> compacted memory (203 lines)

## script - logged bug + added fix task -> compacted memory (203 lines) -> refreshed stale mastodon.md

- Count: 2
- Confidence: 0.6
- Risk: low
- Suggested test: Add a fixture proving `logged bug + added fix task -> compacted memory (203 lines) -> refreshed stale mastodon.md` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:105` logged bug + added fix task -> compacted memory (203 lines) -> refreshed stale mastodon.md
  - `/home/seed/data/event_log.jsonl:158` logged bug + added fix task -> compacted memory (203 lines) -> refreshed stale mastodon.md

## script - logged bug + added fix task -> refreshed stale mastodon.md

- Count: 2
- Confidence: 0.6
- Risk: low
- Suggested test: Add a fixture proving `logged bug + added fix task -> refreshed stale mastodon.md` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:228` logged bug + added fix task -> refreshed stale mastodon.md
  - `/home/seed/data/event_log.jsonl:231` logged bug + added fix task -> refreshed stale mastodon.md

## script - logged bug + added fix task -> refreshed stale mastodon.md -> refreshed stale email.md

- Count: 2
- Confidence: 0.6
- Risk: low
- Suggested test: Add a fixture proving `logged bug + added fix task -> refreshed stale mastodon.md -> refreshed stale email.md` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:228` logged bug + added fix task -> refreshed stale mastodon.md -> refreshed stale email.md
  - `/home/seed/data/event_log.jsonl:231` logged bug + added fix task -> refreshed stale mastodon.md -> refreshed stale email.md

## script - publishing streak at 240 -> version_control streak at 155

- Count: 2
- Confidence: 0.6
- Risk: low
- Suggested test: Add a fixture proving `publishing streak at 240 -> version_control streak at 155` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:198` publishing streak at 240 -> version_control streak at 155
  - `/home/seed/data/event_log.jsonl:199` publishing streak at 240 -> version_control streak at 155

## script - publishing streak at 270 -> version_control streak at 170

- Count: 2
- Confidence: 0.6
- Risk: low
- Suggested test: Add a fixture proving `publishing streak at 270 -> version_control streak at 170` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:245` publishing streak at 270 -> version_control streak at 170
  - `/home/seed/data/event_log.jsonl:246` publishing streak at 270 -> version_control streak at 170

## script - rebuilt feeds -> logged bug + added fix task -> compacted memory (203 lines)

- Count: 2
- Confidence: 0.6
- Risk: low
- Suggested test: Add a fixture proving `rebuilt feeds -> logged bug + added fix task -> compacted memory (203 lines)` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:105` rebuilt feeds -> logged bug + added fix task -> compacted memory (203 lines)
  - `/home/seed/data/event_log.jsonl:158` rebuilt feeds -> logged bug + added fix task -> compacted memory (203 lines)

## script - refreshed stale email.md -> boosted starved drive create -> boosted starved drive connect

- Count: 2
- Confidence: 0.6
- Risk: low
- Suggested test: Add a fixture proving `refreshed stale email.md -> boosted starved drive create -> boosted starved drive connect` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:225` refreshed stale email.md -> boosted starved drive create -> boosted starved drive connect
  - `/home/seed/data/event_log.jsonl:228` refreshed stale email.md -> boosted starved drive create -> boosted starved drive connect

## script - refreshed stale email.md -> broke idle — boosted create + added urgent write task

- Count: 2
- Confidence: 0.6
- Risk: low
- Suggested test: Add a fixture proving `refreshed stale email.md -> broke idle — boosted create + added urgent write task` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:89` refreshed stale email.md -> broke idle — boosted create + added urgent write task
  - `/home/seed/data/event_log.jsonl:244` refreshed stale email.md -> broke idle — boosted create + added urgent write task

## script - refreshed stale email.md -> publishing streak at 185

- Count: 2
- Confidence: 0.6
- Risk: low
- Suggested test: Add a fixture proving `refreshed stale email.md -> publishing streak at 185` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:116` refreshed stale email.md -> publishing streak at 185
  - `/home/seed/data/event_log.jsonl:117` refreshed stale email.md -> publishing streak at 185

## script - refreshed stale email.md -> publishing streak at 215

- Count: 2
- Confidence: 0.6
- Risk: low
- Suggested test: Add a fixture proving `refreshed stale email.md -> publishing streak at 215` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:158` refreshed stale email.md -> publishing streak at 215
  - `/home/seed/data/event_log.jsonl:159` refreshed stale email.md -> publishing streak at 215

## script - refreshed stale email.md -> publishing streak at 235

- Count: 2
- Confidence: 0.6
- Risk: low
- Suggested test: Add a fixture proving `refreshed stale email.md -> publishing streak at 235` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:188` refreshed stale email.md -> publishing streak at 235
  - `/home/seed/data/event_log.jsonl:189` refreshed stale email.md -> publishing streak at 235

## script - refreshed stale email.md -> publishing streak at 235 -> version_control streak at 155

- Count: 2
- Confidence: 0.6
- Risk: low
- Suggested test: Add a fixture proving `refreshed stale email.md -> publishing streak at 235 -> version_control streak at 155` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:188` refreshed stale email.md -> publishing streak at 235 -> version_control streak at 155
  - `/home/seed/data/event_log.jsonl:189` refreshed stale email.md -> publishing streak at 235 -> version_control streak at 155

## script - refreshed stale email.md -> publishing streak at 240

- Count: 2
- Confidence: 0.6
- Risk: low
- Suggested test: Add a fixture proving `refreshed stale email.md -> publishing streak at 240` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:199` refreshed stale email.md -> publishing streak at 240
  - `/home/seed/data/event_log.jsonl:201` refreshed stale email.md -> publishing streak at 240

## script - refreshed stale email.md -> publishing streak at 275

- Count: 2
- Confidence: 0.6
- Risk: low
- Suggested test: Add a fixture proving `refreshed stale email.md -> publishing streak at 275` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:251` refreshed stale email.md -> publishing streak at 275
  - `/home/seed/data/event_log.jsonl:252` refreshed stale email.md -> publishing streak at 275

## script - refreshed stale email.md -> refreshed stale outreach.md -> flagged research for potential essay

- Count: 2
- Confidence: 0.6
- Risk: low
- Suggested test: Add a fixture proving `refreshed stale email.md -> refreshed stale outreach.md -> flagged research for potential essay` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:144` refreshed stale email.md -> refreshed stale outreach.md -> flagged research for potential essay
  - `/home/seed/data/event_log.jsonl:229` refreshed stale email.md -> refreshed stale outreach.md -> flagged research for potential essay

## script - refreshed stale email.md -> refreshed stale trends.md -> boosted starved drive create

- Count: 2
- Confidence: 0.6
- Risk: low
- Suggested test: Add a fixture proving `refreshed stale email.md -> refreshed stale trends.md -> boosted starved drive create` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:23` refreshed stale email.md -> refreshed stale trends.md -> boosted starved drive create
  - `/home/seed/data/event_log.jsonl:71` refreshed stale email.md -> refreshed stale trends.md -> boosted starved drive create

## script - refreshed stale email.md -> research streak at 210

- Count: 2
- Confidence: 0.6
- Risk: low
- Suggested test: Add a fixture proving `refreshed stale email.md -> research streak at 210` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:126` refreshed stale email.md -> research streak at 210
  - `/home/seed/data/event_log.jsonl:127` refreshed stale email.md -> research streak at 210

## script - refreshed stale email.md -> task_completion streak at 215

- Count: 2
- Confidence: 0.6
- Risk: low
- Suggested test: Add a fixture proving `refreshed stale email.md -> task_completion streak at 215` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:178` refreshed stale email.md -> task_completion streak at 215
  - `/home/seed/data/event_log.jsonl:179` refreshed stale email.md -> task_completion streak at 215

## script - refreshed stale email.md -> version_control streak at 155

- Count: 2
- Confidence: 0.6
- Risk: low
- Suggested test: Add a fixture proving `refreshed stale email.md -> version_control streak at 155` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:197` refreshed stale email.md -> version_control streak at 155
  - `/home/seed/data/event_log.jsonl:209` refreshed stale email.md -> version_control streak at 155

## script - refreshed stale email.md -> writing streak at 190

- Count: 2
- Confidence: 0.6
- Risk: low
- Suggested test: Add a fixture proving `refreshed stale email.md -> writing streak at 190` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:129` refreshed stale email.md -> writing streak at 190
  - `/home/seed/data/event_log.jsonl:130` refreshed stale email.md -> writing streak at 190

## script - refreshed stale mastodon.md -> boosted starved drive order

- Count: 2
- Confidence: 0.6
- Risk: low
- Suggested test: Add a fixture proving `refreshed stale mastodon.md -> boosted starved drive order` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:234` refreshed stale mastodon.md -> boosted starved drive order
  - `/home/seed/data/event_log.jsonl:236` refreshed stale mastodon.md -> boosted starved drive order

## script - refreshed stale mastodon.md -> flagged research for potential essay -> publishing streak at 170

- Count: 2
- Confidence: 0.6
- Risk: low
- Suggested test: Add a fixture proving `refreshed stale mastodon.md -> flagged research for potential essay -> publishing streak at 170` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:76` refreshed stale mastodon.md -> flagged research for potential essay -> publishing streak at 170
  - `/home/seed/data/event_log.jsonl:78` refreshed stale mastodon.md -> flagged research for potential essay -> publishing streak at 170

## script - refreshed stale mastodon.md -> refreshed stale email.md -> publishing streak at 185

- Count: 2
- Confidence: 0.6
- Risk: low
- Suggested test: Add a fixture proving `refreshed stale mastodon.md -> refreshed stale email.md -> publishing streak at 185` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:116` refreshed stale mastodon.md -> refreshed stale email.md -> publishing streak at 185
  - `/home/seed/data/event_log.jsonl:117` refreshed stale mastodon.md -> refreshed stale email.md -> publishing streak at 185

## script - refreshed stale mastodon.md -> refreshed stale email.md -> publishing streak at 215

- Count: 2
- Confidence: 0.6
- Risk: low
- Suggested test: Add a fixture proving `refreshed stale mastodon.md -> refreshed stale email.md -> publishing streak at 215` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:158` refreshed stale mastodon.md -> refreshed stale email.md -> publishing streak at 215
  - `/home/seed/data/event_log.jsonl:159` refreshed stale mastodon.md -> refreshed stale email.md -> publishing streak at 215

## script - refreshed stale mastodon.md -> refreshed stale email.md -> publishing streak at 235

- Count: 2
- Confidence: 0.6
- Risk: low
- Suggested test: Add a fixture proving `refreshed stale mastodon.md -> refreshed stale email.md -> publishing streak at 235` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:188` refreshed stale mastodon.md -> refreshed stale email.md -> publishing streak at 235
  - `/home/seed/data/event_log.jsonl:189` refreshed stale mastodon.md -> refreshed stale email.md -> publishing streak at 235

## script - refreshed stale mastodon.md -> refreshed stale email.md -> publishing streak at 240

- Count: 2
- Confidence: 0.6
- Risk: low
- Suggested test: Add a fixture proving `refreshed stale mastodon.md -> refreshed stale email.md -> publishing streak at 240` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:199` refreshed stale mastodon.md -> refreshed stale email.md -> publishing streak at 240
  - `/home/seed/data/event_log.jsonl:201` refreshed stale mastodon.md -> refreshed stale email.md -> publishing streak at 240

## script - refreshed stale mastodon.md -> refreshed stale email.md -> publishing streak at 275

- Count: 2
- Confidence: 0.6
- Risk: low
- Suggested test: Add a fixture proving `refreshed stale mastodon.md -> refreshed stale email.md -> publishing streak at 275` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:251` refreshed stale mastodon.md -> refreshed stale email.md -> publishing streak at 275
  - `/home/seed/data/event_log.jsonl:252` refreshed stale mastodon.md -> refreshed stale email.md -> publishing streak at 275

## script - refreshed stale mastodon.md -> refreshed stale email.md -> research streak at 210

- Count: 2
- Confidence: 0.6
- Risk: low
- Suggested test: Add a fixture proving `refreshed stale mastodon.md -> refreshed stale email.md -> research streak at 210` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:126` refreshed stale mastodon.md -> refreshed stale email.md -> research streak at 210
  - `/home/seed/data/event_log.jsonl:127` refreshed stale mastodon.md -> refreshed stale email.md -> research streak at 210

## script - refreshed stale mastodon.md -> refreshed stale email.md -> task_completion streak at 215

- Count: 2
- Confidence: 0.6
- Risk: low
- Suggested test: Add a fixture proving `refreshed stale mastodon.md -> refreshed stale email.md -> task_completion streak at 215` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:178` refreshed stale mastodon.md -> refreshed stale email.md -> task_completion streak at 215
  - `/home/seed/data/event_log.jsonl:179` refreshed stale mastodon.md -> refreshed stale email.md -> task_completion streak at 215

## script - refreshed stale mastodon.md -> refreshed stale email.md -> version_control streak at 155

- Count: 2
- Confidence: 0.6
- Risk: low
- Suggested test: Add a fixture proving `refreshed stale mastodon.md -> refreshed stale email.md -> version_control streak at 155` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:197` refreshed stale mastodon.md -> refreshed stale email.md -> version_control streak at 155
  - `/home/seed/data/event_log.jsonl:209` refreshed stale mastodon.md -> refreshed stale email.md -> version_control streak at 155

## script - refreshed stale mastodon.md -> refreshed stale email.md -> writing streak at 190

- Count: 2
- Confidence: 0.6
- Risk: low
- Suggested test: Add a fixture proving `refreshed stale mastodon.md -> refreshed stale email.md -> writing streak at 190` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:129` refreshed stale mastodon.md -> refreshed stale email.md -> writing streak at 190
  - `/home/seed/data/event_log.jsonl:130` refreshed stale mastodon.md -> refreshed stale email.md -> writing streak at 190

## script - refreshed stale mastodon.md -> refreshed stale outreach.md

- Count: 2
- Confidence: 0.6
- Risk: low
- Suggested test: Add a fixture proving `refreshed stale mastodon.md -> refreshed stale outreach.md` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:79` refreshed stale mastodon.md -> refreshed stale outreach.md
  - `/home/seed/data/event_log.jsonl:206` refreshed stale mastodon.md -> refreshed stale outreach.md

## script - refreshed stale mastodon.md -> refreshed stale trends.md -> refreshed stale outreach.md

- Count: 2
- Confidence: 0.6
- Risk: low
- Suggested test: Add a fixture proving `refreshed stale mastodon.md -> refreshed stale trends.md -> refreshed stale outreach.md` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:91` refreshed stale mastodon.md -> refreshed stale trends.md -> refreshed stale outreach.md
  - `/home/seed/data/event_log.jsonl:219` refreshed stale mastodon.md -> refreshed stale trends.md -> refreshed stale outreach.md

## script - refreshed stale mastodon.md -> writing streak at 170

- Count: 2
- Confidence: 0.6
- Risk: low
- Suggested test: Add a fixture proving `refreshed stale mastodon.md -> writing streak at 170` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:93` refreshed stale mastodon.md -> writing streak at 170
  - `/home/seed/data/event_log.jsonl:94` refreshed stale mastodon.md -> writing streak at 170

## script - refreshed stale mastodon.md -> writing streak at 265

- Count: 2
- Confidence: 0.6
- Risk: low
- Suggested test: Add a fixture proving `refreshed stale mastodon.md -> writing streak at 265` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:238` refreshed stale mastodon.md -> writing streak at 265
  - `/home/seed/data/event_log.jsonl:239` refreshed stale mastodon.md -> writing streak at 265

## script - refreshed stale outreach.md -> boosted starved drive create

- Count: 2
- Confidence: 0.6
- Risk: low
- Suggested test: Add a fixture proving `refreshed stale outreach.md -> boosted starved drive create` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:31` refreshed stale outreach.md -> boosted starved drive create
  - `/home/seed/data/event_log.jsonl:54` refreshed stale outreach.md -> boosted starved drive create

## script - refreshed stale trends.md -> boosted starved drive create

- Count: 2
- Confidence: 0.6
- Risk: low
- Suggested test: Add a fixture proving `refreshed stale trends.md -> boosted starved drive create` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:23` refreshed stale trends.md -> boosted starved drive create
  - `/home/seed/data/event_log.jsonl:71` refreshed stale trends.md -> boosted starved drive create

## script - research streak at 290 -> version_control streak at 155

- Count: 2
- Confidence: 0.6
- Risk: low
- Suggested test: Add a fixture proving `research streak at 290 -> version_control streak at 155` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:206` research streak at 290 -> version_control streak at 155
  - `/home/seed/data/event_log.jsonl:207` research streak at 290 -> version_control streak at 155

## script - writing streak at 225 -> version_control streak at 155

- Count: 2
- Confidence: 0.6
- Risk: low
- Suggested test: Add a fixture proving `writing streak at 225 -> version_control streak at 155` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/event_log.jsonl:179` writing streak at 225 -> version_control streak at 155
  - `/home/seed/data/event_log.jsonl:180` writing streak at 225 -> version_control streak at 155

## typed_tool - deployed tool-latency-is-organisational-memory-loss

- Count: 2
- Confidence: 0.69
- Risk: low
- Suggested test: Add schema validation and receipt checks for `deployed tool-latency-is-organisational-memory-loss`.
- Examples:
  - `/home/seed/data/event_log.jsonl:59` deployed tool-latency-is-organisational-memory-loss
  - `/home/seed/data/event_log.jsonl:60` deployed tool-latency-is-organisational-memory-loss
