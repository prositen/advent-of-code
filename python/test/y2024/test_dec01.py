import unittest

from python.src.y2024.dec01 import Dec01


class TestDec01(unittest.TestCase):
    data = [
        "3   4",
        "4   3",
        "2   5",
        "1   3",
        "3   9",
        "3   3"
    ]

    def test_part_1(self):
        self.assertEqual(11, Dec01(instructions=self.data).part_1())

    def test_part_2(self):
        self.assertEqual(31, Dec01(instructions=self.data).part_2())


if __name__ == '__main__':
    unittest.main()
