import unittest

from python.src.y2022.dec08 import Dec08


class TestDec08(unittest.TestCase):
    data = [
        "30373",
        "25512",
        "65332",
        "33549",
        "35390"
    ]

    def test_part_1_count_visible_trees(self):
        self.assertEqual(21, Dec08(instructions=self.data).part_1())

    def test_part_2_scenic_score(self):
        self.assertEqual(8, Dec08(instructions=self.data).part_2())
