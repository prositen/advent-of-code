import unittest

from python.src.y2022.dec05 import Dec05


class TestDec05(unittest.TestCase):
    data = [
        "    [D]    ",
        "[N] [C]    ",
        "[Z] [M] [P]",
        " 1   2   3 ",
        "",
        "move 1 from 2 to 1",
        "move 3 from 1 to 3",
        "move 2 from 2 to 1",
        "move 1 from 1 to 2",
    ]

    def test_part_1(self):
        self.assertEqual('CMZ', Dec05(instructions=self.data).part_1())

    def test_part_2(self):
        self.assertEqual('MCD', Dec05(instructions=self.data).part_2())
