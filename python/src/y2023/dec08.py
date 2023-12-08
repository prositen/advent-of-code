import math
from collections import deque

from python.src.common import Day, timer, Timer


def steps_to_exit(instructions, network):
    steps = 0
    current = 'AAA'
    while current != 'ZZZ':
        steps += 1
        next_instruction = instructions[0]
        instructions.rotate(-1)
        current = network[current][next_instruction]

    return steps


def steps_to_all_exists(instructions, network):
    steps = 0
    nodes = [c for c in network if c.endswith('A')]
    steps_per_start = dict()
    while nodes:
        steps += 1
        next_instruction = instructions[0]
        instructions.rotate(-1)
        next_nodes = list()
        for node in nodes:
            node = network[node][next_instruction]
            if node.endswith('Z'):
                steps_per_start[node] = steps
            else:
                next_nodes.append(node)
        nodes = next_nodes

    return math.lcm(*steps_per_start.values())


class Dec08(Day, year=2023, day=8):

    @staticmethod
    def parse_instructions(instructions):
        nodes = dict()
        for line in instructions[2:]:
            split = line.split()
            nodes[split[0]] = {
                'L': split[2][1:-1],
                'R': split[3][:-1]
            }
        return deque(instructions[0]), nodes

    @timer(part=1)
    def part_1(self):
        instructions, nodes = self.instructions
        return steps_to_exit(instructions=instructions, network=nodes)

    @timer(part=2)
    def part_2(self):
        instructions, nodes = self.instructions
        return steps_to_all_exists(instructions=instructions, network=nodes)


if __name__ == '__main__':
    with Timer('Total'):
        Dec08().run_day()
