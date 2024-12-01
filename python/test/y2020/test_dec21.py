import unittest

from python.src.y2020.dec21 import Dec21


class TestDec21(unittest.TestCase):
    foods = [
        "mxmxvkd kfcds sqjhc nhms (contains dairy, fish)",
        "trh fvjkl sbzzf mxmxvkd (contains dairy)",
        "sqjhc fvjkl (contains soy)",
        "sqjhc mxmxvkd sbzzf (contains fish)"
    ]

    def test_part_1(self):
        self.assertEqual(5, Dec21(instructions=self.foods).part_1())

    def test_part_2(self):
        self.assertEqual('mxmxvkd,sqjhc,fvjkl',
                         Dec21(instructions=self.foods).part_2())
