__author__ = 'anna'

import unittest

from python.src.y2015 import dec11


class Dec11Tests(unittest.TestCase):
    def test_password_validExample1(self):
        self.assertFalse(dec11.password_valid('hijklmmn'))

    def test_password_valid_example2(self):
        self.assertFalse(dec11.password_valid('abbceffg'))

    def test_password_valid_example3(self):
        self.assertFalse(dec11.password_valid('abbcegjk'))

    def test_next_password_example1(self):
        self.assertEquals('abcdffaa', dec11.next_password('abcdefgh'))

    def test_next_password_example2(self):
        self.assertEquals('ghjaabcc', dec11.next_password('ghijklmn'))

    def test_filter_bad(self):
        self.assertEquals('abcjaaa', dec11.filter_bad('abcijkl'))

if __name__ == '__main__':
    unittest.main()
