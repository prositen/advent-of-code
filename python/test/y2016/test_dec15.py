#!/usr/bin/python
import unittest

from python.src.y2016 import dec15


class Dec15Tests(unittest.TestCase):
    def test_disc_from_string(self):
        discs = [dec15.Disc.from_string(x)
                 for x in ["Disc #1 has 5 positions; at time=0, it is at position 4.",
                           "Disc #2 has 2 positions; at time=0, it is at position 1."]]
        self.assertEqual(5, discs[0].no_positions)
        self.assertEqual(1, discs[1].start_position)

    def test_disc_position(self):
        disc1 = dec15.Disc(1, 5, 4)
        disc2 = dec15.Disc(2, 2, 1)
        self.assertEqual(0, disc1.position_at_time(1))
        self.assertEqual(1, disc2.position_at_time(2))

    def test_sequence_ok(self):
        disc1 = dec15.Disc(1, 5, 4)
        disc2 = dec15.Disc(2, 2, 1)

        self.assertTrue(dec15.sequence_ok(5,
                                          [disc1, disc2]))


if __name__ == '__main__':
    unittest.main()
