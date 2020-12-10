from python.src.common import Day, timer, Timer


class Dec22(Day):

    def __init__(self, instructions=None, filename=None):
        super().__init__(2019, 22, instructions, filename)
        self.cards = list()

    @staticmethod
    def parse_instructions(instructions):
        return instructions

    def shuffle(self, cards, reset=True):
        if reset:
            self.cards = list(range(cards))
        for technique in self.instructions:
            if technique.startswith('cut'):
                n = int(technique[4:])
                self.cards = self.cards[n:] + self.cards[:n]
            elif technique == 'deal into new stack':
                self.cards = self.cards[::-1]
            elif technique.startswith('deal'):
                n = int(technique[20:])
                new_cards = [0] * cards
                for i, c in enumerate(self.cards):
                    new_cards[(n * i) % cards] = c
                self.cards = new_cards

    @timer(part=1)
    def part_1(self):
        self.shuffle(10007)
        return self.cards.index(2019)


if __name__ == '__main__':
    with Timer('Total'):
        d = Dec22()
        d.part_1()
        d.part_2()
