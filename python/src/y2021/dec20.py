from python.src.common import Day, timer, Timer
from python.src.grid import Grid


class ImageEnhancer(Grid):

    def __init__(self, state, algorithm):
        super().__init__(stay_in_bounds=True, state=state)
        self.algorithm = [ch == '#' for ch in algorithm]
        self.default_lit = False
        self.toggle_default = self.algorithm[0] and not self.algorithm[-1]
        self.min_y, self.min_x = min(self.grid)
        self.max_y, self.max_x = max(self.grid)

    def update_pos(self, pos):
        input_pixels = ''.join('1' if self.at(pos) else '0'
                               for pos in self.neighbours(pos))
        input_number = int(input_pixels, 2)
        return self.algorithm[input_number]

    def count(self):
        return sum(self.grid.values())

    def at(self, pos):
        if (pos not in self.grid) and self.toggle_default:
            return self.default_lit
        return self.grid[pos]

    def __str__(self):
        min_y, min_x = min(self.grid)
        max_y, max_x = max(self.grid)
        lines = list()
        for y in range(min_y, max_y + 1):
            lines.append(''.join('#' if self.grid[(y, x)] else '.'
                                 for x in range(min_x, max_x + 1)))
        lines.append('')
        return '\n'.join(lines)

    def step(self, steps=1):
        for _ in range(steps):

            for y in range(self.min_y - 1, self.max_y + 2):
                self.grid[(y, self.min_x - 1)] = self.default_lit
                self.grid[(y, self.max_x + 1)] = self.default_lit

            for x in range(self.min_x - 1, self.max_x + 2):
                self.grid[(self.min_y - 1, x)] = self.default_lit
                self.grid[(self.max_y + 1, x)] = self.default_lit
            self.min_x -= 1
            self.min_y -= 1
            self.max_x += 1
            self.max_y += 1
            super().step(1)
            if self.toggle_default:
                self.default_lit = not self.default_lit


class Dec20(Day):

    def __init__(self, instructions=None, filename=None):
        super().__init__(2021, 20, instructions, filename)
        self.algo, self.state = self.instructions

    @staticmethod
    def parse_instructions(instructions):
        grid = dict()
        for y, line in enumerate(instructions[2:]):
            for x, char in enumerate(line):
                grid[(y, x)] = char == '#'

        return instructions[0], grid

    @timer(part=1)
    def part_1(self):
        image = ImageEnhancer(state=self.state,
                              algorithm=self.algo)
        image.step(2)
        return image.count()

    @timer(part=2)
    def part_2(self):
        image = ImageEnhancer(state=self.state,
                              algorithm=self.algo)
        image.step(50)
        return image.count()


if __name__ == '__main__':
    with Timer('Trench Map'):
        Dec20().run_day()
