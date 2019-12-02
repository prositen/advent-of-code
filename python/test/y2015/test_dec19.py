__author__ = 'Anna'

import unittest

from python.src.y2015 import dec19


class Dec19Tests(unittest.TestCase):

    def test_count_replace_example1(self):
        rules = ["H => HO",
                 "H => OH",
                 "O => HH"]
        start_string = "HOH"
        r = dec19.FusionFission(rules, start_string)
        self.assertEqual(4, len(r.one_step()))

    def test_count_replace_example2(self):
        rules = ["H => HO",
                 "H => OH",
                 "O => HH"]
        start_string = "HOHOHO"
        r = dec19.FusionFission(rules, start_string)
        self.assertEqual(7, len(r.one_step()))

    @unittest.skip
    def test_count_replace_example3(self):
        rules = ["H => OO"]
        start_string = "H2O"
        r = dec19.FusionFission(rules, start_string)
        rep = r.one_step()
        self.assertEqual("OO2O", rep[0])
        self.assertEqual(1, len(rep))

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
