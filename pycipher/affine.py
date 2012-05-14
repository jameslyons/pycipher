'''
implements affine substitution cipher
Author: James Lyons
Created: 2012-04-28
'''
from .base import Cipher

####################################################################################
class Affine(Cipher):
    def __init__(self,a=5,b=9):
        ''' 
        The Affine Cipher has two components to the key, numbers *a* and *b*.
        This cipher encrypts a letter according to the following equation:
            c = a*p + b
        where c is the ciphertext letter, p the plaintext letter.
        *b* is an integer 0-25, *a* is an integer that has an an inverse (mod 26).
        Allowable values for *a* are: 1,3,5,7,9,11,15,17,19,21,23,25 
        '''    
        self.a = a
        self.b = b
        self.inva = -1
        for i in range(1,26,2):
            if (self.a*i) % 26 == 1: self.inva = i
        assert 0 <= self.inva <= 25, 'invalid key: a='+str(a)+', no inverse exists (mod 26)'

    def encipher(self,string,keep_punct=False):
        '''
        enciphers *string* according to the initialised key. By default all punctuation and whitespace
        are removed, however it can be kept by setting *keep_punct*=True.
        Example:
        ciphertext = Affine(a,b).encipher(plaintext)       
        '''
        if not keep_punct: string = self.remove_punctuation(string)
        ret = ''
        for c in string:
            if c.isalpha(): ret += self.i2a(self.a*self.a2i(c) + self.b)
            else: ret += c
        return ret    

    def decipher(self,string,keep_punct=False):
        '''
        deciphers *string* according to the initialised key. By default all punctuation and whitespace
        are removed, however it can be kept by setting *keep_punct*=True.

        Performs the inverse operation to `encipher`, i.e. the original text is recovered if this function
        is used on the ciphertext when initialised with the same key.

        Example:
        plaintext = Affine(a,b).decipher(ciphertext)               
        '''    
        if not keep_punct: string = self.remove_punctuation(string)    
        ret = ''
        for c in string:
            if c.isalpha(): ret += self.i2a(self.inva*(self.a2i(c) - self.b))
            else: ret += c
        return ret
        
if __name__ == '__main__': 
    print 'use "import pycipher" to access functions'
