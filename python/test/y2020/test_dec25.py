import unittest

from python.src.y2020.dec25 import Dec25


class TestDec25(unittest.TestCase):

    def test_part_1(self):
        d = Dec25(instructions=['5764801', '17807724'])
        self.assertEqual(14897079, d.part_1())
