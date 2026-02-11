import unittest
from generate_site import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_title_extraction(self):
        md = """
# This is the title
"""
        result = extract_title(md)
        self.assertEqual(result, "This is the title")
    
    def test_no_title(self):
        with self.assertRaises(Exception):
            extract_title("## there is no title here")
    
    def test_no_title_multiple(self):
        md = """
## no title
## not here 
###### not here
### not here either
### not here
"""
        with self.assertRaises(Exception):
            extract_title(md)
    
    def test_title_in_middle(self):
        md = """
## no title
## not here 
# here
### not here either
### not here
"""
        result = extract_title(md)
        self.assertEqual(result, "here")

    def test_title_multiple(self):
        md = """
## no title
## not here 
# here
### not here either
# here but shouldn't count
"""
        result = extract_title(md)
        self.assertEqual(result, "here")