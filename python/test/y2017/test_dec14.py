import unittest

from python.src.y2017 import dec14

class TestDefrag(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.defragger = dec14.Defragger("flqrgnkx")

    def test_hash_to_bits(self):
        self.assertEqual('1010000011000010000000010111', self.defragger.hash_to_bits('a0c2017'))

    def test_find_squares_used(self):
        self.assertEqual(8108, self.defragger.find_squares_used())

    def test_find_regions(self):
        self.assertEqual(1242, self.defragger.find_regions())
