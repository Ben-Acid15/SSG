import unittest
from htmlnode import HTMLNode


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


if __name__ == "__main__":
    unittest.main()