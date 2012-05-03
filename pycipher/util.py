'''
some statistics routines for cryptanalysis
'''
import math
import re

def ic(ctext):
    ''' takes ciphertext, calculates index of coincidence.'''
    counts = ngram_count(ctext,N=1)
    icval = 0
    for k in counts.keys():
        icval += counts[k]*(counts[k]-1)
    icval /= (len(ctext)*(len(ctext)-1))
    return icval
    
def chi_sq_en(ctext):
    ''' takes a piece of ciphertext. Calculates Chi-squared statistic vs. expected english'''
    P = ngram_count(ctext,N=1)
    Q = expected_en_count(len(ctext))    
    csval = 0
    for i in Q.keys():
        if i in P:
            csval += (P[i] - Q[i])**2 / Q[i]
        else:
            csval += Q[i]
    return csval

def chi_sq(P,Q):
    ''' takes two dicts of counts. Calculates Chi-squared statistic '''
    csval = 0
    for i in Q.keys():
        if i in P:
            csval += (P[i] - Q[i])**2 / Q[i]
        else:
            csval += Q[i]
    return csval

def expected_en_count(N):
    ''' Given a length N, how many of each letter would we expect to count if the text was english.
        Returns a dict. '''
    count = {}
    for i,c in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
        count[c] = N*enfreq[i]
    return count
    
def ngram_count(text,N=1,nopunc=True):
    ''' if N=1, return a dict containing each letter along with how many times the letter occurred.
        if N=2, returns a dict containing counts of each bigram (pair of letters)
        etc.
        There is an option to remove all spaces and punctuation prior to processing '''
    if nopunc: text = re.sub('[^A-Z]','',text.upper())
    count = {}
    for i in xrange(len(text)-N+1):
        c = text[i:i+N]
        if c in count: count[c] += 1
        else: count[c] = 1.0
    return count
    
def ngram_freq(text,N=1,log=False,floor=0.01):
    ''' returns the n-gram frequencies of all n-grams encountered in text.
        Option to return log probabilities or standard probabilities.
        Note that only n-grams occurring in 'text' will have probabilities.
        For the probability of not-occurring n-grams, use freq['floor'].
        This is set to floor/len(text) '''
    freq = ngram_count(text,N)
    L = 1.0*(len(text)-N+1)
    for c in freq.keys():
        if log: freq[c] = math.log10(freq[c]/L)
        else: freq[c] = freq[c]/L
    if log: freq['floor'] = math.log10(floor/L)
    else: freq['floor'] = floor/L   
    return freq
