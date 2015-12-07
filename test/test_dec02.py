#!/usr/bin/env python
import unittest
from src import dec02

__author__ = 'anna'


class Dec02Tests(unittest.TestCase):
    def setUp(self):
        pass

    def testWrapExample1(self):
        self.assertEquals(58, dec02.wrap(2, 3, 4))

    def testWrapExample2(self):
        self.assertEquals(43, dec02.wrap(1, 1, 10))

    def testRibbonExample1(self):
        self.assertEquals(34, dec02.ribbon(2, 3, 4))

    def testRibbonExample2(self):
        self.assertEquals(14, dec02.ribbon(1, 1, 10))


if __name__ == '__main__':
    unittest.main()