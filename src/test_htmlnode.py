import unittest

from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_reprForP(self):
        node = HTMLNode("p", "This is the contents of the paragraph tag")
        string = """HTMLNode(
        tag: p,
        value: This is the contents of the paragraph tag,
        children: None,
        props: None
        )
        """
        self.assertEqual(repr(node), string)
    
    def test_propsToHtml(self):
        node = HTMLNode("a", None, None, {"href": "https://www.google.com", "target": "_blank"})
        expected_res = 'href="https://www.google.com" target="_blank"'
        self.assertEqual(node.props_to_html(), expected_res) 

    def test_propsToHtmlNone(self):
        node = HTMLNode("a")
        self.assertEqual(node.props_to_html(), None) 
    
    def test_leaf_to_html(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
    def test_leaf_to_html_with_link(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')
    