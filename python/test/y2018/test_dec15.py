import unittest

from python.src.y2018.dec15 import Dec15


class TestDec15(unittest.TestCase):
    def test_part_1_a(self):
        map_start = [
            "#######",
            "#G..#E#",
            "#E#E.E#",
            "#G.##.#",
            "#...#E#",
            "#...E.#",
            "#######"
        ]
        self.assertEqual(36334, Dec15(instructions=map_start).part_1())

    def test_part_1_b(self):
        map_start = [
            "#######",
            "#E..EG#",
            "#.#G.E#",
            "#E.##E#",
            "#G..#.#",
            "#..E#.#",
            "#######"
        ]
        self.assertEqual(39514, Dec15(instructions=map_start).part_1())

    def test_part_1_c(self):
        map_start = [
            "#######",
            "#E.G#.#",
            "#.#G..#",
            "#G.#.G#",
            "#G..#.#",
            "#...E.#",
            "#######"
        ]
        self.assertEqual(27755, Dec15(instructions=map_start).part_1())

    def test_part_1_d(self):
        map_start = [
            "#######",
            "#.E...#",
            "#.#..G#",
            "#.###.#",
            "#E#G#G#",
            "#...#G#",
            "######"
        ]
        self.assertEqual(28944, Dec15(instructions=map_start).part_1())

    def test_part_1_e(self):
        map_start = [
            "#########",
            "#G......#",
            "#.E.#...#",
            "#..##..G#",
            "#...##..#",
            "#...#...#",
            "#.G...G.#",
            "#.....G.#",
            "#########"
        ]
        self.assertEqual(18740, Dec15(instructions=map_start).part_1())