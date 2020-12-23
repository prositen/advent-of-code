import unittest

from python.src.y2020.dec22 import Dec22


class TestDec22(unittest.TestCase):
    starting_hands = ["Player 1:",
                      "9",
                      "2",
                      "6",
                      "3",
                      "1",
                      "",
                      "Player 2:",
                      "5",
                      "8",
                      "4",
                      "7",
                      "10"]

    def test_part_1(self):
        self.assertEqual(306, Dec22(instructions=self.starting_hands).part_1())

    def test_part_2_not_infinite(self):
        hands = ["Player 1:",
                 "43",
                 "19",
                 "",
                 "Player 2:",
                 "2",
                 "29",
                 "14"]
        self.assertTrue(Dec22(instructions=hands).part_2(debug=True))

    def test_part_2(self):
        self.assertEqual(291, Dec22(instructions=self.starting_hands).part_2())
