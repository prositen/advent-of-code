from collections import deque


def office_factory(favorite_number):
    def office(x, y):
        step1 = x * x + 3 * x + 2 * x * y + y + y * y
        step2 = step1 + favorite_number
        step3 = bin(step2)[2:].count('1')
        return step3 % 2 == 0

    return office


def get_floorplan(office, max_x, max_y):
    rows = ["\t" + "".join(str(x) for x in range(max_x))]
    for y in range(max_y):
        row = ['.' if office(x, y) else '#' for x in range(max_x)]
        rows.append("{0}\t{1}".format(y, "".join(row)))
    return rows


def shortest_path(start, end, favorite_number, max_steps=None):
    office = office_factory(favorite_number)

    visited = set()
    visit = deque()
    root = (start, [])
    visit.append(root)
    visited.add(start)
    while visit:
        cell, path = visit.popleft()
        if max_steps is not None:
            if len(path) == max_steps:
                return len(visited)
        elif cell == end:
            return path[1:] + [cell]

        for direction in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            new_x = cell[0] + direction[0]
            new_y = cell[1] + direction[1]
            if new_x > -1 and new_y > -1 and (new_x, new_y) not in visited:
                if office(new_x, new_y):
                    visited.add((new_x, new_y))
                    visit.append(((new_x, new_y), path + [cell]))

    return None


if __name__ == '__main__':
    path = shortest_path((1, 1), (31, 39), 1362)
    print("The fewest number of steps needed to get to (31, 39) is", len(path))
    print("The number of locations you can read in 50 steps is", shortest_path((1, 1), None, 1362, 50))
