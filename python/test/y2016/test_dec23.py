#!/usr/bin/python
import unittest

from python.src.y2016 import dec23


class Dec23Tests(unittest.TestCase):
    def setUp(self):
        self.instructions = ["cpy 2 a",
                             "tgl a",
                             "tgl a",
                             "tgl a",
                             "cpy 1 a",
                             "dec a",
                             "dec a"]
        self.computer = dec23.Computer(self.instructions)

    def test_assembunny(self):
        self.computer.run()
        self.assertEquals(3,
                          self.computer.register('a'))

if __name__ == '__main__':
    unittest.main()
