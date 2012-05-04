'''
implements gronsfeld cipher
Author: James Lyons
Created: 2012-04-28
'''
from .base import Cipher

####################################################################################
class Gronsfeld(Cipher):
    def __init__(self,key=[5, 14, 17, 19, 8, 5, 8, 2, 0, 19, 8, 14, 13]):
        self.key = key

    def encipher(self,string):
        string = self.remove_punctuation(string)  
        ret = ''
        for (i,c) in enumerate(string):
            i = i%len(self.key)
            ret += self.i2a(self.a2i(c) + self.key[i])
        return ret 

    def decipher(self,string):
        string = self.remove_punctuation(string)  
        ret = ''
        for (i,c) in enumerate(string):
            i = i%len(self.key)
            ret += self.i2a(self.a2i(c) - self.key[i])
        return ret         


if __name__ == '__main__': 
    print 'use "import pycipher" to access functions'