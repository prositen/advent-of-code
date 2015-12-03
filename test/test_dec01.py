#!/usr/bin/env python
import unittest
from src import dec01


class Dec01Tests(unittest.TestCase):
    def setUp(self):
        pass

    def testFloorExample1(self):
        assert(dec01.floor(0, "(())") == 0)
        assert(dec01.floor(0, "()()") == 0)

    def testFloorExample2(self):
        assert(dec01.floor(0, "(((") == 3)
        assert(dec01.floor(0, "(()(()(") == 3)

    def testFloorExample3(self):
        assert(dec01.floor(0, "))(((((") == 3)

    def testFloorExample4(self):
        assert(dec01.floor(0, "())") == -1)
        assert(dec01.floor(0, "))(") == -1)

    def testFloorExample5(self):
        self.assertEquals(-3, dec01.floor(0, ")))"))
        self.assertEquals(-3, dec01.floor(0, ")())())"))

    def testWhenOnFloorExample1(self):
        self.assertEquals(1, dec01.when_on_floor(0, ")", -1))
        self.assertEquals(5, dec01.when_on_floor(0, "()())", -1))

if __name__ == '__main__':
    unittest.main()