from pycipher import Autokey
import unittest

class TestAutokey(unittest.TestCase):

    def test_encipher(self):
        keys = ('GERMAN',
                'CIPHERS')
        plaintext = ('abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz',
                     'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz')
        ciphertext = ('gftpesgikmoqsuwyacegikmoqsuwyacegikmoqsuwyacegikmoqs',
                      'cjrkiwyhjlnprtvxzbdfhjlnprtvxzbdfhjlnprtvxzbdfhjlnpr')
        for i,key in enumerate(keys):
            enc = Autokey(key).encipher(plaintext[i])
            self.assertEqual(enc.upper(), ciphertext[i].upper())

    def test_decipher(self):
        keys = ('GERMAN',
                'CIPHERS')
        plaintext= ('abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz',
                     'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz')
        ciphertext = ('gftpesgikmoqsuwyacegikmoqsuwyacegikmoqsuwyacegikmoqs',
                     'cjrkiwyhjlnprtvxzbdfhjlnprtvxzbdfhjlnprtvxzbdfhjlnpr')
        for i,key in enumerate(keys):
            dec = Autokey(key).decipher(ciphertext[i])
            self.assertEqual(dec.upper(), plaintext[i].upper())
            	
if __name__ == '__main__':
    unittest.main()
