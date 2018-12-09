import unittest

from python.src.y2018.dec09 import Dec09


class TestDec09(unittest.TestCase):

    def test_part_1(self):
        examples = [
            ("9 players; last marble is worth 25 points", 32),
            ("10 players; last marble is worth 1618 points", 8317),
            ("13 players; last marble is worth 7999 points", 146373),
            ("17 players; last marble is worth 1104 points", 2764),
            ("21 players; last marble is worth 6111 points", 54718),
            ("30 players; last marble is worth 5807 points", 37305)
        ]

        for example, result in examples:
            d = Dec09(instructions=[example])
            self.assertEqual(result, d.part_1())
