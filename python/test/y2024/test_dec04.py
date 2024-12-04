import unittest

from python.src.y2024.dec04 import Dec04


class TestDec04(unittest.TestCase):
    data = [
        "MMMSXXMASM",
        "MSAMXMSMSA",
        "AMXSXMAAMM",
        "MSAMASMSMX",
        "XMASAMXAMM",
        "XXAMMXXAMA",
        "SMSMSASXSS",
        "SAXAMASAAA",
        "MAMMMXMMMM",
        "MXMXAXMASX"
    ]

    def test_part_1(self):
        self.assertEqual(18, Dec04(instructions=self.data).part_1())

    def test_part_2(self):
        self.assertEqual(9, Dec04(instructions=self.data).part_2())


if __name__ == '__main__':
    unittest.main()
