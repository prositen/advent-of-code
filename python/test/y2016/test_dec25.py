#!/usr/bin/python
import unittest

from python.src.y2016 import dec25


class Dec25Tests(unittest.TestCase):
    def test_out(self):
        self.computer = dec25.Computer(['out a',
                                        'inc a',
                                        'jnz 1 -2'],
                                       10)
        self.computer.run()
        self.assertListEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                             self.computer.output)


if __name__ == '__main__':
    unittest.main()
