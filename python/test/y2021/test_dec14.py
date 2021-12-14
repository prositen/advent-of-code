import unittest

from python.src.y2021.dec14 import Dec14


class TestDec14(unittest.TestCase):
    data = ["NNCB",
            "",
            "CH -> B",
            "HH -> N",
            "CB -> H",
            "NH -> C",
            "HB -> C",
            "HC -> B",
            "HN -> C",
            "NN -> C",
            "BH -> H",
            "NC -> B",
            "NB -> B",
            "BN -> B",
            "BB -> N",
            "BC -> B",
            "CC -> N",
            "CN -> C"]

    def test_10_steps(self):
        self.assertEqual(1588, Dec14(instructions=self.data).part_1())

    def test_40_steps(self):
        self.assertEqual(2188189693529, Dec14(instructions=self.data).part_2())
