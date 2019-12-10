import unittest

from python.src.y2019 import dec10
from python.src.y2019.intcode import IntCode


class TestDec10(unittest.TestCase):
    def test_part_1_small_map(self):
        starmap = [".#..#",
                   ".....",
                   "#####",
                   "....#",
                   "...##"]

        d = dec10.Dec10(instructions=starmap)
        self.assertEqual(8, d.part_1())
        self.assertEqual((3, 4), d.best_position)

    def test_part_1_example_block(self):
        starmap = ["#.........",
                   "...A......",
                   "...B..a...",
                   ".EDCG....a",
                   "..F.c.b...",
                   ".....c....",
                   "..efd.c.gb",
                   ".......c..",
                   "....f...c.",
                   "...e..d..c"]
        d = dec10.Dec10(instructions=starmap)
        d.part_1()

    def test_part_1_medium_maps(self):
        cases = [(["......#.#.",
                   "#..#.#....",
                   "..#######.",
                   ".#.#.###..",
                   ".#..#.....",
                   "..#....#.#",
                   "#..#....#.",
                   ".##.#..###",
                   "##...#..#.",
                   ".#....####"], (5, 8), 33),
                 (["#.#...#.#.",
                   ".###....#.",
                   ".#....#...",
                   "##.#.#.#.#",
                   "....#.#.#.",
                   ".##..###.#",
                   "..#...##..",
                   "..##....##",
                   "......#...",
                   ".####.###."], (1, 2), 35),
                 ([".#..#..###",
                   "####.###.#",
                   "....###.#.",
                   "..###.##.#",
                   "##.##.#.#.",
                   "....###..#",
                   "..#.#..#.#",
                   "#..#.#.###",
                   ".##...##.#",
                   ".....#.#.."], (6, 3), 41)]

        for starmap, pos, satellites in cases:
            d = dec10.Dec10(instructions=starmap)
            self.assertEqual(satellites, d.part_1())
            self.assertEqual(pos, d.best_position)

    def test_part_1_large_map(self):
        starmap = [".#..##.###...#######",
                   "##.############..##.",
                   ".#.######.########.#",
                   ".###.#######.####.#.",
                   "#####.##.#.##.###.##",
                   "..#####..#.#########",
                   "####################",
                   "#.####....###.#.#.##",
                   "##.#################",
                   "#####.##.###..####..",
                   "..######..##.#######",
                   "####.##.####...##..#",
                   ".#####..#.######.###",
                   "##...#.##########...",
                   "#.##########.#######",
                   ".####.#.###.###.#.##",
                   "....##.##.###..#####",
                   ".#.#.###########.###",
                   "#.#.#.#####.####.###",
                   "###.##.####.##.#..##"]

        d = dec10.Dec10(instructions=starmap)
        self.assertEqual(210, d.part_1())
        self.assertEqual((11, 13), d.best_position)

    def test_vaporize(self):
        starmap = [".#....#####...#..",
                   "##...##.#####..##",
                   "##...#...#.#####.",
                   "..#.....#...###..",
                   "..#.#.....#....##"]
        d = dec10.Dec10(instructions=starmap)
        d.part_1()
        self.assertEqual((8, 3), d.best_position)


if __name__ == '__main__':
    unittest.main()
