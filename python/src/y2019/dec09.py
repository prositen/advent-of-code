from python.src.common import Day, timer
from python.src.y2019.intcode import IntCode


class Dec09(Day):

    def __init__(self, instructions=None, filename=None):
        super().__init__(2019, 9, instructions, filename)

    @staticmethod
    def parse_instructions(instructions):
        return Day.parse_int_line(instructions)

    @timer(part=1, title='BOOST keycode')
    def part_1(self):
        ic = IntCode(instructions=self.instructions)
        ic.add_input(1)
        ic.run()
        return ic.get_output()

    @timer(part=2, title='Coordinates of distress signal')
    def part_2(self):
        ic = IntCode(instructions=self.instructions)
        ic.add_input(2)
        ic.run()
        return ic.get_output()


if __name__ == '__main__':
    Dec09().run_day()
