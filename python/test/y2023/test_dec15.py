import unittest

from python.src.y2023.dec15 import Dec15


class TestDec15(unittest.TestCase):
    data = ['rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7']

    def test_part_1(self):
        cases = (
            (['HASH'], 52),
            (self.data, 1320)
        )
        for test, expected in cases:
            self.assertEqual(expected, Dec15(instructions=test).part_1())

    def test_part_2(self):
        self.assertEqual(145, Dec15(instructions=self.data).part_2())


if __name__ == '__main__':
    unittest.main()
