from copy import deepcopy


class Character:
    def __init__(self, name, hp=0, mana=0, damage=0):
        self.name = name
        self.hp = hp
        self.mana = mana
        self.damage = damage


class Game:
    def __init__(self, player, boss):
        self.player = player
        self.boss = boss

    @staticmethod
    def from_game(game):
        return deepcopy(game)


class Spell:
    def __init__(self, name, turns):
        pass

    def run(self):
        pass