from python.src.common import Day, timer, Timer


class Dec21(Day, year=2020, day=21):

    def __init__(self, instructions=None, filename=None):
        super().__init__(instructions=instructions, filename=filename)
        self.foods = self.instructions
        self.allergens = dict()
        self.non_allergens = set()
        self.find_allergens_in_ingredients()

    @staticmethod
    def parse_instructions(instructions):
        foods = list()
        for line in instructions:
            ingredients, allergens = line.split(' (contains ')
            ingredients = ingredients.split(' ')
            allergens = allergens[:-1].split(', ')
            foods.append((ingredients, allergens))
        return foods

    def find_allergens_in_ingredients(self):
        for (ingredients, allergens) in self.foods:
            self.non_allergens.update(ingredients)
            for allergen in allergens:
                if allergen not in self.allergens:
                    self.allergens[allergen] = set(ingredients)
                else:
                    self.allergens[allergen].intersection_update(ingredients)

        for k, v in self.allergens.items():
            self.non_allergens.difference_update(v)

    def match_allergens_to_ingredients(self):
        allergens = dict()
        items = list(sorted(self.allergens.items(), key=lambda x: len(x[1])))
        while items:
            allergen, ingredients = items.pop(0)
            ingredients.difference_update(allergens.values())
            if len(ingredients) == 1:
                allergens[allergen] = ingredients.pop()
            else:
                items.append((allergen, ingredients))
        self.allergens = allergens

    @timer(part=1)
    def part_1(self):
        return sum(len(self.non_allergens.intersection(i)) for (i, v) in self.foods)

    @timer(part=2)
    def part_2(self):
        self.match_allergens_to_ingredients()
        return ','.join(v for k, v in sorted(self.allergens.items()))


if __name__ == '__main__':
    with Timer('Allergen Assessment'):
        Dec21().run_day()
