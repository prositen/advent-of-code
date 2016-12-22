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
        return "{0} wears off".format(self.name)

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
        player.armor = 7
        self.turns -= 1
        return "Shield's timer is now {0}".format(self.turns)

    def expire(self, player):
        player.armor = 0
        return super(Shield, self).expire(player)[:-1] + ", decreasing armor by 7."

    def cast(self, player, boss):
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


SPELLS = [MagicMissile, Drain, Shield, Poison, Recharge]


class Turn(object):
    def __init__(self, player, boss):
        self.player = player
        self.boss = boss
        self.effects = []
        self.player_messages = []
        self.boss_messages = []
        self.player_status = []
        self.boss_status = []

    @staticmethod
    def from_turn(turn):
        new_turn = deepcopy(turn)
        new_turn.player_messages = []
        new_turn.boss_messages = []
        new_turn.player.armor = 0
        return new_turn

    def next_moves(self):
        moves = []
        for spell in SPELLS:
            if spell not in self.effects and self.player.mana > spell.mana:
                move = Turn.from_turn(self)
                move.effects.append(spell())
                moves.append(move)
        return moves

    def run_player(self):
        to_cast = self.effects[-1]

        for spell in self.effects[:-1]:
            self.player_messages.append(spell.run(self.player, self.boss))
            if self.boss.dead():
                self.player_messages.append("This kills the boss, and the player wins")
                return

        self.player_status = self.status("Player")
        self.player_messages.append(self.player.cast(to_cast, self.boss))
        if self.boss.dead():
            self.player_messages.append("This kills the boss, and the player wins")
        else:
            self.update_spells(True)

    def update_spells(self, player):
        new_effects = []
        for spell in self.effects:
            if spell.turns is not None:
                if spell.turns > 0:
                    new_effects.append(spell)
                else:
                    message = spell.expire(self.player)
                    if player:
                        self.player_messages.append(message)
                    else:
                        self.boss_messages.append(message)
        self.effects = new_effects

    def status(self, header):
        return ["-- {0} turn --".format(header),
                "- Player has {0} hit points, {1} armor, {2} mana".format(self.player.hp,
                                                                          self.player.armor,
                                                                          self.player.mana),
                "- Boss has {0} hit points".format(self.boss.hp)]

    def run_boss(self):
        self.boss_status = self.status("Boss")
        for spell in self.effects:
            self.boss_messages.append(spell.run(self.player, self.boss))
        self.update_spells(False)
        if self.boss.dead():
            self.boss_messages.append("This kills the boss, and the player wins")
        else:
            damage = max(1, self.boss.damage - self.player.armor)
            self.player.hp -= damage
            if damage < self.boss.damage:
                self.boss_messages.append("Boss attacks for {0} - {1} = {2} damage.".format(self.boss.damage,
                                                                                            self.player.armor,
                                                                                            damage))
            else:
                self.boss_messages.append("Boss attacks for {0} damage.".format(self.boss.damage))
            if self.player.dead():
                self.boss_messages.append("This kills the player, and the boss wins.")

    def message(self, player):
        if player:
            return self.player_messages
        else:
            return self.boss_messages

    def replay(self):
        r = self.player_status
        r.extend(self.message(True))
        r.extend(self.boss_status)
        r.extend(self.message(False))
        return r


class Game(object):
    def __init__(self, path):
        self.path = path
        self.last_move = path[-1]

    def __len__(self):
        return len(self.path)

    def round(self, no):
        return self.path[no - 1]

    def winner(self):
        return self.last_move.player if self.last_move.boss.dead() else self.last_move.boss

    def cost(self):
        return self.last_move.player.spent

    def replay(self):
        r = ["Total spend: {}".format(self.cost()),
             '-' * 50]
        for x in self.path:
            r.extend(x.replay())
        r.append('-' * 50)
        return r


def play(player, boss):
    moves = deque()
    moves.extend((next_move, []) for next_move in Turn(player, boss).next_moves())
    games = []
    while moves:
        move, path = moves.popleft()
        next_path = path + [move]
        move.run_player()
        if move.boss.dead() or move.player.dead():
            games.append(Game(next_path))
        else:
            move.run_boss()
            if move.boss.dead() or move.player.dead():
                games.append(Game(next_path))
            else:
                next_moves = [(next_move, next_path) for next_move in move.next_moves()]
                moves.extendleft(next_moves)

    winning_games = [game for game in games if game.winner().name == "Player"]
    winning_games.sort(key=lambda x: x.cost())


    with open('derp.txt', 'w') as fh:
        for i, game in enumerate(games):
            print("Game ", i, file=fh)
            # print('\n'.join(game.replay()), file=fh)
            print("Moves", len(game), file=fh)
            print("Winner", game.winner().name, file=fh)

    return winning_games[0]

if __name__ == '__main__':
    winning_game = play(Character('Player', hp=50, mana=500),
                        Character('Boss', hp=71, damage=10))
    print("Smallest mana cost is", winning_game.cost())

