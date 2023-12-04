from python.src.common import Day, timer, Timer


class Dec04(Day, year=2023, day=4):

    @staticmethod
    def parse_instructions(instructions):
        cards = list()
        for line in instructions:
            c = line.index(':')
            winning_numbers, my_numbers = line[c + 1:].split('|')
            winning_numbers = set(map(int, winning_numbers.split()))
            my_numbers = set(map(int, my_numbers.split()))
            cards.append((winning_numbers, my_numbers))
        return cards

    @timer(part=1)
    def part_1(self):
        score = 0
        for (winning, my) in self.instructions:
            if matching := winning.intersection(my):
                score += 2 ** (len(matching) - 1)
        return score

    @timer(part=2)
    def part_2(self):
        matching_numbers = [len(winning.intersection(my))
                            for (winning, my) in self.instructions]
        cards = {n: 1 for n in range(len(matching_numbers))}

        for card_no, matching in enumerate(matching_numbers):
            cards_of_this_type = cards[card_no]
            for m in range(matching):
                cards[card_no+m+1] += cards_of_this_type
        return sum(cards.values())


if __name__ == '__main__':
    with Timer('Total'):
        Dec04().run_day()
