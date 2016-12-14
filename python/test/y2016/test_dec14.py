#!/usr/bin/python
import unittest

from python.src.y2016 import dec14


class Dec14Tests(unittest.TestCase):
    def test_otp_keys(self):
        keys = dec14.get_hash_keys('abc')
        self.assertEquals(39, keys[0])
        self.assertEquals(92, keys[1])
        self.assertEquals(22728, keys[63])

    def test_stretch(self):
        self.assertEquals("a107ff634856bb300138cac6568c0f24",
                          dec14.super_hash("abc0", 2016))


if __name__ == '__main__':
    unittest.main()
