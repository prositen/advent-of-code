from python.src.y2016 import dec02
import unittest

__author__ = 'Anna Holmgren'


class Dec02Tests(unittest.TestCase):
    def test_bathroom_code(self):
        self.assertEquals("1985", dec02.bathroom_code(["ULL",
                                                       "RRDDD",
                                                       "LURDL",
                                                       "UUUUD"], dec02.Standard(5)))

    def test_bathroom_code_designed(self):
        self.assertEquals("5DB3", dec02.bathroom_code(["ULL",
                                                       "RRDDD",
                                                       "LURDL",
                                                       "UUUUD"], dec02.Designed(5)))