import unittest

from python.src.y2019 import dec01


class TestDec01(unittest.TestCase):

    def test_module_mass(self):
        cases = [
            (['12'], 2),
            (['14'], 2),
            (['1969'], 654),
            (['100756'], 33583)
        ]

        for case in cases:
            self.assertEqual(case[1], dec01.Dec01(case[0]).part_1())

    def test_added_fuel_mass(self):
        cases = [
            (['14'], 2),
            (['1969'], 966),
            (['100756'], 50346)
        ]

        for case in cases:
            self.assertEqual(case[1], dec01.Dec01(case[0]).part_2())
