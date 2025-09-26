from enum import Enum
import re
from htmlnode import HTMLNode

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

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    striped_blocks = []
    for block in blocks:
        striped_block = block.strip()
        if block == "":
            blocks.pop(block)
        striped_blocks.append(striped_block)
    return striped_blocks

def header_level(header):
    level = re.findall(r"#{6} \w{6}", header)
    if len(level) > 0:
        return HTMLNode("h6", header)
    level = re.findall(r"#{5} \w{5}", header)
    if len(level) > 0:
        return HTMLNode("h5", header)
    level = re.findall(r"#{4} \w{4}", header)
    if len(level) > 0:
        return HTMLNode("h4", header)
    level = re.findall(r"#{3} \w{3}", header)
    if len(level) > 0:
        return HTMLNode("h3", header)
    level = re.findall(r"#{2} \w{2}", header)
    if len(level) > 0:
        return HTMLNode("h2", header)
    level = re.findall(r"#{1} \w{1}", header)
    if len(level) > 0:
        return HTMLNode("h1", header)
    raise Exception(f"Input {header} is not a header.")

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        block_type = block_to_blocktype(block)
        match block_type:
            case BlockType.PARAGRAPH:
                html_node = HTMLNode("p", block)
            case BlockType.HEADING:
                html_node = header_level(block) 
            case BlockType.CODE:
                html_node = HTMLNode("code", block)
            case BlockType.QUOTE:
                html_node = HTMLNode("q", block)
            case BlockType.UNORDERED_LIST:
                html_node = HTMLNode("ul", block)
            case BlockType.ORDERED_LIST:
                html_node = HTMLNode("ol", block)
            case _:
                raise Exception(f"No valid Blocktype in provided block: {block}")
        