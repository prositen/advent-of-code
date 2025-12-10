from collections import deque
from z3 import Optimize, Int, Sum, sat

from python.src.common import Day, timer, Timer


class Machine:
    def __init__(self, lights, schematics, joltage):
        self.target_lights = lights
        self.schematics = schematics
        self.target_joltages = tuple(joltage)

    def start_machine(self):
        to_visit = deque()
        current_lights = tuple([False] * len(self.target_lights))
        to_visit.append((current_lights, 0))

        seen_states = dict()
        while to_visit:
            state, pushes = to_visit.popleft()
            if state == self.target_lights:
                return pushes
            if state in seen_states and pushes >= seen_states[state]:
                continue
            seen_states[state] = pushes
            for schematic in self.schematics:
                next_state = list(state)
                for button in schematic:
                    next_state[button] = not next_state[button]
                to_visit.append((tuple(next_state), pushes + 1))

    def configure_joltages(self):
        z3_opt = Optimize()
        button_presses = [Int(f"button_{i}")
                          for i in range(len(self.schematics))
                          ]
        # minimize total presses
        z3_opt.minimize(Sum(button_presses))
        for count in button_presses:  # button press count must >= 0
            z3_opt.add(count >= 0)

        # Which buttons affect which target joltage?
        for j_i, target_joltage in enumerate(self.target_joltages):
            buttons = [
                button
                for button, button_affects in zip(button_presses, self.schematics)
                if j_i in button_affects
            ]
            z3_opt.add(Sum(buttons) == target_joltage)

        if z3_opt.check() == sat:
            model = z3_opt.model()
            return sum(model[c].as_long() for c in button_presses)
        else:
            raise ValueError("No solution found")


class Factory:
    def __init__(self, machines):
        self.machines = machines

    def start_all_machines(self):
        return sum(machine.start_machine() for machine in self.machines)

    def configure_joltages(self):
        return sum(machine.configure_joltages() for machine in self.machines)


class Dec10(Day, year=2025, day=10, title='Factory'):

    @staticmethod
    def parse_instructions(instructions):
        machines = list()
        for line in instructions:
            parts = line.split()
            lights = tuple(ch == '#' for ch in (parts[0])[1:-1])
            buttons = list(list(map(int, part[1:-1].split(','))) for part in (parts[1:-1]))
            joltage = list(map(int, parts[-1][1:-1].split(',')))
            machines.append(Machine(lights, buttons, joltage))
        return machines

    @timer(part=1)
    def part_1(self):
        return Factory(self.instructions).start_all_machines()

    @timer(part=2)
    def part_2(self):
        return Factory(self.instructions).configure_joltages()


if __name__ == '__main__':
    with Timer('Total'):
        Dec10().run_day()
