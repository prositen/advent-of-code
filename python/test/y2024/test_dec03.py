import unittest

from python.src.y2024.dec03 import Dec03


class TestDec03(unittest.TestCase):

    def test_part_1(self):
        data = ["xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)"
                "+mul(32,64]then(mul(11,8)mul(8,5))"]
        self.assertEqual(161, Dec03(instructions=data).part_1())

    def test_part_2(self):
        data = ["xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"]
        self.assertEqual(48, Dec03(instructions=data).part_2())

    def test_part_2_no_ending_do(self):
        data = ["xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
                "don't()mul(10,10)"]
        self.assertEqual(48, Dec03(instructions=data).part_2())


if __name__ == '__main__':
    unittest.main()
