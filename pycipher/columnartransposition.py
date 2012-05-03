'''
implements Columnar transposition cipher
Author: James Lyons 
Created: 2012-04-28
'''
from .base import Cipher
from math import ceil

####################################################################################
class ColTrans(Cipher):
    def __init__(self,keyword='GERMAN'):
        self.keyword = keyword.upper()
        assert len(keyword)>0, 'invalid keyword in init: should be >= 1'

    def sortind(self,word):
        ''' return the sorted indices of a word e.g. 'german' = [2,1,5,3,0,4] '''
        t1 = [(word[i],i) for i in xrange(len(word))]
        t2 = [(k[1],i) for i,k in enumerate(sorted(t1))]
        return [q[1] for q in sorted(t2)]
        
    def unsortind(self,word):
        ''' return the unsorted indices of a word '''
        t1 = [(word[i],i) for i in xrange(len(word))]
        return [q[1] for q in sorted(t1)]        
        
    def encipher(self,string):
        ret = ''
        ind = self.sortind(self.keyword)
        for i in range(len(self.keyword)):
            ret += string[ind.index(i)::len(self.keyword)]
        return ret

    def decipher(self,string):
        ''' deciphering is messy because the columns may be ragged '''
        ret = ['_']*len(string)
        L,M = len(string),len(self.keyword)
        ind = self.unsortind(self.keyword)
        upto = 0
        for i in range(len(self.keyword)):
            thiscollen = L/M
            if ind[i]< L%M: thiscollen += 1
            ret[ind[i]::M] = string[upto:upto+thiscollen]
            upto += thiscollen
        return ''.join(ret)    

if __name__ == '__main__': 
    print 'use "import pycipher" to access functions'