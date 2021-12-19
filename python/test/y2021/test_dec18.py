import unittest

from python.src.y2021.dec18 import SnailFish


class TestDec18(unittest.TestCase):

    def test_explode(self):
        data = [
            ('[[[[[9,8],1],2],3],4]',
             '[[[[0,9],2],3],4]'),
            ('[7,[6,[5,[4,[3,2]]]]]',
             '[7,[6,[5,[7,0]]]]'),
            ('[[6,[5,[4,[3,2]]]],1',
             '[[6,[5,[7,0]]],3]'),
            ('[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]',
             '[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]'),
            ('[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]',
             '[[3,[2,[8,0]]],[9,[5,[7,0]]]]')
        ]
        for sf, expected in data:
            self.assertEqual(SnailFish.from_string(expected),
                             SnailFish.from_string(sf).explode())
