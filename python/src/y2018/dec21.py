from python.src.common import Day
from python.src.y2018.dec19 import DeviceIp


class Dec21(Day):
    def __init__(self, instructions=None, filename=None):
        super().__init__(2018, 21, instructions, filename)
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
        self.device.run(self.program, run_until_ip=28)
        return self.device.reg[4]

    def brute_part_2(self):
        # Don't do this. Takes soooo long.
        self.device.reset()
        seen = set()
        last = None
        while True:
            self.device.run(self.program, run_until_ip=28)
            reg4 = self.device.reg[4]
            if reg4 in seen:
                return last
            seen.add(reg4)
            last = reg4

    def part_2(self):
        # Translating the elfsembly to python to improve speed
        seen = set()
        last = 0

        r4 = 707129
        r3 = 65536
        while True:
            r4 = (((r4 + (r3 & 255)) & 16777215) * 65899) & 16777215
            if r3 < 256:
                if r4 in seen:
                    return last
                seen.add(r4)
                last = r4
                r3 = r4 | int(2 ** 16)
                r4 = 707129
                continue
            r3 //= 256


if __name__ == '__main__':
    d = Dec21()
    print('reg[0] value with fewest instructions before return:', d.part_1())
    print('reg[0] value with most instructions before return:', d.part_2())
