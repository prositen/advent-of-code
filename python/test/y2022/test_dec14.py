import unittest

from python.src.y2022.dec14 import Dec14


class TestDec14(unittest.TestCase):
    data = """498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9""".split('\n')

    def test_part_1(self):
        self.assertEqual(24, Dec14(instructions=self.data).part_1())

    def test_part_2(self):
        self.assertEqual(93, Dec14(instructions=self.data).part_2())
