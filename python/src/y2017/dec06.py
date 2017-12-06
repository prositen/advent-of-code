import os

from python.src.y2017.common import DATA_DIR


class Memory(object):
    def __init__(self, banks):
        self.banks = list(map(int, banks.split()))

    def __len__(self):
        return len(self.banks)

    def __str__(self):
        return ",".join([str(x) for x in self.banks])

    def redistribute(self):
        m = max(self.banks)
        p = self.banks.index(m)
        self.banks[p] = 0
        for pos in range(p + 1, m + p + 1):
            self.banks[pos % len(self)] += 1
        return str(self)

    def steps_until_loop(self):
        seen_before = set()
        steps = 0
        state = str(self)
        while state not in seen_before:
            steps += 1
            seen_before.add(state)
            state = self.redistribute()
        return steps

    def loop_size(self):
        state = str(self)
        steps = 0
        while state != self.redistribute():
            steps += 1
        return steps + 1


if __name__ == '__main__':
    with open(os.path.join(DATA_DIR, 'input.6.txt')) as fh:
        puzzle_input = fh.read()
        memory = Memory(puzzle_input)
        print(memory.steps_until_loop())
        print(memory.loop_size())
