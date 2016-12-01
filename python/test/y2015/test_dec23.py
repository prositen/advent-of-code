__author__ = 'Anna'

import unittest
from python.src.y2015 import dec23


class Dec23Tests(unittest.TestCase):
    def test_example(self):
        lines = ['inc a',
                 'jio a, +2',
                 'tpl a',
                 'inc a']

        program = dec23.Program(lines)
        registers = program.run({'a': 0, 'b': 0})

        self.assertEquals(2, registers['a'])


if __name__ == '__main__':
    unittest.main()
