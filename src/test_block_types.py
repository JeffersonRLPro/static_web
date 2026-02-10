import unittest

from block_types import BlockType, block_to_block_type

class TestBlockType(unittest.TestCase):
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




this is code```""".strip()
        results = block_to_block_type(text)

        self.assertEqual(results, BlockType.CODE)

    def test_quote_block_type(self):
        text = ">this is a quote"
        results = block_to_block_type(text)

        self.assertEqual(results, BlockType.QUOTE)

    def test_quote_multiple_lines(self):
        # .strip(), since we always assume the strings that are passed to the function are already stripped
        text = """
>this is a quote
>this is another quote
>last ones
""".strip()
        results = block_to_block_type(text)

        self.assertEqual(results, BlockType.QUOTE)

    def test_quote_space(self):
        text = """
> this is a quote
> this is another quote
> last ones
""".strip()
        results = block_to_block_type(text)

        self.assertEqual(results, BlockType.QUOTE)

    def test_not_quote_block(self):
        text = """this is not a quote block
>this is a quote
>this is another quote
>last ones
""".strip()
        results = block_to_block_type(text)

        self.assertEqual(results, BlockType.PARAGRAPH)

    def test_middle_missing_quote_char(self):
        text = """
>this is a quote
>this is another quote
another quote
>last one
""".strip()
        results = block_to_block_type(text)

        self.assertEqual(results, BlockType.PARAGRAPH)
    
    def test_middle_extra_space(self):
        text = """
>this is a quote
>this is another quote
 >another quote
>last one
""".strip()
        results = block_to_block_type(text)

        self.assertEqual(results, BlockType.PARAGRAPH)

    def test_optional_space(self):
        text = """
> this is a quote
>this is another quote
> another quote
>last one
""".strip()
        results = block_to_block_type(text)

        self.assertEqual(results, BlockType.QUOTE)
    
    def test_double_quote_char(self):
        text = ">> This is a quote".strip()
        results = block_to_block_type(text)

        self.assertEqual(results, BlockType.QUOTE)

    def test_undordered_lists(self):
        text = "- this is an unordered list".strip()
        results = block_to_block_type(text)

        self.assertEqual(results, BlockType.UNORDERED_LIST)
    
    def test_multiple_elements_in_unordered_list(self):
        text = """
- this is one thing on the list 
- this is another item
- another item
- last item
""".strip()
        results = block_to_block_type(text)

        self.assertEqual(results, BlockType.UNORDERED_LIST)
    
    def test_missing_unordered_list_char(self):
        text = """
- this is one thing on the list 
- this is another item
another item
- last item
""".strip()
        results = block_to_block_type(text)

        self.assertEqual(results, BlockType.PARAGRAPH)

    def test_missing_space(self):
        text = """
- this is one thing on the list 
- this is another item
-another item
- last item
""".strip()
        results = block_to_block_type(text)

        self.assertEqual(results, BlockType.PARAGRAPH)

    def test_ordered_list(self):
        text = """
1. This is the first item
""".strip()
        results = block_to_block_type(text)

        self.assertEqual(results, BlockType.ORDERED_LIST)
    
    def test_multiple_items_in_ordered_list(self):
        text = """
1. This is the first item 
2. this is another item
3. another item
4. last item
""".strip()
        results = block_to_block_type(text)

        self.assertEqual(results, BlockType.ORDERED_LIST)

    def test_missing_interval(self):
        text = """
1. This is the first item 
2. this is another item
3. another item
last item
""".strip()
        results = block_to_block_type(text)

        self.assertEqual(results, BlockType.PARAGRAPH)
    
    def test_extra_char_after_interval(self):
        text = """
1. This is the first item 
2. this is another item
3. another item
4w. last item
""".strip()
        results = block_to_block_type(text)

        self.assertEqual(results, BlockType.PARAGRAPH)

    def test_missing_space(self):
        text = """
1.This is the first item 
2.this is another item
3. another item
4. last item
""".strip()
        results = block_to_block_type(text)

        self.assertEqual(results, BlockType.PARAGRAPH)
    
    def test_missing_period(self):
        text = """
1. This is the first item 
2 this is another item
3. another item
4 last item
""".strip()
        results = block_to_block_type(text)

        self.assertEqual(results, BlockType.PARAGRAPH)

    def test_no_block_type_chars(self):
        text = "This has nothing".strip()
        results = block_to_block_type(text)

        self.assertEqual(results, BlockType.PARAGRAPH)

    def test_non_string(self):
        text = ["this is a list"]
        with self.assertRaises(TypeError):
            block_to_block_type(text)

    if __name__ == "__main__":
        unittest.main()