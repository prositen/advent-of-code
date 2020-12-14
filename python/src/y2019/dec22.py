from collections import deque

from python.src.common import Day, timer, Timer


class Dec22(Day):

    def __init__(self, instructions=None, filename=None):
        super().__init__(2019, 22, instructions, filename)
        self.cards = list()

    @staticmethod
    def parse_instructions(instructions):
        result = list()
        for row in instructions:
            tech, *_, n = row.split(' ')
            result.append((tech, int(n) if n != 'stack' else n))
        return result

    def shuffle(self, cards):
        self.cards = list(range(cards))
        for tech, n in self.instructions:
            if tech == 'cut':
                self.cards = self.cards[n:] + self.cards[:n]
            elif tech == 'deal' and n == 'stack':
                self.cards = self.cards[::-1]
            elif tech == 'deal':
                new_cards = [0] * cards
                for i, c in enumerate(self.cards):
                    new_cards[(n * i) % cards] = c
                self.cards = new_cards

    def find_position_of(self, card, size):
        offset = 0
        multiplier = 1
        a, b = 0, 0
        for tech, n in self.instructions:
            if tech == 'cut':
                a, b = 1, -n
            elif tech == 'deal' and n == 'stack':
                a, b = -1, -1
            elif tech == 'deal':
                a, b = n, 0
            multiplier = (a * multiplier) % size
            offset = (a * offset + b) % size
        return ((multiplier * card) + offset) % size

    def find_card_at(self, size):
        offset = 0
        multiplier = 1
        a, b = 0, 0
        for tech, n in self.instructions:
            if tech == 'cut':
                offset += n * multiplier
            elif tech == 'deal' and n == 'stack':
                multiplier *= -1
                offset += multiplier
            elif tech == 'deal':
                multiplier *= pow(n, -1, size)  # "Inverse" deal
            multiplier %= size
            offset %= size
        return multiplier, offset

    @timer(part=1)
    def part_1(self):
        size = 10007
        card = 2019
        return self.find_position_of(size=size, card=card)

    @timer(part=2)
    def part_2(self):
        size = 119315717514047
        iterations = 101741582076661
        index = 2020
        multiplier, offset = self.find_card_at(size)
        # Multipliers: just m * m * .... * m
        all_multipliers = pow(multiplier, iterations, size)
        # Additions, ugh I don't even know
        all_additions = (offset *
                         (pow(multiplier, iterations, size) - 1) *
                         (pow(multiplier - 1, -1, size)))

        return (index * all_multipliers + all_additions) % size


if __name__ == '__main__':
    with Timer('Total'):
        d = Dec22()
        d.part_1()
        d.part_2()
