import json
import tempfile
import unittest
from pathlib import Path

from tools.audit_loop_shrink import build_candidates, load_events, write_reports


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


if __name__ == "__main__":
    unittest.main()
