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
        self.id, self.x, self.y, self.width, self.height = map(int, m.groups())


class Fabric(object):

    def __init__(self, claims):
        self.claims = [Claim(row) for row in claims]
        self.fabric = defaultdict(list)
        self.claim()

    def claim(self):
        """
        Claim square inches by tagging them with the claim ID
        """
        for claim in self.claims:
            for x in range(claim.x, claim.x + claim.width):
                for y in range(claim.y, claim.y + claim.height):
                    self.fabric[(y, x)].append(claim.id)

    def overlapping_squares(self):
        """ Find the number of square inches with overlapping claims """
        return len([x for x in self.fabric.values() if len(x) > 1])

    def no_overlaps(self):
        """ Find the one claim that doesn't overlap with any other """
        ids = {
            c.id: set() for c in self.claims
        }
        for square_inch in self.fabric.values():
            for claim_id in square_inch:
                ids[claim_id].update(square_inch)

        ids_without_overlap = [list(v)[0] for v in ids.values() if len(v) == 1]
        assert len(ids_without_overlap) == 1
        return ids_without_overlap[0]


if __name__ == '__main__':
    with open(os.path.join(DATA_DIR, 'input.3.txt')) as fh:
        instructions = fh.readlines()
        fabric = Fabric(instructions)
        print("Overlapping squares: ", fabric.overlapping_squares())
        print("Non-overlapping claim:", fabric.no_overlaps())
