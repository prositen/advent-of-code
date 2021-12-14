from collections import Counter

from python.src.common import Day, timer, Timer


class Dec14(Day):

    def __init__(self, instructions=None, filename=None):
        super().__init__(2021, 14, instructions, filename)
        self.template, self.mappings = self.instructions

    @staticmethod
    def parse_instructions(instructions):
        template = instructions[0]
        mappings = dict()
        for line in instructions[2:]:
            _from, _to = line.split('->')
            mappings[tuple(c for c in _from.strip())] = _to.strip()
        return template, mappings

    def run(self, steps=1):
        _pairs = Counter((c1, c2)
                         for c1, c2 in zip(self.template, self.template[1:] + ' '))
        for n in range(steps):
            _next_pairs = Counter()
            for pair, amount in _pairs.items():
                if _insert := self.mappings.get(pair):
                    _next_pairs[(pair[0], _insert)] += amount
                    _next_pairs[(_insert, pair[1])] += amount
                else:
                    _next_pairs[pair] += amount
            _pairs = _next_pairs
        common = Counter()
        for (n1, n2), value in _pairs.items():
            common[n1] += value
        common = common.most_common()
        return common[0][1] - common[-1][1]

    @timer(part=1)
    def part_1(self):
        return self.run(10)

    @timer(part=2)
    def part_2(self):
        return self.run(40)


if __name__ == '__main__':
    with Timer('Extended Polymerization'):
        Dec14().run_day()
