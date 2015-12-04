#!/usr/bin/env python
import unittest
from src import dec04

__author__ = 'anna'


class Dec04Tests(unittest.TestCase):
    def setUp(self):
        pass

    def testMiningHashesExample1(self):
        self.assertEqual(609043, dec04.mining_hashes('abcdef'))

    def testMiningHashesExample2(self):
        self.assertEqual(1048970, dec04.mining_hashes('pqrstuv'))
