from python.src.y2022.dec03 import Dec03

import unittest


class TestDec03(unittest.TestCase):
    data = [
        "vJrwpWtwJgWrhcsFMMfFFhFp",
        "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
        "PmmdzqPrVvPwwTWBwg",
        "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
        "ttgJtRGJQctTZtZT",
        "CrZsJsPPZsGzwwsLwLmpwMDw"
    ]

    def test_part_1(self):
        self.assertEqual(157, Dec03(instructions=self.data).part_1())

    def test_part_2(self):
        self.assertEqual(70, Dec03(instructions=self.data).part_2())
