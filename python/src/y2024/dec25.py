import itertools

from python.src.common import Day, timer, Timer


class Key(object):
    def __init__(self, schematic):
        t = list(zip(*schematic))
        self.schematic = [column.count('#') - 1 for column in t]

    def __repr__(self):
        return f'<Key schematic={self.schematic}>'


class Lock(Key):
    def __repr__(self):
        return f'<Lock schematic={self.schematic}>'


class Dec25(Day, year=2024, day=25, title='Code Chronicle'):

    @staticmethod
    def parse_instructions(instructions):
        keys, locks = list(), list()
        for key_or_lock in Day.parse_groups(instructions):
            if all(ch == '#' for ch in key_or_lock[0]):
                keys.append(Key(key_or_lock))
            else:
                locks.append(Lock(key_or_lock))

        return keys, locks

    @timer(part=1)
    def part_1(self):
        return sum(
            all(kk + ll < 6 for kk, ll in zip(k.schematic, l.schematic))
            for k, l in itertools.product(self.instructions[0],
                                          self.instructions[1])

        )


if __name__ == '__main__':
    with Timer('Total'):
        Dec25().run_day()
