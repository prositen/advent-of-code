import unittest

from python.src.y2017 import dec17


class TestSpinlock(unittest.TestCase):
    def test_after_2017(self):
        s = dec17.Spinlock(3)
        self.assertEqual(638, s.part_1())
