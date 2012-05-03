from pycipher import ColTrans
import unittest

class TestColtrans(unittest.TestCase):

    def test_encipher(self):
        keys = ('GERMAN',
                'CIPHERS')
        plaintext = ('abcdefghijklmnopqrstuvwxyz',
                     'abcdefghijklmnopqrstuvwxyz')
        ciphertext = ('EKQWBHNTZAGMSYDJPVFLRXCIOU',
                      'AHOVELSZDKRYBIPWCJQXFMTGNU')
        for i,key in enumerate(keys):
            enc = ColTrans(key).encipher(plaintext[i])
            self.assertEqual(enc.upper(), ciphertext[i].upper())

    def test_decipher(self):
        keys = ('GERMAN',
                'CIPHERS')
        plaintext= ('abcdefghijklmnopqrstuvwxyz',
                     'abcdefghijklmnopqrstuvwxyz')
        ciphertext = ('EKQWBHNTZAGMSYDJPVFLRXCIOU',
                     'AHOVELSZDKRYBIPWCJQXFMTGNU')
        for i,key in enumerate(keys):
            dec = ColTrans(key).decipher(ciphertext[i])
            self.assertEqual(dec.upper(), plaintext[i].upper())
            	
if __name__ == '__main__':
    unittest.main()
