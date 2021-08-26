'''
Largest Increasing Subsquence Algorithm
Dynamic Programming
 Sergio A. Mejía - 2020
Python script for the solution of the problem 
"Given a sequence, find the largest subsequence (non continous) where its order is
strictly increasing"

Recursive, Memoized, Bottom Up (with Backtracking) variants
'''

import math

'''
Recursive Variant
Starting from the back, find the next number that is less than the current one and
  recursively find the best result between considering this number or not considering
  it and moving just to the next one.
'''
def LIS_Aux(S, i):
    if i == 0:
        return 0
    j = i - 1
    while j > 0 and S[j - 1] >= S[i - 1]:
        j -= 1
    return max(LIS_Aux(S, i - 1), LIS_Aux(S, j) + 1)

'''
Memoized variant:
  Same as recursive, but the partial solutions are stored in M, so if this
  solution has been already calculated, the value of M is returned, instead of
  calculating it again.
'''
def LIS_Memo(S, i, M):
    if M[i] == -math.inf:
        if i == 0:
            M[i] = 0
        else:
            j = i
            while j > 0 and S[j] >= S[i]:
                j -= 1
            left = LIS_Memo(S, i - 1, M)
            right = LIS_Memo(S, j, M) + 1
            if left < right:
                M[i] = right
            else:
                M[i] = left
    return M[i]

'''
Bottom Up (with Backtracking) variant:
  Calculate all of the partial solutions and saving in a B vector
  the index of the chosen solution in order to backtrack the solution.
'''
def LIS_BottomUp(S, n, M):
    B = [ -1 for i in range(n + 1) ]
    M[0] = 0
    for i in range(1, n + 1):
        j = i - 1
        while j > 0 and S[j - 1] >= S[i - 1]:
            j -= 1
        left = M[i - 1]
        right = M[j] + 1
        if left <= right:
            M[i] = right
            B[i] = j
        else:
            M[i] = left
            B[i] = -1
    T = []
    j = n
    print(B)
    while j > 0 and B[j] == -1:
        j -= 1
    b = B[ j ]
    T.append( S[j - 1] )
    while b != 0:
        if B[b] == -1:
            b -= 1
        T.append(S[b - 1])
        b = B[b]
    # T.append(S[b])
    T.reverse()
    return [M[j], T]

def LIS(S):
    M = [ -math.inf for i in range(len(S)+1)]

    n = LIS_BottomUp(S, len(S), M)
    # n = LIS_Aux(S, len(S))
    return n

S = [5, 2, 8, 6, 3, 6, 9, 7, 3]
# S = [1, 2, 3, 4, 5 ,6, 7]
print(LIS(S))