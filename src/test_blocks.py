import unittest
from blocks import *

class TestBlock(unittest.TestCase):
    def test_block_p(self):
        block = "Just some simple text."
        Type = block_to_blocktype(block)
        self.assertEqual(BlockType.PARAGRAPH, Type)
    def test_block_h(self):
        block = "### We got a header here"
        Type = block_to_blocktype(block)
        self.assertEqual(BlockType.HEADING, Type)
    def test_block_c(self):                                 #Failed
        block = "```Also some code```"
        Type = block_to_blocktype(block)
        self.assertEqual(BlockType.CODE, Type)
    def test_block_q(self):
        block = ">I bet someone once said this"
        Type = block_to_blocktype(block)
        self.assertEqual(BlockType.QUOTE, Type)
    def test_block_uol(self):                               #Failed
        block = "- Point no 1 \n- point no 2"
        Type = block_to_blocktype(block)
        self.assertEqual(BlockType.UNORDERED_LIST, Type)
    def test_block_ol(self):
        block = "1. Once again, point 1 \n2. And point 2"
        Type = block_to_blocktype(block)
        self.assertEqual(BlockType.ORDERED_LIST, Type)