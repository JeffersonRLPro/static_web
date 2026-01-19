import unittest

from markdown_to_blocks import markdown_to_blocks

class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks_normal(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )
    
    def test_markdown_to_blocks_excessive_newlines(self):
        md = """
This is a block with normal **stuff**



This is another one with some _stuff_ and some code `yay`





last block with list
- hello
- everything is good now
"""
        blocks = markdown_to_blocks(md)
        self.assertListEqual(
            blocks,
            [
                "This is a block with normal **stuff**",
                "This is another one with some _stuff_ and some code `yay`",
                "last block with list\n- hello\n- everything is good now",
            ],
        )
    
    def test_markdown_to_blocks_with_one_block(self):
        md = """
This is a block with normal **stuff**
and no new blocks are here
just one big block
"""
        blocks = markdown_to_blocks(md)
        self.assertListEqual(
            blocks,
            [
                "This is a block with normal **stuff**\nand no new blocks are here\njust one big block",
            ],
        )
    
    def test_markdown_to_blocks_with_start(self):
        md = """











This has lots of newline at the start
# here is a title


New block with some `code` here and some **bold** words

new block ends here
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This has lots of newline at the start\n# here is a title",
                "New block with some `code` here and some **bold** words",
                "new block ends here",
            ],
        )
    
    def test_markdown_to_blocks_with_newlines_at_end(self):
        md = """
This has lots of newline at the end
# here is a title


New block with some `code` here and some **bold** words

new block ends here














"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This has lots of newline at the end\n# here is a title",
                "New block with some `code` here and some **bold** words",
                "new block ends here",
            ],
        )