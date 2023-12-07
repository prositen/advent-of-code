from collections import Counter
from enum import Enum

from python.src.common import Day, timer, Timer


class HandType(int, Enum):
    HIGH_CARD = 1
    ONE_PAIR = 2
    TWO_PAIRS = 3
    THREE_OF_A_KIND = 4
    FULL_HOUSE = 5
    FOUR_OF_A_KIND = 6
    FIVE_OF_A_KIND = 7


def translate_cards(cards, j_is_joker=False):
    """
    Replace the non-numeric card values with
    A-E (part 1) / 1A-D  (part 2) so they sort properly using
    normal string comparison
    :param cards:
    :param j_is_joker:
    :return:
    """
    if j_is_joker:
        tr = str.maketrans('AKQJT', 'DCB1A')
    else:
        tr = str.maketrans('AKQJT', 'EDCBA')
    return cards.translate(tr)


class Hand(object):

    def __init__(self, cards, j_is_joker=False):
        self.cards = cards  # Keep the original values too, for easier debugging
        self.card_values = translate_cards(cards, j_is_joker=j_is_joker)
        self.hand_type = None
        self.j_is_joker = j_is_joker
        self.classify_hand()

    def classify_hand(self):
        card_count = Counter(self.card_values)
        joker_count = card_count['1']
        match len(card_count):
            case 1:
                self.hand_type = HandType.FIVE_OF_A_KIND
            case 2:
                # 4 + 1 or 3 + 2
                if joker_count:
                    self.hand_type = HandType.FIVE_OF_A_KIND
                else:
                    if 4 in card_count.values():
                        self.hand_type = HandType.FOUR_OF_A_KIND
                    else:
                        self.hand_type = HandType.FULL_HOUSE
            case 3:
                # 3 + 1 + 1 or 2 + 2 + 1
                if 3 in card_count.values():
                    if joker_count:
                        self.hand_type = HandType.FOUR_OF_A_KIND
                    else:
                        self.hand_type = HandType.THREE_OF_A_KIND
                else:
                    match joker_count:
                        case 1:
                            self.hand_type = HandType.FULL_HOUSE
                        case 2:
                            self.hand_type = HandType.FOUR_OF_A_KIND
                        case _:
                            self.hand_type = HandType.TWO_PAIRS
            case 4:
                # 2 + 1 + 1 + 1
                if joker_count:
                    self.hand_type = HandType.THREE_OF_A_KIND
                else:
                    self.hand_type = HandType.ONE_PAIR
            case 5 | _:
                # 1 + 1 + 1 + 1 +1
                if joker_count:
                    self.hand_type = HandType.ONE_PAIR
                else:
                    self.hand_type = HandType.HIGH_CARD

    def __repr__(self):
        return self.cards

    def __lt__(self, other):
        return (self.hand_type < other.hand_type or
                (self.hand_type == other.hand_type and self.card_values < other.card_values))


class Dec07(Day, year=2023, day=7):

    @staticmethod
    def parse_instructions(instructions):
        return [((s := line.split(maxsplit=1))[0], int(s[1])) for line in instructions]

    @timer(part=1)
    def part_1(self):
        hands = [(Hand(cards), score) for cards, score in self.instructions]
        return sum(hand[1] * rank
                   for rank, hand in enumerate(sorted(hands), start=1))

    @timer(part=2)
    def part_2(self):
        hands = [(Hand(cards, j_is_joker=True), score) for cards, score in self.instructions]
        return sum(hand[1] * rank
                   for rank, hand in enumerate(sorted(hands), start=1))


if __name__ == '__main__':
    with Timer('Total'):
        Dec07().run_day()
