from python.src.common import Day, timer, Timer


class Dec02(Day):

    def __init__(self, instructions=None, filename=None):
        super().__init__(2021, 2, instructions, filename)
        self.delta = {
            'forward': (1, 0, 1),
            'down': (0, 1, 0),
            'up': (0, -1, 0),
        }
        self.pos = (0, 0, 0)

    @staticmethod
    def parse_instructions(instructions):
        course = list()
        for line in instructions:
            command, units = line.split(' ', 1)
            course.append((command, int(units, 10)))
        return course

    def move_sub(self):
        if self.pos == (0, 0, 0):
            for command, units in self.instructions:
                self.pos = (self.pos[0] + self.delta[command][0] * units,
                            self.pos[1] + self.delta[command][1] * units,
                            self.pos[2] + self.delta[command][2] * units * self.pos[1])

    @timer(part=1)
    def part_1(self):
        self.move_sub()
        return self.pos[0] * self.pos[1]

    @timer(part=2)
    def part_2(self):
        self.move_sub()
        return self.pos[0] * self.pos[2]


if __name__ == '__main__':
    with Timer('Total'):
        Dec02().run_day()
