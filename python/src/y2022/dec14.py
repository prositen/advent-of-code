from python.src.common import Day, timer, Timer
from python.src.grid import Grid


class Cave(Grid):

    def __init__(self, walls, with_floor=False):
        super().__init__(dimensions=2, data_type=int, stay_in_bounds=False)
        self.delta = ((0, 1), (-1, 1), (1, 1))
        for wall in walls:
            self.add_wall(wall)
        x = sorted(k[0] for k in self.grid.keys())
        y = sorted(k[1] for k in self.grid.keys())
        self.min_x, self.max_x = x[0], x[-1]
        self.min_y, self.max_y = 0, y[-1]
        self.with_floor = with_floor
        if with_floor:
            self.max_y += 2
        self.source = (500, 0)

    def add_wall(self, wall):
        (x1, y1) = wall[0]
        for (x2, y2) in wall[1:]:
            self.grid[(x1, y1)] = 2
            if x1 == x2:
                for y in range(min(y1, y2), max(y1, y2) + 1):
                    self.grid[(x1, y)] = 2
            else:
                for x in range(min(x1, x2), max(x1, x2) + 1):
                    self.grid[(x, y1)] = 2
            (x1, y1) = (x2, y2)

    def pr(self, pos):
        if pos == self.source:
            return 'v'
        match self.at(pos):
            case 1:
                return 'o'
            case 2:
                return '#'
            case _:
                return ' '

    def __str__(self):
        x = sorted(k[0] for k in self.grid.keys())
        y = sorted(k[1] for k in self.grid.keys())

        return '\n'.join(
            ''.join(self.pr((x, y)) for x in range(x[0], x[-1] + 1))
            for y in range(0, y[-1] + 1)
        )

    def out_of_bounds(self, pos):
        return not (self.with_floor or (
                    self.min_x <= pos[0] <= self.max_x and self.min_y <= pos[1] <= self.max_y))

    def at(self, pos):
        if self.with_floor and pos[1] == self.max_y:
            return 2
        return self.grid[pos]

    def step(self, steps=0):
        sand_pos = self.source
        while not self.out_of_bounds(sand_pos):
            old_pos = sand_pos
            for n in self.neighbours(sand_pos):
                if not self.at(n):
                    sand_pos = n
                    break
            if sand_pos == old_pos:
                self.grid[sand_pos] = 1
                return sand_pos != self.source
        return False

    def run(self):
        sand_count = 0
        while self.step():
            sand_count += 1
        return sand_count


class Dec14(Day, year=2022, day=14):

    def __init__(self, instructions=None, filename=None):
        super().__init__(instructions=instructions, filename=filename)

    @staticmethod
    def parse_instructions(instructions):
        return [
            [tuple(map(int, p.split(','))) for p in line.split('->')]
            for line in instructions
        ]

    @timer(part=1)
    def part_1(self):
        room = Cave(walls=self.instructions)
        return room.run()

    @timer(part=2)
    def part_2(self):
        room = Cave(walls=self.instructions, with_floor=True)
        return room.run()


if __name__ == '__main__':
    with Timer('Total'):
        Dec14().run_day()
