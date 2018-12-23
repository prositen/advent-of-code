import unittest

from python.src.y2018.dec23 import Dec23


class TestDec23(unittest.TestCase):

    def test_part_1(self):
        nanobots = [
            "pos=<0,0,0>, r=4",
            "pos=<1,0,0>, r=1",
            "pos=<4,0,0>, r=3",
            "pos=<0,2,0>, r=1",
            "pos=<0,5,0>, r=3",
            "pos=<0,0,3>, r=1",
            "pos=<1,1,1>, r=1",
            "pos=<1,1,2>, r=1",
            "pos=<1,3,1>, r=1"
        ]

        d = Dec23(instructions=nanobots)
        self.assertEqual(7, d.part_1())