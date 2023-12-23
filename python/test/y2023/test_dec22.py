import unittest

from python.src.y2023.dec22 import Dec22


class TestDec22(unittest.TestCase):
    data = [
        "1,0,1~1,2,1",
        "0,0,2~2,0,2",
        "0,2,3~2,2,3",
        "0,0,4~0,2,4",
        "2,0,5~2,2,5",
        "0,1,6~2,1,6",
        "1,1,8~1,1,9"
    ]

    def test_part_1(self):
        self.assertEqual(5, Dec22(instructions=self.data).part_1())

    def test_part_2(self):
        self.assertEqual(7, Dec22(instructions=self.data).part_2())


if __name__ == '__main__':
    unittest.main()
