from python.src.common import Day, timer, Timer


class Dec21(Day):

    def __init__(self, instructions=None, filename=None):
        super().__init__(2021, 21, instructions=instructions, filename=filename)

    @staticmethod
    def parse_instructions(instructions):
        return [int(line.split(' ')[-1], 10) for line in instructions]

    @timer(part=1)
    def part_1(self):
        pos = self.instructions
        scores = [0, 0]
        dice = 0
        while True:
            for i in (0, 1):
                roll = (3*dice+6)
                dice += 3
                pos[i] = (pos[i] + roll -1) % 10 + 1

                scores[i] += pos[i]

                if scores[i] >= 1000:
                    return dice * min(scores)



    @timer(part=2)
    def part_2(self):
        return 0


if __name__ == '__main__':
    with Timer('Total'):
        Dec21().run_day()
