# Promotion Docket

Events scanned: 29
Promotion candidates: 6

## Summary

- `deny_or_quarantine`: 1
- `fixture`: 1
- `script`: 4

## deny_or_quarantine - post_publish social outcome=skipped_account_suspended

- Count: 10
- Confidence: 0.95
- Evidence: fresh (first cycle 631, latest cycle 644, age 0, expires cycle 844)
- Risk: medium
- Environment coverage: {'deploy_ok': ['false', 'true'], 'deploy_returncode': ['0', '127'], 'deploy_skipped': ['false', 'true'], 'post_slug_present': ['true'], 'social_attempted': ['false'], 'social_outcome': ['skipped_account_suspended']}
- Suggested test: Add a deny/quarantine regression proving `post_publish social outcome=skipped_account_suspended` cannot execute silently.
- Examples:
  - `/home/seed/data/outreach/post-publish-receipts.jsonl:1` post_publish social attempted=False outcome=skipped_account_suspended reason=tasks.md records disabled-login state
  - `/home/seed/data/outreach/post-publish-receipts.jsonl:2` post_publish social attempted=False outcome=skipped_account_suspended reason=tasks.md records disabled-login state
  - `/home/seed/data/outreach/post-publish-receipts.jsonl:3` post_publish social attempted=False outcome=skipped_account_suspended reason=tasks.md records disabled-login state
  - `/home/seed/data/outreach/post-publish-receipts.jsonl:4` post_publish social attempted=False outcome=skipped_account_suspended reason=tasks.md records disabled-login state
  - `/home/seed/data/outreach/post-publish-receipts.jsonl:5` post_publish social attempted=False outcome=skipped_account_suspended reason=tasks.md records disabled-login state

## script - post_publish deploy blog status=ok

- Count: 9
- Confidence: 0.95
- Evidence: fresh (first cycle 631, latest cycle 644, age 0, expires cycle 844)
- Risk: medium
- Environment coverage: {'deploy_ok': ['true'], 'deploy_returncode': ['0'], 'deploy_skipped': ['false', 'true'], 'post_slug_present': ['true'], 'social_attempted': ['false'], 'social_outcome': ['skipped_account_suspended']}
- Suggested test: Add a fixture proving `post_publish deploy blog status=ok` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/outreach/post-publish-receipts.jsonl:1` post_publish deploy blog command=/home/seed/tools/deploy-blog.sh ok=True skipped=True
  - `/home/seed/data/outreach/post-publish-receipts.jsonl:2` post_publish deploy blog command=/home/seed/tools/deploy-blog.sh ok=True skipped=False
  - `/home/seed/data/outreach/post-publish-receipts.jsonl:3` post_publish deploy blog command=/home/seed/tools/deploy-blog.sh ok=True skipped=False
  - `/home/seed/data/outreach/post-publish-receipts.jsonl:4` post_publish deploy blog command=/home/seed/tools/deploy-blog.sh ok=True skipped=True
  - `/home/seed/data/outreach/post-publish-receipts.jsonl:6` post_publish deploy blog command=/home/seed/tools/deploy-blog.sh ok=True skipped=True

## fixture - post_publish verify live blog post

- Count: 8
- Confidence: 0.95
- Evidence: fresh (first cycle 631, latest cycle 644, age 0, expires cycle 844)
- Risk: medium
- Environment coverage: {'deploy_ok': ['true'], 'deploy_returncode': ['0'], 'deploy_skipped': ['false', 'true'], 'post_slug_present': ['true'], 'social_attempted': ['false'], 'social_outcome': ['skipped_account_suspended']}
- Suggested test: Add positive and negative evidence cases for `post_publish verify live blog post`.
- Examples:
  - `/home/seed/data/outreach/post-publish-receipts.jsonl:1` post_publish verify live blog post
  - `/home/seed/data/outreach/post-publish-receipts.jsonl:3` post_publish verify live blog post
  - `/home/seed/data/outreach/post-publish-receipts.jsonl:4` post_publish verify live blog post
  - `/home/seed/data/outreach/post-publish-receipts.jsonl:6` post_publish verify live blog post
  - `/home/seed/data/outreach/post-publish-receipts.jsonl:7` post_publish verify live blog post

## script - post_publish deploy blog status=ok -> post_publish verify live blog post

- Count: 8
- Confidence: 0.95
- Evidence: fresh (first cycle 631, latest cycle 644, age 0, expires cycle 844)
- Risk: medium
- Environment coverage: {'deploy_ok': ['true'], 'deploy_returncode': ['0'], 'deploy_skipped': ['false', 'true'], 'post_slug_present': ['true'], 'social_attempted': ['false'], 'social_outcome': ['skipped_account_suspended']}
- Suggested test: Add a fixture proving `post_publish deploy blog status=ok -> post_publish verify live blog post` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/outreach/post-publish-receipts.jsonl:1` post_publish deploy blog command=/home/seed/tools/deploy-blog.sh ok=True skipped=True -> post_publish verify live blog post
  - `/home/seed/data/outreach/post-publish-receipts.jsonl:3` post_publish deploy blog command=/home/seed/tools/deploy-blog.sh ok=True skipped=False -> post_publish verify live blog post
  - `/home/seed/data/outreach/post-publish-receipts.jsonl:4` post_publish deploy blog command=/home/seed/tools/deploy-blog.sh ok=True skipped=True -> post_publish verify live blog post
  - `/home/seed/data/outreach/post-publish-receipts.jsonl:6` post_publish deploy blog command=/home/seed/tools/deploy-blog.sh ok=True skipped=True -> post_publish verify live blog post
  - `/home/seed/data/outreach/post-publish-receipts.jsonl:7` post_publish deploy blog command=/home/seed/tools/deploy-blog.sh ok=True skipped=False -> post_publish verify live blog post

## script - post_publish deploy blog status=ok -> post_publish verify live blog post -> post_publish social outcome=skipped_account_suspended

- Count: 8
- Confidence: 0.95
- Evidence: fresh (first cycle 631, latest cycle 644, age 0, expires cycle 844)
- Risk: medium
- Environment coverage: {'deploy_ok': ['true'], 'deploy_returncode': ['0'], 'deploy_skipped': ['false', 'true'], 'post_slug_present': ['true'], 'social_attempted': ['false'], 'social_outcome': ['skipped_account_suspended']}
- Suggested test: Add a fixture proving `post_publish deploy blog status=ok -> post_publish verify live blog post -> post_publish social outcome=skipped_account_suspended` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/outreach/post-publish-receipts.jsonl:1` post_publish deploy blog command=/home/seed/tools/deploy-blog.sh ok=True skipped=True -> post_publish verify live blog post -> post_publish social attempted=False outcome=skipped_account_suspended reason=tasks.md records disabled-login state
  - `/home/seed/data/outreach/post-publish-receipts.jsonl:3` post_publish deploy blog command=/home/seed/tools/deploy-blog.sh ok=True skipped=False -> post_publish verify live blog post -> post_publish social attempted=False outcome=skipped_account_suspended reason=tasks.md records disabled-login state
  - `/home/seed/data/outreach/post-publish-receipts.jsonl:4` post_publish deploy blog command=/home/seed/tools/deploy-blog.sh ok=True skipped=True -> post_publish verify live blog post -> post_publish social attempted=False outcome=skipped_account_suspended reason=tasks.md records disabled-login state
  - `/home/seed/data/outreach/post-publish-receipts.jsonl:6` post_publish deploy blog command=/home/seed/tools/deploy-blog.sh ok=True skipped=True -> post_publish verify live blog post -> post_publish social attempted=False outcome=skipped_account_suspended reason=tasks.md records disabled-login state
  - `/home/seed/data/outreach/post-publish-receipts.jsonl:7` post_publish deploy blog command=/home/seed/tools/deploy-blog.sh ok=True skipped=False -> post_publish verify live blog post -> post_publish social attempted=False outcome=skipped_account_suspended reason=tasks.md records disabled-login state

## script - post_publish verify live blog post -> post_publish social outcome=skipped_account_suspended

- Count: 8
- Confidence: 0.95
- Evidence: fresh (first cycle 631, latest cycle 644, age 0, expires cycle 844)
- Risk: medium
- Environment coverage: {'deploy_ok': ['true'], 'deploy_returncode': ['0'], 'deploy_skipped': ['false', 'true'], 'post_slug_present': ['true'], 'social_attempted': ['false'], 'social_outcome': ['skipped_account_suspended']}
- Suggested test: Add a fixture proving `post_publish verify live blog post -> post_publish social outcome=skipped_account_suspended` runs idempotently from clean inputs.
- Examples:
  - `/home/seed/data/outreach/post-publish-receipts.jsonl:1` post_publish verify live blog post -> post_publish social attempted=False outcome=skipped_account_suspended reason=tasks.md records disabled-login state
  - `/home/seed/data/outreach/post-publish-receipts.jsonl:3` post_publish verify live blog post -> post_publish social attempted=False outcome=skipped_account_suspended reason=tasks.md records disabled-login state
  - `/home/seed/data/outreach/post-publish-receipts.jsonl:4` post_publish verify live blog post -> post_publish social attempted=False outcome=skipped_account_suspended reason=tasks.md records disabled-login state
  - `/home/seed/data/outreach/post-publish-receipts.jsonl:6` post_publish verify live blog post -> post_publish social attempted=False outcome=skipped_account_suspended reason=tasks.md records disabled-login state
  - `/home/seed/data/outreach/post-publish-receipts.jsonl:7` post_publish verify live blog post -> post_publish social attempted=False outcome=skipped_account_suspended reason=tasks.md records disabled-login state
