import unittest
from python.src.y2017 import dec02


class TestDec02(unittest.TestCase):
    def test_minmax_checksum(self):
        input = [[5, 1, 9, 5],
                 [7, 5, 3],
                 [2, 4, 6, 8]]
        self.assertEqual(18, dec02.minmax_checksum(input))

    def test_evenly_divisible_checksum(self):
        input = [[5, 9, 2, 8],
                 [9, 4, 7, 3],
                 [3, 8, 6, 5]]
        self.assertEqual(9, dec02.evenly_divisible_checksum(input))
