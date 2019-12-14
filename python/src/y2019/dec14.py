from collections import Counter

from python.src.common import Day


class Ingredient(object):
    def __init__(self, s):
        s = s.strip()
        i = s.index(' ')
        self.amount = int(s[:i])
        self.name = s[i + 1:]

    def __repr__(self):
        return '{} {}'.format(self.amount, self.name)


class Reaction(object):
    def __init__(self, row):
        ingredients, result = row.split('=>')
        self.ingredients = [Ingredient(i) for i in ingredients.split(',')]
        self.result = Ingredient(result)


class Dec14(Day):
    def __init__(self, filename=None, instructions=None):
        super().__init__(2019, 14, instructions, filename)
        self.least_cost = 0
        self.reactions = {
            r.result.name: (r.result.amount, r.ingredients)
            for r in self.instructions
        }
        self._needs = Counter()
        self.ore = 1000000000000
        self._chems = Counter({'ORE': self.ore})

    @staticmethod
    def parse_instructions(instructions):
        return [Reaction(i) for i in instructions]

    def add_chem(self, chem, amount):
        self._chems[chem] += amount
        self._needs[chem] = False

    def take_chem(self, chem, amount):
        self._chems[chem] -= amount

    def has_chem(self, chem, amount):
        return self._chems[chem] >= amount

    def needs(self, chem):
        return self._needs.get(chem)

    def try_create(self, chem, amount, cost):
        can_create = True
        for c in cost:
            if not self.has_chem(c.name, c.amount):
                self._needs[c.name] = True
                can_create = False
        if can_create:
            for c in cost:
                self.take_chem(c.name, c.amount)
            self.add_chem(chem, amount)

    def part_1(self, needs=1):
        while needs > 0:
            self._needs['FUEL'] = True
            while self.needs('FUEL'):
                for chem, (amount, cost) in self.reactions.items():
                    if self.needs(chem):
                        self.try_create(chem, amount, cost)
            needs -= 1
        if not self.least_cost:
            self.least_cost = self.ore - self._chems['ORE']
        return self.least_cost

    def part_2(self):
        ore1 = self.least_cost
        goal = 1000 ** 4
        maxfuel = goal // ore1
        l = maxfuel
        r = maxfuel * 2
        while l <= r:
            mid = l + (r - l) // 2
            if self.part_1(mid) < goal:
                maxfuel = mid
                l = mid + 1
            else:
                r = mid - 1

        return maxfuel


if __name__ == '__main__':
    d = Dec14()
    print("Part 1", d.part_1())
    print("Part 2", d.part_2())