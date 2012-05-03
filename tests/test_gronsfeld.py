from pycipher import Gronsfeld
import unittest

class TestGronsfeld(unittest.TestCase):

    def test_encipher(self):
        keys = ([2,7,8,1,3,9,3],
                [2,7,8,1,0,3,9,3])
        plaintext = ('abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz',
                     'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz')
        ciphertext = ('cikehojjprlovqqwysvcxxdfzcjeekmgjqllrtnqxssyauxezzfh',
                      'cikeeipkkqsmmqxssyauuyfaagiccgniioqkkovqqwysswdyyega')
        for i,key in enumerate(keys):
            enc = Gronsfeld(key).encipher(plaintext[i])
            self.assertEqual(enc.upper(), ciphertext[i].upper())

    def test_decipher(self):
        keys = ([2,7,8,1,3,9,3],
                [2,7,8,1,0,3,9,3])
        plaintext= ('abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz',
                     'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz')
        ciphertext = ('cikehojjprlovqqwysvcxxdfzcjeekmgjqllrtnqxssyauxezzfh',
                     'cikeeipkkqsmmqxssyauuyfaagiccgniioqkkovqqwysswdyyega')
        for i,key in enumerate(keys):
            dec = Gronsfeld(key).decipher(ciphertext[i])
            self.assertEqual(dec.upper(), plaintext[i].upper())
            	
if __name__ == '__main__':
    unittest.main()
