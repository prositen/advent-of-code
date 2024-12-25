import unittest

from python.src.y2024.dec25 import Dec25


class TestDec25(unittest.TestCase):
    data = """#####
.####
.####
.####
.#.#.
.#...
.....

#####
##.##
.#.##
...##
...#.
...#.
.....

.....
#....
#....
#...#
#.#.#
#.###
#####

.....
.....
#.#..
###..
###.#
###.#
#####

.....
.....
.....
#....
#.#..
#.#.#
#####""".splitlines()

    def test_part_1(self):
        self.assertEqual(3, Dec25(instructions=self.data).part_1())


if __name__ == '__main__':
    unittest.main()
