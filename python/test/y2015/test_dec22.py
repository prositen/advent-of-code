__author__ = 'Anna'

import unittest
from python.src.y2015 import dec22


class Dec21Tests(unittest.TestCase):

    def test_part1_example1(self):
        player = dec22.Character("Player", hp=10, mana=250)
        boss = dec22.Character("Boss", hp=13, damage=8)
        game = dec22.play(player, boss)
        self.assertEquals("Player", game.winner().name)
        self.assertEquals(["Player casts Poison."], game.round(1).message(player=True))
        self.assertEquals(10, game.round(1).boss.hp)
        self.assertEquals({"Poison deals 3 damage; its timer is now 5.",
                           "Boss attacks for 8 damage."}, set(game.round(1).message(player=False)))
        self.assertEquals({"Poison deals 3 damage; its timer is now 4.",
                           "Player casts Magic Missile, dealing 4 damage."}, set(game.round(2).message(player=True)))

    def test_part1_example2(self):
        player = dec22.Character("Player", hp=10, mana=250)
        boss = dec22.Character("Boss", hp=14, damage=8)
        game = dec22.play(player, boss)
        self.assertEquals("Player", game.winner().name)
        self.assertEquals(5, len(game))
        # print('\n'.join(game.replay()))
        self.assertEquals(["Player casts Recharge."], game.round(1).message(player=True))
        self.assertEquals({"Recharge provides 101 mana; its timer is now 4.",
                           "Boss attacks for 8 damage."}, set(game.round(1).message(player=False)))
        self.assertEquals(14, game.round(1).boss.hp)
        self.assertEquals(122, game.round(1).player.mana)
        self.assertEquals({"Player casts Magic Missile, dealing 4 damage.",
                           "Recharge provides 101 mana; its timer is now 2."}, set(game.round(2).message(player=True)))


if __name__ == '__main__':
    unittest.main()
