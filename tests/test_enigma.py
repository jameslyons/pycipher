from pycipher.enigma import Enigma
import unittest

class TestEnigma(unittest.TestCase):

    def test_decipher(self):
        'Enigma (test_decipher): try deciphering a few known pairs'
        text = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        declist = ['ZVEKPJXYYORZCJPOWSFVDROSCJIUOESGAIPCPOHLJSSWVKWOLEDH',
                   'SRBHDZXZESFHYOBCXLBUCOAYUQZPZBWLAYBOEEVJYOEEINLCIHIV',
                   'UNLLTTNBWKQEJFSUTGFQVTSGNQLSFEZVLUYDNUDZZKOIFGBYXGUJ',
                   'YYQULKSDHEGZECAIUKAZVSIENOQVUCSDZGNCAWUJAYJOTJCPTJOU']
        keys = [(('Q','W','R'),(3,2,4),'C',('R','T','W'),[('E','T'),('N','P')]),
                (('T','B','L'),(1,8,2),'B',('A','B','C'),[('U','P'),('Z','X'),('L','K')]),
                (('A','B','C'),(6,5,4),'C',('C','B','A'),[('B','V')]),
                (('E','W','Q'),(8,7,6),'B',('L','L','L'),[])]                
        for i,key in enumerate(keys):
            dec = Enigma(key[0],key[1],key[2],key[3],key[4]).decipher(text)
            self.assertEqual(dec.upper(), declist[i].upper())  
        
    def test_encipher(self):
        'Enigma (test_encipher): encipher operation is identical to decipher operation'
        text = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        declist = 'UNLLTTNBWKQEJFSUTGFQVTSGNQLSFEZVLUYDNUDZZKOIFGBYXGUJ'
        key = (('A','B','C'),(6,5,4),'C',('C','B','A'),[('B','V')])
        dec = Enigma(key[0],key[1],key[2],key[3],key[4]).encipher(text)
        self.assertEqual(dec.upper(), declist.upper())

        
#if __name__ == '__main__':
#    unittest.main()
