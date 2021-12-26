import unittest

from python.src.y2021.dec25 import Dec25


class TestDec125(unittest.TestCase):

    def test_small_map(self):
        data = [
            "v...>>.vv>",
            ".vv>>.vv..",
            ">>.>v>...v",
            ">>v>>.>.v.",
            "v>v.vv.v..",
            ">.>>..v...",
            ".vv..>.>v.",
            "v.v..>>v.v",
            "....v..v.>"]

        self.assertEqual(58, Dec25(instructions=data).part_1())
