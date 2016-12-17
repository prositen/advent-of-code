#!/usr/bin/python
import unittest

from python.src.y2016 import dec16


class Dec16Tests(unittest.TestCase):
    def test_dragon_curve(self):
        self.assertEqual("100", dec16.dragon_curve("1"))
        self.assertEqual("001", dec16.dragon_curve("0"))
        self.assertEqual("11111000000", dec16.dragon_curve("11111"))
        self.assertEqual("1111000010100101011110000", dec16.dragon_curve("111100001010"))

    def test_checksum(self):
        self.assertEqual("100", dec16.checksum("110010110100"))

    def test_checksum_of(self):
        self.assertEqual("01100", dec16.checksum_of("10000", 20))


if __name__ == '__main__':
    unittest.main()
