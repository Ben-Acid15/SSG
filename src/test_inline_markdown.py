import unittest
from textnode import TextNode, TextType
from inline_markdown import *

#split nodes
def test_split_nodes_italic(self):
        old_nodes = [TextNode("The plain text and _the italic text_", "plain"),
                     TextNode("_The italic text and_ the plain text", "plain")]
        new_nodes = split_nodes_delimiter(old_nodes, "_", "italic")
        self.assertEqual(new_nodes, [TextNode("The plain text and", "plain"),
                                     TextNode("the italic text", "italic"),
                                     TextNode("The italic text and", "italic"),
                                     TextNode("the plain text"), "plain"])
def test_split_nodes_bold(self):
    old_nodes = [TextNode("The plain text and _the bold text_", "plain"),
                TextNode("_The bold text and_ the plain text", "plain")]
    new_nodes = split_nodes_delimiter(old_nodes, "_", "bold")
    self.assertEqual(new_nodes, [TextNode("The plain text and", "plain"),
                                TextNode("the bold text", "bold"),
                                TextNode("The bold text and", "bold"),
                                TextNode("the plain text"), "plain"])
def test_split_nodes_code(self):
    old_nodes = [TextNode("The plain text and _the code text_", "plain"),
                TextNode("_The code text and_ the plain text", "plain")]
    new_nodes = split_nodes_delimiter(old_nodes, "_", "code")
    self.assertEqual(new_nodes, [TextNode("The plain text and", "plain"),
                                TextNode("the code text", "code"),
                                TextNode("The code text and", "code"),
                                TextNode("the plain text"), "plain"])
    
#text_extract
def test_extract_markdown_image(self):
    matches = extract_markdown_images(
        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
    )
    self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)
def test_extract_markdown_images(self):
    matches = extract_markdown_images(
          "Damn, now there isn't just one ![image](https://sketchy_stuff.com/png.png) in here, but even two ![images](https://sketchy_stuff.com/scam.png)!"
    )
    self.assertListEqual([("image", "https://sketchy_stuff.com/png.png"), ("images", "https://sketchy_stuff.com/scam.png")], matches)
def test_extract_markdown_link(self):
    matches = extract_markdown_links("There is a [link](https://sketchy_stuff.com) in here somewhere...")
    self.assertListEqual([("link", "https://sketchy_stuff.com")], matches)
def test_extract_markdown_links(self):
    matches = extract_markdown_links("There are some [mines](httsp://bang.com) in this [mine](https://boom.com)-field.")
    self.assertListEqual([("mines", "https://bang.com"), ("mine", "https://boom.com")], matches)

if __name__ == "__main__":
    unittest.main()