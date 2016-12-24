#!/usr/bin/python
import unittest

from python.src.y2016 import dec24


class Dec24Tests(unittest.TestCase):
    def setUp(self):
        self.map = ["###########",
                    "#0.1.....2#",
                    "#.#######.#",
                    "#4.......3#",
                    "###########"]

        self.grid = dec24.Grid(self.map)

    def test_find_numbers(self):
        self.assertDictEqual({'0': (1, 1),
                              '1': (1, 3),
                              '2': (1, 9),
                              '3': (3, 9),
                              '4': (3, 1)},
                             self.grid.find_numbers())

    def test_visit_numbers(self):
        self.assertEquals(14, self.grid.shortest_path())


if __name__ == '__main__':
    unittest.main()
