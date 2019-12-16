from python.src.common import Day
from python.src.y2019.intcode import IntCode


class Dec02(Day):

    def __init__(self, instructions=None, filename=None):
        super().__init__(2019, 2, instructions, filename)

    @staticmethod
    def parse_instructions(instructions):
        return Day.parse_int_line(instructions)


    def part_1(self):
        self.instructions[1] = 12
        self.instructions[2] = 2
        ic = IntCode(self.instructions)
        ic.run()
        return ic.data[0]

    def part_2(self):
        for verb in range(0, 99):
            for noun in range(0, 99):
                self.instructions[1] = noun
                self.instructions[2] = verb
                ic = IntCode(self.instructions)
                ic.run()
                if ic.data[0] == 19690720:
                    return 100 * noun + verb


if __name__ == '__main__':
    d = Dec02()
    print("Data in position 0: ", d.part_1())
    print("100 * noun * verb: ", d.part_2())
