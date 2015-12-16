import re

__author__ = 'anna'


class CookieProperties(object):
    def __init__(self):
        self.capacity = 0
        self.durability = 0
        self.flavor = 0
        self.texture = 0
        self.calories = 0


class Ingredient(CookieProperties):
    RE_INGREDIENT = \
        re.compile(r'(\w+): capacity (-?\d+), durability (-?\d+), flavor (-?\d+), texture (-?\d+), calories (-?\d+)')

    def __init__(self, line):
        super(Ingredient, self).__init__()
        result = re.match(self.RE_INGREDIENT, line)
        if result:
            self.name = result.group(1)
            self.capacity = int(result.group(2))
            self.durability = int(result.group(3))
            self.flavor = int(result.group(4))
            self.texture = int(result.group(5))
            self.calories = int(result.group(6))
        else:
            raise ValueError('Wrong format for ingredient: ', line)


class Recipe(CookieProperties):

    def __init__(self, ingredients):
        super(Recipe, self).__init__()
        self.score = 0
        self.ingredients = ingredients
        self.measurements = dict()

    def measure(self, measurements):
        self.measurements.clear()
        self.measurements.update(measurements)
        for key, value in self.measurements.items():
            ingredient = self.ingredients[key]
            teaspoons = value
            self.capacity += ingredient.capacity * teaspoons
            self.durability += ingredient.durability * teaspoons
            self.flavor += ingredient.flavor * teaspoons
            self.texture += ingredient.texture * teaspoons
            self.calories += ingredient.calories * teaspoons
        self.score = max(self.capacity, 0) * max(self.durability, 0) * max(self.flavor, 0) * max(self.texture, 0)


def next_measure(ingredients, teaspoons, tail=None):
    current = ingredients[0]
    if len(ingredients) == 1:
        tail[current.name] = teaspoons
        yield tail
    else:
        for m in range(teaspoons):
            if tail is None:
                tail = dict()
            tail[current.name] = m+1
            for x in next_measure(ingredients[1:], teaspoons-m-1, tail):
                yield x


def best_recipe(ingredient_lines, teaspoons, calories=None):
    ingredients = dict()
    for i in ingredient_lines:
        ingredient = Ingredient(i)
        ingredients[ingredient.name] = ingredient

    all_recipes = list()
    for x in next_measure(list(ingredients.values()), teaspoons):
        r = Recipe(ingredients)
        r.measure(x)
        all_recipes.append(r)
    if calories:
        all_recipes = filter(lambda k: k.calories <= 500, all_recipes)
    best = max(all_recipes, key=lambda k: k.score)
    return best


def main():
    with open('../../data/input.15.txt', 'r') as fh:
        result = best_recipe(fh.readlines(), 100)
        print("The best score possible is {score} "
              "using measurements {measurements}".format(score=result.score,
                                                         measurements=result.measurements))
        fh.seek(0)
        result = best_recipe(fh.readlines(), 100, calories=500)
        print("With a calorie limit of 500, the best score is {score} "
              "using measurements {measurements}".format(score=result.score,
                                                         measurements=result.measurements))

if __name__ == '__main__':
    main()
