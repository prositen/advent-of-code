from python.src.common import Day, timer, Timer


class Dec05(Day, year=2022, day=5):

    def __init__(self, instructions=None, filename=None):
        super().__init__(instructions=instructions, filename=filename)
        self.stacks, self.moves = self.instructions

    @staticmethod
    def parse_instructions(instructions):
        groups = Dec05.parse_groups(instructions=instructions)
        moves = []
        for g in groups[1]:
            s = g.split(' ')
            moves.append((int(s[1]), int(s[3]) - 1, int(s[5]) - 1))

        stacks = list()
        for row in groups[0][-2::-1]:
            for index in range(0, len(row), 4):
                if stack := row[index:index + 4].strip():
                    crate_index = index // 4
                    if crate_index >= len(stacks):
                        stacks.append(list())
                    stacks[crate_index].append(stack[1])
        return stacks, moves

    @timer(part=1)
    def part_1(self):
        stacks = [list(s) for s in self.stacks]
        for (count, _from, _to) in self.moves:
            for _ in range(count):
                stacks[_to].append(stacks[_from].pop())
        return ''.join(s[-1] if s else '' for s in stacks)

    @timer(part=2)
    def part_2(self):
        stacks = [list(s) for s in self.stacks]
        for (count, _from, _to) in self.moves:
            stacks[_to].extend(stacks[_from][-count:])
            stacks[_from] = stacks[_from][:-count]
        return ''.join(s[-1] if s else '' for s in stacks)


if __name__ == '__main__':
    with Timer('Total'):
        Dec05().run_day()
