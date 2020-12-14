import unittest

from python.src.y2020.dec14 import Dec14


class TestDec14(unittest.TestCase):

    def test_initialization(self):
        instructions = [
            "mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X",
            "mem[8] = 11",
            "mem[7] = 101",
            "mem[8] = 0"
        ]
        self.assertEqual(165, Dec14(instructions=instructions).part_1())

    def test_floating(self):
        instructions = [
            "mask = 000000000000000000000000000000X1001X",
            "mem[42] = 100",
            "mask = 00000000000000000000000000000000X0XX",
            "mem[26] = 1"
        ]
        self.assertEqual(208, Dec14(instructions=instructions).part_2())
