import unittest

from python.src.y2022.dec22 import Dec22


class TestDec22(unittest.TestCase):
    data = """        ...#
        .#..
        #...
        ....
...#.......#
........#...
..#....#....
..........#.
        ...#....
        .....#..
        .#......
        ......#.

10R5L5R10L4R5L5""".split('\n')

    def test_part_1(self):
        self.assertEqual(6032, Dec22(instructions=self.data).part_1())
