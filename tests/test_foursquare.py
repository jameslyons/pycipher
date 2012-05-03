from pycipher import Foursquare
import unittest

class TestFoursquare(unittest.TestCase):

    def test_encipher(self):
        keys = (('zgptfoihmuwdrcnykeqaxvsbl','mfnbdcrhsaxyogvituewlqzkp'),
                ('iebvsurpxanmqoywdlztfkcgh','fobgqehdpwrviknazytmsculx'))
        plaintext = ('abcdefghiiklmnopqrstuvwxyzabcdefghiiklmnopqrstuvwxyz',
                     'abcdefghiiklmnopqrstuvwxyzabcdefghiiklmnopqrstuvwxyz')
        ciphertext = ('gmtnzahrmsovryngkiquypsqlkgmtnzahrmsovryngkiquypsqlk',
                      'efvbiwphxpunqvykdazywxcchlefvbiwphxpunqvykdazywxcchl')
        for i,key in enumerate(keys):
            enc = Foursquare(*key).encipher(plaintext[i])
            self.assertEqual(enc.upper(), ciphertext[i].upper())

    def test_decipher(self):
        keys = (('zgptfoihmuwdrcnykeqaxvsbl','mfnbdcrhsaxyogvituewlqzkp'),
                ('iebvsurpxanmqoywdlztfkcgh','fobgqehdpwrviknazytmsculx'))
        plaintext= ('abcdefghiiklmnopqrstuvwxyzabcdefghiiklmnopqrstuvwxyz',
                     'abcdefghiiklmnopqrstuvwxyzabcdefghiiklmnopqrstuvwxyz')
        ciphertext = ('gmtnzahrmsovryngkiquypsqlkgmtnzahrmsovryngkiquypsqlk',
                      'efvbiwphxpunqvykdazywxcchlefvbiwphxpunqvykdazywxcchl')
        for i,key in enumerate(keys):
            dec = Foursquare(*key).decipher(ciphertext[i])
            self.assertEqual(dec.upper(), plaintext[i].upper())
            	
if __name__ == '__main__':
    unittest.main()
