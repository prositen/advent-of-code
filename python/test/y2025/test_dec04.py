import unittest

from python.src.y2025.dec04 import Dec04


class TestDec04(unittest.TestCase):
    data = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.""".splitlines()

    def test_part_1(self):
        self.assertEqual(13, Dec04(instructions=self.data).part_1())

    def test_part_2(self):
        self.assertEqual(43, Dec04(instructions=self.data).part_2())


if __name__ == '__main__':
    unittest.main()
