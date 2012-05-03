from pycipher import Beaufort
import unittest

class TestBeaufort(unittest.TestCase):

    def test_encipher(self):
        keys = ('GERMAN',
                'CIPHERS')
        plaintext = ('abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz',
                     'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz')
        ciphertext = ('gdpjwiaxjdqcurdxkwolxreqifrlykczlfsewtfzmyqnztgskhtn',
                      'chneammvagxtffotzqmyyhmsjfrraflcykktyevrddmrxokwwfkq')
        for i,key in enumerate(keys):
            enc = Beaufort(key).encipher(plaintext[i])
            self.assertEqual(enc.upper(), ciphertext[i].upper())

    def test_decipher(self):
        keys = ('GERMAN',
                'CIPHERS')
        plaintext= ('abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz',
                     'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz')
        ciphertext = ('gdpjwiaxjdqcurdxkwolxreqifrlykczlfsewtfzmyqnztgskhtn',
                     'chneammvagxtffotzqmyyhmsjfrraflcykktyevrddmrxokwwfkq')
        for i,key in enumerate(keys):
            dec = Beaufort(key).decipher(ciphertext[i])
            self.assertEqual(dec.upper(), plaintext[i].upper())
            	
if __name__ == '__main__':
    unittest.main()
