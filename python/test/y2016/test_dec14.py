#!/usr/bin/python
import unittest

from python.src.y2016 import dec14


class Dec14Tests(unittest.TestCase):
    def test_otp_keys(self):
        keys = dec14.get_hash_keys('abc')
        self.assertEqual(39, keys[0])
        self.assertEqual(92, keys[1])
        self.assertEqual(22728, keys[63])

    def test_stretch(self):
        self.assertEqual("a107ff634856bb300138cac6568c0f24",
                         dec14.super_hash("abc0", 2016))


if __name__ == '__main__':
    unittest.main()
