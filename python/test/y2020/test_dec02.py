import unittest

from python.src.y2020.dec02 import Dec02


class TestDec02(unittest.TestCase):
    data = [
        "1-3 a: abcde",
        "1-3 b: cdefg",
        "2-9 c: ccccccccc"
    ]

    def test_old_policy(self):
        d = Dec02(instructions=self.data)
        self.assertEqual(2, d.part_1())

    def test_new_policy(self):
        d = Dec02(instructions=self.data)
        self.assertEqual(1, d.part_2())
