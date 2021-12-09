import unittest

from python.src.y2021.dec09 import Dec09


class TestDec09(unittest.TestCase):
    data = [
        "2199943210",
        "3987894921",
        "9856789892",
        "8767896789",
        "9899965678"
    ]

    def test_risk_level(self):
        self.assertEqual(15, Dec09(instructions=self.data).part_1())

    def test_basins(self):
        self.assertEqual(1134, Dec09(instructions=self.data).part_2())
