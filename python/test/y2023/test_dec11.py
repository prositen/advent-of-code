import unittest

from python.src.y2023.dec11 import Dec11, StarMap


class TestDec11(unittest.TestCase):
    data = [
        "...#......",
        ".......#..",
        "#.........",
        "..........",
        "......#...",
        ".#........",
        ".........#",
        "..........",
        ".......#..",
        "#...#....."
    ]

    def test_part_1(self):

        self.assertEqual(374, Dec11(instructions=self.data).part_1())

    def test_expansion(self):
        for (factor, expected) in ((10, 1030), (100, 8410)):
            sm = StarMap(self.data, expansion=factor)
            self.assertEqual(expected, sm.sum_shortest_pairs())


if __name__ == '__main__':
    unittest.main()
