__author__ = 'Anna'

import unittest
from python.src import dec19


class Dec19Tests(unittest.TestCase):

    def test_count_replace_example1(self):
        rules = ["H => HO",
                 "H => OH",
                 "O => HH"]
        start_string = "HOH"
        self.assertEqual(4, len(dec19.replace_molecules(rules, start_string)))

    def test_count_replace_example2(self):
        rules = ["H => HO",
                 "H => OH",
                 "O => HH"]
        start_string = "HOHOHO"
        self.assertEqual(7, len(dec19.replace_molecules(rules, start_string)))

    @unittest.skip
    def test_count_replace_example3(self):
        rules = ["H => OO"]
        start_string = "H2O"
        rep = dec19.replace_molecules(rules, start_string)
        self.assertEqual(1, len(rep))
        self.assertEqual("OO2O", rep[0])

    def test_transform_example1(self):
        rule = dec19.Rule('H => OO')
        text = "H2O"
        expected = ["OO2O"]
        self.assertListEqual(sorted(expected), sorted(rule.transform_any(text)))

    def test_transform_example2(self):
        rule = dec19.Rule('H => OO')
        text = "H2H"
        expected = ["OO2H", "H2OO"]
        self.assertListEqual(sorted(expected), sorted(rule.transform_any(text)))


if __name__ == '__main__':
    unittest.main()
