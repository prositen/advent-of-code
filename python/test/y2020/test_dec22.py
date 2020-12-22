import unittest

from python.src.y2020.dec22 import Dec22


class TestDec22(unittest.TestCase):

    def test_part_1(self):
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
        self.assertEqual(306, Dec22(instructions=starting_hands).part_1())
