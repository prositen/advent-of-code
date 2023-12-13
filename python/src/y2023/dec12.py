import itertools
from functools import lru_cache

from python.src.common import Day, timer, Timer


@lru_cache()
def can_replace(springs, expected):
    return all(ch in {ex, '?'} for ch, ex in zip(springs, expected + '.'))


@lru_cache()
def replace_unknown(springs, damaged):
    if (stripped := springs.strip('.')) != springs:
        return replace_unknown(damaged=damaged,
                               springs=stripped)
    if not damaged:
        return int('#' not in springs)

    if sum(damaged) + len(damaged) - 1 > len(springs):
        return 0

    if springs[0] == '#':
        lf = damaged[0]
        if can_replace(springs[:lf + 1], '#' * lf):
            return replace_unknown(damaged=damaged[1:],
                                   springs=springs[lf + 1:])
        else:
            return 0
    else:
        return (replace_unknown(damaged=damaged, springs=springs[1:])
                + replace_unknown(damaged=damaged, springs='#' + springs[1:]))


def verify_count(springs, expected):
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
    return damaged == list(expected)


def brute_force_me(springs, expected):
    springs = springs.strip('.')
    unknowns = [i for i, ch in enumerate(springs) if ch == '?']
    count = 0
    attempt = list(springs)
    for r in itertools.product('.#', repeat=len(unknowns)):
        for ch, index in zip(r, unknowns):
            attempt[index] = ch
        count += verify_count(attempt, expected)
    return count


class Dec12(Day, year=2023, day=12):

    @staticmethod
    def parse_instructions(instructions):
        all_springs = list()
        for line in instructions:
            springs, damaged_count = line.split()
            damaged_count = tuple(int(c) for c in damaged_count.split(','))
            all_springs.append((springs, damaged_count))
        return all_springs

    @timer(part=1)
    def part_1(self):
        # Kept for posterity, this is reaaaaally slow
        # return sum(brute_force_me(*i) for i in self.instructions)
        return sum(replace_unknown(*i) for i in self.instructions)

    @timer(part=2)
    def part_2(self):
        instructions = [
            ('?'.join([springs for _ in range(5)]),
             5 * damaged)
            for springs, damaged in self.instructions
        ]
        return sum(replace_unknown(*i) for i in instructions)


if __name__ == '__main__':
    with Timer('Total'):
        Dec12().run_day()
