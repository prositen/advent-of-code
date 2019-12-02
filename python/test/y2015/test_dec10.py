__author__ = 'Anna'

import unittest

from python.src.y2015 import dec10


class Dec10Tests(unittest.TestCase):

    def test_look_and_say_example1(self):
        self.assertEqual('11', dec10.look_and_say('1'))

    def test_look_and_say_example2(self):
        self.assertEqual('21', dec10.look_and_say('11'))

    def test_look_and_say_example3(self):
        self.assertEqual('1211', dec10.look_and_say('21'))

    def test_look_and_say_example4(self):
        self.assertEqual('111221', dec10.look_and_say('1211'))

    def test_look_and_say_example5(self):
        self.assertEqual('312211', dec10.look_and_say('111221'))


if __name__ == '__main__':
    unittest.main()
