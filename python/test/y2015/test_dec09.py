__author__ = 'anna'

import unittest

from python.src.y2015 import dec09


class Dec09Tests(unittest.TestCase):
    def test_shortest_path(self):
        distances = ["London to Dublin = 464",
                     "London to Belfast = 518",
                     "Dublin to Belfast = 141"]
        self.assertEqual(605, dec09.shortest_path(distances))

    def test_longest_path(self):
        distances = ["London to Dublin = 464",
                     "London to Belfast = 518",
                     "Dublin to Belfast = 141"]
        self.assertEqual(982, dec09.longest_path(distances))


if __name__ == '__main__':
    unittest.main()
