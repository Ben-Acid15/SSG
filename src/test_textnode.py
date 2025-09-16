import unittest
from textnode import TextNode, TextType
from split_nodes_delimiter import *



class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    def test_dif(self):
        node = TextNode("This is a text node", TextType.ITALIC, None)
        node2 = TextNode("This is a text node", TextType.BOLD, None)
        self.assertNotEqual(node, node2)
    def test_url(self):
        node = TextNode("This is a text node", TextType.ITALIC, "https://boot.dev")
        node2 = TextNode("This is a text node", TextType.ITALIC, None)
        self.assertNotEqual(node, node2)
    def test_type(self):
        node = TextNode("This is a text node", TextType.ITALIC, None)
        node2 = TextNode("This is a text node", TextType.PLAIN, None)
        self.assertNotEqual(node, node2)
    def test_text(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        node2 = TextNode("This is another text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    #text_to_html
    def test_image(self):
        node = TextNode("alt text", "image", "https://bootleg.com/img")
        html_node = node.text_node_to_html_node()
        self.assertEqual(html_node.props["alt"], "alt text")
        self.assertEqual(html_node.props["src"], "https://bootleg.com/img")
        self.assertEqual(html_node.tag, "img")
    def test_text(self):
        node = TextNode("This is a text node", "plain")
        html_node = node.text_node_to_html_node()
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
    def test_link(self):
        node = TextNode("Harmless link", "link", "https://bootleg.com")
        html_node = node.text_node_to_html_node()
        self.assertEqual(html_node.props["href"], "https://bootleg.com")
        self.assertEqual(html_node.tag, "a")
    
    #text to nodes
    def text_to_nodes_italic(self):
        old_nodes = [TextNode("The plain text and _the italic text_", "plain"),
                     TextNode("_The italic text and_ the plain text", "plain")]
        new_nodes = split_nodes_delimiter(old_nodes, "_", "italic")
        self.assertEqual(new_nodes, [TextNode("The plain text and", "plain"),
                                     TextNode("the italic text", "italic"),
                                     TextNode("The italic text and", "italic"),
                                     TextNode("the plain text"), "plain"])
    def text_to_nodes_bold(self):
        old_nodes = [TextNode("The plain text and _the bold text_", "plain"),
                    TextNode("_The bold text and_ the plain text", "plain")]
        new_nodes = split_nodes_delimiter(old_nodes, "_", "bold")
        self.assertEqual(new_nodes, [TextNode("The plain text and", "plain"),
                                    TextNode("the bold text", "bold"),
                                    TextNode("The bold text and", "bold"),
                                    TextNode("the plain text"), "plain"])
    def text_to_nodes_code(self):
        old_nodes = [TextNode("The plain text and _the code text_", "plain"),
                    TextNode("_The code text and_ the plain text", "plain")]
        new_nodes = split_nodes_delimiter(old_nodes, "_", "code")
        self.assertEqual(new_nodes, [TextNode("The plain text and", "plain"),
                                    TextNode("the code text", "code"),
                                    TextNode("The code text and", "code"),
                                    TextNode("the plain text"), "plain"])


if __name__ == "__main__":
    unittest.main()