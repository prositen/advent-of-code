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
        while self.console.pc < len(self.console.instructions):
            self.console.step()
            if self.console.pc in self.seen:
                return False, self.console.acc
            self.seen.add(self.console.pc)
        return True, self.console.acc


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

    def change_program(self):
        code = self.instructions
        for index, line in enumerate(code):
            if line[0] == 'jmp':
                new_op = ('nop', line[1])
            elif line[0] == 'nop':
                new_op = ('jmp', line[1])
            else:
                continue
            new_code = [new_op]
            if index > 0:
                new_code = code[:index] + new_code
            if index <= len(code):
                new_code = new_code + code[index + 1:]
            yield Console(instructions=new_code)

    @timer(part=1)
    def part_1(self):
        console = Console(instructions=self.instructions)
        inspector = GameInspector(console=console)
        return inspector.run()[1]

    @timer(part=2)
    def part_2(self):
        for game in self.change_program():
            inspector = GameInspector(console=game)
            finished, acc = inspector.run()
            if finished:
                return acc


if __name__ == '__main__':
    with Timer('Total'):
        d = Dec08()
        d.part_1()
        d.part_2()
