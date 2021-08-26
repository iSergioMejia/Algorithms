'''
Largest Homogeneus Subsequence (LHS) Algorithm
Divide & Conquer
 Sergio A. Mejía - 2020
Python script for the solution of the problem 
"Select the biggest prefix that is common amongst a set of words"

2 Innocent and 1 D&C variants
'''

'''
Innocent Variant
    Check all possible subsequences [i, j] that are homogeneous and save
    the largest size.
'''
def InnocentLHS(S):
    K = 0
    a = -1
    for i in range(len(S)):
        k = 1
        j = i + 1
        while j < len(S) and S[i] == S[j]:
            j += 1
            k += 1
        if k > K:
            K = k
            a = i
    return (a, K)

'''
Innocent Variant 2
    This variant is less efficient because the while is replaced by a for that
    always check until the array's end only counting if is the same.
'''
def MostInnocentLHS(S):
    K = 0
    a = -1
    for i in range(len(S)):
        fin = i
        k = 1
        for j in range(i+1,len(S)):
            if fin == i and S[j] == S[i]:
                k += 1
            else:
                fin = j
        if k > K:
            K = k
            a = fin
    return (a, K)

'''
Auxiliar function for the D&C variant that finds the size
of the LHS in an interval [l, h] that is strictly passing through m
'''
def FindCrossLHS(S, l, m, h):
    kl = 0
    i = m-1
    while i >= l and S[m] == S[i]:
        i -= 1 
        kl += 1
    a = i + 1
    kr = 0
    i = m + 1
    while i <= h and S[m] == S[i]:
        i += 1 
        kr += 1  
    return(a, kl + kr + 1)

'''
Divide & Conquer Variant
    The array is recursively divided in two sections, finding the LHS in each one
    of them. We also check for a LHS that is passing through this 2 sections
    using the auxiliary function. The longest length from this 3 options is returned,
    with the starting index of the sequence.
''' 
def FindLHS_Aux(S, l, h):
    if h <= l:
        return (l, 1)
    else:
        m = (l+h)//2
        (la, lk) = FindLHS_Aux(S, l, m)
        (ra, rk) = FindLHS_Aux(S, m + 1, h)
        (ca, ck) = FindCrossLHS(S, l, m, h)
        if lk >= rk and lk >= ck:
            return(la, lk)
        elif rk > lk and rk > ck:
            return(ra, rk)
        else:
            return(ca, ck)

'''
Interface function for the D&C variant. The functions returns a pair (a, K) 
such that the LHS is in S[a:a+K]
'''
def FindLHS(S):
    return FindLHS_Aux(S, 0, len(S) - 1)

import random, sys, time

'''
if len(sys.argv) == 1:
    exit()
S = []
for i in range(int(sys.argv[ 1 ])):
    s = random.randint(97,99)
    S.append(chr(s))
print(S)
'''

S = ['a', 'a', 'a', 'b', 'b', 'a', 'b', 'b', 'b', 'c']
(a, K) = InnocentLHS(S)
print(S[a:a+K], ": from", a, "by", K)
(a, K) = FindLHS(S)
print(S[a:a+K], ": from", a, "by", K)


'''
# Time comparison of the algorithms. The output can be redirected to data.res
# and then printGraph.gnuplot can be used
S = []
i = 0
aI = -1
kI = -1
aF = -1
kF = -1
tries = 1000
while i < tries:
    S = []
    for j in range(i):
        #s = random.randint(97,99)
        S.append(chr(97))
    mTimeStart = time.process_time()
    #(aI, kI) = MostInnocentLHS(S)
    mTime = time.process_time() - mTimeStart
    iTimeStart = time.process_time()
    (aI, kI) = InnocentLHS(S)
    iTime = time.process_time() - iTimeStart
    fTimeStart = time.process_time()
    (aF, kF) = FindLHS(S)
    fTime = time.process_time() - fTimeStart
    i += 10
    print("%d %f %f %f"%(i,mTime, iTime, fTime))
'''