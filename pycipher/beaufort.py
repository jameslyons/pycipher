'''
implements beaufort cipher
Author: James Lyons
Created: 2012-04-28
'''
from .base import Cipher
import re
####################################################################################
class Beaufort(Cipher):
    def __init__(self,key='fortification'):
        self.key = [k.upper() for k in key]
        
    def encipher(self,string):
        string = re.sub(r'[^A-Z]','',string.upper())
        ret = ''
        for (i,c) in enumerate(string):
            i = i%len(self.key)
            ret += self.i2a(ord(self.key[i])-ord(c))
        return ret    

    def decipher(self,string):
        return self.encipher(string)    

if __name__ == '__main__': 
    print 'use "import pycipher" to access functions'