import unittest

from python.src.y2022.dec20 import Dec20


class TestDec20(unittest.TestCase):
    data = """1
2
-3
3
-2
0
4""".split('\n')

    def test_part_1(self):
        self.assertEqual(3, Dec20(instructions=self.data).part_1())

    def test_part_2(self):
        self.assertEqual(1623178306, Dec20(instructions=self.data).part_2())
