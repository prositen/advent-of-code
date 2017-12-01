from python.src.y2017 import dec01

import unittest


class TestDec01(unittest.TestCase):
    def testCaptchaSum(self):
        cases = [(1122, 3),     # 1122 produces a sum of 3 (1 + 2) because the first digit (1) matches the
                                # second digit and the third digit (2) matches the fourth digit.
                 (1111, 4),     # 1111 produces 4 because each digit (all 1) matches the next.
                 (1234, 0),     # 1234 produces 0 because no digit matches the next.
                 (91212129, 9)  # 91212129 produces 9 because the only digit that matches
                                # the next one is the last digit, 9.
                 ]
        for number, hash in cases:
            self.assertEqual(hash, dec01.captcha_sum(number))

    def testHalfwaySum(self):
        cases = [(1212, 6),
                 (1221, 0),
                 (123425, 4),
                 (123123, 12),
                 (12131415, 4)]
        for number, hash in cases:
            self.assertEqual(hash, dec01.captcha_sum(number, halfway_sum=True))
