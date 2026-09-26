import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
USING_VADMIN = ROOT / "skills" / "using-vadmin"


class VAdminGuidanceTests(unittest.TestCase):
    def test_self_provided_identity_lands_in_outbound_adapters(self):
        text = (USING_VADMIN / "references" / "identity.md").read_text(encoding="utf-8")
        for required in (
            "Self-Provided Identity",
            "secondary adapters",
            "composition-root types",
            "outbound adapter package",
            "must not own SQL",
            "aggregate repositories",
        ):
            self.assertIn(required, text)

    def test_skill_forbids_identity_implementations_in_the_composition_root(self):
        text = (USING_VADMIN / "SKILL.md").read_text(encoding="utf-8")
        for required in (
            "outbound adapters",
            "composition root only wires them",
            "Do not implement VAdmin identity or audit contracts in the composition root",
            "Do not model host IAM tables as the host's aggregate repositories",
        ):
            self.assertIn(required, text)

    def test_first_use_wires_self_provided_identity_from_the_composition_root(self):
        text = (USING_VADMIN / "references" / "first-use.md").read_text(encoding="utf-8")
        self.assertIn("implement VAdmin identity contracts as outbound adapters", text)
        self.assertIn("wire them from the composition root", text)


if __name__ == "__main__":
    unittest.main()
