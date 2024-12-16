import unittest

from python.src.y2024.dec16 import Dec16


class TestDec16(unittest.TestCase):
    data = """###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############""".split('\n')

    def test_part_1(self):
        self.assertEqual(7036, Dec16(instructions=self.data).part_1())

    def test_part_2(self):
        self.assertEqual(45, Dec16(instructions=self.data).part_2())


if __name__ == '__main__':
    unittest.main()
