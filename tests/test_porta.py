from pycipher.porta import Porta
import unittest

class TestPorta(unittest.TestCase):

    def test_encipher(self):
        keys = ('HELLO','FORTIFICATION')
        plaintext = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        ciphertext = ('XZXYXPRPQPUWUFIFFJKAKKBCFCYWXWOQOPOTVTUHEEIJMJJABEBB',
                      'YUUUNQPTVNTRTCIKMIHKIIFBFFYUUUNQPTVNTRTCIKMIHKIIFBFF')
        for i,key in enumerate(keys):
            enc = Porta(key).encipher(plaintext)
            self.assertEqual(enc.upper(), ciphertext[i].upper())

    def test_decipher(self):
        keys = ('HELLO','FORTIFICATION')
        ciphertext = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        plaintext = ('XZXYXPRPQPUWUFIFFJKAKKBCFCYWXWOQOPOTVTUHEEIJMJJABEBB',
                     'YUUUNQPTVNTRTCIKMIHKIIFBFFYUUUNQPTVNTRTCIKMIHKIIFBFF')
        for i,key in enumerate(keys):
            dec = Porta(key).decipher(ciphertext)
            self.assertEqual(dec.upper(), plaintext[i].upper())
            	
if __name__ == '__main__':
    unittest.main()
