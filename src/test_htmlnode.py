import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_empty(self):
        node = HTMLNode(tag="a", value="link", props=None)
        self.assertEqual(node.props_to_html(), "")

    def test_props_to_html_single(self):
        node = HTMLNode(tag="a", value="link", props={"href": "https://example.com"})
        self.assertEqual(node.props_to_html(), ' href="https://example.com"')

    def test_props_to_html_multiple(self):
        node = HTMLNode(tag="a", value="link", props={"href": "https://example.com", "target": "_blank"})
        # Order of dict items is preserved in Python 3.7+, so this is safe
        self.assertEqual(node.props_to_html(), ' href="https://example.com" target="_blank"')

    def test_repr(self):
        node = HTMLNode(tag="p", value="Hello", children=None, props={"class": "text"})
        rep = repr(node)
        self.assertIn("HTMLNode", rep)
        self.assertIn("p", rep)
        self.assertIn("Hello", rep)
        self.assertIn("class", rep)

if __name__ == "__main__":
    unittest.main()
