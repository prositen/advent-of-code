#!/usr/bin/env python
import unittest

from python.src.y2015 import dec06


class Dec06Tests(unittest.TestCase):
    def setUp(self):
        pass

    def testLightingExample1(self):
        instructions = ["turn on 0,0 through 999,999"]
        self.assertEquals(1000000, dec06.lightning(instructions))

    def testLightingExample2(self):
        instructions = ["work 0,0 through 999,0"]
        self.assertEquals(1000, dec06.lightning(instructions))

    def testLightingExample3(self):
        instructions = ["turn on 0,0 through 999,999",
                        "turn off 499,499 through 500,500"]
        self.assertEquals(999996, dec06.lightning(instructions))

    def testLightning_debug1(self):
        instructions = ["turn on 0,0 through 9,9",
                        "work 5,5 through 5,5",
                        "work 1,1 through 1,1"]
        self.assertEquals(98, dec06.lightning(instructions))

    def testBrightnessExample1(self):
        instructions = ["turn on 0,0 through 0,0"]
        self.assertEquals(1, dec06.brightness(instructions))

    def testBrightnessExample2(self):
        instructions = ["work 0,0 through 999,999"]
        self.assertEquals(2000000, dec06.brightness(instructions))

if __name__ == '__main__':
    unittest.main()