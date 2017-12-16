class Generator(object):
    def __init__(self, factor, start, multiplier=1):
        self.factor = factor
        self.reminder = 2147483647
        self.value = start
        self.multiplier = multiplier

    def next_value(self):
        while True:
            self.value = (self.value * self.factor) % self.reminder
            if self.value % self.multiplier == 0:
                yield self.value & 0xFFFF


class Judge(object):
    def __init__(self, gen_A, gen_B):
        self.gen_A = gen_A
        self.gen_B = gen_B
        self.count = 0

    def run(self, steps):
        for x in range(steps):
            if next(self.gen_A.next_value()) == next(self.gen_B.next_value()):
                self.count += 1
        return self.count


def run(mul_a, mul_b, steps):
    factor_a = 16807
    factor_b = 48271
    start_value_a = 289
    start_value_b = 629

    gen_a = Generator(factor_a, start_value_a, mul_a)
    gen_b = Generator(factor_b, start_value_b, mul_b)

    j = Judge(gen_a, gen_b)
    j.run(steps)

    return j.count


def main():
    for mul_a, mul_b, steps in (1, 1, 40000000), (4, 8, 5000000):
        print("Part {}:".format(mul_b // mul_a), run(mul_a, mul_b, steps))


if __name__ == '__main__':
    main()
