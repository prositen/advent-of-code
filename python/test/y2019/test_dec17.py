import unittest

from python.src.y2019.dec17 import Dec17


class TestDec17(unittest.TestCase):

    def test_part_1(self):
        view = ["..#..........",
                "..#..........",
                "#######...###",
                "#.#...#...#.#",
                "#############",
                "..#...#...#..",
                "..#####...^.."]

        d = Dec17()
        self.assertEqual(76, d.alignment_parameters(view))


if __name__ == '__main__':
    unittest.main()
