#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from sm4 import *


class TestPySM4(unittest.TestCase):
    clear_num = 0x0123456789abcdeffedcba9876543210
    mk = 0x0123456789abcdeffedcba9876543210
    cipher_num = 0x681edf34d206965e86b3e94f536e4246

    print(hex(encrypt(clear_num, mk,31)[1]))


    def test_encrypt(self):
        self.assertEqual(encrypt(self.clear_num, self.mk,32)[0],
                         self.cipher_num)


if __name__ == '__main__':
    unittest.main()