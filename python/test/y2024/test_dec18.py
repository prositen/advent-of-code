import unittest

from python.src.y2024.dec18 import Dec18, Computer


class TestDec18(unittest.TestCase):
    data = [(5, 4), (4, 2), (4, 5), (3, 0), (2, 1), (6, 3),
            (2, 4), (1, 5), (0, 6), (3, 3), (2, 6), (5, 1),
            (1, 2), (5, 5), (2, 5), (6, 5), (1, 4), (0, 4),
            (6, 4), (1, 1), (6, 1), (1, 0), (0, 5), (1, 6), (2, 0)]

    def test_part_1(self):
        c = Computer(max_y=7, max_x=7, falling=self.data)
        c.corrupt(12)
        self.assertEqual(22, c.safe_path())

    def test_part_2(self):
        c = Computer(max_y=7, max_x=7, falling=self.data)
        self.assertEqual((6,1), c.bisect(0))

    if __name__ == '__main__':
        unittest.main()
