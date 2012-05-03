'''
implements Caesar substitution cipher
Author: James Lyons 
Created: 2012-04-28
'''

from .base import Cipher

class Caesar(Cipher):
    def __init__(self,key=13):
        ''' key is an integer 0-25 used to encipher characters '''
        self.key = key % 26

    def encipher(self,string):
        ret = ''
        for c in string.upper():
            if c.isalpha(): ret += self.i2a( self.a2i(c) + self.key )
            else: ret += c
        return ret    

    def decipher(self,string):
        ret = ''
        for c in string.upper():
            if c.isalpha(): ret += self.i2a( self.a2i(c) - self.key )
            else: ret += c
        return ret
                
if __name__ == '__main__': 
    print 'use "import pycipher" to access functions'
