import unittest
from python.src.y2017 import dec07


class TestDec07(unittest.TestCase):

    def setUp(self):
        self.puzzle_input = [
            "pbga (66)",
            "xhth (57)",
            "ebii (61)",
            "havc (66)",
            "ktlj (57)",
            "fwft (72) -> ktlj, cntj, xhth",
            "qoyq (66)",
            "padx (45) -> pbga, havc, qoyq",
            "tknk (41) -> ugml, padx, fwft",
            "jptl (61)",
            "ugml (68) -> gyxo, ebii, jptl",
            "gyxo (61)",
            "cntj (57)"
        ]

    def test_find_bottom_program(self):
        rc = dec07.RecursiveCircus(self.puzzle_input)
        root = rc.find_bottom_program()
        self.assertEqual('tknk', root.name)

    def test_get_rebalanced_weight(self):
        rc = dec07.RecursiveCircus(self.puzzle_input)
        self.assertEqual(60, rc.balance_weights()[0])
