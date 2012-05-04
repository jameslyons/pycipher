'''
implements bifid cipher
Author: James Lyons 
Created: 2012-04-28
'''
from .base import Cipher
from polybius import PolybiusSquare
####################################################################################
class Bifid(Cipher):
    def __init__(self,key='phqgmeaylnofdxkrcvszwbuti',period=5):
        self.key = [k.upper() for k in key]
        self.pb = PolybiusSquare(self.key,size=5)
        self.period = period
        assert len(key)==25, 'invalid key in init: must have length 25, has length '+str(len(key))
        assert period>=1, 'invalid period in init: period should be >= 1'

    def encipher(self,string):
        string = self.remove_punctuation(string)
        step1 = self.pb.encipher(string)
        evens = step1[::2]
        odds = step1[1::2]
        step2 = []
        for i in xrange(0,len(string),self.period):
            step2 += evens[i:i+self.period]
            step2 += odds[i:i+self.period]
        return self.pb.decipher(''.join(step2))

    def decipher(self,string):
        ret = ''
        string = string.upper()
        rowseq,colseq = [],[]
        # take blocks of length period, reform rowseq,colseq from them
        for i in range(0,len(string),self.period):
            tempseq = []
            for j in range(0,self.period):
                if i+j >= len(string): continue
                tempseq.append( self.key.index(string[i + j]) / 5 )
                tempseq.append( self.key.index(string[i + j]) % 5 )
            rowseq.extend(tempseq[0:len(tempseq)/2])
            colseq.extend(tempseq[len(tempseq)/2:])
        for i in xrange(len(rowseq)):
            ret += self.key[rowseq[i]*5 + colseq[i]]  
        return ret    

if __name__ == '__main__': 
    print 'use "import pycipher" to access functions'