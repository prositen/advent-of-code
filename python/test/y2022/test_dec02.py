import unittest

from python.src.y2022.dec02 import Dec02, Dec02_2


class TestDec02(unittest.TestCase):
    data = [
        "A Y",
        "B X",
        "C Z"
    ]

    def test_part1_1(self):
        self.assertEqual(15, Dec02(instructions=self.data).part_1())

    def test_part2_1(self):
        self.assertEqual(12, Dec02(instructions=self.data).part_2())

    def test_part1_2(self):
        self.assertEqual(15, Dec02_2(instructions=self.data).part_1())

    def test_part2_2(self):
        self.assertEqual(12, Dec02_2(instructions=self.data).part_2())
