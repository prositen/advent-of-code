import unittest

from python.src.y2020.dec23 import Dec23


class TestDec23(unittest.TestCase):

    def test_part_1_10_moves(self):
        self.assertEqual('92658374', Dec23(instructions=['389125467']).part_1(moves=10))

    def test_part_1(self):
        self.assertEqual('67384529', Dec23(instructions=['389125467']).part_1())

    def test_part_2(self):
        self.assertEqual(149245887792,
                         Dec23(instructions=['389125467']).part_2())