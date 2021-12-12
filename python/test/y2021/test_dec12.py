import unittest

from python.src.y2021.dec12 import Dec12


class TestDec12(unittest.TestCase):

    def test_example_1(self):
        data = [
            "start-A",
            "start-b",
            "A-c",
            "A-b",
            "b-d",
            "A-end",
            "b-end"
        ]

        self.assertEqual(10, Dec12(instructions=data).part_1())
        self.assertEqual(36, Dec12(instructions=data).part_2())

    def test_example_2(self):
        data = [
            "dc-end",
            "HN-start",
            "start-kj",
            "dc-start",
            "dc-HN",
            "LN-dc",
            "HN-end",
            "kj-sa",
            "kj-HN",
            "kj-dc",
        ]
        self.assertEqual(19, Dec12(instructions=data).part_1())
        self.assertEqual(103, Dec12(instructions=data).part_2())

    def test_example_3(self):
        data = [
            "fs-end",
            "he-DX",
            "fs-he",
            "start-DX",
            "pj-DX",
            "end-zg",
            "zg-sl",
            "zg-pj",
            "pj-he",
            "RW-he",
            "fs-DX",
            "pj-RW",
            "zg-RW",
            "start-pj",
            "he-WI",
            "zg-he",
            "pj-fs",
            "start-RW"
        ]

        self.assertEqual(226, Dec12(instructions=data).part_1())
        self.assertEqual(3509, Dec12(instructions=data).part_2())
