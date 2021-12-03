import unittest

from python.src.y2021.dec03 import Dec03


class TestDec03(unittest.TestCase):
    data = [
        "00100",
        "11110",
        "10110",
        "10111",
        "10101",
        "01111",
        "00111",
        "11100",
        "10000",
        "11001",
        "00010",
        "01010"
    ]

    def test_power_consumption(self):
        self.assertEqual(198, Dec03(instructions=self.data).part_1())

    def test_life_support_rating(self):
        self.assertEqual(230, Dec03(instructions=self.data).part_2())
