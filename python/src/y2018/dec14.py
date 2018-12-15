from python.src.common import Day


class Dec14(Day):

    def __init__(self, instructions=None):
        super().__init__(2018, 14, instructions)

    def cook(self, elf_1_pos, elf_2_pos, recipe_scores):
        s1 = recipe_scores[elf_1_pos]
        s2 = recipe_scores[elf_2_pos]
        new_recipe = s1 + s2
        if new_recipe > 9:
            recipe_scores.append(1)
            new_recipe -= 10
        recipe_scores.append(new_recipe)
        return (elf_1_pos + 1 + s1) % len(recipe_scores), (elf_2_pos + 1 + s2) % len(recipe_scores)

    def part_1(self):
        recipe_scores = [3, 7]
        elf_1_pos = 0
        elf_2_pos = 1
        num_recipes = int(self.instructions)
        while len(recipe_scores) < num_recipes + 10:
            elf_1_pos, elf_2_pos = self.cook(elf_1_pos, elf_2_pos, recipe_scores)

        return ''.join(str(score) for score in recipe_scores[num_recipes:num_recipes + 10])

    def part_2(self):
        recipe_scores = [3, 7]
        elf_1_pos = 0
        elf_2_pos = 1
        s = ', '.join(c for c in str(self.instructions))  # "5, 1, 5, 8, 9"
        sl = len(s)
        while s not in str(recipe_scores[-sl - 2:]):
            elf_1_pos, elf_2_pos = self.cook(elf_1_pos, elf_2_pos, recipe_scores)

        return (str(recipe_scores).find(s) - 1) // 3  # skip leading [. Each digit needs 3 chars (, and blank)


if __name__ == '__main__':
    d = Dec14(instructions="290431")
    print("Recipe score:", d.part_1())
    print("Recipes to the left of input:", d.part_2())
