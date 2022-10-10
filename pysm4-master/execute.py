#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pysm4 import *


class SM4_Execution:
    plain_text = 0x0123456789abcdeffedcba9876543210
    key = 0x0123456789abcdeffedcba9876543210
    #cipher_num = 0x681edf34d206965e86b3e94f536e4246

    cipher_text = encrypt(plain_text, key)
    dec_plain_text = decrypt(cipher_text, key)
    print(hex(cipher_text))
    print(hex(dec_plain_text))
    print(plain_text == dec_plain_text)

    print("---------------------------------------------------------------------------------------------------------")

    plain_text = '我冷眼向过去稍稍回顾，只见它曲折灌溉的悲喜，都消失在一片亘古的荒漠，'\
                 '这才知道我的全部努力，不过完成了普通的生活。'
    key = 'hello, world!'
    iv = '11111111'


    cipher_text = encrypt_ecb(plain_text=plain_text,key=key)
    dec_plain_text = decrypt_ecb(cipher_text,key=key)

    print(cipher_text)
    print(dec_plain_text)
    print(plain_text == dec_plain_text)

    print("---------------------------------------------------------------------------------------------------------")

    cipher_text=encrypt_cbc(plain_text=plain_text,key=key,iv=iv)
    dec_plain_text = decrypt_cbc(cipher_text,key=key,iv=iv)

    print(cipher_text)
    print(dec_plain_text)
    print(plain_text == dec_plain_text)



if __name__ == '__main__':
    SM4_Execution()
