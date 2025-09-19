import unittest
from textnode import TextNode, TextType
from inline_markdown import *

#split nodes
def test_split_nodes_italic(self):
        old_nodes = [TextNode("The plain text and _the italic text_", TextType.TEXT),
                     TextNode("_The italic text and_ the plain text", TextType.TEXT)]
        new_nodes = split_nodes_delimiter(old_nodes, "_", TextType.ITALIC)
        self.assertEqual(new_nodes, [TextNode("The plain text and", TextType.TEXT),
                                     TextNode("the italic text", TextType.ITALIC),
                                     TextNode("The italic text and", TextType.ITALIC),
                                     TextNode("the plain text"), TextType.TEXT])
def test_split_nodes_bold(self):
    old_nodes = [TextNode("The plain text and _the bold text_", TextType.TEXT),
                TextNode("_The bold text and_ the plain text", TextType.TEXT)]
    new_nodes = split_nodes_delimiter(old_nodes, "_", TextType.BOLD)
    self.assertEqual(new_nodes, [TextNode("The plain text and", TextType.TEXT),
                                TextNode("the bold text", TextType.BOLD),
                                TextNode("The bold text and", TextType.BOLD),
                                TextNode("the plain text"), TextType.TEXT])
def test_split_nodes_code(self):
    old_nodes = [TextNode("The plain text and _the code text_", TextType.TEXT),
                TextNode("_The code text and_ the plain text", TextType.TEXT)]
    new_nodes = split_nodes_delimiter(old_nodes, "_", "code")
    self.assertEqual(new_nodes, [TextNode("The plain text and", TextType.TEXT),
                                TextNode("the code text", "code"),
                                TextNode("The code text and", "code"),
                                TextNode("the plain text"), TextType.TEXT])
    
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

#split_images
def test_split_images(self):
    node = TextNode(
        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
        TextType.TEXT,
    )
    new_nodes = split_nodes_image([node])
    self.assertListEqual(
        [
            TextNode("This is text with an ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and another ", TextType.TEXT),
            TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png")], new_nodes)
def test_split_images_start(self):
    node = TextNode(
        "![Image](https://i.imgur.com/zjjcJKZ.png) right at the start and another ![second image](https://i.imgur.com/3elNhQu.png) later!",
        TextType.TEXT,
    )
    new_nodes = split_nodes_image([node])
    self.assertListEqual(
        [
            TextNode("Image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" right at the start and another ", TextType.TEXT),
            TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png")],
            TextNode(" later!", TextType.TEXT), new_nodes)

#split_links
def test_split_links(self):
    node = TextNode(
        "[Links](https://i.imgur.com) right at the start? Crazy...",
        TextType.TEXT,
    )
    new_nodes = split_nodes_link([node])
    self.assertListEqual(
        [
            TextNode("Links", TextType.LINK, "https://i.imgur.com"),
            TextNode(" right at the start? Crazy...", TextType.TEXT)], new_nodes)

#text_to_textnode
def test_text_node(self):
    text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
    new_nodes = text_to_textnodes(text)
    self.assertListEqual(
        [
    TextNode("This is ", TextType.TEXT),
    TextNode("text", TextType.BOLD),
    TextNode(" with an ", TextType.TEXT),
    TextNode("italic", TextType.ITALIC),
    TextNode(" word and a ", TextType.TEXT),
    TextNode("code block", TextType.CODE),
    TextNode(" and an ", TextType.TEXT),
    TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
    TextNode(" and a ", TextType.TEXT),
    TextNode("link", TextType.LINK, "https://boot.dev")
    ], new_nodes
    )


if __name__ == "__main__":
    unittest.main()