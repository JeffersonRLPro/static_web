import unittest

from textnode import TextType, TextNode
from text_node_to_html import text_node_to_html_node

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
    
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("This is a bold text node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a bold text node")

    def test_italic(self):
        node = TextNode("This is a italic text node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is a italic text node")
    
    def test_code(self):
        node = TextNode("This is a code text node", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is a code text node")
    
    def test_link(self):
        node = TextNode("This is a link text node", TextType.LINK, "www.url.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a link text node")
        self.assertEqual(html_node.props, {"href": "www.url.com"})
    
    def test_image(self):
        node = TextNode("This is an image text node", TextType.IMAGE, "www.image.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {"src": "www.image.com", "alt": "This is an image text node"})

    def test_non_matching_textType_Enum(self):
        node = TextNode("This should give an error", None)
        with self.assertRaises(Exception):
            text_node_to_html_node(node)
    
    def test_image_with_no_url(self):
        node = TextNode("This is an image text node", TextType.IMAGE)
        with self.assertRaises(ValueError):
            text_node_to_html_node(node)

    def test_link_with_no_url(self):
        node = TextNode("This is a link text node", TextType.LINK)
        with self.assertRaises(ValueError):
            text_node_to_html_node(node)
    
    def test_image_with_empty_string(self):
        node = TextNode("This is an image text node", TextType.IMAGE, "")
        with self.assertRaises(ValueError):
            text_node_to_html_node(node)

    def test_link_with_empty_string(self):
        node = TextNode("This is a link text node", TextType.LINK, "")
        with self.assertRaises(ValueError):
            text_node_to_html_node(node)

if __name__ == "__main__":
    unittest.main()