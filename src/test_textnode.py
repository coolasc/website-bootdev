import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_equal_text(self):
        node = TextNode("Text 1", TextType.BOLD)
        node2 = TextNode("Text 2", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_not_equal_type(self):
        node = TextNode("Same text", TextType.BOLD)
        node2 = TextNode("Same text", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_not_equal_url(self):
        node = TextNode("Same text", TextType.BOLD, "http://a.com")
        node2 = TextNode("Same text", TextType.BOLD, "http://b.com")
        self.assertNotEqual(node, node2)

    def test_url_none(self):
        node = TextNode("Text", TextType.LINK)
        node2 = TextNode("Text", TextType.LINK, None)
        self.assertEqual(node, node2)

if __name__ == "__main__":
    unittest.main()
