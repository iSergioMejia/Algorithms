import random

def InnocentSearch(S, e):
    i = 0
    while i < len(S) and e != S[i]:
        i += 1
    if i == len(S):
        return -1
    else:
        return i

def Partition(S, p, r):
    x = S[r]
    i = p - 1
    for j in range(p, r):
        if S[j] <= x:
            i += 1
            (S[i], S[j]) = (S[j], S[i])
    (S[i+1], S[r]) = (S[r], S[i+1])
    return (i+1)

def RandomizedPartition(S, p, r):
    random.seed(None)
    i = random.randint(p, r+1)
    (S[r], S[i]) = (S[i], S[r])
    return Partition(S, p, r)

def QuickSearch_Aux(S, p, r, e):
    if len(S) == 0:
        return -1
    if p < r:
        q = random.randint(p, r) #RandomizedPartition(S, p, r)
        #print(("(%d,%d,%d)"%(p,q,r)))
        if S[q] == e:
            return q
        lv = QuickSearch_Aux(S, p, q - 1, e)
        if lv != -1:
            return lv
        rv = QuickSearch_Aux(S, q + 1, r, e)
        return rv
    else:
        if p >= 0 and S[p] == e:
            return p
        else:
            return -1

def QuickSearch(S, e):
    return QuickSearch_Aux(S, 0, len(S)-1, e)

import sys, time

n = 0
while n < 10000:
    S = [i for i in range(n)]
    #random.shuffle(S)
    e = n-1
    inStartTime = time.process_time()
    ins = (InnocentSearch(S,e))
    inTime = time.process_time() - inStartTime
    qsStartTime = time.process_time()
    qs = (QuickSearch(S, e))
    qsTime = time.process_time() - qsStartTime
    val = 0
    #print(ins, qs)
    if ins == qs:
        val = 1
    print(n,inTime,qsTime,val)
    n += 100