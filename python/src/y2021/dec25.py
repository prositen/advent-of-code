from python.src.common import Day, timer, Timer


class Trench(object):
    def __init__(self, max_y, max_x, eastward, soutward):
        self.max_y, self.max_x = max_y, max_x
        self.eastward = eastward
        self.southward = soutward

    def run(self):
        steps = 0
        while True:
            steps += 1
            moved = 0
            new_east = set()
            new_south = set()
            for c in self.eastward:
                new_c = (c[0], (c[1] + 1) % self.max_x)
                if new_c in self.eastward or new_c in self.southward:
                    new_east.add(c)
                else:
                    moved += 1
                    new_east.add(new_c)

            for c in self.southward:
                new_c = ((c[0] + 1) % self.max_y, c[1])
                if new_c in new_east or new_c in self.southward:
                    new_south.add(c)
                else:
                    moved += 1
                    new_south.add(new_c)

            if moved == 0:
                return steps
            self.eastward = new_east
            self.southward = new_south


class Dec25(Day):

    def __init__(self, instructions=None, filename=None):
        super().__init__(2021, 25, instructions, filename)
        self.max_y, self.max_x, self.ew, self.sw = self.instructions

    @staticmethod
    def parse_instructions(instructions):
        ew = set()
        sw = set()
        for y, line in enumerate(instructions):
            for x, ch in enumerate(line):
                if ch == '>':
                    ew.add((y, x))
                elif ch == 'v':
                    sw.add((y, x))
        return len(instructions), len(instructions[0]), ew, sw

    @timer(part=1)
    def part_1(self):
        t = Trench(max_y=self.max_y, max_x=self.max_x,
                   eastward=self.ew, soutward=self.sw)
        return t.run()

    @timer(part=2)
    def part_2(self):
        return 0


if __name__ == '__main__':
    with Timer('Sea Cucumber'):
        Dec25().run_day()
