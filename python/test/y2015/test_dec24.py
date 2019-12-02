from python.src.y2015 import dec24
import unittest


class Dec23Tests(unittest.TestCase):

    def test_quantum_entanglement(self):
        self.assertEqual(99, dec24.quantum_entanglement([11, 9]))

    def test_smallest_group(self):
        self.assertSetEqual({9, 11},
                            set(dec24.smallest_group([1, 2, 3, 4, 5, 7, 8, 9, 10, 11], 3)))

    def test_smallest_group_part_2(self):
        self.assertSetEqual({11, 4},
                            set(dec24.smallest_group([1, 2, 3, 4, 5, 7, 8, 9, 10, 11], 4)))
