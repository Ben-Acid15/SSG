from textnode import *
from data_management import copy_and_migrate
import pathlib

print("hello world")

def main(text, text_type, url):
    new_node = TextNode(text, text_type, url)
    print(f"{new_node}")
    copy_and_migrate(pathlib.Path("./static"), pathlib.Path("./public"))


main("Anchor", TextType.LINK.value, "http://boot.com")