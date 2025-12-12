from python.src.common import Day, timer, Timer


class Tree:
    def __init__(self, presents, areas):
        self.present_shapes = presents
        self.present_sizes = [
            ''.join(p).count('#') for p in presents
        ]
        self.needed_presents = areas[1]
        self.tree_area = areas[0][0] * areas[0][1]

    def can_fit_basic(self):
        total_count = sum(present * count
                          for present, count in zip(self.present_sizes, self.needed_presents))
        return total_count <= self.tree_area


class Dec12(Day, year=2025, day=12, title='Christmas Tree Farm'):
    @staticmethod
    def parse_instructions(instructions):
        presents = list()
        areas = list()
        parsing_areas = False
        present = []
        for i, line in enumerate(instructions):
            if parsing_areas:
                size, packages = line.split(':', 1)
                size = tuple(map(int, size.split('x')))
                packages = tuple(map(int, packages.split()))
                areas.append((size, packages))
            else:
                if line == '':
                    presents.append(list(v for v in present))
                    present = []
                    if 'x' in instructions[i + 1]:
                        parsing_areas = True
                elif '.' in line or '#' in line:
                    present.append(line)
        return presents, areas

    @timer(part=1)
    def part_1(self):
        presents = self.instructions[0]
        areas = self.instructions[1]
        return sum(Tree(presents, area).can_fit_basic() for area in areas)


if __name__ == '__main__':
    with Timer('Total'):
        Dec12().run_day()
