'''
Largest Common Prefix (LCP) Algorithm
Divide & Conquer
 Sergio A. Mejía - 2020
Python script for the solution of the problem 
"Select the biggest prefix that is common amongst a set of words"

Innocent and D&C variants
'''

'''
Innocent Variant:
    Get the first word as the largest prefix and then for each word check until
    a different letter between the current largest prefix and the current analyzed
    word is found. The new largest prefix will be the current largest prefix until
    that different letter. 
'''
def InnocentLCP(S):
    if len(S) == 0:
        return ""
    prefixMax = S[0]
    for word in S:
        i = 0
        j = 0
        while i < len(prefixMax) and j < len(word) and prefixMax[i] == word[j]:
            i += 1
            j += 1
        prefixMax = prefixMax[0:i]
    return prefixMax

'''
Auxiliar function for the D&C function.
    This function finds the largest common prefix between just 2 words.
'''
def Prefix2(a, b):
    i = 0
    j = 0
    while i < len(a) and j < len(b) and a[i] == b[j]:
        i += 1
        j += 1
    if i != 0:
        return a[0:i]
    else:
        return ""

'''
Divide & Conquer variant
    The array is recursively divided in two sections finding the largest common
    prefix in each of those sections. Then, the largest common prefix is found
    between the largest common prefixes of those two sections. The base case is
    when the section is just 1 word long, in which the largest prefix is the word itself.
'''
def LCP_Aux(S, b, e):
    if len(S) == 0:
        return ""
    if b >= e:
        return S[b]
    else:
        q = (b+e)//2
        lv = LCP_Aux(S, b, q)
        rv = LCP_Aux(S, q+1, e)
        r = Prefix2(lv, rv)
        return r

'''
Interface function for the D&C call
'''
def LCP(S):
    return LCP_Aux(S, 0, len(S)-1)

import time

S = ["alpaca", "alcalde", "alpiste"]
print(InnocentLCP(S))

'''
# Time calculation for input of increasing size
s = "alpaca"
for i in range(0,10000,10):
    S = [s]*i
    tS = time.process_time()
    r = LCP(S)
    tSf = time.process_time() - tS
    tI = time.process_time()
    ri = InnocentLCP(S)
    tSi = time.process_time() - tI
    print(i,r, ri, tSf,tSi)
'''
