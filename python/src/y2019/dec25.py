from python.src.common import Day, timer, Timer
from src.y2019.intcode import IntCode


class Dec25(Day):

    def __init__(self, instructions=None, filename=None):
        super().__init__(2019, 25, instructions, filename)

    @staticmethod
    def parse_instructions(instructions):
        return Day.parse_int_line(instructions)

    @timer(part=1)
    def part_1(self):
        ic = IntCode(instructions=self.instructions)
        while True:
            ic.run_and_wait()
            print(ic.get_ascii_string())
            command = input()
            if command == 'quit':
                break
            ic.input_ascii_string(command)

if __name__ == '__main__':
    with Timer('Total'):
        d = Dec25()
        d.part_1()
