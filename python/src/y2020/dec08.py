from python.src.common import Day, timer, Timer


class Console(object):
    def __init__(self, instructions):
        self.instructions = instructions
        self.acc = 0
        self.pc = 0

    def step(self):
        if 0 <= self.pc < len(self.instructions):
            op, arg = self.instructions[self.pc]
            if op == 'acc':
                self.acc += arg
                self.pc += 1
            elif op == 'jmp':
                self.pc += arg
            elif op == 'nop':
                self.pc += 1


class GameInspector(object):

    def __init__(self, console):
        self.console = console
        self.seen = set()

    def run(self):
        while True:
            self.console.step()
            if self.console.pc in self.seen:
                return self.console.acc
            self.seen.add(self.console.pc)

class Dec08(Day):

    def __init__(self, instructions=None, filename=None):
        super().__init__(2020, 8, instructions, filename)

    @staticmethod
    def parse_instructions(instructions):
        result = []
        for row in instructions:
            op, arg = row.split(' ')
            arg = int(arg)
            result.append((op, arg))
        return result

    @timer(part=1)
    def part_1(self):
        console = Console(instructions=self.instructions)
        inspector = GameInspector(console=console)
        return inspector.run()

    @timer(part=2)
    def part_2(self):
        return 0


if __name__ == '__main__':
    with Timer('Total'):
        d = Dec08()
        d.part_1()
        d.part_2()
