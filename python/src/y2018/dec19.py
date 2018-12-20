from python.src.common import Day
from python.src.y2018.dec16 import Device


class DeviceIp(Device):

    def __init__(self, ip):
        super().__init__(registers=6)
        self.ip = ip

    def reset(self):
        self.reg = [0 for _ in range(len(self.reg))]

    def run(self, program, opcode_translation=None, run_until_ip=None):
        ip = self.reg[self.ip]
        while 0 <= ip < len(program):
            self.reg[self.ip] = ip
            instruction, a, b, c = program[ip]
            self.reg[c] = self.instructions[instruction](a, b)
            ip = self.reg[self.ip]
            ip += 1
            if run_until_ip and ip == run_until_ip:
                return


class Dec19(Day):
    def __init__(self, instructions=None, filename=None):
        super().__init__(2018, 19, instructions, filename)
        self.device = DeviceIp(ip=self.instructions[0])
        self.program = self.instructions[1]

    @staticmethod
    def parse_instructions(instructions):
        ip = int(instructions[0][4:])
        program = []
        for line in instructions[1:]:
            tokens = line.strip().split()
            program.append((tokens[0], int(tokens[1]), int(tokens[2]), int(tokens[3])))
        return ip, program

    def part_1(self):
        self.device.reset()
        self.device.run(self.program)
        return self.device.reg[0]

    def part_2(self):
        # The program appears to calculate the sum of a large number's factors.
        # Run it just as long as needed to see which number it is and then
        # do it manually.
        self.device.reset()
        self.device.reg[0] = 1
        self.device.run(self.program, run_until_ip=2)
        number = self.device.reg[3]
        sum_of_factors = 0
        for i in range(1, number + 1):
            if number % i == 0:
                sum_of_factors += i
        return sum_of_factors


if __name__ == '__main__':
    d = Dec19()
    print('Reg[0] has value:', d.part_1())
    print('Part 2: ', d.part_2())
