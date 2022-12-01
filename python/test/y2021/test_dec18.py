import unittest

from python.src.y2021.dec18 import SnailFish, Dec18


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

    def test_add(self):
        t1 = SnailFish.from_string("[[[[4,3],4],4],[7,[[8,4],9]]]")
        t2 = SnailFish.from_string("[1,1]")

        expected = SnailFish.from_string("[[[[0,7],4],[[7,8],[6,0]]],[8,1]]")
        self.assertEqual(expected,
                         t1 + t2)

    def test_add_multiple(self):
        data = [
            (["[1,1]", "[2,2]", "[3,3]", "[4,4]"],
             "[[[[1,1],[2,2]],[3,3]],[4,4]]"),
            (["[1,1]", "[2,2]", "[3,3]", "[4,4]", "[5,5]"],
             "[[[[3,0],[5,3]],[4,4]],[5,5]]"),
            (["[1,1]", "[2,2]", "[3,3]", "[4,4]", "[5,5]", "[6,6]"],
             "[[[[5,0],[7,4]],[5,5]],[6,6]]"),
            (
                [
                    "[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]",
                    "[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]",
                    "[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]",
                    "[[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]]",
                    "[7,[5,[[3,8],[1,4]]]]",
                    "[[2,[2,2]],[8,[8,1]]]",
                    "[2,9]",
                    "[1,[[[9,3],9],[[9,0],[0,7]]]]",
                    "[[[5,[7,4]],7],1]",
                    "[[[[4,2],2],6],[8,7]]"
                ],

                "[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]"
            )
        ]
        for terms, expected in data[:]:
            self.assertEqual(SnailFish.from_string(expected),
                             Dec18(instructions=terms).add_all())

    def test_magnitude(self):
        data = [
            # ("[9,1]", 29),
            ("[[9,1],[1,9]]", 129),
            ("[[1,2],[[3,4],5]]", 143),
            ("[[[[0,7],4],[[7,8],[6,0]]],[8,1]]", 1384),
            ("[[[[1,1],[2,2]],[3,3]],[4,4]]", 445),
            ("[[[[3,0],[5,3]],[4,4]],[5,5]]", 791),
            ("[[[[5,0],[7,4]],[5,5]],[6,6]]", 1137),
            ("[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]", 3488)
        ]

        for sf, magnitude in data:
            self.assertEqual(magnitude,
                             SnailFish.from_string(sf).magnitude())

    def test_part_1(self):
        data = [
            "[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]",
            "[[[5,[2,8]],4],[5,[[9,9],0]]]",
            "[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]",
            "[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]",
            "[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]",
            "[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]",
            "[[[[5,4],[7,7]],8],[[8,3],8]]",
            "[[9,3],[[9,9],[6,[4,9]]]]",
            "[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]",
            "[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]"
        ]
        self.assertEqual(4140, Dec18(instructions=data).part_1())

    def test_part_2(self):
        data = [
            "[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]",
            "[[[5,[2,8]],4],[5,[[9,9],0]]]",
            "[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]",
            "[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]",
            "[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]",
            "[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]",
            "[[[[5,4],[7,7]],8],[[8,3],8]]",
            "[[9,3],[[9,9],[6,[4,9]]]]",
            "[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]",
            "[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]"
        ]
        self.assertEqual(3993,
                         Dec18(instructions=data).part_2())