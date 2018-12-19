import unittest

from python.src.y2018.dec18 import Dec18


class TestDec18(unittest.TestCase):

    def test_part_1(self):
        acres = [
            ".#.#...|#.",
            ".....#|##|",
            ".|..|...#.",
            "..|#.....#",
            "#.#|||#|#|",
            "...#.||...",
            ".|....|...",
            "||...#|.#|",
            "|.||||..|.",
            "...#.|..|."
        ]

        d = Dec18(instructions=acres)
        self.assertEqual(1147, d.part_1())
