import unittest

from python.src.y2020.dec16 import Dec16


class TestDec16(unittest.TestCase):

    def test_error_rate(self):
        notes = ["class: 1-3 or 5-7",
                 "row: 6-11 or 33-44",
                 "seat: 13-40 or 45-50",
                 "",
                 "your ticket:",
                 "7,1,14",
                 "",
                 "nearby tickets:",
                 "7,3,47",
                 "40,4,50",
                 "55,2,20",
                 "38,6,12"]
        self.assertEqual(71, Dec16(instructions=notes).part_1())
