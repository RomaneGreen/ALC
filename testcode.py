import unittest
from util import *


class enc_dec_test(unittest.TestCase):

    def does_it_encode(self):
        self.assertEqual(encode(0), hex(0x4000))
        self.assertEqual(encode(-8192), hex(0x0000))
        self.assertEqual(encode(8191), hex(0x7F7F))
        self.assertEqual(encode(2048), hex(0x505d))
        self.assertEqual(encode(-4096), hex(0x2000))

    def does_it_decode(self):
        self.assertEqual(decode(0x40, 0x00), 0)
        self.assertEqual(decode(0x00, 0x00), -8192)
        self.assertEqual(decode(0x7F, 0x7F), 8191)
        self.assertEqual(decode(0x50, 0x00), 2048)
        self.assertEqual(decode(0x0A, 0x05), -6097)
        self.assertEqual(decode(0x55, 0x00), 2688)

    def extract_test(self):
        self.assertEqual(divide_byte(0x4000), (0x40, 0x00))
        self.assertEqual(divide_byte(0x0000), (0x00, 0x00))
        self.assertEqual(divide_byte(0x7F7F), (0x7F, 0x7F))
        self.assertEqual(divide_byte(0x6000), (0x60, 0x00))
        self.assertEqual(divide_byte(0x8000), (0x80, 0x00))