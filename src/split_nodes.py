from textnode import TextType, TextNode
from extract_markdown import extract_markdown_images, extract_markdown_links

# This function is to split text nodes and handle many different text
# types in a single sentence
# NOTE: This only handles inline styles like bold, italic, and code
def split_nodes_delimiter(old_nodes : list[TextNode], delimiter : str, text_type) -> list[TextNode]:
    """
    split_nodes_delimiter is to split text nodes and handle many different text types in a single sentence. it returns a list of TextNodes
    NOTE: This only handles inline styles like bold, italic, and code
    
    :param old_nodes: a list of TextNodes to split into more TextNodes, depending on the text_type
    :type old_nodes: list[TextNode]
    :param delimiter: a delimeter used to split the text within a TextNode please use the following(`, _, **)
    :type delimiter: str
    :param text_type: The TextType of the new nodes
    """
    if not isinstance(old_nodes, list):
        raise TypeError("old_nodes must be a list of TextNodes objects")
    new_nodes = []
    for node in old_nodes:
        if not isinstance(node, TextNode):
            raise TypeError("all items in old_nodes must be a TextNode object")
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        # check if there is a matching delimiter
        elif delimiter not in node.text:
            new_nodes.append(node) 
        else:     
            parts = node.text.split(delimiter)
            if len(parts) % 2 == 0:
                raise Exception("Invalid Markdown syntax")
            node_list =[]
            for i in range(len(parts)):
                if i % 2 == 0:
                    # make a new textNode with a simple text TextType, but first make sure that it is not empty text
                    if parts[i]:
                        node_list.append(TextNode(parts[i], TextType.TEXT))
                if i % 2 == 1:
                    node_list.append(TextNode(parts[i], text_type))
            if len(node_list) != 0:
                new_nodes.extend(node_list)
    return new_nodes
    
# the following functions, like the one above, splits textnodes that have images and links
# NOTE: This function only splits links and images, not bold, italics, etc.
def split_nodes_image(old_nodes : list[TextNode]) -> list[TextNode]:
    """
    split_nodes_image splits TextNodes to create TextNodes with an IMAGE TextType. Returns a list of TextNodes
    NOTE: This function only splits images, not bold, italics, etc.
    
    :param old_nodes: A list of TextNodes
    :type old_nodes: list[TextNode]
    """
    if not isinstance(old_nodes, list):
        raise TypeError("old_nodes must be a list of TextNodes objects")
    new_nodes = []
    for node in old_nodes:
        if not isinstance(node, TextNode):
            raise TypeError("all items in old_nodes must be a TextNode object")
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            matches = extract_markdown_images(node.text)
            if matches:
                inner_nodes = []
                current_text = node.text
                for image_alt, image_url in matches:
                    parts = current_text.split(f"![{image_alt}]({image_url})", 1)
                    if len(parts) != 2:
                        raise ValueError("invalid markdown, link section not closed")
                    if parts[0]:
                        inner_nodes.append(TextNode(parts[0], TextType.TEXT))
                    inner_nodes.append(TextNode(image_alt, TextType.IMAGE, image_url))
                    current_text = parts[1]
                # This will add the leftover of the "parts" list after the loop executes, this will always be a text type.
                if current_text != "":
                    inner_nodes.append(TextNode(current_text, TextType.TEXT))
                new_nodes.extend(inner_nodes)
            # there were no matches
            else:
                new_nodes.append(node)
    return new_nodes

def split_nodes_link(old_nodes : list[TextNode]) -> list[TextNode]:
    """
    split_nodes_link splits TextNodes to create TextNodes with a LINK TextType. Returns a list of TextNodes
    NOTE: This function only splits links, not bold, italics, etc.
    
    :param old_nodes: A list of TextNodes
    :type old_nodes: list[TextNode]
    """
    if not isinstance(old_nodes, list):
        raise TypeError("old_nodes must be a list of TextNodes objects")
    new_nodes = []
    for node in old_nodes:
        if not isinstance(node, TextNode):
            raise TypeError("all items in old_nodes must be a TextNode object")
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            matches = extract_markdown_links(node.text)
            if matches:
                inner_nodes = []
                current_text = node.text
                for link_alt, link_url in matches:
                    parts = current_text.split(f"[{link_alt}]({link_url})", 1)
                    if len(parts) != 2:
                        raise ValueError("invalid markdown, link section not closed")
                    if parts[0]:
                        inner_nodes.append(TextNode(parts[0], TextType.TEXT))
                    inner_nodes.append(TextNode(link_alt, TextType.LINK, link_url))
                    current_text = parts[1]
                if current_text != "":
                    inner_nodes.append(TextNode(current_text, TextType.TEXT))
                new_nodes.extend(inner_nodes)
            else:
                new_nodes.append(node)
    return new_nodes
            