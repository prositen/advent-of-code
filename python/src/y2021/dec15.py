import operator
from heapq import heappush, heappop

from python.src.common import Day, timer, Timer


class ChitonCave(object):
    def __init__(self, state):
        self.grid = state
        self.delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        self.max_y = len(self.grid)
        self.max_x = len(self.grid[0])

    def neighbours(self, pos):
        for d in self.delta:
            nb = tuple(map(operator.add, pos, d))
            if 0 <= nb[0] < self.max_y and 0 <= nb[1] < self.max_x:
                yield nb, self.grid[nb[0]][nb[1]]

    def traverse(self):
        start = (0, 0)
        goal = (self.max_y - 1, self.max_x - 1)
        to_visit = list()
        to_visit.append((0, start))
        visited = dict()
        while to_visit:
            cost, pos = heappop(to_visit)
            if pos == goal:
                return cost
            if pos not in visited or cost < visited.get(pos):
                visited[pos] = cost
                for nb, nb_cost in self.neighbours(pos):
                    new_cost = cost + nb_cost
                    if nb not in visited or new_cost < visited.get(nb):
                        heappush(to_visit, (cost + nb_cost, nb))
        return 0


class Dec15(Day):

    def __init__(self, instructions=None, filename=None):
        super().__init__(2021, 15, instructions=instructions, filename=filename)

    @staticmethod
    def parse_instructions(instructions):
        return [[int(c) for c in line] for line in instructions]

    def enlarge(self):

        tmp_instructions = list()
        for line in self.instructions:
            new_line = list()
            for x in range(5):
                new_line += [(n+x-9) if n+x > 9 else n+x for n in line]
            tmp_instructions.append(new_line)
        instructions = tmp_instructions
        tmp_instructions = list()

        for y in range(5):
            for line in instructions:
                tmp_instructions.append([(n+y-9) if n+y > 9 else n+y for n in line])
        return tmp_instructions

    @timer(part=1)
    def part_1(self):
        return ChitonCave(state=self.instructions).traverse()

    @timer(part=2)
    def part_2(self):
        big_cave = self.enlarge()
        return ChitonCave(state=big_cave).traverse()


if __name__ == '__main__':
    with Timer('Chiton'):
        Dec15().run_day()
