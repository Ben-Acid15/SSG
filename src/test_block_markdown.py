import unittest
from textnode import TextNode, TextType
from block_markdown import *

class TestBlockMarkdown(unittest.TestCase):
    def test_block_split(self):
        doc = "What is this?\n\nIs this a paragraph?\n\n- I think\n- It is"
        split = markdown_to_blocks(doc)
        self.assertEqual(["What is this?", "Is this a paragraph?", "- I think\n- It is"], split)

    def test_block_split_longer_list(self):
        doc = "What is this?\n\nIs this a paragraph?\n\n- I think\n- It really\n- Is"
        split = markdown_to_blocks(doc)
        print(f"{split}")
        self.assertEqual(["What is this?", "Is this a paragraph?", "- I think\n- It really\n- Is"], split)





if __name__ == "__main__":
    unittest.main()