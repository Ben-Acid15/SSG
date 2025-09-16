from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        ident = "second_node_tt"
        count = 0
        dev = float
        if node[0] == delimiter:
            ident = "start_with_tt"
        node_parts = node.split(delimiter)
        for part in node_parts:
            if ident == "start _with_tt":
                dev = int
            if count / 2 == dev:
                tt = text_type
            else:
                tt = "plain"
            text_node = TextNode(part, tt)
            new_nodes.append(text_node)
            count += 1
