from python.src.common import Day, timer, Timer


class VideoSystem(object):

    def __init__(self):
        self.instructions = list()
        self.cycle_count = 0
        self.x = 1
        self.pending_write = 0
        self.signal_sum = 0
        self.screen = dict()

    def step(self):
        if self.pending_write:
            self.x += self.pending_write
            self.pending_write = 0
        else:
            instruction = self.instructions.pop(0)
            match (instruction.split()):
                case ['noop'], _:
                    pass
                case ['addx', number]:
                    self.pending_write = int(number, 10)

    def update_signal_strength(self):
        if ((self.cycle_count - 20) % 40) == 0:
            self.signal_sum += (self.x * self.cycle_count)

    def update_screen(self):
        row, col = divmod(self.cycle_count, 40)
        if (self.x - 1) <= col <= (self.x + 1):
            self.screen[(row, col)] = '#'

    def run(self, instructions):
        self.instructions = list(instructions)
        while self.instructions or self.pending_write:
            self.update_screen()
            self.cycle_count += 1
            self.update_signal_strength()
            self.step()

    def video(self):
        return [
            (''.join(self.screen.get((r, c), '.') for c in range(40)))
            for r in range(6)
        ]


class Dec10(Day, year=2022, day=10):

    @timer(part=1)
    def part_1(self):
        v = VideoSystem()
        v.run(self.instructions)
        return v.signal_sum

    @timer(part=2)
    def part_2(self):
        v = VideoSystem()
        v.run(self.instructions)
        print('\n'.join(v.video()))


if __name__ == '__main__':
    with Timer():
        Dec10().run_day()
