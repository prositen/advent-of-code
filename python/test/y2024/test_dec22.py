import unittest

from python.src.y2024.dec22 import Dec22
from src.y2024.dec22 import Secret


class TestDec22(unittest.TestCase):
    data = ["1", "10", "100", "2024"]

    def test_generate_secrets(self):
        seed = 123
        secrets = [15887950, 16495136, 527345, 704524, 1553684,
                   12683156, 11100544, 12249484, 7753432, 5908254]
        secret_generator = Secret(seed)
        for secret in secrets:
            self.assertEqual(secret, secret_generator.next_secret())

    def test_part_1(self):
        self.assertEqual(37327623, Dec22(instructions=self.data).part_1())

    def test_part_2(self):
        self.assertEqual(0, Dec22(instructions=self.data).part_2())


if __name__ == '__main__':
    unittest.main()
