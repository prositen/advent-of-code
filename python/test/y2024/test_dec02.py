import unittest

from python.src.y2024.dec02 import Dec02


class TestDec02(unittest.TestCase):
    data = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9""".split('\n')

    def test_part_1(self):
        self.assertEqual(2, Dec02(instructions=self.data).part_1())

    def test_part_2(self):
        self.assertEqual(4, Dec02(instructions=self.data).part_2())


if __name__ == '__main__':
    unittest.main()
