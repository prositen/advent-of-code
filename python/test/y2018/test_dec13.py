import unittest

from python.src.y2018.dec13 import Dec13


class TestDec13(unittest.TestCase):

    def a_test_part_1(self):
        instructions = ["/->-\\         ",
                        "|   |  /----\\",
                        "| /-+--+-\\  |",
                        "| | |  | v  |",
                        "\\-+-/  \\-+--/",
                        "\\------/ "]

        d = Dec13(instructions)
        self.assertEqual((7, 3), d.part_1())

    def test_part_2(self):
        instructions = ["/>-<\\",
                        "|   |",
                        "| /<+-\\",
                        "| | | v",
                        "\\>+</ |",
                        "  |   ^",
                        "  \\<->/"]
        d = Dec13(instructions)
        self.assertEqual((6, 4), d.part_2())
