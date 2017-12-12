import unittest

from python.src.y2017 import dec12


class TestDigitalPlumber(unittest.TestCase):

    def test_find_groups(self):
        puzzle_input = ["0 <-> 2",
                        "1 <-> 1",
                        "2 <-> 0, 3, 4",
                        "3 <-> 2, 4",
                        "4 <-> 2, 3, 6",
                        "5 <-> 6",
                        "6 <-> 4, 5"]

        groups = dec12.find_groups(puzzle_input)
        self.assertEqual(6, len(groups.get(0)))
        self.assertEqual(2, dec12.count_groups(groups))
        self.assertSetEqual({0, 2, 3, 4, 5, 6}, groups.get(0))

