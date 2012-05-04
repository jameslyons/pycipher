from pycipher.caesar import Caesar
import unittest

class TestCaesar(unittest.TestCase):

    def test_decipher(self):
        ''' Caesar (test_decipher): test known ciphertext->plaintext pairs '''
        text = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        declist = ['xyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvw',
                   'vwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstu',
                   'stuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqr',
                   'pqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmno',
                   'lmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijk',
                   'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz',
                   'bcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyza']
        for i,key in enumerate((3,5,8,11,15,0,25)):
            dec = Caesar(key).decipher(text)
            self.assertEqual(dec.upper(), declist[i].upper())

    def test_encipher(self):
        ''' Caesar (test_encipher): test known plaintext->ciphertext pairs '''
        text = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        enclist = ['bcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyza',
                   'cdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzab',
                   'efghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcd',
                   'hijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefg',
                   'jklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghi',
                   'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz',
                   'zabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxy']
        for i,key in enumerate((1,2,4,7,9,0,25)):
            enc = Caesar(key).encipher(text)
            self.assertEqual(enc.upper(), enclist[i].upper())
 	
    def test_punctuation(self):
        ''' Caesar (test_punctuation): punctuation should remain unmodified '''
        e = Caesar(key=14)
        original = '!@$%%^&*()_-+={}[]|":;<>,./?'
        enciphered = e.encipher(original,keep_punct=True)
        self.assertEqual(original.upper(), enciphered.upper())
        e = Caesar(key=14)
        original = '!@$%%^&*()_-+={}[]|":;<>,./?'
        enciphered = e.encipher(original,keep_punct=False)
        self.assertEqual('', enciphered.upper())        