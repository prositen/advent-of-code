import unittest

from python.src.y2017 import dec24


class TestBridge(unittest.TestCase):
    def test_strongest_bridge(self):
        puzzle_input = ["0/2",
                        "2/2",
                        "2/3",
                        "3/4",
                        "3/5",
                        "0/1",
                        "10/1",
                        "9/10"]
        b = dec24.Bridges(puzzle_input)
        b.build()
        self.assertEqual(31, b.part1())
