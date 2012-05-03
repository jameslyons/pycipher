from pycipher import Vigenere
import unittest

class TestVigenere(unittest.TestCase):

    def test_encipher(self):
        keys = ('GERMAN',
                'CIPHERS')
        plaintext = ('abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz',
                     'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz')
        ciphertext = ('gftpesmlzvkysrfbqeyxlhwkedrncqkjxtiwqpdzocwvjfuicbpl',
                      'cjrkiwyjqyrpdfqxfywkmxemfdrteltmkyalsatrfhszhaymozgo')
        for i,key in enumerate(keys):
            enc = Vigenere(key).encipher(plaintext[i])
            self.assertEqual(enc.upper(), ciphertext[i].upper())

    def test_decipher(self):
        keys = ('GERMAN',
                'CIPHERS')
        plaintext= ('abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz',
                     'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz')
        ciphertext = ('gftpesmlzvkysrfbqeyxlhwkedrncqkjxtiwqpdzocwvjfuicbpl',
                     'cjrkiwyjqyrpdfqxfywkmxemfdrteltmkyalsatrfhszhaymozgo')
        for i,key in enumerate(keys):
            dec = Vigenere(key).decipher(ciphertext[i])
            self.assertEqual(dec.upper(), plaintext[i].upper())
            	
if __name__ == '__main__':
    unittest.main()
