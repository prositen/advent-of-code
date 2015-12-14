__author__ = 'Anna'

import unittest
from python.src import dec12


class Dec12Tests(unittest.TestCase):
    def test_sum_numbers_example1(self):
        self.assertEqual(6, dec12.sum_numbers('[1,2,3]'))

    def test_sum_numbers_example2(self):
        self.assertEqual(6, dec12.sum_numbers('{"a":2,"b":4}'))

    def test_sum_numbers_example3(self):
        self.assertEqual(3, dec12.sum_numbers('[[[3]]]'))

    def test_sum_numbers_example4(self):
        self.assertEqual(3, dec12.sum_numbers('{"a":{"b":4},"c":-1}'))

    def test_sum_numbers_example5(self):
        self.assertEqual(0, dec12.sum_numbers('{"a":[-1,1]}'))

    def test_sum_numbers_example6(self):
        self.assertEqual(0, dec12.sum_numbers('[-1,{"a":1}]'))

    def test_sum_numbers_example7(self):
        self.assertEqual(0, dec12.sum_numbers('[]'))

    def test_sum_numbers_example8(self):
        self.assertEqual(0, dec12.sum_numbers('{}'))

    def test_skip_red_example1(self):
        self.assertEqual(6, dec12.sum_numbers('[1,2,3]', skip_red=True))

    def test_skip_red_example2(self):
        self.assertEqual(4, dec12.sum_numbers('[1,{"c":"red","b":2},3]', skip_red=True))

    def test_skip_red_example3(self):
        self.assertEqual(0, dec12.sum_numbers('{"d":"red","e":[1,2,3,4],"f":5}', skip_red=True))

    def test_skip_red_example4(self):
        self.assertEqual(6, dec12.sum_numbers('[1,"red",5]', skip_red=True))

if __name__ == '__main__':
    unittest.main()
