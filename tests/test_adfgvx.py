import pycipher
import unittest

class TestADFGVX(unittest.TestCase):
    def test_encipher(self):
        keys = (('ph0qg64mea1yl2nofdxkr3cvs5zw7bj9uti8','GERMAN'),
                ('dxkr3cvs5zw7bj9uti8ph0qg64mea1yl2nof','german'),
                ('ph0qg64mea1yl2nofdxkr3cvs5zw7bj9uti8','ciphers'))
        plaintext = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        ciphertext = ('GFXFFGXGDFAXDAVGDGXVADAAXXXFDDFGGGFDFAXDAVGDVDAGFAXVVXFDDFGGGFVVVAGFFAVVVAGFFAGXVADAAXXVDAGFAXVVGFXFFGXG',
                      'AXFXXAFAVAGFVGDDXVAXDFDDAAAGFFGVVVGVAGFVGDDXFVGAXGFDDAGFFGVVVGXXXDVGGDXXXDVGGDVAXDFDDAAFVGAXGFDDAXFXXAFA',
                      'DXADFFGXGVXDAGGGVXDAGGGDDFGVXVXFVDAXGDXADFFGXGDDFGVXVVAAFGXAVFXAAAVFFVGFGFDVAAFGXAVFXAAAVFFVGFGFDXFVDAXG')
        for i,key in enumerate(keys):
            enc = pycipher.ADFGVX(*key).encipher(plaintext)
            self.assertEqual(enc.upper(), ciphertext[i].upper())

    def test_decipher(self):
        keys = (('ph0qg64mea1yl2nofdxkr3cvs5zw7bj9uti8','german'),
                ('dxkr3cvs5zw7bj9uti8ph0qg64mea1yl2nof','GERMAN'))#,
                #('ph0qg64mea1yl2nofdxkr3cvs5zw7bj9uti8','ciphers'))
        plaintext = ('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ',
                     'Z1QI5T3XOYPBS9UDRH6N2GE87MZ1QI5T3XOYPBS9UDRH6N2GE87M')
        ciphertext =('GFXFFGXGDFAXDAVGDGXVADAAXXXFDDFGGGFDFAXDAVGDVDAGFAXVVXFDDFGGGFVVVAGFFAVVVAGFFAGXVADAAXXVDAGFAXVVGFXFFGXG')
                     
        for i,key in enumerate(keys):
            dec = pycipher.ADFGVX(*key).decipher(ciphertext)
            self.assertEqual(dec.upper(), plaintext[i].upper())
            	
if __name__ == '__main__':
    unittest.main()
