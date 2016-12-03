from python.src.y2016 import dec03
import unittest

__author__ = 'Anna Holmgren'


class Dec03Tests(unittest.TestCase):
    def test_invalid_triangle(self):
        self.assertFalse(dec03.valid_triangle(5, 10, 25))

    def test_valid_triangle(self):
        self.assertTrue(dec03.valid_triangle(7, 10, 5))

    def test_convert_to_vertical(self):
        self.assertListEqual([(101, 102, 103),
                              (201, 202, 203),
                              (301, 302, 303),
                              (401, 402, 403),
                              (501, 502, 503),
                              (601, 602, 603)],
                             dec03.convert_to_vertical(
                                 [(101, 301, 501),
                                  (102, 302, 502),
                                  (103, 303, 503),
                                  (201, 401, 601),
                                  (202, 402, 602),
                                  (203, 403, 603)]))
