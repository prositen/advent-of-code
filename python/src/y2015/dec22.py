from collections import deque
from copy import deepcopy


class Character(object):
    def __init__(self, name, hp=0, mana=0, damage=0):
        self.name = name
        self.hp = hp
        self.mana = mana
        self.damage = damage
        self.armor = 0
        self.spent = 0

    def cast(self, spell, boss):
        self.mana -= spell.mana
        self.spent += spell.mana
        return spell.cast(self, boss)

    def dead(self):
        return self.hp <= 0

    def __repr__(self):
        return "<Character {0} hp={1} mana={2} damage={3} armor={4} spent={5}>".format(self.name,
                                                                                       self.hp,
                                                                                       self.mana,
                                                                                       self.damage,
                                                                                       self.armor,
                                                                                       self.spent)


class Spell(object):
    name = "Spell"
    mana = 0
    turns = None

    def run(self, player, boss):
        pass

    def cast(self, player, boss):
        return "Player casts {0}.".format(self.name)

    def expire(self, player):
        if self.turns is not None:
            return "{0} wears off.".format(self.name)

    def __eq__(self, other):
        return self.name == other.name

    def __repr__(self):
        return "<{0} turns={1}>".format(self.name, self.turns)


class MagicMissile(Spell):
    name = "Magic Missile"
    mana = 53
    turns = None

    def cast(self, player, boss):
        boss.hp -= 4
        return super(MagicMissile, self).cast(player, boss)[:-1] + ", dealing 4 damage."


class Drain(Spell):
    name = "Drain"
    mana = 73
    turns = None

    def cast(self, player, boss):
        boss.hp -= 2
        player.hp += 2
        return "Player casts Drain, dealing 2 damage, and healing 2 hit points."


class Shield(Spell):
    name = "Shield"
    mana = 113
    turns = 6

    def run(self, player, boss):
        self.turns -= 1
        if self.turns == 0:
            player.armor = 0
        return "Shield's timer is now {0}".format(self.turns)

    def expire(self, player):

        return super(Shield, self).expire(player)[:-1] + ", decreasing armor by 7."

    def cast(self, player, boss):
        player.armor = 7
        return super(Shield, self).cast(player, boss)[:-1] + ", increasing armor by 7."


class Poison(Spell):
    name = "Poison"
    mana = 173
    turns = 6

    def run(self, player, boss):
        boss.hp -= 3
        self.turns -= 1
        return "Poison deals 3 damage; its timer is now {0}.".format(self.turns)


class Recharge(Spell):
    name = "Recharge"
    mana = 229
    turns = 5

    def run(self, player, boss):
        player.mana += 101
        self.turns -= 1
        return "Recharge provides 101 mana; its timer is now {0}.".format(self.turns)


class Hardmode(Spell):
    name = "Hard"

    def run(self, player, boss):
        player.hp -= 1
        return "Player takes 1 in damage due to hard mode"


SPELLS = [Shield, Recharge, Poison, Drain, MagicMissile]


class Turn(object):
    def __init__(self, player, boss, hard):
        self.player = player
        self.boss = boss
        self.effects = None
        self.game_id = 0
        self.hard = hard

    nid = 0

    @staticmethod
    def next_id():
        Turn.nid += 1
        return Turn.nid

    gid = 0

    @staticmethod
    def next_game_id():
        Turn.gid += 1
        return Turn.gid

    def next_moves(self):
        moves = []
        if self.effects is None:
            self.effects = []
        for spell in SPELLS:
            can_afford = self.player.mana >= spell.mana

            if spell in self.effects:
                not_running = self.effects[self.effects.index(spell)].turns == 1
            else:
                not_running = True

            if not_running and can_afford:
                move = deepcopy(self)
                move.effects.append(spell())
                moves.append(move)
        return moves

    def debug_print(self, message):
        if fh:
            print(message, file=fh)

    def run(self):
        self.status("Player")

        if self.hard:
            hurt = Hardmode()
            self.debug_print(hurt.run(self.player, self.boss))
            if self.player.dead():
                self.debug_print("This kills the player, and the boss wins")
                return

        to_cast = self.effects[-1]
        for spell in self.effects[:-1]:
            self.debug_print(spell.run(self.player, self.boss))
            if self.boss.dead():
                self.debug_print("This kills the boss, and the player wins")
                return

        self.debug_print(self.player.cast(to_cast, self.boss))
        if self.boss.dead():
            self.debug_print("This kills the boss, and the player wins")
            return

        self.update_spells()

        self.status("Boss")

        for spell in self.effects:
            self.debug_print(spell.run(self.player, self.boss))

        self.update_spells()
        if self.boss.dead():
            self.debug_print("This kills the boss, and the player wins")
        else:
            damage = max(1, self.boss.damage - self.player.armor)
            self.player.hp -= damage
            if damage < self.boss.damage:
                self.debug_print("Boss attacks for {0} - {1} = {2} damage.".format(self.boss.damage,
                                                                                   self.player.armor,
                                                                                   damage))
            else:
                self.debug_print("Boss attacks for {0} damage.".format(self.boss.damage))
            if self.player.dead():
                self.debug_print("This kills the player, and the boss wins.")

    def update_spells(self):
        new_effects = []
        for spell in self.effects:
            if spell.turns:
                new_effects.append(spell)
            else:
                self.debug_print(spell.expire(self.player))
        self.debug_print("Effects: {}".format(", ".join(spell.name for spell in self.effects)))
        self.effects = new_effects

    def status(self, header):
        if fh:
            print("-- {0} turn {1}--".format(header, self.game_id), file=fh)
            print("- Player has {0} hit points, {1} armor, {2} mana".format(self.player.hp,
                                                                            self.player.armor,
                                                                            self.player.mana), file=fh)
            print("- Boss has {0} hit points".format(self.boss.hp), file=fh)


def play(player, boss, hard_mode=False):
    moves = deque()
    moves.extend((next_move, 0) for next_move in Turn(player, boss, hard_mode).next_moves())
    games = []
    cheapest_found = 999999

    while moves:
        move, path = moves.popleft()
        next_path = path + 1
        move.run()
        # print(len(moves), next_path, move.player.spent)
        if move.boss.dead() or move.player.dead():
            if move.boss.dead():
                games.append(move)
                cheapest_found = min(cheapest_found, move.player.spent)
        else:
            # DFS instead of BFS to decrease memory requirements. At least I'm pruning the search space
            # a bit by only considering paths cheaper than the ones I've already found.
            if move.player.spent < cheapest_found:
                moves.extendleft([(next_move, next_path) for next_move in move.next_moves()][::-1])

    return min(games, key=lambda x: x.player.spent)

fh = None
if __name__ == '__main__':

    winning_game = play(Character('Player', hp=50, mana=500),
                        Character('Boss', hp=71, damage=10))
    print("Part 1: Smallest mana cost is", winning_game.player.spent)

    hard_winning_game = play(Character('Player', hp=50, mana=500),
                             Character('Boss', hp=71, damage=10),
                             hard_mode=True)
    print("Part 2: Smallest mana cost is", hard_winning_game.player.spent)
