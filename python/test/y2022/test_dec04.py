import unittest

from python.src.y2022.dec04 import Dec04


class TestDec04(unittest.TestCase):
    data = [
        "2-4,6-8",
        "2-3,4-5",
        "5-7,7-9",
        "2-8,3-7",
        "6-6,4-6",
        "2-6,4-8"
    ]

    def test_part_1(self):
        self.assertEqual(2, Dec04(instructions=self.data).part_1())

    def test_part_2(self):
        self.assertEqual(4, Dec04(instructions=self.data).part_2())
