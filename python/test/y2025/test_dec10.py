import unittest

from python.src.y2025.dec10 import Dec10


class TestDec10(unittest.TestCase):
    data = """[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}""".splitlines()

    def test_part_1(self):
        self.assertEqual(7, Dec10(instructions=self.data).part_1())

    def test_part_2(self):
        self.assertEqual(0, Dec10(instructions=self.data).part_2())


if __name__ == '__main__':
    unittest.main()
