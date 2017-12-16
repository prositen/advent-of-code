import os

from python.src.y2017.common import DATA_DIR
import re

re_SPIN = re.compile(r's(\d+)')
re_EXCHANGE = re.compile(r'x(\d+)/(\d+)')
re_PARTNER = re.compile(r'p([a-p])/([a-p])')

SPIN = 0
EXCHANGE = 1
PARTNER = 2


def parse_line(line):
    match = re.match(re_SPIN, line)
    if match:
        return SPIN, int(match.group(1))
    match = re.match(re_EXCHANGE, line)
    if match:
        return EXCHANGE, (int(match.group(1)), int(match.group(2)))

    match = re.match(re_PARTNER, line)
    if match:
        return PARTNER, (match.group(1), match.group(2))

    return None, None


class Dance(object):
    def __init__(self, puzzle_input):
        self.puzzle_input = [parse_line(l) for l in puzzle_input]

    def dance(self, programs):
        programs = [c for c in programs]
        for command, pos in self.puzzle_input:
            if command == SPIN:
                programs = programs[-pos:] + programs[:-pos]
            elif command == EXCHANGE:
                programs[pos[0]], programs[pos[1]] = programs[pos[1]], programs[pos[0]]
            elif command == PARTNER:
                pos_a = programs.index(pos[0])
                pos_b = programs.index(pos[1])
                programs[pos_a], programs[pos_b] = programs[pos_b], programs[pos_a]

        return "".join(programs)


def main():
    with open(os.path.join(DATA_DIR, 'input.16.txt')) as fh:
        puzzle_input = fh.read().split(',')

    dance = Dance(puzzle_input)
    order = "abcdefghijklmnop"
    seen = [order]
    i = 0
    while True:
        i += 1
        order = dance.dance(order)
        if order in seen:
            cycle_length = i - seen.index(order)
            break
        seen.append(order)

    print("Part 1:", seen[1])
    print("Part 2:", seen[(10 ** 9 % cycle_length)])


if __name__ == '__main__':
    main()
