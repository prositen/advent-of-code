import unittest

from python.src.y2020.dec17 import Dec17


class TestDec17(unittest.TestCase):

    def test_active_cubes_3d(self):
        state = [".#.",
                 "..#",
                 "###"]
        self.assertEqual(112, Dec17(instructions=state).part_1())

    def test_active_cubes_4d(self):
        state = [".#.",
                 "..#",
                 "###"]
        self.assertEqual(848, Dec17(instructions=state).part_2())
