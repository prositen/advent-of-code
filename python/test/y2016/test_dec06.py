#!/usr/bin/env python
import unittest

from python.src.y2016 import dec06

__author__ = 'anna'


class Dec06Tests(unittest.TestCase):
    def setUp(self):
        pass

    def test_repetition_code(self):
        self.assertEqual('easter',
                         dec06.repetition_code(['eedadn',
                                                'drvtee',
                                                'eandsr',
                                                'raavrd',
                                                'atevrs',
                                                'tsrnev',
                                                'sdttsa',
                                                'rasrtv',
                                                'nssdts',
                                                'ntnada',
                                                'svetve',
                                                'tesnvt',
                                                'vntsnd',
                                                'vrdear',
                                                'dvrsen',
                                                'enarar']))

    def test_modified_repetition_code(self):
        self.assertEqual('advent',
                         dec06.modified_repetition_code(['eedadn',
                                                         'drvtee',
                                                         'eandsr',
                                                         'raavrd',
                                                         'atevrs',
                                                         'tsrnev',
                                                         'sdttsa',
                                                         'rasrtv',
                                                         'nssdts',
                                                         'ntnada',
                                                         'svetve',
                                                         'tesnvt',
                                                         'vntsnd',
                                                         'vrdear',
                                                         'dvrsen',
                                                         'enarar']))

    if __name__ == '__main__':
        unittest.main()
