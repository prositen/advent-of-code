#!/usr/bin/python
import unittest

from python.src.y2016 import dec12


class Dec12Tests(unittest.TestCase):
    def setUp(self):
        self.instructions = ["cpy 41 a",
                             "inc a",
                             "inc a",
                             "dec a",
                             "jnz a 2",
                             "dec a"]
        self.computer = dec12.Computer(self.instructions)

    def test_part_1(self):
        self.computer.run()
        self.assertEqual(42, self.computer.register('a'))
if __name__ == '__main__':
    unittest.main()
