import unittest

from python.src.y2021.dec15 import Dec15


class TestDec15(unittest.TestCase):
    data = [
        "1163751742",
        "1381373672",
        "2136511328",
        "3694931569",
        "7463417111",
        "1319128137",
        "1359912421",
        "3125421639",
        "1293138521",
        "2311944581"
    ]

    def test_risk_level(self):
        self.assertEqual(40, Dec15(instructions=self.data).part_1())

    def test_full_map(self):
        self.assertEqual(315, Dec15(instructions=self.data).part_2())
