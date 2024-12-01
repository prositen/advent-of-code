import unittest

from python.src.y2022.dec18 import Dec18


class TestDec18(unittest.TestCase):
    data = """2,2,2
1,2,2
3,2,2
2,1,2
2,3,2
2,2,1
2,2,3
2,2,4
2,2,6
1,2,5
3,2,5
2,1,5
2,3,5""".split('\n')

    def test_part_1(self):
        self.assertEqual(64, Dec18(instructions=self.data).part_1())

    def test_part_2(self):
        self.assertEqual(58, Dec18(instructions=self.data).part_2())
