import unittest

from python.src.y2021.dec23 import Dec23


class TestDec23(unittest.TestCase):

    def test_part_1(self):
        data = [
            "#############",
            "#...........#",
            "###B#C#B#D###",
            "  #A#D#C#A# ",
            "  ######### "
        ]

        self.assertEqual(12521, Dec23(instructions=data).part_1())
