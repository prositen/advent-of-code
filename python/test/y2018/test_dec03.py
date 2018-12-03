import unittest

from python.src.y2018 import dec03


class TestDec01(unittest.TestCase):

    def setUp(self):
        claims = [
            "#1 @ 1,3: 4x4",
            "#2 @ 3,1: 4x4",
            "#3 @ 5,5: 2x2"
        ]
        self.fabric = dec03.Fabric(claims)

    def test_overlapping_squares(self):
        self.assertEqual(4, self.fabric.overlapping_squares())

    def test_no_overlaps(self):
        self.assertEqual(3, self.fabric.no_overlaps())
