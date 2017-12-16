import unittest
from python.src.y2017 import dec16


class TestDancer(unittest.TestCase):
    def test_dance(self):
        puzzle_input = ["s1", "x3/4", "pe/b"]
        dancers = dec16.Dance(puzzle_input)
        self.assertEqual("baedc", dancers.dance("abcde"))
