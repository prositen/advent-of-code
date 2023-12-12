import itertools
import re
from collections import deque

from python.src.common import Day, timer, Timer


class SpringRow(object):
    def __init__(self, springs, damaged_count, unfold=False):
        if unfold:
            springs = 5 * springs
            damaged_count = 5 * damaged_count
        self.springs: str = springs

        self.unknown = list(i for i, ch in enumerate(self.springs) if ch == '?')

        self.damaged_count = damaged_count
        expected = (f'{"#" * c}' for c in self.damaged_count)

        self.expected = re.compile('^\.*' + '\.+'.join(expected) + '\.*$')

        self.groups = list()

    def verify_count(self, springs):
        damaged = list()
        count = 0
        for ch in springs:
            if ch == '#':
                count += 1
            elif count:
                damaged.append(count)
                count = 0
        if count:
            damaged.append(count)
        return damaged == self.damaged_count

    def brute_force_me(self):
        for r in itertools.product('.#', repeat=len(self.unknown)):
            attempt = list(self.springs)
            for ch, index in zip(r, self.unknown):
                attempt[index] = ch
            yield attempt

    def arrangements_from_groups(self, groups):
        result = list()
        to_visit = deque()
        to_visit.append(groups)
        result.append(groups)
        while to_visit:
            items = to_visit.popleft()
            for ((i1, (s1, c1, l1)), (i2, (s2, c2, l2))) in itertools.pairwise(enumerate(items)):
                if s1 + l1  == s2:
                    new_version = items[:i1] + [(s1, '#', l1+l2)] + items[i1+2:]
                    to_visit.append(new_version)
                    result.append(new_version)

        return result

    def match_groups(self):

        groups = list()
        start, min_length, max_length = 0, 0, 0
        prev_ch = '.'
        index = 0
        for index, ch in enumerate(self.springs):
            if ch != prev_ch:
                if prev_ch != '.':
                    groups.append((start, prev_ch, (index - start)))
                start = index
                prev_ch = ch
        if prev_ch != '.':
            groups.append((start, prev_ch, (index + 1 - start)))

        x = self.arrangements_from_groups(groups)

        return 0

    def count_attempts(self, method):
        match method:
            case 'regex':
                matches = [bool(self.expected.match(''.join(s)))
                           for s in self.brute_force_me()]
                count = sum(matches)
            case 'group':
                count = self.match_groups()

            case 'brute' | _:
                attempts = [s for s in self.brute_force_me()]
                matches = [self.verify_count(s) for s in attempts]
                count = sum(matches)
        return count


class Dec12(Day, year=2023, day=12):

    @staticmethod
    def parse_instructions(instructions):
        all_springs = list()
        for line in instructions:
            springs, damaged_count = line.split()
            damaged_count = [int(c) for c in damaged_count.split(',')]
            all_springs.append((springs, damaged_count))
        return all_springs

    @timer(part=1)
    def part_1(self):
        counts = 0
        for i, spring_row in enumerate(self.instructions):
            counts += SpringRow(*spring_row).count_attempts(method='group')
        return counts

    @timer(part=2)
    def part_2(self):
        counts = 0
        for i, spring_row in enumerate(self.instructions):
            counts += SpringRow(*spring_row, unfold=True).count_attempts(method='regex')
            print(i, counts)
        return counts


if __name__ == '__main__':
    with Timer('Total'):
        Dec12().run_day()
