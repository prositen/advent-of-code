import unittest

from python.src.y2019.intcode import IntCode


class TestDec05(unittest.TestCase):
    def test_intcode(self):
        cases = [
            ([1002, 4, 3, 4, 33],
             [1002, 4, 3, 4, 99])
        ]

        for case in cases:
            ic = IntCode(case[0])
            ic.run()
            self.assertEqual(case[1], ic.data)

    def test_compare_with_8(self):
        cases = [
            ([3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8], (1, 8)),
            ([3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8], (8, 1)),
            ([3, 3, 1108, -1, 8, 3, 4, 3, 99], (1, 8)),
            ([3, 3, 1107, -1, 8, 3, 4, 3, 99], (8, 1))
        ]

        for case in cases:
            ic = IntCode(case[0])
            for test in (1,):
                ic.input = case[1][test]
                ic.run()
                self.assertEqual(ic.output, test)

    def test_jumps(self):
        cases = [
            ([3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9]),
            ([3, 3, 1105, -1, 9, 1101, 0, 0, 12, 4, 12, 99, 1])
        ]

        for case in cases:
            for inp in (0, 1):
                ic = IntCode(case)
                ic.input = inp
                ic.run()
                self.assertEqual(ic.output, inp)

    def test_large_exampple(self):
        program = [3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20, 31,
                   1106, 0, 36, 98, 0, 0, 1002, 21, 125, 20, 4, 20, 1105, 1, 46, 104,
                   999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98, 99]

        for (inp, outp) in [(7, 999), (8, 1000), (9, 1001)]:
            ic = IntCode(program)
            ic.input = inp
            ic.run()
            self.assertEqual(outp, ic.output)
