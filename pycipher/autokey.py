'''
implements autokey cipher
Author: James Lyons
Created: 2012-04-28
'''
from .base import Cipher

####################################################################################
class Autokey(Cipher):
    def __init__(self,key='a'):
        self.key = [k.upper() for k in key]
        
    def encipher(self,string):
        string = self.remove_punctuation(string)
        ret = ''
        for (i,c) in enumerate(string):
            if i<len(self.key): offset = self.a2i(self.key[i])
            else: offset = self.a2i(string[i-len(self.key)])     
            ret += self.i2a(self.a2i(c)+offset)
        return ret    

    def decipher(self,string):
        string = self.remove_punctuation(string)
        ret = ''
        for (i,c) in enumerate(string):
            if i<len(self.key): offset = self.a2i(self.key[i])
            else: offset = self.a2i(ret[i-len(self.key)])             
            ret += self.i2a(self.a2i(c)-offset)
        return ret    

if __name__ == '__main__': 
    print 'use "import pycipher" to access functions'