import unittest

from python.src.y2020.dec12 import Dec12


class TestDec12(unittest.TestCase):
    instructions = [
        "F10",
        "N3",
        "F7",
        "R90",
        "F11"
    ]

    def test_manhattan_distance(self):
        self.assertEqual(25, Dec12(instructions=self.instructions).part_1())

    def test_with_waypoint(self):
        self.assertEqual(286, Dec12(instructions=self.instructions).part_2())
