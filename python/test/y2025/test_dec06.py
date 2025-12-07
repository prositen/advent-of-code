import unittest

from python.src.y2025.dec06 import Dec06


class TestDec06(unittest.TestCase):
    data = """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  """.splitlines()

    def test_part_1(self):
        self.assertEqual(4277556, Dec06(instructions=self.data).part_1())

    def test_part_2(self):
        self.assertEqual(3263827, Dec06(instructions=self.data).part_2())


if __name__ == '__main__':
    unittest.main()
