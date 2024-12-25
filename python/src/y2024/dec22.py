from collections import deque, Counter

from python.src.common import Day, timer, Timer


class Secret(object):
    prune = 16777216

    def __init__(self, secret):
        self.secret = secret
        self.changes = deque([0], maxlen=4)
        self.costs = deque([secret % 10], maxlen=4)
        self.banana_prices: dict[tuple, int] = dict()

    def next_secret(self):
        self.secret = ((self.secret << 6) ^ self.secret) % self.prune
        self.secret = ((self.secret >> 5) ^ self.secret) % self.prune
        self.secret = ((self.secret << 11) ^ self.secret) % self.prune
        cost = self.secret % 10
        self.changes.append(self.costs[-1] - cost)
        self.costs.append(cost)
        if len(self.changes) == 4 and (changes := tuple(self.changes)) not in self.banana_prices:
            self.banana_prices[changes] = cost
        return self.secret

    def nth_secret(self, n):
        for _ in range(n):
            self.next_secret()
        return self.secret


class Dec22(Day, year=2024, day=22, title='Monkey Market'):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.secrets = [Secret(seed) for seed in self.instructions]
        self.has_generated_secrets = False

    def generate_secrets(self):
        if not self.has_generated_secrets:
            for secret in self.secrets:
                secret.nth_secret(2000)
            self.has_generated_secrets = True

    @staticmethod
    def parse_instructions(instructions):
        return Day.parse_int_lines(instructions)

    @timer(part=1)
    def part_1(self):
        self.generate_secrets()
        return sum(
            secret.secret
            for secret in self.secrets
        )

    @timer(part=2)
    def part_2(self):
        self.generate_secrets()
        prices = Counter()
        for secret in self.secrets:
            prices.update(secret.banana_prices)
        return prices.most_common(1)[0][1]


if __name__ == '__main__':
    with Timer('Total'):
        Dec22().run_day()
