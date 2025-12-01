import unittest

from python.src.y2025.dec01 import Dec01
from src.y2025.dec01 import Dial0x434C49434B


class TestDec01(unittest.TestCase):
    data = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82""".splitlines()

    def test_part_1(self):
        self.assertEqual(3, Dec01(instructions=self.data).part_1())

    def test_part_2(self):
        self.assertEqual(6, Dec01(instructions=self.data).part_2())

    def test_part_2_mini(self):
        d = Dial0x434C49434B()
        d.rotate(1050, 'L')
        self.assertEqual(11, d.password)

    def test_part_2_2(self):
        d = Dial0x434C49434B()
        d.rotate(50, 'L')
        d.rotate(101, 'R')
        self.assertEqual(2, d.password)


if __name__ == '__main__':
    unittest.main()
