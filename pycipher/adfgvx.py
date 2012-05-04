'''
implements ADFGVX cipher
Author: James Lyons
Created: 2012-04-28
'''
from .base import Cipher
from columnartransposition import ColTrans
from polybius import PolybiusSquare

####################################################################################
class ADFGVX(Cipher):
    def __init__(self,key='ph0qg64mea1yl2nofdxkr3cvs5zw7bj9uti8',keyword='GERMAN'):
        self.key = [k.upper() for k in key]
        self.keyword = keyword
        assert len(key)==36, 'invalid key in init: must have length 36, has length '+str(len(key))
        assert len(keyword)>0, 'invalid keyword in init: should have length >= 1'
       
    def encipher(self,string):
        step1 = PolybiusSquare(self.key,size=6,chars='ADFGVX').encipher(string)
        step2 = ColTrans(self.keyword).encipher(step1)
        return step2

    def decipher(self,string):
        step2 = ColTrans(self.keyword).decipher(string)
        step1 = PolybiusSquare(self.key,size=6,chars='ADFGVX').decipher(step2)
        return step1    

if __name__ == '__main__': 
    print 'use "import pycipher" to access functions'