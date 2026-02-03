import unittest

from block_types import BlockType, block_to_block_type

class TestBlocktype(unittest.TestCase):
    def test_headings_block_case(self):
        text = "# Title"
        results = block_to_block_type(text)

        self.assertEqual(results, BlockType.HEADING)
    
    def test_heading_multiple_hashes(self):
        text = "##### Title"
        results = block_to_block_type(text)

        self.assertEqual(results, BlockType.HEADING)

    def test_heading_too_many_dashes(self):
        text = "####### Title"
        results = block_to_block_type(text)

        self.assertEqual(results, BlockType.PARAGRAPH)

    def test_heading_no_space(self):
        text = "###Title"
        results = block_to_block_type(text)

        self.assertEqual(results, BlockType.PARAGRAPH)

    def test_code_blockcase(self):
        text = """```
        this is code
        ```"""
        results = block_to_block_type(text)

        self.assertEqual(results, BlockType.CODE)
    
    def test_code_blockcase_no_ending_space(self):
        text = """```
        this is still code```"""
        results = block_to_block_type(text)

        self.assertEqual(results, BlockType.CODE)

    def test_code_no_newline_at_start(self):
        text = """```this is code```"""
        results = block_to_block_type(text)

        self.assertEqual(results, BlockType.PARAGRAPH)

    def test_code_missing_pair(self):
        text = """```
        this is code"""
        results = block_to_block_type(text)

        self.assertEqual(results, BlockType.PARAGRAPH)

    def test_code_spaces_between(self):
        text = """```
        
        
        
        
        
        this is code```"""
        results = block_to_block_type(text)

        self.assertEqual(results, BlockType.CODE)

    def test_quote_block_type(self):
        text = ">this is a quote"
        results = block_to_block_type(text)

        self.assertEqual(results, BlockType.QUOTE)