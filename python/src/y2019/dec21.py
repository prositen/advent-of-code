from python.src.common import Day, timer, Timer
from src.y2019.intcode import IntCode


class Dec21(Day):

    def __init__(self, instructions=None, filename=None):
        super().__init__(2019, 21, instructions, filename)

    @staticmethod
    def parse_instructions(instructions):
        return Day.parse_int_line(instructions)

    def program_computer(self, spring_code):
        ic = IntCode(instructions=self.instructions)
        for line in spring_code:
            ic.input_ascii_string(line)
        ic.run()
        if ic.output[-1] < 128:
            print(ic.get_ascii_string())
            return None
        else:
            return ic.get_output()

    @timer(part=1)
    def part_1(self):
        """

        ^(A | B | C) & D

        :return: Hull damage
        """

        code = [
            "NOT A J",
            "NOT B T",
            "OR J T",  # A or B is a hole
            "NOT C J",
            "OR T J",  # A, B or C is a hole
            "AND D J",  # ..and D is ground
            "WALK"
        ]
        return self.program_computer(spring_code=code)

    @timer(part=2)
    def part_2(self):
        code = [
            "NOT B T",
            "NOT C J",
            "OR T J",  # B or C is a hole
            "AND D J",  # ..and D is ground
            "AND H J",  # and H is ground

            "NOT A T",  # A is a hole, panic jump!
            "OR T J",

            "RUN"
        ]
        return self.program_computer(spring_code=code)


if __name__ == '__main__':
    with Timer('Total'):
        d = Dec21()
        d.part_1()
        d.part_2()
