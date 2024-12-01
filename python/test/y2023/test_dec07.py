import unittest

from python.src.y2023.dec07 import Dec07, Hand, HandType


class TestDec07(unittest.TestCase):
    data = [
        "32T3K 765",
        "T55J5 684",
        "KK677 28",
        "KTJJT 220",
        "QQQJA 483"
    ]

    def test_hand_types(self):
        cases = (
            ('32T3K', HandType.ONE_PAIR),
            ('T55J5', HandType.THREE_OF_A_KIND),
            ('KK677', HandType.TWO_PAIRS),
            ('KTJJT', HandType.TWO_PAIRS),
            ('QQQJA', HandType.THREE_OF_A_KIND)
        )
        for (cards, hand_type) in cases:
            self.assertEqual(hand_type, Hand(cards).hand_type)

    def test_hand_types_j_is_joker(self):
        cases = (
            ('32T3K', HandType.ONE_PAIR),
            ('T55J5', HandType.FOUR_OF_A_KIND),
            ('KK677', HandType.TWO_PAIRS),
            ('KTJJT', HandType.FOUR_OF_A_KIND),
            ('QQQJA', HandType.FOUR_OF_A_KIND)
        )
        for (cards, hand_type) in cases:
            self.assertEqual(hand_type, Hand(cards, j_is_joker=True).hand_type, msg=cards)

    def test_sorting(self):
        cards = [Hand('32T3K'), Hand('T55J5'), Hand('KK677'),
                 Hand('KTJJT'), Hand('QQQJA')]
        expected = ['32T3K', 'KTJJT', 'KK677', 'T55J5', 'QQQJA']
        ranked_cards = sorted(cards)
        self.assertEqual(expected, [str(c) for c in ranked_cards])

    def test_sorting_j_is_joker(self):
        cards = [Hand('32T3K', j_is_joker=True), Hand('T55J5', j_is_joker=True),
                 Hand('KK677', j_is_joker=True),
                 Hand('KTJJT', j_is_joker=True), Hand('QQQJA', j_is_joker=True)]
        expected = ['32T3K', 'KK677', 'T55J5', 'QQQJA', 'KTJJT']
        ranked_cards = sorted(cards)
        self.assertEqual(expected, [str(c) for c in ranked_cards])

    def test_part_1(self):
        self.assertEqual(6440, Dec07(instructions=self.data).part_1())

    def test_part_2(self):
        self.assertEqual(5905, Dec07(instructions=self.data).part_2())


if __name__ == '__main__':
    unittest.main()
