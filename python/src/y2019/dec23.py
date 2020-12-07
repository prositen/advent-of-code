from python.src.common import Day, timer, Timer
from src.y2019.intcode import IntCode


class NAT(object):
    def __init__(self, int_code, computers):
        self.computers = list()
        for cid in range(computers):
            c = IntCode(instructions=int_code)
            c.add_input(cid)
            self.computers.append(c)

        self.packet = (0, 0)
        self.step_count = 0
        self.idle = False
        self.traffic = [[] for _ in range(computers)]

    def run(self):
        self.step_count += 1
        self.idle = True
        idle_count = 0
        for index, computer in enumerate(self.computers):
            computer.run_and_wait()
            if self.traffic[index]:
                for t in self.traffic[index]:
                    computer.add_input(t)
            else:
                computer.add_input(-1)
                idle_count += 1

            if len(computer.output) > 2:
                target = computer.get_output(0)
                x = computer.get_output(0)
                y = computer.get_output(0)
                if target < len(self.computers):
                    self.traffic[target].append(x)
                    self.traffic[target].append(y)
                elif target == 255:
                    self.packet = x, y

    def run_until_first(self):
        while self.packet == (0, 0):
            self.run()
        return self.packet[1]


class Dec23(Day):

    def __init__(self, instructions=None, filename=None):
        super().__init__(2019, 23, instructions, filename)
        self.nat = NAT(int_code=self.instructions, computers=50)

    @staticmethod
    def parse_instructions(instructions):
        return Day.parse_int_line(instructions)

    @timer(part=1)
    def part_1(self):
        return self.nat.run_until_first()

    @timer(part=2)
    def part_2(self):
        return 0


if __name__ == '__main__':
    with Timer('Total'):
        d = Dec23()
        d.part_1()
        d.part_2()
