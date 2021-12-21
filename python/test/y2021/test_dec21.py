import unittest

from python.src.y2021.dec21 import Dec21


class TestDec21(unittest.TestCase):

    def test_part_1(self):
        data = ["Player 1 starting position: 4",
                "Player 2 starting position: 8"]

        self.assertEqual(739785, Dec21(instructions=data).part_1())
