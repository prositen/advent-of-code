from python.src.y2018 import dec02

import unittest


class TestDec02(unittest.TestCase):
    def test_box_checksum(self):
        boxes = [
            "abcdef",
            "bababc",
            "abbcde",
            "abcccd",
            "aabcdd",
            "abcdee",
            "ababab"
        ]
        day2 = dec02.Dec02(instructions=boxes)
        self.assertEqual(12, day2.part_1())

    def test_common_letters(self):
        boxes = [
            "abcde",
            "fghij",
            "klmno",
            "pqrst",
            "fguij",
            "axcye",
            "wvxyz"
        ]
        day2 = dec02.Dec02(instructions=boxes)
        self.assertEqual('fgij', day2.part_2())
