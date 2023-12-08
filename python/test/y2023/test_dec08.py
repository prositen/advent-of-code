import unittest

from python.src.y2023.dec08 import Dec08


class TestDec08(unittest.TestCase):

    def test_part_1_a(self):
        data = [
            "RL",
            "",
            "AAA = (BBB, CCC)",
            "BBB = (DDD, EEE)",
            "CCC = (ZZZ, GGG)",
            "DDD = (DDD, DDD)",
            "EEE = (EEE, EEE)",
            "GGG = (GGG, GGG)",
            "ZZZ = (ZZZ, ZZZ)"
        ]

        self.assertEqual(2, Dec08(instructions=data).part_1())

    def test_part_1_b(self):
        data = [
            "LLR",
            "",
            "AAA = (BBB, BBB)",
            "BBB = (AAA, ZZZ)",
            "ZZZ = (ZZZ, ZZZ)"
        ]
        self.assertEqual(6, Dec08(instructions=data).part_1())

    def test_part_2(self):
        data = [
            "LR",
            "",
            "11A = (11B, XXX)",
            "11B = (XXX, 11Z)",
            "11Z = (11B, XXX)",
            "22A = (22B, XXX)",
            "22B = (22C, 22C)",
            "22C = (22Z, 22Z)",
            "22Z = (22B, 22B)",
            "XXX = (XXX, XXX)"
        ]
        self.assertEqual(6, Dec08(instructions=data).part_2())


if __name__ == '__main__':
    unittest.main()
