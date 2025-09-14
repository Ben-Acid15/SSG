import unittest
from htmlnode import HTMLNode, LeadNode


class TestHTMLNode(unittest.Testcase):
    def test_empty(self):
        node = HTMLNode("p", "A paragraph", None, None)
        print(f"{self.props_to_html()}")
    def test_one_prop(self):
        node = HTMLNode("link", "A picture", None, props={"href": "https://picture"})
        print(f"{self.props_to_html()}")
    def test_two_props(self):
        node = HTMLNode("h2", "A subtitle", None, props={"href": "https://picture2", "target": "__blank"})
        print(f"{self.props_to_html()}")

    def test_to_html_para(self):
        node = HTMLNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    def test_to_html_tagless(self):
        node = HTMLNode(None, "Just print me")
        self.assertEqual(node.to_html(), "Just print me")
    def test_to_html_error(self):
        node = HTMLNode("p", None)
        self.assertNotEqual(node.to_html(), "<p></p>")


if __name__ == "__main__":
    unittest.main()