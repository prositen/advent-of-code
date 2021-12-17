from python.src.common import Day, timer, Timer


class Dec17(Day):

    def __init__(self, instructions=None, filename=None):
        super().__init__(2021, 17, instructions, filename)
        self.target_x, self.target_y = self.instructions
        self.max_y = 0
        self.probes = 0
        self.run()

    @staticmethod
    def parse_instructions(instructions):
        coords = list()
        for c in instructions[0][13:].split(', '):
            c = c.split('=')[1].split('..')
            coords.append((int(c[0]), int(c[1])))
        return coords

    def hits_target(self, vel_y, vel_x):
        x, y = 0, 0
        max_y = 0
        while x <= self.target_x[1] and y >= self.target_y[0]:
            if x >= self.target_x[0] and y <= self.target_y[1]:
                self.max_y = max(max_y, self.max_y)
                return True
            x += vel_x
            y += vel_y
            max_y = max(max_y, y)
            vel_y -= 1
            if vel_x > 0:
                vel_x -= 1
            if vel_x == 0 and x < self.target_x[0]:
                return False
        return False

    def run(self):
        self.probes = sum(
            self.hits_target(vel_x=vel_x, vel_y=vel_y)
            for vel_x in range(1, self.target_x[1] + 1)
            for vel_y in range(self.target_y[0], -self.target_y[0])
        )

    @timer(part=1)
    def part_1(self):
        return self.max_y

    @timer(part=2)
    def part_2(self):
        return self.probes


if __name__ == '__main__':
    with Timer('Trick Shot'):
        Dec17().run_day()
