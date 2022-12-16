from collections import deque, namedtuple

from python.src.common import Day, timer, Timer

CaveState = namedtuple('CaveState', ['pos', 'increase'])
State = namedtuple('State', ['cave', 'time', 'pressure', 'open'])


class Cave(object):

    def __init__(self, valves):
        self.tunnels = {valve[0]: (valve[1], valve[2]) for valve in valves}
        self.open_valves = set()
        self.position = 'AA'
        self.pressure = 0
        self.time = 0

    def release_pressure(self, open_valves=None):
        return sum(self.tunnels[v][0] for v in open_valves)

    MOVE = 0
    OPEN = 1

    def run(self, time=30):
        to_visit = deque()
        to_visit.append(State(time=0, pressure=0, open=set(),
                              cave=CaveState(pos='AA', increase=0)
                              )
                        )
        best = dict()
        max_pressure = 0
        while to_visit:
            state: State = to_visit.popleft()
            cave: CaveState = state.cave
            if state.time == time:
                continue

            pressure = state.pressure + cave.increase
            max_pressure = max(max_pressure, pressure)
            if cave in best and best.get(cave) >= pressure:
                continue

            best[cave] = pressure

            if (i := self.tunnels[cave.pos][0]) and cave.pos not in state.open:
                cv = CaveState(pos=cave.pos,
                               increase=cave.increase + i)
                to_visit.append(State(cave=cv,
                                      time=state.time + 1,
                                      pressure=pressure,
                                      open=state.open.union({cave.pos}))
                                )
            for tunnel in self.tunnels[cave.pos][1]:
                cv = CaveState(pos=tunnel, increase=cave.increase)
                to_visit.append(State(cave=cv,
                                      time=state.time + 1,
                                      pressure=pressure, open=state.open),
                                )

        return max_pressure


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
        c = Cave(self.instructions)
        return c.run()

    @timer(part=2)
    def part_2(self):
        return 0


if __name__ == '__main__':
    with Timer('Total'):
        Dec16().run_day()
