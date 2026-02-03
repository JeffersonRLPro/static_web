from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(md_block : str):
    # check if varibale is string
    if not isinstance(md_block, str):
        raise TypeError("block type can only be found when the markdown is a string")
    # check for heading
    if md_block.startswith("#"):
        text = md_block.split(" ", 1)
        if len(text) > 1:
            if len(text[0]) <= 6 and len(text[0]) >= 1:
                all_hash = all(c == "#" for c in text[0])
                if all_hash:
                    return BlockType.HEADING
    # check for code block
    if md_block.startswith("```\n") and md_block.endswith("```"):
        return BlockType.CODE
    # split block to check everyline conditions
    lines = md_block.split("\n")
    if lines[0].startswith(">"):
        if len(lines) < 2:
            return BlockType.QUOTE
        for line in lines:
            if not line.startswith(">"):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    if lines[0].startswith("- "):
        if len(lines) < 2:
            return BlockType.UNORDERED_LIST
        for line in lines:
            if not line.startswith("- "):
                return BlockType.PARAGRAPH
        return BlockType.UNORDERED_LIST
    if lines[0].startswith("1. "):
        if len(lines) < 2:
            return BlockType.ORDERED_LIST
        order = 2
        for i in range(1, len(lines)):
            if lines[i] != f"{i}. ":
                return BlockType.PARAGRAPH
            order += 1
        return BlockType.ORDERED_LIST
    # doesn't pass a single case
    return BlockType.PARAGRAPH

    

        

        


