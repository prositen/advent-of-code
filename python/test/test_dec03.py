#!/usr/bin/env python
import unittest

import dec03

__author__ = 'anna'


class Dec03Tests(unittest.TestCase):
    def setUp(self):
        pass

    def testHousesExample1(self):
        self.assertEqual(2, dec03.houses('>'))

    def testHousesExample2(self):
        self.assertEqual(4, dec03.houses('^>v<'))

    def testHousesExample3(self):
        self.assertEqual(2, dec03.houses('^v^v^v^v^v'))

    def testRoboSantaExample1(self):
        self.assertEqual(3, dec03.houses('^v', 2))

    def testRoboSantaExample2(self):
        self.assertEqual(3, dec03.houses('^>v<', 2))

    def testRoboSantaExample3(self):
        self.assertEqual(11, dec03.houses('^v^v^v^v^v', 2))

if __name__ == '__main__':
    unittest.main()