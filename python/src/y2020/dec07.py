import re
from collections import defaultdict, deque

from python.src.common import Day, timer, Timer


class Dec07(Day, year=2020, day=7):

    def __init__(self, instructions=None, filename=None):
        super().__init__(instructions=instructions, filename=filename)
        self.bag_contains = dict()
        self.bag_contained_by = defaultdict(set)
        self.lookup_bags()

    bag_match = re.compile(r'(\d+ )?(\w+ \w+) bags?')

    @staticmethod
    def parse_instructions(instructions):
        return [list(re.findall(Dec07.bag_match, row))
                for row in instructions]

    def lookup_bags(self):
        for row in self.instructions:
            holder = row[0][1]
            try:
                contents = [(int(bags[0]), bags[1]) for bags in row[1:]]
            except ValueError:
                contents = []
            self.bag_contains[holder] = contents
            for _, color in contents:
                self.bag_contained_by[color].add(holder)

    @timer(part=1)
    def part_1(self):
        to_visit = deque(['shiny gold'])
        containers = set()
        while to_visit:
            color = to_visit.pop()
            if color not in containers:
                containers.add(color)
                to_visit.extend(c for c in self.bag_contained_by.get(color, list()))
        containers.discard('shiny gold')  # Don't count the shiny gold bag
        return len(containers)

    @timer(part=2)
    def part_2(self):
        to_visit = deque([(1, 'shiny gold')])
        bag_count = 0
        while to_visit:
            count, color = to_visit.pop()
            bag_count += count
            to_visit.extend((_count * count, _color) for (_count, _color) in
                            self.bag_contains.get(color, list()))
        return bag_count - 1  # Don't count the shiny gold bag


if __name__ == '__main__':
    with Timer('Handy Haversacks'):
        Dec07().run_day()
