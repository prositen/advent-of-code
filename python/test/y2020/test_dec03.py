import unittest

from python.src.y2020.dec03 import Dec03


class TestDec02(unittest.TestCase):
    area_map = [
        "..##.......",
        "#...#...#..",
        ".#....#..#.",
        "..#.#...#.#",
        ".#...##..#.",
        "..#.##.....",
        ".#.#.#....#",
        ".#........#",
        "#.##...#...",
        "#...##....#",
        ".#..#...#.#"

    ]

    def test_part_1(self):
        d = Dec03(instructions=self.area_map)
        self.assertEqual(7, d.part_1())

    def test_part_2(self):
        d = Dec03(instructions=self.area_map)
        self.assertEqual(336, d.part_2())
