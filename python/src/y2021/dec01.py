from python.src.common import Day, timer, Timer


class Dec01(Day, year=2021, day=1):

    @staticmethod
    def parse_instructions(instructions):
        return Day.parse_int_lines(instructions)

    def get_depth(self, window_size=1):
        decreases = 0
        prev_depth = None
        for i in range(0, len(self.instructions) - (window_size - 1)):
            depth = sum(self.instructions[i:i + window_size])
            if prev_depth and depth > prev_depth:
                decreases += 1
            prev_depth = depth
        return decreases

    @timer(part=1)
    def part_1(self):
        return self.get_depth()

    @timer(part=2)
    def part_2(self):
        return self.get_depth(window_size=3)


if __name__ == '__main__':
    with Timer('Sonar Sweep'):
        Dec01().run_day()
