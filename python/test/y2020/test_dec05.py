import unittest

from python.src.y2020.dec05 import Dec05


class TestDec01(unittest.TestCase):
    data = [
        ("FBFBBFFRLR", 357),
        ("BFFFBBFRRR", 567),
        ("FFFBBBFRRR", 119),
        ("BBFFBBFRLL", 820)
    ]

    def test_seat_id(self):
        for case in self.data:
            self.assertEqual(case[1], Dec05.seat_id(case[0]))

    def test_part_1(self):
        self.assertEqual(820, Dec05(instructions=[d[0] for d in self.data]).part_1())
