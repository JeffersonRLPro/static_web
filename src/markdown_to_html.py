from markdown_to_blocks import markdown_to_blocks
from block_types import BlockType, block_to_block_type
from htmlnode import HTMLNode

def markdown_to_html_node(markdown : str):
    """
    markdown_to_html_node creates HTML Nodes by splitting the given markdown string
    
    :param markdown: 
    :type markdown: str
    """
    # split the markdown into blocks
    blocks = markdown_to_blocks(markdown)
    # loop over every block
    for block in blocks:
        # find the block type
        block_type = block_to_block_type(block)
        # create HTML nodes based on what block it is


def paragraph_block_to_html_node(block : str):
    """
    paragraph_block_to_html_node is a helper method that creates HTML Nodes for markdown blocks 
    that are identified as a "paragraph" block
    
    :param block: A markdown block that will be made into a HTML Node
    :type markdown: str
    """