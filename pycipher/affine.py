'''
implements affine substitution cipher
Author: James Lyons
Created: 2012-04-28
'''
from .base import Cipher

####################################################################################
class AffineSubstitution(Cipher):
    def __init__(self,a=5,b=9):
        self.a = a
        self.b = b
        self.inva = -1
        for i in range(1,26,2):
            if (self.a*i) % 26 == 1: self.inva = i
        assert 0 <= self.inva <= 25, 'invalid key: a='+str(a)+', no inverse exists (mod 26)'

    def encipher(self,string,keep_punct=False):
        if not keep_punct: string = self.remove_punctuation(string)
        ret = ''
        for c in string:
            if c.isalpha(): ret += self.i2a(self.a*self.a2i(c) + self.b)
            else: ret += c
        return ret    

    def decipher(self,string,keep_punct=False):
        if not keep_punct: string = self.remove_punctuation(string)    
        ret = ''
        for c in string:
            if c.isalpha(): ret += self.i2a(self.inva*(self.a2i(c) - self.b))
            else: ret += c
        return ret
        
if __name__ == '__main__': 
    print 'use "import pycipher" to access functions'
