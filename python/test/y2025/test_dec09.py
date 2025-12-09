import unittest

from python.src.y2025.dec09 import Dec09


class TestDec09(unittest.TestCase):
    data = """7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3""".splitlines()

    def test_part_1(self):
        self.assertEqual(50, Dec09(instructions=self.data).part_1())

    def test_part_2(self):
        self.assertEqual(24, Dec09(instructions=self.data).part_2())


if __name__ == '__main__':
    unittest.main()
