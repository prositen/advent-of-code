#!/usr/bin/python
import unittest

from python.src.y2016 import dec20


class Dec20Tests(unittest.TestCase):

    def test_firewall(self):
        fw = dec20.Firewall(['5-8',
                             '0-2',
                             '4-7'])
        self.assertEquals(3, fw.lowest_not_blocked())

    def test_firewall_with_overlaps(self):
        fw = dec20.Firewall(['5-10',
                             '0-2',
                             '6-9',
                             '4-7'])
        self.assertEquals(3, fw.lowest_not_blocked())

    def test_len(self):
        self.assertEquals(1, len(dec20.Range(1,1)))
        self.assertEquals(11, len(dec20.Range(20, 30)))

    def test_allowed(self):
        fw = dec20.Firewall(['5-8',
                             '0-2',
                             '4-7'])
        self.assertEquals([dec20.Range(3, 3)], fw.allowed)

if __name__ == '__main__':
    unittest.main()


