import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
USING_JFOUNDRY = ROOT / "skills" / "using-jfoundry"
PERSISTENCE = USING_JFOUNDRY / "references" / "persistence-data-mappers.md"
REPOSITORIES = USING_JFOUNDRY / "references" / "repository-and-read-contracts.md"
TESTING = USING_JFOUNDRY / "references" / "testing.md"


class JFoundryGuidanceTests(unittest.TestCase):
    def test_persistence_reference_requires_preflight(self):
        text = PERSISTENCE.read_text(encoding="utf-8")
        self.assertIn("Aggregate Persistence Preflight", text)
        for required in (
            "List aggregate roots",
            "domain aggregate repository contract",
            "add / modify / remove",
            "non-aggregate read, store, CAS, lease, or history contract",
            "Repository suffix",
        ):
            self.assertIn(required, text)

    def test_skill_routes_persistence_preflight_before_implementation(self):
        text = (USING_JFOUNDRY / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("complete the Aggregate Persistence Preflight", text)

    def test_repository_reference_links_preflight_and_read_contracts(self):
        text = REPOSITORIES.read_text(encoding="utf-8")
        self.assertIn("Aggregate Persistence Preflight", text)

    def test_testing_reference_requires_repository_semantic_rules(self):
        text = TESTING.read_text(encoding="utf-8")
        self.assertIn("Repository naming and aggregate adapter rules", text)
        for required in (
            "project-local aggregate inventory",
            "AggregateRepository",
            "MybatisPlusAggregateRepository",
            "direct implementation",
            "Repository suffix",
        ):
            self.assertIn(required, text)


if __name__ == "__main__":
    unittest.main()
