from python.src.y2015 import dec14

__author__ = 'anna'

import unittest


class Dec14Tests(unittest.TestCase):
    reindeer_rules = ['Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.',
                      'Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.']

    def test_winner(self):
        winner = dec14.winner(self.reindeer_rules, 1000)
        self.assertEqual('Comet', winner.name)
        self.assertEqual(1120, winner.location)

    def test_winning_ticks(self):
        winner = dec14.winner_ticks(self.reindeer_rules, 1000)
        self.assertEqual('Dancer', winner.name)
        self.assertEqual(689, winner.score)


if __name__ == '__main__':
    unittest.main()
