import unittest

from python.src.y2025.dec05 import Dec05


class TestDec05(unittest.TestCase):
    data = """3-5
10-14
16-20
12-18

1
5
8
11
17
32""".splitlines()

    def test_part_1(self):
        self.assertEqual(3, Dec05(instructions=self.data).part_1())

    def test_part_2(self):
        self.assertEqual(14, Dec05(instructions=self.data).part_2())


if __name__ == '__main__':
    unittest.main()
