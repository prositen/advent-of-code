#!/usr/bin/env python
import unittest

from python.src.y2016 import dec09

__author__ = 'anna'


class Dec09Tests(unittest.TestCase):
    def setUp(self):
        pass

    def test_decompress_1(self):
        self.assertEqual("ADVENT", dec09.decompressed_length("ADVENT", 1, return_text=True))

    def test_decompress_2(self):
        self.assertEqual("ABBBBBC", dec09.decompressed_length("A(1x5)BC", 1, return_text=True))

    def test_decompress_3(self):
        self.assertEqual("XYZXYZXYZ", dec09.decompressed_length("(3x3)XYZ", 1, return_text=True))

    def test_decompress_4(self):
        self.assertEqual("ABCBCDEFEFG", dec09.decompressed_length("A(2x2)BCD(2x2)EFG", 1, return_text=True))

    def test_decompress_5(self):
        self.assertEqual("(1x3)A", dec09.decompressed_length("(6x1)(1x3)A", 1, return_text=True))

    def test_decompress_6(self):
        self.assertEqual("X(3x3)ABC(3x3)ABCY", dec09.decompressed_length("X(8x2)(3x3)ABCY", 1, return_text=True))

    def test_decompressed_length_1(self):
        self.assertEqual(9, dec09.decompressed_length("(3x3)XYZ", 2))

    def test_decompressed_length_2(self):
        self.assertEqual(20, dec09.decompressed_length("X(8x2)(3x3)ABCY", 2))

    def test_decompressed_length_3(self):
        self.assertEqual(241920, dec09.decompressed_length("(27x12)(20x12)(13x14)(7x10)(1x12)A", 2))

    def test_decompressed_length_4(self):
        self.assertEqual(445, dec09.decompressed_length("(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN", 2))

if __name__ == '__main__':
    unittest.main()
