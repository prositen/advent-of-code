#!/usr/bin/python
import unittest

from python.src.y2016 import dec18


class Dec18Tests(unittest.TestCase):

    def test_floor_map(self):
        self.assertEqual(['..^^.',
                          '.^^^^',
                          '^^..^'],
                         dec18.floor_map('..^^.', 3))

    def test_floor_map_2(self):
        self.assertEqual(['.^^.^.^^^^',
                          '^^^...^..^',
                          '^.^^.^.^^.',
                          '..^^...^^^',
                          '.^^^^.^^.^',
                          '^^..^.^^..',
                          '^^^^..^^^.',
                          '^..^^^^.^^',
                          '.^^^..^.^^',
                          '^^.^^^..^^'],
                         dec18.floor_map('.^^.^.^^^^', 10))

    def test_count_safe_tiles(self):
        self.assertEqual(38, dec18.count_safe_tiles('.^^.^.^^^^', 10))


if __name__ == '__main__':
    unittest.main()
