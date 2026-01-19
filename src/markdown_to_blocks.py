def markdown_to_blocks(markdown : str):
    if not isinstance(markdown, str):
        raise TypeError("markdown_to_blocks must be passed a string.")
    blocks = markdown.split("\n\n")
    new_blocks = []
    for block in blocks:
        if block.strip():
            block = block.strip()
            new_blocks.append(block)
    return new_blocks