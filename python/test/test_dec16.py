import dec16

__author__ = 'anna'

import unittest


class Dec16Tests(unittest.TestCase):
    aunt_lines = ["Sue 27: trees: 3, cars: 6, perfumes: 2",
                  "Sue 28: goldfish: 8, trees: 7, akitas: 10",
                  "Sue 29: children: 5, trees: 1, goldfish: 10"]

    def test_parse_aunt(self):
        line = "Sue 1: cars: 9, akitas: 3, goldfish: 0"
        aunt = dec16.Aunt(line)
        self.assertEqual(1, aunt.number)
        self.assertEquals(9, aunt.possessions['cars'])
        self.assertEquals(3, aunt.possessions['akitas'])
        self.assertEquals(0, aunt.possessions['goldfish'])
        self.assertNotIn('trees', aunt.possessions)

    def test_filter(self):
        tree_filter = dec16.filter_factory('trees', 3, False)
        aunts = [dec16.Aunt(line) for line in self.aunt_lines]
        filtered_aunts = list(filter(tree_filter, aunts))
        self.assertEquals(1, len(filtered_aunts))
        self.assertEquals(27, filtered_aunts[0].number)

    def test_filter_missing_data(self):
        akita_filter = dec16.filter_factory('akitas', 9, False)
        aunts = [dec16.Aunt(line) for line in self.aunt_lines]
        filtered_aunts = list(filter(akita_filter, aunts))
        self.assertEquals(2, len(filtered_aunts))

    def test_filter_retroencabulator_trees(self):
        tree_filter = dec16.filter_factory('trees', 2, True)
        aunts = [dec16.Aunt(line) for line in self.aunt_lines]
        filtered_aunts = list(filter(tree_filter, aunts))
        self.assertEquals(2, len(filtered_aunts))

    def test_filter_retroencabulator_goldfish(self):
        goldfish_filter = dec16.filter_factory('goldfish', 9, True)
        aunts = [dec16.Aunt(line) for line in self.aunt_lines]
        filtered_aunts = list(filter(goldfish_filter, aunts))
        self.assertEquals(2, len(filtered_aunts))
        self.assertEquals(27, filtered_aunts[0].number)
        self.assertEquals(28, filtered_aunts[1].number)

if __name__ == '__main__':
    unittest.main()
