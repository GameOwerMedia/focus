"""Structure checks for the focus skill. Standard library only: python -m unittest discover -s tests"""

import json
import os
import re
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILL = os.path.join(ROOT, "skills", "focus")
MARKETS = os.path.join(SKILL, "references", "markets")
SECTIONS = ["Detect", "Language and style", "Panel A", "Panel B", "Rules and regulators", "Benchmarks", "Labels"]


def read(*parts):
    with open(os.path.join(*parts), encoding="utf-8") as fh:
        return fh.read()


def frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return {}
    out, key = {}, None
    for line in m.group(1).split("\n"):
        kv = re.match(r"^([a-z][a-z0-9_-]*):\s*(.*)$", line)
        if kv:
            key = kv.group(1)
            out[key] = kv.group(2).strip()
        elif key and line.startswith(" "):
            out[key] = (out[key] + " " + line.strip()).strip()
    return out


class TestSkill(unittest.TestCase):
    def setUp(self):
        self.text = read(SKILL, "SKILL.md")
        self.fm = frontmatter(self.text)

    def test_frontmatter(self):
        self.assertEqual(self.fm.get("name"), "focus")
        desc = self.fm.get("description", "").lstrip(">").strip()
        self.assertGreater(len(desc), 100)
        self.assertLessEqual(len(desc), 1024, "description must fit the 1024-character limit")
        self.assertIn("argument-hint", self.fm)

    def test_core_sections(self):
        for heading in ("Panel A", "Panel B", "Joint synthesis", "Rules that hold everywhere"):
            self.assertIn(heading, self.text)
        self.assertIn("All personas are fictional", self.text)

    def test_referenced_files_exist(self):
        for ref in re.findall(r"`(references/[^`<>]+\.md)`", self.text):
            self.assertTrue(os.path.exists(os.path.join(SKILL, ref)), ref)


class TestMarkets(unittest.TestCase):
    def test_world_exists(self):
        self.assertTrue(os.path.exists(os.path.join(MARKETS, "world.md")))

    def test_every_market_has_all_sections(self):
        files = [f for f in os.listdir(MARKETS) if f.endswith(".md")]
        self.assertIn("TEMPLATE.md", files)
        for f in files:
            text = read(MARKETS, f)
            heads = re.findall(r"^## (.+?)\s*$", text, re.M)
            for s in SECTIONS:
                self.assertIn(s, heads, "%s is missing the '## %s' section" % (f, s))
            if f != "TEMPLATE.md":
                self.assertRegex(f, r"^[a-z]{2,8}\.md$", "market file names are short lower-case codes")


class TestPlugin(unittest.TestCase):
    def test_manifests_agree(self):
        plugin = json.loads(read(ROOT, ".claude-plugin", "plugin.json"))
        market = json.loads(read(ROOT, ".claude-plugin", "marketplace.json"))
        self.assertEqual(plugin["name"], "focus")
        entry = [p for p in market["plugins"] if p["name"] == "focus"][0]
        self.assertEqual(entry["version"], plugin["version"])
        self.assertIn("## [%s]" % plugin["version"], read(ROOT, "CHANGELOG.md"))


class TestExamples(unittest.TestCase):
    def test_example_outputs_follow_the_shape(self):
        for name in ("output-full.md", "output-lite.md"):
            text = read(ROOT, "examples", "larder", name)
            self.assertIn("All personas are fictional", text)
            self.assertIn("## Panel A", text)
            self.assertIn("## Panel B", text)
            self.assertNotIn("—", text, "%s contains an em dash" % name)

    def test_example_counts_add_up(self):
        for name, size in (("output-full.md", 10), ("output-lite.md", 3)):
            text = read(ROOT, "examples", "larder", name)
            self.assertEqual(len(re.findall(r"^### A\d+\. ", text, re.M)), size, name)
            self.assertEqual(len(re.findall(r"^### B\d+\. ", text, re.M)), size, name)
            synthesis = text[text.index("## Synthesis"):]
            for panel, labels in (("A", ("YES", "MAYBE", "NO")), ("B", ("FUND", "CONDITIONAL", "PASS"))):
                line = re.search(r"Panel %s:.*" % panel, synthesis).group(0)
                counts = [int(re.search(r"(\d+) %s\b" % label, line).group(1)) for label in labels]
                self.assertEqual(sum(counts), size, "%s panel %s scoreboard: %s" % (name, panel, line))


if __name__ == "__main__":
    unittest.main()
