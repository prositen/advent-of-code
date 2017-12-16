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


def part_1():
    a_start = 289
    b_start = 629
    steps = 40000000

    A = Generator(16807, a_start, 1)
    B = Generator(48271, b_start, 1)

    j = Judge(A, B)
    j.run(steps)

    return j.count


def part_2():
    a_start = 289
    b_start = 629
    steps = 5000000

    A = Generator(16807, a_start, 4)
    B = Generator(48271, b_start, 8)

    j = Judge(A, B)
    j.run(steps)
    return j.count


def main():
    print("Part 1:", part_1())
    print("Part 2:", part_2())


if __name__ == '__main__':
    main()
