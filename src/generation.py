import os
import stat

from block_markdown import markdown_to_html_node
from htmlnode import HTMLNode, LeafNode, ParentNode
from block_markdown import extract_header


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path) as file:
        source_content = file.read()
    with open(template_path) as template:
        template_content = template.read()
    html_node = markdown_to_html_node(source_content)
    html_string = html_node.to_html()
    title = extract_header(source_content)
    template_content = template_content.replace("{{ Title }}", title)
    template_content = template_content.replace("{{ Content }}", html_string)
    with open(dest_path, "w") as file:
        file.write(template_content)
