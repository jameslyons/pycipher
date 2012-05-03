from pycipher.playfair import Playfair
import unittest

class TestPlayfair(unittest.TestCase):

    def test_decipher(self):
        ciphertext = 'abcdefghiklmnopqrstuvwxyzABCDEFGHIKLMNOPQRSTUVWXYZ'
        keys = ('lsfdpxwirnyveamoqgkchbtzu',
                'dytqplngirabskxcvoemzufwh',
                'ecsyinfmkpdrtuvgwqzbolaxh',
                'xquwfstzgeipboalykdnvrmch',
                'bxuthifmzrweasdovlpgcqnyk')
        plaintext = ['vzkpitotrgpyxcscwdbzwslxkruqfatetxodnpclkwfbbmxnah',
                   'xaazowrfqircgvqtgxyfeubpclavqcotwraivrmtpigfvbhkdu',
                   'hqercnboypafegmbtcrtrbzxqxwinonwbhfxfphnwtamtuzlxu',
                   'opdofhecblkvdatrvtzqcxqlebomngwevaynhkbiryesxmufkt',
                   'wukwfxdkrcauclvyzduxoetqmscoswrvbrngulglkfzyxlebpt']
        for i,key in enumerate(keys):
            dec = Playfair(key).decipher(ciphertext)
            self.assertEqual(dec.upper(), plaintext[i].upper())

    def test_encipher(self):
        # test odd length string
        keys = ('czbniwemuorkpdslqfxagthyv',
                'ohnuwkdbtiepyzxcsqamlgrvf',
                'pslqofaiymcnwtuhdxezbkgrv',
                'xqvlpnakrsewfcyhutdbgziom',
                'xbhpuvmiyesdnwlakcrgfzotq')
        plaintext =   'abcdefghiklmnopqrstuvwxyzABCDEFGHIKLMNOPQRSTUVWXY'
        ciphertext = ['finrmqtyzsfwiukfkryegoyniqnzkulhvbrqubmslkkvoyulny',
                      'qtskxlhdkdfcuhysgqztfuezavkqkplrwdeoqwhernadtuimze',
                      'fknhhybxagoiussokqucgueidmphxzibxfgsaupsyqqnzoxgie',
                      'sudowcxgvfporgxvsndtqfpeqwdyhceitgrvgsmllakbtqeqep',
                      'kxknvqcumcdechutawqpyspvfkhklmqaingdidthtgwfxespvp']
        for i,key in enumerate(keys):
            enc = Playfair(key).encipher(plaintext)
            self.assertEqual(enc.upper(), ciphertext[i].upper())
        # test even length string
        plaintext ='aaaaaaaaajjjjjkkkkkllllmmmmnnnnffffooooossssoffffffe'
        key = 'tpaydcmhfoizwsuvxrbkelqgn'
        ciphertext = 'prprprprtwzvzvvrvrxnplpzzlollkgombocmkmkzbzbcombmbcg'
        enc = Playfair(key).encipher(plaintext)
        self.assertEqual(enc.upper(), ciphertext.upper())
