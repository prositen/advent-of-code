import unittest

from python.src.y2022.dec21 import Dec21


class TestDec21(unittest.TestCase):
    data = """root: pppw + sjmn
dbpl: 5
cczh: sllz + lgvd
zczc: 2
ptdq: humn - dvpt
dvpt: 3
lfqf: 4
humn: 5
ljgn: 2
sjmn: drzm * dbpl
sllz: 4
pppw: cczh / lfqf
lgvd: ljgn * ptdq
drzm: hmdt - zczc
hmdt: 32""".split('\n')

    def test_part_1(self):
        self.assertEqual(152, Dec21(instructions=self.data).part_1())

    def test_part_2(self):
        self.assertEqual(301, Dec21(instructions=self.data).part_2())
