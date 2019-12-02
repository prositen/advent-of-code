from python.src.common import Day


class Dec18(Day):
    """
    - An open acre will become filled with trees if three or more adjacent
      acres contained trees.
      Otherwise, nothing happens.
    - An acre filled with trees will become a lumberyard if three or more adjacent
      acres were lumberyards.
      Otherwise, nothing happens.
    - An acre containing a lumberyard will remain a lumberyard if it was adjacent to at least
      one other lumberyard and at least one acre containing trees. Otherwise, it becomes open.
"""

    OPEN = '.'
    TREE = '|'
    LUMBERYARD = '#'

    def __init__(self, instructions=None, filename=None):
        super().__init__(2018, 18, instructions, filename)
        self.grid = [[x for x in y] for y in self.instructions]
        self.maxy = len(self.grid)
        self.maxx = len(self.grid[0])
        self.rules = {
            self.OPEN: (lambda adj: adj.count(self.TREE) >= 3, self.TREE),
            self.TREE: (lambda adj: adj.count(self.LUMBERYARD) >= 3, self.LUMBERYARD),
            self.LUMBERYARD: (lambda adj: (adj.count(self.TREE) == 0 or
                                           adj.count(self.LUMBERYARD) == 0),
                              self.OPEN)
        }

    @staticmethod
    def parse_instructions(instructions):
        return [
            [c for c in row.strip()]
            for row in instructions
        ]

    def adjacent(self, x, y):
        return [self.grid[yy][xx]
                for yy, xx in
                [(y - 1, x - 1), (y - 1, x), (y - 1, x + 1),
                 (y, x - 1), (y, x + 1),
                 (y + 1, x - 1), (y + 1, x), (y + 1, x + 1)]
                if 0 <= yy < self.maxy and 0 <= xx < self.maxx]

    def step(self):
        new_grid = [[x for x in y] for y in self.grid]
        for y in range(self.maxy):
            for x in range(self.maxx):
                adj = self.adjacent(x, y)
                acre = self.grid[y][x]
                rule = self.rules[acre]
                new_grid[y][x] = rule[1] if rule[0](adj) else self.grid[y][x]
        self.grid = [[x for x in y] for y in new_grid]

    def run(self, minutes):
        for _ in range(minutes):
            self.step()
        trees = 0
        lumberyards = 0
        for y in self.grid:
            trees += y.count(self.TREE)
            lumberyards += y.count(self.LUMBERYARD)
        return trees * lumberyards

    def part_1(self):
        return self.run(10)

    def part_2(self):
        self.grid = [[x for x in y] for y in self.instructions]
        generations = 1000000000
        scores = list()
        score = 0
        while True:
            prev_score = score
            score = self.run(1)
            if score in scores:
                si = scores.index(score)
                if scores[si - 1] == prev_score:
                    cycle_length = len(scores) - si
                    cycle_start = si - 1
                    score_index = cycle_start + ((generations - cycle_start) % cycle_length) - 1
                    return scores[score_index]

            scores.append(score)


if __name__ == '__main__':
    d = Dec18()
    print('Resource value after 10 minutes:', d.part_1())
    print('After 1000000000 minutes:', d.part_2())
