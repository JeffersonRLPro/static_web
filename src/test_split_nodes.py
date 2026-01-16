import unittest

from split_nodes import split_nodes_delimiter
from textnode import TextType, TextNode

class TestSplitNodes(unittest.TestCase):
    def test_split_nodes_with_nothing(self):
        node = TextNode("This has no special delimiter present", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)

        self.assertEqual([node], result)

    def test_split_nodes_with_delimiter(self):
        node = TextNode('This has a `special` delimiter present', TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)

        self.assertEqual(len(result), 3)
        self.assertEqual(result[0].text, "This has a ")
        self.assertEqual(result[0].text_type, TextType.TEXT)
        self.assertEqual(result[1].text, "special")
        self.assertEqual(result[1].text_type, TextType.CODE)
        self.assertEqual(result[2].text, " delimiter present")
        self.assertEqual(result[2].text_type, TextType.TEXT)

    def test_split_nodes_with_missing_end(self):
        node = TextNode("This has a missing end **delimiter somewhere", TextType.TEXT)

        with self.assertRaises(Exception):
            split_nodes_delimiter([node], "**", TextType.BOLD)
    
    def test_split_nodes_with_missing_beginning(self):
        node = TextNode("This has a missing end delimiter** somewhere", TextType.TEXT)

        with self.assertRaises(Exception):
            split_nodes_delimiter([node], "**", TextType.BOLD)
    
    def test_split_nodes_with_italic(self):
        node = TextNode('This has a _special_ delimiter present', TextType.TEXT)
        result = split_nodes_delimiter([node], "_", TextType.ITALIC)

        self.assertEqual(len(result), 3)
        self.assertEqual(result[0].text, "This has a ")
        self.assertEqual(result[0].text_type, TextType.TEXT)
        self.assertEqual(result[1].text, "special")
        self.assertEqual(result[1].text_type, TextType.ITALIC)
        self.assertEqual(result[2].text, " delimiter present")
        self.assertEqual(result[2].text_type, TextType.TEXT)

    def test_split_nodes_with_bold(self):
        node = TextNode('This has a **special** delimiter present', TextType.TEXT)
        result = split_nodes_delimiter([node], "**", TextType.BOLD)

        self.assertEqual(len(result), 3)
        self.assertEqual(result[0].text, "This has a ")
        self.assertEqual(result[0].text_type, TextType.TEXT)
        self.assertEqual(result[1].text, "special")
        self.assertEqual(result[1].text_type, TextType.BOLD)
        self.assertEqual(result[2].text, " delimiter present")
        self.assertEqual(result[2].text_type, TextType.TEXT)
    
    def test_split_nodes_with_non_text_type(self):
        node = TextNode("This has no special delimiter present", TextType.BOLD)
        result = split_nodes_delimiter([node], "`", TextType.CODE)

        self.assertEqual([node], result)

    def test_split_nodes_with_non_textNodes(self):
        with self.assertRaises(TypeError):
            split_nodes_delimiter("im not a list of nodes", "**", TextType.BOLD)

    def test_split_nodes_with_list_of_non_TextNodes(self):
        with self.assertRaises(TypeError):
            split_nodes_delimiter(["no TextNodes here champ"], "**", TextType.BOLD)
    
    def test_split_nodes_with_multiple_nodes_with_nothing(self):
        node1 = TextNode("This has no special delimiter present", TextType.BOLD)
        node2 = TextNode("This also has nothing", TextType.TEXT)
        result = split_nodes_delimiter([node1, node2], "`", TextType.CODE)

        self.assertEqual([node1, node2], result)
    
    def test_split_nodes_with_multiple_bold_nodes(self):
        node1 = TextNode("This has a **special** delimiter present", TextType.TEXT)
        node2 = TextNode("This also has **something** special", TextType.TEXT)
        result = split_nodes_delimiter([node1, node2], "**", TextType.BOLD)

        self.assertEqual(len(result), 6)
        self.assertEqual(result[0].text, "This has a ")
        self.assertEqual(result[0].text_type, TextType.TEXT)
        self.assertEqual(result[1].text, "special")
        self.assertEqual(result[1].text_type, TextType.BOLD)
        self.assertEqual(result[2].text, " delimiter present")
        self.assertEqual(result[2].text_type, TextType.TEXT)
        self.assertEqual(result[3].text,"This also has ")
        self.assertEqual(result[3].text_type, TextType.TEXT)
        self.assertEqual(result[4].text, "something")
        self.assertEqual(result[4].text_type, TextType.BOLD)
        self.assertEqual(result[5].text, " special")
        self.assertEqual(result[5].text_type, TextType.TEXT)