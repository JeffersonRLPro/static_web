import re
from markdown_to_blocks import markdown_to_blocks
from block_types import BlockType, block_to_block_type
from htmlnode import HTMLNode, ParentNode
from text_to_textnodes import text_to_textnodes
from text_node_to_html import text_node_to_html_node
from textnode import TextNode, TextType


def markdown_to_html_node(markdown : str) -> HTMLNode:
    """
    markdown_to_html_node creates HTML Nodes by splitting the given markdown string
    
    :param markdown: markdown passed in as a string, This can be a large string
    :type markdown: str
    """
    # split the markdown into blocks
    blocks = markdown_to_blocks(markdown)
    # loop over every block
    html_nodes = []
    for block in blocks:
        # find the block type
        block_type = block_to_block_type(block)
        # create HTML nodes based on what block it is
        if block_type == BlockType.PARAGRAPH:
            node = _paragraph_block_to_html_node(block)
        elif block_type == BlockType.CODE:
            node = _code_to_html(block)
        elif block_type == BlockType.HEADING:
            node = _heading_block_to_html_node(block)
        elif block_type == BlockType.QUOTE:
            node = _quote_block_to_html_node(block)
        elif block_type == BlockType.UNORDERED_LIST:
            node = _unordered_list_to_html_node(block)
        elif block_type == BlockType.ORDERED_LIST:
            node = _ordered_lists_html_node(block)
        else:
            raise ValueError(f"Invalid BlockType: {block_type}")
        html_nodes.append(node)
    return ParentNode("div", html_nodes)



def _paragraph_block_to_html_node(block : str) -> HTMLNode:
    """
    paragraph_block_to_html_node is a helper method that creates HTML Nodes for markdown blocks 
    that are identified as a "paragraph" block
    """
    # clean the block string to make sure it is all one line
    lines = block.split("\n")
    clean_lines = [line.strip() for line in lines if line.strip() != ""]
    text = " ".join(clean_lines)
    # find the children of the overall HTML Node
    children = _text_to_children(text)
    return ParentNode("p", children)

def _heading_block_to_html_node(block : str) -> HTMLNode:
    """
    _heading_block_to_html_node is a helper method that creates HTML Nodes for markdown blocks 
    that are identified as a "heading" block 
    """
    # count the #'s
    count = 1
    for i in range(1, 6):
        if block[i] == "#":
            count += 1
        else:
            break
    # strip the #'s
    clean_block = block[count + 1:] # 1 for the space between the #'s and the actual heading
    # find all children for the overall HTMLNode
    children = _text_to_children(clean_block)
    return ParentNode(f"h{count}", children)

def _quote_block_to_html_node(block : str) -> HTMLNode:
    """
    _quote_block_to_html_node is a helper method that creates HTML Nodes for markdown blocks 
    that are identified as a "quote" block 
    """
    # clean the block string to make sure it is all one line
    lines = block.split("\n")
    clean_lines = []
    for line in lines:
        if line.startswith("> "):
            clean_lines.append(line[2:].strip())
        elif line.startswith(">"):
            clean_lines.append(line[1:].strip())
        else:
            continue
    text = " ".join(clean_lines)
    # find all children for the overall HTMLNode
    children = _text_to_children(text)
    return ParentNode("blockquote", children)

def _unordered_list_to_html_node(block : str) -> HTMLNode:
    """
    _unordered_list_to_html_node is a helper method that creates HTML Nodes for markdown blocks 
    that are identified as a "unordered_list" block 
    """ 
    # clean the block
    clean_block = block.split("\n")
    parent_nodes = []
    for line in clean_block:
        if line.startswith("- "):
            line = line[2:].strip()
            # get the inline markdown (children) of the element in unordered list 
            children = _text_to_children(line)
            parent_nodes.append(ParentNode("li", children))
        else:
            continue
    return ParentNode("ul", parent_nodes)

def _ordered_lists_html_node(block : str) -> HTMLNode:
    """
    _ordered_lists_html_node is a helper method that creates HTML Nodes for markdown blocks 
    that are identified as a "ordered_list" block 
    """
    clean_block = block.split("\n")
    parent_nodes = []
    for line in clean_block:
        if re.match(r"(\d*\.\ )", line):
            line = line[3:].strip()
            children = _text_to_children(line)
            parent_nodes.append(ParentNode("li", children))
        else:
            continue
    return ParentNode("ol", parent_nodes)

def _code_to_html(block : str) -> HTMLNode:
    """
    _code_to_html is a helper method that creates HTML Nodes for markdown blocks 
    that are identified as a "code" block
    """
    clean_block = block.split("\n")
    clean_block = [line for line in clean_block if line.strip("```") != ""]
    text = "\n".join(clean_block) + "\n"
    # manually create a textNode
    node = TextNode(text, TextType.CODE)
    leaf_node = text_node_to_html_node(node)
    return ParentNode("pre", [leaf_node])

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