# Promotion Docket

Events scanned: 27
Promotion candidates: 13

## Summary

- `approval_budget`: 2
- `deny_or_quarantine`: 2
- `fixture`: 2
- `script`: 7

## Gate Summary

- Blocked: 9
- Passed: 0
- Condition-bound: 2
- Missing environment: 8
- Not required: 2

## script - approve run rg over blog for queued topic

- Count: 3
- Confidence: 0.81
- Evidence: fresh (first cycle 1, latest cycle 3, age 16, expires cycle 203)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Demotion intakes: none
- Suggested test: Add a fixture proving `approve run rg over blog for queued topic` runs idempotently from clean inputs.
- Examples:
  - `samples/events/cycles.jsonl:1` approve run rg over blog for queued topic
  - `samples/events/cycles.jsonl:2` approve run rg over blog for queued topic
  - `samples/events/cycles.jsonl:3` approve run rg over blog for queued topic

## script - rg queued topic blog

- Count: 3
- Confidence: 0.81
- Evidence: fresh (first cycle 12, latest cycle 14, age 5, expires cycle 214)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Demotion intakes: none
- Suggested test: Add a fixture proving `rg queued topic blog` runs idempotently from clean inputs.
- Examples:
  - `samples/events/cycles.jsonl:12` rg queued topic blog
  - `samples/events/cycles.jsonl:14` rg queued topic blog
  - `samples/events/cycles.jsonl:16` rg queued topic blog

## script - rg queued topic blog -> sed -n 1,120p data/blog_queue.txt

- Count: 3
- Confidence: 0.7
- Evidence: fresh (first cycle 12, latest cycle 14, age 5, expires cycle 214)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Demotion intakes: none
- Suggested test: Add a fixture proving `rg queued topic blog -> sed -n 1,120p data/blog_queue.txt` runs idempotently from clean inputs.
- Examples:
  - `samples/events/cycles.jsonl:12` rg queued topic blog -> sed -n 1,120p data/blog_queue.txt
  - `samples/events/cycles.jsonl:14` rg queued topic blog -> sed -n 1,120p data/blog_queue.txt
  - `samples/events/cycles.jsonl:16` rg queued topic blog -> sed -n 1,120p data/blog_queue.txt

## script - sed -n 1,120p data/blog_queue.txt

- Count: 3
- Confidence: 0.81
- Evidence: fresh (first cycle 12, latest cycle 14, age 5, expires cycle 214)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Demotion intakes: none
- Suggested test: Add a fixture proving `sed -n 1,120p data/blog_queue.txt` runs idempotently from clean inputs.
- Examples:
  - `samples/events/cycles.jsonl:13` sed -n 1,120p data/blog_queue.txt
  - `samples/events/cycles.jsonl:15` sed -n 1,120p data/blog_queue.txt
  - `samples/events/cycles.jsonl:17` sed -n 1,120p data/blog_queue.txt

## approval_budget - approve action=post public status scope=mastodon account sink=public social

- Count: 2
- Confidence: 0.69
- Evidence: fresh (first cycle 16, latest cycle 17, age 2, expires cycle 217)
- Risk: high
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Demotion intakes: none
- Suggested test: Require exact-call approval, expiry, replay rejection, and recovery evidence for `approve action=post public status scope=mastodon account sink=public social`.
- Examples:
  - `samples/events/cycles.jsonl:20` approve action=post public status scope=mastodon account sink=public social
  - `samples/events/cycles.jsonl:21` approve action=post public status scope=mastodon account sink=public social

## approval_budget - approve publish public post to mastodon account

- Count: 2
- Confidence: 0.69
- Evidence: fresh (first cycle 8, latest cycle 9, age 10, expires cycle 209)
- Risk: high
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Demotion intakes: none
- Suggested test: Require exact-call approval, expiry, replay rejection, and recovery evidence for `approve publish public post to mastodon account`.
- Examples:
  - `samples/events/cycles.jsonl:8` approve publish public post to mastodon account
  - `samples/events/cycles.jsonl:9` approve publish public post to mastodon account

## deny_or_quarantine - blocked retry after mastodon 403 suspended account

- Count: 2
- Confidence: 0.69
- Evidence: fresh (first cycle 10, latest cycle 11, age 8, expires cycle 211)
- Risk: medium
- Environment coverage: {}
- Promotion gate: condition_bound (blocks=False)
- Contradiction coverage: inherent_negative_signal
- Demotion intakes: none
- Suggested test: Add a deny/quarantine regression proving `blocked retry after mastodon 403 suspended account` cannot execute silently.
- Examples:
  - `samples/events/cycles.jsonl:10` blocked retry after mastodon 403 suspended account
  - `samples/events/cycles.jsonl:11` blocked retry after mastodon 403 suspended account

## deny_or_quarantine - post_publish social outcome=skipped_account_suspended

- Count: 2
- Confidence: 0.69
- Evidence: fresh (first cycle 18, latest cycle 19, age 0, expires cycle 219)
- Risk: medium
- Environment coverage: {'deploy_ok': ['true'], 'deploy_returncode': ['0'], 'deploy_skipped': ['false'], 'post_slug_present': ['true'], 'social_attempted': ['false'], 'social_outcome': ['skipped_account_suspended']}
- Promotion gate: condition_bound (blocks=False)
- Contradiction coverage: inherent_negative_signal
- Demotion intakes: none
- Suggested test: Add a deny/quarantine regression proving `post_publish social outcome=skipped_account_suspended` cannot execute silently.
- Examples:
  - `samples/events/cycles.jsonl:22` post_publish social attempted=False outcome=skipped_account_suspended reason=tasks.md records disabled-login state
  - `samples/events/cycles.jsonl:23` post_publish social attempted=False outcome=skipped_account_suspended reason=tasks.md records disabled-login state

## fixture - expected output includes promotion-map json

- Count: 2
- Confidence: 0.69
- Evidence: fresh (first cycle 6, latest cycle 7, age 12, expires cycle 207)
- Risk: low
- Environment coverage: {}
- Promotion gate: not_required (blocks=False)
- Contradiction coverage: missing
- Demotion intakes: none
- Suggested test: Add positive and negative evidence cases for `expected output includes promotion-map json`.
- Examples:
  - `samples/events/cycles.jsonl:6` expected output includes promotion-map json
  - `samples/events/cycles.jsonl:7` expected output includes promotion-map json

## fixture - post_publish verify live blog post

- Count: 2
- Confidence: 0.69
- Evidence: fresh (first cycle 18, latest cycle 19, age 0, expires cycle 219)
- Risk: low
- Environment coverage: {'deploy_ok': ['true'], 'deploy_returncode': ['0'], 'deploy_skipped': ['false'], 'post_slug_present': ['true'], 'social_attempted': ['false'], 'social_outcome': ['skipped_account_suspended']}
- Promotion gate: not_required (blocks=False)
- Contradiction coverage: missing
- Demotion intakes: none
- Suggested test: Add positive and negative evidence cases for `post_publish verify live blog post`.
- Examples:
  - `samples/events/cycles.jsonl:22` post_publish verify live blog post
  - `samples/events/cycles.jsonl:23` post_publish verify live blog post

## script - approve action=run deploy-blog scope=blog publish pipeline

- Count: 2
- Confidence: 0.69
- Evidence: fresh (first cycle 14, latest cycle 15, age 4, expires cycle 215)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Demotion intakes: none
- Suggested test: Add a fixture proving `approve action=run deploy-blog scope=blog publish pipeline` runs idempotently from clean inputs.
- Examples:
  - `samples/events/cycles.jsonl:18` approve action=run deploy-blog scope=blog publish pipeline
  - `samples/events/cycles.jsonl:19` approve action=run deploy-blog scope=blog publish pipeline

## script - post_publish deploy blog status=ok

- Count: 2
- Confidence: 0.69
- Evidence: fresh (first cycle 18, latest cycle 19, age 0, expires cycle 219)
- Risk: low
- Environment coverage: {'deploy_ok': ['true'], 'deploy_returncode': ['0'], 'deploy_skipped': ['false'], 'post_slug_present': ['true'], 'social_attempted': ['false'], 'social_outcome': ['skipped_account_suspended']}
- Promotion gate: blocked_narrow_environment (blocks=True)
- Contradiction coverage: missing
- Demotion intakes: none
- Suggested test: Add a fixture proving `post_publish deploy blog status=ok` runs idempotently from clean inputs.
- Examples:
  - `samples/events/cycles.jsonl:22` post_publish deploy blog command=/home/seed/tools/deploy-blog.sh ok=True skipped=False
  - `samples/events/cycles.jsonl:23` post_publish deploy blog command=/home/seed/tools/deploy-blog.sh ok=True skipped=False

## script - python3 tools/deploy-blog.sh

- Count: 2
- Confidence: 0.69
- Evidence: fresh (first cycle 4, latest cycle 5, age 14, expires cycle 205)
- Risk: low
- Environment coverage: {}
- Promotion gate: needs_environment_record (blocks=True)
- Contradiction coverage: missing
- Demotion intakes: none
- Suggested test: Add a fixture proving `python3 tools/deploy-blog.sh` runs idempotently from clean inputs.
- Examples:
  - `samples/events/cycles.jsonl:4` python3 tools/deploy-blog.sh
  - `samples/events/cycles.jsonl:5` python3 tools/deploy-blog.sh
