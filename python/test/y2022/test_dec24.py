import unittest

from python.src.y2022.dec24 import Dec24


class TestDec24(unittest.TestCase):
    data = """#.######
#>>.<^<#
#.<..<<#
#>v.><>#
#<^v^^>#
######.#""".split('\n')

    def test_part_1(self):
        self.assertEqual(18, Dec24(instructions=self.data).part_1())

    def test_part_2(self):
        self.assertEqual(54, Dec24(instructions=self.data).part_2())
