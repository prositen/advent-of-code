import unittest

from python.src.y2024.dec08 import Dec08
from src.y2024.dec08 import SignalMap


class TestDec08(unittest.TestCase):
    data = """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............""".split('\n')

    def test_antinodes(self):
        data = """..........
..........
..........
....a.....
..........
.....a....
..........
..........
..........
..........""".split('\n')
        sm = SignalMap(data)
        sm.count_anti_nodes()
        self.assertEqual({(1, 3), (7, 6)}, sm.anti_nodes)

    def test_part_1(self):
        self.assertEqual(14, Dec08(instructions=self.data).part_1())

    def test_resonant_harmonics(self):
        data = """T.........
...T......
.T........
..........
..........
..........
..........
..........
..........
..........""".split('\n')
        sm = SignalMap(data, resonant_harmonics=True)
        self.assertEqual(9, sm.count_anti_nodes())

    def test_part_2(self):
        self.assertEqual(34, Dec08(instructions=self.data).part_2())


if __name__ == '__main__':
    unittest.main()