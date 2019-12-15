import math
from collections import Counter, deque

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
        self.reactions = {
            r.result.name: (r.result.amount, r.ingredients)
            for r in self.instructions
        }
        self.cost_per_fuel = 0

    def create_fuel(self, fuel_amount=1):
        to_create = deque()
        to_create.append(('FUEL', fuel_amount))
        stock = Counter()
        while to_create:
            chem, needed = to_create.popleft()
            if chem == 'ORE' or stock[chem] >= needed:
                stock[chem] -= needed
            else:
                needed -= stock[chem]
                stock[chem] = 0
                no_created, recipe = self.reactions[chem]
                reps = int(math.ceil(needed / no_created))
                stock[chem] += int(no_created * reps - needed)
                to_create.extend([(c.name, reps * c.amount) for c in recipe])
        return -stock['ORE']

    @staticmethod
    def parse_instructions(instructions):
        return [Reaction(i) for i in instructions]

    def part_1(self):
        self.cost_per_fuel = self.create_fuel(1)
        return self.cost_per_fuel

    def part_2(self):
        goal = 10 ** 12
        usage = goal // self.cost_per_fuel
        low = usage
        high = 2 * low
        while low <= high:
            mid = low + (high - low) // 2
            if self.create_fuel(mid) < goal:
                usage = mid
                low = mid + 1
            else:
                high = mid - 1

        return usage


if __name__ == '__main__':
    d = Dec14()
    print("Part 1", d.part_1())
    print("Part 2", d.part_2())
