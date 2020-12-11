import unittest

from python.src.y2020.dec11 import Dec11


class TestDec11(unittest.TestCase):
    seat_layout = [
        "L.LL.LL.LL",
        "LLLLLLL.LL",
        "L.L.L..L..",
        "LLLL.LL.LL",
        "L.LL.LL.LL",
        "L.LLLLL.LL",
        "..L.L.....",
        "LLLLLLLLLL",
        "L.LLLLLL.L",
        "L.LLLLL.LL"
    ]

    def test_part_1_a(self):
        self.assertEqual(37, Dec11(instructions=self.seat_layout).part_1())

    def test_part_2(self):
        self.assertEqual(26, Dec11(instructions=self.seat_layout).part_2())
