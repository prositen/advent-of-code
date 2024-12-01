import unittest

from python.src.y2020.dec08 import Dec08


class TestDec08(unittest.TestCase):
    instructions = [
        "nop +0",
        "acc +1",
        "jmp +4",
        "acc +3",
        "jmp -3",
        "acc -99",
        "acc +1",
        "jmp -4",
        "acc +6"
    ]

    def test_debug_part_1(self):
        self.assertEqual(5, Dec08(instructions=self.instructions).part_1())

    def test_change_par_2(self):
        self.assertEqual(8, Dec08(instructions=self.instructions).part_2())
