import unittest

from python.src.y2024.dec10 import Dec10


class TestDec10(unittest.TestCase):
    data = [
        "89010123",
        "78121874",
        "87430965",
        "96549874",
        "45678903",
        "32019012",
        "01329801",
        "10456732"
    ]

    def test_part_1(self):
        cases = (
            (["0123", "1234", "8765", "9876"], 1),
            (["9990999", "9991998", "9992997", "6543456", "7651987", "8761111", "29871111"], 3),
            (self.data, 36)
        )
        for example, expected in cases:
            self.assertEqual(expected, Dec10(instructions=example).part_1())

    def test_part_2(self):
        self.assertEqual(81, Dec10(instructions=self.data).part_2())


if __name__ == '__main__':
    unittest.main()
