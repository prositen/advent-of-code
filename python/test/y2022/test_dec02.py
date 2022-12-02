import unittest

from python.src.y2022.dec02 import Dec02


class TestDec02(unittest.TestCase):
    data = [
        "A Y",
        "B X",
        "C Z"
    ]

    def test_part1(self):
        self.assertEqual(15, Dec02(instructions=self.data).part_1())

    def test_part2(self):
        self.assertEqual(12, Dec02(instructions=self.data).part_2())
