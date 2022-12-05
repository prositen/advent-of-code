from python.src.common import Day, timer, Timer


class Dec05(Day):

    def __init__(self, instructions=None, filename=None):
        super().__init__(2022, 5, instructions=instructions, filename=filename)
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
                    if crate_index <= len(stacks):
                        stacks.append(list())
                    stacks[crate_index].append(stack[1])
        return stacks, moves

    @timer(part=1)
    def part_1(self):
        stacks = [list(s) for s in self.stacks]
        for move in self.moves:
            for _ in range(move[0]):
                if stacks[move[1]]:
                    stacks[move[2]].append(stacks[move[1]].pop())
        return ''.join(s[-1] if s else '' for s in stacks)

    @timer(part=2)
    def part_2(self):
        stacks = [list(s) for s in self.stacks]
        for move in self.moves:
            mover = list()
            for _ in range(move[0]):
                mover.append(stacks[move[1]].pop())
            stacks[move[2]].extend(mover[::-1])
        return ''.join(s[-1] if s else '' for s in stacks)


if __name__ == '__main__':
    with Timer('Total'):
        Dec05().run_day()
