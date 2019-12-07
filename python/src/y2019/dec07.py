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
                amp.input = [phases[i], prev_output]
                amp.run()
                prev_output = amp.output
            output = max(output, prev_output)
        return output

    def part_2(self):
        output = 0
        for phases in itertools.permutations([5, 6, 7, 8, 9]):
            amps = list()
            for i in range(5):
                amps.append(IntCode(self.instructions))
                amps[i].input = [phases[i]]
            amps[4].output = 0

            while amps[4].pc < len(amps[4].data):
                for i in range(5):
                    amps[i].step()
                    if amps[i].output is not None:
                        amps[(i + 1) % 5].input.append(amps[i].output)
                        amps[i].output = None

            output = max(output, amps[0].input[-1])
        return output


if __name__ == '__main__':
    d = Dec07()
    print("Largest output signal:", d.part_1())
    print(":", d.part_2())
