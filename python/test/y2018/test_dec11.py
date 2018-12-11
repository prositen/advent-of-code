import unittest

from python.src.y2018.dec11 import Dec11


class TestDec11(unittest.TestCase):

    def test_part_1(self):
        cases = [
            ((33, 45), "18"),
            ((21, 61), "42")
        ]
        for expected, serial in cases:
            self.assertEqual(expected, Dec11([serial]).part_1())

    def test_power_level(self):
        cases = [
            (-5, (122, 79), "57"),
            (0, (217, 196), "39"),
            (4, (101, 153), "71")
        ]

        for expected, (x, y), serial in cases:
            self.assertEqual(expected, Dec11([serial]).power_level(x, y))

    def test_part_2(self):
        cases = [
            ((90, 269, 16), "18"),
            ((232, 251, 12), "42")
        ]
        for expected, serial in cases:
            self.assertEqual(expected, Dec11([serial]).part_2)
