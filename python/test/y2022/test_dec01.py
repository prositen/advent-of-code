import unittest

from python.src.y2022.dec01 import Dec01


class TestDec01(unittest.TestCase):
    data = [
        "1000",
        "2000",
        "3000",
        "",
        "4000",
        "",
        "5000",
        "6000",
        "",
        "7000",
        "8000",
        "9000",
        "",
        "10000"
    ]

    def test_carrying_most_calories(self):
        self.assertEqual(24000, Dec01(instructions=self.data).part_1())

    def test_sum_top_three_calories(self):
        self.assertEqual(45000, Dec01(instructions=self.data).part_2())
