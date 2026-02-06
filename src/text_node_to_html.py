from textnode import TextType, TextNode
from htmlnode import LeafNode

def text_node_to_html_node(text_node : TextNode):
    """
    text_node_to_html_node takes a text_node as input and returns a corresponding leaf node
    based on what TextType the text_node is
    
    :param text_node: A TextNode Class object
    """
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