from python.src.common import Day, timer, Timer


class Dec06(Day, year=2022, day=6):

    @staticmethod
    def parse_instructions(instructions):
        return instructions[0]

    def run(self, window_size):
        window = self.instructions[:window_size]
        char_count = window_size
        for ch in self.instructions[window_size:]:
            char_count += 1
            window = window[1:] + ch
            if len(set(window)) == window_size:
                return char_count

    @timer(part=1, title='Start of packet')
    def part_1(self):
        return self.run(window_size=4)

    @timer(part=2, title='Start of message')
    def part_2(self):
        return self.run(window_size=14)


if __name__ == '__main__':
    with Timer('Total'):
        Dec06().run_day()
