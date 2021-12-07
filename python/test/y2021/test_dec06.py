import unittest

from python.src.y2021.dec06 import Dec06


class TestDec06(unittest.TestCase):

    data = ["3,4,3,1,2"]

    def test_80_days(self):
        self.assertEqual(5934, Dec06(instructions=self.data).part_1())

    def test_256_days(self):
        self.assertEqual(26984457539, Dec06(instructions=self.data).part_2())
