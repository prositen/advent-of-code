import unittest

from python.src.y2020.dec06 import Dec06


class TestDec06(unittest.TestCase):
    data = [
        "abc",
        "",
        "a",
        "b",
        "c",
        "",
        "ab",
        "ac",
        "",
        "a",
        "a",
        "a",
        "a",
        "",
        "b"
    ]

    def test_count_any_yes_groups(self):
        self.assertEqual(11, Dec06(instructions=self.data).part_1())

    def test_count_all_yes_groups(self):
        self.assertEqual(6, Dec06(instructions=self.data).part_2())
