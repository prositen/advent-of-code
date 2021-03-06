#!/usr/bin/env python
import unittest

from python.src.y2015 import dec06


class Dec06Tests(unittest.TestCase):
    def setUp(self):
        pass

    def testLightingExample1(self):
        instructions = ["turn on 0,0 through 999,999"]
        self.assertEqual(1000000, dec06.lightning(instructions))

    def testLightingExample2(self):
        instructions = ["toggle 0,0 through 999,0"]
        self.assertEqual(1000, dec06.lightning(instructions))

    def testLightingExample3(self):
        instructions = ["turn on 0,0 through 999,999",
                        "turn off 499,499 through 500,500"]
        self.assertEqual(999996, dec06.lightning(instructions))

    def testLightning_debug1(self):
        instructions = ["turn on 0,0 through 9,9",
                        "toggle 5,5 through 5,5",
                        "toggle 1,1 through 1,1"]
        self.assertEqual(98, dec06.lightning(instructions))

    def testBrightnessExample1(self):
        instructions = ["turn on 0,0 through 0,0"]
        self.assertEqual(1, dec06.brightness(instructions))

    def testBrightnessExample2(self):
        instructions = ["toggle 0,0 through 999,999"]
        self.assertEqual(2000000, dec06.brightness(instructions))


if __name__ == '__main__':
    unittest.main()
