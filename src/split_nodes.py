from textnode import TextType, TextNode

# This function is to split text nodes and handle many different text
# types in a single sentence
# NOTE: This only handles inline styles like bold, italic, and code
def split_nodes_delimiter(old_nodes : list[TextNode], delimiter : str, text_type):
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
                    # make a new textNode with a simple text TextType
                    node_list.append(TextNode(parts[i], TextType.TEXT))
                if i % 2 == 1:
                    node_list.append(TextNode(parts[i], text_type))
            if len(node_list) != 0:
                new_nodes.extend(node_list)
    return new_nodes
    

