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
            "## Bounded Context Crossings",
            "stored state",
            "Package-dependency tests do not see",
        ):
            self.assertIn(required, text)

    def test_skill_routes_the_transaction_rule_to_architecture_constraints(self):
        text = SKILL.read_text(encoding="utf-8")
        self.assertIn("Transaction Boundaries", text)
        self.assertIn("outbound HTTP, client-SDK, or broker calls", text)
        self.assertIn("state-changing domain behavior", text)
        self.assertIn("Bounded Context Crossings", text)

    def test_guidance_reads_only_matching_references(self):
        text = SKILL.read_text(encoding="utf-8")
        self.assertIn("Do not read the skill directory recursively", text)
        self.assertIn("Skip every row that does not match", text)
        self.assertIn("references/architecture-constraints.md", text)
        self.assertIn("the one section for the stack chosen", text)
        self.assertNotIn(
            "Apply source hierarchy from `references/source-policy.md` before citing",
            text,
        )
        self.assertNotIn(
            "Apply backend implementation guidance from `references/backend-guidance.md` when changing code",
            text,
        )


if __name__ == "__main__":
    unittest.main()
