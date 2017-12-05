import unittest

from python.src.y2017 import dec05

class TestDec05(unittest.TestCase):
    def test_jump_offsets(self):
        offsets = [0, 3, 0, 1, -3]

        self.assertEqual(5, dec05.jump_offsets(offsets))
        self.assertEqual(10, dec05.jump_offsets(offsets, strange_jumps=True))