from python.src.y2015 import dec25

__author__ = 'anna'

import unittest


class MyTestCase(unittest.TestCase):
    def test_example(self):
        codes = {1: {1: 20151125,
                     2: 18749137,
                     3: 17289845,
                     4: 30943339,
                     5: 10071777,
                     6: 33511524},
                 2: {1: 31916031,
                     2: 21629792,
                     3: 16929656,
                     4: 7726640,
                     5: 15514188,
                     6: 4041754},
                 3: {1: 16080970,
                     2: 8057251,
                     3: 1601130,
                     4: 7981243,
                     5: 11661866,
                     6: 16474243},
                 4: {1: 24592653,
                     2: 32451966,
                     3: 21345942,
                     4: 9380097,
                     5: 10600672,
                     6: 31527494},
                 5: {1: 77061,
                     2: 17552253,
                     3: 28094349,
                     4: 6899651,
                     5: 9250759,
                     6: 31663883},
                 6: {1: 33071741,
                     2: 6796745,
                     3: 25397450,
                     4: 24659492,
                     5: 1534922,
                     6: 27995004}
                 }

        #dec25.code(6, 6)
        #print(dec25.codes)
        for row_index, row in codes.items():
            for col_index, cell in row.items():
                #self.assertEqual(cell, dec25.codes[row_index][col_index], (row_index, col_index))
                self.assertEquals(cell, dec25.code(row_index, col_index), (row_index, col_index))


if __name__ == '__main__':
    unittest.main()
