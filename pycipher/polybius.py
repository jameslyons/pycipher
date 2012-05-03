'''
implements polybius square cipher
Author: James Lyons
Created: 2012-04-28
'''
from .base import Cipher
import re

####################################################################################
class PolybiusSquare(Cipher):
    def __init__(self,key='phqgiumeaylnofdxkrcvstzwb',size=5,chars=None):
        self.key = ''.join([k.upper() for k in key])
        self.chars = chars or 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'[:size]
        self.size = size
        assert len(self.key)==size*size, 'invalid key in init: must have length size*size, has length '+str(len(key))
        assert len(self.chars)==size, 'invalid chars in init: must have length=size, has length '+str(len(chars))

    def encipher_char(self,ch):
        row = self.key.index(ch) / self.size
        col = self.key.index(ch) % self.size
        return self.chars[row]+self.chars[col]
    
    def decipher_pair(self,pair):
        row = self.chars.index(pair[0])
        col = self.chars.index(pair[1])
        return self.key[row*self.size + col]

    def encipher(self,string):
        ''' punctuation is removed with this cipher '''
        string = re.sub('[^'+self.key+']','',string.upper())
        ret = ''
        for c in string:
            if c.isalpha(): ret += self.encipher_char(c)
        return ret    

    def decipher(self,string):
        ret = ''
        for i in xrange(0,len(string),2):
            ret += self.decipher_pair(string[i:i+2])
        return ret    

if __name__ == '__main__': 
    print 'use "import pycipher" to access functions'