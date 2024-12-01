import unittest

from python.src.y2021.dec17 import Dec17


class TestDec17(unittest.TestCase):

    def test_highest_y(self):
        self.assertEqual(45, Dec17(instructions=['target area: x=20..30, y=-10..-5']).part_1())

    def test_number_of_hits(self):
        self.assertEqual(112, Dec17(instructions=['target area: x=20..30, y=-10..-5']).part_2())

    def test_breaks_simple_solution(self):
        self.assertEqual(66, Dec17(instructions=['target area: x=352..377, y=-49..-30']).part_1())
