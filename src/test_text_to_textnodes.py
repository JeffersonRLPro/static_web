import unittest

from textnode import TextNode, TextType
from text_to_textnodes import text_to_textnodes

class TestTexttoTextNodes(unittest.TestCase):
    def test_text_to_textNodes_with_everything(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        result = text_to_textnodes(text)

        self.assertListEqual(
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("text", TextType.BOLD),
                TextNode(" with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" and an ", TextType.TEXT),
                TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode(" and a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
            ],
            result,
        )
    
    def test_text_to_textnodes_without_string(self):
        text = 123
        with self.assertRaises(TypeError):
            text_to_textnodes(text)

    def test_text_to_textnode_with_nothing(self):
        text = "This text contains nothing for the functions to split"
        results = text_to_textnodes(text)

        self.assertListEqual(
            [
                TextNode("This text contains nothing for the functions to split", TextType.TEXT),
            ],
            results,
        )
    
    def test_text_to_textnodes_with_bold_only(self):
        text = "**This is nice and bolded** while this is not *bolded*"
        results = text_to_textnodes(text)

        self.assertListEqual(
            [
                TextNode("This is nice and bolded", TextType.BOLD),
                TextNode(" while this is not *bolded*", TextType.TEXT),
            ],
            results,
        )
    
    def test_text_to_nodes_with_italic_and_links(self):
        results = text_to_textnodes("This is text with an _italic word_ and a link [to bootdev](https://boot.dev)")

        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("italic word", TextType.ITALIC),
                TextNode(" and a link ", TextType.TEXT),
                TextNode("to bootdev", TextType.LINK, "https://boot.dev"),
            ],
            results,
        )

    def test_text_to_textnode_invalidMarkdown(self):
        with self.assertRaises(Exception):
            text_to_textnodes("This should raise an error _due to missing end, but includes a link [to bootdev](https://boot.dev)")

    def test_text_to_textnode_complex_error(self):
        with self.assertRaises(Exception):
            text_to_textnodes("This is **text* with an _italic word and a code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)")

if __name__ == "__main__":
    unittest.main()