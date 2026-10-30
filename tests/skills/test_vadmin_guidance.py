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

    def test_business_views_route_to_page_interaction_reference(self):
        skill = (USING_VADMIN / "SKILL.md").read_text(encoding="utf-8")
        module = (USING_VADMIN / "references" / "module-declaration.md").read_text(encoding="utf-8")
        first_use = (USING_VADMIN / "references" / "first-use.md").read_text(encoding="utf-8")
        self.assertIn("references/page-interactions.md", skill)
        self.assertIn("page-interactions.md", module)
        self.assertIn("page-interactions.md", first_use)
        self.assertIn("adding or changing a business administration view", skill)
        self.assertNotIn("Keep domain-specific CSS scoped", module)

    def test_page_interaction_reference_selects_shared_patterns(self):
        text = (USING_VADMIN / "references" / "page-interactions.md").read_text(encoding="utf-8")
        for required in (
            "AdminPageFrame",
            "PageHeader",
            "PageToolbar",
            "DataWorkspace",
            "PagedGrid",
            "CompactDataItem",
            "EditorDialog",
            "DetailDialog",
            "ConfirmationDialog",
            "OperationFeedback",
            "EmptyState",
            "no data",
            "filtered-empty",
            "failure",
            "Aura",
            "selected VAdmin release documentation",
            "Do not add business-module CSS",
            "extend VAdmin",
        ):
            self.assertIn(required, text)
        self.assertNotIn("new AdminPageFrame", text)
        self.assertNotIn("Lumo", text)

    def test_consumer_visual_language_choice_is_removed(self):
        first_use = (USING_VADMIN / "references" / "first-use.md").read_text(encoding="utf-8")
        result = (USING_VADMIN / "references" / "implementation-guidance-result.md").read_text(encoding="utf-8")
        prompt = (USING_VADMIN / "agents" / "openai.yaml").read_text(encoding="utf-8")
        shell = (USING_VADMIN / "references" / "shell-boundaries.md").read_text(encoding="utf-8")
        skill = (USING_VADMIN / "SKILL.md").read_text(encoding="utf-8")
        for text in (first_use, result, prompt):
            self.assertNotIn("visual-language", text)
            self.assertNotIn("Visual language", text)
            self.assertNotRegex(text, r"\bant\b")
        self.assertIn("Do not add business-module CSS", shell)
        self.assertIn("Do not add business-module CSS", skill)
        self.assertNotIn("Lumo", shell)
        self.assertNotIn("visual-language", shell)


if __name__ == "__main__":
    unittest.main()
