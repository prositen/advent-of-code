import unittest

from python.src.y2019.dec22 import Dec22


class TestDec22(unittest.TestCase):

    def test_shuffle_1(self):
        data = ["deal with increment 7",
                "deal into new stack",
                "deal into new stack"]
        day = Dec22(instructions=data)
        day.shuffle(cards=10)
        self.assertEqual([0, 3, 6, 9, 2, 5, 8, 1, 4, 7], day.cards)

    def test_shuffle_2(self):
        data = ["cut 6",
                "deal with increment 7",
                "deal into new stack"]
        day = Dec22(instructions=data)
        day.shuffle(cards=10)
        self.assertEqual([3, 0, 7, 4, 1, 8, 5, 2, 9, 6], day.cards)

    def test_shuffle_3(self):
        data = ["deal with increment 7",
                "deal with increment 9",
                "cut -2"]
        day = Dec22(instructions=data)
        day.shuffle(cards=10)
        self.assertEqual([6, 3, 0, 7, 4, 1, 8, 5, 2, 9], day.cards)

    def test_part_1_d(self):
        data = ["deal into new stack",
                "cut -2",
                "deal with increment 7",
                "cut 8",
                "cut -4",
                "deal with increment 7",
                "cut 3",
                "deal with increment 9",
                "deal with increment 3",
                "cut -1"]
        day = Dec22(instructions=data)
        day.shuffle(cards=10)
        self.assertEqual([9, 2, 5, 8, 1, 4, 7, 0, 3, 6], day.cards)
        self.assertEqual(7, day.find_position_of(card=0, size=10))
