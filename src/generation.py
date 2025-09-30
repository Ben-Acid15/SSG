import os
import stat
import pathlib
from pathlib import Path

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

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)
    content_items = os.listdir(dir_path_content)
    for item in content_items:
        item_path = pathlib.Path(item)
        item_path_full = os.path.join(dir_path_content, item_path)
        if Path(item_path_full).suffix == ".md":
            dest_item = item.replace(".md", ".html")
            dest_path_item = os.path.join(dest_dir_path, dest_item)
            generate_page(item_path_full, template_path, dest_path_item)
        elif os.path.isdir(item_path_full):
            dest_path_sub = os.path.join(dest_dir_path, item_path)
            if not os.path.exists(dest_path_sub):
                os.mkdir(dest_path_sub)
            generate_pages_recursive(item_path_full, template_path, dest_path_sub)