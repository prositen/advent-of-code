__author__ = 'anna'

import unittest

from python.src.y2015 import dec15


class Dec15Tests(unittest.TestCase):
    ingredients = ['Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8',
                   'Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3']

    def test_best_recipe(self):
        result = dec15.best_recipe(self.ingredients, 100)
        self.assertEqual(62842880, result.score)
        self.assertEquals(44, result.measurements['Butterscotch'])
        self.assertEquals(56, result.measurements['Cinnamon'])

    def test_best_recipe_500_cals(self):
        result = dec15.best_recipe(self.ingredients, teaspoons=100, calories=500)
        self.assertEqual(57600000, result.score)
        self.assertEqual(40, result.measurements['Butterscotch'])
        self.assertEqual(60, result.measurements['Cinnamon'])
if __name__ == '__main__':
    unittest.main()
