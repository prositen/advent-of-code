import unittest

from python.src.y2024.dec06 import Dec06


class TestDec06(unittest.TestCase):
    data = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...""".split('\n')

    def test_part_1(self):
        self.assertEqual(41, Dec06(instructions=self.data).part_1())

    def test_part_2(self):
        self.assertEqual(6, Dec06(instructions=self.data).part_2())


if __name__ == '__main__':
    unittest.main()
