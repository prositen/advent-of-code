import unittest
from python.src.y2017 import dec10


class TestKnotHash(unittest.TestCase):
    def test_check_first_two(self):
        kh = dec10.KnotHash.from_string_input("3,4,1,5", 5)
        kh.round()
        self.assertEqual(12, kh.check_first_two())

    def test_checksum(self):
        test_cases = [
            ("", "a2582a3a0e66e6e86e3812dcb672a272"),
            ("AoC 2017", "33efeb34ea91902bb2f59c9920caa6cd"),
            ("1,2,3", "3efbe78a8d82f29979031a4aa0b16a9d"),
            ("1,2,4", "63960835bcdc130f0b66d7ff4f6a5a8e")
        ]
        for lengths, expected_result in test_cases:
            kh = dec10.KnotHash.from_bytes_input(lengths)
            kh.run()
            self.assertEqual(expected_result, kh.checksum())
