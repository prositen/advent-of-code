__author__ = 'anna'

import unittest
from python.src import dec08


class Dec08Tests(unittest.TestCase):
    def testCharDecodeDiff_Example1(self):
        self.assertEquals(2, dec08.char_decode_diff(r'""'))

    def testCharDecodeDiff_Example2(self):
        self.assertEquals(2, dec08.char_decode_diff(r'"abc"'))

    def testCharDecodeDiff_Example3(self):
        self.assertEquals(3, dec08.char_decode_diff(r'"aaa\"aaa"'))

    def testCharDecodeDiff_Example4(self):
        self.assertEquals(5, dec08.char_decode_diff(r'"\x27"'))

    def testCharEncodeDiff_Example1(self):
        self.assertEquals(4, dec08.char_encode_diff(r'""'))

    def testCharEncodeDiff_Example2(self):
        self.assertEquals(4, dec08.char_encode_diff(r'"abc"'))

    def testCharEncodeDiff_Example3(self):
        self.assertEquals(6, dec08.char_encode_diff(r'"aaa\"aaa"'))

    def testCharEncodeDiff_Example4(self):
        self.assertEquals(5, dec08.char_encode_diff(r'"\x27"'))

if __name__ == '__main__':
    unittest.main()
