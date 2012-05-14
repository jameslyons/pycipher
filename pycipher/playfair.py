'''
implements Playfair cipher
Author: James Lyons
Created: 2012-04-28
'''
from .base import Cipher
import re

####################################################################################
class Playfair(Cipher):
    '''
    Create a Playfair cipher object with a certain key. This object allows enciphering and deciphering
    of text.
    '''
    def __init__(self,key='monarchybdefgiklpqstuvwxz'):
        self.key = [k.upper() for k in key]
        
    def encipher_pair(self,a,b):
        if a == b: b = 'X'
        arow,acol = self.key.index(a)/5 , self.key.index(a)%5
        brow,bcol = self.key.index(b)/5 , self.key.index(b)%5
        if arow == brow: return (self.key[arow*5+(acol+1)%5] + self.key[brow*5+(bcol+1)%5])
        elif acol == bcol: return (self.key[((arow+1)%5)*5+acol] + self.key[((brow+1)%5)*5+bcol])
        else: return (self.key[arow*5 + bcol] + self.key[brow*5 + acol])
        
    def decipher_pair(self,a,b):
        assert a != b, 'two of the same letters occured together, illegal in playfair'
        arow,acol = self.key.index(a)/5 , self.key.index(a)%5
        brow,bcol = self.key.index(b)/5 , self.key.index(b)%5
        if arow == brow: return (self.key[arow*5+(acol-1)%5] + self.key[brow*5+(bcol-1)%5])
        elif acol == bcol: return (self.key[((arow-1)%5)*5+acol] + self.key[((brow-1)%5)*5+bcol])
        else: return self.key[arow*5 + bcol] + self.key[brow*5 + acol]        
        
    def encipher(self,string):
        '''
        Encipher a string *string* using the Playfair cipher. All punctuation and spaces are removed from the string.
        If the string has an odd number of characters, a pad character is appended. All 'J' characters are replaced with 'I'.
        '''
        string = self.remove_punctuation(string)  
        string = re.sub(r'[J]','I',string)
        if len(string)%2 == 1: string = string + 'X'
        ret = ''
        for c in xrange(0,len(string),2):
            ret += self.encipher_pair(string[c],string[c+1])
        return ret    

    def decipher(self,string):
        '''
        Decipher a string *string* using the Playfair cipher. All punctuation and spaces are removed from the string.
        If the string has an odd number of characters, a pad character is appended. An error will be raised
        if a character is encountered that is not in the key.
        '''    
        string = self.remove_punctuation(string)  
        if len(string)%2 == 1: string = string + 'X'
        ret = ''
        for c in xrange(0,len(string),2):
            ret += self.decipher_pair(string[c],string[c+1])
        return ret    
        
    def pad_doubles(string):
        ''' There are two ways of handling double letters in playfair, 
        method 1: replacing the second occurrance with a pad character 
                  e.g. 'THEATTACK'->'THEATXACK'
        method 2: putting a pad character between the pair
                  e.g. 'THEATTACK'->'THEATXTACK'.
        This function implements method 2. It returns a modified string, possibly of different
        length to the original.
        '''
        c=0
        L = len(string)
        while c < L-1:
            if string[c] == string[c+1]:
                string = string[:c]+string[c]+'X'+string[c+1:]
            L = len(string)
            c += 2
        return string            
        
if __name__ == '__main__': 
    print 'use "import pycipher" to access functions'
