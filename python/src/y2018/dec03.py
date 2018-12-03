import os
import re
from collections import defaultdict

from python.src.y2018.common import DATA_DIR


class Claim(object):
    re_CLAIM = re.compile(r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)')

    def __init__(self, row):
        m = self.re_CLAIM.match(row)
        if not m:
            raise "Syntax error" + row
        self.id = int(m.group(1))
        self.x = int(m.group(2))
        self.y = int(m.group(3))
        self.width = int(m.group(4))
        self.height = int(m.group(5))


class Fabric(object):

    def __init__(self, claims):
        self.claims = [Claim(row) for row in claims]
        self.fabric = defaultdict(list)
        self.claim()

    def claim(self):
        """
        Claim square inches by tagging them with the claim ID
        """
        self.fabric = defaultdict(list)
        for claim in self.claims:
            for x in range(claim.x, claim.x + claim.width):
                for y in range(claim.y, claim.y + claim.height):
                    self.fabric[(y, x)].append(claim.id)

    def overlapping_squares(self):
        """ Find the number of square inches with overlapping claims """
        overlaps = list(filter(lambda x: len(x) > 1, self.fabric.values()))
        return len(overlaps)

    def no_overlaps(self):
        """ Find the one claim that doesn't overlap with any other """
        ids = {
            c.id: set() for c in self.claims
        }
        for square_inch in self.fabric.values():
            for claim_id in square_inch:
                ids[claim_id].update(square_inch)

        ids_without_overlap = list(filter(lambda i: len(i) == 1, ids.values()))
        assert len(ids_without_overlap) == 1
        return next(iter(ids_without_overlap[0]))

    def print(self):
        """ Visualize the fabric with all the claims.

        Each square inch is marked with either:
            - the claim ID, if only one claim,
            - x if more than one claim
            - *claim_id* if this is the one non-overlapping claim.
        """
        id_width = len(str(max([c.id for c in self.claims]))) + 3
        n_o = self.no_overlaps()
        for y in range(1000):
            line = []
            for x in range(1000):
                claims = self.fabric.get((y,x))
                if not claims:
                    marker = '.'
                elif len(claims) == 1:
                    marker = next(iter(claims))
                    if marker == n_o:
                        marker = '*{}*'.format(marker)
                else:
                    marker = 'x'
                line.append('{marker:>{width}}'.format(marker=marker, width=id_width))
            print(''.join(line))


if __name__ == '__main__':
    with open(os.path.join(DATA_DIR, 'input.3.txt')) as fh:
        instructions = fh.readlines()
        fabric = Fabric(instructions)
        print("Overlapping squares: ", fabric.overlapping_squares())
        print("Non-overlapping claim:", fabric.no_overlaps())
