from python.src.common import Day, timer, Timer


class Secret(object):
    prune = 16777216

    def __init__(self, secret):
        self.secret = secret

    def next_secret(self):
        self.secret = ((self.secret * 64) ^ self.secret) % self.prune
        self.secret = ((self.secret // 32) ^ self.secret) % self.prune
        self.secret = ((self.secret * 2048) ^ self.secret) % self.prune
        return self.secret

    def nth_secret(self, n):
        for _ in range(n):
            self.next_secret()
        return self.secret


class Dec22(Day, year=2024, day=22):

    @staticmethod
    def parse_instructions(instructions):
        return Day.parse_int_lines(instructions)

    @timer(part=1)
    def part_1(self):
        return sum(
            Secret(seed).nth_secret(2000)
            for seed in self.instructions
        )

    @timer(part=2)
    def part_2(self):
        return 0


if __name__ == '__main__':
    with Timer('Total'):
        Dec22().run_day()
