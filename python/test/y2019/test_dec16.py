import unittest

from python.src.y2019.dec16 import Dec16


class TestDec16(unittest.TestCase):

    def test_multiply_repeating_pattern(self):
        inputs = [9, 8, 7, 6, 5]
        pattern = [1, 2, 3]
        expected = [9, 16, 21, 6, 10]

        self.assertEqual(expected, Dec16.apply_pattern(inputs, pattern))

    def test_ftt_one_phase(self):
        signal = "12345678"
        d = Dec16(instructions=[signal])
        self.assertEqual("48226158", d.phase())

    def test_ftt_four_phases(self):
        signal = "12345678"
        d = Dec16(instructions=[signal])
        self.assertEqual("01029498", d.phase(phases=4))

    def test_ftt_100_phases(self):
        cases = [
            (["80871224585914546619083218645595"], "24176176"),
            (["19617804207202209144916044189917"], "73745418"),
            (["69317163492948606335995924319873"], "52432133")
        ]

        for signal, expected in cases:
            d = Dec16(instructions=signal)
            self.assertEqual(expected, d.part_1())

    def test_part_2(self):
        cases = [
            (["03036732577212944063491565474664"], "84462026"),
            (["02935109699940807407585447034323"], "78725270"),
            (["03081770884921959731165446850517"], "53553731")
        ]
        for signal, expected in cases:
            d = Dec16(instructions=signal)
            self.assertEqual(expected, d.part_2())

if __name__ == '__main__':
    unittest.main()
