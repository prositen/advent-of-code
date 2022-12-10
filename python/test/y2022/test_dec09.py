import unittest

from python.src.y2022.dec09 import Dec09


class TestDec09(unittest.TestCase):
    data = [
        "R 4",
        "U 4",
        "L 3",
        "D 1",
        "R 4",
        "D 1",
        "L 5",
        "R 2",
    ]

    def test_part_1_count_tail_positions(self):
        self.assertEqual(13, Dec09(instructions=self.data).part_1())

    def test_part_2_count_tail_positions(self):
        self.assertEqual(1, Dec09(instructions=self.data).part_2())
