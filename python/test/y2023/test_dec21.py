import unittest

from python.src.y2023.dec21 import Farm


class TestDec21(unittest.TestCase):
    data = [
        "...........",
        ".....###.#.",
        ".###.##..#.",
        "..#.#...#..",
        "....#.#....",
        ".##..S####.",
        ".##..#...#.",
        ".......##..",
        ".##.#.####.",
        ".##..##.##.",
        "..........."
    ]

    def test_part_1(self):
        f = Farm(self.data)
        for (case, expected) in (
                (3, 6), (6, 16), (10, 50), (50, 1594),
                (100, 6536), (500, 167004)  # , (1000, 668697) , (5000, 16733044)
        ):
            self.assertEqual(expected, f.move(max_steps=case))


if __name__ == '__main__':
    unittest.main()
