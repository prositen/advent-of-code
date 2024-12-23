import unittest

from python.src.y2024.dec23 import Dec23


class TestDec23(unittest.TestCase):
    data = """kh-tc
qp-kh
de-cg
ka-co
yn-aq
qp-ub
cg-tb
vc-aq
tb-ka
wh-tc
yn-cg
kh-ub
ta-co
de-co
tc-td
tb-wq
wh-td
ta-ka
td-qp
aq-cg
wq-ub
ub-vc
de-ta
wq-aq
wq-vc
wh-yn
ka-de
kh-ta
co-tc
wh-qp
tb-vc
td-yn""".splitlines()

    def test_part_1(self):
        self.assertEqual(7, Dec23(instructions=self.data).part_1())

    def test_part_2(self):
        self.assertEqual('co,de,ka,ta', Dec23(instructions=self.data).part_2())


if __name__ == '__main__':
    unittest.main()
