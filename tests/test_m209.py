from pycipher.m209 import M209
import unittest

class TestM209(unittest.TestCase):

    def test_encipher(self):
        text = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        enclist = ['TMHRSVOJLBSOYAGEYCJJCFVPKPJGWQHRJHIEBXWHINKNLGSZLRBN',
                   'CIRLWCGMGBMBCNLEMVGPWTSTPPEVWUZFOBACQBDCFSTVYJEFOTSN']
        keys = ['AAAAAA','ZSMJDE']                
        for i,key in enumerate(keys):
            enc = M209(key).encipher(text)
            self.assertEqual(enc.upper(), enclist[i].upper()) 
	
if __name__ == '__main__':
    unittest.main()
