import unittest

from python.src.y2019 import dec01
from python.src.y2020.dec01 import Dec01


class TestDec01(unittest.TestCase):
    data = [
        "1721",
        "979",
        "366",
        "299",
        "675",
        "1456"
    ]

    def test_two_entries(self):
        self.assertEqual(514579, Dec01(instructions=self.data).part_1())

    def test_three_entries(self):
        self.assertEqual(241861950, Dec01(instructions=self.data).part_2())
