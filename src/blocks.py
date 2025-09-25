from enum import Enum
import re

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_blocktype(block):
    headings = re.findall(r"#+ \w+", block)
    if len(headings) > 0:
        return BlockType.HEADING
    code = re.findall(r"`{3}", block)
    if len(code) > 1:
        return BlockType.CODE
    quotes = re.findall(r"^>\w+", block)
    if len(quotes) > 0:
        return BlockType.QUOTE
    uo_lists = re.findall(r"^- ", block)
    if len(uo_lists) > 0:
        return BlockType.UNORDERED_LIST
    o_lists = re.findall(r"^\d{1}.", block)
    if len(o_lists) > 0:
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH