import re
from collections import defaultdict

from python.src.common import Day


class Claim(object):
    re_CLAIM = re.compile(r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)')

    def __init__(self, row):
        m = self.re_CLAIM.match(row)
        if not m:
            raise "Syntax error" + row
        self.id, self.x, self.y, self.width, self.height = map(int, m.groups())


class Dec03(Day):
    def __init__(self, instructions=None):
        super().__init__(2018, 3, instructions)
        self.fabric = defaultdict(list)
        self.claim()

    @staticmethod
    def parse_instructions(instructions):
        return [Claim(row) for row in instructions]

    def claim(self):
        """
        Claim square inches by tagging them with the claim ID
        """
        for claim in self.instructions:
            for x in range(claim.x, claim.x + claim.width):
                for y in range(claim.y, claim.y + claim.height):
                    self.fabric[(y, x)].append(claim.id)

    def part_1(self):
        """ Find the number of square inches with overlapping claims """
        return len([x for x in self.fabric.values() if len(x) > 1])

    def part_2(self):
        """ Find the one claim that doesn't overlap with any other """
        ids = {
            c.id: set() for c in self.instructions
        }
        for square_inch in self.fabric.values():
            for claim_id in square_inch:
                ids[claim_id].update(square_inch)

        ids_without_overlap = [list(v)[0] for v in ids.values() if len(v) == 1]
        assert len(ids_without_overlap) == 1
        return ids_without_overlap[0]


if __name__ == '__main__':
    d = Dec03()
    print("Overlapping squares: ", d.part_1())
    print("Non-overlapping claim:", d.part_2())
