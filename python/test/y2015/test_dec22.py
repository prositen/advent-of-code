__author__ = 'Anna'

import unittest
from python.src.y2015 import dec22


class Dec21Tests(unittest.TestCase):
    def test_part1_example1(self):
        player = dec22.Character("Player", hp=10, mana=250)
        boss = dec22.Character("Boss", hp=13, damage=8)
        game = dec22.play(player, boss)
        self.assertTrue(game.boss.dead())
        self.assertEqual(226, game.player.spent)

    def test_part1_example2(self):
        player = dec22.Character("Player", hp=10, mana=250)
        boss = dec22.Character("Boss", hp=14, damage=8)
        game = dec22.play(player, boss)
        self.assertTrue(game.boss.dead())
        self.assertEqual(641, game.player.spent)


if __name__ == '__main__':
    unittest.main()
