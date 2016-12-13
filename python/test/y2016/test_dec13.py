#!/usr/bin/python
import unittest

from python.src.y2016 import dec13


class Dec13Tests(unittest.TestCase):
    @unittest.skip
    def test_shortest_path_len(self):
        self.assertEquals(11, len(dec13.shortest_path(start=(1, 1), end=(7, 4), favorite_number=10)))

    def test_shortest_path(self):
        self.assertEquals([(1, 2),
                           (2, 2),
                           (3, 2),
                           (3, 3),
                           (3, 4),
                           (4, 4),
                           (4, 5),
                           (5, 5),
                           (6, 5),
                           (7, 5)],
                          dec13.shortest_path(start=(1, 1), end=(7, 5), favorite_number=10))

    def test_office_factory(self):
        # using a slightly different test case than in the example,
        # because there were two possible paths to that end cell.
        office = dec13.office_factory(10)
        self.assertEquals(["\t0123456789",
                           "0\t.#.####.##",
                           "1\t..#..#...#",
                           "2\t#....##...",
                           "3\t###.#.###.",
                           "4\t.##..#..#.",
                           "5\t..##....#.",
                           "6\t#...##.###"],
                          dec13.get_floorplan(office, 10, 7))


if __name__ == '__main__':
    unittest.main()
