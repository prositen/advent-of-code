import unittest

from python.src.y2024.dec11 import Dec11, StoneCorridor


class TestDec11(unittest.TestCase):

    def test_blink(self):
        result = StoneCorridor([0, 1, 10, 99, 999]).blink(1)
        self.assertEqual(7, result)

    def test_blink_6(self):
        result = StoneCorridor([125, 17]).blink(6)
        self.assertEqual(22, result)

    def test_part_1(self):
        self.assertEqual(55312, Dec11(instructions=['125 17']).part_1())

    def atest_part_2(self):
        self.assertEqual(0, Dec11(instructions=self.data).part_2())


if __name__ == '__main__':
    unittest.main()
