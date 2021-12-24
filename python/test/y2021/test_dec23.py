import unittest

from python.src.y2021.dec23 import Dec23


class TestDec23(unittest.TestCase):
    data = [
        "#############",
        "#...........#",
        "###B#C#B#D###",
        "  #A#D#C#A# ",
        "  ######### "
    ]

    def test_part_1(self):
        self.assertEqual(12521, Dec23(instructions=self.data).part_1())

    def test_part_2(self):
        self.assertEqual(44169, Dec23(instructions=self.data).part_2())

    def test_4_deep(self):
        data = [
            "#############",
            "#...........#",
            "###B#C#D#A###",
            "  #A#B#C#D#  ",
            "  #A#B#C#D#  ",
            "  #A#B#C#D#  ",
            "  #########  "
        ]
        self.assertEqual(4450,
                         Dec23(instructions=data).part_1())
