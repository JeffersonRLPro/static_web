def markdown_to_blocks(markdown : str):
    """
    markdown_to_blocks is a function that splits a markdown string into multiple blocks. The blocks are identified
    by double newlines. The function return a list of blocks
    
    :param markdown: markdown string
    :type markdown: str
    """
    if not isinstance(markdown, str):
        raise TypeError("markdown_to_blocks must be passed a string.")
    blocks = markdown.split("\n\n")
    new_blocks = []
    for block in blocks:
        if block.strip():
            block = block.strip()
            new_blocks.append(block)
    return new_blocks