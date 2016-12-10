#!/usr/bin/env python
import unittest

from python.src.y2016 import dec07

__author__ = 'anna'


class Dec07Tests(unittest.TestCase):
    def setUp(self):
        pass

    def test_supports_tls_1(self):
        self.assertTrue(dec07.ipv7_supports_tls('abba[mnop]qrst'))

    def test_supports_tls_2(self):
        self.assertFalse(dec07.ipv7_supports_tls('abcd[bddb]xyyx'))

    def test_supports_tls_3(self):
        self.assertFalse(dec07.ipv7_supports_tls('aaaa[qwer]tyui'))

    def test_supports_tls_4(self):
        self.assertTrue(dec07.ipv7_supports_tls('ioxxoj[asdfgh]zxcvbn'))

    def test_supports_ssl_1(self):
        self.assertTrue(dec07.ipv7_supports_ssl('aba[bab]xyz'))

    def test_supports_ssl_2(self):
        self.assertFalse(dec07.ipv7_supports_ssl('xyx[xyx]xyx'))

    def test_supports_ssl_3(self):
        self.assertTrue(dec07.ipv7_supports_ssl('aaa[kek]eke'))

    def test_supports_ssl_4(self):
        self.assertTrue(dec07.ipv7_supports_ssl('zazbz[bzb]cdb'))

if __name__ == '__main__':
    unittest.main()
