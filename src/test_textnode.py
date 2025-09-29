import unittest
from textnode import TextNode, TextType, text_node_to_html_node



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
        node2 = TextNode("This is a text node", TextType.TEXT, None)
        self.assertNotEqual(node, node2)
    def test_text(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        node2 = TextNode("This is another text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    #text_to_html
    def test_image(self):
        node = TextNode("alt text", TextType.IMAGE, "https://bootleg.com/img")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.props["alt"], "alt text")
        self.assertEqual(html_node.props["src"], "https://bootleg.com/img")
        self.assertEqual(html_node.tag, "img")
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
    def test_link(self):
        node = TextNode("Harmless link", TextType.LINK, "https://bootleg.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.props["href"], "https://bootleg.com")
        self.assertEqual(html_node.tag, "a")


if __name__ == "__main__":
    unittest.main()