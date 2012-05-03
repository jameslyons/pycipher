from pycipher import Bifid
import unittest

class TestBifid(unittest.TestCase):

    def test_encipher(self):
        keys = (('tgcmpfyxuiewdhbzrvalknqso',5),
                ('ezrxdkuatgvncmiwhsqpyfblo',6))
        plaintext = ('abcdefghiiklmnopqrstuvwxyzabcdefghiiklmnopqrstuvwxyz',
                     'abcdefghiiklmnopqrstuvwxyzabcdefghiiklmnopqrstuvwxyz')
        ciphertext = ('vchqefwfuospksiplpwzuwuwwaeeldwcfglizoprksoqugvfvxuf',
                      'gvdciztcgfoxclwhoshawmkxygvzcidtczfogclxhowhasmkwyxz')
        for i,key in enumerate(keys):
            enc = Bifid(*key).encipher(plaintext[i])
            self.assertEqual(enc.upper(), ciphertext[i].upper())

    def test_decipher(self):
        keys = (('tgcmpfyxuiewdhbzrvalknqso',5),
                ('ezrxdkuatgvncmiwhsqpyfblo',6))
        plaintext= ('abcdefghiiklmnopqrstuvwxyzabcdefghiiklmnopqrstuvwxyz',
                     'abcdefghiiklmnopqrstuvwxyzabcdefghiiklmnopqrstuvwxyz')
        ciphertext = ('vchqefwfuospksiplpwzuwuwwaeeldwcfglizoprksoqugvfvxuf',
                      'gvdciztcgfoxclwhoshawmkxygvzcidtczfogclxhowhasmkwyxz')
        for i,key in enumerate(keys):
            dec = Bifid(*key).decipher(ciphertext[i])
            self.assertEqual(dec.upper(), plaintext[i].upper())
            	
if __name__ == '__main__':
    unittest.main()
