#!/usr/bin/env python
import unittest

from python.src.y2016 import dec08

__author__ = 'anna'


class Dec08Tests(unittest.TestCase):
    def setUp(self):
        pass

    def test_simple_sequence(self):
        grid = dec08.Screen(7, 3)
        grid.rect(3, 2)
        self.assertListEqual(['###....',
                              '###....',
                              '.......'],
                             grid.get_rows())
        grid.rotate_column(1, 1)
        self.assertListEqual(['#.#....',
                              '###....',
                              '.#.....'],
                             grid.get_rows())
        grid.rotate_row(0, 4)
        self.assertListEqual(['....#.#',
                              '###....',
                              '.#.....'],
                             grid.get_rows())
        grid.rotate_column(1, 1)
        self.assertListEqual(['.#..#.#',
                              '#.#....',
                              '.#.....'],
                             grid.get_rows())

        self.assertEquals(6, grid.count_lit())

if __name__ == '__main__':
    unittest.main()
