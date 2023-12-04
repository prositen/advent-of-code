import unittest

from python.src.y2023.dec03 import Dec03


class TestDec03(unittest.TestCase):
    data = [
        "467..114..",
        "...*......",
        "..35..633.",
        "......#...",
        "617*......",
        ".....+.58.",
        "..592.....",
        "......755.",
        "...$.*....",
        ".664.598.."
    ]

    def test_part_1(self):
        self.assertEqual(4361, Dec03(instructions=self.data).part_1())

    def test_part_2(self):
        self.assertEqual(467835, Dec03(instructions=self.data).part_2())


if __name__ == '__main__':
    unittest.main()
