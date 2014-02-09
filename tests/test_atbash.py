from pycipher import Atbash
import unittest

class TestAtbash(unittest.TestCase):

    def test_decipher(self):
        text = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        declist = ['zyxwvutsrqponmlkjihgfedcbazyxwvutsrqponmlkjihgfedcba']
        dec = Atbash().decipher(text)
        self.assertEqual(dec.upper(), declist[0].upper())

    def test_encipher(self):
        text = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        enclist = ['zyxwvutsrqponmlkjihgfedcbazyxwvutsrqponmlkjihgfedcba']
        enc = Atbash().encipher(text)
        self.assertEqual(enc.upper(), enclist[0].upper())
 