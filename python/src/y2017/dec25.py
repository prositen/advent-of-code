import os
from collections import deque

from python.src.y2017.common import DATA_DIR


class Action(object):
    def __init__(self, value, move, next_state):
        self.value = value
        self.move = move
        self.state = next_state

    def run(self, tape):
        tape.write(self.value)
        tape.move(self.move)
        return self.state


class State(object):
    def __init__(self, action0, action1):
        self.action0 = action0
        self.action1 = action1

    def run(self, tape):
        if tape.read() == 0:
            return self.action0.run(tape)
        else:
            return self.action1.run(tape)


class Tape(object):
    def __init__(self):
        self.slots = dict()
        self.pos = 0

    def read(self):
        return self.slots.get(self.pos, 0)

    def write(self, value):
        self.slots[self.pos] = value

    def move(self, move):
        if move == 'right':
            self.pos += 1
        else:
            self.pos -= 1

    def part1(self):
        return sum(self.slots.values())


def last_word(line):
    return line.split()[-1]


class StateMachine(object):
    def __init__(self, puzzle_input):
        self.start = None
        self.checksum_after = None
        self.states = dict()
        self.parse(puzzle_input)
        self.tape = Tape()

    def parse(self, puzzle_input):
        self.start = last_word(puzzle_input[0])
        self.checksum_after = int(puzzle_input[1].split()[-2])
        input_length = len(puzzle_input)
        s = 3
        while s < input_length:
            actions = [None, None]
            state = last_word(puzzle_input[s])
            s += 2
            for i in 0, 1:
                w1 = int(last_word(puzzle_input[s]))
                move = last_word(puzzle_input[s + 1])
                next_state = last_word(puzzle_input[s + 2])
                actions[i] = Action(w1, move, next_state)
                s += 4
            self.states[state] = State(actions[0], actions[1])

    def run(self):
        state = self.states[self.start]
        steps = 0
        while steps < self.checksum_after:
            next_state = state.run(self.tape)
            state = self.states[next_state]
            steps += 1

    def part1(self):
        return self.tape.part1()


def main():
    with open(os.path.join(DATA_DIR, 'input.25.txt')) as fh:
        puzzle_input = [line[:-2] for line in fh.readlines()]

    s_m = StateMachine(puzzle_input)
    s_m.run()
    print("Part 1:", s_m.part1())


if __name__ == '__main__':
    main()
