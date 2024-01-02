import unittest

from python.src.y2023.dec24 import Dec24, Hailstorm


class TestDec24(unittest.TestCase):
    data = [
        "19, 13, 30 @ -2,  1, -2",
        "18, 19, 22 @ -1, -1, -2",
        "20, 25, 34 @ -2, -2, -4",
        "12, 31, 28 @ -1, -2, -1",
        "20, 19, 15 @  1, -5, -3"
    ]

    def test_part_1(self):
        day = Dec24(instructions=self.data)
        self.assertEqual(2, Hailstorm(day.instructions).count_intersections(
            min_pos=7, max_pos=27
        ))

    def test_part_2(self):
        self.assertEqual(47, Dec24(instructions=self.data).part_2())


if __name__ == '__main__':
    unittest.main()
