#!/usr/bin/env python
import unittest

from python.src.y2015 import dec04

__author__ = 'anna'


class Dec04Tests(unittest.TestCase):
    def setUp(self):
        pass

    def testMiningHashesExample1(self):
        self.assertEqual(609043, dec04.mining_hashes('abcdef'))

    def testMiningHashesExample2(self):
        self.assertEqual(1048970, dec04.mining_hashes('pqrstuv'))

if __name__ == '__main__':
    unittest.main()