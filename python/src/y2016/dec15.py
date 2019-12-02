import re


class Disc:
    re_DISC = re.compile(r"Disc #(\d+) has (\d+) positions; at time=0, it is at position (\d+).")

    def __init__(self, number, positions, start_position):
        self.number = number
        self.no_positions = positions
        self.start_position = start_position

    @staticmethod
    def from_string(line):
        result = Disc.re_DISC.match(line)
        if result:
            return Disc(int(result.group(1)), int(result.group(2)), int(result.group(3)))

    def position_at_time(self, time):
        return (self.start_position + time) % self.no_positions


def sequence_ok(start, discs):
    for disc in discs:
        if disc.position_at_time(start + disc.number) != 0:
            return False
    return True


def find_first_start(discs):
    number = 0
    while not sequence_ok(number, discs):
        number += 1
    return number


if __name__ == '__main__':
    with open('../../../data/2016/input.15.txt', 'r') as fh:
        disc_lines = fh.readlines()
        discs = [Disc.from_string(line) for line in disc_lines]
        first_start = find_first_start(discs)
        print("First possible start", first_start)
        discs.append(Disc(discs[-1].number + 1, 11, 0))
        first_start_part_2 = find_first_start(discs)
        print("First possible start", first_start_part_2)
