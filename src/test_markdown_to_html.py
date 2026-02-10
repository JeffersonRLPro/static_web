import unittest
from markdown_to_html import markdown_to_html_node

class TestMarkdownToHTML(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )
    
    def test_headings(self):
        md = """
#### this is a level four heading
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h4>this is a level four heading</h4></div>"
        )
    
    def test_too_many_hash(self):
        md = """
####### This should be an ordinary paragraph
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>####### This should be an ordinary paragraph</p></div>"
        )

    def test_quotes(self):
        md = """
> this is one quote
> another
> last quote
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>this is one quote another last quote</blockquote></div>"
        )
    
    def test_quotes_no_optional_space(self):
        md = """
>this is one quote
>another
>last quote
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>this is one quote another last quote</blockquote></div>"
        )

    def test_unordered_lists(self):
        md = """
- This is an item
- another item
- cool item here
- last item
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This is an item</li><li>another item</li><li>cool item here</li><li>last item</li></ul></div>"
        )
    
    def test_unordered_lists_no_space(self):
        md = """
-This is an item
-another item
-cool item here
-last item
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>-This is an item -another item -cool item here -last item</p></div>"
        )
    
    def test_ordered_lists(self):
        md = """
1. first item
2. second item
3. third item
4. fourth item
5. last item
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>first item</li><li>second item</li><li>third item</li><li>fourth item</li><li>last item</li></ol></div>"
        )
    
    def test_ordered_list_with_no_space(self):
        md = """
1. first item
2. second item
3.last item
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>1. first item 2. second item 3.last item</p></div>"
        )

if __name__ == "__main__":
    unittest.main()