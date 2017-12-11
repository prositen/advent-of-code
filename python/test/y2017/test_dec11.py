import unittest

from python.src.y2017 import dec11


class TestHex(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.puzzle_inputs = [
            ("ne,ne,ne", 3),
            ("ne,ne,sw,sw", 0),
            ("se,sw,se,sw,sw", 3)
        ]

    def test_naive_hex(self):
        for puzzle, expected in self.puzzle_inputs:
            h = dec11.NaiveHex()
            steps, max_steps = h.solve(puzzle)
            self.assertEqual(expected, steps)

    def test_quicker_hex(self):
        for puzzle, expected in self.puzzle_inputs:
            h = dec11.QuickerHex()
            steps, max_steps = h.solve(puzzle)
            self.assertEqual(expected, steps)
