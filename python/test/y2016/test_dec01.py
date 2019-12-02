from python.src.y2016 import dec01
import unittest

__author__ = 'Anna Holmgren'


class Dec01Tests(unittest.TestCase):
    def testDistanceExample1(self):
        self.assertEqual(5, dec01.distance(["R2", "L3"]))

    def testDistanceExample2(self):
        self.assertEqual(2, dec01.distance(["R2", "R2", "R2"]))

    def testDistanceExample3(self):
        self.assertEqual(12, dec01.distance(["R5", "L5", "R5", "R3"]))

    def testVisitedTwice(self):
        position = dec01.visited_twice(["R8", "R4", "R4", "R8"])
        self.assertEqual(4, position)
