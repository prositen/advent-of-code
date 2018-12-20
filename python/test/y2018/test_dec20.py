import unittest

from python.src.y2018.dec20 import Dec20


class TestDec20(unittest.TestCase):

    def test_part1(self):
        cases = [
            #(3, ['^WNE$']),
            #(10, ['^ENWWW(NEEE|SSE(EE|N))$']),
            (18, ['^ENNWSWW(NEWS|)SSSEEN(WNSE|)EE(SWEN|)NNN$'])
        ]

        for expected, instruction in cases:
            d = Dec20(instructions=instruction)
            self.assertEqual(expected, d.part_1())


