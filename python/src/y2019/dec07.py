import itertools

from python.src.common import Day
from python.src.y2019.intcode import IntCode


class Dec07(Day):

    def __init__(self, instructions=None, filename=None):
        super().__init__(2019, 7, instructions, filename)

    @staticmethod
    def parse_instructions(instructions):
        return [
            int(row) for row in instructions[0].split(',')
        ]

    def part_1(self):
        output = 0
        for phases in itertools.permutations([0, 1, 2, 3, 4]):
            prev_output = 0
            for i in range(5):
                amp = IntCode(self.instructions)
                amp.add_input(phases[i])
                amp.add_input(prev_output)
                amp.run()
                prev_output = amp.get_output()
            output = max(output, prev_output)
        return output

    def part_2(self):
        output = 0
        for phases in itertools.permutations([5, 6, 7, 8, 9]):
            amps = list()
            for i in range(5):
                amps.append(IntCode(self.instructions))
                amps[i].add_input(phases[i])
            amps[0].add_input(0)
            while not amps[4].run_and_wait():
                for i in range(5):
                    if not amps[i].run_and_wait():
                        amps[i].add_input(amps[(i - 1) % 5].get_output())
            output = max(output, amps[4].get_output())
        return output


if __name__ == '__main__':
    d = Dec07()
    print("Largest output signal:", d.part_1())
    print("Highest signal with feedback loop mode:", d.part_2())
