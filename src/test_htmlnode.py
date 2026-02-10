import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

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

    def test_props_to_html_with_ints(self):
        node = HTMLNode("a", None, None, {"href": "https://www.google.com", "target": 3})
        expected_res = 'href="https://www.google.com" target="3"'
        self.assertEqual(node.props_to_html(), expected_res)

    def test_propsToHtmlNone(self):
        node = HTMLNode("a")
        self.assertEqual(node.props_to_html(), None) 
    
    def test_leaf_to_html(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leafNode_to_html_with_value_none(self):
        with self.assertRaises(ValueError):
            LeafNode("b", None).to_html()
    
    def test_leaf_to_html_with_link(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')
    
    def test_repr_with_link(self):
        node = HTMLNode("a", "Click me!", None, {"href": "https://www.google.com", "target": "_blank"})
        string = f"""HTMLNode(
        tag: a,
        value: Click me!,
        children: None,
        props: {node.props}
        )
        """
        self.assertEqual(repr(node), string)

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
    
    def test_parentNode_with_none_children(self):
        with self.assertRaises(ValueError):
            ParentNode("p", None)

    def test_parentNode_with_empty_children(self):
        with self.assertRaises(ValueError):
            ParentNode("p", [])

    def test_parentNode_with_children_not_HTMLNode(self):
        child_node = LeafNode("b", "grandchild")
        child_node2 = LeafNode("p", "hello, world!")
        with self.assertRaises(ValueError):
            ParentNode("p", [child_node, child_node2, 3, "hello"])

if __name__ == "__main__":
    unittest.main()