import unittest

from python.src.y2025.dec03 import Dec03


class TestDec03(unittest.TestCase):
    data = """987654321111111
811111111111119
234234234234278
818181911112111""".split('\n')

    def test_part_1(self):
        self.assertEqual(357, Dec03(instructions=self.data).part_1())

    def test_part_2(self):
        self.assertEqual(3121910778619, Dec03(instructions=self.data).part_2())


if __name__ == '__main__':
    unittest.main()
