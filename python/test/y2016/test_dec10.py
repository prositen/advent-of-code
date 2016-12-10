#!/usr/bin/env python
import unittest

from python.src.y2016 import dec10

__author__ = 'anna'


class Dec10Tests(unittest.TestCase):
    def setUp(self):
        factory = dec10.Factory(["value 5 goes to bot 2",
                                 "bot 2 gives low to bot 1 and high to bot 0",
                                 "value 3 goes to bot 1",
                                 "bot 1 gives low to output 1 and high to bot 0",
                                 "bot 0 gives low to output 2 and high to output 0",
                                 "value 2 goes to bot 2"])

    def test_example_instructions(self):
        pass

if __name__ == '__main__':
        unittest.main()
