import unittest

from python.src.y2021.dec05 import Dec05


class TestDec04(unittest.TestCase):
    data = [
        "0,9 -> 5,9",
        "8,0 -> 0,8",
        "9,4 -> 3,4",
        "2,2 -> 2,1",
        "7,0 -> 7,4",
        "6,4 -> 2,0",
        "0,9 -> 2,9",
        "3,4 -> 1,4",
        "0,0 -> 8,8",
        "5,5 -> 8,2"
    ]

    def test_overlap(self):
        self.assertEqual(5, Dec05(instructions=self.data).part_1())

    def test_overlap_with_diagonals(self):
        self.assertEqual(12, Dec05(instructions=self.data).part_2())
