import json
import tempfile
import unittest
from pathlib import Path

from tools.audit_loop_shrink import Event, build_candidates, load_events, write_reports


class LoopShrinkAuditTests(unittest.TestCase):
    def test_repeated_safe_approval_promotes_to_script(self):
        events = load_events(Path("samples/events"))
        candidates = build_candidates(events)
        shapes = {candidate["shape"]: candidate for candidate in candidates}

        self.assertIn("approve run rg over blog for queued topic", shapes)
        self.assertEqual(shapes["approve run rg over blog for queued topic"]["classification"], "script")

    def test_high_risk_approval_stays_in_budget(self):
        events = load_events(Path("samples/events"))
        candidates = build_candidates(events)
        budget = [
            candidate
            for candidate in candidates
            if candidate["classification"] == "approval_budget"
        ]

        self.assertTrue(any("publish" in candidate["shape"] for candidate in budget))

    def test_approval_log_shape_ignores_noisy_request_text(self):
        events = load_events(Path("samples/events"))
        candidates = build_candidates(events)
        shapes = {candidate["shape"]: candidate for candidate in candidates}

        shape = "approve action=run deploy-blog scope=blog publish pipeline"
        self.assertIn(shape, shapes)
        self.assertEqual(shapes[shape]["classification"], "script")
        self.assertEqual(shapes[shape]["count"], 2)

    def test_high_risk_approval_log_uses_budget(self):
        events = load_events(Path("samples/events"))
        candidates = build_candidates(events)
        shapes = {candidate["shape"]: candidate for candidate in candidates}

        shape = "approve action=post public status scope=mastodon account sink=public social"
        self.assertIn(shape, shapes)
        self.assertEqual(shapes[shape]["classification"], "approval_budget")

    def test_reports_are_written(self):
        events = load_events(Path("samples/events"))
        candidates = build_candidates(events)
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp)
            write_reports(candidates, events, output)
            payload = json.loads((output / "promotion-map.json").read_text())

        self.assertGreaterEqual(payload["candidate_count"], 4)
        self.assertIn("script", payload["summary"])

    def test_repeated_adjacent_commands_promote_sequence(self):
        events = load_events(Path("samples/events"))
        candidates = build_candidates(events)
        sequences = [
            candidate
            for candidate in candidates
            if candidate["kind"] == "sequence"
        ]

        self.assertTrue(sequences)
        self.assertTrue(any("rg queued topic blog -> sed" in candidate["shape"] for candidate in sequences))

    def test_jsonl_action_lists_from_cycle_logs_are_loaded(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "events.jsonl"
            path.write_text(
                json.dumps(
                    {
                        "cycle": 99,
                        "actions": [
                            "refreshed stale mastodon.md",
                            "refreshed stale email.md",
                        ],
                    }
                )
                + "\n",
                encoding="utf-8",
            )

            events = load_events(path)

        self.assertEqual([event.text for event in events], ["refreshed stale mastodon.md", "refreshed stale email.md"])

    def test_stale_evidence_decays_candidate_confidence(self):
        events = [
            Event("events.jsonl", 1, "command", "python deploy", "python deploy", cycle="1"),
            Event("events.jsonl", 2, "command", "python deploy", "python deploy", cycle="2"),
            Event("events.jsonl", 3, "command", "recent unrelated command", "recent unrelated command", cycle="300"),
        ]

        candidates = build_candidates(events)
        candidate = next(candidate for candidate in candidates if candidate["shape"] == "python deploy")

        self.assertEqual(candidate["evidence"]["first_cycle"], 1)
        self.assertEqual(candidate["evidence"]["latest_cycle"], 2)
        self.assertEqual(candidate["evidence"]["evidence_age_cycles"], 298)
        self.assertEqual(candidate["evidence"]["evidence_expires_cycle"], 202)
        self.assertEqual(candidate["evidence"]["evidence_status"], "stale")
        self.assertLess(candidate["confidence"], 0.69)

    def test_post_publish_receipts_are_first_class_evidence(self):
        events = load_events(Path("samples/events"))
        candidates = build_candidates(events)
        shapes = {candidate["shape"]: candidate for candidate in candidates}

        self.assertIn("post_publish deploy blog status=ok", shapes)
        self.assertEqual(shapes["post_publish deploy blog status=ok"]["classification"], "script")
        self.assertEqual(
            shapes["post_publish deploy blog status=ok"]["environment_coverage"]["social_outcome"],
            ["skipped_account_suspended"],
        )
        self.assertEqual(
            shapes["post_publish deploy blog status=ok"]["promotion_gate"]["status"],
            "blocked_narrow_environment",
        )
        self.assertTrue(shapes["post_publish deploy blog status=ok"]["promotion_gate"]["blocks_promotion"])
        self.assertEqual(
            shapes["post_publish deploy blog status=ok"]["contradiction_coverage"]["status"],
            "missing",
        )

        social_shape = "post_publish social outcome=skipped_account_suspended"
        self.assertIn(social_shape, shapes)
        self.assertEqual(shapes[social_shape]["classification"], "deny_or_quarantine")
        self.assertEqual(shapes[social_shape]["promotion_gate"]["status"], "condition_bound")
        self.assertFalse(shapes[social_shape]["promotion_gate"]["blocks_promotion"])

    def test_post_publish_receipt_failure_is_not_lost_as_note(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "receipts.jsonl"
            receipt = {
                "schema": "seed.post_publish_receipt.v1",
                "cycle": 638,
                "deploy": {
                    "command": "the-agent-as-compiler",
                    "ok": False,
                    "returncode": 127,
                    "skipped": False,
                },
                "output_tail": "[Errno 2] No such file or directory: 'the-agent-as-compiler'",
                "post": {"slug": "434"},
                "social": {
                    "attempted": False,
                    "outcome": "skipped_account_suspended",
                    "reason": "tasks.md records disabled-login state",
                },
            }
            path.write_text(json.dumps(receipt) + "\n", encoding="utf-8")

            events = load_events(path)

        self.assertTrue(any(event.shape == "post_publish deploy failed" for event in events))
        failure = next(event for event in events if event.shape == "post_publish deploy failed")
        self.assertEqual(failure.kind, "failure")
        self.assertEqual(failure.environment["deploy_ok"], "false")

    def test_environment_gate_passes_when_conditions_vary(self):
        events = [
            Event(
                "events.jsonl",
                1,
                "command",
                "refresh feed",
                "refresh feed",
                cycle="1",
                environment={"network_state": "online"},
            ),
            Event(
                "events.jsonl",
                2,
                "command",
                "refresh feed",
                "refresh feed",
                cycle="2",
                environment={"network_state": "offline"},
            ),
        ]

        candidate = build_candidates(events)[0]

        self.assertEqual(candidate["promotion_gate"]["status"], "passes_environment_gate")
        self.assertFalse(candidate["promotion_gate"]["blocks_promotion"])


if __name__ == "__main__":
    unittest.main()
