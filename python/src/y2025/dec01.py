from python.src.common import Day, timer, Timer


class Dial:

    def __init__(self):
        self.position = 50
        self.steps = 100
        self.password = 0

    def rotate(self, rotations: int, direction: str):
        if direction == 'L':
            self.position = (self.position - rotations) % self.steps
        else:
            self.position = (self.position + rotations) % self.steps
        if self.position == 0:
            self.password += 1


class Dial0x434C49434B(Dial):
    def rotate(self, rotations: int, direction: str):

        clicks, rotations = divmod(rotations, self.steps)
        before = self.position
        self.password += clicks
        if direction == 'L':
            self.position -= rotations
        else:
            self.position += rotations
        if before and (not 0 < self.position < self.steps):
            self.password += 1
        self.position %= self.steps


class Dec01(Day, year=2025, day=1, title='Secret entrance'):

    @staticmethod
    def parse_instructions(instructions):
        return [(i[0], int(i[1:]))
                for i in instructions]

    @timer(part=1)
    def part_1(self):
        d = Dial()
        for direction, rotations in self.instructions:
            d.rotate(rotations=rotations, direction=direction)

        return d.password

    @timer(part=2)
    def part_2(self):
        d = Dial0x434C49434B()
        for direction, rotations in self.instructions:
            d.rotate(rotations=rotations, direction=direction)
        return d.password


if __name__ == '__main__':
    with Timer('Total'):
        Dec01().run_day()
