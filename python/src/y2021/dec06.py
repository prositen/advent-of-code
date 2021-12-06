from collections import Counter

from python.src.common import Day, timer, Timer


class School(object):

    def __init__(self, fish_timers):
        self.fish = Counter(fish_timers)

    def step(self):
        parents = self.fish.pop(0, 0)
        self.fish = Counter({
            k - 1: v
            for k, v in self.fish.items()
        })
        if parents:
            self.fish.update({
                8: parents,
                6: parents
            })

    def count(self):
        return sum(self.fish.values())

    def run(self, days):
        for i in range(days):
            self.step()
        return self.count()


class Dec06(Day):

    def __init__(self, instructions=None, filename=None):
        super().__init__(2021, 6, instructions, filename)

    @staticmethod
    def parse_instructions(instructions):
        return Day.parse_int_line(instructions)

    @timer(part=1)
    def part_1(self):
        return School(self.instructions).run(80)

    @timer(part=2)
    def part_2(self):
        return School(self.instructions).run(256)


if __name__ == '__main__':
    with Timer('Lanternfish'):
        Dec06().run_day()
