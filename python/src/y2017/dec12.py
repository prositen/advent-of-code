import os

from python.src.y2017.common import DATA_DIR


def parse_line(line):
    words = line.split('<->')
    return set([int(words[0])] + list(map(int, words[1].split(','))))


def find_groups(puzzle_input):
    instructions = {a: parse_line(x) for a, x in enumerate(puzzle_input)}
    programs = dict()

    while programs != instructions:
        for bidi_set in instructions.values():
            for x in bidi_set:
                programs[x] = programs.get(x, set()).union(bidi_set)
        programs, instructions = instructions, programs
    return programs


def main():
    with open(os.path.join(DATA_DIR, 'input.12.txt')) as fh:
        puzzle_input = fh.readlines()

    groups = find_groups(puzzle_input)
    s = set()
    for e in groups.values():
        s.add(",".join(str(x) for x in sorted(e)))

    print("Part 1:", len(groups.get(0)))
    print("Part 2:", len(s))


if __name__ == '__main__':
    main()
