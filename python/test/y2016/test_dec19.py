#!/usr/bin/python
import unittest

from python.src.y2016 import dec19


class Dec19Tests(unittest.TestCase):

    def test_remaining_elf(self):
        self.assertEquals(3, dec19.remaining_elf_dumb(5))
        self.assertEquals(7, dec19.remaining_elf_dumb(11))

    def test_steal_across(self):
        self.assertEquals(2, dec19.steal_across(5))
        self.assertEquals(2, dec19.steal_across(11))
if __name__ == '__main__':
    unittest.main()


