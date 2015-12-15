from collections import defaultdict
import itertools
import re

__author__ = 'anna'

RE_POTENTIAL = re.compile(r'(\w+) would (gain|lose) (\d+) happiness units by sitting next to (\w+).')


def parse_potential(line, potential):
    result = re.match(RE_POTENTIAL, line)
    if result:
        name_1 = result.group(1)
        verb = result.group(2)
        units = int(result.group(3))
        name_2 = result.group(4)
        if verb == 'lose':
            units = -units
        if name_1 not in potential:
            potential[name_1] = dict()
        potential[name_1][name_2] = units


def calculate_happiness(order, potential):
    happiness = 0
    left_name = order[-1]
    for right_name in order:
        happiness += potential[left_name][right_name] + potential[right_name][left_name]
        left_name = right_name
    return happiness


def maximum_happiness(potential_happiness, include_me=False):
    potential = dict()
    for line in potential_happiness:
        parse_potential(line, potential)

    if include_me:
        potential['Me'] = dict()
        for name in potential.keys():
            potential[name]['Me'] = 0
            potential['Me'][name] = 0

    max_happiness = 0
    for order in itertools.permutations(potential.keys()):
        happiness = calculate_happiness(order, potential)
        max_happiness = max(max_happiness, happiness)
    return max_happiness


def main():
    with open('../../data/input.13.txt', 'r') as fh:
        max_happiness = maximum_happiness(fh.readlines())
        print("Maximum happiness is {max}".format(max=max_happiness))
        fh.seek(0)
        max_happiness = maximum_happiness(fh.readlines(), include_me=True)
        print("Maximum happiness with me in place is {max}".format(max=max_happiness))

if __name__ == '__main__':
    main()
