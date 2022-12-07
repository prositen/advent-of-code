import unittest

from python.src.y2022.dec07 import Dec07


class TestDec07(unittest.TestCase):
    data = [
        "$ cd /",
        "$ ls",
        "dir a",
        "14848514 b.txt",
        "8504156 c.dat",
        "dir d",
        "$ cd a",
        "$ ls",
        "dir e",
        "29116 f",
        "2557 g",
        "62596 h.lst",
        "$ cd e",
        "$ ls",
        "584 i",
        "$ cd ..",
        "$ cd ..",
        "$ cd d",
        "$ ls",
        "4060174 j",
        "8033020 d.log",
        "5626152 d.ext",
        "7214296 k"
    ]

    def test_part_1(self):
        self.assertEqual(95437, Dec07(instructions=self.data).part_1())

    def test_part_2(self):
        self.assertEqual(24933642, Dec07(instructions=self.data).part_2())