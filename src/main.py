from textnode import *

print("hello world")

def main(text, text_type, url):
    new_node = TextNode(text, text_type, url)
    print(f"{new_node}")


main("Anchor", TextType.LINK.value, "http://boot.com")