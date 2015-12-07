from collections import defaultdict

__author__ = 'anna'

import unittest
from python.src import dec07


class Dec07Tests(unittest.TestCase):
    def testInstructionList(self):
        instructions = ["123 -> x",
                        "456 -> y",
                        "x AND y -> d",
                        "x OR y -> e",
                        "x LSHIFT 2 -> f",
                        "y RSHIFT 2 -> g",
                        "NOT x -> h",
                        "NOT y -> i"]
        result = dec07.run(instructions)
        self.assertEquals(72, result['d'])
        self.assertEquals(507, result['e'])
        self.assertEquals(495, result['f'])
        self.assertEquals(114, result['g'])
        self.assertEquals(65412, result['h'])
        self.assertEquals(65079, result['i'])
        self.assertEquals(123, result['x'])
        self.assertEquals(456, result['y'])

    def test_Store(self):
        cmd = dec07.StoreCommand(1, 'a')
        g = defaultdict(int)
        cmd.run(g)
        self.assertEquals(1, g['a'])

    def test_And(self):
        cmd = dec07.AndCommand(1, 2, 'b')
        g = defaultdict(int)
        g[1] = 1
        g[2] = 2
        cmd.run(g)
        self.assertEquals(0, g['b'])

    def test_And2(self):
        cmd = dec07.AndCommand(1, 2, 'b')
        g = defaultdict(int)
        g[1] = 1
        g[2] = 3
        cmd.run(g)
        self.assertEquals(1, g['b'])


if __name__ == '__main__':
    unittest.main()
