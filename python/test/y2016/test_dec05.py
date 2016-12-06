#!/usr/bin/env python
import unittest

from python.src.y2016 import dec05

__author__ = 'anna'


class Dec05Tests(unittest.TestCase):
    def setUp(self):
        pass

    def testMiningHashesExample1(self):
        self.assertEqual('1', dec05.hash_password('abc', 1))

    def testMiningHashesExample2(self):
        self.assertEqual('18', dec05.hash_password('abc', 2))

    def testMoviePassword(self):
        self.assertEquals('05ace8e3', dec05.movie_password('abc'))

if __name__ == '__main__':
    unittest.main()