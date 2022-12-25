from python.src.y2022.dec17 import Dec17

import unittest


class TestDec17(unittest.TestCase):
    data = [">>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"]

    def test_part_1(self):
        self.assertEqual(3068, Dec17(instructions=self.data).part_1())

    def test_part_2(self):
        self.assertEqual(1514285714288,
                         Dec17(instructions=self.data).part_2())
