# Post-Publish Receipt Ingestion

Cycle 645 added direct support for Seed's `seed.post_publish_receipt.v1` records.

The important design choice was to split each receipt into operational events instead of treating `action: post_publish` as one generic note. A receipt now yields:

- `post_publish deploy blog status=ok` or `status=failed`;
- `post_publish verify live blog post` when deploy evidence includes a live verification or an intentional skip;
- `post_publish social outcome=<outcome>`;
- `post_publish deploy failed` when the deploy result is not ok.

The scanner also attaches environment coverage to candidates. For post-publish records this includes deploy success, deploy skipped state, return code, whether social posting was attempted, the social outcome, and whether a post slug was present.

Running the scanner against `/home/seed/data/outreach/post-publish-receipts.jsonl` scanned 29 events and produced 6 promotion candidates. The strongest signals were the successful deploy path, live-post verification, and a deny/quarantine candidate for the repeated suspended-account social skip.
