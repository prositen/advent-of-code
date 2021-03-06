#!/usr/bin/env python
import unittest

from python.src.y2015 import dec02

__author__ = 'anna'


class Dec02Tests(unittest.TestCase):
    def setUp(self):
        pass

    def testWrapExample1(self):
        self.assertEqual(58, dec02.wrap(2, 3, 4))

    def testWrapExample2(self):
        self.assertEqual(43, dec02.wrap(1, 1, 10))

    def testRibbonExample1(self):
        self.assertEqual(34, dec02.ribbon(2, 3, 4))

    def testRibbonExample2(self):
        self.assertEqual(14, dec02.ribbon(1, 1, 10))


if __name__ == '__main__':
    unittest.main()
