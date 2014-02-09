from pycipher import Rot13
import unittest

class TestRot13(unittest.TestCase):

    def test_decipher(self):
        text = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        declist = ['nopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklm']
        dec = Rot13().decipher(text)
        self.assertEqual(dec.upper(), declist[0].upper())

    def test_encipher(self):
        text = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        enclist = ['nopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklm']
        enc = Rot13().encipher(text)
        self.assertEqual(enc.upper(), enclist[0].upper())
 