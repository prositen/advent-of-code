import unittest

from python.src.y2019.intcode import IntCode


class TestDec09(unittest.TestCase):
    def test_quine(self):
        data = [109, 1, 204, -1, 1001, 100, 1, 100, 1008, 100, 16, 101, 1006, 101, 0, 99]
        ic = IntCode(instructions=data)
        ic.run(debug=True)
        self.assertEqual(data, ic.output)

    def atest_16bit(self):
        data = [1102, 34915192, 34915192, 7, 4, 7, 99, 0]
        ic = IntCode(instructions=data)
        ic.run()
        self.assertGreaterEqual(ic.output[0], 2 ** 16)

    def atest_large_number(self):
        data = [104, 1125899906842624, 99]
        ic = IntCode(instructions=data)
        ic.run()
        self.assertEqual(data[1], ic.output[0])


if __name__ == '__main__':
    unittest.main()
