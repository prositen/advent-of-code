import unittest

from python.src.y2023.dec06 import Dec06


class TestDec04(unittest.TestCase):
    data = [
        "Time:      7  15   30",
        "Distance:  9  40  200"
    ]

    def test_number_of_ways(self):
        self.assertEqual(4, Dec06.brute_wins(time=7, distance=9))
    def test_part_1(self):
        self.assertEqual(288, Dec06(instructions=self.data).part_1())

    def test_part_2(self):
        self.assertEqual(71503, Dec06(instructions=self.data).part_2())


if __name__ == '__main__':
    unittest.main()
