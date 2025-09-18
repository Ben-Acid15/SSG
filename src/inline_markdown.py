from textnode import TextNode, TextType
import re

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

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:    
        #Extracts images
        matches = extract_markdown_images(node.text)
        if len(matches) == 0:
                new_nodes.append(node)
        else:
            image_nodes = []
            #Funal matches into TextNodes
            for i in range(0, len(matches), 2):
                image_node = TextNode(matches[i], "image", matches[i + 1])
                alt = matches[i]
                url = matches[i + 1]
                new_nodes.append(image_node)
                image_nodes.append(node.split(f"![{alt}]({url})"))
            #Get nodes in order
            first_iteration = True
            for image in image_nodes:
                plain_texts = []
                if first_iteration == True:
                    plain_texts = node.text.split(f"![{alt}]({url})", 1)
                else:
                    plain_texts = plain_texts[1].split(f"![{alt}]({url})", 1)
                textnode = TextNode(plain_texts[0], "plain")
                new_nodes.append(textnode)
                image_node = TextNode(image, "image",)
                new_nodes.append(image_node)
                textnode = TextNode(plain_texts[1], "plain")
                new_nodes.append(textnode)
                first_iteration = False
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:    
        #Extracts images
        matches = extract_markdown_links(node.text)
        if len(matches) == 0:
                new_nodes.append(node)
        else:
            link_nodes = []
            #Funal matches into TextNodes
            for i in range(0, len(matches), 2):
                link_node = TextNode(matches[i], "image", matches[i + 1])
                alt = matches[i]
                url = matches[i + 1]
                new_nodes.append(link_node)
                link_nodes.append(node.split(f"![{alt}]({url})"))
            #Get nodes in order
            first_iteration = True
            for link in link_nodes:
                plain_texts = []
                if first_iteration == True:
                    plain_texts = node.text.split(f"![{alt}]({url})", 1)
                else:
                    plain_texts = plain_texts[1].split(f"![{alt}]({url})", 1)
                textnode = TextNode(plain_texts[0], "plain")
                new_nodes.append(textnode)
                link_node = TextNode(link, "image",)
                new_nodes.append(link_node)
                textnode = TextNode(plain_texts[1], "plain")
                new_nodes.append(textnode)
                first_iteration = False
    return new_nodes

def extract_markdown_images(text):
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches

def extract_markdown_links(text):
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches
    