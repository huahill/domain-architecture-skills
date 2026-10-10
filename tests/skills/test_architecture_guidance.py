from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[2]
CONSTRAINTS = ROOT / "skills/domain-architecture-guidance/references/architecture-constraints.md"
SKILL = ROOT / "skills/domain-architecture-guidance/SKILL.md"


class ArchitectureGuidanceTests(unittest.TestCase):
    def test_transaction_boundary_forbids_outbound_calls_without_a_framework(self):
        text = CONSTRAINTS.read_text(encoding="utf-8")
        for required in (
            "## Transaction Boundaries",
            "outbound HTTP, client-SDK, or broker call",
            "any persistence technology",
            "optimistic version check",
            "pessimistic lock",
        ):
            self.assertIn(required, text)

    def test_skill_routes_the_transaction_rule_to_architecture_constraints(self):
        text = SKILL.read_text(encoding="utf-8")
        self.assertIn("Transaction Boundaries", text)
        self.assertIn("outbound HTTP, client-SDK, or broker calls", text)


if __name__ == "__main__":
    unittest.main()
