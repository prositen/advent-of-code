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
        self.shapes = [
            Block.from_lists(['####']),
            Block.from_lists(['.#.', '###', '.#.']),
            Block.from_lists(['..#', '..#', '###']),
            Block.from_lists(['#', '#', '#', '#']),
            Block.from_lists(['##', '##'])
        ]
        self.shape_index = 0
        self.resting_blocks = set()
        self.resting_blocks.update({
            (0, n) for n in range(self.width)
        })
        self.block = None
        self.jets = jets
        self.jet_index = 0
        self.cycle_found = False

    def push(self):
        delta = 1 if self.jets[self.jet_index] == '>' else -1
        # pp = 'right' if delta==1 else 'left'
        self.jet_index = (self.jet_index + 1) % len(self.jets)
        blocks = {(b[0], b[1] + delta) for b in self.block.shape}
        if any(x in (self.width, -1) for _, x in blocks):
            # print(f'Jet of gas pushes rock {pp}, but nothing happens')
            return
        if blocks.intersection(self.resting_blocks):
            # print(f'Jet of gas pushes rock {pp}, but nothing happens')
            return
        # print(f'Jet of gas pushes rock {pp}')
        self.block.shape = blocks
        # self.print()

    def fall(self):
        blocks_below = {(b[0] - 1, b[1]) for b in self.block.shape}
        if blocks_below.intersection(self.resting_blocks):
            # We hit something!
            self.resting_blocks.update(self.block.shape)
            self.max_height = max(self.max_height, max(y for y, _ in self.block.shape))

            self.block = None
            # print('Rock falls 1 unit, causing it to come to rest.')
            self.block_rest_count += 1
        else:
            # print('Rock falls 1 unit')
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
        self.push()
        self.fall()

    def footprint(self):
        max_y = [0, 0, 0, 0, 0, 0, 0]
        for y, x in self.resting_blocks:
            max_y[x] = max(max_y[x], y)
        min_y = min(max_y)
        max_y = (y - min_y for y in max_y)
        return (self.shape_index, self.jet_index,
                *max_y)

    def run(self, resting_rocks):
        visited = dict()
        heights = list()
        while self.block_rest_count < resting_rocks:
            heights.append(self.max_height)
            state = self.footprint()
            if state in visited:
                stored_block_count = visited[state]
                cycle_length = self.block_rest_count - stored_block_count
                diff_heights = self.max_height - heights[stored_block_count]
                cycle_count, remaining_blocks = divmod(resting_rocks-stored_block_count,
                                                       cycle_length)
                height = heights[remaining_blocks + stored_block_count]
                return height + cycle_count * diff_heights
            else:
                visited[state] = self.block_rest_count
            # print('Rock begins falling')
            self.block = Block(shape=self.shapes[self.shape_index].shape,
                               pos=(self.max_height + 4, 2))
            self.shape_index = (self.shape_index + 1) % len(self.shapes)
            while self.block:
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
