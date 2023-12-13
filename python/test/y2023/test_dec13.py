import unittest

from python.src.y2023.dec13 import Dec13


class TestDec13(unittest.TestCase):
    data = [
        "#.##..##.",
        "..#.##.#.",
        "##......#",
        "##......#",
        "..#.##.#.",
        "..##..##.",
        "#.#.##.#.",
        "",
        "#...##..#",
        "#....#..#",
        "..##..###",
        "#####.##.",
        "#####.##.",
        "..##..###",
        "#....#..#"
    ]

    def test_part_1(self):
        self.assertEqual(405, Dec13(instructions=self.data).part_1())

    def test_part_2(self):
        self.assertEqual(400, Dec13(instructions=self.data).part_2())


if __name__ == '__main__':
    unittest.main()
