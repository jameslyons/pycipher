from pycipher.affine import Affine
import unittest

class TestAffine(unittest.TestCase):

    def test_decipher(self):
        ''' AffineSubstitution (test_decipher): test known ciphertext->plaintext pairs '''
        text = 'pmjgdaxurolifczwtqnkhebyvspmjgdaxurolifczwtqnkhebyvs'
        declist = ['yfmtahovcjqxelszgnubipwdkryfmtahovcjqxelszgnubipwdkr',
                   'onmlkjihgfedcbazyxwvutsrqponmlkjihgfedcbazyxwvutsrqp',
                   'jarizqhypgxofwnevmdulctkbsjarizqhypgxofwnevmdulctkbs',
                   'pmjgdaxurolifczwtqnkhebyvspmjgdaxurolifczwtqnkhebyvs',
                   'tmfyrkdwpibungzslexqjcvohatmfyrkdwpibungzslexqjcvoha',
                   'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz']
        for i,key in enumerate(((7,3),(3,25),(9,12),(1,0),(19,18),(23,15))):
            a,b = key
            dec = Affine(a,b).decipher(text)
            self.assertEqual(dec.upper(), declist[i].upper())        

    def test_encipher(self):
        ''' AffineSubstitution (test_encipher): test known plaintext->ciphertext pairs '''
        text = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        enclist = ['hijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefg',
                   'dgjmpsvybehknqtwzcfiloruxadgjmpsvybehknqtwzcfiloruxa',
                   'afkpuzejotydinsxchmrwbglqvafkpuzejotydinsxchmrwbglqv',
                   'ovcjqxelszgnubipwdkryfmtahovcjqxelszgnubipwdkryfmtah',
                   'sbktcludmvenwfoxgpyhqzirajsbktcludmvenwfoxgpyhqziraj',
                   'pmjgdaxurolifczwtqnkhebyvspmjgdaxurolifczwtqnkhebyvs']
        for i,key in enumerate(((1,7),(3,3),(5,0),(7,14),(9,18),(23,15))):
            a,b = key
            enc = Affine(a,b).encipher(text)
            self.assertEqual(enc.upper(), enclist[i].upper())          

    def test_punctuation(self):
        ''' AffineSubstitution (test_punctuation): punctuation should be unmodified '''
        e = Affine(a=7,b=8)
        original = '!@$%%^&*()_-+={}[]|":;<>,./?'
        enciphered = e.encipher(original,keep_punct=True)
        self.assertEqual(original.upper(), enciphered.upper())
        e = Affine(a=7,b=8)
        original = '!@$%%^&*()_-+={}[]|":;<>,./?'
        enciphered = e.encipher(original,keep_punct=False)
        self.assertEqual('', enciphered.upper())
