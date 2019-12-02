#!/usr/bin/python
import unittest

from python.src.y2016 import dec11


class Dec11Tests(unittest.TestCase):
    def test_part_1(self):
        self.instructions = [
            "The first floor contains a hydrogen-compatible "
            "microchip and a lithium-compatible microchip.",

            "The second floor contains a hydrogen generator.",
            "The third floor contains a lithium generator.",
            "The fourth floor contains nothing relevant."]
        self.factory = dec11.Factory(self.instructions)

        self.factory.run()
        self.assertEqual(11, self.factory.minimum_steps())
        for no, step in enumerate(self.factory.steps):
            print("Step", no)
            print(step)

    def test_safe_extra_generator(self):
        items = [[dec11.Item('lithium', 'generator'),
                  dec11.Item('strontium', 'generator'),
                  dec11.Item('strontium', 'microchip')]]
        self.assertTrue(dec11.Configuration(items=items).is_safe())

    def test_safe_extra_microchip(self):
        items = [[dec11.Item('lithium', 'generator'),
                  dec11.Item('lithium', 'microchip'),
                  dec11.Item('strontium', 'microchip')]]
        self.assertFalse(dec11.Configuration(items=items).is_safe())

    def test_configurations_equal(self):
        items1 = [[dec11.Item('lithium', 'generator'),
                   dec11.Item('lithium', 'microchip'),
                   dec11.Item('strontium', 'generator')]]
        cfg1 = dec11.Configuration(elevator_floor=1, items=items1)

        items2 = [[dec11.Item('lithium', 'generator'),
                   dec11.Item('strontium', 'microchip'),
                   dec11.Item('strontium', 'generator')]]
        cfg2 = dec11.Configuration(elevator_floor=1, items=items2)
        self.assertEqual(cfg1.configuration_key(),
                         cfg2.configuration_key())

    def test_lone_microchip_safe(self):
        self.assertTrue(
            dec11.Configuration(items=[[dec11.Item('lithium', 'microchip')]]).is_safe())

    def test_lone_generator_safe(self):
        self.assertTrue(
            dec11.Configuration(items=[[dec11.Item('lithium', 'generator')]]).is_safe())

    def test_configurations_differ(self):
        cfg1 = dec11.Configuration(elevator_floor=1, items=[[dec11.Item('lithium', 'generator'),
                                                             dec11.Item('lithium', 'microchip'),
                                                             dec11.Item('strontium',
                                                                        'generator')]])
        cfg2 = dec11.Configuration(elevator_floor=1, items=[[dec11.Item('strontium', 'generator'),
                                                             dec11.Item('lithium', 'microchip'),
                                                             dec11.Item('strontium',
                                                                        'microchip')]])
        self.assertNotEqual(cfg1.configuration_key(),
                            cfg2.configuration_key())


if __name__ == '__main__':
    unittest.main()
