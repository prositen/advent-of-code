from python.src.y2016 import dec04
import unittest

__author__ = 'Anna Holmgren'


class Dec04Tests(unittest.TestCase):
    def test_valid_room1(self):
        self.assertTrue(dec04.valid_room('aaaaa-bbb-z-y-x-', 'abxyz'))

    def test_valid_room2(self):
        self.assertTrue(dec04.valid_room('a-b-c-d-e-f-g-h-', 'abcde'))

    def test_valid_room3(self):
        self.assertTrue(dec04.valid_room('not-a-real-room-', 'oarel'))

    def test_valid_room4(self):
        self.assertFalse(dec04.valid_room('totally-real-room-', 'decoy'))

    def test_valid_rooms(self):
        self.assertListEqual([('aaaaa-bbb-z-y-x', 123, 'abxyz'),
                              ('a-b-c-d-e-f-g-h', 987, 'abcde'),
                              ('not-a-real-room', 404, 'oarel')],
                             dec04.valid_rooms(['aaaaa-bbb-z-y-x-123[abxyz]',
                                                'a-b-c-d-e-f-g-h-987[abcde]',
                                                'not-a-real-room-404[oarel]',
                                                'totally-real-room-200[decoy]']))

    def test_sum_valid_sector_ids(self):
        self.assertEquals(1514,
                          dec04.sum_valid_sector_ids(['aaaaa-bbb-z-y-x-123[abxyz]',
                                                      'a-b-c-d-e-f-g-h-987[abcde]',
                                                      'not-a-real-room-404[oarel]',
                                                      'totally-real-room-200[decoy]']))

    def test_decrypt(self):
        self.assertEquals('very encrypted name',
                          dec04.decrypt_name('qzmt-zixmtkozy-ivhz', 343))
