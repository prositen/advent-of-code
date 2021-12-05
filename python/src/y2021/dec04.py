from python.src.common import Day, timer, Timer


class BingoCard(object):
    def __init__(self, card):
        self.number_to_position = dict()
        self.position_to_numbers = dict()
        self.marked = dict()
        self.bingo = False
        for y, line in enumerate(card):
            self.position_to_numbers[y] = dict()
            self.marked[y] = dict()
            for x, digit in enumerate(Day.parse_int_line([line], None)):
                self.number_to_position[digit] = (y, x)
                self.position_to_numbers[y][x] = digit
                self.marked[y][x] = False

    def print(self):
        for y in self.position_to_numbers:
            print()
            for x, digit in self.position_to_numbers[y].items():
                marked = self.marked[y][x]
                left = '[' if marked else ' '
                right = ']' if marked else ' '
                print(f'{left}{digit:02}{right} ', end='')
        print()

    def call(self, number):
        if number in self.number_to_position:
            y, x = self.number_to_position[number]
            self.marked[y][x] = True
            self.bingo |= self.check(y, x)

    def check(self, last_y, last_x):
        return (
                all(self.marked[y][last_x] for y in range(0, 5)) or
                all(self.marked[last_y][x] for x in range(0, 5))
        )

    def score(self):
        score = 0
        for y in range(0, 5):
            for x in range(0, 5):
                if not self.marked[y][x]:
                    score += self.position_to_numbers[y][x]
        return score

    def reset(self):
        for y in range(0, 5):
            for x in range(0, 5):
                self.marked[y][x] = False
        self.bingo = False


class Dec04(Day):

    def __init__(self, instructions=None, filename=None):
        super().__init__(2021, 4, instructions, filename)
        self.called_numbers, self.bingo_cards = self.instructions

    @staticmethod
    def parse_instructions(instructions):
        bingo_cards = [
            BingoCard(group) for group in Day.parse_groups(instructions[2:])
        ]
        called_numbers = Day.parse_int_line(instructions)
        return called_numbers, bingo_cards

    def play(self, to_win):
        cards = [card for card in self.bingo_cards]
        for number in self.called_numbers:
            next_cards = list()
            for index, card in enumerate(cards):
                card.call(number)
                if card.bingo:
                    if to_win or len(cards) == 1:
                        return number * card.score()
                else:
                    if not to_win:
                        next_cards.append(card)
            if not to_win:
                cards = next_cards

    @timer(part=1)
    def part_1(self):
        return self.play(to_win=True)

    @timer(part=2)
    def part_2(self):
        return self.play(to_win=False)


if __name__ == '__main__':
    with Timer('Total'):
        Dec04().run_day()
