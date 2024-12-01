from python.src.common import Day, timer, Timer, stringify


class CrabCups(object):

    def __init__(self, cups, crab_count=False):
        self.cups = dict()
        self.current = cups[0]
        prev = self.current
        for cup in cups[1:]:
            self.cups[prev] = cup
            prev = cup
        self.cups[prev] = self.current

        if crab_count:
            for cup in range(max(self.cups) + 1, int(1_000_001)):
                self.cups[prev] = cup
                prev = cup
            self.cups[prev] = 1_000_000
            self.cups[1_000_000] = self.current
        self.len = max(self.cups)

    def play(self, moves):
        for _ in range(moves):
            a = self.cups[self.current]
            b = self.cups[a]
            c = self.cups[b]
            self.cups[self.current] = self.cups[c]
            destination = self.current - 1
            while destination in (a, b, c, 0):
                destination -= 1
                if destination < 0:
                    destination = self.len
            next_cup = self.cups[destination]
            self.cups[destination] = a
            self.cups[c] = next_cup
            self.current = self.cups[self.current]

    def get(self, n):
        a = 1
        return [
            a := self.cups[a] # noqa 841
            for _ in range(n)
        ]


class Dec23(Day, year=2020, day=23):

    @staticmethod
    def parse_instructions(instructions):
        return Day.parse_digits(instructions=instructions)

    @timer(part=1)
    def part_1(self, moves=100):
        game = CrabCups(self.instructions)
        game.play(moves)
        cups = stringify(game.get(10), '')
        return cups[:cups.index('1')]

    @timer(part=2)
    def part_2(self):
        game = CrabCups(self.instructions, crab_count=True)
        game.play(10_000_000)
        cups = game.get(2)
        return cups[0] * cups[1]


if __name__ == '__main__':
    with Timer('Crab Cups'):
        Dec23().run_day()
