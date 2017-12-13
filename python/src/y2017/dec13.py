import os

from python.src.y2017.common import DATA_DIR


# This took me far longer than it should have.
# First I spent too much time visualizing the firewall;
# this included simulating stepping through the model over time.
#
# I got the correct response for part 1 this way at least.
#
# For part 2, the result triggered too soon. Turned out it wasn't
# a good idea reusing the severity check straight off - if the scanners
# triggered only at position 0 that function would return 0 and the program
# would report that everything was ok. Oh well. What is a leaderboard..

class FireWall(object):
    def __init__(self, puzzle_input):
        self.layers = dict()
        self.parse(puzzle_input)

    def parse(self, puzzle_input):
        lines = [line.split(': ') for line in puzzle_input]
        self.layers = {int(line[0]): int(line[1]) for line in lines}

    @staticmethod
    def found_at_layer(layer, delay=0):
        return (layer[0] + delay) % (2 * layer[1] - 2) == 0

    def severity(self, delay=0, break_at_found=False):
        total = 0
        for layer in self.layers.items():
            if self.found_at_layer(layer, delay):
                if break_at_found:
                    return True
                else:
                    total += layer[0] * layer[1]
        return total

    def shortest_delay(self):
        delay = 1
        while self.severity(delay, break_at_found=True):
            delay += 1
        return delay


def main():
    with open(os.path.join(DATA_DIR, 'input.13.txt')) as fh:
        puzzle_input = fh.readlines()

    fw = FireWall(puzzle_input)
    print(fw.severity())
    print(fw.shortest_delay())


if __name__ == '__main__':
    main()
