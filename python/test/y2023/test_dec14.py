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
        expected = (
            ".....#....",
            "....#...O#",
            "...OO##...",
            ".OO#......",
            ".....OOO#.",
            ".O#...O#.#",
            "....O#....",
            "......OOOO",
            "#...O###..",
            "#..OO#...."
        )
        mp = MetalPlatform(self.data)
        mp.cycle()
        self.assertEqual(expected,
                         mp.platform)

    def test_part_2(self):
       self.assertEqual(64, Dec14(instructions=self.data).part_2())


if __name__ == '__main__':
    unittest.main()
