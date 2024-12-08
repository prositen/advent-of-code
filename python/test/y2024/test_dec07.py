import unittest

from python.src.y2024.dec07 import Dec07


class TestDec07(unittest.TestCase):
    data = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20""".split('\n')

    def test_part_1(self):
        self.assertEqual(3749, Dec07(instructions=self.data).part_1())

    def test_part_2(self):
        self.assertEqual(11387, Dec07(instructions=self.data).part_2())


if __name__ == '__main__':
    unittest.main()
