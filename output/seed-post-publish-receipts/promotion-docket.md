# Promotion Docket

Events scanned: 41
Promotion candidates: 6

## Summary

- `deny_or_quarantine`: 1
- `fixture`: 1
- `script`: 4

## script - post_publish deploy blog status=ok

- Count: 13
- Confidence: 0.95
- Evidence: fresh (first cycle 631, latest cycle 650, age 0, expires cycle 850)
- Risk: medium
- Environment coverage: {'deploy_ok': ['true'], 'deploy_returncode': ['0'], 'deploy_skipped': ['false', 'true'], 'post_slug_present': ['true'], 'social_attempted': ['false', 'true'], 'social_outcome': ['failed', 'skipped_account_suspended', 'unknown_not_recorded']}
- Promotion gate: passes_environment_gate (blocks=False)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `post_publish deploy blog status=ok` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/outreach/post-publish-receipts.jsonl:1` post_publish deploy blog command=/home/seed/tools/deploy-blog.sh ok=True skipped=True
  - `/home/seed/data/outreach/post-publish-receipts.jsonl:2` post_publish deploy blog command=/home/seed/tools/deploy-blog.sh ok=True skipped=False
  - `/home/seed/data/outreach/post-publish-receipts.jsonl:3` post_publish deploy blog command=/home/seed/tools/deploy-blog.sh ok=True skipped=False
  - `/home/seed/data/outreach/post-publish-receipts.jsonl:4` post_publish deploy blog command=/home/seed/tools/deploy-blog.sh ok=True skipped=True
  - `/home/seed/data/outreach/post-publish-receipts.jsonl:6` post_publish deploy blog command=/home/seed/tools/deploy-blog.sh ok=True skipped=True

## deny_or_quarantine - post_publish social outcome=skipped_account_suspended

- Count: 12
- Confidence: 0.95
- Evidence: fresh (first cycle 631, latest cycle 650, age 0, expires cycle 850)
- Risk: medium
- Environment coverage: {'deploy_ok': ['false', 'true'], 'deploy_returncode': ['0', '127'], 'deploy_skipped': ['false', 'true'], 'post_slug_present': ['true'], 'social_attempted': ['false'], 'social_outcome': ['skipped_account_suspended']}
- Promotion gate: condition_bound (blocks=False)
- Contradiction coverage: inherent_negative_signal
- Suggested test: Add a deny/quarantine regression proving `post_publish social outcome=skipped_account_suspended` cannot execute silently.
- Examples:
  - `/home/seed/data/outreach/post-publish-receipts.jsonl:1` post_publish social attempted=False outcome=skipped_account_suspended reason=tasks.md records disabled-login state
  - `/home/seed/data/outreach/post-publish-receipts.jsonl:2` post_publish social attempted=False outcome=skipped_account_suspended reason=tasks.md records disabled-login state
  - `/home/seed/data/outreach/post-publish-receipts.jsonl:3` post_publish social attempted=False outcome=skipped_account_suspended reason=tasks.md records disabled-login state
  - `/home/seed/data/outreach/post-publish-receipts.jsonl:4` post_publish social attempted=False outcome=skipped_account_suspended reason=tasks.md records disabled-login state
  - `/home/seed/data/outreach/post-publish-receipts.jsonl:5` post_publish social attempted=False outcome=skipped_account_suspended reason=tasks.md records disabled-login state

## fixture - post_publish verify live blog post

- Count: 12
- Confidence: 0.95
- Evidence: fresh (first cycle 631, latest cycle 650, age 0, expires cycle 850)
- Risk: medium
- Environment coverage: {'deploy_ok': ['true'], 'deploy_returncode': ['0'], 'deploy_skipped': ['false', 'true'], 'post_slug_present': ['true'], 'social_attempted': ['false', 'true'], 'social_outcome': ['failed', 'skipped_account_suspended', 'unknown_not_recorded']}
- Promotion gate: not_required (blocks=False)
- Contradiction coverage: missing
- Suggested test: Add positive and negative evidence cases for `post_publish verify live blog post`.
- Examples:
  - `/home/seed/data/outreach/post-publish-receipts.jsonl:1` post_publish verify live blog post
  - `/home/seed/data/outreach/post-publish-receipts.jsonl:3` post_publish verify live blog post
  - `/home/seed/data/outreach/post-publish-receipts.jsonl:4` post_publish verify live blog post
  - `/home/seed/data/outreach/post-publish-receipts.jsonl:6` post_publish verify live blog post
  - `/home/seed/data/outreach/post-publish-receipts.jsonl:7` post_publish verify live blog post

## script - post_publish deploy blog status=ok -> post_publish verify live blog post

- Count: 12
- Confidence: 0.95
- Evidence: fresh (first cycle 631, latest cycle 650, age 0, expires cycle 850)
- Risk: medium
- Environment coverage: {'deploy_ok': ['true'], 'deploy_returncode': ['0'], 'deploy_skipped': ['false', 'true'], 'post_slug_present': ['true'], 'social_attempted': ['false', 'true'], 'social_outcome': ['failed', 'skipped_account_suspended', 'unknown_not_recorded']}
- Promotion gate: passes_environment_gate (blocks=False)
- Contradiction coverage: missing
- Suggested test: Add a fixture proving `post_publish deploy blog status=ok -> post_publish verify live blog post` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/outreach/post-publish-receipts.jsonl:1` post_publish deploy blog command=/home/seed/tools/deploy-blog.sh ok=True skipped=True -> post_publish verify live blog post
  - `/home/seed/data/outreach/post-publish-receipts.jsonl:12` post_publish deploy blog command=/home/seed/tools/deploy-blog.sh ok=True skipped=False -> post_publish verify live blog post
  - `/home/seed/data/outreach/post-publish-receipts.jsonl:3` post_publish deploy blog command=/home/seed/tools/deploy-blog.sh ok=True skipped=False -> post_publish verify live blog post
  - `/home/seed/data/outreach/post-publish-receipts.jsonl:4` post_publish deploy blog command=/home/seed/tools/deploy-blog.sh ok=True skipped=True -> post_publish verify live blog post
  - `/home/seed/data/outreach/post-publish-receipts.jsonl:6` post_publish deploy blog command=/home/seed/tools/deploy-blog.sh ok=True skipped=True -> post_publish verify live blog post

## script - post_publish deploy blog status=ok -> post_publish verify live blog post -> post_publish social outcome=skipped_account_suspended

- Count: 10
- Confidence: 0.95
- Evidence: fresh (first cycle 631, latest cycle 650, age 0, expires cycle 850)
- Risk: medium
- Environment coverage: {'deploy_ok': ['true'], 'deploy_returncode': ['0'], 'deploy_skipped': ['false', 'true'], 'post_slug_present': ['true'], 'social_attempted': ['false'], 'social_outcome': ['skipped_account_suspended']}
- Promotion gate: passes_environment_gate (blocks=False)
- Contradiction coverage: observed
- Suggested test: Add a fixture proving `post_publish deploy blog status=ok -> post_publish verify live blog post -> post_publish social outcome=skipped_account_suspended` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/outreach/post-publish-receipts.jsonl:1` post_publish deploy blog command=/home/seed/tools/deploy-blog.sh ok=True skipped=True -> post_publish verify live blog post -> post_publish social attempted=False outcome=skipped_account_suspended reason=tasks.md records disabled-login state
  - `/home/seed/data/outreach/post-publish-receipts.jsonl:3` post_publish deploy blog command=/home/seed/tools/deploy-blog.sh ok=True skipped=False -> post_publish verify live blog post -> post_publish social attempted=False outcome=skipped_account_suspended reason=tasks.md records disabled-login state
  - `/home/seed/data/outreach/post-publish-receipts.jsonl:4` post_publish deploy blog command=/home/seed/tools/deploy-blog.sh ok=True skipped=True -> post_publish verify live blog post -> post_publish social attempted=False outcome=skipped_account_suspended reason=tasks.md records disabled-login state
  - `/home/seed/data/outreach/post-publish-receipts.jsonl:6` post_publish deploy blog command=/home/seed/tools/deploy-blog.sh ok=True skipped=True -> post_publish verify live blog post -> post_publish social attempted=False outcome=skipped_account_suspended reason=tasks.md records disabled-login state
  - `/home/seed/data/outreach/post-publish-receipts.jsonl:7` post_publish deploy blog command=/home/seed/tools/deploy-blog.sh ok=True skipped=False -> post_publish verify live blog post -> post_publish social attempted=False outcome=skipped_account_suspended reason=tasks.md records disabled-login state

## script - post_publish verify live blog post -> post_publish social outcome=skipped_account_suspended

- Count: 10
- Confidence: 0.95
- Evidence: fresh (first cycle 631, latest cycle 650, age 0, expires cycle 850)
- Risk: medium
- Environment coverage: {'deploy_ok': ['true'], 'deploy_returncode': ['0'], 'deploy_skipped': ['false', 'true'], 'post_slug_present': ['true'], 'social_attempted': ['false'], 'social_outcome': ['skipped_account_suspended']}
- Promotion gate: passes_environment_gate (blocks=False)
- Contradiction coverage: observed
- Suggested test: Add a fixture proving `post_publish verify live blog post -> post_publish social outcome=skipped_account_suspended` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/outreach/post-publish-receipts.jsonl:1` post_publish verify live blog post -> post_publish social attempted=False outcome=skipped_account_suspended reason=tasks.md records disabled-login state
  - `/home/seed/data/outreach/post-publish-receipts.jsonl:3` post_publish verify live blog post -> post_publish social attempted=False outcome=skipped_account_suspended reason=tasks.md records disabled-login state
  - `/home/seed/data/outreach/post-publish-receipts.jsonl:4` post_publish verify live blog post -> post_publish social attempted=False outcome=skipped_account_suspended reason=tasks.md records disabled-login state
  - `/home/seed/data/outreach/post-publish-receipts.jsonl:6` post_publish verify live blog post -> post_publish social attempted=False outcome=skipped_account_suspended reason=tasks.md records disabled-login state
  - `/home/seed/data/outreach/post-publish-receipts.jsonl:7` post_publish verify live blog post -> post_publish social attempted=False outcome=skipped_account_suspended reason=tasks.md records disabled-login state
