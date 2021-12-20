from python.src.common import Day, timer, Timer
from src.grid import Grid


class ImageEnhancer(Grid):

    def __init__(self, state, algorithm):
        super().__init__(stay_in_bounds=True, state=state)
        self.algorithm = algorithm
        self.even_step = False
        self.shitty_toggle = self.algorithm[0] == '#' and self.algorithm[-1] == '.'

    def update_pos(self, pos):
        input_pixels = ''.join('1' if self.at(pos) else '0'
                               for pos in self.neighbours(pos))
        input_number = int(input_pixels, 2)
        return self.algorithm[input_number] == '#'

    def count(self):
        return sum(self.grid.values())

    def at(self, pos):
        if (pos not in self.grid) and self.shitty_toggle:
            return self.even_step
        return super().at(pos)

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

            min_y, min_x = min(self.grid)
            max_y, max_x = max(self.grid)

            for y in range(min_y - 1, max_y + 2):
                self.grid[(y, min_x - 1)] = self.even_step
                self.grid[(y, max_x + 1)] = self.even_step

            for x in range(min_x - 1, max_x + 2):
                self.grid[(min_y - 1, x)] = self.even_step
                self.grid[(max_y + 1, x)] = self.even_step

            super().step(1)
            if self.shitty_toggle:
                self.even_step = not self.even_step


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
