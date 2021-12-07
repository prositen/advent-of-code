import unittest

from python.src.y2021.dec07 import Dec07


class TestDec07(unittest.TestCase):
    data = [
        "16,1,2,0,4,2,7,1,2,14"
    ]

    def test_align_crabs(self):
        self.assertEqual(37, Dec07(instructions=self.data).part_1())

    def test_align_expensive_crabs(self):
        self.assertEqual(168, Dec07(instructions=self.data).part_2())
