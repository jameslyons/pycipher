'''
implements Foursquare cipher
Author: James Lyons
Created: 2012-04-28
'''
from .base import Cipher
import re

####################################################################################
class Foursquare(Cipher):
    def __init__(self,key1='zgptfoihmuwdrcnykeqaxvsbl',key2='mfnbdcrhsaxyogvituewlqzkp'):
        self.key1 = [k.upper() for k in key1]
        self.key2 = [k.upper() for k in key2]
        self.alph = 'ABCDEFGHIKLMNOPQRSTUVWXYZ' # no letter j
        assert len(self.key1)==25, 'key1 is not length 25'
        assert len(self.key2)==25, 'key2 is not length 25'
        
    def encipher_pair(self,a,b):
        arow,acol = self.alph.index(a)/5, self.alph.index(a)%5
        brow,bcol = self.alph.index(b)/5, self.alph.index(b)%5
        return (self.key1[arow*5+bcol], self.key2[brow*5+acol])
        
    def decipher_pair(self,a,b):
        arow,acol = self.key1.index(a)/5, self.key1.index(a)%5
        brow,bcol = self.key2.index(b)/5, self.key2.index(b)%5
        return (self.alph[arow*5+bcol], self.alph[brow*5+acol])
        
    def encipher(self,string):
        string = re.sub(r'[^A-Z]','',string.upper())
        if len(string)%2 == 1: string = string + 'X'
        ret = ''
        for c in xrange(0,len(string.upper()),2):
            a,b = self.encipher_pair(string[c],string[c+1])
            ret += a + b
        return ret    

    def decipher(self,string):
        string = re.sub(r'[^A-Z]','',string.upper())
        if len(string)%2 == 1: string = string + 'X'
        ret = ''
        for c in xrange(0,len(string.upper()),2):
            a,b = self.decipher_pair(string[c],string[c+1])
            ret += a + b
        return ret    
        
if __name__ == '__main__': 
    print 'use "import pycipher" to access functions'