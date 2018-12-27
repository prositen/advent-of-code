import unittest

from python.src.y2018.dec25 import Dec25


class TestDec25(unittest.TestCase):

    def test_part_1_case_1(self):
        stars = ["0,0,0,0",
                 "3,0,0,0",
                 "0,3,0,0",
                 "0,0,3,0",
                 "0,0,0,3",
                 "0,0,0,6",
                 "9,0,0,0",
                 "12,0,0,0"
                 ]
        d = Dec25(instructions=stars)
        self.assertEqual(2, d.part_1())

    def test_part_1_case_2(self):
        stars = ["-1,2,2,0",
                 "0,0,2,-2",
                 "0,0,0,-2",
                 "-1,2,0,0",
                 "-2,-2,-2,2",
                 "3,0,2,-1",
                 "-1,3,2,2",
                 "-1,0,-1,0",
                 "0,2,1,-2",
                 "3,0,0,0"]
        self.assertEqual(4, Dec25(instructions=stars).part_1())

    def test_part_1_case_3(self):
        stars = """1,-1,0,1
2,0,-1,0
3,2,-1,0
0,0,3,1
0,0,-1,-1
2,3,-2,0
-2,2,0,0
2,-2,0,-1
1,-1,0,-1
3,2,0,2""".split('\n')
        self.assertEqual(3, Dec25(instructions=stars).part_1())

    def test_part_1_case_4(self):
        stars = """1,-1,-1,-2
-2,-2,0,1
0,2,1,3
-2,3,-2,1
0,2,3,-2
-1,-1,1,-2
0,-2,-1,0
-2,2,3,-1
1,2,2,0
-1,-2,0,-2""".split('\n')
        self.assertEqual(8, Dec25(instructions=stars).part_1())
