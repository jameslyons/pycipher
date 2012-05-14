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
    enfreq = (0.081175175864, 0.014349030017, 0.0243448791891, 0.0454671319963, 0.124190588544, 
              0.0217233036221, 0.0199365360248, 0.0640450910998, 0.0694062131341, 0.000991556342028, 
              0.00784206099532, 0.0394271311225, 0.0241520841526, 0.071597140298, 0.07666988902, 
              0.0178952571329, 0.000934755538078, 0.0578677305894, 0.063886158081, 0.0911043933237, 
              0.0271690807008, 0.0102552759208, 0.0238071831171, 0.00159834185345, 0.0193089963735, 
              0.000855015947918)
    count = {}
    for i,c in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
        count[c] = N*enfreq[i]
    return count
    
def ngram_count(text,N=1,keep_punct=False):
    ''' if N=1, return a dict containing each letter along with how many times the letter occurred.
        if N=2, returns a dict containing counts of each bigram (pair of letters)
        etc.
        There is an option to remove all spaces and punctuation prior to processing '''
    if not keep_punct: text = re.sub('[^A-Z]','',text.upper())
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

def restore_punctuation(original,modified):
    ''' If punctuation was accidently removed, use this function to restore it.
        requires the orignial string with punctuation. '''
    ret = ''
    count = 0
    try:
        for c in original:
            if c.isalpha(): 
                ret+=modified[count]
                count+=1
            else: ret+=c
    except IndexError:
        print 'restore_punctuation: strings must have same number of alphabetic chars'
        raise
    return ret
    
from itertools import permutations
    
def markov_freq(text,order=1,log=False,floor=0.01):
    if order == 0: return ngram_freq(text,1,log,floor)
    freq = ngram_count(text,order+1)
    prior_count = {}
    for k in freq.keys():            
        prior = k[:order]
        if prior in prior_count: prior_count[prior] += freq[k]
        else: prior_count[prior] = freq[k]
    for k in freq.keys():            
        prior = k[:order]
        freq[prior] = True # put the priors in the db too, we need to know which ones are there
        if log:
            freq[k] = math.log10(freq[k]/prior_count[prior])
        else:
            freq[k] = freq[k]/prior_count[prior]
        freq['floor'] = math.log10(floor)
      
    return freq    


def keyword_to_key(word,alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
    ''' convert a key word to a key by appending on the other letters of the alphabet.
    e.g. MONARCHY -> MONARCHYBDEFGIJKLPQSTUVWXZ
    '''
    ret = ''
    word = (word + alphabet).upper()
    for i in word:
        if i in ret: continue
        ret += i
    return ret    
