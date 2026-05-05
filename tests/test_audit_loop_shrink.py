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

        self.assertEqual(len(budget), 1)
        self.assertIn("publish", budget[0]["shape"])

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


if __name__ == "__main__":
    unittest.main()
