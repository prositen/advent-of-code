import unittest
from python.src.y2017 import dec13


class TestFireWall(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.puzzle_input = ["0: 3", "1: 2", "4: 4", "6: 4"]

    def test_severity(self):
        fw = dec13.FireWall(self.puzzle_input)
        self.assertEqual(24, fw.severity())

    def test_shortest_delay(self):
        fw = dec13.FireWall(self.puzzle_input)
        self.assertEqual(10, fw.shortest_delay())