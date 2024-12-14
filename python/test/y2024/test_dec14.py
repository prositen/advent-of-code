import unittest

from python.src.y2024.dec14 import Dec14


class TestDec14(unittest.TestCase):
    data = """p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3""".split('\n')

    def test_part_1(self):
        self.assertEqual(12, Dec14(instructions=self.data).part_1(max_y=7, max_x=11))


if __name__ == '__main__':
    unittest.main()
