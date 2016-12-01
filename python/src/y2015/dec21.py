from itertools import product


class Item(object):
    name = None
    cost = 0
    damage = 0
    armor = 0

    def __init__(self, name, cost, damage, armor):
        self.name = name
        self.cost = cost
        self.damage = damage
        self.armor = armor

    def __repr__(self):
        return "{0}: cost {1}, damage {2}, armor {3}".format(self.name, self.cost, self.damage, self.armor)


Weapons = [
    Item("Dagger", 8, 4, 0),
    Item("Shortsword", 10, 5, 0),
    Item("Warhammer", 25, 6, 0),
    Item("Longsword", 40, 7, 0),
    Item("Greataxe", 74, 8, 0)
]

Armor = [
    Item("No armor", 0, 0, 0),
    Item("Leather", 13, 0, 1),
    Item("Chainmail", 31, 0, 2),
    Item("Splintmail", 53, 0, 3),
    Item("Bandedmail", 75, 0, 4),
    Item("Platemail", 102, 0, 5)
]

Rings = [
    Item("No ring", 0, 0, 0),
    Item("Damage +1", 25, 1, 0),
    Item("Damage +2", 50, 2, 0),
    Item("Damage +3", 100, 3, 0),
    Item("Defense +1", 20, 0, 1),
    Item("Defense +2", 40, 0, 2),
    Item("Defense +3", 80, 0, 3)
]


class Character(object):
    name = None
    hp = 0
    damage = 0
    armor = 0

    def __init__(self, name, hp, damage, armor):
        self.name = name
        self.hp = hp
        self.current_hp = hp
        self.damage = damage
        self.armor = armor

    def reset_hp(self):
        self.current_hp = self.hp

    def hit(self, damage, debug=False):
        self.current_hp -= max(1, damage - self.armor)
        if debug:
            print("{0} was hit for {1} ({3} after armor), remaining HP {2}".format(self.name, damage, self.current_hp,
                                                                                   max(1, damage - self.armor)))

    def alive(self):
        return self.current_hp > 0

    def __repr__(self):
        return "{0}  HP {1}/{2}, Damage {3}, Armor {4}".format(self.name, self.current_hp, self.hp, self.damage,
                                                               self.armor)


def fight(player, boss, debug=False):
    if debug:
        print("---")
    while player.alive() and boss.alive():
        boss.hit(player.damage)
        if not boss.alive():
            return True
        player.hit(boss.damage)
        if not player.alive():
            return False


def find_best_equipment():
    equipment = filter(lambda x: (x[2].cost == 0) or (x[2] != x[3]), product(Weapons, Armor, Rings, Rings))

    won_games = filter(lambda e: fight(Character('Player', 100, sum([x.damage for x in e]), sum([x.armor for x in e])),
                                       Character("Boss", 104, 8, 1)),
                       equipment)

    return min([sum([x.cost for x in eq]) for eq in won_games])


def find_worst_equipment():
    equipment = filter(lambda x: (x[2].cost == 0) or (x[2] != x[3]), product(Weapons, Armor, Rings, Rings))
    won_games = filter(
        lambda e: not fight(Character('Player', 100, sum([x.damage for x in e]), sum([x.armor for x in e])),
                            Character("Boss", 104, 8, 1)),
        equipment)

    return max([sum([x.cost for x in eq]) for eq in won_games])


if __name__ == '__main__':
    print("Cheapest equipment to win the game: ", find_best_equipment())
    print("Priciest equipment to lose the game: ", find_worst_equipment())
