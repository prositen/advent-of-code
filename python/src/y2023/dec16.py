from python.src.common import Day, timer, Timer


class Contraption(object):
    def __init__(self, layout):
        self.layout = [
            [ch for ch in row]
            for row in layout
        ]
        self.max_y = len(layout)
        self.max_x = len(layout[0])

        self.beams = [((0, -1), (0, 1))]
        self.visited = set()

    def step(self):
        new_beams = list()
        for beam, delta in self.beams:
            new_pos = beam[0] + delta[0], beam[1] + delta[1]
            if (new_pos, delta) in self.visited:
                continue
            if 0 <= new_pos[0] < self.max_y and 0 <= new_pos[1] < self.max_x:
                self.visited.add((new_pos, delta))
                match self.layout[new_pos[0]][new_pos[1]]:
                    case '.':
                        new_beams.append((new_pos, delta))
                    case '|':
                        if delta[0] == 0:
                            new_beams.append((new_pos, (-1, 0)))
                            new_beams.append((new_pos, (1, 0)))
                        else:
                            new_beams.append((new_pos, delta))
                    case '-':
                        if delta[1] == 0:
                            new_beams.append((new_pos, (0, -1)))
                            new_beams.append((new_pos, (0, 1)))
                        else:
                            new_beams.append((new_pos, delta))
                    case '/':
                        new_beams.append((new_pos, (-delta[1], -delta[0])))
                    case '\\':
                        new_beams.append((new_pos, (delta[1], delta[0])))
        self.beams = new_beams

    def energized(self):
        cells = set(c[0] for c in self.visited)
        return len(cells)

    def run(self, start=None):
        self.visited = set()
        if start:
            self.beams = [start]
        while self.beams:
            self.step()


class Dec16(Day, year=2023, day=16):

    @timer(part=1)
    def part_1(self):
        c = Contraption(self.instructions)
        c.run()
        return c.energized()

    @timer(part=2)
    def part_2(self):
        c = Contraption(self.instructions)
        cell_count = 0
        for x in range(c.max_x):
            c.run(start=((-1, x), (1, 0)))
            cell_count = max(cell_count, c.energized())
            c.run(start=((c.max_y, x), (-1, 0)))
            cell_count = max(cell_count, c.energized())
        for y in range(c.max_y):
            c.run(start=((y, -1), (0, 1)))
            cell_count = max(cell_count, c.energized())
            c.run(start=((y, c.max_x), (0, -1)))
            cell_count = max(cell_count, c.energized())
        return cell_count


if __name__ == '__main__':
    with Timer('Total'):
        Dec16().run_day()
