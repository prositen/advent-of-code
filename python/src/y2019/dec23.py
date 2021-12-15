from python.src.common import Day, timer, Timer
from python.src.y2019.intcode import IntCode


class NAT(object):
    def __init__(self, int_code, computers):
        self.computers = list()
        for cid in range(computers):
            c = IntCode(instructions=int_code)
            c.add_input(cid)
            self.computers.append(c)

        self.packet = (0, 0)
        self.step_count = 0
        self.idle_nodes = set()
        self.idle = False
        self.traffic = [[] for _ in range(computers)]

    def run(self):
        self.step_count += 1
        all_idle = True
        for index, computer in enumerate(self.computers):
            computer.run_and_wait()
            if self.traffic[index]:
                for t in self.traffic[index]:
                    computer.add_input(t)
                self.traffic[index] = []
            else:
                computer.add_input(-1)
                if index not in self.idle_nodes:
                    self.idle_nodes.add(index)
                    all_idle = False

            if len(computer.output) > 2:
                self.idle_nodes.discard(index)
                all_idle = False
                target = computer.get_output(0)
                x = computer.get_output(0)
                y = computer.get_output(0)
                if target < len(self.computers):
                    self.traffic[target].append(x)
                    self.traffic[target].append(y)
                elif target == 255:
                    self.packet = x, y
        self.idle = (all_idle and sum(len(x) for x in self.traffic) == 0)

    def run_until_first(self):
        while self.packet == (0, 0):
            self.run()
        return self.packet[1]

    def resume(self):
        self.idle_nodes = set()
        self.idle = False
        self.computers[0].add_input(self.packet[0])
        self.computers[0].add_input(self.packet[1])

    def run_until_idle(self):
        old_packet = (-1, -1)
        while old_packet[1] != self.packet[1]:
            old_packet = self.packet
            while not self.idle:
                self.run()
            self.resume()
        return old_packet[1]


class Dec23(Day):

    def __init__(self, instructions=None, filename=None):
        super().__init__(2019, 23, instructions, filename)

    @staticmethod
    def parse_instructions(instructions):
        return Day.parse_int_line(instructions)

    @timer(part=1)
    def part_1(self):
        nat = NAT(int_code=self.instructions, computers=50)
        return nat.run_until_first()

    @timer(part=2)
    def part_2(self):
        nat = NAT(int_code=self.instructions, computers=50)
        return nat.run_until_idle()


if __name__ == '__main__':
    with Timer('Total'):
        d = Dec23()
        d.part_1()
        d.part_2()
