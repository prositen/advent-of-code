import itertools
from collections import Counter, deque, defaultdict

from python.src.common import Day, timer, Timer


class Dec21(Day):

    def __init__(self, instructions=None, filename=None):
        super().__init__(2021, 21, instructions=instructions, filename=filename)

    @staticmethod
    def parse_instructions(instructions):
        return [int(line.split(' ')[-1], 10) for line in instructions]

    @staticmethod
    def update(pos, score, roll):
        pos = (pos + roll - 1) % 10 + 1
        score += pos
        return pos, score

    @timer(part=1)
    def part_1(self):
        pos = [c for c in self.instructions]
        scores = [0, 0]
        dice = 0
        while True:
            for i in (0, 1):
                roll = (3 * dice + 6)
                dice += 3
                pos[i], scores[i] = self.update(pos[i], scores[i], roll)
                if scores[i] >= 1000:
                    return dice * min(scores)

    @timer(part=2)
    def part_2(self):
        dice_rolls = Counter(
            sum(dice) for dice in itertools.product((1, 2, 3), repeat=3)
        )
        winner = [0, 0]
        to_visit = Counter({
            ((self.instructions[0], self.instructions[1]), (0, 0), 0)
        })
        while to_visit:
            next_visit = Counter()
            for (pos, score, player), seen in to_visit.items():
                for roll, amount in dice_rolls.items():
                    new_pos = list(pos)
                    new_score = list(score)
                    new_pos[player], new_score[player] = self.update(pos[player],
                                                                     score[player],
                                                                     roll)
                    if new_score[player] >= 21:
                        winner[player] += seen * amount
                    else:
                        next_visit[(tuple(new_pos),
                                    tuple(new_score), 1-player)] += (seen * amount)
            to_visit = next_visit
        return max(winner)


if __name__ == '__main__':
    with Timer('Total'):
        Dec21().run_day()
