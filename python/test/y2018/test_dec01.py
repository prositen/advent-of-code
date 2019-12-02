from python.src.y2018 import dec01

import unittest


class TestDec01(unittest.TestCase):

    def test_frequency_change(self):
        cases = [
            (['+1', '-2', '+3', '+1'], 3),
            (['+1', '+1', '+1'], 3),
            (['-1', '-2', '-3'], -6)
        ]

        for case in cases:
            self.assertEqual(case[1], dec01.Dec01(case[0]).part_1())

    def test_first_repeating_frequency(self):
        cases = [
            (['-1', '+1'], 0),
            (['+3', '+3', '+4', '-2', '-4'], 10),
            (['-6', '+3', '+8', '+5', '-6'], 5),
            (['+7', '+7', '-2', '-7', '-4'], 14)
        ]

        for case in cases:
            self.assertEqual(case[1], dec01.Dec01(case[0]).part_2())
