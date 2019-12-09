import unittest

from python.src.y2019.intcode import IntCode


class TestDec02(unittest.TestCase):
    def test_intcode(self):
        cases = [
            ([1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50],
             [3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50]),
            ([1, 0, 0, 0, 99],
             [2, 0, 0, 0, 99]),
            ([2, 3, 0, 3, 99],
             [2, 3, 0, 6, 99]),
            ([2, 4, 4, 5, 99, 0],
             [2, 4, 4, 5, 99, 9801]),
            ([1, 1, 1, 4, 99, 5, 6, 0, 99],
             [30, 1, 1, 4, 2, 5, 6, 0, 99])
        ]

        for case in cases:
            ic = IntCode(case[0])
            ic.run()
            self.assertEqual(case[1], list(ic.data.values()))
