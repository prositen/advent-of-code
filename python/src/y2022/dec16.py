import itertools
from collections import deque
from heapq import heappop, heappush

from python.src.common import Day, timer, Timer


class Cave(object):

    def __init__(self, valves, with_elephant=False):
        self.tunnels = {valve[0]: (valve[1], valve[2]) for valve in valves}
        self.tunnels[None] = (0, [])
        self.open_valves = set()
        self.with_elephant = with_elephant

    def release_pressure(self, open_valves=None):
        return sum(self.tunnels[v][0] for v in open_valves)

    MOVE = 0
    OPEN = 1

    def run(self, time=30):
        if self.with_elephant:
            to_visit = list()
            to_visit.append(((0,0), (0, 0, set(), (('AA', 'AA'), 0))))
        else:
            to_visit = deque()
            to_visit.append((0, 0, set(), (('AA', 'AA'), 0)))

        to_open = {v for v in self.tunnels if self.tunnels[v][0]}
        best = dict()
        max_pressure = 0
        while to_visit:
            if self.with_elephant:
                _, state = heappop(to_visit)
            else:
                state = to_visit.popleft()
            cave = state[3]
            if state[0] == time:
                continue
            pressure = state[1] + cave[1]
            if cave in best and best.get(cave) >= pressure:
                continue
            if state[2] == to_open:
                max_pressure = max(max_pressure,
                                   state[1] + cave[1] * (time - state[0]))
                continue
            max_pressure = max(max_pressure, pressure)
            best[cave] = pressure

            if self.with_elephant:
                for (my_action, elephant_action) in self.get_actions(cave[0]):
                    increase = 0
                    new_open = set(state[2])
                    new_pos = cave[0]
                    match my_action:
                        case (self.OPEN, valve, inc):
                            if valve not in new_open:
                                new_open.add(valve)
                                increase += inc
                        case (self.MOVE, pos, _):
                            new_pos = (pos, new_pos[1])
                    match elephant_action:
                        case (self.OPEN, valve, inc):
                            if valve not in new_open:
                                new_open.add(valve)
                                increase += inc
                        case (self.MOVE, pos, _):
                            new_pos = (new_pos[0], pos)
                    if new_pos != cave[0] or new_open != state[2]:
                        cv = (new_pos, cave[1] + increase)
                        heappush(to_visit, ((state[0], -pressure), (state[0] + 1, pressure, new_open, cv)))


            else:
                my_pos = cave[0][0]
                ele_pos = cave[0][1]

                if (i := self.tunnels[my_pos][0]) and my_pos not in state[2]:
                    cv = ((my_pos, ele_pos), cave[1] + i)
                    new_open = state[2].union({my_pos})
                    to_visit.append((state[0] + 1, pressure, new_open, cv))

                for tunnel in self.tunnels[my_pos][1]:
                    cv = ((tunnel, ele_pos), cave[1])
                    to_visit.append((state[0] + 1, pressure, state[2], cv))

        return max_pressure

    def get_actions(self, pos):
        if i := self.tunnels[pos[0]][0]:
            my_action = (self.OPEN, pos[0], i)
            if pos[0] != pos[1] and (j := self.tunnels[pos[1]][0]):
                elephant_action = (self.OPEN, pos[1], j)
                yield my_action, elephant_action

            for e_tunnel in self.tunnels[pos[1]][1]:
                elephant_action = (self.MOVE, e_tunnel, 0)
                yield my_action, elephant_action

        for tunnel in self.tunnels[pos[0]][1]:
            my_action = (self.MOVE, tunnel, 0)
            if j := self.tunnels[pos[1]][0]:
                elephant_action = (self.OPEN, pos[1], j)
                yield my_action, elephant_action

            for e_tunnel in self.tunnels[pos[1]][1]:
                elephant_action = (self.MOVE, e_tunnel, 0)
                yield my_action, elephant_action


class Dec16(Day, year=2022, day=16):

    @staticmethod
    def parse_instructions(instructions):
        valves = list()
        for line in instructions:
            valve_data, tunnels = line.split(';')
            valve_name = valve_data[6:8]
            flow_rate = int(valve_data[23:])
            tunnels = [t.strip() for t in tunnels[23:].split(', ')]
            valves.append((valve_name, flow_rate, tunnels))
        return valves

    @timer(part=1)
    def part_1(self):
        return Cave(self.instructions).run()

    @timer(part=2)
    def part_2(self):
        # 2675
        return Cave(self.instructions, with_elephant=True).run(time=26)


if __name__ == '__main__':
    with Timer('Total'):
        Dec16().run_day()
