import re
from python.src.common import Day


class Army(object):
    def __init__(self, name, boost=0):
        self.name = name
        self.groups = list()
        self.enemies = None
        self.selected = list()
        self.boost = boost

    def alive(self):
        return any(g.units > 0 for g in self.groups)

    def add_group(self, group):
        group.army = self
        self.groups.append(group)

    def reset_targets(self):
        self.selected = list()

    def reset_units(self):
        for g in self.groups:
            g.units = g.original_units


class Group(object):
    def __init__(self, units, hp, weaknesses, immunities,
                 attack_damage, attack_type, initiative, index):
        self.units = units
        self.original_units = units
        self.hp = hp
        self.weaknesses = weaknesses
        self.immunities = immunities
        self.attack_damage = attack_damage
        self.attack_type = attack_type
        self.initiative = initiative
        self.target = None
        self.army = None
        self.index = index

    def __repr__(self):
        return '{}: Group {} ({} units)'.format(self.army.name, self.index, self.units)

    def effective_power(self):
        return (self.attack_damage + self.army.boost) * self.units

    def factor(self, attack):
        if attack in self.weaknesses:
            return 2
        elif attack in self.immunities:
            return 0
        else:
            return 1

    def select_target(self):
        enemies = [e for e in self.army.enemies
                   if e.units > 0 and e.index not in self.army.selected]
        if not enemies:
            return None

        enemies.sort(key=lambda e: (self.effective_power() * e.factor(self.attack_type),
                                    e.effective_power(),
                                    e.initiative),
                     reverse=True)
        if self.attack_type in enemies[0].immunities:
            return None
        self.target = enemies[0]
        self.army.selected.append(self.target.index)

    def attack(self):
        if self.units and self.target:
            self.target.damage(self.effective_power(), self.attack_type)
            self.target = None

    def damage(self, power, attack_type):
        power *= self.factor(attack_type)
        killed_units = min(power // self.hp, self.units)
        self.units -= killed_units
        return killed_units


class Battle(object):
    def __init__(self, immune_system, infection):
        self.immune_system = immune_system
        self.infection = infection
        self.immune_system.enemies = self.infection.groups
        self.infection.enemies = self.immune_system.groups

    def reset_battle(self, boost):
        self.immune_system.reset_units()
        self.immune_system.boost = boost
        self.infection.reset_units()

    def groups(self):
        return [group for group in self.immune_system.groups + self.infection.groups
                if group.units > 0]

    def select_targets(self):
        for army in self.immune_system, self.infection:
            army.reset_targets()
        for g in sorted(self.groups(), key=lambda x: (x.effective_power(), x.initiative),
                        reverse=True):
            g.select_target()

    def attack(self):
        for g in sorted(self.groups(), key=lambda x: x.initiative, reverse=True):
            g.attack()

    def fight(self):
        prev_units = []
        units = None
        while self.immune_system.alive() and self.infection.alive() and prev_units != units:
            self.select_targets()
            self.attack()
            prev_units = units
            units = [g.units for g in self.immune_system.groups + self.infection.groups]

        if units == prev_units:
            return 0, False

        return sum(g.units for g in self.groups()), self.immune_system.alive()


class Dec24(Day):

    def __init__(self, instructions=None, filename=None):
        super().__init__(2018, 24, instructions, filename)
        self.battle = Battle(*self.instructions)

    @staticmethod
    def parse_instructions(instructions):
        re_unit = re.compile(r'(\d+) units each with (\d+) hit points (\(.*\) |)with an '
                             r'attack that does (\d+) (\w+) damage at initiative (\d+)')

        immune = Army('Immune system')
        infection = Army('Infection')
        is_immune = True
        index = 1
        for row in instructions[1:]:
            row = row.strip()
            if not len(row):
                is_immune = False
                index = 0
                continue
            u = re_unit.match(row)
            if u:
                i = w = []
                w_i = u.group(3).rstrip(') ').lstrip('(')
                if len(w_i):
                    for w_i in w_i.strip().split(';'):
                        types = [ww.rstrip(', ') for ww in w_i.strip().split(' ')[2:]]
                        if w_i.strip().startswith('immune'):
                            i = types
                        else:
                            w = types
                g = Group(units=int(u.group(1)),
                          hp=int(u.group(2)),
                          weaknesses=w,
                          immunities=i,
                          attack_damage=int(u.group(4)),
                          attack_type=u.group(5),
                          initiative=int(u.group(6)),
                          index=index)
                if is_immune:
                    immune.add_group(g)
                else:
                    infection.add_group(g)
            index += 1
        return immune, infection

    def part_1(self):
        return self.battle.fight()[0]

    def part_2(self):
        boost = 1
        while True:
            self.battle.reset_battle(boost)
            battle_result = self.battle.fight()
            if battle_result[1]:
                return battle_result[0]
            boost += 1


if __name__ == '__main__':
    d = Dec24()
    print('The winning army have {} units left'.format(d.part_1()))
    print('Immune system units left after boost:', d.part_2())
