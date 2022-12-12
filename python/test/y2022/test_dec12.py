import unittest

from python.src.y2022.dec12 import Dec12


class TestDec12(unittest.TestCase):
    data = [
        "Sabqponm",
        "abcryxxl",
        "accszExk",
        "acctuvwj",
        "abdefghi"
    ]

    def test_part_1(self):
        self.assertEqual(31, Dec12(instructions=self.data).part_1())

    def test_part_2(self):
        self.assertEqual(29, Dec12(instructions=self.data).part_2())
