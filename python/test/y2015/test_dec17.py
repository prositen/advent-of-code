__author__ = 'anna'

import unittest

from python.src.y2015 import dec17


class Dec17Tests(unittest.TestCase):
    def test_fit_eggnog(self):
        bins = [20, 15, 10, 5, 5]
        combinations = dec17.fit_eggnog(bins, 25)
        self.assertEqual(4, len(combinations))


if __name__ == '__main__':
    unittest.main()
