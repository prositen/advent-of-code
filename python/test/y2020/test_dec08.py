import unittest

from python.src.y2020.dec08 import Dec08


class TestDec08(unittest.TestCase):

    def test_debug_part_1(self):
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

        self.assertEqual(5, Dec08(instructions=instructions).part_1())
