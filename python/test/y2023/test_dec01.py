import unittest

from python.src.y2023.dec01 import Dec01


class TestDec01(unittest.TestCase):

    def test_part_1_calibration_values(self):
        data = [
            "1abc2",
            "pqr3stu8vwx",
            "a1b2c3d4e5f",
            "treb7uchet"
        ]
        self.assertEqual(142, Dec01(instructions=data).part_1())

    def test_part_2(self):
        data = [
            "two1nine",
            "eightwothree",
            "abcone2threexyz",
            "xtwone3four",
            "4nineeightseven2",
            "zoneight234",
            "7pqrstsixteen"
        ]
        self.assertEqual(281, Dec01(instructions=data).part_2())


if __name__ == '__main__':
    unittest.main()
