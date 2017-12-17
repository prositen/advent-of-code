class Spinlock(object):

    def __init__(self, step):
        self.values = [0]
        self.position = 0
        self.value = 0
        self.skip = step

    def next_value(self):
        self.value += 1
        return self.value

    def step(self):
        next_value = self.next_value()
        self.position = 1 + ((self.position + self.skip) % len(self.values))
        self.values.insert(self.position, next_value)

    def part_1(self):
        for _ in range(2017):
            self.step()
        return self.values[(self.position + 1) % len(self.values)]

    def part_2(self):
        # 0 is always first, keep track of what's changed behind it.
        after_0 = self.values[1]
        pos = self.position
        for x in range(2017+1, 50000000):
            pos = 1 + ((pos + self.skip) % x)
            if pos == 1:
                after_0 = x
        return after_0

def main():
    s = Spinlock(344)
    print("Part 1:", s.part_1())
    print("Part 2:", s.part_2())

if __name__ == '__main__':
    main()