'''
implements autokey cipher
Author: James Lyons
Created: 2012-04-28
'''
from .base import Cipher
import re

####################################################################################
class Autokey(Cipher):
    def __init__(self,key='fortification'):
        self.key = [k.upper() for k in key]
        
    def subst(self,ch,key='ABCDEFGHIJKLMNOPQRSTUVWXYZ',offset=0):
        ''' substitute a single character according to the key '''
        index = (self.val(ch) + offset)%26
        return key[index]
        
    def encipher(self,string):
        string = re.sub(r'[^A-Z]','',string.upper())
        ret = ''
        for (i,c) in enumerate(string):
            if i<len(self.key): offset = self.a2i(self.key[i])
            else: offset = self.a2i(string[i-len(self.key)])     
            ret += self.i2a(self.a2i(c)+offset)
        return ret    

    def decipher(self,string):
        string = re.sub(r'[^A-Z]','',string.upper())
        ret = ''
        for (i,c) in enumerate(string):
            if i<len(self.key): offset = self.a2i(self.key[i])
            else: offset = self.a2i(ret[i-len(self.key)])             
            ret += self.i2a(self.a2i(c)-offset)
        return ret    

if __name__ == '__main__': 
    print 'use "import pycipher" to access functions'