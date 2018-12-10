import unittest

from python.src.y2018.dec10 import Dec10


class TestDec10(unittest.TestCase):

    def setUp(self):
        instructions = [
            'position=< 9,  1> velocity=< 0,  2>',
            'position=< 7,  0> velocity=<-1,  0>',
            'position=< 3, -2> velocity=<-1,  1>',
            'position=< 6, 10> velocity=<-2, -1>',
            'position=< 2, -4> velocity=< 2,  2>',
            'position=<-6, 10> velocity=< 2, -2>',
            'position=< 1,  8> velocity=< 1, -1>',
            'position=< 1,  7> velocity=< 1,  0>',
            'position=<-3, 11> velocity=< 1, -2>',
            'position=< 7,  6> velocity=<-1, -1>',
            'position=<-2,  3> velocity=< 1,  0>',
            'position=<-4,  3> velocity=< 2,  0>',
            'position=<10, -3> velocity=<-1,  1>',
            'position=< 5, 11> velocity=< 1, -2>',
            'position=< 4,  7> velocity=< 0, -1>',
            'position=< 8, -2> velocity=< 0,  1>',
            'position=<15,  0> velocity=<-2,  0>',
            'position=< 1,  6> velocity=< 1,  0>',
            'position=< 8,  9> velocity=< 0, -1>',
            'position=< 3,  3> velocity=<-1,  1>',
            'position=< 0,  5> velocity=< 0, -1>',
            'position=<-2,  2> velocity=< 2,  0>',
            'position=< 5, -2> velocity=< 1,  2>',
            'position=< 1,  4> velocity=< 2,  1>',
            'position=<-2,  7> velocity=< 2, -2>',
            'position=< 3,  6> velocity=<-1, -1>',
            'position=< 5,  0> velocity=< 1,  0>',
            'position=<-6,  0> velocity=< 2,  0>',
            'position=< 5,  9> velocity=< 1, -2>',
            'position=<14,  7> velocity=<-2,  0>',
            'position=<-3,  6> velocity=< 2, -1>'
        ]
        self.d = Dec10(instructions)

    def test_part_1(self):
        expected = \
            "#...#..###\n" \
            "#...#...#.\n" \
            "#...#...#.\n" \
            "#####...#.\n" \
            "#...#...#.\n" \
            "#...#...#.\n" \
            "#...#...#.\n" \
            "#...#..###"
        self.assertEqual(expected, str(self.d.part_1()))

    def test_part_2(self):
        self.assertEqual(3, self.d.part_2())
