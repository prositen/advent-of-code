import math
from collections import deque

from python.src.common import Day, timer, Timer


def steps_to_exit(instructions, network):
    steps = 0
    current = 'AAA'
    instructions = deque(instructions)
    while current != 'ZZZ':
        steps += 1
        next_instruction = instructions[0]
        instructions.rotate(-1)
        current = network[current][next_instruction]

    return steps


def find_loop(start, instructions, network):
    visited = set()
    goals = dict()
    steps = 0
    instructions = deque(instructions)
    n = len(instructions)
    current = start
    cycle_detected = False
    while True:
        steps += 1
        current = network[current][instructions[0]]
        instructions.rotate(-1)
        if (current, steps % n) in visited:
            if not cycle_detected:
                visited = set()
                cycle_detected = True
            else:
                break
        if current.endswith('Z'):
            if current in goals:
                assert steps % goals[current] == 0
            else:
                goals[current] = steps

        visited.add((current, steps % n))
    assert len(goals) == 1
    return min(goals.values())


def steps_to_all_exists(instructions, network):
    nodes = [c for c in network if c.endswith('A')]
    steps_per_start = dict()
    for node in nodes:
        steps_per_start[node] = find_loop(node, instructions, network)
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
        return instructions[0], nodes

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
