class Direction(object):
    Walk = {
        0: (-1, 0),
        1: (0, 1),
        2: (1, 0),
        3: (0, -1)
    }

    def __init__(self, direction):
        self.value = direction

    def turn_left(self):
        self.value = (self.value - 1) % 4

    def turn_right(self):
        self.value = (self.value + 1) % 4

    def turn(self, turn_direction):
        if turn_direction == 'L':
            return self.turn_left()
        else:
            return self.turn_right()

    def diff(self):
        return self.Walk[self.value]


def walk(direction, position, blocks):
    diff = direction.diff()
    return position[0] + blocks * diff[0], position[1] + blocks * diff[1]


def walk_and_mark(direction, position, blocks, city_map):
    diff = direction.diff()
    for _ in range(blocks):
        position = tuple((position[0] + diff[0], position[1] + diff[1]))
        if position in city_map:
            return position, True
        city_map[position] = True
    return position, False


def distance(instructions, stop_at_revisit=False):
    direction = Direction(1)
    position = (0, 0)
    city_map = dict()
    city_map[position] = True
    for instruction in instructions:
        blocks = int(instruction[1:])
        direction.turn(instruction[0])
        if stop_at_revisit:
            position, stop = walk_and_mark(direction, position, blocks, city_map)
            if stop:
                break
        else:
            position = walk(direction, position, blocks)

    return abs(position[0]) + abs(position[1])


def visited_twice(instructions):
    return distance(instructions, stop_at_revisit=True)


if __name__ == '__main__':
    with open('../../../data/2016/input.1.txt', 'r') as fh:
        for i in fh.readlines():
            lines = [x.strip() for x in i.split(',')]
            print(distance(lines))
            print(visited_twice(lines))


