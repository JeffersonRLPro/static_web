from textnode import TextNode, TextType
from split_nodes import split_nodes_delimiter, split_nodes_image, split_nodes_link

def text_to_textnodes(text : str):
    """
    text_to_textnodes takes text as input and returns a list of TextNodes contained with the input string. 
    
    :param text: A string to split into TextNodes
    :type text: str
    """
    if not isinstance(text, str):
        raise TypeError("The text must be a string")
    # split everything
    node = TextNode(text, TextType.TEXT)
    nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    # now do images and links
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes

    