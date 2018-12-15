import unittest

from python.src.y2018.dec14 import Dec14


class TestDec14(unittest.TestCase):


    def test_part_1(self):

        cases = [
            (9, "5158916779"),
            (5, "0124515891"),
            (18, "9251071085"),
            (2018, "5941429882")
        ]

        for num_recipes, result in cases:
            self.assertEqual(result, Dec14(num_recipes).part_1())

    def test_part_2(self):
        cases = [
            ("51589", 9),
            ("01245", 5),
            ("92510", 18),
            ("59414", 2018)
        ]

        for num_recipes, result in cases:
            self.assertEqual(result, Dec14(num_recipes).part_2())
