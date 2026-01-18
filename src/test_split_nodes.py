import unittest

from split_nodes import split_nodes_delimiter, split_nodes_image, split_nodes_link
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

    def test_split_nodes_with_delimiter_at_start_or_end(self):
        node = TextNode("**This** has a special delimiter present", TextType.TEXT)
        result = split_nodes_delimiter([node], "**", TextType.BOLD)

        self.assertEqual(len(result), 2)
        self.assertEqual(result[0].text, "This")
        self.assertEqual(result[0].text_type, TextType.BOLD)
        self.assertEqual(result[1].text, " has a special delimiter present")
        self.assertEqual(result[1].text_type, TextType.TEXT)

        node2 = TextNode("This has a special delimiter **present**", TextType.TEXT)
        result2 = split_nodes_delimiter([node2], "**", TextType.BOLD)
        
        self.assertEqual(len(result2), 2)
        self.assertEqual(result2[0].text, "This has a special delimiter ")
        self.assertEqual(result2[0].text_type, TextType.TEXT)
        self.assertEqual(result2[1].text, "present")
        self.assertEqual(result2[1].text_type, TextType.BOLD)

    def test_split_nodes_with_mulitple_delimiters(self):
        node = TextNode("**This** has a **special** delimiter present", TextType.TEXT)
        result = split_nodes_delimiter([node], "**", TextType.BOLD)

        self.assertEqual(len(result), 4)
        self.assertEqual(result[0].text, "This")
        self.assertEqual(result[0].text_type, TextType.BOLD)
        self.assertEqual(result[1].text, " has a ")
        self.assertEqual(result[1].text_type, TextType.TEXT)
        self.assertEqual(result[2].text, "special")
        self.assertEqual(result[2].text_type, TextType.BOLD)
        self.assertEqual(result[3].text, " delimiter present")
        self.assertEqual(result[3].text_type, TextType.TEXT)
    
    def test_split_images_multiple(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )
    
    def test_split_image_start(self):
        node = TextNode("![image](https://i.imgur.com/zjjcJKZ.png) This node starts with an image", TextType.TEXT)
        results = split_nodes_image([node])

        self.assertListEqual(
            [
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" This node starts with an image", TextType.TEXT),
            ],
            results,
        )

    def test_split_image_end(self):
        node = TextNode("This node ends with an image ![image](https://i.imgur.com/zjjcJKZ.png)", TextType.TEXT)
        results = split_nodes_image([node])

        self.assertListEqual(
            [
                TextNode("This node ends with an image ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            ],
            results,
        )
    
    def test_split_image_end_and_start(self):
        node = TextNode("![image](https://i.imgur.com/zjjcJKZ.png) This node starts and ends with an image ![image](https://i.imgur.com/zjjcJKZ.png)", TextType.TEXT)
        results = split_nodes_image([node])

        self.assertListEqual(
            [
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" This node starts and ends with an image ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            ],
            results,
        )
    
    def test_split_image_no_link(self):
        node = TextNode("This node has no link for an image", TextType.TEXT)
        results = split_nodes_image([node])

        self.assertEqual([node], results)

    def test_split_image_multiple_nodes(self):
        node1 = TextNode("![image](https://i.imgur.com/zjjcJKZ.png) This node starts with an image", TextType.TEXT)
        node2 = TextNode("![image](https://i.imgur.com/zjjcJKZ.png) This node starts and ends with an image ![image](https://i.imgur.com/zjjcJKZ.png)", TextType.TEXT)
        results = split_nodes_image([node1, node2])

        self.assertListEqual(
            [
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" This node starts with an image", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" This node starts and ends with an image ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            ],
            results,
        )

    def test_split_image_middle(self):
        node = TextNode("This node has the image in the middle ![image](https://i.imgur.com/zjjcJKZ.png) now that is a nice change", TextType.TEXT)
        results = split_nodes_image([node])

        self.assertListEqual(
            [
                TextNode("This node has the image in the middle ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" now that is a nice change", TextType.TEXT),
            ],
            results,
        )

    def test_split_image_with_parameter(self):
        with self.assertRaises(TypeError):
            split_nodes_image("this is not a list")

    def test_split_image_with_invalid_type_in_list(self):
        with self.assertRaises(TypeError):
            split_nodes_image(["This is not a node"])
    
    def test_split_image_with_nonText_textType(self):
        node = TextNode("This is an image ![image](https://i.imgur.com/zjjcJKZ.png)", TextType.BOLD)
        results = split_nodes_image([node])

        self.assertEqual([node], results)
    
    def test_split_link_multiple(self):
        node = TextNode("This node has a link [to youtube](https://www.youtube.com/@bootdotdev) and a link [to bootdev](https://www.boot.dev) cool!", TextType.TEXT)
        results = split_nodes_link([node])

        self.assertListEqual(
            [
                TextNode("This node has a link ", TextType.TEXT),
                TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"),
                TextNode(" and a link ", TextType.TEXT),
                TextNode("to bootdev", TextType.LINK, "https://www.boot.dev"),
                TextNode(" cool!", TextType.TEXT),
            ],
            results,
        )
    
    def test_split_link_start(self):
        node = TextNode("[to bootdev](https://www.boot.dev) This node has a link first", TextType.TEXT)
        results = split_nodes_link([node])

        self.assertListEqual(
            [
                TextNode("to bootdev", TextType.LINK, "https://www.boot.dev"),
                TextNode(" This node has a link first", TextType.TEXT),
            ],
            results,
        )

    def test_split_link_end(self):
        node = TextNode("This node has a link last [to bootdev](https://www.boot.dev)", TextType.TEXT)
        results = split_nodes_link([node])

        self.assertListEqual(
            [
                TextNode("This node has a link last ", TextType.TEXT),
                TextNode("to bootdev", TextType.LINK, "https://www.boot.dev"),
            ],
            results,
        )
    
    def test_split_link_start_and_end(self):
        node = TextNode("[to youtube](https://www.youtube.com/@bootdotdev) this node has a link at the start and at the end [to bootdev](https://www.boot.dev)", TextType.TEXT)
        results = split_nodes_link([node])

        self.assertListEqual(
            [
                TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"),
                TextNode(" this node has a link at the start and at the end ", TextType.TEXT),
                TextNode("to bootdev", TextType.LINK, "https://www.boot.dev"),
            ],
            results,
        )

    def test_split_link_no_link(self):
        node = TextNode("There is no link present", TextType.TEXT)
        results = split_nodes_link([node])

        self.assertEqual([node], results)

    def test_split_link_with_multiple_nodes(self):
        node1 = TextNode("[to youtube](https://www.youtube.com/@bootdotdev) this node has a link at the start", TextType.TEXT)
        node2 = TextNode("This node has a link [to youtube](https://www.youtube.com/@bootdotdev) and [to bootdev](https://www.boot.dev) cool!", TextType.TEXT)
        results = split_nodes_link([node1, node2])

        self.assertListEqual(
            [
                TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"),
                TextNode(" this node has a link at the start", TextType.TEXT),
                TextNode("This node has a link ", TextType.TEXT),
                TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"),
                TextNode(" and ", TextType.TEXT),
                TextNode("to bootdev", TextType.LINK, "https://www.boot.dev"),
                TextNode(" cool!", TextType.TEXT),
            ],
            results,
        )
    
    def test_split_link_middle(self):
        node = TextNode("This node has a link in the middle [to bootdev](https://www.boot.dev) this is so very cool", TextType.TEXT)
        results = split_nodes_link([node])

        self.assertListEqual(
            [
                TextNode("This node has a link in the middle ", TextType.TEXT),
                TextNode("to bootdev", TextType.LINK, "https://www.boot.dev"),
                TextNode(" this is so very cool", TextType.TEXT),
            ],
            results,
        )

    def test_split_link_with_invalid_parameter(self):
        with self.assertRaises(TypeError):
            split_nodes_link("this is not a list")

    def test_split_link_with_invalid_list_objects(self):
        with self.assertRaises(TypeError):
            split_nodes_link(["This is not a list of TextNode objects"])

    def test_split_link_with_nonTEXT_TextType(self):
        node = TextNode("This is a non text **type**", TextType.BOLD)
        results = split_nodes_link([node])

        self.assertEqual([node], results)