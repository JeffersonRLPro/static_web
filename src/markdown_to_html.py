from markdown_to_blocks import markdown_to_blocks
from block_types import BlockType, block_to_block_type
from htmlnode import HTMLNode, LeafNode
from text_to_textnodes import text_to_textnodes
from text_node_to_html import text_node_to_html_node

def markdown_to_html_node(markdown : str) -> HTMLNode:
    """
    markdown_to_html_node creates HTML Nodes by splitting the given markdown string
    
    :param markdown: markdown passed in as a string, This can be a large string
    :type markdown: str
    """
    # split the markdown into blocks
    blocks = markdown_to_blocks(markdown)
    # loop over every block
    for block in blocks:
        # find the block type
        block_type = block_to_block_type(block)
        # create HTML nodes based on what block it is


def _paragraph_block_to_html_node(block : str) -> HTMLNode:
    """
    paragraph_block_to_html_node is a helper method that creates HTML Nodes for markdown blocks 
    that are identified as a "paragraph" block
    """
    # clean the block string to make sure it is all one line
    lines = block.split("\n")
    clean_lines = [line.strip() for line in lines if line.strip() != ""]
    text = "".join(clean_lines)
    # find the children of the overall HTML Node
    children = _text_to_children(text)
    return HTMLNode("p", None, children)

def _heading_block_to_html_node(block : str) -> HTMLNode:
    """
    _heading_block_to_html_node is a helper method that creates HTML Nodes for markdown blocks 
    that are identified as a "heading" block 
    """
    # count the #'s
    count = 1
    for i in range(1, 6):
        if block[i] == "#":
            count =+ 1
        else:
            break
    # find all children for the overall HTMLNode
    children = _text_to_children(block)
    return HTMLNode("h" + count, None, children)

def _quote_block_to_html_node(block : str) -> HTMLNode:
    """
    _quote_block_to_html_node is a helper method that creates HTML Nodes for markdown blocks 
    that are identified as a "quote" block 
    """
    # clean the block string to make sure it is all one line
    if block.startswith("> "):
        stripped = block.strip("> ")
    else:
        stripped = block.strip(">")
    lines = stripped.split("\n")
    clean_lines = [line.strip() for line in lines if line.strip() != ""]
    text = "".join(clean_lines)
    # find all children for the overall HTMLNode
    children = _text_to_children(text)
    return HTMLNode("blockquote", None, children)

def _unordered_list_to_html_node(block : str) -> HTMLNode:
    """
    _unordered_list_to_html_node is a helper method that creates HTML Nodes for markdown blocks 
    that are identified as a "unordered_list" block 
    """ 

def _text_to_children(text : str) -> list[HTMLNode]:
    """
    text_to_children is a helper method to find children nodes of an HTMLNode. 
    It takes a mardown string as input and returns a list of HTML Nodes
    """
    # turn the text into TextNodes
    text_nodes = text_to_textnodes(text)
    # TextNode -> HTMLNodes
    children = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)
    return children