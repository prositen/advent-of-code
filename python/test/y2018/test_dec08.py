import unittest

from python.src.y2018.dec08 import Dec08


class TestDec08(unittest.TestCase):

    def test_part_1(self):
        instructions = [
            "2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2"
        ]
        d = Dec08(instructions)
        self.assertEqual(138, d.part_1())

    def test_part_2(self):
        instructions = [
            "2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2"
        ]
        d = Dec08(instructions)
        self.assertEqual(66, d.part_2())
