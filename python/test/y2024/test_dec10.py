import unittest

from python.src.y2024.dec10 import Dec10


class TestDec10(unittest.TestCase):
    data = [
    ]

    def test_part_1(self):
        self.assertEqual(0, Dec10(instructions=self.data).part_1())

    def test_part_2(self):
        self.assertEqual(0, Dec10(instructions=self.data).part_2())


if __name__ == '__main__':
    unittest.main()
