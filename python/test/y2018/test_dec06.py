import unittest

from python.src.y2018 import dec06


class TestDec06(unittest.TestCase):
    def test_part_1(self):
        coordinates = [
            "1, 1",
            "1, 6",
            "8, 3",
            "3, 4",
            "5, 5",
            "8, 9"
        ]

        self.assertEqual(17, dec06.Dec06(coordinates).part_1())

    def test_part_2(self):
        coordinates = [
            "1, 1",
            "1, 6",
            "8, 3",
            "3, 4",
            "5, 5",
            "8, 9"
        ]
        self.assertEqual(16, dec06.Dec06(coordinates).part_2(32))
