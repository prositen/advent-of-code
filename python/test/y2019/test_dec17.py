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
        d.height = len(view)
        d.width = len(view[0])

        self.assertEqual(76, d.alignment_parameters(view))

    def test_part_2(self):
        d = Dec17()
        path = ['R', '8', 'R', '8', 'R', '4', 'R', '4', 'R', '8', 'L', '6', 'L', '2',
                'R', '4', 'R', '4', 'R', '8', 'R', '8', 'R', '8', 'L', '6', 'L', '2']
        sub = dict()
        main, sub['A'], sub['B'], sub['C'] = d.compress_path(path)
        result = ''
        for prog in main.split(','):
            result += sub[prog] + ','

        result = result[:-1]
        self.assertEqual(','.join(path), result)


if __name__ == '__main__':
    unittest.main()
