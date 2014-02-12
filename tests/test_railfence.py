from pycipher.railfence import Railfence
import unittest

class TestRailfence(unittest.TestCase):

    def test_encipher(self):
        keys = (3,6,7,8)
        plaintext = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        ciphertext = ('aeimquycgkoswbdfhjlnprtvxzbdfhjlnprtvxzcgkoswaeimquy',
                      'akueoybjltvdfnpxzcimswcgmqwdhnrxbhlrvegoqyaiksufpzjt',
                      'amykwblnxzjlvxckowaimuydjpvbhntzeiqucgosfhrtdfprgseq',
                      'aocqbnpbdprcmqaeosdlrzfnteksygmufjtxhlvzgiuwikwyhvjx')
        for i,key in enumerate(keys):
            enc = Railfence(key).encipher(plaintext)
            self.assertEqual(enc.upper(), ciphertext[i].upper())

    def test_decipher(self):
        keys = (3,6,7,8)
        ciphertext = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        plaintext = ('annobpoqcrpsdtquevrwfxsygztahbucidvejfwgkhxiljykmlzm',
                     'agrblvmcshbitdnwoeujckvfpxqgwldmxhrysiyneozjtzukapfq',
                     'afoxgowphypgbhqziqxrjaricjsbksytlctkdludmuzvnevmenwf',
                     'aelszgowphatmfbgnubiqxrjcvohcipwdksytlexqjdkryfmuzvn')
        for i,key in enumerate(keys):
            dec = Railfence(key).decipher(ciphertext)
            self.assertEqual(dec.upper(), plaintext[i].upper())
            	
if __name__ == '__main__':
    unittest.main()
