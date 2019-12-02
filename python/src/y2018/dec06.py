import itertools

from python.src.common import Day


class Dec06(Day):

    def __init__(self, instructions=None, filename=None):
        super().__init__(2018, 6, instructions, filename)
        self.min_x = self.min_y = self.max_x = self.max_y = None
        self.all_distances = list()
        self.closest_area = list()
        self.generate_distances()

    @staticmethod
    def parse_instructions(instructions):
        return [tuple(map(int, c.split(','))) for c in instructions]

    def distance_to_coords(self, x1, y1):
        return sorted([(abs(x1 - x2) + abs(y1 - y2), i)
                       for i, (x2, y2) in enumerate(self.instructions)],
                      key=lambda x: x[0])

    def generate_distances(self):
        self.min_x = min(self.instructions, key=lambda i: i[0])[0]
        self.max_x = max(self.instructions, key=lambda i: i[0])[0]
        self.min_y = min(self.instructions, key=lambda i: i[1])[1]
        self.max_y = max(self.instructions, key=lambda i: i[1])[1]

        self.all_distances = list()
        self.closest_area = list()
        for y in range(self.min_y, self.max_y + 1):
            for x in range(self.min_x, self.max_x + 1):
                d = self.distance_to_coords(x, y)
                self.all_distances.append([dd[0] for dd in d])
                if d[0][0] < d[1][0]:
                    closest = d[0][1]
                else:
                    closest = -1
                self.closest_area.append((y, x, closest))

    def part_1(self):
        distances = list()
        borders = {-1}
        areas = set()
        for y, x, closest in self.closest_area:
            areas.add(closest)
            if (x == self.min_x) or (x == self.max_x) or (y == self.min_y) or (y == self.max_y):
                borders.add(closest)
            distances.append(closest)

        non_borders = areas - borders
        areas = [len(list(v)) for k, v in itertools.groupby(sorted(distances)) if k in non_borders]
        return max(areas)

    def part_2(self, max_distance=10000):
        distance_sum = map(sum, self.all_distances)
        within_distance = filter(lambda x: x < max_distance, distance_sum)
        return len(list(within_distance))


if __name__ == '__main__':
    day = Dec06()
    print("Max area: ", day.part_1())
    print("Min total distance:", day.part_2())
