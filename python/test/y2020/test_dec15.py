import unittest

from python.src.y2020.dec15 import Dec15


class TestDec15(unittest.TestCase):

    def test_part_1(self):
        cases = [
            (436, "0,3,6"),
            (1, "1,3,2"),
            (10, "2,1,3"),
            (27, "1,2,3"),
            (78, "2,3,1"),
            (438, "3,2,1"),
            (1836, "3,1,2")
        ]
        for expected, data in cases:
            self.assertEqual(expected, Dec15(instructions=[data]).part_1())

    def test_part_2(self):
        cases = [
            (175594, "0,3,6"),
            (2578, "1,3,2"),
            (3544142, "2,1,3"),
            (261214, "1,2,3"),
            (6895259, "2,3,1"),
            (18, "3,2,1"),
            (362, "3,1,2")
        ]
        for expected, data in cases:
            self.assertEqual(expected, Dec15(instructions=[data]).part_2())