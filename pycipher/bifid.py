'''
implements bifid cipher
Author: James Lyons 
Created: 2012-04-28
'''
from .base import Cipher
import re
####################################################################################
class Bifid(Cipher):
    def __init__(self,key='phqgmeaylnofdxkrcvszwbuti',period=5,combine='IJ'):
        self.key = [k.upper() for k in key]
        self.period = period
        self.combine = combine
        assert len(key)==25, 'invalid key in init: must have length 25, has length '+str(len(key))
        assert period>=1, 'invalid period in init: period should be >= 1'

    def encipher(self,string):
        ''' punctuation is removed with this cipher '''
        ret = ''
        rowseq,colseq = [],[]
        for ch in string.upper():
            if not ch.isalpha(): continue
            if ch in self.combine: ch = self.combine[0]
            rowseq.append(self.key.index(ch) / 5)
            colseq.append(self.key.index(ch) % 5)
        # rearrange row,col sequences based on period
        seq = []
        for i in xrange(0,len(string),self.period):
            seq += rowseq[i:i+self.period]
            seq += colseq[i:i+self.period]
        # take pairs of seq, run through polybius square        
        for i in xrange(0,len(seq),2):
            ret += self.key[seq[i]*5 + seq[i+1]]
        return ret

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