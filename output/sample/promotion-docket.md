# Promotion Docket

Events scanned: 19
Promotion candidates: 10

## Summary

- `approval_budget`: 2
- `deny_or_quarantine`: 1
- `fixture`: 1
- `script`: 6

## script - approve run rg over blog for queued topic

- Count: 3
- Confidence: 0.81
- Evidence: fresh (first cycle 1, latest cycle 3, age 14, expires cycle 203)
- Risk: low
- Suggested test: Add a fixture proving `approve run rg over blog for queued topic` runs idempotently from clean inputs.
- Examples:
  - `samples/events/cycles.jsonl:1` approve run rg over blog for queued topic
  - `samples/events/cycles.jsonl:2` approve run rg over blog for queued topic
  - `samples/events/cycles.jsonl:3` approve run rg over blog for queued topic

## approval_budget - approve action=post public status scope=mastodon account sink=public social

- Count: 2
- Confidence: 0.69
- Evidence: fresh (first cycle 16, latest cycle 17, age 0, expires cycle 217)
- Risk: high
- Suggested test: Require exact-call approval, expiry, replay rejection, and recovery evidence for `approve action=post public status scope=mastodon account sink=public social`.
- Examples:
  - `samples/events/cycles.jsonl:18` approve action=post public status scope=mastodon account sink=public social
  - `samples/events/cycles.jsonl:19` approve action=post public status scope=mastodon account sink=public social

## approval_budget - approve publish public post to mastodon account

- Count: 2
- Confidence: 0.69
- Evidence: fresh (first cycle 8, latest cycle 9, age 8, expires cycle 209)
- Risk: high
- Suggested test: Require exact-call approval, expiry, replay rejection, and recovery evidence for `approve publish public post to mastodon account`.
- Examples:
  - `samples/events/cycles.jsonl:8` approve publish public post to mastodon account
  - `samples/events/cycles.jsonl:9` approve publish public post to mastodon account

## deny_or_quarantine - blocked retry after mastodon 403 suspended account

- Count: 2
- Confidence: 0.69
- Evidence: fresh (first cycle 10, latest cycle 11, age 6, expires cycle 211)
- Risk: medium
- Suggested test: Add a deny/quarantine regression proving `blocked retry after mastodon 403 suspended account` cannot execute silently.
- Examples:
  - `samples/events/cycles.jsonl:10` blocked retry after mastodon 403 suspended account
  - `samples/events/cycles.jsonl:11` blocked retry after mastodon 403 suspended account

## fixture - expected output includes promotion-map json

- Count: 2
- Confidence: 0.69
- Evidence: fresh (first cycle 6, latest cycle 7, age 10, expires cycle 207)
- Risk: low
- Suggested test: Add positive and negative evidence cases for `expected output includes promotion-map json`.
- Examples:
  - `samples/events/cycles.jsonl:6` expected output includes promotion-map json
  - `samples/events/cycles.jsonl:7` expected output includes promotion-map json

## script - approve action=run deploy-blog scope=blog publish pipeline

- Count: 2
- Confidence: 0.69
- Evidence: fresh (first cycle 14, latest cycle 15, age 2, expires cycle 215)
- Risk: low
- Suggested test: Add a fixture proving `approve action=run deploy-blog scope=blog publish pipeline` runs idempotently from clean inputs.
- Examples:
  - `samples/events/cycles.jsonl:16` approve action=run deploy-blog scope=blog publish pipeline
  - `samples/events/cycles.jsonl:17` approve action=run deploy-blog scope=blog publish pipeline

## script - python3 tools/deploy-blog.sh

- Count: 2
- Confidence: 0.69
- Evidence: fresh (first cycle 4, latest cycle 5, age 12, expires cycle 205)
- Risk: low
- Suggested test: Add a fixture proving `python3 tools/deploy-blog.sh` runs idempotently from clean inputs.
- Examples:
  - `samples/events/cycles.jsonl:4` python3 tools/deploy-blog.sh
  - `samples/events/cycles.jsonl:5` python3 tools/deploy-blog.sh

## script - rg queued topic blog

- Count: 2
- Confidence: 0.69
- Evidence: fresh (first cycle 12, latest cycle 13, age 4, expires cycle 213)
- Risk: low
- Suggested test: Add a fixture proving `rg queued topic blog` runs idempotently from clean inputs.
- Examples:
  - `samples/events/cycles.jsonl:12` rg queued topic blog
  - `samples/events/cycles.jsonl:14` rg queued topic blog

## script - rg queued topic blog -> sed -n 1,120p data/blog_queue.txt

- Count: 2
- Confidence: 0.6
- Evidence: fresh (first cycle 12, latest cycle 13, age 4, expires cycle 213)
- Risk: low
- Suggested test: Add a fixture proving `rg queued topic blog -> sed -n 1,120p data/blog_queue.txt` runs idempotently from clean inputs.
- Examples:
  - `samples/events/cycles.jsonl:12` rg queued topic blog -> sed -n 1,120p data/blog_queue.txt
  - `samples/events/cycles.jsonl:14` rg queued topic blog -> sed -n 1,120p data/blog_queue.txt

## script - sed -n 1,120p data/blog_queue.txt

- Count: 2
- Confidence: 0.69
- Evidence: fresh (first cycle 12, latest cycle 13, age 4, expires cycle 213)
- Risk: low
- Suggested test: Add a fixture proving `sed -n 1,120p data/blog_queue.txt` runs idempotently from clean inputs.
- Examples:
  - `samples/events/cycles.jsonl:13` sed -n 1,120p data/blog_queue.txt
  - `samples/events/cycles.jsonl:15` sed -n 1,120p data/blog_queue.txt
