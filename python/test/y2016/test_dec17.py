#!/usr/bin/python
import unittest

from python.src.y2016 import dec17


class Dec17Tests(unittest.TestCase):

    def test_shortest_path_example1(self):
        self.assertEquals('DDRRRD', dec17.shortest_path('ihgpwlah'))

    def test_shortest_path_example2(self):
        self.assertEquals('DDUDRLRRUDRD', dec17.shortest_path('kglvqrro'))

    def test_shortest_path_example3(self):
        self.assertEquals('DRURDRUDDLLDLUURRDULRLDUUDDDRR', dec17.shortest_path('ulqzkmiv'))

    def test_longest_path_example1(self):
        self.assertEquals(370, dec17.longest_path('ihgpwlah'))

    def test_longest_path_example2(self):
        self.assertEquals(492, dec17.longest_path('kglvqrro'))

    def test_longest_path_example3(self):
        self.assertEquals(830, dec17.longest_path('ulqzkmiv'))

if __name__ == '__main__':
    unittest.main()
