import unittest

from python.src.y2024.dec13 import Dec13


class TestDec13(unittest.TestCase):
    data = """Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279""".split('\n')

    def test_part_1(self):
        self.assertEqual(480, Dec13(instructions=self.data).part_1())

    def test_part_2(self):
        self.assertEqual(0, Dec13(instructions=self.data).part_2())


if __name__ == '__main__':
    unittest.main()
