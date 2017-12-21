import unittest

from python.src.y2017 import dec21


class TestFractalArt(unittest.TestCase):

    def test_list_pixels(self):
        puzzle_input = [
            "../.# => ##./#../...",
            ".#./..#/### => #..#/..../..../#..#"
        ]

        FA = dec21.FractalArt(puzzle_input)
        for _ in range(2):
            FA.step()
        self.assertEqual(12, FA.lit_pixels())
