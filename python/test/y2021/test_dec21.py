import unittest

from python.src.y2021.dec21 import Dec21


class TestDec21(unittest.TestCase):
    data = ["Player 1 starting position: 4",
            "Player 2 starting position: 8"]

    def test_part_1(self):

        self.assertEqual(739785, Dec21(instructions=self.data).part_1())

    def test_part_2(self):
        self.assertEqual(444356092776315, Dec21(instructions=self.data).part_2())
