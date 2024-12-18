import unittest

from python.src.y2024.dec17 import Dec17


class TestDec17(unittest.TestCase):
    data = """Register A: 729
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0""".split('\n')

    def test_part_1(self):
        self.assertEqual('4,6,3,5,6,3,5,2,1,0', Dec17(instructions=self.data).part_1())

    def test_part_2(self):
        data = """Register A: 2024
Register B: 0
Register C: 0

Program: 0,3,5,4,3,0""".split('\n')
        self.assertEqual(117440, Dec17(instructions=data).part_2())

    def test_part_2_challenge(self):
        data = """Register A: 12345678
Register B: 0
Register C: 0

Program: 2,4,1,0,7,5,1,5,0,3,4,5,5,5,3,0 
""".split('\n')
        self.assertEqual(202797954918051, Dec17(instructions=data).part_2())


if __name__ == '__main__':
    unittest.main()
