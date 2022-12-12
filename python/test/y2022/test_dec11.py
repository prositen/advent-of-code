import unittest

from python.src.y2022.dec11 import Dec11


class TestDec11(unittest.TestCase):
    data = """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1""".split('\n')

    def test_part_1(self):
        self.assertEqual(10605, Dec11(instructions=self.data).part_1())

    def test_part_2(self):
        self.assertEqual(2713310158, Dec11(instructions=self.data).part_2())
