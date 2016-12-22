#!/usr/bin/python
import unittest

from python.src.y2016 import dec22


class Dec22Tests(unittest.TestCase):
    def setUp(self):
        self.df = ["root@ebhq-gridcenter# df -h",
                   "Filesystem            Size  Used  Avail  Use%",
                   "/dev/grid/node-x0-y0   10T    8T     2T   80%",
                   "/dev/grid/node-x0-y1   11T    6T     5T   54%",
                   "/dev/grid/node-x0-y2   32T   28T     4T   87%",
                   "/dev/grid/node-x1-y0    9T    7T     2T   77%",
                   "/dev/grid/node-x1-y1    8T    0T     8T    0%",
                   "/dev/grid/node-x1-y2   11T    7T     4T   63%",
                   "/dev/grid/node-x2-y0   10T    6T     4T   60%",
                   "/dev/grid/node-x2-y1    9T    8T     1T   88%",
                   "/dev/grid/node-x2-y2    9T    6T     3T   66%"
                   ]
        self.grid = dec22.Grid(self.df, large=20)

    def test_get_viable_pairs(self):
        self.assertEqual({((0, 0), (1, 1)),
                          ((0, 1), (1, 1)),
                          ((1, 0), (1, 1)),
                          ((1, 2), (1, 1)),
                          ((0, 2), (1, 1)),
                          ((2, 1), (1, 1)),
                          ((2, 2), (1, 1))},
                         set(self.grid.viable_pairs()))

    def test_shortest_path(self):
        shortest_path = dec22.find_shortest_path(self.grid)
        self.assertEqual(7, shortest_path)


if __name__ == '__main__':
    unittest.main()
