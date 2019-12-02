import unittest
from python.src.y2017 import dec19


class TestRouting(unittest.TestCase):
    def test_routing(self):
        puzzle_input = [
            "     |          ",
            "     |  +--+    ",
            "     A  |  C    ",
            " F---|----E|--+ ",
            "     |  |  |  D ",
            "     +B-+  +--+ "
        ]
        r = dec19.Routing(puzzle_input)
        self.assertEqual('ABCDEF', r.part_1())
        self.assertEqual(38, r.part_2())
