import unittest

from python.src.y2024.dec09 import Dec09


class TestDec09(unittest.TestCase):
    data = ["2333133121414131402"]

    def test_part_1(self):
        self.assertEqual(1928, Dec09(instructions=self.data).part_1())

    def test_part_2(self):
        self.assertEqual(2858, Dec09(instructions=self.data).part_2())


if __name__ == '__main__':
    unittest.main()
