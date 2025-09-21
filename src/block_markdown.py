def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    for block in blocks:
        striped_block = block.strip()
        if block == "":
            blocks.pop(block)
    
    

    return blocks