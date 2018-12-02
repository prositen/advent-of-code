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
        self.assertEqual(12, dec02.box_checksum(boxes))

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
        self.assertEqual('fgij', dec02.common_letters(boxes))
