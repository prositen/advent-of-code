#!/usr/bin/env python
import unittest

from python.src.y2015 import dec05

__author__ = 'anna'


class Dec05Tests(unittest.TestCase):
    def setUp(self):
        pass

    def testNaughtyOrNiceExample1(self):
        self.assertTrue(dec05.naughty_or_nice_1('ugknbfddgicrmopn'))

    def testNaughtyOrNiceExample2(self):
        self.assertTrue(dec05.naughty_or_nice_1('aaa'))

    def testNaughtyOrNiceExample3(self):
        self.assertFalse(dec05.naughty_or_nice_1('jchzalrnumimnmhp'))

    def testNaughtyOrNiceExample4(self):
        self.assertFalse(dec05.naughty_or_nice_1('haegwjzuvuyypxyu'))

    def testNaughtyOrNiceExample5(self):
        self.assertFalse(dec05.naughty_or_nice_1('dvszwmarrgswjxmb'))

    def testNaughtyOrNiceExample6(self):
        self.assertTrue(dec05.naughty_or_nice_2('qjhvhtzxzqqjkmpb'))

    def testNaughtyOrNiceExample7(self):
        self.assertTrue(dec05.naughty_or_nice_2('xxyxx'))

    def testNaughtyOrNiceExample8(self):
        self.assertFalse(dec05.naughty_or_nice_2('uurcxstgmygtbstg'))

    def testNaughtyOrNiceExample9(self):
        self.assertFalse(dec05.naughty_or_nice_2('ieodomkazucvgmuy'))


if __name__ == '__main__':
    unittest.main()
