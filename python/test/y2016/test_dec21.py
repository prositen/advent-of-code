#!/usr/bin/python
import unittest

from python.src.y2016 import dec21


class Dec21Tests(unittest.TestCase):
    def test_swap_position(self):
        self.assertEqual('ebcda', dec21.Scrambler.swap_position('abcde', (0, 4)))

    def test_swap_letter(self):
        self.assertEqual('badda', dec21.Scrambler.swap_letter('dabba', ('b', 'd')))

    def test_rotate_left(self):
        self.assertEqual('abcd', dec21.Scrambler.rotate_left('dabc', (1,)))

    def test_rotate_right(self):
        self.assertEqual('cdab', dec21.Scrambler.rotate_right('abcd', (2,)))

    def test_reverse_positions(self):
        self.assertEqual('aedcb', dec21.Scrambler.reverse('abcde', (1, 4)))

    def test_part_1(self):
        self.assertEqual('decab',
                         dec21.scramble_password('abcde',
                                                 ['swap position 4 with position 0',
                                                  'swap letter d with letter b',
                                                  'reverse positions 0 through 4',
                                                  'rotate left 1 step',
                                                  'move position 1 to position 4',
                                                  'move position 3 to position 0',
                                                  'rotate based on position of letter b',
                                                  'rotate based on position of letter d']))

    def test_part_2(self):
        """ Not using the same example as above, since that has two solutions """
        self.assertEqual('abcde',
                         dec21.unscramble_password('ecabd',
                                                   ['swap position 4 with position 0',
                                                    'swap letter d with letter b',
                                                    'reverse positions 0 through 4',
                                                    'rotate left 1 step',
                                                    'move position 1 to position 4',
                                                    'move position 3 to position 0',
                                                    'rotate based on position of letter b']))


if __name__ == '__main__':
    unittest.main()
