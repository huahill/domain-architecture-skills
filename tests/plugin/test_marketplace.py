import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MARKETPLACE = ROOT / ".agents" / "plugins" / "marketplace.json"


class MarketplaceManifestTests(unittest.TestCase):
    def test_codex_plugin_category_is_developer_tools(self):
        plugin = json.loads((ROOT / ".codex-plugin" / "plugin.json").read_text(encoding="utf-8"))
        self.assertEqual(plugin["interface"]["category"], "Developer Tools")

    def test_codex_marketplace_uses_local_root_plugin_source(self):
        data = json.loads(MARKETPLACE.read_text(encoding="utf-8"))
        self.assertEqual(data["name"], "huahill")
        self.assertEqual(len(data["plugins"]), 1)
        plugin = data["plugins"][0]
        self.assertEqual(plugin["name"], "domain-architecture")
        self.assertEqual(plugin["source"], {"source": "local", "path": "./"})
        self.assertEqual(plugin["category"], "Developer Tools")

    def test_readmes_require_marketplace_before_plugin_add(self):
        for name in ("README.md", "README_ZH.md"):
            text = (ROOT / name).read_text(encoding="utf-8")
            self.assertIn("codex plugin marketplace add huahill/domain-architecture-skills", text)
            self.assertIn("codex plugin add domain-architecture@huahill", text)
            self.assertIn("codex plugin list --marketplace huahill", text)
            self.assertNotRegex(text, r"`0\.\d+\.\d+`")
            self.assertLess(
                text.index("codex plugin marketplace add huahill/domain-architecture-skills"),
                text.index("codex plugin add domain-architecture@huahill"),
            )


if __name__ == "__main__":
    unittest.main()
