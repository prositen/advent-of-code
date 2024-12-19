import unittest

from python.src.y2024.dec19 import Dec19


class TestDec19(unittest.TestCase):
    data = """r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb""".split('\n')

    def test_part_1(self):
        self.assertEqual(6, Dec19(instructions=self.data).part_1())

    def test_part_2(self):
        self.assertEqual(16, Dec19(instructions=self.data).part_2())


if __name__ == '__main__':
    unittest.main()
