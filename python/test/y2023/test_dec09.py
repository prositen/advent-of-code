import unittest

from python.src.y2023.dec09 import Dec09


class TestDec01(unittest.TestCase):
    data = [
        "0 3 6 9 12 15",
        "1 3 6 10 15 21",
        "10 13 16 21 30 45"
    ]

    def test_part_1(self):
        self.assertEqual(114, Dec09(instructions=self.data).part_1())

    def test_part_2(self):
        self.assertEqual(2, Dec09(instructions=self.data).part_2())

    def test_extrapolate_part_1(self):
        cases = [
            ([0, 3, 6, 9, 12, 15], 18),
            ([1, 3, 6, 10, 15, 21], 28),
            ([10, 13, 16, 21, 30, 45], 68)
        ]
        for case in cases:
            self.assertEqual(case[1], Dec09.extrapolate(case[0]))

    def test_extrapolate_part_2(self):
        cases = [
            ([0, 3, 6, 9, 12, 15], -3),
            ([1, 3, 6, 10, 15, 21], 0),
            ([10, 13, 16, 21, 30, 45], 5)
        ]
        for case in cases:
            self.assertEqual(case[1], Dec09.extrapolate(case[0], forwards=False))


if __name__ == '__main__':
    unittest.main()
