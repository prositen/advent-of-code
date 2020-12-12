from python.src.common import Day, timer, Timer


class Ship(object):

    def __init__(self):
        self.pos = 0, 0
        self.dir = 0, 1

    def forward(self, steps):
        self.pos = self.pos[0] + self.dir[0] * steps, self.pos[1] + self.dir[1] * steps

    def north(self, steps):
        self.pos = self.pos[0] - steps, self.pos[1]

    def south(self, steps):
        self.pos = self.pos[0] + steps, self.pos[1]

    def east(self, steps):
        self.pos = self.pos[0], self.pos[1] + steps

    def west(self, steps):
        self.pos = self.pos[0], self.pos[1] - steps

    def left(self, degrees):
        if degrees == 90:
            self.dir = -self.dir[1], self.dir[0]
        elif degrees == 180:
            self.dir = -self.dir[0], -self.dir[1]
        elif degrees == 270:
            self.dir = self.dir[1], -self.dir[0]

    def right(self, degrees):
        self.left(360 - degrees)

    def distance(self, distance_from=None):
        if distance_from is None:
            distance_from = 0, 0
        return abs(self.pos[0] - distance_from[0]) + abs(self.pos[1] - distance_from[1])

    def run(self, instructions):
        for command, num in instructions:
            if command == 'F':
                self.forward(num)
            elif command == 'N':
                self.north(num)
            elif command == 'E':
                self.east(num)
            elif command == 'S':
                self.south(num)
            elif command == 'W':
                self.west(num)
            elif command == 'L':
                self.left(num)
            elif command == 'R':
                self.right(num)
        return self.distance()


class Waypoint(Ship):

    def __init__(self):
        super().__init__()
        self.pos = -1, 10
        self.ship = Ship()

    def forward(self, steps):
        y, x = self.ship.pos
        wy, wx = self.pos
        pos_y = y + wy * steps
        pos_x = x + wx * steps
        self.ship.pos = pos_y, pos_x

    def left(self, degrees):
        self.dir = self.pos
        super().left(degrees)
        self.pos = self.dir

    def right(self, degrees):
        self.left(360 - degrees)

    def distance(self, distance_from=None):
        return self.ship.distance(distance_from)


class Dec12(Day):

    def __init__(self, instructions=None, filename=None):
        super().__init__(2020, 12, instructions, filename)

    @staticmethod
    def parse_instructions(instructions):
        return [(r[0], int(r[1:], 10)) for r in instructions]

    @timer(part=1)
    def part_1(self):
        ship = Ship()
        return ship.run(self.instructions)

    @timer(part=2)
    def part_2(self):
        waypoint = Waypoint()
        return waypoint.run(self.instructions)


if __name__ == '__main__':
    with Timer():
        Dec12().run_day()
