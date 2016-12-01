import random
from collections import defaultdict

__author__ = 'anna'

import unittest
from python.src.y2015 import dec07


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
        random.shuffle(instructions)
        result = dec07.run(instructions)
        self.assertEquals(72, result['d'])
        self.assertEquals(507, result['e'])
        self.assertEquals(492, result['f'])
        self.assertEquals(114, result['g'])
        self.assertEquals(65412, result['h'])
        self.assertEquals(65079, result['i'])
        self.assertEquals(123, result['x'])
        self.assertEquals(456, result['y'])

    def test_Store(self):
        cmd = dec07.StoreCommand('12', 'a')
        g = defaultdict(int)
        cmd.run(g)
        self.assertEquals(12, g['a'])

    def test_And(self):
        cmd = dec07.AndCommand('a', 'b', 'c')
        g = defaultdict(int)
        g['a'] = 1
        g['b'] = 2
        cmd.run(g)
        self.assertEquals(0, g['c'])

    def test_And2(self):
        cmd = dec07.AndCommand('a', 'b', 'c')
        g = defaultdict(int)
        g['a'] = 1
        g['b'] = 3
        cmd.run(g)
        self.assertEquals(1, g['c'])

    def test_not(self):
        cmd = dec07.NotCommand('a', 'b')
        g = defaultdict(int)
        g['a'] = 123
        cmd.run(g)
        self.assertEquals(65412, g['b'])

    def test_parseStore(self):
        line = "123 -> a"
        cmd = dec07.parse(line)
        self.assertIsInstance(cmd, dec07.StoreCommand)
        g = defaultdict(int)
        cmd.run(g)
        self.assertEquals(123, g['a'])

    def test_parseOr(self):
        line = 'a OR b -> c'
        cmd = dec07.parse(line)
        self.assertIsInstance(cmd, dec07.OrCommand)
        g = defaultdict(int)
        g['a'] = 1
        g['b'] = 2
        cmd.run(g)
        self.assertEquals(3, g['c'])


if __name__ == '__main__':
    unittest.main()
