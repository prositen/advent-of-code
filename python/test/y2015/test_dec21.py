__author__ = 'Anna'

import unittest
from python.src.y2015 import dec21


class Dec21Tests(unittest.TestCase):
    def test_part1(self):
        player = dec21.Character("Player", 8, 5, 5)
        boss = dec21.Character("Boss", 12, 7, 2)
        self.assertTrue(dec21.fight(player, boss))


if __name__ == '__main__':
    unittest.main()
