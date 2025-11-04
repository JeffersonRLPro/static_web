from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode

def main():
    test = TextNode("This is a test", TextType.LINK, "https://www.boot.dev")
    print(test)

def text_node_to_html_node(text_node):
    if text_node.text_type == TextType.TEXT:
        return LeafNode(None, text_node.text)
    if text_node.text_type == TextType.BOLD:
        return LeafNode("b", text_node.text)
    if text_node.text_type == TextType.ITALIC:
        return LeafNode("i", text_node.text)
    if text_node.text_type == TextType.CODE:
        return LeafNode("code", text_node.text)
    if text_node.text_type == TextType.LINK:
        if text_node.url == "" or text_node.url is None:
            raise ValueError("Error: The TextType LINK, must have a valid url")
        return LeafNode("a", text_node.text, {"href": text_node.url})
    if text_node.text_type == TextType.IMAGE:
        if text_node.url == "" or text_node.url is None:
            raise ValueError("Error: The TextType IMAGE, must have a url") 
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
    # nothing was found
    raise Exception("Error: text_node.text_type did not match any of the available text_types")

if __name__ == "__main__":
    main()