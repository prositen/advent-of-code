__author__ = 'anna'

import unittest

from python.src.y2015 import dec08


class Dec08Tests(unittest.TestCase):
    def testCharDecodeDiff_Example1(self):
        self.assertEqual(2, dec08.char_decode_diff(r'""'))

    def testCharDecodeDiff_Example2(self):
        self.assertEqual(2, dec08.char_decode_diff(r'"abc"'))

    def testCharDecodeDiff_Example3(self):
        self.assertEqual(3, dec08.char_decode_diff(r'"aaa\"aaa"'))

    def testCharDecodeDiff_Example4(self):
        self.assertEqual(5, dec08.char_decode_diff(r'"\x27"'))

    def testCharEncodeDiff_Example1(self):
        self.assertEqual(4, dec08.char_encode_diff(r'""'))

    def testCharEncodeDiff_Example2(self):
        self.assertEqual(4, dec08.char_encode_diff(r'"abc"'))

    def testCharEncodeDiff_Example3(self):
        self.assertEqual(6, dec08.char_encode_diff(r'"aaa\"aaa"'))

    def testCharEncodeDiff_Example4(self):
        self.assertEqual(5, dec08.char_encode_diff(r'"\x27"'))


if __name__ == '__main__':
    unittest.main()
