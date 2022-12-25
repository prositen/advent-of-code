from collections import deque, defaultdict

from python.src.common import Day, timer, Timer


class Block(object):
    def __init__(self, shape, pos):
        self.shape = {(b[0] + pos[0],
                       b[1] + pos[1]) for b in shape}

    @staticmethod
    def from_lists(lists):
        shape = {
            (y, x)
            for y, line in enumerate(lists[::-1])
            for x, c in enumerate(line)
            if c == '#'
        }
        return Block(shape=shape, pos=(0, 0))


class Chamber(object):
    def __init__(self, jets):
        self.max_height = 0
        self.width = 7
        self.block_rest_count = 0
        self.shapes = deque([
            Block.from_lists(['####']),
            Block.from_lists(['.#.', '###', '.#.']),
            Block.from_lists(['..#', '..#', '###']),
            Block.from_lists(['#', '#', '#', '#']),
            Block.from_lists(['##', '##'])
        ])
        self.resting_blocks = set()
        self.resting_blocks.update({
            (0, n) for n in range(self.width)
        })
        self.block = None
        self.jets = deque(jets)

    def push(self):
        delta = 1 if self.jets[0] == '>' else -1
        #pp = 'right' if delta==1 else 'left'
        self.jets.rotate(-1)
        blocks = {(b[0], b[1] + delta) for b in self.block.shape}
        if any(x in (self.width, -1) for _, x in blocks):
            #print(f'Jet of gas pushes rock {pp}, but nothing happens')
            return
        if blocks.intersection(self.resting_blocks):
            #print(f'Jet of gas pushes rock {pp}, but nothing happens')
            return
        #print(f'Jet of gas pushes rock {pp}')
        self.block.shape = blocks
        #self.print()

    def fall(self):
        blocks_below = {(b[0] - 1, b[1]) for b in self.block.shape}
        if blocks_below.intersection(self.resting_blocks):
            # We hit something!
            self.resting_blocks.update(self.block.shape)
            self.max_height = max(self.max_height, max(y for y,_ in self.block.shape))

            self.block = None
            #print('Rock falls 1 unit, causing it to come to rest.')
            self.block_rest_count += 1
        else:
            #print('Rock falls 1 unit')
            self.block.shape = blocks_below

    def print(self):
        print()
        for y in range(self.max_height, 0, -1):
            line = ''.join("#" if (y, x) in self.resting_blocks
                            else "@" if self.block and (y, x) in self.block.shape else "." for x in
                            range(0, self.width))
            print(f'|{line}|')
        print('+', '-' * (self.width - 1), '+')

    def step(self):
        if not self.block:
            #print('Rock begins falling')
            self.block = Block(shape=self.shapes[0].shape,
                               pos=(self.max_height+4, 2))
            self.shapes.rotate(-1)
        self.push()
        self.fall()

    def run(self, resting_rocks):
        #print()
        while self.block_rest_count < resting_rocks:
            self.step()
       #  self.print()
        return self.max_height


class Dec17(Day, year=2022, day=17):

    @staticmethod
    def parse_instructions(instructions):
        return instructions[0]
    @timer(part=1)
    def part_1(self):
        return Chamber(jets=self.instructions).run(2022)

    @timer(part=2)
    def part_2(self):
        return Chamber(jets=self.instructions).run(1000000000000)


if __name__ == '__main__':
    with Timer('Total'):
        Dec17().run_day()
