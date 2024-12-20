import unittest

from python.src.y2024.dec20 import Dec20, Race


class TestDec20(unittest.TestCase):
    data = """###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############""".split('\n')

    def test_part_1(self):
        r = Race(self.data)
        cases = ((1, 64),
                 (1, 40),
                 (1, 38),
                 (1, 36),
                 (1, 20),
                 (3, 12),
                 (2, 10),
                 (4, 8),
                 (2, 6),
                 (14, 4),
                 (14, 2))
        r.count_cheats()
        for (expected, save) in cases:
            self.assertEqual(expected, r.found_cheats.get(save))

    def test_part_2(self):
        r = Race(self.data)
        cases = (
            (32,50),
            (31,52),
            (29,54),
            (39,56),
            (25,58),
            (23,60),
            (20,62),
            (19,64),
            (12,66),
            (14,68),
            (12,70),
            (22,72),
            (4,74),
            (3, 76)
        )
        r.count_cheats(skip=20)
        for (expected, save) in cases:
            self.assertEqual(expected, r.found_cheats.get(save))

if __name__ == '__main__':
    unittest.main()
