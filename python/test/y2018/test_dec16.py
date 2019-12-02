import unittest

from python.src.y2018.dec16 import Dec16, Device


class TestDec16(unittest.TestCase):

    def test_parse(self):
        instructions = [
            "Before: [3, 2, 1, 1]",
            "9 2 1 2",
            "After:  [3, 2, 2, 1]",
            "1 1 1 1",
        ]

        d = Dec16(instructions=instructions)
        self.assertEqual([(
            [3, 2, 1, 1],
            [9, 2, 1, 2],
            [3, 2, 2, 1]
        )], d.samples)

    def test_sample(self):
        sample = (
            [3, 2, 1, 1],
            [9, 2, 1, 2],
            [3, 2, 2, 1]
        )
        d = Device()
        matches = d.sample(sample[0], sample[1], sample[2])
        self.assertEqual(3, len(matches))
        self.assertListEqual(['addi', 'mulr', 'seti'], sorted(matches))
