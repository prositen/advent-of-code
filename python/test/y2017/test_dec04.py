import unittest
from python.src.y2017 import dec04


class TestDec04(unittest.TestCase):
    def test_valid_passphrases(self):
        puzzle_input = [("aa bb cc dd ee", True),
                        ("aa bb cc dd aa", False),
                        ("aa bb cc dd aaa", True)]
        self.assertEqual(2, dec04.valid_passphrases([p[0] for p in puzzle_input]))
        for passphrase, valid in puzzle_input:
            self.assertEqual(valid, dec04.is_valid(passphrase))

    def test_anagram_passphrases(self):
        puzzle_input = [("abcde fghij", True),
                        ("abcde xyz ecdab", False),
                        ("a ab abc abd abf abj", True),
                        ("iiii oiii ooii oooi oooo", True),
                        ("oiii ioii iioi iiio", False)]
        self.assertEqual(3, dec04.valid_anagram_passphrases([p[0] for p in puzzle_input]))
        for passphrase, valid in puzzle_input:
            self.assertEqual(valid, dec04.is_valid_anagram(passphrase))
