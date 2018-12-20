from collections import defaultdict, deque
from python.src.common import Day


class Dec20(Day):
    DIRS = {
        'N': (-1, 0),
        'E': (0, 1),
        'S': (1, 0),
        'W': (0, -1)
    }

    def __init__(self, instructions=None, filename=None):
        super().__init__(2018, 20, instructions, filename)
        self.map = defaultdict(lambda: len(self.instructions))

    @staticmethod
    def parse_instructions(instructions):
        return instructions[0].strip()[1:-1]

    def run_chars(self, chars):
        nested = deque()
        pos = (0, 0)
        distance = 0
        pc = 0
        for c in chars:
            if c == '(':
                nested.append((pos, distance, []))
            elif c == ')':
                pos, distance, distances = nested.pop()
                if pc == '|':
                    distances.append(distance)
                distance = min(distances)
            elif c == '|':
                pos, dist, distances = nested[-1]
                distances.append(distance)
                distance = dist
            else:
                dyx = self.DIRS[c]
                distance = distance + 1
                pos = pos[0] + dyx[0], pos[1] + dyx[1]
                self.map[pos] = min([self.map[pos], distance])
            pc = c

    def part_1(self):
        self.run_chars(self.instructions)
        return max(self.map.values())

    def part_2(self):
        return len(list(filter(lambda c: c >= 1000, self.map.values())))


if __name__ == '__main__':
    d = Dec20()
    print('The door furthest away is:', d.part_1())
    print('Number of rooms more than 1000 doors away:', d.part_2())
