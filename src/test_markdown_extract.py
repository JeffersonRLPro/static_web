import unittest
from extract_markdown import extract_markdown_images, extract_markdown_links

class TestExtractMarkdown(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)")
        
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_link(self):
        matches = extract_markdown_links("This is a link [to boot dev](https://www.boot.dev)")

        self.assertListEqual([("to boot dev", "https://www.boot.dev")], matches)

    def test_extract_markdown_link_with_multiple(self):
        matches = extract_markdown_links("This is a link [to boot dev](https://www.boot.dev) and this is a link [to youtube](https://www.youtube.com/@bootdotdev)")
        
        self.assertListEqual([("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")], matches)

    def test_extract_markdown_images_with_multiple(self):
        matches = extract_markdown_images("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and this is another text with an ![alt text for image](https://i.imgur.com/aKaOqIh.gif)")
        
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png"), ("alt text for image", "https://i.imgur.com/aKaOqIh.gif")], matches)

    def test_images_and_links_no_mixed_in(self):
        matches = extract_markdown_links("This is supposed to be a link, but shows and image instead ![to boot dev](https://www.boot.dev)")

        self.assertListEqual([], matches)

    def test_links_and_images_dont_mix(self):
        matches = extract_markdown_images("This is text with and image, that is actually a link [image](https://i.imgur.com/zjjcJKZ.png)")

        self.assertListEqual([], matches)