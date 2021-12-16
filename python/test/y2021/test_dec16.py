import unittest

from python.src.y2021.dec16 import Dec16, Packet


class TestDec16(unittest.TestCase):

    def test_decode(self):
        data = [
            ('D2FE28', '110100101111111000101000'),
            ('38006F45291200', '00111000000000000110111101000101001010010001001000000000'),
            ('EE00D40C823060', '11101110000000001101010000001100100000100011000001100000')
        ]

        for hexstring, expected in data:
            self.assertEqual(expected,
                             Packet(hexstring=hexstring).bitstring)

    def test_literal(self):
        self.assertEqual(2021, Packet('D2FE28').value)

    def test_part_1(self):
        data = [
            ('8A004A801A8002F478', 16),
            ('620080001611562C8802118E34', 12),
            ('C0015000016115A2E0802F182340', 23),
            ('A0016C880162017C3686B18A3D4780', 31)
        ]
        for hexstring, expected in data:
            self.assertEqual(expected,
                             Dec16(instructions=[hexstring]).part_1())

    """
    
    C200B40A82 finds the sum of 1 and 2, resulting in the value 3.
    04005AC33890 finds the product of 6 and 9, resulting in the value 54.
    880086C3E88112 finds the minimum of 7, 8, and 9, resulting in the value 7.
    CE00C43D881120 finds the maximum of 7, 8, and 9, resulting in the value 9.
    D8005AC2A8F0 produces 1, because 5 is less than 15.
    F600BC2D8F produces 0, because 5 is not greater than 15.
    9C005AC2F8F0 produces 0, because 5 is not equal to 15.
    9C0141080250320F1802104A08 produces 1, because 1 + 3 = 2 * 2.

    """

    def test_part_2(self):
        data = [
            ('C200B40A82', 3),
            ('04005AC33890', 54),
            ('880086C3E88112', 7),
            ('CE00C43D881120', 9),
            ('D8005AC2A8F0', 1),
            ('F600BC2D8F', 0),
            ('9C005AC2F8F0', 0),
            ('9C0141080250320F1802104A08', 1)
        ]

        for hexstring, expected in data:
            self.assertEqual(expected,
                             Dec16(instructions=[hexstring]).part_2())
