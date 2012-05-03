from pycipher.simplesubstitution import SimpleSubstitution
import unittest

class TestSimple(unittest.TestCase):

    def test_encipher(self):
        keys = ('abronjdfuetchiszlgwqvxkymp',
                'mufykewgqtnrlopcbadsvxzijh',
                'rtuzesbxjaniypqclghmvwodkf',
                'ymdsvtxizewurqfnbgjlckoahp',
                'lcvmwezojbgdtsrniufyqphxak')
        plaintext = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        ciphertext = ('abronjdfuetchiszlgwqvxkympabronjdfuetchiszlgwqvxkymp',
                      'mufykewgqtnrlopcbadsvxzijhmufykewgqtnrlopcbadsvxzijh',
                      'rtuzesbxjaniypqclghmvwodkfrtuzesbxjaniypqclghmvwodkf',
                      'ymdsvtxizewurqfnbgjlckoahpymdsvtxizewurqfnbgjlckoahp',
                      'lcvmwezojbgdtsrniufyqphxaklcvmwezojbgdtsrniufyqphxak')
        for i,key in enumerate(keys):
            enc = SimpleSubstitution(key).encipher(plaintext)
            self.assertEqual(enc.upper(), ciphertext[i].upper())

    def test_decipher(self):
        keys = ('zidvgmlefwpsktrnaoqjyubhxc',
                'wyqtnaopsxigdbzlhumvckrejf',
                'bqcjpkfeuzlnxmgdastwhriyvo',
                'enwdirhmykbfzsaojulpcqtvxg',
                'rtzeawivnubkyjfchsldomqxpg')
        ciphertext = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        plaintext = ('qwzchiexbtmgfprksolnvdjyuaqwzchiexbtmgfprksolnvdjyua',
                     'fnumxzlqkyvpseghcwidrtajbofnumxzlqkyvpseghcwidrtajbo',
                     'qacphgouwdfknlzebvrsiytmxjqacphgouwdfknlzebvrsiytmxj',
                     'okudalzgeqjshbptvfnwrxcyimokudalzgeqjshbptvfnwrxcyim',
                     'ekptdozqgnlsviuywarbjhfxmcekptdozqgnlsviuywarbjhfxmc')
        for i,key in enumerate(keys):
            dec = SimpleSubstitution(key).decipher(ciphertext)
            self.assertEqual(dec.upper(), plaintext[i].upper())
            	
if __name__ == '__main__':
    unittest.main()
