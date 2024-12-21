import unittest

from python.src.y2024.dec21 import Dec21
from src.y2024.dec21 import KeyPad, ReindeerStarship


class TestDec21(unittest.TestCase):
    data = [
        "029A",
        "980A",
        "179A",
        "456A",
        "379A"
    ]

    def test_part_1(self):
        self.assertEqual(126384, Dec21(instructions=self.data).part_1())


if __name__ == '__main__':
    unittest.main()
