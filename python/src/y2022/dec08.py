from collections import defaultdict
from itertools import takewhile

from python.src.common import Day, timer, Timer


class Dec08(Day, year=2022, day=8):

    def __init__(self, instructions=None, filename=None):
        super().__init__(instructions=instructions, filename=filename)
        self.forest = self.instructions
        self.max_x = len(self.forest[0])
        self.max_y = len(self.forest)

    @staticmethod
    def parse_instructions(instructions):
        return [
            [int(c) for c in line]
            for line in instructions
        ]

    def view_trees(self):
        visible = defaultdict(bool)
        for row in range(self.max_y):
            height_left = height_right = -1
            for col in range(self.max_x):
                if (height := self.forest[row][col]) > height_left:
                    visible[(row, col)] = True
                    height_left = height
                if (height := self.forest[row][self.max_x - col - 1]) > height_right:
                    visible[(row, self.max_x - col - 1)] = True
                    height_right = height
        for col in range(self.max_x):
            height_top = height_bottom = -1
            for row in range(self.max_y):
                if (height := self.forest[row][col]) > height_top:
                    visible[(row, col)] = True
                    height_top = height
                if (height := self.forest[self.max_y - row - 1][col]) > height_bottom:
                    visible[(self.max_y - row - 1, col)] = True
                    height_bottom = height
        return visible

    @timer(part=1, title='Visible trees')
    def part_1(self):
        return sum(self.view_trees().values())

    @staticmethod
    def treeline(height, trees):
        visible_trees = list(takewhile(lambda c: c < height,
                                       trees))
        score = len(visible_trees)
        if trees != visible_trees:
            score += 1
        return score

    def scenic_score(self, row, col):
        height = self.forest[row][col]
        return (
                self.treeline(height, self.forest[row][:col][::-1]) *
                self.treeline(height, self.forest[row][col + 1:]) *
                self.treeline(height, [self.forest[r][col] for r in range(row - 1, -1, -1)]) *
                self.treeline(height, [self.forest[r][col] for r in range(row + 1, self.max_y)])
        )

    @timer(part=2, title='Scenic score')
    def part_2(self):
        return max(self.scenic_score(row, col)
                   for row in range(0, self.max_y)
                   for col in range(0, self.max_x))


if __name__ == '__main__':
    with Timer('Total'):
        Dec08().run_day()
