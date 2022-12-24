import unittest

from python.src.y2022.dec23 import Dec23, Grove


class TestDec23(unittest.TestCase):
    larger_data = """....#..
..###.#
#...#.#
.#...##
#.###..
##.#.##
.#..#..""".split('\n')

    def atest_part_1(self):
        self.assertEqual(110, Dec23(instructions=self.larger_data).part_1())

    def test_part_2(self):
        self.assertEqual(20, Dec23(instructions=self.larger_data).part_2())