import unittest

from textnode import TextType, TextNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", TextType.LINK)
        self.assertEqual(repr(node), "TextNode(This is a text node, link, None)")
    
    def test_texttype(self):
        node = TextNode("This is a text node", TextType.LINK)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_difftext(self):
        node = TextNode("This is a different text node", TextType.LINK)
        node2 = TextNode("This is a text node", TextType.LINK)
        self.assertNotEqual(node, node2)

    def test_diffurl(self):
        node = TextNode("This is a text node", TextType.LINK, "https://thisisadifferenturl.com")
        node2 = TextNode("This is a text node", TextType.LINK, "https://dummysite.gov")
        self.assertNotEqual(node, node2)
    
    def test_sameUrl(self):
        node = TextNode("This is a text node", TextType.LINK, "https://dummysite.gov")
        node2 = TextNode("This is a text node", TextType.LINK, "https://dummysite.gov")
        self.assertEqual(node, node2)

    def test_defaultUrl(self):
        node = TextNode("This is a text node", TextType.LINK)
        node2 = TextNode("This is a text node", TextType.LINK, "https://dummysite.gov")
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()