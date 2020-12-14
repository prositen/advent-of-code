import unittest

from python.src.y2020.dec14 import Dec14


class TestDec14(unittest.TestCase):
    instructions = [
        "mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X",
        "mem[8] = 11",
        "mem[7] = 101",
        "mem[8] = 0"
    ]

    def test_initialization(self):
        self.assertEqual(165, Dec14(instructions=self.instructions).part_1())
