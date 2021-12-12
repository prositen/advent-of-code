from collections import deque

from python.src.common import Day, timer, Timer


class Caves(object):

    def __init__(self, passages):
        self.passages = dict()
        for start, end in passages:
            if start != 'end' and end != 'start':
                self.passages[start] = self.passages.get(start, list()) + [end]
            if end != 'end' and start != 'start':
                self.passages[end] = self.passages.get(end, list()) + [start]

    def find_paths(self, twice=False):
        to_visit = deque()
        to_visit.append(('start', [], False))
        paths = list()
        while to_visit:
            cave, path, small_visited = to_visit.popleft()
            if cave == 'end':
                paths.append(path)
            else:
                for neighbour in self.passages.get(cave, list()):
                    if (neighbour.isupper()
                            or neighbour not in path
                            or (twice and not small_visited)):
                        v = small_visited or (neighbour.islower() and neighbour in path)
                        to_visit.appendleft((neighbour, path + [cave], v))
        return len(paths)


class Dec12(Day):

    def __init__(self, instructions=None, filename=None):
        super().__init__(2021, 12, instructions, filename)

    @staticmethod
    def parse_instructions(instructions):
        return [
            tuple(line.split('-')) for line in instructions
        ]

    @timer(part=1)
    def part_1(self):
        return Caves(self.instructions).find_paths()

    @timer(part=2)
    def part_2(self):
        return Caves(self.instructions).find_paths(twice=True)


if __name__ == '__main__':
    with Timer('Passage Pathing'):
        Dec12().run_day()
