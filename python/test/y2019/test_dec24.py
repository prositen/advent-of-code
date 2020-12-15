import unittest

from python.src.y2019.dec24 import Dec24


class TestDec24(unittest.TestCase):

    def test_first_repeat(self):
        layout = ["....#",
                  "#..#.",
                  "#..##",
                  "..#..",
                  "#...."]
        self.assertEqual(2129920,
                         Dec24(instructions=layout).part_1())

    def test_biodiversity(self):
        layout = [".....",
                  ".....",
                  ".....",
                  "#....",
                  ".#..."]

        self.assertEqual(2129920,
                         Dec24(instructions=layout).get_biodiversity())

    def test_run_recursive(self):
        layout = ["....#",
                  "#..#.",
                  "#..##",
                  "..#..",
                  "#...."]

        self.assertEqual(99,
                         Dec24(instructions=layout).run(10))
