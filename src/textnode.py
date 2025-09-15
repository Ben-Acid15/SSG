from enum import Enum
from htmlnode import LeafNode

class TextType(Enum):
    PLAIN = "plain"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
    def __eq__(self, node2):
        if self.text == node2.text and self.text_type == node2.text_type and self.url == node2.url:
            return True
        else:
            return False
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
    def text_node_to_html_node(self):
        match self.text_type:
            case "plain":
                return LeafNode(None, self.text, None)
            case "bold":
                return LeafNode("b", self.text, None)
            case "italic":
                return LeafNode("i", self.text, None)
            case "code":
                return LeafNode("code", self.text, None)
            case "link":
                return LeafNode("a", self.text, props={"href": self.url})
            case "image":
                return LeafNode("img", "", props={"src": self.url,"alt": self.text})
            case _:
                raise Exception("No valid TextType in provided node")