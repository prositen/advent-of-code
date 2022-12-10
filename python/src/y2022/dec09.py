from python.src.common import Day, timer, Timer, sgn


class Dec09(Day):

    def __init__(self, instructions=None, filename=None):
        super().__init__(2022, 9, instructions=instructions, filename=filename)
        self.rope = [(0, 0), (0, 0)]

    @staticmethod
    def parse_instructions(instructions):
        return [((s := i.split())[0], int(s[1])) for i in instructions]

    def move_head(self, move):
        match move:
            case 'U':
                self.rope[0] = (self.rope[0][0] - 1, self.rope[0][1])
            case 'D':
                self.rope[0] = (self.rope[0][0] + 1, self.rope[0][1])
            case 'L':
                self.rope[0] = (self.rope[0][0], self.rope[0][1] - 1)
            case 'R':
                self.rope[0] = (self.rope[0][0], self.rope[0][1] + 1)

    def move_part(self, part):
        dy = self.rope[part - 1][0] - self.rope[part][0]
        dx = self.rope[part - 1][1] - self.rope[part][1]
        if dy == 0 and abs(dx) > 1:
            self.rope[part] = (self.rope[part][0], self.rope[part][1] + sgn(dx))
        elif dx == 0 and abs(dy) > 1:
            self.rope[part] = (self.rope[part][0] + sgn(dy), self.rope[part][1])
        elif abs(dx) + abs(dy) > 2:
            self.rope[part] = (self.rope[part][0] + sgn(dy), self.rope[part][1] + sgn(dx))

    def run(self, parts=2):
        touched = {(0, 0): True}
        self.rope = [(0, 0) for _ in range(parts + 1)]
        for (direction, steps) in self.instructions:
            for _ in range(steps):
                self.move_head(direction)
                for p in range(parts):
                    self.move_part(p + 1)
                touched[self.rope[parts - 1]] = True

        return sum(touched.values())

    @timer(part=1)
    def part_1(self):
        return self.run()

    @timer(part=2)
    def part_2(self):
        return self.run(parts=10)


if __name__ == '__main__':
    with Timer('Total'):
        Dec09().run_day()
