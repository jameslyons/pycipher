from pycipher import ADFGX
import unittest

class TestADFGX(unittest.TestCase):

    def test_encipher(self):
        keys = (('ypgknveqzxmdhwcblfisrauto','GERMAN'),
                ('haoqkzdmpieslycbwvgufntrx','CIPHERS'))
        plaintext = ('abcdefghiiklmnopqrstuvwxyzabcdefghiiklmnopqrstuvwxyz',
                     'abcdefghiiklmnopqrstuvwxyzabcdefghiiklmnopqrstuvwxyz')
        ciphertext = ('FGGGXXXDXFAGFAGDADDFGADXAAADFGXFGGGXFAGFAGDAGDFAADXFDADFGXFGGGXFGDXAFXXFGDXAFXDDFGADXAAGDFAADXFDFGGGXXXD',
                      'ADAXAGGGFADFAFXFADFAFXDFAFFFFDAXXDGXDADAXAGGGDFAFFFFDXGXXGGXGADFDDGADGADXXFXGXXGGXGADFDDGADGADXXFAXXDGXD')
        for i,key in enumerate(keys):
            enc = ADFGX(*key).encipher(plaintext[i])
            self.assertEqual(enc.upper(), ciphertext[i].upper())

    def test_decipher(self):
        keys = (('ypgknveqzxmdhwcblfisrauto','GERMAN'),
                ('haoqkzdmpieslycbwvgufntrx','CIPHERS'))
        plaintext = ('abcdefghiiklmnopqrstuvwxyzabcdefghiiklmnopqrstuvwxyz',
                     'abcdefghiiklmnopqrstuvwxyzabcdefghiiklmnopqrstuvwxyz')
        ciphertext = ('FGGGXXXDXFAGFAGDADDFGADXAAADFGXFGGGXFAGFAGDAGDFAADXFDADFGXFGGGXFGDXAFXXFGDXAFXDDFGADXAAGDFAADXFDFGGGXXXD',
                      'ADAXAGGGFADFAFXFADFAFXDFAFFFFDAXXDGXDADAXAGGGDFAFFFFDXGXXGGXGADFDDGADGADXXFXGXXGGXGADFDDGADGADXXFAXXDGXD')
        for i,key in enumerate(keys):
            dec = ADFGX(*key).decipher(ciphertext[i])
            self.assertEqual(dec.upper(), plaintext[i].upper())
            	
if __name__ == '__main__':
    unittest.main()
