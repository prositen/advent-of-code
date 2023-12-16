import unittest

from python.src.y2023.dec16 import Dec16


class TestDec16(unittest.TestCase):
    data = [
        ".|...\\....",
        "|.-.\\.....",
        ".....|-...",
        "........|.",
        "..........",
        ".........\\",
        "..../.\\\\..",
        ".-.-/..|..",
        ".|....-|.\\",
        "..//.|...."

    ]

    def test_part_1(self):
        self.assertEqual(46, Dec16(instructions=self.data).part_1())

    def test_part_2(self):
        self.assertEqual(51, Dec16(instructions=self.data).part_2())


if __name__ == '__main__':
    unittest.main()
