import itertools
from collections import deque
from heapq import heappop, heappush

from python.src.common import Day, timer, Timer


class Cave(object):

    def __init__(self, valves, with_elephant=False):
        self.tunnels = {valve[0]: (valve[1], valve[2]) for valve in valves}

    def run(self, max_time=30):
        to_visit = deque()
        to_visit.append((0, 0, 0, ('AA', 0)))

        best = dict()
        final_paths = set()
        valves = {v: 1 << i for i, v in enumerate(vv for vv, info in self.tunnels.items()
                                                  if info[0])}

        while to_visit:
            (time, pressure, open_valves, cave) = to_visit.popleft()
            (pos, increase) = cave
            # state = (sum(valves[c] for c in open_valves), pos)
            state = (open_valves, pos)
            pressure += increase

            time = time + 1
            if best.get(state, -1) >= pressure:
                continue

            best[state] = pressure
            if time == max_time:
                final_paths.add((open_valves, pressure))
                continue
            else:
                my_pos = cave[0]
                if (i := self.tunnels[my_pos][0]) and not open_valves & valves[my_pos]:
                    cv = (my_pos, increase + i)
                    new_open = open_valves + valves[my_pos]
                    to_visit.append(
                        (time, pressure, new_open, cv))

                for tunnel in self.tunnels[my_pos][1]:
                    cv = (tunnel, increase)
                    to_visit.append(
                        (time, pressure, open_valves, cv))

        return final_paths


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
        paths = Cave(self.instructions).run()
        return max(v for (_, v) in paths)

    @timer(part=2)
    def part_2(self):
        # 2675
        paths = list(Cave(self.instructions).run(max_time=26))
        max_pressure = 0
        for my_valves, my_pressure in paths:
            for ele_valves, ele_pressure in paths:
                if not my_valves & ele_valves:
                    max_pressure = max(max_pressure, ele_pressure + my_pressure)
        return max_pressure


if __name__ == '__main__':
    with Timer('Total'):
        Dec16().run_day()
