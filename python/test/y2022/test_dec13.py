import unittest

from python.src.y2022.dec13 import Dec13


class TestDec13(unittest.TestCase):
    data = """[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]""".split('\n')

    def test_part_1(self):
        self.assertEqual(13, Dec13(instructions=self.data).part_1())


    def test_part_2(self):
        self.assertEqual(140, Dec13(instructions=self.data).part_2())
