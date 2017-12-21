import os

from python.src.y2017.common import DATA_DIR


class Instruction(object):
    def run(self, context):
        pass


class OneInstruction(Instruction):
    def __init__(self, x):
        self.x = x


class TwoInstruction(Instruction):
    def __init__(self, x, y):
        self.x = x
        self.y = y


class SndInstruction(OneInstruction):
    def run(self, context):
        context.play(context.get(self.x))


class SetInstruction(TwoInstruction):
    def run(self, context):
        context.set(self.x, context.get(self.y))


class AddInstruction(TwoInstruction):
    def run(self, context):
        context.set(self.x, context.get(self.x) + context.get(self.y))


class MulInstruction(TwoInstruction):
    def run(self, context):
        context.set(self.x, context.get(self.x) * context.get(self.y))


class ModInstruction(TwoInstruction):
    def run(self, context):
        context.set(self.x, context.get(self.x) % context.get(self.y))


class RcvInstruction(OneInstruction):
    def run(self, context):
        context.recover(self.x)


class JgzInstruction(TwoInstruction):
    def run(self, context):
        context.jump(context.get(self.x), context.get(self.y))


class Duet(object):
    def __init__(self, puzzle_input):
        self.instructions = [self.parse_line(line) for line in puzzle_input]
        self.registers = dict()
        self.pc = 0
        self.played = 0
        self.recovered = 0
        self.running = True

    def get(self, register_or_value):
        try:
            value = int(register_or_value, 10)
        except ValueError:
            value = self.registers.get(register_or_value, 0)
        return value

    def set(self, register, value):
        self.registers[register] = value
        self.next()

    def play(self, value):
        self.played = value
        self.next()

    def recover(self, value):
        value = self.get(value)
        if value > 0:
            self.recovered = self.played
            self.running = False
        else:
            self.next()

    def jump(self, x, y):
        if x > 0:
            self.pc += y
        else:
            self.next()

    def run(self):
        while self.running and 0 <= self.pc < len(self.instructions):
            i = self.instructions[self.pc]
            i.run(self)
        self.running = False

    def next(self):
        self.pc += 1

    def parse_line(self, line):
        words = line.split()
        if words[0] == 'snd':
            return SndInstruction(words[1])
        elif words[0] == 'set':
            return SetInstruction(words[1], words[2])
        elif words[0] == 'add':
            return AddInstruction(words[1], words[2])
        elif words[0] == 'mul':
            return MulInstruction(words[1], words[2])
        elif words[0] == 'mod':
            return ModInstruction(words[1], words[2])
        elif words[0] == 'rcv':
            return RcvInstruction(words[1])
        elif words[0] == 'jgz':
            return JgzInstruction(words[1], words[2])
        else:
            raise ValueError("You forgot something: ", line)


class Duet2(Duet):
    def __init__(self, id, coordinator, puzzle_input):
        super().__init__(puzzle_input)
        self.id = id
        self.coordinator = coordinator
        self.registers['p'] = self.id

    def step(self):
        if self.running:
            if 0 <= self.pc < len(self.instructions):
                i = self.instructions[self.pc]
                i.run(self)
            else:
                self.running = False

    def send(self, value):
        self.coordinator.send(self.id, value)

    def receive(self):
        return self.coordinator.receive(self.id)

    def play(self, value):
        self.send(value)
        self.next()

    def recover(self, register):
        v = self.receive()
        if v is not None:
            self.set(register, v)


class Coordinator(object):

    def __init__(self, puzzle_input):
        self.d1 = Duet2(0, self, puzzle_input)
        self.d2 = Duet2(1, self, puzzle_input)
        self.q = [list(), list()]
        self.waiting = [False, False]
        self.counter = [0, 0]

    def send(self, id, value):
        self.q[id].append(value)
        self.counter[id] += 1

    def receive(self, id):
        f = 0 if id == 1 else 1
        if len(self.q[f]):
            self.waiting[id] = False
            return self.q[f].pop(0)
        else:
            self.waiting[id] = True
            return None

    def run(self):
        while self.d1.running and self.d2.running and not (self.waiting == [True, True]):
            self.d1.step()
            self.d2.step()

    def result(self):
        return self.counter[1]


def main():
    with open(os.path.join(DATA_DIR, 'input.18.txt')) as fh:
        puzzle_input = fh.readlines()

    d = Duet(puzzle_input)
    d.run()
    print("Part 1:", d.recovered)

    c = Coordinator(puzzle_input)
    c.run()
    print("Part 2:", c.result())


if __name__ == '__main__':
    main()
