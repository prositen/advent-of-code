from python.src.common import Day
from python.src.y2019.intcode import IntCode


class Dec05(Day):

    def __init__(self, instructions=None, filename=None):
        super().__init__(2019, 5, instructions, filename)

    @staticmethod
    def parse_instructions(instructions):
        return Day.parse_int_line(instructions)


    def part_1(self):
        ic = IntCode(self.instructions)
        ic.add_input(1)
        ic.run()
        return ic.get_output()

    def part_2(self):
        ic = IntCode(self.instructions)
        ic.add_input(5)
        ic.run()
        return ic.get_output()


if __name__ == '__main__':
    d = Dec05()
    print("Part 1:", d.part_1())
    print("Part 2:", d.part_2())
