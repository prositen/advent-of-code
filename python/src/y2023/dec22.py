from python.src.common import Day, timer, Timer

FROM_POS_X = {'positive_x': True, 'positive_y': True}
FROM_POS_Y = {'positive_y': True, 'positive_x': False}
FROM_NEG_X = {'positive_x': False, 'positive_y': False}
FROM_NEG_Y = {'positive_x': True, 'positive_y': False}


class Node(object):
    def __init__(self, index):
        self.index = index
        self.above = set()
        self.below = set()

    def __repr__(self):
        return f'<Node {self.index}>'


class BrickTower(object):

    def __init__(self, falling_bricks):
        x_coords = sorted([*(c[0][0] for c in falling_bricks),
                           *(c[1][0] for c in falling_bricks)])
        self.min_x, self.max_x = x_coords[0], x_coords[-1]

        y_coords = sorted([*(c[0][1] for c in falling_bricks),
                           *(c[1][1] for c in falling_bricks)])
        self.min_y, self.max_y = y_coords[0], y_coords[-1]

        z_coords = sorted([*(c[0][2] for c in falling_bricks),
                           *(c[1][2] for c in falling_bricks)])
        self.min_z, self.max_z = 0, z_coords[-1]

        self.grid = [
            {
                (x, y): 0 if z else -1
                for x in range(self.min_x, self.max_x + 1)
                for y in range(self.min_y, self.max_y + 1)
            }
            for z in range(self.max_z + 1)
        ]

        self.bricks = dict()
        for index, (start, end) in enumerate(falling_bricks, start=1):
            brick = list()
            for x in range(start[0], end[0] + 1):
                for y in range(start[1], end[1] + 1):
                    for z in range(start[2], end[2] + 1):
                        self.grid[z][(x, y)] = index
                        brick.append((x, y, z))
            self.bricks[index] = brick

    def view(self, positive_x=True, positive_y=True):
        if positive_x:
            x_start, x_end, x_step = self.min_x, self.max_x, 1
        else:
            x_start, x_end, x_step = self.max_x, self.min_x, -1
        if positive_y:
            y_start, y_end, y_step = self.min_y, self.max_y, 1
        else:
            y_start, y_end, y_step = self.max_y, self.min_y, -1

        for z in range(self.max_z, 0, -1):
            row = list()
            plane = self.grid[z]
            for x in range(x_start, x_end + x_step, x_step):
                for y in range(y_start, y_end + y_step, y_step):
                    if (n := plane[(x, y)]) > 0:
                        row.append(chr(n - 1 + ord('A')))
                        break
                else:
                    row.append('.')
            print(''.join(row), z)
        print('-' * abs(x_end + 1 - x_start), 0)

    def empty_below(self, block, x, y, z):
        if 0 < z < len(self.grid):
            return self.grid[z - 1][(x, y)] in (block, 0)
        return False

    def drop(self, brick):
        new_pos = []
        for (x, y, z) in self.bricks[brick]:
            self.grid[z][(x, y)] = 0
            new_pos.append((x, y, z - 1))
            self.grid[z - 1][(x, y)] = brick
        self.bricks[brick] = new_pos

    def state(self):
        return [list(c.values()) for c in self.grid]

    def settle_bricks(self):
        state = self.state()
        prev_state = ''
        while prev_state != state:
            moved = set()
            for z, plane in enumerate(self.grid[1:], start=1):
                for block in set(plane.values()).difference({0}).difference(moved):
                    if all(self.empty_below(block, *pos) for pos in self.bricks[block]):
                        moved.add(block)
                        self.drop(block)

            prev_state, state = state, self.state()

    def find_disintegrate_options(self):
        nodes = {
            i: Node(i) for i in self.bricks.keys()
        }
        nodes[-1] = Node(-1)
        for index, blocks in self.bricks.items():
            bricks_below = set(self.grid[z - 1][(x, y)] for (x, y, z) in blocks) - {index, 0}
            n = nodes[index]
            n.below = {nodes[b] for b in bricks_below}
            for p in n.below:
                p.above.add(n)
            nodes[index] = n
        can_disintegrate = {n for n in nodes.values() if all(len(p.below) > 1 for p in n.above)}

        chain_options = set(nodes.values()) - can_disintegrate - {nodes[-1]}
        sum_removed = 0
        for node in chain_options:
            removed = {node}
            to_remove = set(node.above)
            while to_remove:
                this_node = to_remove.pop()
                if this_node.below <= removed:
                    to_remove.update(this_node.above)
                    removed.add(this_node)
            sum_removed += (len(removed) - 1)

        return len(can_disintegrate), sum_removed


class Dec22(Day, year=2023, day=22):

    def __init__(self, filename=None, instructions=None):
        super().__init__(filename=filename, instructions=instructions)
        bt = BrickTower(self.instructions)
        bt.settle_bricks()
        self.can_disintegrate, self.sum_of_falling_bricks = bt.find_disintegrate_options()

    @staticmethod
    def parse_instructions(instructions):
        return [
            (tuple(map(int, s[0].split(','))),
             tuple(map(int, s[1].split(','))))
            for row in instructions
            for s in [row.split('~')]
        ]

    @timer(part=1)
    def part_1(self):
        return self.can_disintegrate

    @timer(part=2)
    def part_2(self):
        return self.sum_of_falling_bricks


if __name__ == '__main__':
    with Timer('Total'):
        Dec22().run_day()
