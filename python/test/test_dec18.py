__author__ = 'Anna'

import unittest
from python.src import dec18


class Dec18Tests(unittest.TestCase):

    def test_step_example1(self):
        grid = dec18.Grid(['.#.#.#',
                           '...##.',
                           '#....#',
                           '..#...',
                           '#.#..#',
                           '####..'])

        expected = dec18.Grid(['..##..',
                               '..##.#',
                               '...##.',
                               '......',
                               '#.....',
                               '#.##..'])

        self.assertEqual(str(expected), str(dec18.step(grid, 1)))

    def test_neighbours_example1(self):
        grid = dec18.Grid(['..',
                           '..'])

        self.assertEqual(0, grid.neighbours(0, 0))

    def test_neighbours_example2(self):
        grid = dec18.Grid(['.#',
                           '..'])
        self.assertEqual(1, grid.neighbours(1, 1))
        self.assertEqual(1, grid.neighbours(0, 0))
        self.assertEqual(1, grid.neighbours(1, 0))
        self.assertEqual(0, grid.neighbours(0, 1))

    def test_count_example1(self):
        grid = dec18.Grid(['.#',
                           '..'])
        self.assertEqual(1, grid.count())

    def test_count_example2(self):
        grid = dec18.Grid(['.#.#.#',
                           '...##.',
                           '#....#',
                           '..#...',
                           '#.#..#',
                           '####..'])
        self.assertEqual(15, grid.count())

    def test_broken_grid(self):
        grid = dec18.CornerLitGrid(['##.#.#',
                                    '...##.',
                                    '#....#',
                                    '..#...',
                                    '#.#..#',
                                    '####.#'])
        step = dec18.step(grid, 5)
        expected = dec18.CornerLitGrid(['##.###',
                                        '.##..#',
                                        '.##...',
                                        '.##...',
                                        '#.#...',
                                        '##...#'])


        self.assertEqual(str(expected), str(step))
        self.assertEqual(17, step.count())
if __name__ == '__main__':
    unittest.main()
