import unittest

from python.src.y2021.dec02 import Dec02


class TestDec02(unittest.TestCase):
    data = [
        "forward 5",
        "down 5   ",
        "forward 8",
        "up 3     ",
        "down 8   ",
        "forward 2"
    ]

    def test_part_1(self):
        self.assertEqual(150, Dec02(instructions=self.data).part_1())

    def test_part_2(self):
        self.assertEqual(900, Dec02(instructions=self.data).part_2())
