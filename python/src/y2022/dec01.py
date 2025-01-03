from python.src.common import Day, timer, Timer


class Dec01(Day, year=2022, day=1):

    @staticmethod
    def parse_instructions(instructions):
        return [
            [int(r) for r in g]
            for g in Day.parse_groups(instructions=instructions)
        ]

    @timer(part=1, title='Most calories carried by one elf')
    def part_1(self):
        return max(sum(g) for g in self.instructions)

    @timer(part=2, title='Total calories carried by top three elves')
    def part_2(self):
        elves = [sum(g) for g in self.instructions]
        return sum(sorted(elves, reverse=True)[:3])


if __name__ == '__main__':
    with Timer('Total'):
        Dec01().run_day()
