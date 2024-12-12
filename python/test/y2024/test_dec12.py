import unittest

from python.src.y2024.dec12 import Dec12, Garden


class TestDec12(unittest.TestCase):
    data = (
        ["AAAA", "BBCD", "BBCC", "EEEC"],
        ["OOOOO", "OXOXO", "OOOOO", "OXOXO", "OOOOO"],
        ["RRRRIICCFF", "RRRRIICCCF", "VVRRRCCFFF", "VVRCCCJFFF", "VVVVCJJCFE",
         "VVIVCCJJEE", "VVIIICJJEE", "MIIIIIJJEE", "MIIISIJEEE", "MMMISSJEEE"]
    )

    def test_find_regions(self):
        cases = zip((5, 5, 11), self.data)
        for expected, data in cases:
            self.assertEqual(expected, len(Garden(data).regions))

    def test_part_1(self):
        cases = zip((140,772,1930), self.data)
        for expected, data in cases:
            self.assertEqual(expected, Dec12(instructions=data).part_1())

    def test_part_2(self):
        cases = zip((80, 436, 1206), self.data)
        for expected, data in cases:
            self.assertEqual(expected, Dec12(instructions=data).part_2())


if __name__ == '__main__':
    unittest.main()
