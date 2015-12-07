#!/usr/bin/env python
import unittest
from src import dec05

__author__ = 'anna'


class Dec04Tests(unittest.TestCase):
    def setUp(self):
        pass

    def testNaughtyOrNiceExample1(self):
        self.assertTrue(dec05.naughty_or_nice('ugknbfddgicrmopn'))

    def testNaughtyOrNiceExample2(self):
        self.assertTrue(dec05.naughty_or_nice('aaa'))

    def testNaughtyOrNiceExample3(self):
        self.assertFalse(dec05.naughty_or_nice('jchzalrnumimnmhp'))

    def testNaughtyOrNiceExample4(self):
        self.assertFalse(dec05.naughty_or_nice('haegwjzuvuyypxyu'))

    def testNaughtyOrNiceExample5(self):
        self.assertFalse(dec05.naughty_or_nice('dvszwmarrgswjxmb'))
