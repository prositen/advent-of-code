import unittest

from python.src.y2021.dec01 import Dec01


class TestDec01(unittest.TestCase):
    data = [
        "199",
        "200",
        "208",
        "210",
        "200",
        "207",
        "240",
        "269",
        "260",
        "263"
    ]

    def test_number_of_decreases(self):
        self.assertEqual(7, Dec01(instructions=self.data).part_1())

    def test_three_measurement_window(self):
        self.assertEqual(5, Dec01(instructions=self.data).part_2())
