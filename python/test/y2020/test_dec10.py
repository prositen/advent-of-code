import unittest

from python.src.y2020.dec10 import Dec10


class TestDec10(unittest.TestCase):

    def test_part_1_a(self):
        data = [
            "16",
            "10",
            "15",
            "5",
            "1",
            "11",
            "7",
            "19",
            "6",
            "12",
            "4",
        ]
        self.assertEqual(7 * 5, Dec10(instructions=data).part_1())

    def test_part_1_b(self):
        data = """28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3"""
        self.assertEqual(22 * 10, Dec10(instructions=data.splitlines()).part_1())
