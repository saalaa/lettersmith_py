"""
Unit tests for Doc
"""

import unittest
from pathlib import Path
from lettersmith import doc as Doc

module_path = Path(__file__).parent
fixtures_path = Path(module_path, "package_data", "fixtures")

class test_bare_doc(unittest.TestCase):
    def setUp(self):
        doc_path = fixtures_path.joinpath("Bare doc.md")
        doc = Doc.load(doc_path, relative_to=fixtures_path)
        self.doc = doc

    def test_content(self):
        self.assertEqual(self.doc["content"], "Lorem ipsum")

    def test_meta(self):
        """
        Meta should always be a dict
        """
        self.assertEqual(type(self.doc["meta"]), dict)

    def test_id_path(self):
        self.assertEqual(str(self.doc["id_path"]), "Bare doc.md")


class test_doc_with_meta(unittest.TestCase):
    def setUp(self):
        doc_path = fixtures_path.joinpath("Doc with meta.md")
        doc = Doc.load(doc_path, relative_to=fixtures_path)
        self.doc = doc

    def test_content(self):
        self.assertEqual(self.doc["content"], "Lorem ipsum")

    def test_meta(self):
        """
        Meta should always be a dict
        """
        self.assertEqual(self.doc["meta"]["title"], "Doc title")


if __name__ == '__main__':
    unittest.main()