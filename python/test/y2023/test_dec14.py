import unittest

from python.src.y2023.dec14 import Dec14, MetalPlatform


class TestDec14(unittest.TestCase):
    data = [
        "O....#....",
        "O.OO#....#",
        ".....##...",
        "OO.#O....O",
        ".O.....O#.",
        "O.#..O.#.#",
        "..O..#O..O",
        ".......O..",
        "#....###..",
        "#OO..#...."
    ]

    def test_part_1(self):
        self.assertEqual(136, Dec14(instructions=self.data).part_1())

    def test_cycle(self):
        expected = [
            [c for c in ".....#...."],
            [c for c in "....#...O#"],
            [c for c in "...OO##..."],
            [c for c in ".OO#......"],
            [c for c in ".....OOO#."],
            [c for c in ".O#...O#.#"],
            [c for c in "....O#...."],
            [c for c in "......OOOO"],
            [c for c in "#...O###.."],
            [c for c in "#..OO#...."]
        ]
        mp = MetalPlatform(self.data)
        mp.cycle()
        self.assertEqual(expected,
                         mp.platform)

    def test_part_2(self):
        self.assertEqual(64, Dec14(instructions=self.data).part_2())


if __name__ == '__main__':
    unittest.main()
