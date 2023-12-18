from python.src.common import Day, timer, Timer


class Dec04(Day, year=2022, day=4):

    @staticmethod
    def parse_instructions(instructions):
        result = list()
        for line in instructions:
            s = line.split(',')
            pair = (s[0].split('-'), s[1].split('-'))
            result.append(
                ((int(pair[0][0]), int(pair[0][1])),
                 (int(pair[1][0]), int(pair[1][1])))
            )
        return result

    @timer(part=1, title='Ranges contain the other')
    def part_1(self):
        return sum(
            (a[0] <= b[0] and a[1] >= b[1]) or
            (b[0] <= a[0] and b[1] >= a[1])
            for (a, b) in self.instructions
        )

    @timer(part=2, title='Ranges overlap each other')
    def part_2(self):
        return sum(
            (a[0] <= b[1] and b[0] <= a[1])
            for (a, b) in self.instructions
        )


if __name__ == '__main__':
    with Timer('Total'):
        Dec04().run_day()
