from python.src.common import Day, timer, Timer


class Dec02(Day, year=2022, day=2):

    @staticmethod
    def parse_instructions(instructions):
        return instructions

    SCORES_PART_1 = {
        'A X': 3 + 1,
        'A Y': 6 + 2,
        'A Z': 0 + 3,
        'B X': 0 + 1,
        'B Y': 3 + 2,
        'B Z': 6 + 3,
        'C X': 6 + 1,
        'C Y': 0 + 2,
        'C Z': 3 + 3
    }

    @timer(part=1, title='Part 1, hardcoded version')
    def part_1(self):
        return sum(self.SCORES_PART_1[s] for s in self.instructions)

    SCORES_PART_2 = {
        'A X': 0 + 3,
        'A Y': 3 + 1,
        'A Z': 6 + 2,
        'B X': 0 + 1,
        'B Y': 3 + 2,
        'B Z': 6 + 3,
        'C X': 0 + 2,
        'C Y': 3 + 3,
        'C Z': 6 + 1
    }

    @timer(part=2, title='Part 2, hardcoded version')
    def part_2(self):
        return sum(self.SCORES_PART_2[s] for s in self.instructions)


class Dec02_2(Dec02):
    @staticmethod
    def score_part_1(move):
        me = (ord(move[2]) - ord('X'))
        them = (ord(move[0]) - ord('A'))
        match (me - them) % 3:
            case 0:  # draw
                return 3 + me + 1
            case 1:  # win
                return 6 + me + 1
            case 2 | _:  # loss
                return me + 1

    @timer(part=1, title='Part 1, algorithmic version')
    def part_1(self):
        return sum(self.score_part_1(s) for s in self.instructions)

    @staticmethod
    def score_part_2(move):
        them = (ord(move[0]) - ord('A'))
        match move[2]:
            case 'X':  # loss
                me = (them - 1) % 3
                result = 0
            case 'Y':  # draw
                me = them
                result = 3
            case 'Z' | _:  # win
                me = (them + 1) % 3
                result = 6

        return result + me + 1

    @timer(part=2, title='Part 2, algorithmic version')
    def part_2(self):
        return sum(self.score_part_2(s) for s in self.instructions)


if __name__ == '__main__':
    with Timer('Total'):
        Dec02().run_day()
