import re

from python.src.common import Day, timer, Timer


class ClawMachine(object):

    def __init__(self, instructions):
        self.ax, self.ay = instructions[0]
        self.bx, self.by = instructions[1]
        self.tx, self.ty = instructions[2]

    def play(self, delta=0):
        """
            Button A: (ax, ay)
            Button B: (bx, by)
            Target: (tx, ty)

            M * ax + N * bx = tx
            M * ay + N * by = ty

            M = (tx * by - bx*ty) / (ax * by - bx*ay)
            N = (tx - M*ax) / bx

        """
        self.tx += delta
        self.ty += delta
        a_presses, m = divmod(
            self.tx * self.by - self.ty * self.bx,
            self.ax * self.by - self.ay * self.bx)
        if m:
            return 0
        b_presses, m = divmod(self.tx - a_presses * self.ax,
                              self.bx)
        if m:
            return 0

        return 3 * a_presses + b_presses


class Dec13(Day, year=2024, day=13, title='Claw Contraption'):

    @staticmethod
    def parse_instructions(instructions):
        pattern: re.Pattern = re.compile(r'(\d+)')
        return [
            tuple(tuple(map(int, pattern.findall(group[n])))
                  for n in range(len(group)))
            for group in Day.parse_groups(instructions)
        ]

    @timer(part=1)
    def part_1(self):
        return sum(
            ClawMachine(data).play()
            for data in self.instructions
        )

    @timer(part=2)
    def part_2(self):
        return sum(
            ClawMachine(data).play(delta=10_000_000_000_000)
            for data in self.instructions
        )


if __name__ == '__main__':
    with Timer('Total'):
        Dec13().run_day()
